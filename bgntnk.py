import os
import sys
import json
import time
import hashlib
import argparse
from datetime import datetime

import requests 

CONFIG = {
    "name": "Flash sms",
    "api_url": os.environ.get("FLASH_API_URL", "https://flash-sms-delta.vercel.app/api/cdr/viewstats"),
    "api_token": os.environ.get("FLASH_API_TOKEN", ""),       
    "records_per_fetch": 50,
    "timeout": 15,
}

TELEGRAM = {
    "bot_token": os.environ.get("TELEGRAM_BOT_TOKEN", "8635536355:AAHJs6WWIYk69b40WCSVR8f984hpiqOyh80"),    # <-- توكن البوت من BotFather
    "chat_id":   os.environ.get("TELEGRAM_CHAT_ID", "-1003947736633"),      # <-- آي دي الجروب
}

POLL_INTERVAL_SECONDS = int(os.environ.get("POLL_INTERVAL_SECONDS", "20"))
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flash_sms_forwarder_state.json")

HEADERS = {"User-Agent": "FlashSMS-Forwarder/1.0"}


# ─────────────────────────────── STATE (anti-duplicate) ────────────────────

def load_seen_ids():
    """
    """
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()


def save_seen_ids(seen_ids):
    # Keep the file from growing forever — last 5000 IDs is more than enough.
    trimmed = list(seen_ids)[-5000:]
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(trimmed, f)
    except Exception as e:
        print(f"⚠️  Couldn't save state file: {e}")


def make_id(row):
    """Stable unique id for a CDR row, used to detect duplicates."""
    raw = f"{row.get('number')}|{row.get('date')}|{row.get('message')}|{row.get('cli')}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


# ─────────────────────────────── FETCH FROM FLASH SMS API ──────────────────

def fetch_flash_codes():
    """
    """
    if not CONFIG["api_token"]:
        return [], "FLASH_API_TOKEN غير موجود — املأه في الإعدادات فوق."

    try:
        r = requests.get(
            CONFIG["api_url"],
            headers={**HEADERS, "X-API-Token": CONFIG["api_token"]},
            params={"records": CONFIG["records_per_fetch"]},
            timeout=CONFIG["timeout"],
        )
    except requests.RequestException as e:
        return [], f"تعذر الاتصال بالبانل: {e}"

    if r.status_code == 401:
        return [], "توكن غير صحيح (401) — تأكد من FLASH_API_TOKEN."
    if r.status_code != 200:
        return [], f"البانل رجّع كود غير متوقع: {r.status_code}"

    try:
        data = r.json()
    except ValueError:
        return [], "الرد مش JSON صحيح."

    if not data.get("success"):
        return [], data.get("error", "success=false من البانل.")

    return data.get("results", []), "ok"


# ─────────────────────────────── TELEGRAM ───────────────────────────────────

def telegram_selftest():
    """
    """
    if not TELEGRAM["bot_token"] or not TELEGRAM["chat_id"]:
        return False, "TELEGRAM_BOT_TOKEN أو TELEGRAM_CHAT_ID غير موجودين."
    try:
        r = requests.get(
            f"https://api.telegram.org/bot{TELEGRAM['bot_token']}/getMe", timeout=10
        )
        if not r.ok or not r.json().get("ok"):
            return False, "توكن البوت غير صحيح."
    except requests.RequestException as e:
        return False, f"تعذر الوصول لتليجرام: {e}"
    return True, "ok"


def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM['bot_token']}/sendMessage"
    payload = {
        "chat_id": TELEGRAM["chat_id"],
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True,
    }
    try:
        r = requests.post(url, data=payload, timeout=15)
        if r.status_code == 200 and r.json().get("ok"):
            return True, "ok"
        return False, f"Telegram API error: {r.text[:200]}"
    except requests.RequestException as e:
        return False, str(e)


def format_message(row):
    number = row.get("number") or "—"
    message = (row.get("message") or "").strip()
    date = row.get("date") or "—"
    country = row.get("country") or "—"
    operator = row.get("operator") or "—"
    cli = row.get("cli") or "—"
    return (
        f"📩 <b>New Code — {CONFIG['name']}</b>\n"
        f"📱 Number: <code>{number}</code>\n"
        f"🌍 {country} / {operator}\n"
        f"📨 From: {cli}\n"
        f"🕒 {date}\n"
        f"💬 <code>{message}</code>"
    )


# ─────────────────────────────── MAIN CYCLE ─────────────────────────────────

def run_cycle(seen_ids):
    rows, status = fetch_flash_codes()
    if status != "ok":
        print(f"❌ Fetch failed: {status}")
        return seen_ids, {"fetched": 0, "sent": 0, "duplicate": 0, "failed": 0}

    stats = {"fetched": len(rows), "sent": 0, "duplicate": 0, "failed": 0}

    # Oldest first, so the group receives them in the right order.
    for row in reversed(rows):
        rid = make_id(row)
        if rid in seen_ids:
            stats["duplicate"] += 1
            continue

        ok, err = send_to_telegram(format_message(row))
        if ok:
            seen_ids.add(rid)
            stats["sent"] += 1
            time.sleep(0.4)  # stay well under Telegram's rate limit
        else:
            stats["failed"] += 1
            print(f"⚠️  Failed to send {row.get('number')}: {err}")

    if stats["sent"]:
        save_seen_ids(seen_ids)

    return seen_ids, stats


def main():
    parser = argparse.ArgumentParser(description="Flash SMS -> Telegram code forwarder")
    parser.add_argument("--once", action="store_true", help="Run a single cycle then exit (good for cron)")
    args = parser.parse_args()

    print("── Flash SMS Telegram Forwarder ──────────────────────────────")

    # Self-test before doing anything else, so misconfiguration is obvious.
    ok_tg, msg_tg = telegram_selftest()
    print(f"{'✅' if ok_tg else '❌'} Telegram bot: {msg_tg}")

    if not CONFIG["api_token"]:
        print("❌ Flash SMS API: FLASH_API_TOKEN غير موجود.")
    else:
        print(f"✅ Flash SMS API: token set, target = {CONFIG['api_url']}")

    if not ok_tg or not CONFIG["api_token"]:
        print("\n⛔ إصلح الإعدادات فوق (CONFIG / TELEGRAM) وشغّل تاني.")
        sys.exit(1)

    seen_ids = load_seen_ids()
    print(f"ℹ️  Loaded {len(seen_ids)} previously-seen codes from state file.")
    print("── Running ────────────────────────────────────────────────────")

    if args.once:
        seen_ids, stats = run_cycle(seen_ids)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] "
              f"fetched={stats['fetched']} sent={stats['sent']} "
              f"duplicate={stats['duplicate']} failed={stats['failed']}")
        return

    print(f"🔁 Polling every {POLL_INTERVAL_SECONDS}s — Ctrl+C to stop.\n")
    while True:
        seen_ids, stats = run_cycle(seen_ids)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] "
              f"fetched={stats['fetched']} sent={stats['sent']} "
              f"duplicate={stats['duplicate']} failed={stats['failed']}")
        try:
            time.sleep(POLL_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("\n👋 Stopped.")
            break


if __name__ == "__main__":
    main()
