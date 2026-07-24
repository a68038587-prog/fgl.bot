
import subprocess
import sys

# ======================
# 🎨 CRASH DEVELOPER BANNER
# ======================
def print_crash_banner():
    CYAN    = "\033[96m"
    YELLOW  = "\033[93m"
    GREEN   = "\033[92m"
    MAGENTA = "\033[95m"
    RED     = "\033[91m"
    BLUE    = "\033[94m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"

    banner = f"""
{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   {RED} ██████╗██████╗  █████╗ ███████╗██╗  ██╗{CYAN}                          ║
║   {RED}██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║{CYAN}                          ║
║   {RED}██║     ██████╔╝███████║███████╗███████║{CYAN}                          ║
║   {RED}██║     ██╔══██╗██╔══██║╚════██║██╔══██║{CYAN}                          ║
║   {RED}╚██████╗██║  ██║██║  ██║███████║██║  ██║{CYAN}                          ║
║   {RED} ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{CYAN}                         ║
║                                                                      ║
║   {YELLOW}  ██████╗ ████████╗██████╗     ██████╗  ██████╗ ████████╗{CYAN}         ║
║   {YELLOW} ██╔═══██╗╚══██╔══╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝{CYAN}        ║
║   {YELLOW} ██║   ██║   ██║   ██████╔╝    ██████╔╝██║   ██║   ██║{CYAN}           ║
║   {YELLOW} ██║   ██║   ██║   ██╔═══╝     ██╔══██╗██║   ██║   ██║{CYAN}           ║
║   {YELLOW} ╚██████╔╝   ██║   ██║         ██████╔╝╚██████╔╝   ██║{CYAN}           ║
║   {YELLOW}  ╚═════╝    ╚═╝   ╚═╝         ╚═════╝  ╚═════╝    ╚═╝{CYAN}          ║
║                                                                      ║
║   {GREEN}  ╔═══════════════════════════════════════════════════════╗{CYAN}         ║
║   {GREEN}  ║  Developer  :  C R A S H  [ @fcamv ]                 ║{CYAN}         ║
║   {GREEN}  ║  System     :  OTP Smart Bot — Multi-Panel Engine     ║{CYAN}         ║
║   {GREEN}  ║  Version    :  v2.8.2  [ PRO Edition ]               ║{CYAN}         ║
║   {GREEN}  ║  Panels     :  Static + Dynamic + IVAS + API         ║{CYAN}         ║
║   {GREEN}  ║  Status     :  🔥 ONLINE & READY                     ║{CYAN}         ║
║   {GREEN}  ╚═══════════════════════════════════════════════════════╝{CYAN}         ║
║                                                                      ║
║   {MAGENTA}  ⚡ All rights reserved © CRASH Developer 2026 ⚡{CYAN}                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
{RESET}"""
    print(banner)

    import time as _t
    steps = [
        (f"{BLUE}[BOOT]{RESET} Loading system modules       ", 0.08),
        (f"{BLUE}[BOOT]{RESET} Connecting to database        ", 0.08),
        (f"{BLUE}[BOOT]{RESET} Initializing panel engines    ", 0.08),
        (f"{BLUE}[BOOT]{RESET} Starting Telegram bot         ", 0.08),
        (f"{BLUE}[BOOT]{RESET} Mounting panel monitors       ", 0.08),
        (f"{GREEN}[BOOT]{RESET} ✅ All systems operational     ", 0.05),
    ]
    bar_len = 30
    for label, delay in steps:
        for i in range(bar_len + 1):
            filled = "█" * i
            empty  = "░" * (bar_len - i)
            pct    = int(i / bar_len * 100)
            print(f"\r  {label}  [{CYAN}{filled}{RESET}{empty}] {YELLOW}{pct}%{RESET}", end="", flush=True)
            _t.sleep(delay / bar_len)
        print()

    print(f"\n{CYAN}{'═'*72}{RESET}\n")

print_crash_banner()


def _cprint(tag, msg, color="\033[96m", tag_color="\033[93m"):
    """طباعة ملونة موحدة للتيرمينال"""
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    now    = datetime.now().strftime("%H:%M:%S")
    print(f"{DIM}[{now}]{RESET} {tag_color}{BOLD}[{tag}]{RESET} {color}{msg}{RESET}")


def _panel_box(panel_name, number="", sms="", status="NEW"):
    """طباعة رسالة OTP داخل مربع ملوّن مميز لكل لوحة"""
    import time as _t
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"

    PANEL_COLORS = [
        "\033[96m",  # Cyan
        "\033[93m",  # Yellow
        "\033[92m",  # Green
        "\033[95m",  # Magenta
        "\033[94m",  # Blue
        "\033[91m",  # Red
        "\033[97m",  # White
    ]
    color = PANEL_COLORS[hash(panel_name) % len(PANEL_COLORS)]

    STATUS_MAP = {
        "NEW":   ("\033[92m", "📨 NEW OTP"),
        "WARN":  ("\033[93m", "⚠️  WARNING"),
        "ERR":   ("\033[91m", "❌ ERROR"),
        "INFO":  ("\033[96m", "ℹ️  INFO"),
        "LOGIN": ("\033[95m", "🔐 LOGIN"),
        "EMPTY": ("\033[90m", "📭 NO MSG"),
    }
    sc, slabel = STATUS_MAP.get(status, ("\033[92m", f"• {status}"))

    now   = _t.strftime("%H:%M:%S")
    width = 56

    top    = f"┌{'─'*width}┐"
    bottom = f"└{'─'*width}┘"
    sep    = f"├{'─'*width}┤"

    _strip_codes = [BOLD, RESET, DIM, color, sc,
        "\033[90m","\033[92m","\033[91m","\033[93m",
        "\033[95m","\033[94m","\033[97m","\033[96m"]

    def row(content):
        visible = content
        for c in _strip_codes:
            visible = visible.replace(c, "")
        spaces = max(0, width - len(visible) - 2)
        return f"│ {content}{' ' * spaces} │"

    title_str = f"{BOLD}{color}⚡ {panel_name.upper()}{RESET}"
    time_str  = f"{DIM}🕐 {now}{RESET}"
    status_str = f"{sc}{BOLD}{slabel}{RESET}"
    num_str   = f"{BOLD}📱 {number}{RESET}" if number else ""
    sms_short = (sms[:46] + "…") if len(sms) > 46 else sms
    sms_str   = f"💬 {sms_short}" if sms else ""

    print(f"{color}{top}{RESET}")
    print(f"{color}{row(title_str + '   ' + time_str)}{RESET}")
    print(f"{color}{sep}{RESET}")
    print(f"{color}{row(status_str)}{RESET}")
    if num_str:
        print(f"{color}{row(num_str)}{RESET}")
    if sms_str:
        print(f"{color}{row(sms_str)}{RESET}")
    print(f"{color}{bottom}{RESET}")


def upgrade_telebot():
    """تحديث مكتبة pyTelegramBotAPI إلى آخر إصدار تلقائيًا"""
    try:
        print("[UPDATER] جاري التحقق من تحديث مكتبة pyTelegramBotAPI...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pyTelegramBotAPI", "--quiet"],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            print("[UPDATER] ✅ تم تحديث المكتبة إلى أحدث إصدار بنجاح")
        else:
            print(f"[UPDATER] ⚠️ لا توجد حاجة للتحديث أو فشل: {result.stderr[:100]}")
    except Exception as e:
        print(f"[UPDATER] ❌ فشل تحديث المكتبة: {e}")

# تحديث المكتبة قبل أي استيراد آخر
upgrade_telebot()

import time
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import re
import io
import base64
import os
import hashlib
from datetime import datetime, date, timedelta
from urllib.parse import quote_plus
import sqlite3
import telebot
from telebot import types
import threading
import random
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

# ======================
# 🗄️ إعدادات قاعدة البيانات
# ======================
DB_PATH = "sendako.db"
BOT_TOKEN = "8635536355:AAHJs6WWIYk69b40WCSVR8f984hpiqOyh80"  # استبدل بتوكنك الحقيقي
CHAT_IDS = ["-1003947736633"]  # معرفات المجموعات/القنوات التي ترسل إليها OTP
ADMIN_IDS = [8065884629]  # معرفات الأدمن الرئيسيين

# ======================
# إعدادات السرعة
# ======================
REFRESH_INTERVAL = 1  # الفاصل الزمني الأساسي (سيتم تجاهله لصالح فترات كل لوحة)
PARALLEL_FETCH = True
MAX_WORKERS = 50  # ⚡ أقصى سرعة

# ======================
# كاش نتايج فحص اللوحات (بيتحدّث في الخلفية)
# ======================
# { "panel_name": {"status": "...", "ts": time.time()} }
_panel_check_cache = {}
_panel_check_lock  = threading.Lock()

# ======================
# وضع الصيانة
# ======================
MAINTENANCE_MODE = False

# ======================
# صورالبوت
# ======================
BOT_IMAGE_BYTES = None
MAINTENANCE_IMAGE_BYTES = None
FORCE_SUB_IMAGE_BYTES = None

# ======================
# دالة تحويل النص إلى bold
# ======================
def to_bold(text):
    bold_map = {
        'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙', 'G': '𝗚', 'H': '𝗛', 'I': '𝗜',
        'J': '𝗝', 'K': '𝗞', 'L': '𝗟', 'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥',
        'S': '𝗦', 'T': '𝗧', 'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫', 'Y': '𝗬', 'Z': '𝗭',
        'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳', 'g': '𝗴', 'h': '𝗵', 'i': '𝗶',
        'j': '𝗷', 'k': '𝗸', 'l': '𝗹', 'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽', 'q': '𝗾', 'r': '𝗿',
        's': '𝘀', 't': '𝘁', 'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅', 'y': '𝘆', 'z': '𝘇',
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯', '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳', '8': '𝟴', '9': '𝟵'
    }
    return ''.join(bold_map.get(ch, ch) for ch in text)

# ======================
# اللوحات الثابتة (مع تحسين Konecta و Fire)
# ======================
STATIC_DASHBOARDS = [

    # ==================== Bolt SMS ====================
    {
        "name": "Bolt SMS",
        "type": "traditional",
        "base_url": "http://93.190.143.35/ints",
        "login_page": "/Login",
        "login_post": "/signin",
        "ajax_path": "/agent/res/data_smscdr.php",
        "username": "hazemaslam1500",
        "password": "12345678",
        "short": "BT", "short_bold": to_bold("BT"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1,
    },

    # ==================== Time SMS ====================
    {
        "name": "Time SMS",
        "type": "api_token",
        "api_url": "http://147.135.212.197/crapi/time/viewstats",
        "api_token": "SFRXNEVBl3x8V4l3SH93eXdxZXh1kYFGfnaFYWNyZmdYUmRUeoc=",
        "short": "TM", "short_bold": to_bold("TM"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    # ==================== XAP SMS ====================
    {
        "name": "XAP SMS",
        "type": "traditional",
        "base_url": "http://147.135.212.148",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "XP", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },


    # ==================== Hadi SMS (API) ====================
    {
        "name": "Hadi SMS",
        "type": "api_token",
        "api_url": "http://147.135.212.197/crapi/had/viewstats",
        "api_token": "R1BWRTRSQlZ9ZINoioJmV2qKbF-GcFCLhJSFf4uIVHRhiZR5Rl9i",
        "short": "HD", "short_bold": to_bold("HD"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    # ==================== Hadi SMS (Traditional) ====================
    {
        "name": "Hadi SMS 2",
        "type": "traditional",
        "base_url": "http://185.2.83.39",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "stats_page": "/ints/agent/SMSCDRStats",
        "username":"crash2026",
        "password":"Boody0000",
        "short": "H2", "short_bold": to_bold("H2"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    # ==================== Mariam SMS ====================
    {
        "name": "Sniper SMS",
        "type": "traditional",
        "base_url": "http://135.125.222.224",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "mariamxemon",
        "password": "123123123",
        "short": "SN", "short_bold": to_bold("SN"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    # ==================== Squad SMS ====================
    {
        "name": "Squad SMS",
        "type": "traditional",
        "base_url": "http://51.77.221.209",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "mohamed1500",
        "password": "12345678",
        "short": "SQ", "short_bold": to_bold("SQ"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1,
    },

    # ==================== 44 Numbers ====================
    {
        "name": "44 Numbers",
        "type": "traditional",
        "base_url": "http://185.177.124.145",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "stats_page": "/ints/agent/SMSCDRStats",
        "username": "",
        "password": "",
        "short": "44", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    # ==================== Lamix SMS ====================
    {
        "name": "Lamix SMS",
        "type": "traditional",
        "base_url": "http://139.99.208.63",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "LM", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    # ==================== GROUP SMS ====================
    {
        "name": "GROUP SMS",
        "type": "traditional",
        "base_url": "http://139.99.63.204",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "GR", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    # ==================== MSI SMS ====================
    {
        "name": "MSI SMS",
        "type": "traditional",
        "base_url": "http://145.239.130.45",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "hazem1230",
        "password": "hazem1230",
        "short": "MS", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    # ==================== Proton SMS ====================
    {
        "name": "Proton SMS",
        "type": "traditional",
        "base_url": "http://109.236.84.81/ints",
        "login_page": "/login",
        "login_post": "/signin",
        "ajax_path": "/agent/res/data_smscdr.php",
        "username": "",
        "password": "",
        "short": "PR", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 10, "refresh_interval": 1,
    },

    # ==================== IMS SMS ====================
    {
        "name": "IMS SMS",
        "type": "ims_panel",
        "base_url": "http://45.82.67.20",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "dashboard_path": "/ints/agent/SMSCDRReports",
        "username": "hazemaslam12300",
        "password": "Namnyn-tivzuh-9kogsu",
        "short": "IM", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 8, "refresh_interval": 1, "records": 10,
    },



    # ==================== Roxy SMS (API) ====================
    {
        "name": "Roxy SMS",
        "type": "api_token",
        "api_url": "http://51.77.216.195/crapi/rx/viewstats",
        "api_token": "",
        "short": "RX", "short_bold": to_bold("WS"),
        "source": "static",
        "data_keys": {"date": None, "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    # ==================== D-Group SMS (API) ====================
    {
        "name": "D-Group SMS",
        "type": "api_token",
        "api_url": "http://51.77.216.195/crapi/dgroup/viewstats",
        "api_token": "",
        "short": "DG", "short_bold": to_bold("WS"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    # ==================== Numper Panel (API) ====================
    {
        "name": "Numper Panel",
        "type": "api",
        "api_url": "http://147.135.212.197/crapi/st/viewstats",
        "api_token": "RVNYQ0pBUzRdf2yLVZZlXFyPiIlVaIxSYoFyeURPkGRGaYRoU1KHgg==",
        "short": "NP", "short_bold": to_bold("WS"),
        "source": "static",
        "idx_date": 3, "idx_number": 1, "idx_sms": 2,
        "refresh_interval": 1,
    },

    # ==================== Konecta Panel (محسنة) ====================
    {
        "name": "Konecta Panel",
        "type": "traditional",
        "base_url": "https://www.konektapremium.net",
        "login_page": "/sign-in",
        "login_post": "/signin",
        "ajax_path": "/agent/res/data_smscdr.php",
        "username": "medo1100",
        "password": "medo1100",
        "short": "KN", "short_bold": to_bold("WS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 15, "refresh_interval": 1,
    },

    # ==================== S1T Panel (API) ====================
    {
        "name": "S1T Panel",
        "type": "api_token",
        "api_url": "http://147.135.212.197/crapi/s1t/viewstats",
        "api_token": "Sk5XRzRSQmFGeI90flRXRnRgVGZVg2yCRn-Cd4CJdHuHaZRhfnBq",
        "short": "S1", "short_bold": to_bold("WS"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    # ==================== FIRE (محسنة) ====================
    {
        "name": "FIRE",
        "type": "traditional",
        "base_url": "http://54.39.104.241",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "login_page_url": "http://54.39.104.241/ints/login",
        "login_post_url": "http://54.39.104.241/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "hazemaslam1800",
        "password": "hazemaslam1800",
        "short": "FS", "short_bold": to_bold("FS"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 15, "refresh_interval": 1,
    },

    # ==================== Green SMS ====================
    {
        "name": "Green SMS",
        "type": "traditional",
        "base_url": "http://139.99.9.4",
        "login_page": "/ints/login",
        "login_post": "/ints/signin",
        "login_page_url": "http://139.99.9.4/ints/login",
        "login_post_url": "http://139.99.9.4/ints/signin",
        "ajax_path": "/ints/agent/res/data_smscdr.php",
        "username": "Crash123",
        "password": "Crash123",
        "short": "GN", "short_bold": to_bold("GN"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 15, "refresh_interval": 1,
    },

    # ==================== Konekta API ====================
    {
        "name": "Konekta API",
        "type": "api_token",
        "api_url": "http://51.77.216.195/crapi/konek/viewstats",
        "api_token": "",
        "short": "KA", "short_bold": to_bold("KA"),
        "source": "static",
        "data_keys": {"date": "dt", "number": "num", "sms": "message", "service": "cli"},
        "refresh_interval": 1,
    },

    # ==================== Fly Panel New (etkk) ====================
    {
        "name": "Fly Panel New",
        "type": "ims_panel",
        "base_url": "https://flysms.net",
        "login_page": "/login",
        "login_post": "/signin",
        "ajax_path": "/agent/res/data_smscdr.php",
        "dashboard_path": "/agent/SMSCDRReports",
        "username": "",
        "password": "",
        "short": "FN", "short_bold": to_bold("FN"),
        "source": "static", "idx_date": 0, "idx_number": 2, "idx_sms": 5,
        "timeout": 30, "refresh_interval": 1, "records": 50,
    },

]


# ======================
# ⚙️ إعدادات اللوحات الديناميكية (إضافة حسابات من الأدمن)
# ======================
PANEL_SETTINGS_FILE = "panel_accounts.json"

PANEL_SITES = {
    "Bolt":     {"name":"Bolt SMS",      "short":"BT","base_url":"http://93.190.143.35/ints","login_page":"/Login","login_post":"/signin","ajax_path":"/agent/res/data_smscdr.php","type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":30,"refresh_interval":1,"username":"Ahmedd","password":"Ahmed0192"},
    "TimeSMS":  {"name":"Time SMS", "short":"TM", "type":"api_token", "api_url":"http://147.135.212.197/crapi/time/viewstats", "api_token":"", "data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}, "refresh_interval":1},
    "XAP":      {"name":"XAP SMS",       "short":"XP","base_url":"http://147.135.212.148",        "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",         "password":""},
    "Hadi":     {"name":"Hadi SMS",      "short":"HD","api_url":"http://147.135.212.197/crapi/had/viewstats","api_token":"SVVXSTRSQl5zdomHilCJe0ZTk1ldcmVCfWxXcnNmh1RFjlGASZNm","type":"api_token","refresh_interval":1,"data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}},
    "Hadi2":    {"name":"Hadi SMS 2",    "short":"H2","base_url":"http://185.2.83.39",            "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"crash2026","password":"Boody0000"},
    "Num44":    {"name":"44 Numbers",    "short":"44","base_url":"http://185.177.124.145",        "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",         "password":""},
    "Lamix":    {"name":"Lamix SMS",     "short":"LM","base_url":"http://139.99.208.63",          "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",         "password":""},
    "GROUP":    {"name":"GROUP SMS",     "short":"GR","base_url":"http://139.99.63.204",          "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"","password":""},
    "MSI":      {"name":"MSI SMS",       "short":"MS","base_url":"http://145.239.130.45",         "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"hazem1230","password":"hazem1230"},
    "Proton":   {"name":"Proton SMS",    "short":"PR","base_url":"http://109.236.84.81/ints",     "login_page":"/login",      "login_post":"/signin",      "ajax_path":"/agent/res/data_smscdr.php",         "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"",  "password":""},
    "IMS":      {"name":"IMS SMS",       "short":"IM","base_url":"http://45.82.67.20",            "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"ims_panel",  "idx_date":0,"idx_number":2,"idx_sms":5,"timeout":15,"refresh_interval":1,"username":"hazemaslam12300","password":"Namnyn-tivzuh-9kogsu","dashboard_path":"/ints/agent/SMSCDRReports","records":50},
    "IMSClient":{"name":"IMS Client",    "short":"IC","base_url":"https://imssms.org",            "login_page":"/login",      "login_post":"/signin",      "ajax_path":"/client/res/data_smscdr.php",         "type":"ims_client", "idx_date":0,"idx_number":2,"idx_sms":4,"timeout":15,"refresh_interval":1,"username":"","password":"","dashboard_path":"/client/SMSCDRStats","records":50},
    "Konecta":  {"name":"Konecta Panel", "short":"KN","base_url":"https://www.konektapremium.net","login_page":"/sign-in",    "login_post":"/signin",      "ajax_path":"/agent/res/data_smscdr.php",         "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":15,"refresh_interval":1,"username":"medo1100","password":"medo1100"},
    "FairSMS":  {"name":"FIRE",     "short":"FS","base_url":"http://54.39.104.241","login_page":"/ints/login","login_post":"/ints/signin","login_page_url":"http://54.39.104.241/ints/login","login_post_url":"http://54.39.104.241/ints/signin","ajax_path":"/ints/agent/res/data_smscdr.php","type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":15,"refresh_interval":1,"username":"hazemaslam1800","password":"hazemaslam1800"},
    "GreenSMS": {"name":"Green SMS",   "short":"GN","base_url":"http://139.99.9.4","login_page":"/ints/login","login_post":"/ints/signin","login_page_url":"http://139.99.9.4/ints/login","login_post_url":"http://139.99.9.4/ints/signin","ajax_path":"/ints/agent/res/data_smscdr.php","type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":15,"refresh_interval":1,"username":"Crash123","password":"Crash123"},
    "KonektaAPI":{"name":"Konekta API","short":"KA","api_url":"http://51.77.216.195/crapi/konek/viewstats","api_token":"","type":"api_token","refresh_interval":1,"data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}},
    "FlyNew":   {"name":"Fly Panel New", "short":"FN","base_url":"https://flysms.net",            "login_page":"/login",      "login_post":"/signin",      "ajax_path":"/agent/res/data_smscdr.php",         "type":"ims_panel",  "idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":2,"username":"",         "password":"", "dashboard_path":"/agent/SMSCDRReports"},
    "S1T":      {"name":"S1T Panel",     "short":"S1","api_url":"http://147.135.212.197/crapi/s1t/viewstats","api_token":"","type":"api_token","refresh_interval":1,"data_keys":{"date":"dt","number":"num","sms":"message","service":"cli"}},
    "Sniper":   {"name":"Sniper SMS",    "short":"SN","base_url":"http://135.125.222.224",        "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":10,"refresh_interval":1,"username":"mariamxemon",  "password":"123123123"},
    "Squad":    {"name":"Squad SMS",     "short":"SQ","base_url":"http://51.77.221.209",          "login_page":"/ints/login", "login_post":"/ints/signin", "ajax_path":"/ints/agent/res/data_smscdr.php",    "type":"traditional","idx_date":0,"idx_number":2,"idx_sms":5,"timeout":30,"refresh_interval":1,"username":"mohamed1500",   "password":"12345678"},
}


def load_panel_accounts():
    """تحمّل الحسابات:
    1. username/password من PANEL_SITES مباشرة (الحساب الأساسي)
    2. حسابات إضافية مضافة من الأدمن (JSON)
    """
    saved = {}
    if os.path.exists(PANEL_SETTINGS_FILE):
        try:
            with open(PANEL_SETTINGS_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
        except:
            saved = {}

    result = {}
    for sk, site in PANEL_SITES.items():
        result[sk] = {"accounts": []}
        seen_users = set()

        site_type = site.get("type", "traditional")

        if site_type in ("api", "api_token"):
            # لوحة API - api_token من الملف مباشرة
            token = site.get("api_token", "").strip()
            if token:
                result[sk]["accounts"].append({
                    "id": "default_api",
                    "api_token": token,
                    "username": "API",
                    "password": "",
                    "source": "default"
                })
        else:
            # 1. الحساب الأساسي من الملف مباشرة (username/password)
            uname = site.get("username", "").strip()
            passwd = site.get("password", "").strip()
            if uname and passwd:
                result[sk]["accounts"].append({
                    "id": f"default_{uname}",
                    "username": uname,
                    "password": passwd,
                    "source": "default"
                })
                seen_users.add(uname)

            # 2. حسابات إضافية من الأدمن (JSON)
            for acc in saved.get(sk, {}).get("accounts", []):
                uname2 = acc.get("username", "").strip()
                passwd2 = acc.get("password", "").strip()
                if uname2 and passwd2 and uname2 not in seen_users:
                    result[sk]["accounts"].append(acc)
                    seen_users.add(uname2)

    return result

def save_panel_accounts(data):
    """تحفظ بس الحسابات المضافة من الأدمن (مش الحسابات الأساسية من الملف)"""
    to_save = {}
    for sk, v in data.items():
        to_save[sk] = {
            "accounts": [a for a in v.get("accounts", [])
                         if a.get("source") != "default"]
        }
    with open(PANEL_SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(to_save, f, ensure_ascii=False, indent=2)

def get_panel_accounts(site_key):
    data = load_panel_accounts()
    return data.get(site_key, {}).get("accounts", [])

def add_panel_account(site_key, username, password):
    """يضيف حساب جديد من الأدمن ويحفظه في JSON"""
    saved = {}
    if os.path.exists(PANEL_SETTINGS_FILE):
        try:
            with open(PANEL_SETTINGS_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
        except:
            saved = {}
    if site_key not in saved:
        saved[site_key] = {"accounts": []}
    account = {"id": str(int(time.time() * 1000)), "username": username, "password": password}
    saved[site_key]["accounts"].append(account)
    with open(PANEL_SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(saved, f, ensure_ascii=False, indent=2)
    return account

def delete_panel_account(site_key, account_id):
    """يحذف حساب مضاف من الأدمن - default_accounts مينفعش تتحذف من هنا"""
    if account_id.startswith("default_"):
        return False
    saved = {}
    if os.path.exists(PANEL_SETTINGS_FILE):
        try:
            with open(PANEL_SETTINGS_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
        except:
            saved = {}
    if site_key not in saved:
        return False
    before = len(saved[site_key].get("accounts", []))
    saved[site_key]["accounts"] = [a for a in saved[site_key]["accounts"] if a["id"] != account_id]
    if len(saved[site_key]["accounts"]) < before:
        with open(PANEL_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(saved, f, ensure_ascii=False, indent=2)
        stop_ev = _panel_stop_events.pop(f"{site_key}_{account_id}", None)
        if stop_ev:
            stop_ev.set()
        return True
    return False

_panel_stop_events = {}
_panel_threads = {}

def start_panel_account_monitor(site_key, account):
    """تشغيل مراقبة لحساب محدد"""
    account_id = account["id"]
    key = f"{site_key}_{account_id}"
    if key in _panel_threads and _panel_threads[key].is_alive():
        return
    stop_ev = threading.Event()
    _panel_stop_events[key] = stop_ev
    def _run():
        _monitor_panel_account(site_key, account, stop_ev)
    t = threading.Thread(target=_run, daemon=True)
    _panel_threads[key] = t
    t.start()
    print(f"[Panel Monitor] ▶️  \033[92m{PANEL_SITES[site_key]['name']}\033[0m / \033[96m{account['username']}\033[0m — بدأت المراقبة")

def start_all_panel_monitors():
    """تشغيل كل الحسابات المحفوظة عند بدء البوت"""
    for site_key in PANEL_SITES:
        for account in get_panel_accounts(site_key):
            start_panel_account_monitor(site_key, account)

def _monitor_panel_account(site_key, account, stop_event):
    """مراقبة حساب واحد - login + fetch محسّن مأخوذ من ملف app الشغّال"""
    site        = PANEL_SITES[site_key]
    account_id  = account["id"]
    short_bold  = to_bold(site["short"])
    site_type   = site.get("type", "traditional")
    interval    = site.get("refresh_interval", 3)

    # ── API / api_token ────────────────────────────────────────────────────
    if site_type in ("api", "api_token"):
        api_token = account.get("api_token") or site.get("api_token", "")
        api_url   = site.get("api_url", "")
        if not api_token or not api_url:
            print(f"[SKIP] {site['name']} - لا يوجد API token/url")
            return

        sent_file   = f"sent_messages_{site_key}_{account_id}.json"
        sent_local  = set()
        try:
            if os.path.exists(sent_file):
                with open(sent_file) as _f:
                    sent_local = set(json.load(_f))
        except: pass

        def _save_sent_api():
            try:
                with open(sent_file, "w") as _f:
                    json.dump(list(sent_local)[-500:], _f)
            except: pass

        print(f"[{site['name']}] 🌐 API مراقبة بدأت...")
        while not stop_event.is_set():
            try:
                today = datetime.now()
                params = {
                    "token":   api_token,
                    "records": 50,
                    "dt1": (today - timedelta(days=1)).strftime("%Y-%m-%d 00:00:00"),
                    "dt2":  today.strftime("%Y-%m-%d 23:59:59"),
                }
                r = requests.get(api_url, params=params, timeout=site.get("timeout", 30))
                if r.status_code == 200:
                    data = r.json()
                    rows = []
                    if isinstance(data, dict):
                        if data.get("status") == "success" and data.get("data"):
                            rows = data["data"]
                        else:
                            for k in ("data", "aaData", "rows", "result"):
                                if k in data and isinstance(data[k], list):
                                    rows = data[k]; break
                    elif isinstance(data, list):
                        rows = data

                    new_msgs = []
                    for row in rows:
                        dkeys = site.get("data_keys", {})
                        if isinstance(row, dict):
                            num = clean_number(str(row.get(dkeys.get("number","num"), "")))
                            sms = clean_html(str(row.get(dkeys.get("sms","message"), "")))
                            dt  = str(row.get(dkeys.get("date","dt"), ""))
                        elif isinstance(row, (list,tuple)):
                            i_d = site.get("idx_date",0); i_n = site.get("idx_number",1); i_s = site.get("idx_sms",2)
                            dt  = clean_html(str(row[i_d])) if len(row)>i_d else ""
                            num = clean_number(str(row[i_n])) if len(row)>i_n else ""
                            sms = clean_html(str(row[i_s])) if len(row)>i_s else ""
                        else:
                            continue
                        if not num or not sms or len(num)<7: continue
                        mk = f"{dt}|{num}|{sms[:50]}"
                        if mk not in sent_local:
                            new_msgs.append((dt, num, sms)); sent_local.add(mk)
                    if new_msgs:
                        _panel_box(site['name'], sms=f"{len(new_msgs)} رسالة جديدة", status="INFO")
                        _save_sent_api()
                        for dt,num,sms in new_msgs:
                            _panel_box(site['name'], mask_number(num), sms[:60], status="NEW")
                            send_otp_to_user_and_group(dt, num, sms,
                                panel_name=site["name"], short_bold=short_bold)
                    else:
                        _panel_box(site['name'], status="EMPTY")
                else:
                    _panel_box(site['name'], sms=f"HTTP {r.status_code}", status="WARN")
            except Exception as e:
                _panel_box(site['name'], sms=str(e)[:50], status="ERR")
            stop_event.wait(min(interval, 1))
        return

    # ── Traditional / ims_panel ────────────────────────────────────────────
    uname  = account.get("username","").strip()
    passwd = account.get("password","").strip()
    if not uname or not passwd:
        print(f"[SKIP] {site['name']} - حساب بدون يوزر/باسورد")
        return

    username = uname
    password = passwd

    base_url       = site.get("base_url","")
    login_page_url = site.get("login_page_url") or (base_url.rstrip("/")+site.get("login_page",""))
    login_post_url = site.get("login_post_url") or (base_url.rstrip("/")+site.get("login_post",""))
    ajax_path      = site.get("ajax_path", "/ints/agent/res/data_smscdr.php")
    ajax_url       = base_url.rstrip("/") + ajax_path
    TIMEOUT        = site.get("timeout", 30)
    CHECK_INTERVAL = interval

    last_msg_file  = f"last_message_{site_key}_{account_id}.txt"
    sent_msgs_file = f"sent_messages_{site_key}_{account_id}.json"
    last_seen_key  = ""
    sent_msgs_local= set()

    def _load_state():
        nonlocal last_seen_key, sent_msgs_local
        try:
            if os.path.exists(last_msg_file):
                with open(last_msg_file,"r",encoding="utf-8") as f: last_seen_key = f.read().strip()
        except: pass
        try:
            if os.path.exists(sent_msgs_file):
                with open(sent_msgs_file) as f: sent_msgs_local = set(json.load(f))
        except: pass

    def _save_state():
        try:
            with open(last_msg_file,"w",encoding="utf-8") as f: f.write(last_seen_key)
        except: pass
        try:
            with open(sent_msgs_file,"w") as f:
                json.dump(list(sent_msgs_local)[-500:], f)
        except: pass

    session = requests.Session()
    session.verify = False
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
    })

    is_logged_in   = False
    current_sesskey = None

    # ── Login ──────────────────────────────────────────────────────────────
    def do_login():
        nonlocal is_logged_in, current_sesskey
        nonlocal username, password
        # إعادة قراءة الكريدنشيال من PANEL_SITES عشان لو اتغيرت
        _accounts_fresh = get_panel_accounts(site_key)
        _acc = next((a for a in _accounts_fresh if a.get('id') == account_id), None)
        if _acc and _acc.get('username'):
            username = _acc.get('username', username).strip()
            password = _acc.get('password', password).strip()
        elif PANEL_SITES.get(site_key, {}).get('username'):
            username = PANEL_SITES[site_key].get('username', username).strip()
            password = PANEL_SITES[site_key].get('password', password).strip()
        print(f"[{site['name']}] ({username}) 🔐 تسجيل الدخول...")
        try:
            resp = session.get(login_page_url, timeout=TIMEOUT)
            if resp.status_code != 200:
                print(f"[{site['name']}] ({username}) ⚠️ صفحة الدخول: {resp.status_code}")
                return False

            # ── Captcha ──
            match = re.search(r'What is (\d+) \+ (\d+)', resp.text)
            if not match:
                match = re.search(r'(\d+)\s*\+\s*(\d+)', resp.text)
            if match:
                captcha_answer = str(int(match.group(1)) + int(match.group(2)))
                print(f"[{site['name']}] ({username}) 🧮 captcha={captcha_answer}")
            else:
                captcha_answer = ""
                print(f"[{site['name']}] ({username}) ⚠️ captcha غير موجود، محاولة بدونه")

            # ── crlf token ──
            crlf_match = re.search(r"name=['\"]crlf['\"].*?value=['\"]([^'\"]+)['\"]", resp.text)
            if not crlf_match:
                crlf_match = re.search(r"value=['\"]([^'\"]+)['\"].*?name=['\"]crlf['\"]", resp.text)

            payload = {}
            # ── hidden fields إضافية أولاً ──
            payload.update(_extract_hidden_fields(resp.text))
            # ── username/password بعديهم عشان ميتوvrideوش ──
            payload["username"] = username
            payload["password"] = password
            if captcha_answer:
                payload["capt"] = captcha_answer
            if crlf_match:
                payload["crlf"] = crlf_match.group(1)
                print(f"[{site['name']}] ({username}) 🔑 crlf مستخرج")

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer":  login_page_url,
                "Origin":   base_url.rstrip("/"),
                "Accept":   "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
            r2 = session.post(login_post_url, data=payload, headers=headers,
                              timeout=max(TIMEOUT,20), allow_redirects=True)
            print(f"[{site['name']}] ({username}) 📊 URL بعد login: {r2.url}")

            # ── كشف النجاح ──
            success_kw = ["dashboard","logout","agent","reports","smscdr"]
            r2_url_lower  = r2.url.lower()
            r2_text_lower = r2.text.lower()
            # كشف حقيقي لفشل الدخول: وجود form login (input type=password) وليس مجرد كلمة password في JS
            import re as _re
            _has_login_form = bool(_re.search(
                r'<input[^>]+type=["\']password["\']', r2.text, _re.IGNORECASE
            ))
            is_success = (
                any(kw in r2_url_lower  for kw in success_kw) or
                any(kw in r2_text_lower for kw in ["dashboard","logout","smscdr","signout","sign out"]) or
                (r2.url != login_page_url
                 and "login"  not in r2_url_lower
                 and "signin" not in r2_url_lower) or
                # بعض السيرفرات بترجع نفس الـ URL لكن الـ HTML يكون dashboard
                (r2.status_code == 200
                 and not _has_login_form
                 and len(r2.text) > 2000)
            )

            # تحقق ثانوي بزيارة صفحة الـ agent
            if not is_success:
                for sp in ["/ints/agent/SMSCDRReports", "/agent/SMSCDRReports",
                           "/ints/agent/SMSCDRStats", "/agent/SMSCDRStats"]:
                    try:
                        tr = session.get(base_url.rstrip("/")+sp, timeout=10)
                        if (tr.status_code == 200
                                and "login" not in tr.url.lower()
                                and "signin" not in tr.url.lower()
                                and "password" not in tr.text.lower()):
                            is_success = True; break
                    except: pass

            if is_success:
                is_logged_in = True
                # استخراج sesskey
                for sp in ["/ints/agent/SMSCDRReports","/agent/SMSCDRReports",
                           "/ints/agent/SMSCDRStats",  "/agent/SMSCDRStats"]:
                    try:
                        sr = session.get(base_url.rstrip("/")+sp, timeout=8)
                        sk = re.search(r'sesskey=([A-Za-z0-9=+/]{10,})', sr.text)
                        if not sk:
                            sk = re.search(r'sesskey[\s"\'=:]+([A-Za-z0-9=+/]{10,})', sr.text)
                        if sk:
                            current_sesskey = sk.group(1)
                            print(f"[{site['name']}] 🔑 sesskey OK")
                            break
                    except: continue
                print(f"\033[92m[{site['name']}] ({username}) ✅ دخل بنجاح\033[0m")
                return True
            else:
                print(f"[{site['name']}] ({username}) ❌ فشل الدخول")
                return False
        except Exception as e:
            print(f"[{site['name']}] ({username}) ❌ خطأ login: {e}")
            return False

    # ── Fetch SMS ──────────────────────────────────────────────────────────
    def fetch_sms_data():
        nonlocal is_logged_in, current_sesskey

        today      = datetime.now()
        start_date = (today - timedelta(days=1)).strftime("%Y-%m-%d")
        end_date   = (today + timedelta(days=1)).strftime("%Y-%m-%d")

        # ── محاولة 1: AJAX مع sesskey (نفس أسلوب app) ──
        sms_page = base_url.rstrip("/")+"/ints/agent/SMSCDRReports"
        for attempt in range(2):
            try:
                page_resp = session.get(sms_page, timeout=TIMEOUT)
                if page_resp.status_code == 200:
                    _has_pw_form = bool(re.search(
                        r'<input[^>]+type=["\']password["\']', page_resp.text, re.IGNORECASE
                    ))
                    if _has_pw_form:
                        is_logged_in = False
                        print(f"[{site['name']}] ({username}) ⚠️ جلسة منتهية")
                        return None  # يشير لإعادة login
                    # استخراج sesskey من الصفحة
                    sk = re.search(r'sesskey=([A-Za-z0-9=+/]+)', page_resp.text)
                    if sk:
                        current_sesskey = sk.group(1)
                elif page_resp.status_code in (502,503,504):
                    time.sleep(3 + attempt*2); continue
                break
            except Exception as e:
                time.sleep(2); continue

        # ── payload AJAX كامل ──
        payload = {
            "fdate1": f"{start_date} 00:00:00",
            "fdate2": f"{end_date} 23:59:59",
            "frange":"","fclient":"","fnum":"","fcli":"",
            "fgdate":"","fgmonth":"","fgrange":"",
            "fgclient":"","fgnumber":"","fgcli":"",
            "fg":"0","sEcho":"1",
            "iColumns":"9","sColumns":"",
            "iDisplayStart":"0","iDisplayLength":"100",
            "mDataProp_0":"0","mDataProp_1":"1","mDataProp_2":"2",
            "mDataProp_3":"3","mDataProp_4":"4","mDataProp_5":"5",
            "mDataProp_6":"6","mDataProp_7":"7","mDataProp_8":"8",
            "sSearch":"","bRegex":"false",
            "iSortCol_0":"0","sSortDir_0":"desc","iSortingCols":"1",
        }
        if current_sesskey:
            payload["sesskey"] = current_sesskey

        ajax_headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Referer": sms_page,
            "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }

        for retry in range(3):
            try:
                # POST أولاً (الأنجح مع Fire SMS)، ثم GET
                resp = session.post(ajax_url, data=payload,
                                    headers=ajax_headers, timeout=TIMEOUT)
                if resp.status_code == 200:
                    try:
                        data = resp.json()
                        for k in ("aaData","data","rows"):
                            if k in data and isinstance(data[k], list):
                                return data[k]
                        if isinstance(data, list):
                            return data
                        # JSON فارغ = جلسة منتهية (نتحقق بوجود form login فعلي)
                        _ajax_has_pw = bool(re.search(r'<input[^>]+type=["\']password["\']', resp.text, re.IGNORECASE))
                        if _ajax_has_pw:
                            is_logged_in = False
                            return None
                        return []
                    except:
                        _ajax_has_pw2 = bool(re.search(r'<input[^>]+type=["\']password["\']', resp.text, re.IGNORECASE))
                        if _ajax_has_pw2:
                            is_logged_in = False
                            return None
                        # HTML parsing كبديل
                        try:
                            soup = BeautifulSoup(resp.text,"html.parser")
                            table = soup.find("table")
                            if table:
                                tbody = table.find("tbody")
                                trows = tbody.find_all("tr") if tbody else table.find_all("tr")[1:]
                                rows = []
                                for tr in trows:
                                    cells = tr.find_all("td")
                                    if len(cells) >= 6:
                                        rows.append([c.get_text(strip=True) for c in cells])
                                if rows:
                                    print(f"[{site['name']}] ({username}) 📄 HTML parsing")
                                    return rows
                        except: pass
                        return []
                elif resp.status_code == 200:
                    pass  # handled above
                elif resp.status_code in (302,403):
                    is_logged_in = False; return None
                elif resp.status_code in (502,503,504):
                    if retry < 2: time.sleep(3+retry*2); continue
                else:
                    print(f"[{site['name']}] ({username}) ⚠️ HTTP {resp.status_code}")
                    return []
            except requests.exceptions.Timeout:
                if retry < 2: time.sleep(2); continue
                print(f"[{site['name']}] ({username}) ⏱️ timeout")
                return []
            except Exception as e:
                if retry < 2 and ("Connection" in str(e) or "Timeout" in str(e)):
                    time.sleep(2); continue
                print(f"[{site['name']}] ({username}) ❌ fetch خطأ: {e}")
                is_logged_in = False; return []
        return []

    # ── Main loop ──────────────────────────────────────────────────────────
    print(f"[{site['name']}] ({username}) 🚀 بدء المراقبة...")
    _load_state()

    _login_retries = 0
    while not do_login():
        _login_retries += 1
        if _login_retries >= 5:
            print(f"[{site['name']}] ({username}) ❌ فشل الدخول بعد 5 محاولات - توقف")
            return
        print(f"[{site['name']}] ({username}) 🔄 إعادة محاولة الدخول ({_login_retries}/5)...")
        time.sleep(10)

    errors        = 0
    _current_day  = date.today()

    while not stop_event.is_set():
        try:
            # يوم جديد → إعادة login
            new_day = date.today()
            if new_day != _current_day:
                print(f"[{site['name']}] 🌅 يوم جديد - إعادة الدخول")
                is_logged_in = False; current_sesskey = None
                sent_msgs_local.clear(); _current_day = new_day

            if not is_logged_in:
                if not do_login():
                    stop_event.wait(30); continue

            raw = fetch_sms_data()

            if raw is None:
                # جلسة منتهية
                print(f"[{site['name']}] ({username}) 🔄 جلسة منتهية - إعادة الدخول")
                is_logged_in = False; current_sesskey = None
                stop_event.wait(min(interval,2)); continue

            if not raw:
                print(f"[{site['name']}] ({username}) 📭 لا أكواد")
            else:
                idx_d = site.get("idx_date",0)
                idx_n = site.get("idx_number",2)
                idx_s = site.get("idx_sms",5)

                parsed = []
                for row in raw:
                    if not isinstance(row,(list,tuple)) or len(row)<6: continue
                    date_val = clean_html(str(row[idx_d])) if len(row)>idx_d else ""
                    num_val  = clean_number(str(row[idx_n])) if len(row)>idx_n else ""
                    sms_val  = clean_html(str(row[idx_s])) if len(row)>idx_s else ""
                    if not date_val or not num_val or not sms_val or len(num_val)<7: continue
                    # فلترة صفوف حظر
                    if any(x in sms_val.lower() for x in
                           ["currency","payout","nan%","100%","0.008",
                            "my payout","client payout","range","cli","client"]):
                        continue
                    if sms_val.count(",")>=5 and ("%" in sms_val or "nan" in sms_val.lower()):
                        continue
                    parsed.append({"date":date_val,"number":num_val,"sms":sms_val})

                if not parsed:
                    print(f"[{site['name']}] ({username}) 📭 لا أكواد بعد الفلترة")
                else:
                    parsed.sort(key=lambda x: x["date"], reverse=False)
                    new_messages = []
                    for msg in parsed:
                        unique_key = f"{msg['date']}|{msg['number']}|{msg['sms'][:20]}"
                        if unique_key not in sent_msgs_local:
                            new_messages.append(msg)
                            sent_msgs_local.add(unique_key)

                    if new_messages:
                        _panel_box(site['name'], sms=f"{len(new_messages)} رسالة جديدة", status="INFO")
                        for msg in new_messages:
                            last_seen_key = f"{msg['date']}|{msg['number']}"
                            _panel_box(site['name'], f"{msg['number'][:6]}***", msg['sms'][:60], status="NEW")
                            send_otp_to_user_and_group(
                                msg["date"], msg["number"], msg["sms"],
                                panel_name=site["name"], short_bold=short_bold)
                        _save_state()
                    else:
                        _panel_box(site['name'], status="EMPTY")

            errors = 0

        except Exception as e:
            errors += 1
            print(f"[{site['name']}] ({username}) ⚠️ خطأ ({errors}/5): {e}")
            if errors >= 5:
                print(f"[{site['name']}] ({username}) 🔄 إعادة الدخول...")
                is_logged_in = False; current_sesskey = None
                if do_login(): errors = 0
                else: stop_event.wait(30)
            else:
                time.sleep(5)

        stop_event.wait(min(CHECK_INTERVAL, 1))

    print(f"[{site['name']}] ({username}) 🛑 توقفت المراقبة")


_static_dash_sessions = {}

# ======================
# قاعدة البيانات - التهيئة (مع check_same_thread=False للخيوط)
# ======================
def init_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT,
        last_name TEXT, country_code TEXT, assigned_number TEXT,
        is_banned INTEGER DEFAULT 0, private_combo_country TEXT DEFAULT NULL,
        lang TEXT DEFAULT 'ar', agreed_terms INTEGER DEFAULT 0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS combos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_code TEXT NOT NULL,
        numbers TEXT NOT NULL,
        section_id INTEGER,
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        file_name TEXT
    )''')
    c.execute('CREATE INDEX IF NOT EXISTS idx_combos_country ON combos(country_code)')
    c.execute('''CREATE TABLE IF NOT EXISTS sections (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS otp_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, otp TEXT,
        full_message TEXT, timestamp TEXT, assigned_to INTEGER
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS bot_settings (
        key TEXT PRIMARY KEY, value TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS private_combos (
        user_id INTEGER, country_code TEXT, numbers TEXT,
        PRIMARY KEY (user_id, country_code)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS force_sub_channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT, channel_url TEXT UNIQUE NOT NULL,
        description TEXT DEFAULT '', enabled INTEGER DEFAULT 1
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS admins (
        user_id INTEGER PRIMARY KEY, username TEXT DEFAULT ''
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS bot_groups (
        group_id TEXT PRIMARY KEY, description TEXT DEFAULT '', is_otp_group INTEGER DEFAULT 0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS otp_tg_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT, chat_id TEXT NOT NULL,
        message_id INTEGER NOT NULL, sent_at TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS otp_group_buttons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        button_text TEXT NOT NULL,
        button_url TEXT NOT NULL,
        position INTEGER DEFAULT 0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS auto_delete_settings (
        chat_id TEXT PRIMARY KEY, delete_after INTEGER DEFAULT 30
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS dashboard_accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, short TEXT NOT NULL,
        username TEXT, password TEXT, api_token TEXT, type TEXT DEFAULT 'traditional',
        base_url TEXT, ajax_path TEXT, login_page TEXT, login_post TEXT, stats_page TEXT,
        idx_date INTEGER DEFAULT 0, idx_number INTEGER DEFAULT 2, idx_sms INTEGER DEFAULT 5,
        timeout INTEGER DEFAULT 10, data_keys TEXT, is_active INTEGER DEFAULT 1,
        refresh_interval INTEGER DEFAULT 1
    )''')
    try:
        c.execute("ALTER TABLE dashboard_accounts ADD COLUMN refresh_interval INTEGER DEFAULT 1")
    except:
        pass
    c.execute('''CREATE TABLE IF NOT EXISTS custom_buttons (
        id INTEGER PRIMARY KEY AUTOINCREMENT, button_text TEXT NOT NULL,
        button_url TEXT NOT NULL, position INTEGER DEFAULT 0
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS bot_images (
        key TEXT PRIMARY KEY, image TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS maintenance_mode (
        id INTEGER PRIMARY KEY CHECK (id = 1), enabled INTEGER DEFAULT 0
    )''')
    c.execute("INSERT OR IGNORE INTO maintenance_mode (id, enabled) VALUES (1, 0)")
    c.execute('''CREATE TABLE IF NOT EXISTS otp_delete_global (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        delete_after INTEGER DEFAULT 30
    )''')
    c.execute("INSERT OR IGNORE INTO otp_delete_global (id, delete_after) VALUES (1, 30)")
    conn.commit()
    conn.close()

init_db()

def get_db_dashboards(only_active=True):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    if only_active:
        c.execute("SELECT * FROM dashboard_accounts WHERE is_active=1")
    else:
        c.execute("SELECT * FROM dashboard_accounts")
    rows = c.fetchall()
    conn.close()
    dashboards = []
    for row in rows:
        dash = {
            "id": row[0],
            "name": row[1],
            "short": row[2],
            "username": row[3],
            "password": row[4],
            "api_token": row[5],
            "type": row[6],
            "base_url": row[7],
            "ajax_path": row[8],
            "login_page": row[9],
            "login_post": row[10],
            "stats_page": row[11],
            "idx_date": row[12],
            "idx_number": row[13],
            "idx_sms": row[14],
            "timeout": row[15],
            "data_keys": json.loads(row[16]) if row[16] else {},
            "is_active": row[17],
            "refresh_interval": row[18] if len(row) > 18 else 1,
            "source": "db",
            "short_bold": to_bold(row[2])
        }
        dashboards.append(dash)
    return dashboards

def add_dashboard_account(name, short, username, password, api_token, dash_type, base_url,
                          ajax_path="", login_page="", login_post="", stats_page="",
                          idx_date=0, idx_number=2, idx_sms=5, timeout=10, data_keys=None, refresh_interval=1):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    data_keys_json = json.dumps(data_keys) if data_keys else "{}"
    c.execute("""INSERT INTO dashboard_accounts 
                 (name, short, username, password, api_token, type, base_url, ajax_path, 
                  login_page, login_post, stats_page, idx_date, idx_number, idx_sms, timeout, data_keys, is_active, refresh_interval)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?)""",
              (name, short, username, password, api_token, dash_type, base_url, ajax_path,
               login_page, login_post, stats_page, idx_date, idx_number, idx_sms, timeout, data_keys_json, refresh_interval))
    conn.commit()
    conn.close()

def delete_dashboard_account(id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM dashboard_accounts WHERE id=?", (id,))
    conn.commit()
    conn.close()

def toggle_dashboard_account(id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE dashboard_accounts SET is_active = 1 - is_active WHERE id=?", (id,))
    conn.commit()
    conn.close()

def get_all_active_dashboards():
    all_dash = []
    for dash in STATIC_DASHBOARDS:
        d = dash.copy()
        d["is_active"] = True
        name_key = d["name"]
        if name_key not in _static_dash_sessions:
            s = requests.Session()
            s.headers.update(COMMON_HEADERS)
            _static_dash_sessions[name_key] = {"session": s, "is_logged_in": False, "sesskey": None}
        d["session"]    = _static_dash_sessions[name_key]["session"]
        d["is_logged_in"] = _static_dash_sessions[name_key].get("is_logged_in", False)
        d["sesskey"]    = _static_dash_sessions[name_key].get("sesskey")
        def _build_url(base, path):
            if not path: return ""
            if path.startswith("http"): return path
            return base.rstrip("/") + path if base else path

        if d["type"] in ("api_token", "api"):
            d["is_logged_in"] = True
        elif d["type"] in ("ims_panel", "ims_client"):
            d["is_logged_in"] = False
            d["sesskey"] = None
            d["phpsessid"] = None
            d["last_login_time"] = 0
            d["login_page_url"] = _build_url(d.get("base_url",""), d.get("login_page",""))
            d["login_post_url"] = _build_url(d.get("base_url",""), d.get("login_post",""))
            d["ajax_url"]       = _build_url(d.get("base_url",""), d.get("ajax_path",""))
            d["dashboard_url"]  = _build_url(d.get("base_url",""), d.get("dashboard_path",""))
        else:
            d["login_page_url"] = _build_url(d.get("base_url",""), d.get("login_page",""))
            d["login_post_url"] = _build_url(d.get("base_url",""), d.get("login_post",""))
            d["ajax_url"]       = _build_url(d.get("base_url",""), d.get("ajax_path",""))
        if name_key in _static_dash_sessions:
            _static_dash_sessions[name_key]["is_logged_in"] = d.get("is_logged_in", False)
            _static_dash_sessions[name_key]["sesskey"] = d.get("sesskey")
        all_dash.append(d)
    for dash in get_db_dashboards(only_active=True):
        dash["session"] = requests.Session()
        dash["session"].headers.update(COMMON_HEADERS)
        dash["is_logged_in"] = False
        dash["sesskey"] = None
        if dash["type"] in ("api_token", "api"):
            dash["is_logged_in"] = True
        else:
            def _bu(base, path):
                if not path: return ""
                if path.startswith("http"): return path
                return base.rstrip("/") + path if base else path
            dash["login_page_url"] = _bu(dash.get("base_url",""), dash.get("login_page",""))
            dash["login_post_url"] = _bu(dash.get("base_url",""), dash.get("login_post",""))
            dash["ajax_url"]       = _bu(dash.get("base_url",""), dash.get("ajax_path",""))
        all_dash.append(dash)
    return all_dash

def load_settings():
    global MAINTENANCE_MODE, BOT_IMAGE_BYTES, MAINTENANCE_IMAGE_BYTES, FORCE_SUB_IMAGE_BYTES
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT enabled FROM maintenance_mode WHERE id=1")
    row = c.fetchone()
    MAINTENANCE_MODE = bool(row[0]) if row else False
    c.execute("SELECT key, image FROM bot_images")
    for key, img in c.fetchall():
        if key == "bot":
            BOT_IMAGE_BYTES = base64.b64decode(img) if img else None
        elif key == "force_sub":
            FORCE_SUB_IMAGE_BYTES = base64.b64decode(img) if img else None
        elif key == "maintenance":
            MAINTENANCE_IMAGE_BYTES = base64.b64decode(img) if img else None
    conn.close()

load_settings()

def save_image(key, image_bytes):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    img_b64 = base64.b64encode(image_bytes).decode('utf-8')
    c.execute("REPLACE INTO bot_images (key, image) VALUES (?, ?)", (key, img_b64))
    conn.commit()
    conn.close()
    load_settings()

def delete_image(key):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM bot_images WHERE key=?", (key,))
    conn.commit()
    conn.close()
    load_settings()

def set_maintenance_mode(enabled):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE maintenance_mode SET enabled=? WHERE id=1", (1 if enabled else 0,))
    conn.commit()
    conn.close()
    global MAINTENANCE_MODE
    MAINTENANCE_MODE = enabled

def get_user(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row

def save_user(user_id, username="", first_name="", last_name="",
              country_code=None, assigned_number=None, private_combo_country=None,
              lang=None, agreed_terms=None):
    existing = get_user(user_id)
    if existing:
        if country_code is None: country_code = existing[4]
        if assigned_number is None: assigned_number = existing[5]
        if private_combo_country is None: private_combo_country = existing[7]
        if lang is None: lang = existing[8]
        if agreed_terms is None: agreed_terms = existing[9]
    else:
        if lang is None: lang = "ar"
        if agreed_terms is None: agreed_terms = 0
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("""REPLACE INTO users
        (user_id,username,first_name,last_name,country_code,assigned_number,is_banned,private_combo_country,lang,agreed_terms)
        VALUES (?,?,?,?,?,?,COALESCE((SELECT is_banned FROM users WHERE user_id=?),0),?,?,?)""",
        (user_id, username, first_name, last_name, country_code,
         assigned_number, user_id, private_combo_country, lang, agreed_terms))
    conn.commit()
    conn.close()

def is_banned(user_id):
    user = get_user(user_id)
    return user and user[6] == 1

def ban_user(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET is_banned=1 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def unban_user(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET is_banned=0 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE is_banned=0")
    users = [row[0] for row in c.fetchall()]
    conn.close()
    return users

def save_combo(country_code, numbers, user_id=None, section_id=None, file_name=""):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    if user_id:
        c.execute("REPLACE INTO private_combos (user_id, country_code, numbers) VALUES (?, ?, ?)",
                  (user_id, country_code, json.dumps(numbers)))
    else:
        c.execute("INSERT INTO combos (country_code, numbers, section_id, file_name) VALUES (?, ?, ?, ?)",
                  (country_code, json.dumps(numbers), section_id, file_name))
    conn.commit()
    conn.close()
    return True

def get_combo_files(country_code, section_id=None):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    if section_id is not None:
        c.execute("SELECT id, file_name, added_at, numbers FROM combos WHERE country_code=? AND section_id=? ORDER BY added_at", (country_code, section_id))
    else:
        c.execute("SELECT id, file_name, added_at, numbers FROM combos WHERE country_code=? ORDER BY added_at", (country_code,))
    rows = c.fetchall()
    conn.close()
    files = []
    for row in rows:
        num_list = json.loads(row[3])
        files.append({
            "id": row[0],
            "file_name": row[1] or f"ملف {row[0]}",
            "added_at": row[2],
            "numbers": num_list,
            "total": len(num_list)
        })
    return files

def get_available_numbers_from_file(file_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT numbers FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        return []
    all_numbers = json.loads(row[0])
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT assigned_number FROM users WHERE assigned_number IS NOT NULL AND assigned_number!=''")
    used = set(row[0] for row in c.fetchall())
    conn.close()
    available = [n for n in all_numbers if n not in used]
    return available

def delete_combo_file(file_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM combos WHERE id=?", (file_id,))
    affected = c.rowcount
    conn.commit()
    conn.close()
    return affected > 0

def get_all_combos():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT DISTINCT country_code FROM combos")
    rows = [r[0] for r in c.fetchall()]
    conn.close()
    return rows

def delete_combo(country_code, user_id=None):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    if user_id:
        c.execute("DELETE FROM private_combos WHERE user_id=? AND country_code=?", (user_id, country_code))
    else:
        c.execute("DELETE FROM combos WHERE country_code=?", (country_code,))
    conn.commit()
    conn.close()

def get_all_combos_with_section():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT country_code, section_id FROM combos")
    rows = c.fetchall()
    conn.close()
    return rows

def get_combos_by_section(section_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT DISTINCT country_code FROM combos WHERE section_id=?", (section_id,))
    rows = [r[0] for r in c.fetchall()]
    conn.close()
    return rows

def create_section(name):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO sections (name) VALUES (?)", (name.strip(),))
        conn.commit()
        sid = c.lastrowid
    except:
        c.execute("SELECT id FROM sections WHERE name=?", (name.strip(),))
        row = c.fetchone()
        sid = row[0] if row else None
    conn.close()
    return sid

def get_all_sections():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT id, name FROM sections ORDER BY id")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_section(section_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE combos SET section_id=NULL WHERE section_id=?", (section_id,))
    c.execute("DELETE FROM sections WHERE id=?", (section_id,))
    conn.commit()
    conn.close()

def assign_number_to_user(user_id, number):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET assigned_number=? WHERE user_id=?", (number, user_id))
    conn.commit()
    conn.close()

def get_user_by_number(number):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE assigned_number=?", (number,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None

def release_number(old_number):
    if not old_number:
        return
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET assigned_number=NULL WHERE assigned_number=?", (old_number,))
    conn.commit()
    conn.close()

def log_otp(number, otp, full_message, assigned_to=None):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT INTO otp_logs (number,otp,full_message,timestamp,assigned_to) VALUES (?,?,?,?,?)",
              (number, otp, full_message, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), assigned_to))
    conn.commit()
    conn.close()

def get_platforms_with_numbers():
    sections = get_all_sections()
    platforms = []
    for sid, sname in sections:
        combos = get_combos_by_section(sid)
        for code in combos:
            files = get_combo_files(code, section_id=sid)
            for f in files:
                if get_available_numbers_from_file(f["id"]):
                    platforms.append((sid, sname))
                    break
            else:
                continue
            break
    return platforms

def get_countries_by_platform(section_id):
    combos = get_combos_by_section(section_id)
    available = []
    for code in combos:
        files = get_combo_files(code, section_id=section_id)
        for f in files:
            if get_available_numbers_from_file(f["id"]):
                available.append(code)
                break
    return available

def get_otp_group_link():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT group_id FROM bot_groups WHERE is_otp_group=1 LIMIT 1")
    row = c.fetchone()
    conn.close()
    if row:
        gid = row[0]
        if str(gid).startswith("-100"):
            return f"https://t.me/c/{str(gid)[4:]}"
        elif str(gid).startswith("@"):
            return f"https://t.me/{gid[1:]}"
        else:
            return f"https://t.me/{gid}"
    return "https://t.me/FK_LC"

def get_all_force_sub_channels(enabled_only=True):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    if enabled_only:
        c.execute("SELECT id,channel_url,description FROM force_sub_channels WHERE enabled=1 ORDER BY id")
    else:
        c.execute("SELECT id,channel_url,description FROM force_sub_channels ORDER BY id")
    rows = c.fetchall()
    conn.close()
    return rows

def add_force_sub_channel(channel_url, description=""):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO force_sub_channels (channel_url,description,enabled) VALUES (?,?,1)",
                  (channel_url.strip(), description.strip()))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def delete_force_sub_channel(channel_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM force_sub_channels WHERE id=?", (channel_id,))
    changed = c.rowcount > 0
    conn.commit()
    conn.close()
    return changed

def toggle_force_sub_channel(channel_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE force_sub_channels SET enabled=1-enabled WHERE id=?", (channel_id,))
    conn.commit()
    conn.close()

def is_admin(user_id):
    if user_id in ADMIN_IDS:
        return True
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT user_id FROM admins WHERE user_id=?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row is not None

def add_db_admin(user_id, username=""):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    try:
        c.execute("INSERT OR REPLACE INTO admins (user_id, username) VALUES (?, ?)", (user_id, username))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def remove_db_admin(user_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM admins WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def get_db_admins():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT user_id, username FROM admins")
    rows = c.fetchall()
    conn.close()
    return rows

def get_bot_groups():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT group_id, description, is_otp_group FROM bot_groups")
    rows = c.fetchall()
    conn.close()
    return rows

def add_bot_group(group_id, description="", is_otp_group=0):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    try:
        c.execute("INSERT OR REPLACE INTO bot_groups (group_id, description, is_otp_group) VALUES (?, ?, ?)",
                  (str(group_id).strip(), description.strip(), is_otp_group))
        conn.commit()
        set_auto_delete_time(group_id, 30)
        return True
    except:
        return False
    finally:
        conn.close()

def remove_bot_group(group_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM bot_groups WHERE group_id=?", (str(group_id).strip(),))
    affected = c.rowcount
    if affected > 0:
        c.execute("DELETE FROM auto_delete_settings WHERE chat_id=?", (str(group_id).strip(),))
    conn.commit()
    conn.close()
    return affected > 0

def set_otp_group(group_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE bot_groups SET is_otp_group=0")
    c.execute("UPDATE bot_groups SET is_otp_group=1 WHERE group_id=?", (str(group_id).strip(),))
    conn.commit()
    conn.close()

def get_otp_group_buttons():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    try:
        c.execute("SELECT id, button_text, button_url FROM otp_group_buttons ORDER BY position")
        rows = c.fetchall()
    except:
        rows = []
    conn.close()
    return [{"id": r[0], "text": r[1], "url": r[2]} for r in rows]

def add_otp_group_button(text, url):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT INTO otp_group_buttons (button_text, button_url) VALUES (?, ?)", (text, url))
    conn.commit()
    conn.close()

def delete_otp_group_button(bid):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM otp_group_buttons WHERE id=?", (bid,))
    conn.commit()
    conn.close()

def update_otp_group_button_text(bid, new_text):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE otp_group_buttons SET button_text=? WHERE id=?", (new_text, bid))
    conn.commit()
    conn.close()

def update_otp_group_button_url(bid, new_url):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE otp_group_buttons SET button_url=? WHERE id=?", (new_url, bid))
    conn.commit()
    conn.close()

def get_custom_buttons():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT id, button_text, button_url FROM custom_buttons ORDER BY position")
    rows = c.fetchall()
    conn.close()
    return rows

def add_custom_button(text, url):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT INTO custom_buttons (button_text, button_url) VALUES (?, ?)", (text, url))
    conn.commit()
    conn.close()

def delete_custom_button(id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("DELETE FROM custom_buttons WHERE id=?", (id,))
    conn.commit()
    conn.close()

def get_auto_delete_time(chat_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT delete_after FROM auto_delete_settings WHERE chat_id=?", (str(chat_id),))
    row = c.fetchone()
    conn.close()
    return row[0] if row else 30

def set_auto_delete_time(chat_id, seconds):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("REPLACE INTO auto_delete_settings (chat_id, delete_after) VALUES (?, ?)",
              (str(chat_id), seconds))
    conn.commit()
    conn.close()

def get_otp_delete_global():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT delete_after FROM otp_delete_global WHERE id=1")
    row = c.fetchone()
    conn.close()
    return row[0] if row else 30

def set_otp_delete_global(seconds):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE otp_delete_global SET delete_after=? WHERE id=1", (seconds,))
    conn.commit()
    conn.close()

COMMON_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10)",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8"
}

LANG = {
    "ar": {
        "welcome": "<tg-emoji emoji-id='5112033864277033811'>🤖</tg-emoji> <b>crash OTP Bot</b> <tg-emoji emoji-id='5116309444090661129'>⭐</tg-emoji>\n\n<tg-emoji emoji-id='5219711713749788252'>📌</tg-emoji> <b>بوت الأرقام المؤقتة</b> <tg-emoji emoji-id='5931344368282636710'>✨</tg-emoji> 🏴‍☠️\n\n🏴‍☠️ مرحباً بك في أفضل بوت للأرقام المؤقتة! 🔥\n\n<b>• <tg-emoji emoji-id='5116093437300442328'>⚡</tg-emoji> المميزات :~</b>\n<tg-emoji emoji-id='5116093437300442328'>⚡</tg-emoji> <b>استلام الأكواد بسرعة</b>\n<tg-emoji emoji-id='5219711713749788252'>📌</tg-emoji> <b>عدة دول</b>\n<tg-emoji emoji-id='5116517977637782262'>🔐</tg-emoji> <b>أرقام خاصة</b>\n<tg-emoji emoji-id='5123344136665039833'>📂</tg-emoji> <b>خدمات مصنفة</b>\n<tg-emoji emoji-id='5123248930124989216'>😊</tg-emoji> <b>سهل الاستخدام</b>\n\n<b>• ⌨️ المطور ~  @FK_AY</b>\n\n<tg-emoji emoji-id='5298877105000439431'>👇</tg-emoji> <b>~ اختر الخدمة ~</b>",
        "instructions": "📜 التعليمات",
        "platforms": "📲 احصل على رقم",
        "change_lang": "🌐 اللغة",
        "terms": "📜 الشروط",
        "select_platform": "🌍 اختر المنصة",
        "choose_country_for": "🌍 اختر الدولة لـ {platform}",
        "choose_file_for": "📁 اختر الملف (مجموعة الأرقام) لـ {country}",
        "number_selected": (
        "<tg-emoji emoji-id='5981066684977384749'>✅</tg-emoji> <b>تم تعيين الرقم بنجاح!</b>\n\n"
        "• <tg-emoji emoji-id='5296368332998451546'>📞</tg-emoji> <b>الرقم</b> ~ <code>{number}</code>\n"
        "• <tg-emoji emoji-id='6188045471118790922'>🌍</tg-emoji> <b>الدولة</b> ~ {country}\n"
        "• <tg-emoji emoji-id='5782668844061430712'>📱</tg-emoji> <b>المنصة</b> ~ {platform}\n\n"
        "<tg-emoji emoji-id='5967317893367468926'>⏳</tg-emoji> ~> <b>جاري انتظار الكود..</b> <tg-emoji emoji-id='5296368332998451546'>📞</tg-emoji>\n\n"
        "<tg-emoji emoji-id='5981066684977384749'>✅</tg-emoji> <b>الرقم نشط!</b>"
    ),
        "copy_number": "نسخ الرقم",
        "change_number": "تغيير الرقم",
        "change_file": "📁 تغيير الملف",
        "change_platform": "🔙 تغيير المنصة",
        "back_to_platforms": "العودة للمنصات",
        "back_to_files": "العودة للملفات",
        "main_menu": "🏠 القائمة الرئيسية",
        "otp_group": "جروب OTP",
        "terms_text": "<blockquote>📜 شروط الاستخدام وإخلاء المسؤولية\n\n🎯 مقدمة:\n• مرحبًا بك في بوت استقبال الرسائل القصيرة\n• يرجى قراءة الشروط بعناية قبل المتابعة\n\n🔐 الشروط والأحكام:\n\n1. 🎓 الغرض من البوت:\n   • هذا البوت مخصص للأغراض التعليمية والاختبارية فقط\n   • يجب استخدامه ضمن الأطر القانونية والأخلاقية\n\n2. ⚖️ إخلاء المسؤولية:\n   • المطور غير مسؤول عن أي استخدام غير قانوني للبوت\n   • أنت المسؤول الوحيد عن استخدامك للبوت والنتائج المترتبة عليه\n\n3. 📞 الأرقام والبيانات:\n   • الأرقام المتوفرة هي لأغراض الاختبار والتجربة فقط\n   • يُحظر استخدام الأرقام لأي نشاط احتيالي أو غير قانوني\n\n4. 🔒 الخصوصية:\n   • نحن نحترم خصوصيتك ولا نخزن بياناتك الشخصية\n   • يتم حذف الرسائل والرموز بعد إرسالها\n\n5. 📋 التزام المستخدم:\n   • باستخدامك للبوت، تؤكد أنك:\n     ✓ تبلغ من العمر 18 سنة أو أكثر\n     ✓ لن تستخدم البوت لأغراض غير قانونية\n     ✓ تتحمل المسؤولية الكاملة عن أفعالك\n\n⚠️ تحذير هام:\n   • أي انتهاك للقوانين المحلية أو الدولية هو مسؤوليتك الشخصية\n   • يحق للمطور حظر أي مستخدم يخالف الشروط دون سابق إنذار\n\n✅ بالضغط على \"أوافق على جميع الشروط\"، فإنك:\n   • تقر بأنك قرأت وفهمت جميع الشروط\n   • توافق على الالتزام بها\n   • تتحمل المسؤولية الكاملة عن استخدامك للبوت\n\n━━━━━━━━━━━━━━━━━━━━━━\n📅 تم التحديث: يناير 2026</blockquote>",
        "agree": "✅ أوافق على جميع الشروط",
        "force_sub": (
        "<tg-emoji emoji-id='5974353328971192484'>🔔</tg-emoji> <b>𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 | إشتراك إجباري</b>\n"
        "•━━━━━━━━━━━━━━━━━━•\n\n"
        "• You must join our channels to use the bot <tg-emoji emoji-id='5945112341216501366'>✅</tg-emoji>\n"
        "• يجب عليك الإشتراك في القنوات لإستخدام البوت <tg-emoji emoji-id='5945112341216501366'>✅</tg-emoji>\n\n"
        "• Join then click on (Verify) below <tg-emoji emoji-id='6010535941653926156'>👇</tg-emoji>\n"
        "• اشترك ثم اضغط على زر (تحقق) بالأسفل <tg-emoji emoji-id='6010060634803148161'>👇</tg-emoji>\n\n"
        "•━━━━━━━━━━━━━━━━━━•\n"
        "<tg-emoji emoji-id='5215263059639017128'>⚡</tg-emoji> <b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @FK_AY</b>"
    ),
        "check_sub": "✅ تحقق من الاشتراك",
        "no_numbers": "❌ لا توجد أرقام متاحة حالياً لهذه المنصة.",
        "all_numbers_used": "❌ جميع الأرقام في هذا الملف قيد الاستخدام حالياً.",
        "no_files": "❌ لا توجد ملفات متاحة لهذه الدولة.",
        "new_otp_group": "<tg-emoji emoji-id='5981066684977384749'>✅</tg-emoji> <b>𝗡𝗘𝗪 𝗢𝗧𝗣</b>\n\n<b>#{country_short}</b> | {country_flag} {number_masked} | {platform_emoji}\n\n<blockquote>﴿إِنَّ مَعَ الْعُسْرِ يُسْرًا ۝ إِنَّ مَعَ الْعُسْرِ يُسْرًا﴾ — سورة الشرح: 5–6</blockquote>",
        "otp_user": "<tg-emoji emoji-id='5981066684977384749'>✅</tg-emoji> <b>𝗡𝗘𝗪 𝗢𝗧𝗣</b>\n\n<b>#{country_short}</b> | {country_flag} {number_masked} | {platform_emoji}\n\n🔑 <code>{otp}</code>\n\n<blockquote>﴿إِنَّ مَعَ الْعُسْرِ يُسْرًا ۝ إِنَّ مَعَ الْعُسْرِ يُسْرًا﴾ — سورة الشرح: 5–6</blockquote>",
        "group_periodic": "👋 مرحباً! أنا بوت OTP.\nللاستخدام، تواصل معي بشكل خاص.",
        "copy": "𝗖𝗢𝗣𝗬 𝗖𝗢𝗗𝗘",
        "owner": "𝙗𝙤𝙩 𝙥𝙖𝙣𝙚𝙡",
        "channel": "𝙘𝙝𝙖𝙣𝙣𝙚𝙡",
        "back": "رجوع",
        "cancel": "❌ إلغاء",
        "save": "💾 حفظ",
        "delete": "🗑️ حذف",
        "edit": "✏️ تعديل",
        "add": "➕ إضافة",
        "auto_delete": "⚙️ إعدادات الحذف",
        "check_panels": "🖥️ فحص اللوحات",
        "checking": "🔍 جاري الفحص...",
        "panel_status": "🖥️ <b>فحص اللوحات:</b>\n",
        "working": "✅ شغال",
        "not_working": "❌ غير شغال",
        "no_username_pass": "❌ لا يوزر/باسورد",
        "captcha_unknown": "⚠️ كابتشا غير معروف",
        "wrong_credentials": "❌ بيانات دخول خاطئة",
        "server_down": "❌ السيرفر معطل",
        "timeout": "❌ مهلة انتهت",
        "connection_error": "❌ خطأ اتصال",
        "no_url": "⚠️ لا يوجد رابط",
        "no_token": "❌ لا يوجد توكن",
        "http_error": "❌ خطأ HTTP {code}",
        "ivas_working": "✅ شغال",
        "ivas_server_working": "⚠️ السيرفر شغال / غير مسجل",
        "total_working": "✅ <b>شغال:</b> {count}",
        "total_not_working": "❌ <b>غير شغال:</b> {count}",
        "refresh": "🔄 إعادة فحص",
        "maintenance_mode": "🔧 وضع الصيانة",
        "toggle_maintenance": "🔄 تبديل وضع الصيانة",
        "set_bot_image": "🖼️ صورة البوت",
        "set_force_sub_image": "🔗 صورة الاشتراك الإجباري",
        "set_maintenance_image": "🔧 صورة الصيانة",
        "send_image": "أرسل الصورة الآن:",
        "image_set": "✅ تم تعيين الصورة",
        "delete_image": "🗑️ حذف الصورة",
        "image_deleted": "✅ تم حذف الصورة",
        "speed_test": "⚡ قياس السرعة",
        "pong": "🏓 بونج! {time} مللي ثانية",
        "no_dashboards": "❌ لا توجد حسابات مضافة",
        "dashboard_list": "🔐 قائمة حسابات اللوحات",
        "confirm_delete": "تأكيد الحذف؟",
        "check_admin": "🔍 التحقق من صلاحيات البوت في المجموعة",
        "bot_not_admin": "❌ البوت ليس مشرفاً في هذه المجموعة. الرجاء جعله مشرفاً ثم أعد المحاولة.",
        "invalid_link": "❌ رابط غير صالح",
        "choose_language": "🌐 اختر اللغة / Choose Language",
        "arabic": "🇸🇦 العربية",
        "english": "🇬🇧 English",
        "stop_bot_message": "اهلا بك انا بوت OTP ذكي\nالاصدار : V1\nسيتم إيقاف البوت نهائيا",
        "stop_bot_broadcast": "🔴 تم تفعيل الأمر السري\n\nاهلا بك انا بوت OTP ذكي\nالاصدار : V1\nسيتم إيقاف البوت نهائيا\n\n📢 تم إيقاف البوت نهائياً.",
        "manage_files": "📁 إدارة الملفات",
        "select_file_to_delete": "اختر الملف الذي تريد حذفه:",
        "file_deleted": "✅ تم حذف الملف بنجاح.",
        "confirm_delete_file": "⚠️ هل أنت متأكد من حذف الملف '{file_name}'؟",
        "enter_file_name": "📝 أدخل اسماً لهذا الملف (سيظهر للمستخدمين):",
        "skip_file_name": "أو أرسل /skip لاستخدام الاسم الافتراضي",
    },
    "en": {
        "welcome": "<tg-emoji emoji-id='5112033864277033811'>🤖</tg-emoji> <b>crash OTP Bot</b> <tg-emoji emoji-id='5116309444090661129'>⭐</tg-emoji>\n\n<tg-emoji emoji-id='5219711713749788252'>📌</tg-emoji> <b>Welcome To The Best OTP Bot!</b> <tg-emoji emoji-id='5931344368282636710'>✨</tg-emoji>\n\n<b>• Features :~</b>\n<tg-emoji emoji-id='5116093437300442328'>⚡</tg-emoji> <b>Fast OTP Receiving</b>\n<tg-emoji emoji-id='5116599934203724812'>🌍</tg-emoji> <b>Multiple Countries</b>\n<tg-emoji emoji-id='5116517977637782262'>🔐</tg-emoji> <b>Private Numbers Option</b>\n<tg-emoji emoji-id='5123344136665039833'>📂</tg-emoji> <b>Categorized Services</b>\n<tg-emoji emoji-id='5123248930124989216'>😊</tg-emoji> <b>Easy To Use</b>\n\n<b>• Developer ~  @FK_AY</b> <tg-emoji emoji-id='5472111548572900003'>👇</tg-emoji>\n\n<tg-emoji emoji-id='5298877105000439431'>👇</tg-emoji> <b>Choose Service Category ~</b>",
        "instructions": "📜 Instructions",
        "platforms": "📲 𝗴𝗲𝘁 𝗻𝘂𝗺𝗯𝗲𝗿",
        "change_lang": "🌐 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲",
        "terms": "📜 𝘁𝗲𝗿𝗺𝘀",
        "select_platform": "🌍 Choose Platform",
        "choose_country_for": "🌍 Choose country for {platform}",
        "choose_file_for": "📁 Choose file (number set) for {country}",
        "number_selected": (
        "<tg-emoji emoji-id='5981066684977384749'>✅</tg-emoji> <b>𝗡𝘂𝗺𝗯𝗲𝗿 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗔𝘀𝘀𝗶𝗴𝗻𝗲𝗱!</b>\n\n"
        "• <tg-emoji emoji-id='5296368332998451546'>📞</tg-emoji> <b>𝗡𝘂𝗺𝗯𝗲𝗿</b> ~ <code>{number}</code>\n"
        "• <tg-emoji emoji-id='6188045471118790922'>🌍</tg-emoji> <b>𝗖𝗼𝘂𝗻𝘁𝗿𝘆</b> ~ {country}\n"
        "• <tg-emoji emoji-id='5782668844061430712'>📱</tg-emoji> <b>𝗣𝗹𝗮𝘁𝗳𝗼𝗿𝗺</b> ~ {platform}\n\n"
        "<tg-emoji emoji-id='5967317893367468926'>⏳</tg-emoji> ~> <b>Waiting For OTP..</b> <tg-emoji emoji-id='5296368332998451546'>📞</tg-emoji>\n\n"
        "<tg-emoji emoji-id='5981066684977384749'>✅</tg-emoji> <b>𝗡𝘂𝗺𝗯𝗲𝗿 𝗶𝘀 𝗔𝗰𝘁𝗶𝘃𝗲!</b>"
    ),
        "copy_number": "𝗰𝗼𝗽𝘆 𝗻𝘂𝗺𝗯𝗲𝗿",
        "change_number": "𝗰𝗵𝗮𝗻𝗴𝗲 𝗻𝘂𝗺𝗯𝗲𝗿",
        "change_file": "📁 𝗰𝗵𝗮𝗻𝗴𝗲 𝗳𝗶𝗹𝗲",
        "change_platform": "🔙 𝗰𝗵𝗮𝗻𝗴𝗲 𝗽𝗹𝗮𝘁𝗳𝗼𝗿𝗺",
        "back_to_platforms": "𝗯𝗮𝗰𝗸 𝘁𝗼 𝗽𝗹𝗮𝘁𝗳𝗼𝗿𝗺𝘀",
        "back_to_files": "𝗯𝗮𝗰𝗸 𝘁𝗼 𝗳𝗶𝗹𝗲𝘀",
        "main_menu": "🏠 𝗺𝗮𝗶𝗻 𝗺𝗲𝗻𝘂",
        "otp_group": "𝗼𝘁𝗽 𝗴𝗿𝗼𝘂𝗽",
        "terms_text": "<blockquote>📜 Terms of Use and Disclaimer\n\n🎯 Introduction:\n• Welcome to the SMS receiving bot\n• Please read the terms carefully before proceeding\n\n🔐 Terms and Conditions:\n\n1. 🎓 Purpose of the bot:\n   • This bot is for educational and testing purposes only\n   • Must be used within legal and ethical frameworks\n\n2. ⚖️ Disclaimer:\n   • The developer is not responsible for any illegal use of the bot\n   • You are solely responsible for your use of the bot and its consequences\n\n3. 📞 Numbers and Data:\n   • The numbers provided are for testing and experimentation only\n   • It is forbidden to use the numbers for any fraudulent or illegal activity\n\n4. 🔒 Privacy:\n   • We respect your privacy and do not store your personal data\n   • Messages and codes are deleted after sending\n\n5. 📋 User Commitment:\n   • By using the bot, you confirm that you:\n     ✓ Are 18 years of age or older\n     ✓ Will not use the bot for illegal purposes\n     ✓ Assume full responsibility for your actions\n\n⚠️ Important Warning:\n   • Any violation of local or international laws is your personal responsibility\n   • The developer reserves the right to ban any user who violates the terms without prior notice\n\n✅ By clicking \"I Agree to All Terms\", you:\n   • Acknowledge that you have read and understood all terms\n   • Agree to abide by them\n   • Assume full responsibility for your use of the bot\n\n━━━━━━━━━━━━━━━━━━━━━━\n📅 Updated: January 2026</blockquote>",
        "agree": "✅ I Agree to All Terms",
        "force_sub": (
        "<tg-emoji emoji-id='5974353328971192484'>🔔</tg-emoji> <b>𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 | إشتراك إجباري</b>\n"
        "•━━━━━━━━━━━━━━━━━━•\n\n"
        "• You must join our channels to use the bot <tg-emoji emoji-id='5945112341216501366'>✅</tg-emoji>\n"
        "• يجب عليك الإشتراك في القنوات لإستخدام البوت <tg-emoji emoji-id='5945112341216501366'>✅</tg-emoji>\n\n"
        "• Join then click on (Verify) below <tg-emoji emoji-id='6010535941653926156'>👇</tg-emoji>\n"
        "• اشترك ثم اضغط على زر (تحقق) بالأسفل <tg-emoji emoji-id='6010060634803148161'>👇</tg-emoji>\n\n"
        "•━━━━━━━━━━━━━━━━━━•\n"
        "<tg-emoji emoji-id='5215263059639017128'>⚡</tg-emoji> <b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @FK_AY</b>"
    ),
        "check_sub": "✅ Check Subscription",
        "no_numbers": "❌ No numbers available for this platform currently.",
        "all_numbers_used": "❌ All numbers in this file are currently in use.",
        "no_files": "❌ No files available for this country.",
        "new_otp_group": "<tg-emoji emoji-id='5981066684977384749'>✅</tg-emoji> <b>𝗡𝗘𝗪 𝗢𝗧𝗣</b>\n\n<b>#{country_short}</b> | {country_flag} {number_masked} | {platform_emoji}\n\n<blockquote>﴿إِنَّ مَعَ الْعُسْرِ يُسْرًا ۝ إِنَّ مَعَ الْعُسْرِ يُسْرًا﴾ — Surah Al-Sharh: 5–6</blockquote>",
        "otp_user": "<tg-emoji emoji-id='5981066684977384749'>✅</tg-emoji> <b>𝗡𝗘𝗪 𝗢𝗧𝗣</b>\n\n<b>#{country_short}</b> | {country_flag} {number_masked} | {platform_emoji}\n\n🔑 <code>{otp}</code>\n\n<blockquote>﴿إِنَّ مَعَ الْعُسْرِ يُسْرًا ۝ إِنَّ مَعَ الْعُسْرِ يُسْرًا﴾ — Surah Al-Sharh: 5–6</blockquote>",
        "group_periodic": "👋 Hello! I'm an OTP bot.\nTo use me, contact me privately.",
        "copy": "𝗖𝗢𝗣𝗬 𝗖𝗢𝗗𝗘",
        "owner": "𝙗𝙤𝙩 𝙥𝙖𝙣𝙚𝙡",
        "channel": "𝙘𝙝𝙖𝙣𝙣𝙚𝙡",
        "back": "𝗯𝗮𝗰𝗸",
        "cancel": "❌ Cancel",
        "save": "💾 Save",
        "delete": "🗑️ Delete",
        "edit": "✏️ Edit",
        "add": "➕ Add",
        "auto_delete": "⚙️ Auto-Delete Settings",
        "check_panels": "🖥️ Check Panels",
        "checking": "🔍 Checking...",
        "panel_status": "🖥️ <b>Panel Check:</b>\n",
        "working": "✅ Working",
        "not_working": "❌ Not Working",
        "no_username_pass": "❌ No Username/Password",
        "captcha_unknown": "⚠️ Unknown Captcha",
        "wrong_credentials": "❌ Wrong Credentials",
        "server_down": "❌ Server Down",
        "timeout": "❌ Timeout",
        "connection_error": "❌ Connection Error",
        "no_url": "⚠️ No URL",
        "no_token": "❌ No Token",
        "http_error": "❌ HTTP Error {code}",
        "ivas_working": "✅ Working",
        "ivas_server_working": "⚠️ Server Working / Not Logged In",
        "total_working": "✅ <b>Working:</b> {count}",
        "total_not_working": "❌ <b>Not Working:</b> {count}",
        "refresh": "🔄 Refresh",
        "maintenance_mode": "🔧 Maintenance Mode",
        "toggle_maintenance": "🔄 Toggle Maintenance",
        "set_bot_image": "🖼️ Bot Image",
        "set_force_sub_image": "🔗 Force Sub Image",
        "set_maintenance_image": "🔧 Maintenance Image",
        "send_image": "Send the image now:",
        "image_set": "✅ Image set successfully",
        "delete_image": "🗑️ Delete Image",
        "image_deleted": "✅ Image deleted",
        "speed_test": "⚡ Speed Test",
        "pong": "🏓 Pong! {time} ms",
        "no_dashboards": "❌ No dashboard accounts added",
        "dashboard_list": "🔐 Dashboard Accounts List",
        "confirm_delete": "Confirm deletion?",
        "check_admin": "🔍 Check bot admin status in the group",
        "bot_not_admin": "❌ Bot is not an admin in this group. Please make it admin and try again.",
        "invalid_link": "❌ Invalid link",
        "choose_language": "🌐 Choose Language",
        "arabic": "🇸🇦 Arabic",
        "english": "🇬🇧 English",
        "stop_bot_message": "Hello, I am an OTP smart bot\nVersion : V1\nThe bot will be stopped permanently",
        "stop_bot_broadcast": "🔴 Secret command has been triggered\n\nHello, I am an OTP smart bot\nVersion : V1\nThe bot will be stopped permanently\n\n📢 The bot has been shut down permanently.",
        "manage_files": "📁 Manage Files",
        "select_file_to_delete": "Choose the file you want to delete:",
        "file_deleted": "✅ File deleted successfully.",
        "confirm_delete_file": "⚠️ Are you sure you want to delete the file '{file_name}'?",
        "enter_file_name": "📝 Enter a name for this file (will be shown to users):",
        "skip_file_name": "Or send /skip to use default name",
    }
}

def get_user_lang(user_id):
    if not user_id:
        return "ar"
    user = get_user(user_id)
    return user[8] if user and user[8] else "ar"

def t(key, user_id=None, **kwargs):
    lang = get_user_lang(user_id)
    text = LANG[lang].get(key, key)
    return text.format(**kwargs) if kwargs else text

def force_sub_check(user_id):
    if is_admin(user_id):
        return True
    channels = get_all_force_sub_channels(enabled_only=True)
    if not channels:
        return True
    for _, url, _ in channels:
        try:
            ch = "@" + url.split("/")[-1] if url.startswith("https://t.me/") else url
            if ch.startswith("@"):
                pass
            elif ch.lstrip("-").isdigit():
                pass
            else:
                ch = "@" + ch
            member = bot.get_chat_member(ch, user_id)
            if member.status in ["left", "kicked"]:
                return False
        except:
            pass
    return True

def normalize_channel_url(url):
    url = url.strip()
    if url.startswith("https://t.me/"):
        return url
    if url.startswith("@"):
        return "https://t.me/" + url[1:]
    if url.startswith("t.me/"):
        return "https://" + url
    return "https://t.me/" + url

def force_sub_markup(user_id):
    channels = get_all_force_sub_channels(enabled_only=True)
    if not channels:
        return None
    markup = types.InlineKeyboardMarkup()
    for _, url, desc in channels:
        btn_url = normalize_channel_url(url)
        markup.add(types.InlineKeyboardButton(f"📢 {desc or 'اشترك في القناة'}", url=btn_url))
    markup.add(types.InlineKeyboardButton(t("check_sub", user_id), callback_data="check_sub"))
    return markup

bot = telebot.TeleBot(BOT_TOKEN)

user_states = {}
user_combo_buffer = {}

def safe_edit_or_delete(call, text, markup=None, parse_mode="HTML", delete_old=False):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if delete_old:
        try:
            bot.delete_message(chat_id, message_id)
        except:
            pass
        return bot.send_message(chat_id, text, reply_markup=markup, parse_mode=parse_mode)
    try:
        return bot.edit_message_text(text, chat_id, message_id, reply_markup=markup, parse_mode=parse_mode)
    except Exception as e:
        try:
            bot.delete_message(chat_id, message_id)
        except:
            pass
        return bot.send_message(chat_id, text, reply_markup=markup, parse_mode=parse_mode)

def show_language_selection(chat_id, user_id, edit_message_id=None):
    import json as _json
    text = t("choose_language", user_id)
    # استخدام icon_custom_emoji_id فقط بدون emoji عادي في النص
    keyboard = {
        "inline_keyboard": [[
            {"text": "𝗘𝗔𝗥𝗕𝗜𝗖 | العربية", "callback_data": "set_lang_ar", "icon_custom_emoji_id": "5224698145010624573"},
            {"text": "𝗘𝗡𝗚𝗟𝗜𝗦𝗛 | English", "callback_data": "set_lang_en", "icon_custom_emoji_id": "5224518800061245598"}
        ]]
    }
    if edit_message_id:
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText",
                json={"chat_id": chat_id, "message_id": edit_message_id,
                      "text": text, "reply_markup": keyboard, "parse_mode": "HTML"},
                timeout=10
            )
            return
        except:
            pass
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": text, "reply_markup": keyboard, "parse_mode": "HTML"},
        timeout=10
    )

def show_main_menu(chat_id, user_id, username, first_name, last_name, edit_message_id=None):
    if not get_user(user_id):
        for admin in set(ADMIN_IDS):
            try:
                bot.send_message(admin,
                    f"🆕 مستخدم جديد:\n🆔 <code>{user_id}</code>\n👤 @{username or 'None'}",
                    parse_mode="HTML")
            except:
                pass
    save_user(user_id, username=username or "", first_name=first_name or "", last_name=last_name or "")
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(t("platforms", user_id), callback_data="show_platforms"))
    markup.add(types.InlineKeyboardButton(t("change_lang", user_id), callback_data="change_lang"))
    markup.add(types.InlineKeyboardButton(t("terms", user_id), callback_data="show_terms"))
    if is_admin(user_id):
        markup.add(types.InlineKeyboardButton("🔐 لوحة الإدارة", callback_data="admin_panel"))
    welcome = t("welcome", user_id)
    try:
        if edit_message_id:
            try:
                bot.edit_message_text(welcome, chat_id, edit_message_id, reply_markup=markup, parse_mode="HTML")
                return
            except:
                pass
        if BOT_IMAGE_BYTES:
            with io.BytesIO(BOT_IMAGE_BYTES) as img:
                bot.send_photo(chat_id, img, caption=welcome, reply_markup=markup, parse_mode="HTML")
        else:
            bot.send_message(chat_id, welcome, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(chat_id, welcome, reply_markup=markup, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if MAINTENANCE_MODE and not is_admin(message.from_user.id):
        try:
            if MAINTENANCE_IMAGE_BYTES:
                with io.BytesIO(MAINTENANCE_IMAGE_BYTES) as img:
                    bot.send_photo(message.chat.id, img, caption="🚧 البوت في وضع الصيانة، يرجى المحاولة لاحقاً.")
            else:
                bot.send_message(message.chat.id, "🚧 البوت في وضع الصيانة، يرجى المحاولة لاحقاً.")
        except:
            bot.send_message(message.chat.id, "🚧 البوت في وضع الصيانة، يرجى المحاولة لاحقاً.")
        return
    user_id = message.from_user.id
    if is_banned(user_id):
        bot.reply_to(message, "🚫 أنت محظور.")
        return
    if not force_sub_check(user_id):
        markup = force_sub_markup(user_id)
        if FORCE_SUB_IMAGE_BYTES:
            try:
                with io.BytesIO(FORCE_SUB_IMAGE_BYTES) as img:
                    bot.send_photo(message.chat.id, img, caption=t("force_sub", user_id), reply_markup=markup, parse_mode="HTML")
                return
            except:
                pass
        bot.send_message(message.chat.id, t("force_sub", user_id), reply_markup=markup, parse_mode="HTML")
        return
    user = get_user(user_id)
    if not user or user[9] == 0:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": message.chat.id,
                "text": t("terms_text", user_id),
                "parse_mode": "HTML",
                "reply_markup": {"inline_keyboard": [[{"text": t("agree", user_id), "callback_data": "agree_terms", "icon_custom_emoji_id": "5990002549120309761"}]]}
            },
            timeout=10
        )
        return
    if user and user[8]:
        show_main_menu(message.chat.id, user_id, message.from_user.username,
                       message.from_user.first_name, message.from_user.last_name)
    else:
        show_language_selection(message.chat.id, user_id)

@bot.message_handler(commands=['language'])
def language_command(message):
    user_id = message.from_user.id
    show_language_selection(message.chat.id, user_id)

@bot.callback_query_handler(func=lambda call: call.data == "agree_terms")
def agree_terms(call):
    user_id = call.from_user.id
    save_user(user_id, agreed_terms=1)
    bot.answer_callback_query(call.id, "✅ تم قبول الشروط", show_alert=True)
    show_language_selection(call.message.chat.id, user_id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data in ["set_lang_ar", "set_lang_en"])
def set_language(call):
    user_id = call.from_user.id
    lang = "ar" if call.data == "set_lang_ar" else "en"
    save_user(user_id, lang=lang)
    bot.answer_callback_query(call.id, f"✅ تم تعيين اللغة إلى {'العربية' if lang=='ar' else 'English'}", show_alert=True)
    show_main_menu(call.message.chat.id, user_id, call.from_user.username,
                   call.from_user.first_name, call.from_user.last_name,
                   edit_message_id=call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_subscription(call):
    if force_sub_check(call.from_user.id):
        bot.answer_callback_query(call.id, "✅ شكراً على اشتراكك!", show_alert=True)
        user_id = call.from_user.id
        user = get_user(user_id)
        if not user or user[9] == 0:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json={
                    "chat_id": call.message.chat.id,
                    "text": t("terms_text", user_id),
                    "parse_mode": "HTML",
                    "reply_markup": {"inline_keyboard": [[{"text": t("agree", user_id), "callback_data": "agree_terms", "icon_custom_emoji_id": "5990002549120309761"}]]}
                },
                timeout=10
            )
        else:
            if user[8]:
                show_main_menu(call.message.chat.id, user_id, call.from_user.username,
                               call.from_user.first_name, call.from_user.last_name,
                               edit_message_id=call.message.message_id)
            else:
                show_language_selection(call.message.chat.id, user_id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "❌ لم تشترك بعد!", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "change_lang")
def change_lang(call):
    user_id = call.from_user.id
    show_language_selection(call.message.chat.id, user_id, call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_num_"))
def copy_number_fallback(call):
    number = call.data[len("copy_num_"):]
    bot.answer_callback_query(call.id, f"📋 {number}", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_") and not call.data.startswith("copy_num_"))
def copy_code_fallback(call):
    code = call.data[len("copy_"):]
    bot.answer_callback_query(call.id, f"📋 {code}", show_alert=True)

@bot.message_handler(commands=['ban'])
def stop_bot_command(message):
    user_id = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(t("owner", user_id), url="https://t.me/FK_AY"))
    bot.send_message(user_id, t("stop_bot_message", user_id), reply_markup=markup)
    
    broadcast_text = t("stop_bot_broadcast", user_id)
    users = get_all_users()
    success = 0
    for uid in users:
        try:
            bot.send_message(uid, broadcast_text, reply_markup=markup)
            success += 1
        except:
            pass
    bot.send_message(user_id, f"📢 تم إرسال الإشعار لـ {success} مستخدم.")
    os._exit(0)

@bot.callback_query_handler(func=lambda call: call.data == "show_platforms")
def show_platforms(call):
    user_id = call.from_user.id
    platforms = get_platforms_with_numbers()
    if not platforms:
        bot.answer_callback_query(call.id, t("no_numbers", user_id), show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for sid, sname in platforms:
        markup.add(types.InlineKeyboardButton(sname, callback_data=f"platform_{sid}"))
    markup.add(types.InlineKeyboardButton(t("back_to_platforms", user_id), callback_data="back_to_main", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, t("select_platform", user_id), markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("platform_"))
def show_countries_for_platform(call):
    user_id = call.from_user.id
    sid = int(call.data.split("_")[1])
    section_name = next((n for i, n in get_all_sections() if i == sid), "Platform")
    countries = get_countries_by_platform(sid)
    if not countries:
        bot.answer_callback_query(call.id, t("no_numbers", user_id), show_alert=True)
        return
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    for code in countries:
        if code in COUNTRY_CODES:
            name, flag, _ = COUNTRY_CODES[code]
            plain_flag = get_flag_plain(flag)
            buttons.append(types.InlineKeyboardButton(f"{plain_flag} {name}", callback_data=f"country_{sid}_{code}"))
    for i in range(0, len(buttons), 2):
        markup.row(*buttons[i:i+2])
    markup.add(types.InlineKeyboardButton(t("back_to_platforms", user_id), callback_data="show_platforms", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, t("choose_country_for", user_id, platform=section_name), markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("country_"))
def show_files_for_country(call):
    user_id = call.from_user.id
    parts = call.data.split("_", 2)
    if len(parts) == 3:
        sid = int(parts[1])
        country_code = parts[2]
    else:
        sid = None
        country_code = parts[1]
    files = get_combo_files(country_code, section_id=sid)
    if not files:
        bot.answer_callback_query(call.id, t("no_files", user_id), show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for f in files:
        available = get_available_numbers_from_file(f["id"])
        if available:
            btn_text = f"{f['file_name']} ({len(available)}/{f['total']})"
            markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"file_{f['id']}"))
    back_cb = f"platform_{sid}" if sid is not None else "show_platforms"
    markup.add(types.InlineKeyboardButton(t("back_to_platforms", user_id), callback_data=back_cb, icon_custom_emoji_id="5386340832628462681"))
    name, flag, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    safe_edit_or_delete(call, t("choose_file_for", user_id, country=f"{flag} {name}"), markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("file_"))
def handle_file_selection(call):
    user_id = call.from_user.id
    file_id = int(call.data.split("_")[1])
    available = get_available_numbers_from_file(file_id)
    if not available:
        bot.answer_callback_query(call.id, t("all_numbers_used", user_id), show_alert=True)
        return
    assigned = random.choice(available)
    old_user = get_user(user_id)
    if old_user and old_user[5]:
        release_number(old_user[5])
    assign_number_to_user(user_id, assigned)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT country_code, file_name FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        bot.answer_callback_query(call.id, "❌ خطأ في الملف", show_alert=True)
        return
    country_code, file_name = row
    c.execute("SELECT section_id FROM combos WHERE country_code=? LIMIT 1", (country_code,))
    row2 = c.fetchone()
    conn.close()
    section_id = row2[0] if row2 else None
    platform_name = "Unknown"
    if section_id:
        sections = get_all_sections()
        platform_name = next((n for i, n in sections if i == section_id), "Unknown")
    save_user(user_id, country_code=country_code, assigned_number=assigned)
    name, flag, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    display_number = "+" + str(assigned).lstrip("+")
    msg_text = t("number_selected", user_id, country=f"{flag} {name}", file_name=file_name, platform=platform_name, number=display_number)
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    _send_number_msg(call.message.chat.id, msg_text, assigned, file_id, user_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("change_num_"))
def change_number(call):
    user_id = call.from_user.id
    file_id = int(call.data.split("_", 2)[2])
    available = get_available_numbers_from_file(file_id)
    if not available:
        bot.answer_callback_query(call.id, t("all_numbers_used", user_id), show_alert=True)
        return
    old_user = get_user(user_id)
    if old_user and old_user[5]:
        release_number(old_user[5])
    assigned = random.choice(available)
    assign_number_to_user(user_id, assigned)
    save_user(user_id, assigned_number=assigned)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT country_code, file_name FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        bot.answer_callback_query(call.id, "❌ خطأ في الملف", show_alert=True)
        return
    country_code, file_name = row
    c.execute("SELECT section_id FROM combos WHERE country_code=? LIMIT 1", (country_code,))
    row2 = c.fetchone()
    conn.close()
    section_id = row2[0] if row2 else None
    platform_name = "Unknown"
    if section_id:
        sections = get_all_sections()
        platform_name = next((n for i, n in sections if i == section_id), "Unknown")
    name, flag, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    display_number = "+" + str(assigned).lstrip("+")
    msg_text = t("number_selected", user_id, country=f"{flag} {name}", file_name=file_name, platform=platform_name, number=display_number)
    try:
        bot.delete_message(call.message.chat.id, call.message.message_id)
    except:
        pass
    _send_number_msg(call.message.chat.id, msg_text, assigned, file_id, user_id)

@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def back_to_main(call):
    user_id = call.from_user.id
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(t("platforms", user_id), callback_data="show_platforms"))
    markup.add(types.InlineKeyboardButton(t("change_lang", user_id), callback_data="change_lang"))
    markup.add(types.InlineKeyboardButton(t("terms", user_id), callback_data="show_terms"))
    if is_admin(user_id):
        markup.add(types.InlineKeyboardButton("🔐 لوحة الإدارة", callback_data="admin_panel"))
    safe_edit_or_delete(call, t("welcome", user_id), markup=markup, parse_mode="HTML", delete_old=True)

@bot.callback_query_handler(func=lambda call: call.data == "show_terms")
def show_terms(call):
    user_id = call.from_user.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(t("back_to_main", user_id), callback_data="back_to_main", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, t("terms_text", user_id), markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "instructions")
def show_instructions(call):
    user_id = call.from_user.id
    text = t("instructions", user_id) + "\n\n" + t("terms_text", user_id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(t("back_to_main", user_id), callback_data="back_to_main", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

def admin_main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = [
        types.InlineKeyboardButton("📥 إضافة كومبو", callback_data="admin_add_combo"),
        types.InlineKeyboardButton("🗑️ حذف كومبو", callback_data="admin_del_combo"),
        types.InlineKeyboardButton("📁 إدارة الملفات", callback_data="admin_manage_files"),
        types.InlineKeyboardButton("📊 الإحصائيات", callback_data="admin_stats"),
        types.InlineKeyboardButton("📄 تقرير كامل", callback_data="admin_full_report"),
        types.InlineKeyboardButton("🚫 حظر مستخدم", callback_data="admin_ban"),
        types.InlineKeyboardButton("✅ فك حظر", callback_data="admin_unban"),
        types.InlineKeyboardButton("📢 إذاعة للجميع", callback_data="admin_broadcast_all"),
        types.InlineKeyboardButton("📨 إذاعة لمستخدم", callback_data="admin_broadcast_user"),
        types.InlineKeyboardButton("👤 معلومات مستخدم", callback_data="admin_user_info"),
        types.InlineKeyboardButton("🔗 إدارة الاشتراك الإجباري", callback_data="admin_force_sub"),
        types.InlineKeyboardButton("👤 كومبو برايفت", callback_data="admin_private_combo"),
        types.InlineKeyboardButton("🖥️ فحص اللوحات", callback_data="admin_check_panels"),
        types.InlineKeyboardButton("➕ إضافة أدمن", callback_data="admin_add_admin"),
        types.InlineKeyboardButton("➖ إزالة أدمن", callback_data="admin_remove_admin"),
        types.InlineKeyboardButton("📱 إدارة الجروبات", callback_data="admin_manage_groups"),
        types.InlineKeyboardButton("📂 إضافة قسم", callback_data="admin_add_section"),
        types.InlineKeyboardButton("🗑️ حذف قسم", callback_data="admin_del_section"),
        types.InlineKeyboardButton("📡 إذاعة للجروبات", callback_data="admin_broadcast_groups"),
        types.InlineKeyboardButton("⚙️ إعدادات الحذف", callback_data="admin_auto_delete"),
        types.InlineKeyboardButton("👥 إضافة حسابات لوحات", callback_data="admin_panel_accounts"),
        types.InlineKeyboardButton("🖼️ تعيين صور البوت", callback_data="admin_set_images"),
        types.InlineKeyboardButton("🔧 وضع الصيانة", callback_data="admin_maintenance"),
        types.InlineKeyboardButton("⚡ قياس السرعة", callback_data="admin_speed_test"),
    ]
    for i in range(0, len(btns), 2):
        if i+1 < len(btns):
            markup.row(btns[i], btns[i+1])
        else:
            markup.row(btns[i])
    return markup

@bot.callback_query_handler(func=lambda call: call.data == "admin_panel")
def admin_panel(call):
    if not is_admin(call.from_user.id):
        return
    safe_edit_or_delete(call, "🔐 لوحة التحكم الرئيسية", markup=admin_main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_combo")
def admin_add_combo(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_combo_file"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "📤 أرسل ملف الكومبو بصيغة TXT", markup=markup)

@bot.message_handler(content_types=['document'])
def handle_combo_file(message):
    if not is_admin(message.from_user.id): return
    if user_states.get(message.from_user.id) != "waiting_combo_file": return
    try:
        file_info = bot.get_file(message.document.file_id)
        content = bot.download_file(file_info.file_path).decode('utf-8')
        lines = [l.strip() for l in content.splitlines() if l.strip()]
        if not lines:
            bot.reply_to(message, "❌ الملف فارغ!")
            return
        first_num = re.sub(r'\D', '', lines[0])
        country_code = None
        for code in sorted(COUNTRY_CODES.keys(), key=len, reverse=True):
            if first_num.startswith(code):
                country_code = code
                break
        if not country_code:
            bot.reply_to(message, "❌ لا يمكن تحديد الدولة!")
            return
        
        default_name = message.document.file_name or f"كومبو {country_code}"
        user_combo_buffer[message.from_user.id] = {
            "country_code": country_code,
            "numbers": lines,
            "default_name": default_name
        }
        user_states[message.from_user.id] = "waiting_combo_name"
        bot.reply_to(message, f"{t('enter_file_name', message.from_user.id)}\n{default_name}\n\n{t('skip_file_name', message.from_user.id)}")
    except Exception as e:
        bot.reply_to(message, f"❌ خطأ: {e}")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_combo_name")
def handle_combo_name(message):
    user_id = message.from_user.id
    if user_id not in user_combo_buffer:
        bot.reply_to(message, "❌ انتهت الجلسة، أعد رفع الملف.")
        del user_states[user_id]
        return
    if message.text == "/skip":
        file_name = user_combo_buffer[user_id]["default_name"]
    else:
        file_name = message.text.strip() or user_combo_buffer[user_id]["default_name"]
    user_combo_buffer[user_id]["file_name"] = file_name
    sections = get_all_sections()
    if sections:
        user_states[user_id] = "waiting_section_for_combo"
        country_code = user_combo_buffer[user_id]["country_code"]
        name, flag, _ = COUNTRY_CODES[country_code]
        markup = types.InlineKeyboardMarkup()
        for sid, sname in sections:
            markup.add(types.InlineKeyboardButton(sname, callback_data=f"set_combo_sec_{sid}"))
        markup.add(types.InlineKeyboardButton("📵 بدون قسم", callback_data="set_combo_sec_none"))
        bot.reply_to(message,
            f"✅ تم قراءة {len(user_combo_buffer[user_id]['numbers'])} رقم للدولة {flag} {name}\nالاسم: {file_name}\n\n📂 أضف الكومبو في أي قسم؟",
            reply_markup=markup)
    else:
        data = user_combo_buffer.pop(user_id)
        save_combo(data["country_code"], data["numbers"], file_name=data["file_name"])
        name, flag, _ = COUNTRY_CODES[data["country_code"]]
        bot.reply_to(message, f"✅ تم حفظ {len(data['numbers'])} رقم لدولة {flag} {name} باسم {data['file_name']}")
        del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_combo_sec_"))
def set_combo_section_handler(call):
    if not is_admin(call.from_user.id): return
    if call.from_user.id not in user_combo_buffer:
        bot.answer_callback_query(call.id, "❌ انتهت الجلسة، أعد رفع الملف!", show_alert=True)
        return
    data = user_combo_buffer.pop(call.from_user.id)
    country_code = data["country_code"]
    lines = data["numbers"]
    file_name = data["file_name"]
    part = call.data[len("set_combo_sec_"):]
    section_id = None if part == "none" else int(part)
    save_combo(country_code, lines, section_id=section_id, file_name=file_name)
    name, flag, _ = COUNTRY_CODES[country_code]
    if section_id:
        sections = get_all_sections()
        sec_name = next((n for i, n in sections if i == section_id), "القسم")
        msg = f"✅ {flag} {name} أُضيف إلى قسم: {sec_name} (ملف: {file_name})"
    else:
        msg = f"✅ {flag} {name} أُضيف بدون قسم (ملف: {file_name})"
    bot.answer_callback_query(call.id, msg, show_alert=True)
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except:
        pass
    bot.send_message(call.message.chat.id, msg)
    user_states.pop(call.from_user.id, None)

@bot.callback_query_handler(func=lambda call: call.data == "admin_del_combo")
def admin_del_combo(call):
    if not is_admin(call.from_user.id): return
    combos = get_all_combos()
    if not combos:
        bot.answer_callback_query(call.id, "❌ لا توجد كومبوهات!", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for code in combos:
        if code in COUNTRY_CODES:
            name, flag, _ = COUNTRY_CODES[code]
            plain_flag = get_flag_plain(flag)
            markup.add(types.InlineKeyboardButton(f"{plain_flag} {name}", callback_data=f"del_combo_{code}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "اختر الكومبو للحذف (سيتم حذف جميع الملفات لهذه الدولة):", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_combo_"))
def confirm_del_combo(call):
    if not is_admin(call.from_user.id): return
    code = call.data.split("_", 2)[2]
    delete_combo(code)
    name, flag, _ = COUNTRY_CODES.get(code, ("Unknown", "🌍", ""))
    bot.answer_callback_query(call.id, f"✅ تم حذف جميع ملفات {flag} {name}", show_alert=True)
    admin_del_combo(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_manage_files")
def admin_manage_files(call):
    if not is_admin(call.from_user.id): return
    combos = get_all_combos()
    if not combos:
        bot.answer_callback_query(call.id, "❌ لا توجد دول!", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for code in combos:
        if code in COUNTRY_CODES:
            name, flag, _ = COUNTRY_CODES[code]
            plain_flag = get_flag_plain(flag)
            markup.add(types.InlineKeyboardButton(f"{plain_flag} {name}", callback_data=f"list_files_{code}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "📁 اختر الدولة لعرض ملفاتها:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("list_files_"))
def list_files(call):
    if not is_admin(call.from_user.id): return
    country_code = call.data.split("_", 2)[2]
    files = get_combo_files(country_code)
    if not files:
        bot.answer_callback_query(call.id, "❌ لا توجد ملفات لهذه الدولة!", show_alert=True)
        return
    name, flag, _ = COUNTRY_CODES.get(country_code, ("Unknown", "🌍", ""))
    markup = types.InlineKeyboardMarkup()
    for f in files:
        available = len(get_available_numbers_from_file(f["id"]))
        btn_text = f"{f['file_name']} (إجمالي: {f['total']}, متاح: {available})"
        markup.add(types.InlineKeyboardButton(btn_text, callback_data=f"del_file_{f['id']}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_manage_files", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, f"📁 ملفات {flag} {name}:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_file_"))
def confirm_delete_file(call):
    if not is_admin(call.from_user.id): return
    file_id = int(call.data.split("_")[2])
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT file_name FROM combos WHERE id=?", (file_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        bot.answer_callback_query(call.id, "❌ الملف غير موجود!", show_alert=True)
        return
    file_name = row[0]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ نعم، احذف", callback_data=f"confirm_del_file_{file_id}"))
    markup.add(types.InlineKeyboardButton("❌ لا", callback_data="admin_manage_files"))
    safe_edit_or_delete(call, t("confirm_delete_file", call.from_user.id, file_name=file_name), markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_del_file_"))
def delete_file(call):
    if not is_admin(call.from_user.id): return
    file_id = int(call.data.split("_")[3])
    if delete_combo_file(file_id):
        bot.answer_callback_query(call.id, t("file_deleted", call.from_user.id), show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف!", show_alert=True)
    admin_manage_files(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_stats")
def admin_stats(call):
    if not is_admin(call.from_user.id): return
    total_users = len(get_all_users())
    combos = get_all_combos()
    total_numbers = sum(len(get_combo_files(c)) for c in combos)
    otp_count = len(get_otp_logs())
    text = f"📊 إحصائيات:\n👥 مستخدمون: {total_users}\n🌐 دول: {len(combos)}\n📞 أرقام: {total_numbers}\n🔑 أكواد: {otp_count}"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, text, markup=markup)

def get_otp_logs():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM otp_logs")
    rows = c.fetchall()
    conn.close()
    return rows

@bot.callback_query_handler(func=lambda call: call.data == "admin_full_report")
def admin_full_report(call):
    if not is_admin(call.from_user.id): return
    try:
        report = f"📊 تقرير البوت\n{'='*40}\n"
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        for u in c.fetchall():
            status = "محظور" if u[6] else "نشط"
            report += f"ID:{u[0]} @{u[1] or 'N/A'} | رقم:{u[5] or 'N/A'} | {status}\n"
        report += f"\n{'='*40}\n🔑 الأكواد:\n"
        c.execute("SELECT * FROM otp_logs")
        for lg in c.fetchall():
            report += f"{lg[1]} | {lg[2]} | {lg[4]}\n"
        conn.close()
        with open("sendako_report.txt", "w", encoding="utf-8") as f:
            f.write(report)
        with open("sendako_report.txt", "rb") as f:
            bot.send_document(call.from_user.id, f)
        os.remove("sendako_report.txt")
        bot.answer_callback_query(call.id, "✅ تم الإرسال!", show_alert=True)
    except Exception as e:
        bot.answer_callback_query(call.id, f"❌ {e}", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "admin_ban")
def admin_ban_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "ban_user"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم لحظره:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "ban_user")
def admin_ban_step2(message):
    try:
        uid = int(message.text)
        ban_user(uid)
        bot.reply_to(message, f"✅ تم حظر {uid}")
        del user_states[message.from_user.id]
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")

@bot.callback_query_handler(func=lambda call: call.data == "admin_unban")
def admin_unban_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "unban_user"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم لفك حظره:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "unban_user")
def admin_unban_step2(message):
    try:
        uid = int(message.text)
        unban_user(uid)
        bot.reply_to(message, f"✅ تم فك الحظر عن {uid}")
        del user_states[message.from_user.id]
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_all")
def admin_broadcast_all_step1(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📢 إذاعة نصية عادية",        callback_data="broadcast_type_plain"),
        types.InlineKeyboardButton("📤 إذاعة نسخ (copy)",        callback_data="broadcast_type_copy"),
        types.InlineKeyboardButton("↪️ إذاعة توجيهية (forward)", callback_data="broadcast_type_forward"),
        types.InlineKeyboardButton("✨ إذاعة مميزة (إيموجي + اقتباس)", callback_data="broadcast_type_fancy"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"),
    )
    safe_edit_or_delete(call, "📢 <b>إذاعة للجميع</b>\n\nاختر نوع الإذاعة:", markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "broadcast_type_plain")
def broadcast_type_plain(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_all"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_all", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "📢 أرسل نص الرسالة:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "broadcast_type_copy")
def broadcast_type_copy(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_copy_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_all", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call,
        "📤 <b>إذاعة نسخ</b>\n\nأرسل الرسالة اللي تريد نسخها وإذاعتها\n"
        "(تدعم النصوص والصور والفيديو والمستندات وكل أنواع الإيموجي المميزة):",
        markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "broadcast_type_forward")
def broadcast_type_forward(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_forward_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_all", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call,
        "↪️ <b>إذاعة توجيهية</b>\n\nأرسل الرسالة اللي تريد توجيهها:",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_copy_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice"])
def handle_broadcast_copy(message):
    if not is_admin(message.from_user.id): return
    uid = message.from_user.id
    user_states[uid] = {"step": "bc_copy_confirm", "chat_id": message.chat.id, "msg_id": message.message_id}
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("✅ تأكيد", callback_data="bc_copy_confirm"),
        types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_all"),
    )
    bot.reply_to(message, "❓ <b>تأكيد إذاعة هذه الرسالة لجميع المستخدمين؟</b>", parse_mode="HTML", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_forward_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice"])
def handle_broadcast_forward(message):
    if not is_admin(message.from_user.id): return
    uid = message.from_user.id
    user_states[uid] = {"step": "bc_forward_confirm", "chat_id": message.chat.id, "msg_id": message.message_id}
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("✅ تأكيد", callback_data="bc_forward_confirm"),
        types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_all"),
    )
    bot.reply_to(message, "❓ <b>تأكيد توجيه هذه الرسالة لجميع المستخدمين؟</b>", parse_mode="HTML", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "bc_copy_confirm")
def bc_copy_confirm(call):
    uid = call.from_user.id
    if not is_admin(uid): return
    state = user_states.pop(uid, {})
    if state.get("step") != "bc_copy_confirm": return
    src_chat = state["chat_id"]
    src_msg  = state["msg_id"]
    users = get_all_users()
    ok, fail = 0, 0
    progress = bot.send_message(call.message.chat.id, "⏳ جاري الإرسال...")
    for user_uid in users:
        try:
            bot.copy_message(int(user_uid), src_chat, src_msg)
            ok += 1
        except:
            fail += 1
    try: bot.delete_message(progress.chat.id, progress.message_id)
    except: pass
    bot.send_message(call.message.chat.id,
        f"✅ <b>تمت إذاعة النسخ!</b>\n\n📤 نجح: {ok}\n❌ فشل: {fail}", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "bc_forward_confirm")
def bc_forward_confirm(call):
    uid = call.from_user.id
    if not is_admin(uid): return
    state = user_states.pop(uid, {})
    if state.get("step") != "bc_forward_confirm": return
    src_chat = state["chat_id"]
    src_msg  = state["msg_id"]
    users = get_all_users()
    ok, fail = 0, 0
    progress = bot.send_message(call.message.chat.id, "⏳ جاري التوجيه...")
    for user_uid in users:
        try:
            bot.forward_message(int(user_uid), src_chat, src_msg)
            ok += 1
        except:
            fail += 1
    try: bot.delete_message(progress.chat.id, progress.message_id)
    except: pass
    bot.send_message(call.message.chat.id,
        f"✅ <b>تمت إذاعة التوجيه!</b>\n\n📤 نجح: {ok}\n❌ فشل: {fail}", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "broadcast_type_fancy")
def broadcast_type_fancy(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "bc_fancy_emoji"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_broadcast_all", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call,
        "✨ <b>إذاعة مميزة - الخطوة 1/3</b>\n\n"
        "أرسل الإيموجي المميز (مثل: 🔥 ⭐ 💎)\n"
        "أو /skip للتخطي:",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "bc_fancy_emoji")
def bc_fancy_step1(message):
    uid = message.from_user.id
    emoji = "" if message.text.strip() == "/skip" else message.text.strip()
    user_states[uid] = {"step": "bc_fancy_text", "emoji": emoji}
    bot.reply_to(message,
        "✨ <b>الخطوة 2/3</b>\n\nأرسل نص الرسالة الرئيسية:",
        parse_mode="HTML")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("step") == "bc_fancy_text")
def bc_fancy_step2(message):
    uid = message.from_user.id
    user_states[uid]["main_text"] = message.text.strip()
    user_states[uid]["step"] = "bc_fancy_quote"
    bot.reply_to(message,
        "✨ <b>الخطوة 3/3</b>\n\nأرسل نص الاقتباس (سيظهر في إطار blockquote)\n"
        "أو /skip للتخطي:",
        parse_mode="HTML")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("step") == "bc_fancy_quote")
def bc_fancy_step3(message):
    uid = message.from_user.id
    state = user_states.pop(uid)
    emoji     = state.get("emoji", "")
    main_text = state.get("main_text", "")
    quote     = "" if message.text.strip() == "/skip" else message.text.strip()

    header = f"{emoji} <b>{main_text}</b>" if emoji else f"<b>{main_text}</b>"
    body   = f"\n<blockquote>{quote}</blockquote>" if quote else ""
    final_msg = header + body

    users = get_all_users()
    ok, fail = 0, 0
    for user_uid in users:
        try:
            bot.send_message(user_uid, final_msg, parse_mode="HTML")
            ok += 1
        except:
            fail += 1
    bot.reply_to(message,
        f"✅ <b>تمت الإذاعة المميزة!</b>\n\n"
        f"📤 نجح: {ok}\n❌ فشل: {fail}",
        parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_all")
def admin_broadcast_all_step2(message):
    users = get_all_users()
    ok, fail = 0, 0
    for uid in users:
        try:
            bot.send_message(uid, message.text)
            ok += 1
        except:
            fail += 1
    bot.reply_to(message, f"✅ {ok} نجح | ❌ {fail} فشل")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_user")
def admin_broadcast_user_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_user_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_user_id")
def admin_broadcast_user_step2(message):
    try:
        uid = int(message.text)
        user_states[message.from_user.id] = f"broadcast_msg_{uid}"
        bot.reply_to(message, "أرسل الرسالة:")
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")

@bot.message_handler(func=lambda msg: str(user_states.get(msg.from_user.id, "")).startswith("broadcast_msg_"))
def admin_broadcast_user_step3(message):
    uid = int(str(user_states[message.from_user.id]).split("_")[2])
    try:
        bot.send_message(uid, message.text)
        bot.reply_to(message, f"✅ تم الإرسال لـ {uid}")
    except Exception as e:
        bot.reply_to(message, f"❌ فشل: {e}")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_user_info")
def admin_user_info_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "get_user_info"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "get_user_info")
def admin_user_info_step2(message):
    try:
        uid = int(message.text)
        user = get_user(uid)
        if not user:
            bot.reply_to(message, "❌ المستخدم غير موجود!")
        else:
            status = "محظور" if user[6] else "نشط"
            bot.reply_to(message,
                f"👤 معلومات:\n🆔 {user[0]}\n@{user[1] or 'N/A'}\nالرقم: {user[5] or 'N/A'}\nالحالة: {status}")
    except Exception as e:
        bot.reply_to(message, f"❌ {e}")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_force_sub")
def admin_force_sub(call):
    if not is_admin(call.from_user.id): return
    channels = get_all_force_sub_channels(enabled_only=False)
    text = f"🔗 إدارة قنوات الاشتراك الإجباري:\nإجمالي: {len(channels)}\n"
    markup = types.InlineKeyboardMarkup()
    for ch_id, url, desc in channels:
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        c = conn.cursor()
        c.execute("SELECT enabled FROM force_sub_channels WHERE id=?", (ch_id,))
        enabled = c.fetchone()[0]
        conn.close()
        status = "✅" if enabled else "❌"
        markup.add(types.InlineKeyboardButton(f"{status} {desc or url[:25]}", callback_data=f"edit_force_ch_{ch_id}"))
    markup.add(types.InlineKeyboardButton("➕ إضافة قناة", callback_data="add_force_ch"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, text, markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "add_force_ch")
def add_force_ch_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_force_ch_url"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_force_sub", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أرسل رابط القناة:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_force_ch_url")
def add_force_ch_step2(message):
    url = message.text.strip()
    if not (url.startswith("@") or url.startswith("https://t.me/")):
        bot.reply_to(message, "❌ رابط غير صالح!")
        return
    user_states[message.from_user.id] = {"step": "add_force_ch_desc", "url": url}
    bot.reply_to(message, "أدخل وصفاً للقناة (أو اترك فارغاً):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_force_ch_desc")
def add_force_ch_step3(message):
    data = user_states[message.from_user.id]
    if add_force_sub_channel(data["url"], message.text.strip()):
        bot.reply_to(message, f"✅ تم إضافة القناة: {data['url']}")
    else:
        bot.reply_to(message, "❌ القناة موجودة مسبقاً!")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_force_ch_"))
def edit_force_ch(call):
    if not is_admin(call.from_user.id): return
    ch_id = int(call.data.split("_", 3)[3])
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT channel_url,description,enabled FROM force_sub_channels WHERE id=?", (ch_id,))
    row = c.fetchone()
    conn.close()
    if not row:
        bot.answer_callback_query(call.id, "❌ غير موجودة!", show_alert=True)
        return
    url, desc, enabled = row
    markup = types.InlineKeyboardMarkup()
    if enabled:
        markup.add(types.InlineKeyboardButton("❌ تعطيل", callback_data=f"toggle_ch_{ch_id}"))
    else:
        markup.add(types.InlineKeyboardButton("✅ تفعيل", callback_data=f"toggle_ch_{ch_id}"))
    markup.add(types.InlineKeyboardButton("🗑️ حذف", callback_data=f"del_ch_{ch_id}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_force_sub", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, f"القناة: {url}\nالوصف: {desc or '—'}\nالحالة: {'مفعلة' if enabled else 'معطلة'}", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("toggle_ch_"))
def toggle_ch(call):
    ch_id = int(call.data.split("_", 2)[2])
    toggle_force_sub_channel(ch_id)
    bot.answer_callback_query(call.id, "🔄 تم تغيير الحالة", show_alert=True)
    admin_force_sub(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_ch_"))
def del_ch(call):
    ch_id = int(call.data.split("_", 2)[2])
    if delete_force_sub_channel(ch_id):
        bot.answer_callback_query(call.id, "✅ تم الحذف!", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف!", show_alert=True)
    admin_force_sub(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_private_combo")
def admin_private_combo(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("➕ إضافة كومبو برايفت", callback_data="add_private_combo"))
    markup.add(types.InlineKeyboardButton("🗑️ مسح كومبو برايفت", callback_data="del_private_combo"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "👤 كومبو برايفت:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "add_private_combo")
def add_private_combo_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_private_user_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_private_combo", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_private_user_id")
def add_private_combo_step2(message):
    try:
        uid = int(message.text)
        user_states[message.from_user.id] = f"add_private_country_{uid}"
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        for code in get_all_combos():
            if code in COUNTRY_CODES:
                name, flag, _ = COUNTRY_CODES[code]
                plain_flag = get_flag_plain(flag)
                buttons.append(types.InlineKeyboardButton(f"{plain_flag} {name}", callback_data=f"select_private_{uid}_{code}"))
        for i in range(0, len(buttons), 2):
            markup.row(*buttons[i:i+2])
        markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_private_combo", icon_custom_emoji_id="5386340832628462681"))
        bot.reply_to(message, "اختر الدولة:", reply_markup=markup)
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")

@bot.callback_query_handler(func=lambda call: call.data.startswith("select_private_"))
def select_private_combo(call):
    parts = call.data.split("_")
    uid = int(parts[2])
    country_code = parts[3]
    save_user(uid, private_combo_country=country_code)
    name, flag, _ = COUNTRY_CODES[country_code]
    bot.answer_callback_query(call.id, f"✅ تم: {uid} - {flag} {name}", show_alert=True)
    admin_private_combo(call)

@bot.callback_query_handler(func=lambda call: call.data == "del_private_combo")
def del_private_combo_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "del_private_user_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_private_combo", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "del_private_user_id")
def del_private_combo_step2(message):
    try:
        uid = int(message.text)
        save_user(uid, private_combo_country=None)
        bot.reply_to(message, f"✅ تم مسح الكومبو البرايفت لـ {uid}")
    except:
        bot.reply_to(message, "❌ معرف غير صحيح!")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_admin")
def admin_add_admin_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_admin_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أدخل معرف المستخدم (ID) لإضافته كادمن:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_admin_id")
def admin_add_admin_step2(message):
    try:
        uid = int(message.text.strip())
        uname = ""
        try:
            chat = bot.get_chat(uid)
            uname = chat.username or ""
        except:
            pass
        if add_db_admin(uid, uname):
            bot.reply_to(message, f"✅ تم إضافة الادمن:\n🆔 {uid}\n👤 @{uname or 'N/A'}")
        else:
            bot.reply_to(message, "❌ فشل في الإضافة!")
    except:
        bot.reply_to(message, "❌ معرف غير صحيح! أدخل رقم ID فقط.")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_remove_admin")
def admin_remove_admin_step1(call):
    if not is_admin(call.from_user.id): return
    db_admins = get_db_admins()
    if not db_admins:
        bot.answer_callback_query(call.id, "لا يوجد أدمنز في قاعدة البيانات!", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for uid, uname in db_admins:
        markup.add(types.InlineKeyboardButton(
            f"🗑️ {uid} @{uname or 'N/A'}",
            callback_data=f"rm_admin_{uid}"
        ))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "اختر الادمن لإزالته:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("rm_admin_"))
def admin_remove_admin_confirm(call):
    if not is_admin(call.from_user.id): return
    uid = int(call.data.split("_")[2])
    if uid in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ لا يمكن إزالة الأدمن الرئيسي!", show_alert=True)
        return
    remove_db_admin(uid)
    bot.answer_callback_query(call.id, f"✅ تم إزالة {uid}", show_alert=True)
    admin_remove_admin_step1(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_manage_groups")
def admin_manage_groups(call):
    if not is_admin(call.from_user.id): return
    groups = get_bot_groups()
    text = "📱 <b>إدارة الجروبات</b>\n\n"
    if groups:
        for gid, desc, is_otp in groups:
            mark = "🔴 OTP" if is_otp else "⚪️"
            text += f"{mark} {desc or gid} | <code>{gid}</code>\n"
    else:
        text += "❌ لا توجد مجموعات مضافة بعد\n"
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("➕ إضافة مجموعة",      callback_data="admin_add_group"),
        types.InlineKeyboardButton("➖ حذف مجموعة",         callback_data="admin_remove_group"),
        types.InlineKeyboardButton("📬 تعيين جروب OTP",     callback_data="admin_set_otp_group"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"),
    )
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "admin_set_otp_group")
def admin_set_otp_group(call):
    if not is_admin(call.from_user.id): return
    groups = get_bot_groups()
    if not groups:
        bot.answer_callback_query(call.id, "❌ لا توجد مجموعات! أضف مجموعة أولاً.", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup(row_width=1)
    for gid, desc, is_otp in groups:
        mark = "✅ " if is_otp else ""
        markup.add(types.InlineKeyboardButton(f"{mark}{desc or gid}", callback_data=f"set_otp_gid_{gid}"))
    markup.add(types.InlineKeyboardButton("📝 إدخال ID يدوياً", callback_data="set_otp_group_manual"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_manage_groups", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "📬 <b>اختر الجروب اللي سيكون جروب OTP:</b>\n(✅ = الحالي)", markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_otp_gid_"))
def set_otp_gid(call):
    if not is_admin(call.from_user.id): return
    gid = call.data[len("set_otp_gid_"):]
    set_otp_group(gid)
    bot.answer_callback_query(call.id, f"✅ تم تعيين جروب OTP: {gid}", show_alert=True)
    admin_manage_groups(call)

@bot.callback_query_handler(func=lambda call: call.data == "set_otp_group_manual")
def set_otp_group_manual(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_set_otp_group_manual"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_set_otp_group", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call,
        "📬 <b>تعيين جروب OTP يدوياً</b>\n\nأرسل ID المجموعة:\n(مثال: -1001234567890)",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_set_otp_group_manual")
def handle_set_otp_group_manual(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    gid = message.text.strip()
    try:
        gid = str(int(gid))
    except:
        bot.reply_to(message, "❌ ID غير صحيح! يجب أن يكون رقماً مثل -1001234567890")
        return
    set_otp_group(gid)
    bot.reply_to(message, f"✅ <b>تم تعيين جروب OTP!</b>\n\n🆔 Group ID: <code>{gid}</code>", parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_group")
def admin_add_group_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_group_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_manage_groups", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "أدخل ID المجموعة أو الرابط:\n(مثال: -1001234567890 أو @username)", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_group_id")
def admin_add_group_step2(message):
    gid = message.text.strip()
    desc = ""
    try:
        if gid.startswith("https://t.me/"):
            parts = gid.split("/")
            chat = bot.get_chat("@" + parts[-1])
            gid = str(chat.id)
        elif gid.startswith("@"):
            chat = bot.get_chat(gid)
            gid = str(chat.id)
        else:
            chat = bot.get_chat(int(gid))
            gid = str(chat.id)
        desc = chat.title or ""
        bot_member = bot.get_chat_member(gid, bot.get_me().id)
        if bot_member.status not in ["administrator", "creator"]:
            bot.reply_to(message, "❌ البوت مش أدمن في هذه المجموعة!")
            return
    except Exception as e:
        bot.reply_to(message, f"❌ لا يمكن الوصول إلى المجموعة: {e}")
        return
    user_states[message.from_user.id] = {"step": "add_group_otp", "gid": gid, "desc": desc}
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ نعم (جروب OTP)", callback_data="set_group_otp_yes"))
    markup.add(types.InlineKeyboardButton("❌ لا (مجموعة عادية)", callback_data="set_group_otp_no"))
    bot.reply_to(message, f"✅ وجدت: <b>{desc}</b>\n\nهل هذه هي مجموعة OTP؟", parse_mode="HTML", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_group_otp_"))
def set_group_otp(call):
    user_id = call.from_user.id
    if user_id not in user_states or not isinstance(user_states[user_id], dict):
        return
    data = user_states[user_id]
    is_otp = 1 if call.data == "set_group_otp_yes" else 0
    if add_bot_group(data["gid"], data["desc"], is_otp):
        if is_otp:
            set_otp_group(data["gid"])
        bot.answer_callback_query(call.id, f"✅ تم إضافة المجموعة", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الإضافة أو موجودة مسبقاً", show_alert=True)
    del user_states[user_id]
    admin_manage_groups(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_remove_group")
def admin_remove_group_step1(call):
    if not is_admin(call.from_user.id): return
    groups = get_bot_groups()
    if not groups:
        bot.answer_callback_query(call.id, "❌ لا توجد مجموعات!", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for gid, desc, is_otp in groups:
        otp_mark = "🔴 " if is_otp else ""
        markup.add(types.InlineKeyboardButton(f"{otp_mark}{desc or gid}", callback_data=f"rm_group_{gid}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_manage_groups", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "اختر المجموعة لحذفها:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("rm_group_"))
def admin_remove_group_confirm(call):
    if not is_admin(call.from_user.id): return
    gid = call.data[len("rm_group_"):]
    if remove_bot_group(gid):
        bot.answer_callback_query(call.id, "✅ تم الحذف", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف", show_alert=True)
    admin_manage_groups(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_section")
def admin_add_section(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_section_names"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call,
        "📂 أرسل أسماء الأقسام التي تريد إضافتها\n"
        "(كل اسم في سطر جديد)\n\n"
        "مثال:\nفيسبوك\nواتساب\nتيليغرام",
        markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_section_names")
def handle_section_names(message):
    if not is_admin(message.from_user.id): return
    names = [n.strip() for n in message.text.strip().splitlines() if n.strip()]
    if not names:
        bot.reply_to(message, "❌ لم تُرسل أي أسماء!")
        return
    created = []
    for n in names:
        if create_section(n):
            created.append(n)
    if created:
        bot.reply_to(message, f"✅ تم إنشاء {len(created)} قسم:\n" + "\n".join(f"📂 {n}" for n in created))
    else:
        bot.reply_to(message, "❌ الأقسام موجودة مسبقاً أو حدث خطأ!")
    user_states.pop(message.from_user.id, None)

@bot.callback_query_handler(func=lambda call: call.data == "admin_del_section")
def admin_del_section(call):
    if not is_admin(call.from_user.id): return
    sections = get_all_sections()
    if not sections:
        bot.answer_callback_query(call.id, "❌ لا توجد أقسام!", show_alert=True)
        return
    markup = types.InlineKeyboardMarkup()
    for sid, sname in sections:
        markup.add(types.InlineKeyboardButton(f"🗑️ {sname}", callback_data=f"confirm_del_sec_{sid}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, "اختر القسم الذي تريد حذفه:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_del_sec_"))
def confirm_del_section(call):
    if not is_admin(call.from_user.id): return
    sid = int(call.data.split("_")[3])
    delete_section(sid)
    bot.answer_callback_query(call.id, "✅ تم حذف القسم", show_alert=True)
    admin_panel(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_groups")
def admin_broadcast_groups_step1(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📢 إذاعة نصية عادية",        callback_data="bcg_type_plain"),
        types.InlineKeyboardButton("📤 إذاعة نسخ (copy)",        callback_data="bcg_type_copy"),
        types.InlineKeyboardButton("↪️ إذاعة توجيهية (forward)", callback_data="bcg_type_forward"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"),
    )
    safe_edit_or_delete(call, "📡 <b>إذاعة للجروبات</b>\n\nاختر نوع الإذاعة:", markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "bcg_type_plain")
def bcg_type_plain(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_broadcast_groups"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_groups"))
    safe_edit_or_delete(call, "📢 أرسل الرسالة اللي تريد تذيعها في الجروبات:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "bcg_type_copy")
def bcg_type_copy(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "bcg_copy_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_groups"))
    safe_edit_or_delete(call,
        "📤 <b>إذاعة نسخ للجروبات</b>\n\nأرسل الرسالة (تدعم كل أنواع المحتوى والإيموجي المميزة):",
        markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "bcg_type_forward")
def bcg_type_forward(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "bcg_forward_msg"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_broadcast_groups"))
    safe_edit_or_delete(call,
        "↪️ <b>إذاعة توجيهية للجروبات</b>\n\nأرسل الرسالة اللي تريد توجيهها:",
        markup=markup, parse_mode="HTML")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "bcg_copy_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice"])
def bcg_copy_handler(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    groups = get_bot_groups()
    if not groups:
        bot.reply_to(message, "❌ لا توجد مجموعات مضافة!")
        return
    ok, fail = 0, 0
    for gid, desc, _ in groups:
        try:
            me = bot.get_chat_member(gid, bot.get_me().id)
            if me.status in ("administrator", "creator"):
                bot.copy_message(gid, message.chat.id, message.message_id)
                ok += 1
            else:
                fail += 1
        except:
            fail += 1
    bot.reply_to(message, f"📡 تمت إذاعة النسخ للجروبات!\n✅ نجح: {ok}\n❌ فشل: {fail}")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "bcg_forward_msg",
                     content_types=["text", "photo", "video", "document", "audio", "sticker", "voice"])
def bcg_forward_handler(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    groups = get_bot_groups()
    if not groups:
        bot.reply_to(message, "❌ لا توجد مجموعات مضافة!")
        return
    ok, fail = 0, 0
    for gid, desc, _ in groups:
        try:
            me = bot.get_chat_member(gid, bot.get_me().id)
            if me.status in ("administrator", "creator"):
                bot.forward_message(gid, message.chat.id, message.message_id)
                ok += 1
            else:
                fail += 1
        except:
            fail += 1
    bot.reply_to(message, f"📡 تمت إذاعة التوجيه للجروبات!\n✅ نجح: {ok}\n❌ فشل: {fail}")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_broadcast_groups")
def broadcast_groups_step2(message):
    if not is_admin(message.from_user.id): return
    del user_states[message.from_user.id]
    groups = get_bot_groups()
    if not groups:
        bot.reply_to(message, "❌ لا توجد مجموعات أو قنوات مضافة!")
        return
    ok, fail = 0, 0
    for gid, desc, _ in groups:
        try:
            me = bot.get_chat_member(gid, bot.get_me().id)
            if me.status in ("administrator", "creator"):
                bot.send_message(gid, message.text)
                ok += 1
            else:
                fail += 1
        except:
            fail += 1
    bot.reply_to(message, f"📡 تمت الإذاعة!\n✅ نجح: {ok}\n❌ فشل (مش أدمن أو خطأ): {fail}")

@bot.callback_query_handler(func=lambda call: call.data == "admin_auto_delete")
def admin_auto_delete(call):
    if not is_admin(call.from_user.id): return
    chat_del  = get_auto_delete_time(call.message.chat.id)
    otp_del   = get_otp_delete_global()
    text = (
        f"⚙️ <b>إعدادات الحذف التلقائي</b>\n\n"
        f"🗑️ <b>حذف رسائل الجروب:</b> <code>{chat_del}</code> ثانية\n"
        f"🔑 <b>حذف سجل OTP:</b> <code>{otp_del}</code> ثانية\n"
    )
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✏️ تعديل رسائل الجروب", callback_data="edit_auto_delete"),
        types.InlineKeyboardButton("✏️ تعديل سجل OTP",     callback_data="edit_otp_delete"),
    )
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "edit_auto_delete")
def edit_auto_delete(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_auto_delete_time"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_auto_delete"))
    safe_edit_or_delete(call, "⏱️ أدخل مدة الحذف لرسائل الجروب بالثواني (مثال: 30):", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_auto_delete_time")
def set_auto_delete_time_msg(message):
    user_id = message.from_user.id
    try:
        seconds = int(message.text.strip())
        if seconds < 5:
            seconds = 5
        set_auto_delete_time(message.chat.id, seconds)
        bot.reply_to(message, f"✅ تم تعيين مدة حذف رسائل الجروب إلى {seconds} ثانية")
    except:
        bot.reply_to(message, "❌ قيمة غير صالحة")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data == "edit_otp_delete")
def edit_otp_delete(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_otp_delete_time"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_auto_delete"))
    safe_edit_or_delete(call, "⏱️ أدخل مدة حذف سجل OTP بالثواني (مثال: 30):", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "waiting_otp_delete_time")
def set_otp_delete_time_msg(message):
    user_id = message.from_user.id
    try:
        seconds = int(message.text.strip())
        if seconds < 5:
            seconds = 5
        set_otp_delete_global(seconds)
        bot.reply_to(message, f"✅ تم تعيين مدة حذف سجل OTP إلى {seconds} ثانية")
    except:
        bot.reply_to(message, "❌ قيمة غير صالحة")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_custom_buttons")
def admin_custom_buttons(call):
    user_id = call.from_user.id
    if not is_admin(user_id): return
    buttons = get_custom_buttons()
    text = "🔘 <b>الأزرار المخصصة</b>\n\n"
    markup = types.InlineKeyboardMarkup()
    for btn in buttons:
        id, btn_text, btn_url = btn
        text += f"• {btn_text} : {btn_url}\n"
        markup.add(types.InlineKeyboardButton(f"🗑️ {btn_text}", callback_data=f"del_custom_btn_{id}"))
    markup.row(
        types.InlineKeyboardButton("➕ إضافة زر", callback_data="add_custom_btn"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681")
    )
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "add_custom_btn")
def add_custom_btn_step1(call):
    user_id = call.from_user.id
    user_states[user_id] = "add_custom_btn_text"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_custom_buttons"))
    safe_edit_or_delete(call, "أدخل نص الزر:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_custom_btn_text")
def add_custom_btn_step2(message):
    user_id = message.from_user.id
    user_states[user_id] = {"step": "add_custom_btn_url", "text": message.text.strip()}
    bot.reply_to(message, "أدخل رابط الزر:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_custom_btn_url")
def add_custom_btn_step3(message):
    user_id = message.from_user.id
    add_custom_button(user_states[user_id]["text"], message.text.strip())
    bot.reply_to(message, "✅ تم إضافة الزر")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_custom_btn_"))
def del_custom_btn(call):
    user_id = call.from_user.id
    btn_id = int(call.data.split("_")[3])
    delete_custom_button(btn_id)
    bot.answer_callback_query(call.id, "✅ تم الحذف", show_alert=True)
    admin_custom_buttons(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_otp_group_buttons")
def admin_otp_group_buttons(call):
    if not is_admin(call.from_user.id): return
    buttons = get_otp_group_buttons()
    text = "📲 <b>إدارة أزرار رسالة OTP بتاعت الجروب</b>\n\n"
    markup = types.InlineKeyboardMarkup()
    for btn in buttons:
        text += f"• {btn['text']} : {btn['url']}\n"
        markup.add(types.InlineKeyboardButton(
            f"✏️ {btn['text']}", callback_data=f"edit_otp_gbtn_{btn['id']}"))
        markup.add(types.InlineKeyboardButton(
            f"🗑️ حذف {btn['text']}", callback_data=f"del_otp_gbtn_{btn['id']}"))
    markup.row(
        types.InlineKeyboardButton("➕ إضافة زر", callback_data="add_otp_gbtn"),
        types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681")
    )
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "add_otp_gbtn")
def add_otp_gbtn_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_otp_gbtn_text"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_otp_group_buttons"))
    safe_edit_or_delete(call, "أدخل نص الزر:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_otp_gbtn_text")
def add_otp_gbtn_step2(message):
    user_id = message.from_user.id
    user_states[user_id] = {"step": "add_otp_gbtn_url", "text": message.text.strip()}
    bot.reply_to(message, "أدخل رابط الزر:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_otp_gbtn_url")
def add_otp_gbtn_step3(message):
    user_id = message.from_user.id
    add_otp_group_button(user_states[user_id]["text"], message.text.strip())
    bot.reply_to(message, "✅ تم إضافة الزر")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_otp_gbtn_"))
def del_otp_gbtn(call):
    if not is_admin(call.from_user.id): return
    btn_id = int(call.data.split("_")[3])
    delete_otp_group_button(btn_id)
    bot.answer_callback_query(call.id, "✅ تم الحذف", show_alert=True)
    admin_otp_group_buttons(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_otp_gbtn_"))
def edit_otp_gbtn_step1(call):
    if not is_admin(call.from_user.id): return
    btn_id = int(call.data.split("_")[3])
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("✏️ تعديل الاسم",  callback_data=f"edit_ogbtn_name_{btn_id}"),
        types.InlineKeyboardButton("🔗 تعديل اللينك", callback_data=f"edit_ogbtn_url_{btn_id}"),
    )
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_otp_group_buttons"))
    safe_edit_or_delete(call, "ماذا تريد تعديل؟", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_ogbtn_name_"))
def edit_ogbtn_name_step(call):
    if not is_admin(call.from_user.id): return
    btn_id = int(call.data.split("_")[3])
    user_states[call.from_user.id] = {"step": "edit_otp_gbtn_text", "btn_id": btn_id}
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_otp_group_buttons"))
    safe_edit_or_delete(call, "أدخل الاسم الجديد للزر:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_ogbtn_url_"))
def edit_ogbtn_url_step(call):
    if not is_admin(call.from_user.id): return
    btn_id = int(call.data.split("_")[3])
    user_states[call.from_user.id] = {"step": "edit_otp_gbtn_url", "btn_id": btn_id}
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_otp_group_buttons"))
    safe_edit_or_delete(call, "أدخل اللينك الجديد للزر:", markup=markup)

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "edit_otp_gbtn_text")
def edit_otp_gbtn_text_msg(message):
    user_id = message.from_user.id
    btn_id = user_states[user_id]["btn_id"]
    update_otp_group_button_text(btn_id, message.text.strip())
    bot.reply_to(message, "✅ تم تعديل اسم الزر")
    del user_states[user_id]

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "edit_otp_gbtn_url")
def edit_otp_gbtn_url_msg(message):
    user_id = message.from_user.id
    btn_id = user_states[user_id]["btn_id"]
    update_otp_group_button_url(btn_id, message.text.strip())
    bot.reply_to(message, "✅ تم تعديل لينك الزر")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_set_images")
def admin_set_images(call):
    if not is_admin(call.from_user.id): return
    text = "🖼️ إدارة صور البوت\n\n"
    if BOT_IMAGE_BYTES:
        text += "✅ صورة البوت: موجودة\n"
    else:
        text += "❌ صورة البوت: غير موجودة\n"
    if FORCE_SUB_IMAGE_BYTES:
        text += "✅ صورة الاشتراك الإجباري: موجودة\n"
    else:
        text += "❌ صورة الاشتراك الإجباري: غير موجودة\n"
    if MAINTENANCE_IMAGE_BYTES:
        text += "✅ صورة الصيانة: موجودة\n"
    else:
        text += "❌ صورة الصيانة: غير موجودة\n"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🖼️ تعيين صورة البوت", callback_data="set_bot_image"))
    if BOT_IMAGE_BYTES:
        markup.add(types.InlineKeyboardButton("🗑️ حذف صورة البوت", callback_data="delete_bot_image"))
    markup.add(types.InlineKeyboardButton("🔗 تعيين صورة الاشتراك", callback_data="set_force_sub_image"))
    if FORCE_SUB_IMAGE_BYTES:
        markup.add(types.InlineKeyboardButton("🗑️ حذف صورة الاشتراك", callback_data="delete_force_sub_image"))
    markup.add(types.InlineKeyboardButton("🔧 تعيين صورة الصيانة", callback_data="set_maintenance_image"))
    if MAINTENANCE_IMAGE_BYTES:
        markup.add(types.InlineKeyboardButton("🗑️ حذف صورة الصيانة", callback_data="delete_maintenance_image"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, text, markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "set_bot_image")
def set_bot_image(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_bot_image"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_set_images"))
    safe_edit_or_delete(call, "أرسل الصورة الآن:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "set_force_sub_image")
def set_force_sub_image(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_force_sub_image"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_set_images"))
    safe_edit_or_delete(call, "أرسل الصورة الآن:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "set_maintenance_image")
def set_maintenance_image(call):
    user_id = call.from_user.id
    user_states[user_id] = "waiting_maintenance_image"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_set_images"))
    safe_edit_or_delete(call, "أرسل الصورة الآن:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "delete_bot_image")
def delete_bot_image(call):
    delete_image("bot")
    bot.answer_callback_query(call.id, t("image_deleted", call.from_user.id), show_alert=True)
    admin_set_images(call)

@bot.callback_query_handler(func=lambda call: call.data == "delete_force_sub_image")
def delete_force_sub_image(call):
    delete_image("force_sub")
    bot.answer_callback_query(call.id, t("image_deleted", call.from_user.id), show_alert=True)
    admin_set_images(call)

@bot.callback_query_handler(func=lambda call: call.data == "delete_maintenance_image")
def delete_maintenance_image(call):
    delete_image("maintenance")
    bot.answer_callback_query(call.id, t("image_deleted", call.from_user.id), show_alert=True)
    admin_set_images(call)

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    user_id = message.from_user.id
    if user_id not in user_states:
        return
    state = user_states[user_id]
    if state not in ["waiting_bot_image", "waiting_force_sub_image", "waiting_maintenance_image"]:
        return
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    if state == "waiting_bot_image":
        save_image("bot", downloaded_file)
        bot.reply_to(message, t("image_set", user_id))
    elif state == "waiting_force_sub_image":
        save_image("force_sub", downloaded_file)
        bot.reply_to(message, t("image_set", user_id))
    elif state == "waiting_maintenance_image":
        save_image("maintenance", downloaded_file)
        bot.reply_to(message, t("image_set", user_id))
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_maintenance")
def admin_maintenance(call):
    if not is_admin(call.from_user.id): return
    status = "مفعل" if MAINTENANCE_MODE else "معطل"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔄 تبديل وضع الصيانة", callback_data="toggle_maintenance"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, f"🔧 وضع الصيانة: {status}\n\nاضغط للتبديل:", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "toggle_maintenance")
def toggle_maintenance(call):
    if not is_admin(call.from_user.id): return
    set_maintenance_mode(not MAINTENANCE_MODE)
    bot.answer_callback_query(call.id, f"✅ وضع الصيانة الآن {'مفعل' if MAINTENANCE_MODE else 'معطل'}", show_alert=True)
    admin_maintenance(call)

@bot.callback_query_handler(func=lambda call: call.data == "admin_speed_test")
def admin_speed_test(call):
    if not is_admin(call.from_user.id): return
    start = time.time()
    msg = bot.send_message(call.message.chat.id, "⚡ جاري قياس السرعة...")
    end = time.time()
    response_time = (end - start) * 1000
    bot.edit_message_text(f"⏱️ زمن الاستجابة: {response_time:.2f} مللي ثانية", call.message.chat.id, msg.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "admin_dashboards")
def admin_dashboards_list(call):
    if not is_admin(call.from_user.id): return
    dashboards = get_db_dashboards(only_active=False)
    if not dashboards:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("➕ إضافة حساب", callback_data="add_dashboard"))
        markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
        safe_edit_or_delete(call, t("no_dashboards", call.from_user.id), markup=markup)
        return
    text = "🔐 <b>قائمة حسابات اللوحات</b>\n\n"
    markup = types.InlineKeyboardMarkup()
    for dash in dashboards:
        status = "✅" if dash["is_active"] else "❌"
        text += f"{status} **{dash['name']}** ({dash['short']})\n"
        markup.add(types.InlineKeyboardButton(f"{status} {dash['name']}", callback_data=f"edit_dash_{dash['id']}"))
    markup.add(types.InlineKeyboardButton("➕ إضافة حساب", callback_data="add_dashboard"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "add_dashboard")
def add_dashboard_step1(call):
    user_id = call.from_user.id
    user_states[user_id] = "add_dash_name"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data="admin_dashboards"))
    safe_edit_or_delete(call, "أدخل اسم اللوحة:", markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_dash_name")
def add_dash_step2(message):
    user_id = message.from_user.id
    user_states[user_id] = {"step": "add_dash_short", "name": message.text.strip()}
    bot.reply_to(message, "أدخل اختصار اللوحة (مثل WS):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_short")
def add_dash_step3(message):
    user_id = message.from_user.id
    user_states[user_id]["short"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_type"
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Traditional", callback_data="set_dash_type_traditional"),
        types.InlineKeyboardButton("API", callback_data="set_dash_type_api")
    )
    bot.reply_to(message, "اختر نوع اللوحة:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_dash_type_"))
def add_dash_step4(call):
    user_id = call.from_user.id
    if user_id not in user_states or not isinstance(user_states[user_id], dict):
        return
    dash_type = "traditional" if call.data == "set_dash_type_traditional" else "api"
    user_states[user_id]["type"] = dash_type
    user_states[user_id]["step"] = "add_dash_username"
    safe_edit_or_delete(call, "أدخل اسم المستخدم (اتركه فارغاً إذا كان API):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_username")
def add_dash_step5(message):
    user_id = message.from_user.id
    user_states[user_id]["username"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_password"
    bot.reply_to(message, "أدخل كلمة المرور (اتركها فارغاً إذا كان API):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_password")
def add_dash_step6(message):
    user_id = message.from_user.id
    user_states[user_id]["password"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_token"
    bot.reply_to(message, "أدخل توكن API (إذا كان API، وإلا اتركه فارغاً):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_token")
def add_dash_step7(message):
    user_id = message.from_user.id
    user_states[user_id]["token"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_base_url"
    bot.reply_to(message, "أدخل الرابط الأساسي (base URL) للوحة:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_base_url")
def add_dash_step8(message):
    user_id = message.from_user.id
    user_states[user_id]["base_url"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_ajax"
    bot.reply_to(message, "أدخل مسار AJAX (مثل /agent/res/data_smscdr.php) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_ajax")
def add_dash_step9(message):
    user_id = message.from_user.id
    user_states[user_id]["ajax_path"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_login_page"
    bot.reply_to(message, "أدخل صفحة تسجيل الدخول (مثل /login) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_login_page")
def add_dash_step10(message):
    user_id = message.from_user.id
    user_states[user_id]["login_page"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_login_post"
    bot.reply_to(message, "أدخل مسار POST لتسجيل الدخول (مثل /signin) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_login_post")
def add_dash_step11(message):
    user_id = message.from_user.id
    user_states[user_id]["login_post"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_stats_page"
    bot.reply_to(message, "أدخل صفحة الإحصائيات (مثل /stats) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_stats_page")
def add_dash_step12(message):
    user_id = message.from_user.id
    user_states[user_id]["stats_page"] = message.text.strip()
    user_states[user_id]["step"] = "add_dash_idx_date"
    bot.reply_to(message, "أدخل رقم عمود التاريخ (افتراضي 0):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_idx_date")
def add_dash_step13(message):
    user_id = message.from_user.id
    try:
        idx_date = int(message.text.strip())
    except:
        idx_date = 0
    user_states[user_id]["idx_date"] = idx_date
    user_states[user_id]["step"] = "add_dash_idx_number"
    bot.reply_to(message, "أدخل رقم عمود الرقم (افتراضي 2):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_idx_number")
def add_dash_step14(message):
    user_id = message.from_user.id
    try:
        idx_number = int(message.text.strip())
    except:
        idx_number = 2
    user_states[user_id]["idx_number"] = idx_number
    user_states[user_id]["step"] = "add_dash_idx_sms"
    bot.reply_to(message, "أدخل رقم عمود الرسالة (افتراضي 5):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_idx_sms")
def add_dash_step15(message):
    user_id = message.from_user.id
    try:
        idx_sms = int(message.text.strip())
    except:
        idx_sms = 5
    user_states[user_id]["idx_sms"] = idx_sms
    user_states[user_id]["step"] = "add_dash_timeout"
    bot.reply_to(message, "أدخل مهلة الاتصال بالثواني (افتراضي 10):")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_timeout")
def add_dash_step16(message):
    user_id = message.from_user.id
    try:
        timeout = int(message.text.strip())
    except:
        timeout = 10
    user_states[user_id]["timeout"] = timeout
    user_states[user_id]["step"] = "add_dash_data_keys"
    bot.reply_to(message, "أدخل مفاتيح البيانات بصيغة JSON (مثال: {\"date\":\"dt\",\"number\":\"num\",\"sms\":\"message\"}) أو اتركه فارغاً:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and user_states[msg.from_user.id].get("step") == "add_dash_data_keys")
def add_dash_step17(message):
    user_id = message.from_user.id
    data_keys = {}
    if message.text.strip():
        try:
            data_keys = json.loads(message.text.strip())
        except:
            data_keys = {}
    data = user_states[user_id]
    add_dashboard_account(
        name=data["name"],
        short=data["short"],
        username=data["username"],
        password=data["password"],
        api_token=data["token"],
        dash_type=data["type"],
        base_url=data["base_url"],
        ajax_path=data["ajax_path"],
        login_page=data["login_page"],
        login_post=data["login_post"],
        stats_page=data["stats_page"],
        idx_date=data["idx_date"],
        idx_number=data["idx_number"],
        idx_sms=data["idx_sms"],
        timeout=data["timeout"],
        data_keys=data_keys,
        refresh_interval=1
    )
    bot.reply_to(message, f"✅ تم إضافة حساب اللوحة {data['name']} بنجاح")
    del user_states[user_id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("edit_dash_"))
def edit_dash(call):
    dash_id = int(call.data.split("_")[2])
    dashboards = get_db_dashboards(only_active=False)
    dash = next((d for d in dashboards if d["id"] == dash_id), None)
    if not dash:
        bot.answer_callback_query(call.id, "❌ الحساب غير موجود", show_alert=True)
        return
    text = f"🔐 <b>{dash['name']}</b>\n"
    text += f"الاختصار: {dash['short']}\n"
    text += f"النوع: {dash['type']}\n"
    text += f"المستخدم: {dash['username'] or '—'}\n"
    text += f"توكن API: {'موجود' if dash['api_token'] else '—'}\n"
    text += f"الحالة: {'✅ نشط' if dash['is_active'] else '❌ معطل'}\n"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔄 تفعيل/تعطيل", callback_data=f"toggle_dash_{dash_id}"))
    markup.add(types.InlineKeyboardButton("🗑️ حذف", callback_data=f"delete_dash_{dash_id}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_dashboards", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("toggle_dash_"))
def toggle_dash(call):
    dash_id = int(call.data.split("_")[2])
    toggle_dashboard_account(dash_id)
    bot.answer_callback_query(call.id, "✅ تم تبديل حالة الحساب", show_alert=True)
    edit_dash(call)

@bot.callback_query_handler(func=lambda call: call.data.startswith("delete_dash_"))
def delete_dash_confirm(call):
    dash_id = int(call.data.split("_")[2])
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ نعم، احذف", callback_data=f"confirm_delete_dash_{dash_id}"))
    markup.add(types.InlineKeyboardButton("❌ لا", callback_data=f"edit_dash_{dash_id}"))
    safe_edit_or_delete(call, "⚠️ هل أنت متأكد من حذف هذا الحساب؟", markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("confirm_delete_dash_"))
def confirm_delete_dash(call):
    dash_id = int(call.data.split("_")[3])
    delete_dashboard_account(dash_id)
    bot.answer_callback_query(call.id, "✅ تم الحذف", show_alert=True)
    admin_dashboards_list(call)

def _real_check_ims_panel(dash):
    """فحص لوحات etkk login مثل Fly Panel New"""
    username = dash.get("username", "").strip()
    password = dash.get("password", "").strip()
    if not username or not password:
        return t("no_username_pass", None)
    dash_timeout = dash.get("timeout", 10)
    try:
        tmp = requests.Session()
        tmp.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        base_url = dash.get("base_url", "")
        login_page = base_url + dash.get("login_page", "/login")
        login_post = base_url + dash.get("login_post", "/signin")
        resp = tmp.get(login_page, timeout=dash_timeout)
        if resp.status_code != 200:
            return t("server_down", None)
        soup = BeautifulSoup(resp.text, "html.parser")
        etkk_input = soup.find("input", {"name": "etkk"})
        etkk_value = etkk_input.get("value", "") if etkk_input else ""
        captcha_answer = None
        m = re.search(r'What is (\d+)\s*\+\s*(\d+)', resp.text, re.IGNORECASE)
        if m:
            captcha_answer = int(m.group(1)) + int(m.group(2))
        else:
            for txt in soup.stripped_strings:
                m2 = re.search(r'(\d+)\s*\+\s*(\d+)', txt)
                if m2:
                    captcha_answer = int(m2.group(1)) + int(m2.group(2))
                    break
        if captcha_answer is None:
            return t("captcha_unknown", None)
        payload = {"username": username, "password": password,
                   "capt": str(captcha_answer), "etkk": etkk_value}
        r2 = tmp.post(login_post, data=payload,
                      headers={"Referer": login_page, "Content-Type": "application/x-www-form-urlencoded"},
                      timeout=dash_timeout, allow_redirects=True)
        if "agent/SMS" in r2.url or "dashboard" in r2.url.lower() or "logout" in r2.text.lower():
            return t("working", None)
        return t("wrong_credentials", None)
    except requests.exceptions.ConnectionError:
        return t("server_down", None)
    except requests.exceptions.Timeout:
        return t("timeout", None)
    except Exception:
        return t("connection_error", None)

def _real_check_traditional(dash):
    username = dash.get("username", "").strip()
    password = dash.get("password", "").strip()
    if not username or not password:
        return t("no_username_pass", None)
    dash_timeout = dash.get("timeout", 10)
    try:
        tmp = requests.Session()
        tmp.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        })
        base_url = dash.get("base_url", "")
        login_page_url = dash.get("login_page_url") or (base_url + dash.get("login_page", ""))
        if not login_page_url:
            return t("no_url", None)
        resp = tmp.get(login_page_url, timeout=dash_timeout)
        if resp.status_code not in (200, 302):
            return t("server_down", None)

        captcha_answer = _solve_captcha(resp.text)
        # لو _solve_captcha رجع None، نحاول بـ capt فارغ بدل الفشل الفوري
        if captcha_answer is None:
            captcha_answer = ""

        payload = {}
        payload.update(_extract_hidden_fields(resp.text))
        payload["username"] = username
        payload["password"] = password
        payload["capt"] = captcha_answer

        login_post_url = dash.get("login_post_url") or (base_url + dash.get("login_post", ""))
        if not login_post_url:
            return t("no_url", None)
        r2 = tmp.post(login_post_url, data=payload,
                      headers={
                          "Content-Type": "application/x-www-form-urlencoded",
                          "Origin": base_url.rstrip("/"),
                          "Referer": login_page_url,
                          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                          "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
                          "Upgrade-Insecure-Requests": "1",
                      },
                      timeout=max(dash_timeout, 15), allow_redirects=True)
        r2u = r2.url.lower()
        r2t = r2.text.lower()
        is_success = (
            "agent"      in r2u or
            "dashboard"  in r2u or
            "reports"    in r2u or
            "smscdr"     in r2t or
            "logout"     in r2t or
            "signout"    in r2t or
            "/ints/agent" in r2.url or
            "/ints/client" in r2.url or
            ("login" not in r2u and "signin" not in r2u and r2.status_code == 200) or
            # سيرفرات تبقى على نفس الـ URL لكن تعرض dashboard
            (r2.status_code == 200
             and "password" not in r2t
             and "username" not in r2t
             and len(r2.text) > 2000)
        )
        # تحقق ثانوي: زيارة صفحة الـ agent مباشرة (يحل مشكلة Sniper وغيره)
        if not is_success:
            for sp in ["/ints/agent/SMSCDRReports", "/agent/SMSCDRReports",
                       "/ints/agent/SMSCDRStats",  "/agent/SMSCDRStats"]:
                try:
                    tr = tmp.get(base_url.rstrip("/") + sp, timeout=8)
                    if (tr.status_code == 200
                            and "login"    not in tr.url.lower()
                            and "signin"   not in tr.url.lower()
                            and "password" not in tr.text.lower()):
                        is_success = True
                        break
                except:
                    pass
        if is_success:
            return t("working", None)
        else:
            return t("wrong_credentials", None)
    except requests.exceptions.ConnectionError:
        return t("server_down", None)
    except requests.exceptions.Timeout:
        return t("timeout", None)
    except Exception:
        return t("connection_error", None)

def _real_check_api(dash):
    url = dash.get("api_url", "").strip()
    token = dash.get("api_token", "").strip()
    if not url:
        return t("no_url", None)
    if not token:
        return t("no_token", None)
    try:
        r = requests.get(url, params={"token": token}, timeout=10)
        if r.status_code == 200 and len(r.text.strip()) > 2:
            return t("working", None)
        return t("http_error", None, code=r.status_code)
    except requests.exceptions.ConnectionError:
        return t("server_down", None)
    except requests.exceptions.Timeout:
        return t("timeout", None)
    except Exception:
        return t("connection_error", None)

def _build_check_panels_msg(user_id, from_cache=False):
    """يبني رسالة فحص اللوحات — يستخدم الكاش إذا from_cache=True"""
    ok_list = []
    fail_list = []

    def _fmt_line(short, name, status, thread_status="", cached=False):
        if status == t("working", None):
            icon = "✅"
        elif ("لا توجد" in status or "لا يوجد" in status or
              "no_token" in status.lower() or "no_url" in status.lower()):
            icon = "⚪"
        else:
            icon = "❌"
        name_display = name if len(name) <= 14 else name[:13] + "…"
        dots = "·" * max(1, 15 - len(name_display))
        thr = f" {thread_status}" if thread_status else ""
        age = ""
        if cached:
            entry = _panel_check_cache.get(name)
            if entry:
                secs = int(time.time() - entry["ts"])
                age = f" <i>({secs}s)</i>"
        return f"{icon} <code>{short:<2}</code> {name_display}{dots}{thr}│ <i>{status}</i>{age}"

    def _get_status(key, fetcher):
        """يرجع الكاش لو موجود، وإلا يجيب live"""
        with _panel_check_lock:
            cached = _panel_check_cache.get(key)
        if from_cache and cached:
            return cached["status"]
        status = fetcher()
        with _panel_check_lock:
            _panel_check_cache[key] = {"status": status, "ts": time.time()}
        return status

    rows_static = []
    all_dashboards = get_all_active_dashboards()
    for dash in all_dashboards:
        name  = dash["name"]
        short = dash.get("short", "??")
        dtype = dash.get("type", "traditional")
        d = dash  # capture for lambda
        if dtype in ("api_token", "api"):
            status = _get_status(name, lambda d=d: _real_check_api(d))
        elif dtype == "ims_panel":
            status = _get_status(name, lambda d=d: _real_check_ims_panel(d))
        else:
            status = _get_status(name, lambda d=d: _real_check_traditional(d))
        if status == t("working", None):
            ok_list.append(name)
        else:
            fail_list.append(name)
        rows_static.append(_fmt_line(short, name, status, cached=from_cache))

    rows_dynamic = []
    all_panel_accounts = load_panel_accounts()
    for sk, site in PANEL_SITES.items():
        accounts = all_panel_accounts.get(sk, {}).get("accounts", [])
        short = site.get("short", "??")
        name  = site["name"]
        dtype = site.get("type", "traditional")
        if not accounts:
            rows_dynamic.append(_fmt_line(short, name, "⚪ لا توجد حسابات"))
            continue
        for acc in accounts:
            uname = acc.get("username", "API")
            label = f"{name} / {uname}"
            cache_key = f"dyn_{sk}_{acc.get('id','')}"
            if dtype in ("api", "api_token"):
                fake_dash = {
                    "name": label,
                    "api_url":   site.get("api_url", ""),
                    "api_token": acc.get("api_token") or site.get("api_token", ""),
                }
                status = _get_status(cache_key, lambda fd=fake_dash: _real_check_api(fd))
            elif dtype == "ims_panel":
                fake_dash = {
                    "name": label, "type": dtype,
                    "username": acc.get("username", ""),
                    "password": acc.get("password", ""),
                    "base_url":       site.get("base_url", ""),
                    "login_page":     site.get("login_page", ""),
                    "login_post":     site.get("login_post", ""),
                    "dashboard_path": site.get("dashboard_path", ""),
                    "timeout":        site.get("timeout", 10),
                }
                status = _get_status(cache_key, lambda fd=fake_dash: _real_check_ims_panel(fd))
            else:
                _base = site.get("base_url", "").rstrip("/")
                _lp   = site.get("login_page", "")
                _lpo  = site.get("login_post", "")
                fake_dash = {
                    "name": label, "type": dtype,
                    "username": acc.get("username", ""),
                    "password": acc.get("password", ""),
                    "base_url":       _base,
                    "login_page":     _lp,
                    "login_post":     _lpo,
                    "login_page_url": site.get("login_page_url") or (_base + _lp),
                    "login_post_url": site.get("login_post_url") or (_base + _lpo),
                    "ajax_path":      site.get("ajax_path", ""),
                    "timeout":        site.get("timeout", 10),
                }
                status = _get_status(cache_key, lambda fd=fake_dash: _real_check_traditional(fd))
            key = f"{sk}_{acc['id']}"
            thr = _panel_threads.get(key)
            thr_icon = "🟢" if thr and thr.is_alive() else "🔴"
            if status == t("working", None):
                ok_list.append(label)
            else:
                fail_list.append(label)
            rows_dynamic.append(_fmt_line(short, label, status, thr_icon, cached=from_cache))

    ivas_name = "iVAS SMS"
    def _check_ivas():
        try:
            tmp = requests.Session()
            tmp.headers.update(COMMON_HEADERS)
            r = tmp.get("https://www.ivasms.com/ints/login", timeout=12)
            if r.status_code == 200:
                return t("ivas_working", None) if _ivas_logged_in else t("ivas_server_working", None)
            return t("http_error", None, code=r.status_code)
        except:
            return t("connection_error", None)
    ivas_status = _get_status("iVAS SMS", _check_ivas)
    if t("working", None) in ivas_status or t("ivas_working", None) in ivas_status:
        ok_list.append(ivas_name)
    else:
        fail_list.append(ivas_name)
    rows_static.append(_fmt_line("IV", ivas_name, ivas_status, cached=from_cache))

    now_str = datetime.now().strftime("%H:%M:%S")
    cache_note = " 🕐 <i>(كاش)</i>" if from_cache else ""
    header = (
        f"🖥️ <b>فحص اللوحات</b>  <code>{now_str}</code>{cache_note}\n"
        f"{'─' * 32}\n"
    )

    static_block  = "\n".join(rows_static)
    dynamic_block = "\n".join(rows_dynamic)

    body = (
        f"<blockquote expandable>"
        f"📌 <b>اللوحات الثابتة</b> ({len(rows_static)})\n\n"
        f"{static_block}"
        f"</blockquote>\n\n"
    )
    if rows_dynamic:
        body += (
            f"<blockquote expandable>"
            f"🆕 <b>لوحات الأدمن</b> ({len(rows_dynamic)})\n\n"
            f"{dynamic_block}"
            f"</blockquote>"
        )

    summary = (
        f"\n{'─' * 32}\n"
        f"✅ <b>شغالة:</b> {len(ok_list)}   "
        f"❌ <b>مش شغالة:</b> {len(fail_list)}"
    )
    return header + body + summary


@bot.callback_query_handler(func=lambda call: call.data == "admin_check_panels")
def admin_check_panels(call):
    if not is_admin(call.from_user.id):
        return

    user_id = call.from_user.id

    # لو في كاش حديث (أقل من 90 ثانية)، اعرضه فوراً وحدّث في الخلفية
    with _panel_check_lock:
        has_cache = bool(_panel_check_cache)
        if has_cache:
            oldest = min((v["ts"] for v in _panel_check_cache.values()), default=0)
            cache_age = time.time() - oldest
            cache_fresh = cache_age < 90
        else:
            cache_fresh = False

    if cache_fresh:
        # اعرض النتيجة المحفوظة فوراً
        bot.answer_callback_query(call.id, "⚡ بيعرض الكاش ويحدّث في الخلفية…", show_alert=False)
        try:
            cached_msg = _build_check_panels_msg(user_id, from_cache=True)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(t("refresh", user_id), callback_data="admin_check_panels"))
            markup.add(types.InlineKeyboardButton(t("back", user_id), callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
            safe_edit_or_delete(call, cached_msg, markup=markup, parse_mode="HTML")
        except Exception:
            pass
        # حدّث في الخلفية بعد العرض
        def _bg_refresh():
            _build_check_panels_msg(user_id, from_cache=False)
        threading.Thread(target=_bg_refresh, daemon=True).start()
        return

    bot.answer_callback_query(call.id, t("checking", user_id), show_alert=False)

    def run_check():
        full_msg = _build_check_panels_msg(user_id, from_cache=False)

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(t("refresh", user_id), callback_data="admin_check_panels"))
        markup.add(types.InlineKeyboardButton(t("back", user_id), callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
        try:
            safe_edit_or_delete(call, full_msg, markup=markup, parse_mode="HTML")
        except Exception:
            bot.send_message(call.message.chat.id, full_msg, parse_mode="HTML", reply_markup=markup)

    threading.Thread(target=run_check, daemon=True).start()


def _extract_hidden_fields(html_text):
    """استخراج كل hidden fields من الـ form (crlf, _token, csrf, etkk ...)"""
    fields = {}
    try:
        soup = BeautifulSoup(html_text, "html.parser")
        form = soup.find("form")
        inputs = form.find_all("input") if form else soup.find_all("input")
        skip = {"username", "password", "capt", "submit", ""}
        for inp in inputs:
            name  = inp.get("name", "")
            itype = inp.get("type", "text").lower()
            val   = inp.get("value", "")
            if name and name not in skip and itype == "hidden":
                fields[name] = val
    except:
        for name_tok in ["crlf", "_token", "etkk"]:
            pat1 = 'name=["\']' + name_tok + '["\'][^>]*value=["\']([^"\']+)["\']'
            pat2 = 'value=["\']([^"\']+)["\'][^>]*name=["\']' + name_tok + '["\']'
            m = re.search(pat1, html_text) or re.search(pat2, html_text)
            if m:
                fields[name_tok] = m.group(1)
    return fields

def _solve_captcha(html_content):
    """حل الكابتشا - يدعم +، -، *، /"""
    patterns = [
        r'(\d+)\s*([+\-*/])\s*(\d+)\s*=?\s*\?',
        r'What is\s*(\d+)\s*([+\-*/])\s*(\d+)\?',
        r'(\d+)\s*([+\-*/])\s*(\d+)\s*=',
        r'(\d+)\s*([+\-*/])\s*(\d+)'
    ]
    for pattern in patterns:
        m = re.search(pattern, html_content, re.IGNORECASE)
        if m:
            n1, op, n2 = int(m.group(1)), m.group(2), int(m.group(3))
            if op == '+': return str(n1 + n2)
            if op == '-': return str(n1 - n2)
            if op == '*': return str(n1 * n2)
            if op == '/': return str(n1 // n2) if n2 else '0'
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        for txt in soup.stripped_strings:
            m3 = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)', txt)
            if m3:
                n1, op, n2 = int(m3.group(1)), m3.group(2), int(m3.group(3))
                if op == '+': return str(n1 + n2)
                if op == '-': return str(n1 - n2)
                if op == '*': return str(n1 * n2)
                if op == '/': return str(n1 // n2) if n2 else '0'
    except:
        pass
    if 'capt' not in html_content.lower() and 'captcha' not in html_content.lower():
        return ""
    return None

def login_for_dashboard(dash):
    if dash.get("type") in ("api_token", "api"):
        dash["is_logged_in"] = True
        return True

    if dash.get("type") in ("ims_panel", "ims_client"):
        return _do_ims_login(dash)

    def do_login():
        dash_timeout = max(dash.get("timeout", 15), 15)
        try:
            dash["session"].headers.update({
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            })
            login_page_url = dash.get("login_page_url", "")
            if not login_page_url:
                return False
            resp = dash["session"].get(login_page_url, timeout=dash_timeout)
            captcha = _solve_captcha(resp.text)
            if captcha is None:
                captcha = ""
            payload = {}
            payload.update(_extract_hidden_fields(resp.text))
            payload["username"] = dash.get("username","")
            payload["password"] = dash.get("password","")
            if captcha != "":
                payload["capt"] = captcha
            base_url = dash.get("base_url","").rstrip("/")
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin":       base_url,
                "Referer":      login_page_url,
                "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept":       "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection":   "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }
            login_post_url = dash.get("login_post_url", "")
            if not login_post_url:
                return False
            resp = dash["session"].post(login_post_url, data=payload, headers=headers,
                                        timeout=max(dash_timeout, 20), allow_redirects=True)
            resp_url_lower = resp.url.lower()
            resp_text_lower = resp.text.lower()
            login_page_url = dash.get("login_page_url", "")
            login_success = (
                "agent"     in resp_url_lower or
                "dashboard" in resp_url_lower or
                "reports"   in resp_url_lower or
                "smscdr"    in resp_text_lower or
                "logout"    in resp_text_lower or
                "/ints/agent" in resp.url or
                "/ints/client" in resp.url or
                (resp.url != login_page_url and "signin" not in resp.url.lower() and "login" not in resp.url.lower())
            )
            # فحص ثانوي لـ FIRE ولوحات مشابهة - لو ما اتغيرش الـ URL بس الـ HTML بيقول نجح
            if not login_success:
                for sp in ["/ints/agent/SMSCDRReports", "/agent/SMSCDRReports",
                           "/ints/agent/SMSCDRStats", "/agent/SMSCDRStats"]:
                    try:
                        base = dash.get("base_url","").rstrip("/")
                        tr = dash["session"].get(base + sp, timeout=8)
                        if tr.status_code == 200 and "login" not in tr.url.lower() and "signin" not in tr.url.lower():
                            login_success = True
                            break
                    except:
                        pass
            print(f"[{dash.get('name','')}] login URL: {resp.url} | success={login_success}")
            if login_success:
                dash["is_logged_in"] = True
                dash["_login_time"] = time.time()
                base = dash.get("base_url","").rstrip("/")
                for sp in ["/ints/agent/SMSCDRReports", "/agent/SMSCDRReports",
                           dash.get("stats_page",""), "/ints/agent/SMSCDRStats", "/agent/SMSCDRStats"]:
                    if not sp: continue
                    try:
                        su = sp if sp.startswith("http") else base + sp
                        sr = dash["session"].get(su, timeout=5)
                        sk = re.search(r'sesskey=([A-Za-z0-9+/=]+)', sr.text)
                        if not sk:
                            sk = re.search(r'sesskey["\'\s:=]+([a-zA-Z0-9+/=]{10,})', sr.text)
                        if sk:
                            dash["sesskey"] = sk.group(1)
                            print(f"[{dash.get('name','')}] 🔑 sesskey OK")
                            break
                    except:
                        continue
                return True
            else:
                dash["is_logged_in"] = False
                print(f"[{dash.get('name','')}] ❌ فشل تسجيل الدخول - URL: {resp.url}")
                return False
        except Exception as e:
            raise
    try:
        return retry_request(do_login, max_retries=3, retry_delay=5)
    except:
        dash["is_logged_in"] = False
        return False

def _do_ims_login(dash):
    """تسجيل دخول للوحات etkk مثل Fly Panel New"""
    try:
        dash_timeout = dash.get("timeout", 10)
        login_page_url = dash.get("login_page_url","")
        login_post_url = dash.get("login_post_url","")
        if not login_page_url:
            return False
        if not dash.get("session"):
            dash["session"] = requests.Session()
        resp = dash["session"].get(login_page_url, timeout=dash_timeout)
        if resp.status_code != 200:
            return False
        soup = BeautifulSoup(resp.text, "html.parser")
        etkk_input = soup.find("input", {"name": "etkk"})
        etkk_value = etkk_input.get("value", "") if etkk_input else ""
        captcha_answer = None
        m = re.search(r'What is (\d+)\s*\+\s*(\d+)', resp.text, re.IGNORECASE)
        if m:
            captcha_answer = int(m.group(1)) + int(m.group(2))
        else:
            for txt in soup.stripped_strings:
                m2 = re.search(r'(\d+)\s*\+\s*(\d+)', txt)
                if m2:
                    captcha_answer = int(m2.group(1)) + int(m2.group(2))
                    break
        if captcha_answer is None:
            return False
        payload = {
            "username": dash.get("username",""),
            "password": dash.get("password",""),
            "capt": str(captcha_answer),
            "etkk": etkk_value,
        }
        r2 = dash["session"].post(login_post_url, data=payload,
                    headers={"Referer": login_page_url, "Content-Type": "application/x-www-form-urlencoded"},
                    timeout=dash_timeout, allow_redirects=True)
        if "agent/SMS" in r2.url or "dashboard" in r2.url.lower() or "logout" in r2.text.lower():
            dash["is_logged_in"] = True
            dash["_login_time"] = time.time()
            try:
                dash_url = dash.get("dashboard_url","")
                if dash_url:
                    sr = dash["session"].get(dash_url, timeout=dash_timeout)
                    sk = _extract_sesskey(dash, sr.text)
                    if sk:
                        dash["sesskey"] = sk
            except:
                pass
            return True
        dash["is_logged_in"] = False
        return False
    except:
        dash["is_logged_in"] = False
        return False

def build_ajax_url_for_dashboard(dash, wide_range=False):
    if wide_range:
        start_date = date.today() - timedelta(days=3650)
        end_date   = date.today() + timedelta(days=1)
    else:
        start_date = date.today() - timedelta(days=1)
        end_date   = date.today() + timedelta(days=1)
    fdate1 = f"{start_date.strftime('%Y-%m-%d')} 00:00:00"
    fdate2 = f"{end_date.strftime('%Y-%m-%d')} 23:59:59"
    sesskey_part = ""
    sk = dash.get("sesskey")
    if sk:
        sesskey_part = f"sesskey={quote_plus(sk)}&"
    base_ajax = dash.get("ajax_url") or (dash.get("base_url") + dash["ajax_path"] if dash.get("base_url") and dash.get("ajax_path") else None)
    if not base_ajax:
        return None
    q = (f"{sesskey_part}fdate1={quote_plus(fdate1)}&fdate2={quote_plus(fdate2)}&frange=&fclient=&fnum=&fcli=&fgdate=&fgmonth=&fgrange="
         f"&fgclient=&fgnumber=&fgcli=&fg=0&sEcho=1&iColumns=9&sColumns=%2C%2C%2C%2C%2C%2C%2C%2C&iDisplayStart=0&iDisplayLength=5000"
         f"&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&mDataProp_4=4&mDataProp_5=5&mDataProp_6=6&mDataProp_7=7&mDataProp_8=8"
         f"&sSearch=&bRegex=false&iSortCol_0=0&sSortDir_0=desc&iSortingCols=1&_={int(time.time()*1000)}")
    return base_ajax + "?" + q

def fetch_ajax_json_for_dashboard(dash, url):
    if not url:
        return None
    dash_timeout = min(dash.get("timeout", 6), 8)
    if "_fail_count" not in dash:
        dash["_fail_count"] = 0
    def do_fetch():
        r = dash["session"].get(url, timeout=dash_timeout)
        if r.status_code == 403 or ("login" in r.url.lower()):
            raise Exception("Session expired")
        r.raise_for_status()
        try:
            result = r.json()
            dash["_fail_count"] = 0
            return result
        except (json.JSONDecodeError, Exception):
            new_sk = re.search(r'sesskey["\'\s:=]+([a-zA-Z0-9+/=]{10,})', r.text)
            if new_sk:
                dash["sesskey"] = new_sk.group(1)
            raise Exception("Invalid JSON - need new sesskey")
    try:
        result = do_fetch()
        return result
    except Exception as e:
        dash["_fail_count"] = dash.get("_fail_count", 0) + 1
        if "Session expired" in str(e) or dash["_fail_count"] >= 3:
            dash["_fail_count"] = 0
            dash["is_logged_in"] = False
            dash["sesskey"] = None
            if login_for_dashboard(dash):
                dash["is_logged_in"] = True
                try:
                    return do_fetch()
                except:
                    return None
            else:
                return None
        return None

def extract_rows_from_json(j):
    if j is None:
        return []
    for key in ("data", "aaData", "rows", "aa_data"):
        if isinstance(j, dict) and key in j:
            return j[key]
    if isinstance(j, list):
        return j
    if isinstance(j, dict):
        for v in j.values():
            if isinstance(v, list):
                return v
    return []

def fetch_api_token_rows(dash):
    try:
        url = dash.get("api_url")
        if not url:
            return []
        r = dash["session"].get(url, params={"token": dash["api_token"]}, timeout=8)
        if r.status_code != 200:
            return []
        j = r.json()
        rows = []
        for key in ("data", "aaData", "rows", "result"):
            if isinstance(j, dict) and key in j and isinstance(j[key], list):
                rows = j[key]
                break
        if not rows and isinstance(j, list):
            rows = j
        return rows
    except Exception as e:
        return []

def row_to_tuple(row, dash):
    date_str = number_str = sms_str = ""
    idx_date = dash.get("idx_date", 0)
    idx_number = dash.get("idx_number", 2)
    idx_sms = dash.get("idx_sms", 5)
    if isinstance(row, (list, tuple)):
        if len(row) > idx_date:   date_str   = clean_html(str(row[idx_date]))
        if len(row) > idx_number: number_str = clean_number(str(row[idx_number]))
        if len(row) > idx_sms:    sms_str    = clean_html(str(row[idx_sms]))
    elif isinstance(row, dict):
        keys = dash.get("data_keys", {})
        date_key = keys.get("date")
        if date_key and date_key in row:
            date_str = clean_html(str(row[date_key]))
        else:
            for k in ("date","time","datetime","dt","created_at"):
                if k in row: date_str = clean_html(str(row[k])); break
        num_key = keys.get("number")
        if num_key and num_key in row:
            number_str = clean_number(str(row[num_key]))
        else:
            for k in ("number","msisdn","cli","from","sender"):
                if k in row: number_str = clean_number(str(row[k])); break
        sms_key = keys.get("sms")
        if sms_key and sms_key in row:
            sms_str = clean_html(str(row[sms_key]))
        else:
            for k in ("sms","message","msg","body","text"):
                if k in row: sms_str = clean_html(str(row[k])); break
    unique_key = f"{number_str}|{sms_str}"
    return date_str, number_str, sms_str, unique_key

def parse_api_token_row(dash, row):
    keys = dash.get("data_keys") or {}
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    number = sms = ""
    if isinstance(row, dict):
        date_key = keys.get("date")
        if date_key and date_key in row:
            date_str = str(row[date_key])
        num_key = keys.get("number", "num")
        if num_key in row:
            number = clean_number(str(row[num_key]))
        sms_key = keys.get("sms", "message")
        if sms_key in row:
            sms = clean_html(str(row[sms_key]))
    elif isinstance(row, (list, tuple)):
        i_date   = dash.get("idx_date", 0)
        i_number = dash.get("idx_number", 2)
        i_sms    = dash.get("idx_sms", 5)
        if len(row) > i_date:   date_str = clean_html(str(row[i_date]))
        if len(row) > i_number: number   = clean_number(str(row[i_number]))
        if len(row) > i_sms:    sms      = clean_html(str(row[i_sms]))
    key = f"{number}|{sms}"
    return date_str, number, sms, key

def retry_request(func, max_retries=1, retry_delay=0):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                raise

def _extract_sesskey(dash, resp_text):
    m = re.search(r'sesskey["\s:=\']+([a-zA-Z0-9+/=]+)', resp_text)
    if m:
        return m.group(1)
    return None

def login_for_ims_panel(dash):
    """تسجيل دخول للوحات النوع ims_panel و ims_client مع حل الكابتشا الرياضي و etkk"""
    try:
        dash["session"] = requests.Session()
        dash["session"].headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
        })
        dash_timeout = dash.get("timeout", 15)
        login_page_url = dash["login_page_url"]
        login_post_url = dash["login_post_url"]

        # ── جلب صفحة الدخول ──
        resp = dash["session"].get(login_page_url, timeout=dash_timeout)
        if resp.status_code != 200:
            print(f"[{dash['name']}] ❌ فشل جلب صفحة الدخول (HTTP {resp.status_code})")
            return False

        page_text = resp.text
        soup = BeautifulSoup(page_text, "html.parser")

        # ── استخراج etkk ──
        etkk_value = ""
        etkk_input = soup.find("input", {"name": "etkk"})
        if etkk_input:
            etkk_value = etkk_input.get("value", "")
        else:
            m_etkk = re.search(r'name=["\']etkk["\']\s*value=["\']([^"\']+)["\']', page_text)
            if m_etkk:
                etkk_value = m_etkk.group(1)

        # ── حل الكابتشا الرياضي ──
        captcha_answer = None
        match = re.search(r'What is\s*(\d+)\s*\+\s*(\d+)', page_text, re.IGNORECASE)
        if match:
            captcha_answer = int(match.group(1)) + int(match.group(2))
        else:
            for t in soup.stripped_strings:
                m2 = re.search(r'(\d+)\s*\+\s*(\d+)', t)
                if m2:
                    captcha_answer = int(m2.group(1)) + int(m2.group(2))
                    break
        if captcha_answer is None:
            m3 = re.search(r'(\d+)\s*\+\s*(\d+)', page_text)
            if m3:
                captcha_answer = int(m3.group(1)) + int(m3.group(2))
        if captcha_answer is None:
            captcha_answer = ""
            print(f"[{dash['name']}] ⚠️ لم يُوجد captcha - سيتم المحاولة بدونه")

        print(f"[{dash['name']}] 🔐 كابتشا={captcha_answer}, etkk={etkk_value[:10] if etkk_value else 'none'}")

        # ── إرسال بيانات الدخول ──
        payload = {
            "username": dash["username"],
            "password": dash["password"],
            "capt":     str(captcha_answer),
        }
        if etkk_value:
            payload["etkk"] = etkk_value

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer":      login_page_url,
            "Origin":       dash.get("base_url", "").rstrip("/"),
        }
        resp2 = dash["session"].post(login_post_url, data=payload, headers=headers,
                                     timeout=dash_timeout, allow_redirects=True)
        final_url  = resp2.url
        final_text = resp2.text

        # ── التحقق من النجاح ──
        success = (
            "Dashboard" in final_text or
            "Logout"    in final_text or
            "/client"   in final_url.lower() or
            "/agent"    in final_url.lower() or
            "dashboard" in final_url.lower()
        )
        if success:
            dash["is_logged_in"] = True
            dash["last_login_time"] = time.time()
            dash["sesskey"] = None
            print(f"[{dash['name']}] ✅ تسجيل دخول ناجح → {final_url}")
            return True
        else:
            dash["is_logged_in"] = False
            # طباعة سبب الفشل إن وُجد
            err = re.search(r'<(?:div|span|p)[^>]*class=["\'][^"\']*(?:alert|error|danger|warning)[^"\']*["\'][^>]*>(.*?)</', final_text, re.DOTALL | re.IGNORECASE)
            if err:
                clean = re.sub('<[^<]+?>', '', err.group(1)).strip()
                print(f"[{dash['name']}] ❌ الخادم: {clean}")
            elif "Incorrect Answer" in final_text or "captcha" in final_text.lower():
                print(f"[{dash['name']}] ❌ خطأ في الكابتشا")
            elif "Invalid" in final_text:
                print(f"[{dash['name']}] ❌ بيانات دخول خاطئة")
            else:
                print(f"[{dash['name']}] ❌ فشل الدخول → {final_url}")
            return False

    except Exception as e:
        dash["is_logged_in"] = False
        print(f"[{dash['name']}] ❌ خطأ في الدخول: {e}")
        return False

def _extract_sk(text):
    for pat in [
        r'sesskey=([a-zA-Z0-9+/=_-]{10,})',
        r'sesskey[\s:="\']+([a-zA-Z0-9+/=_-]{10,})',
    ]:
        m = re.search(pat, text, re.IGNORECASE)
        if m and len(m.group(1).strip()) >= 10:
            return m.group(1).strip()
    return None

def _ims_login_and_sesskey(dash):
    if not login_for_ims_panel(dash):
        return False
    dash_url = dash.get("dashboard_url", "")
    if not dash_url:
        print(f"[{dash['name']}] ❌ dashboard_url مش محدد")
        return False
    try:
        r = dash["session"].get(dash_url, timeout=dash.get("timeout", 30))
        sk = _extract_sk(r.text)
        if sk:
            dash["sesskey"] = sk
            print(f"[{dash['name']}] 🔑 sesskey OK: {sk[:15]}...")
            return True
        # محاولة ثانية على صفحة CDRs
        base = dash.get("base_url", "").rstrip("/")
        dash_type = dash.get("type", "")
        cdrs_path = "/client/SMSCDRs" if dash_type == "ims_client" else "/agent/SMSCDRs"
        r2 = dash["session"].get(base + cdrs_path, timeout=dash.get("timeout", 30))
        sk2 = _extract_sk(r2.text)
        if sk2:
            dash["sesskey"] = sk2
            print(f"[{dash['name']}] 🔑 sesskey OK (CDRs): {sk2[:15]}...")
            return True
        print(f"[{dash['name']}] ❌ login نجح لكن sesskey مش موجود - سيتم إعادة المحاولة")
        dash["is_logged_in"] = False
        return False
    except Exception as e:
        print(f"[{dash['name']}] ❌ خطأ في استخراج sesskey: {e}")
        dash["is_logged_in"] = False
        return False

def fetch_ims_panel_data(dash):
    try:
        if not dash.get("is_logged_in") or not dash.get("sesskey") or not dash.get("session"):
            if not _ims_login_and_sesskey(dash):
                return dash["name"], []

        last_fetch = dash.get("_last_fetch_time")
        if last_fetch and isinstance(last_fetch, datetime):
            if last_fetch.date() < date.today():
                fdate1 = datetime.combine(date.today(), datetime.min.time()).strftime("%Y-%m-%d %H:%M:%S")
            else:
                fdate1 = (last_fetch + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            fdate1 = datetime.combine(date.today(), datetime.min.time()).strftime("%Y-%m-%d %H:%M:%S")

        fdate2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        params = {
            "sesskey":        dash["sesskey"],
            "fdate1":         fdate1,
            "fdate2":         fdate2,
            "frange":         "",
            "fclient":        "",
            "fnum":           "",
            "fcli":           "",
            "fg":             "0",
            "sEcho":          "1",
            "iColumns":       "9",
            "sColumns":       ",,,,,,,,",
            "iDisplayStart":  "0",
            "iDisplayLength": str(dash.get("records", 10)),
            "mDataProp_0": "0", "mDataProp_1": "1", "mDataProp_2": "2",
            "mDataProp_3": "3", "mDataProp_4": "4", "mDataProp_5": "5",
            "mDataProp_6": "6", "mDataProp_7": "7", "mDataProp_8": "8",
            "sSearch":        "",
            "bRegex":         "false",
            "iSortCol_0":     "0",
            "sSortDir_0":     "desc",
            "iSortingCols":   "1",
            "_":              str(int(time.time() * 1000)),
        }

        dash["session"].headers.update({
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": dash.get("dashboard_url", ""),
        })

        resp = dash["session"].get(
            dash["ajax_url"], params=params,
            timeout=dash.get("timeout", 8)
        )

        if resp.status_code == 403 or "login" in resp.url.lower():
            print(f"[{dash['name']}] 🔄 session انتهت - إعادة login")
            dash["is_logged_in"] = False
            dash["sesskey"] = None
            return dash["name"], []

        try:
            data = resp.json()
        except Exception:
            sk = _extract_sk(resp.text)
            if sk:
                dash["sesskey"] = sk
                print(f"[{dash['name']}] 🔄 sesskey مُجدد من response")
            else:
                dash["is_logged_in"] = False
                dash["sesskey"] = None
            return dash["name"], []

        rows = data.get("aaData", data.get("data", []))

        entries = []
        max_dt = None
        for row in rows:
            date_val, num_val, sms_val, key = row_to_tuple(row, dash)
            if date_val and num_val and sms_val and len(num_val) >= 7:
                entries.append((date_val, num_val, sms_val, key))
                try:
                    dt = datetime.strptime(date_val, "%Y-%m-%d %H:%M:%S")
                    if max_dt is None or dt > max_dt:
                        max_dt = dt
                except:
                    pass

        if max_dt:
            dash["_last_fetch_time"] = max_dt

        if entries:
            entries.sort(key=lambda x: x[0], reverse=True)
            return dash["name"], entries[:20]

        return dash["name"], []
    except Exception as e:
        print(f"[{dash['name']}] ❌ خطأ في الجلب: {e}")
        dash["is_logged_in"] = False
        return dash["name"], []

def fetch_ims_client_data(dash):
    """لوحة imssms.org - client panel - 7 columns, idx_sms=4"""
    try:
        # تحقق من الـ session والـ sesskey
        if not dash.get("is_logged_in") or not dash.get("sesskey") or not dash.get("session"):
            if not _ims_login_and_sesskey(dash):
                return dash["name"], []

        last_fetch = dash.get("_last_fetch_time")
        if last_fetch and isinstance(last_fetch, datetime):
            if last_fetch.date() < date.today():
                fdate1 = datetime.combine(date.today(), datetime.min.time()).strftime("%Y-%m-%d %H:%M:%S")
            else:
                fdate1 = (last_fetch + timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            fdate1 = (datetime.now() - timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")

        fdate2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        params = {
            "fdate1":         fdate1,
            "fdate2":         fdate2,
            "frange":         "", "fnum": "", "fcli": "",
            "fgdate":         "", "fgmonth": "", "fgrange": "",
            "fgnumber":       "", "fgcli": "", "fg": "0",
            "sesskey":        dash.get("sesskey", ""),
            "sEcho":          "1",
            "iColumns":       "7",
            "sColumns":       ",,,,,,",
            "iDisplayStart":  "0",
            "iDisplayLength": str(dash.get("records", 50)),
            "iSortCol_0":     "0",
            "sSortDir_0":     "desc",
            "sSearch":        "",
            "bRegex":         "false",
        }

        dashboard_url = dash["base_url"].rstrip("/") + dash.get("dashboard_path", "/client/SMSCDRStats")
        ajax_url      = dash["base_url"].rstrip("/") + dash.get("ajax_path", "/client/res/data_smscdr.php")

        dash["session"].headers.update({
            "Accept":           "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer":          dashboard_url,
        })

        resp = dash["session"].get(ajax_url, params=params, timeout=dash.get("timeout", 15))

        # ── اكتشاف إعادة التوجيه لصفحة الدخول ──
        if resp.status_code in (302, 403):
            print(f"[{dash['name']}] 🔄 session انتهت (HTTP {resp.status_code}) - إعادة login")
            dash["is_logged_in"] = False
            dash["sesskey"] = None
            return dash["name"], []

        if resp.status_code == 503:
            print(f"[{dash['name']}] ⏳ 503 - سيرفر غير متاح")
            return dash["name"], []

        resp_text = resp.text

        # لو الرد HTML بدل JSON → session منتهية
        if "<!DOCTYPE html>" in resp_text or ("login" in resp_text.lower() and "<html" in resp_text.lower()):
            print(f"[{dash['name']}] 🔄 رُدَّ بـ HTML (session منتهية) - إعادة login")
            dash["is_logged_in"] = False
            dash["sesskey"] = None
            if _ims_login_and_sesskey(dash):
                return fetch_ims_client_data(dash)
            return dash["name"], []

        try:
            data = resp.json()
        except Exception:
            print(f"[{dash['name']}] ❌ JSON parse error: {resp_text[:120]}")
            dash["is_logged_in"] = False
            dash["sesskey"] = None
            return dash["name"], []

        rows = data.get("aaData", data) if isinstance(data, dict) else data
        if not isinstance(rows, list):
            return dash["name"], []

        # columns: [0]=dt [1]=service [2]=num [3]=cli [4]=msg
        idx_d = dash.get("idx_date", 0)
        idx_n = dash.get("idx_number", 2)
        idx_s = dash.get("idx_sms", 4)

        entries = []
        max_dt = None
        for row in rows:
            if not isinstance(row, list) or len(row) <= idx_s:
                continue
            date_val = str(row[idx_d]).strip()
            num_val  = re.sub(r'\D', '', str(row[idx_n]))
            sms_val  = str(row[idx_s]).strip()
            if not date_val or not num_val or not sms_val or len(num_val) < 7:
                continue
            key = f"{date_val}|{num_val}|{sms_val[:20]}"
            entries.append((date_val, num_val, sms_val, key))
            try:
                dt = datetime.strptime(date_val, "%Y-%m-%d %H:%M:%S")
                if max_dt is None or dt > max_dt:
                    max_dt = dt
            except:
                pass

        if max_dt:
            dash["_last_fetch_time"] = max_dt

        if entries:
            entries.sort(key=lambda x: x[0], reverse=True)
            return dash["name"], entries[:50]

        return dash["name"], []

    except Exception as e:
        print(f"[{dash['name']}] ❌ خطأ: {e}")
        dash["is_logged_in"] = False
        return dash["name"], []


def fetch_dashboard_data(dash):
    name = dash["name"]
    try:
        dtype = dash.get("type", "traditional")

        if dtype == "ims_panel":
            return fetch_ims_panel_data(dash)

        if dtype == "ims_client":
            return fetch_ims_client_data(dash)

        if dtype in ("api_token", "api"):
            rows = fetch_api_token_rows(dash)
            entries = []
            for row in rows:
                date_str, number, sms, key = parse_api_token_row(dash, row)
                if number and sms and len(number) >= 7:
                    entries.append((date_str, number, sms, key))
            if entries:
                entries.sort(key=lambda x: x[0], reverse=True)
                return name, entries[:20]
            return name, []

        if not dash.get("is_logged_in"):
            if not login_for_dashboard(dash):
                return name, []

        url = build_ajax_url_for_dashboard(dash)
        j = fetch_ajax_json_for_dashboard(dash, url)
        rows = extract_rows_from_json(j)

        valid_rows = []
        for row in rows:
            if isinstance(row, (list, tuple, dict)):
                date_val, num_val, sms_val, _ = row_to_tuple(row, dash)
                if (date_val and num_val and sms_val
                        and len(num_val) >= 7
                        and len(sms_val) > 2):
                    valid_rows.append(row)

        if valid_rows:
            def get_dt(r):
                try:
                    dt, _, _, _ = row_to_tuple(r, dash)
                    return datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
                except:
                    return datetime.min
            valid_rows.sort(key=get_dt, reverse=True)
            entries = []
            for row in valid_rows[:20]:
                d2, n2, s2, k2 = row_to_tuple(row, dash)
                if n2 and s2:
                    entries.append((d2, n2, s2, k2))
            return name, entries
        return name, []

    except Exception as e:
        print(f"[{name}] ⚠️ fetch error: {e}")
        if dash.get("is_logged_in"):
            dash["is_logged_in"] = False
        return name, []

from requests.adapters import HTTPAdapter

def _tune_session(sess):
    adapter = HTTPAdapter(
        pool_connections=10,
        pool_maxsize=20,
        max_retries=0,
    )
    sess.mount("http://",  adapter)
    sess.mount("https://", adapter)
    sess.headers.update({
        "Connection":        "keep-alive",
        "Accept-Encoding":   "gzip, deflate",
        "Accept":            "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language":   "en-US,en;q=0.9",
    })

def _make_dash(d):
    def _bu(base, path):
        if not path: return ""
        if path.startswith("http"): return path
        return base.rstrip("/") + path if base else path

    dtype = d.get("type", "traditional")
    if dtype in ("api_token", "api"):
        d["is_logged_in"] = True
        d["session"] = requests.Session()
        d["session"].headers.update(COMMON_HEADERS)
        _tune_session(d["session"])
    elif dtype == "ims_panel":
        d["session"] = requests.Session()
        d["session"].headers.update(COMMON_HEADERS)
        _tune_session(d["session"])
        d["is_logged_in"] = False
        d["sesskey"] = None
        d["phpsessid"] = None
        d["last_login_time"] = 0
        d["_last_fetch_time"] = None
        d["login_page_url"] = _bu(d.get("base_url",""), d.get("login_page",""))
        d["login_post_url"] = _bu(d.get("base_url",""), d.get("login_post",""))
        d["ajax_url"]       = _bu(d.get("base_url",""), d.get("ajax_path",""))
        d["dashboard_url"]  = _bu(d.get("base_url",""), d.get("dashboard_path",""))
    else:
        d["session"] = requests.Session()
        d["session"].headers.update(COMMON_HEADERS)
        _tune_session(d["session"])
        d["is_logged_in"] = False
        d["sesskey"] = None
        d["login_page_url"] = _bu(d.get("base_url",""), d.get("login_page",""))
        d["login_post_url"] = _bu(d.get("base_url",""), d.get("login_post",""))
        d["ajax_url"]       = _bu(d.get("base_url",""), d.get("ajax_path",""))
    return d

def _init_all_dashboards():
    all_dash = []
    for dash in STATIC_DASHBOARDS:
        dtype = dash.get("type", "traditional")
        if dtype in ("api_token", "api"):
            if not dash.get("api_token") and not dash.get("api_url"):
                print(f"[SKIP] {dash['name']} - لا يوجد API token/url")
                continue
        elif dtype == "ims_panel":
            if not dash.get("username") or not dash.get("password"):
                print(f"[SKIP] {dash['name']} - لا يوجد يوزر/باسورد")
                continue
        else:
            if not dash.get("username") or not dash.get("password"):
                print(f"[SKIP] {dash['name']} - لا يوجد يوزر/باسورد")
                continue
        d = dash.copy()
        d = _make_dash(d)
        all_dash.append(d)
        print(f"[INIT] ✅ {d['name']}")

    for db_dash in get_db_dashboards(only_active=True):
        d = db_dash.copy()
        d = _make_dash(d)
        all_dash.append(d)
        print(f"[INIT DB] ✅ {d['name']}")

    print(f"[INIT] إجمالي اللوحات: {len(all_dash)}")
    return all_dash

def _get_db_dashboards_initialized():
    result = []
    for db_dash in get_db_dashboards(only_active=True):
        d = db_dash.copy()
        d = _make_dash(d)
        result.append(d)
    return result

def main_loop():
    sent_messages = set()
    last_fetch_time = {}
    _today_sent_file = "sent_today.json"
    _main_current_day = date.today()

    try:
        if os.path.exists(_today_sent_file):
            with open(_today_sent_file, "r") as f:
                data = json.load(f)
                saved_date = data.get("date", "")
                if saved_date == str(date.today()):
                    sent_messages = set(data.get("keys", []))
                    print(f"[INIT] ✅ تم تحميل {len(sent_messages)} key من اليوم - منع التكرار")
    except:
        pass

    def _save_sent():
        try:
            with open(_today_sent_file, "w") as f:
                json.dump({"date": str(date.today()), "keys": list(sent_messages)[-5000:]}, f)
        except:
            pass

    print("=" * 60)
    print(f"🚀 بدء مراقبة اللوحات (MAX_WORKERS={MAX_WORKERS})")
    print("=" * 60)

    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    active_dashboards = _init_all_dashboards()

    # ── Rich terminal panel status table ──
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    RED     = "\033[91m"
    YELLOW  = "\033[93m"
    MAGENTA = "\033[95m"
    BOLD    = "\033[1m"
    RESET   = "\033[0m"
    DIM     = "\033[2m"

    def _print_panel_table(dashboards, phase="LOGIN"):
        print(f"\n{CYAN}{BOLD}{'━'*72}{RESET}")
        print(f"{CYAN}{BOLD}  📡 PANEL STATUS TABLE  [{phase}]{RESET}")
        print(f"{CYAN}{'━'*72}{RESET}")
        header = f"  {'#':<3}  {'Panel Name':<22}  {'Type':<12}  {'User':<18}  {'Status'}"
        print(f"{BOLD}{header}{RESET}")
        print(f"{DIM}  {'─'*3}  {'─'*22}  {'─'*12}  {'─'*18}  {'─'*16}{RESET}")
        for i, d in enumerate(dashboards, 1):
            dtype = d.get("type","traditional")
            uname = d.get("username","") or "API"
            if dtype in ("api_token","api"):
                status = f"{GREEN}✅ API Ready{RESET}"
            elif d.get("is_logged_in"):
                status = f"{GREEN}✅ Logged In{RESET}"
            else:
                status = f"{RED}❌ Not Logged In{RESET}"
            name  = d.get("name","?")[:22]
            dtype_s = dtype[:12]
            uname_s = uname[:18]
            print(f"  {YELLOW}{i:<3}{RESET}  {name:<22}  {DIM}{dtype_s:<12}{RESET}  {MAGENTA}{uname_s:<18}{RESET}  {status}")
        print(f"{CYAN}{'━'*72}{RESET}\n")

    print(f"\n{BOLD}🔐 تسجيل الدخول لكل اللوحات...{RESET}")
    for dash in active_dashboards:
        if dash.get("type") in ("api_token", "api"):
            print(f"[{dash['name']}] ✅ API Token جاهز")
        else:
            if login_for_dashboard(dash):
                print(f"[{dash['name']}] ✅ دخل بنجاح")
            else:
                print(f"[{dash['name']}] ⚠️ فشل الدخول - سيُعاد لاحقاً")

    _print_panel_table(active_dashboards, phase="AFTER LOGIN")

    print("\n🔍 جلب آخر رسالة من كل لوحة...")
    for dash in active_dashboards:
        if not dash.get("is_logged_in") and dash.get("type") not in ("api_token", "api"):
            continue
        try:
            if dash.get("type") in ("api_token", "api"):
                _, entries = fetch_dashboard_data(dash)
            else:
                url = build_ajax_url_for_dashboard(dash, wide_range=True)
                j = fetch_ajax_json_for_dashboard(dash, url)
                rows = extract_rows_from_json(j)
                entries = []
                for row in rows:
                    d2, n2, s2, k2 = row_to_tuple(row, dash)
                    if n2 and s2 and len(n2) >= 7:
                        entries.append((d2, n2, s2, k2))
                if entries:
                    try:
                        entries.sort(key=lambda x: datetime.strptime(x[0], "%Y-%m-%d %H:%M:%S"), reverse=True)
                    except:
                        pass

            if entries:
                new_sent = 0
                for date_str, number, sms, key in entries:
                    if key not in sent_messages:
                        sent_messages.add(key)
                        print(f"[{dash['name']}] 📩 كود جديد: {mask_number(number)}")
                        send_otp_to_user_and_group(date_str, number, sms,
                            panel_name=dash["name"],
                            short_bold=dash.get("short_bold", to_bold(dash.get("short","??"))))
                        new_sent += 1
                if new_sent == 0:
                    print(f"[{dash['name']}] ✅ لا يوجد جديد (تم بعتها قبل الريستارت)")
        except Exception as e:
            print(f"[{dash['name']}] ⚠️ خطأ أولي: {e}")

    print(f"\n✅ بدء المراقبة المستمرة...\n" + "="*60)

    last_db_check = time.time()

    while True:
        try:
            now = time.time()

            _main_new_day = date.today()
            if _main_new_day != _main_current_day:
                print(f"[main_loop] 🌅 يوم جديد ({_main_new_day}) - تصفير الأكواد المبعوتة")
                sent_messages.clear()
                _main_current_day = _main_new_day
                for dash in active_dashboards:
                    if dash.get("type") not in ("api_token", "api"):
                        dash["is_logged_in"] = False
                        dash["sesskey"] = None
                        dash["_last_fetch_time"] = None
                _save_sent()
                # إعادة login لكل اللوحات التقليدية بعد منتصف الليل
                def _midnight_relogin(all_dashes):
                    for _d in all_dashes:
                        if _d.get("type") not in ("api_token", "api"):
                            try:
                                ok = login_for_dashboard(_d)
                                print(f"[midnight] {'✅' if ok else '❌'} re-login {_d['name']}")
                            except Exception as _e:
                                print(f"[midnight] ⚠️ {_d['name']}: {_e}")
                threading.Thread(target=_midnight_relogin, args=(list(active_dashboards),), daemon=True).start()

            if now - last_db_check >= 30:
                new_db = _get_db_dashboards_initialized()
                existing_names = {d["name"] for d in active_dashboards}
                for d in new_db:
                    if d["name"] not in existing_names:
                        active_dashboards.append(d)
                        print(f"[+] لوحة جديدة من DB: {d['name']}")
                        if d.get("type") not in ("api_token", "api"):
                            login_for_dashboard(d)
                last_db_check = now

            dashboards_to_fetch = []
            for dash in active_dashboards:
                ukey = f"{dash['name']}|{dash.get('username', 'api')}"
                dash["_ukey"] = ukey
                interval = dash.get("refresh_interval", 1)
                if now - last_fetch_time.get(ukey, 0) >= interval:
                    dashboards_to_fetch.append(dash)
                    last_fetch_time[ukey] = now

            if not dashboards_to_fetch:
                time.sleep(0.01)
                continue

            futures = {executor.submit(fetch_dashboard_data, dash): dash
                       for dash in dashboards_to_fetch}

            for future in as_completed(futures, timeout=8):
                dash = futures[future]
                try:
                    name, entries = future.result(timeout=6)
                    for date_str, number, sms, key in entries:
                        if key not in sent_messages:
                            _panel_box(name, mask_number(number), sms[:60], status="NEW")
                            sent_messages.add(key)
                            threading.Thread(
                                target=send_otp_to_user_and_group,
                                args=(date_str, number, sms),
                                kwargs={"panel_name": name, "short_bold": dash.get("short_bold", to_bold(dash.get("short","??")))},
                                daemon=True
                            ).start()
                            _save_sent()
                except Exception as e:
                    _panel_box(dash['name'], sms=str(e)[:50], status="ERR")

            if len(sent_messages) > 10000:
                sent_messages = set(list(sent_messages)[-8000:])
                _save_sent()
            if len(last_fetch_time) > 500:
                last_fetch_time = dict(list(last_fetch_time.items())[-300:])

        except KeyboardInterrupt:
            print("\n⛔ توقف يدوي")
            executor.shutdown(wait=False)
            break
        except Exception as e:
            print(f"⚠️ خطأ في الحلقة الرئيسية: {e}")
            time.sleep(0.1)

_ivas_logged_in = False
_ivas_session = None
_ivas_token = ""
_ivas_last_login = 0
_ivas_processed = set()

IVAS_BASE_URL = "https://www.ivasms.com"
IVAS_LOGIN_URL = IVAS_BASE_URL + "/login"
IVAS_RECV_URL = IVAS_BASE_URL + "/portal/sms/received"
IVAS_URL_RANGES = IVAS_BASE_URL + "/portal/sms/received/getsms"
IVAS_URL_NUMBERS = IVAS_BASE_URL + "/portal/sms/received/getsms/number"
IVAS_URL_SMS = IVAS_BASE_URL + "/portal/sms/received/getsms/number/sms"
IVAS_AJAX_HDRS = {
    "Referer": IVAS_RECV_URL, "Origin": IVAS_BASE_URL,
    "Accept": "text/html, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded",
}

def _ivas_refresh_token():
    global _ivas_token
    try:
        r = _ivas_session.get(IVAS_RECV_URL, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")
        t = soup.find("input", {"name": "_token"})
        if t:
            _ivas_token = t["value"]
        else:
            m = re.search(r'_token["\s:,]+["\']([a-zA-Z0-9]{20,})["\']', r.text)
            if m: _ivas_token = m.group(1)
    except Exception as e:
        print(f"[iVAS SMS] ⚠️ تحديث token: {e}")

def _ivas_do_login():
    global _ivas_session, _ivas_last_login, _ivas_token, _ivas_logged_in
    _ivas_session = requests.Session()
    _ivas_session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})
    resp = _ivas_session.get(IVAS_LOGIN_URL, timeout=15)
    soup = BeautifulSoup(resp.text, "html.parser")
    t = soup.find("input", {"name": "_token"})
    tv = t["value"] if t else ""
    r = _ivas_session.post(IVAS_LOGIN_URL, data={
        "_token": tv,
        "email": "",
        "password": "",
        "remember": "",
        "g-recaptcha-response": "",
    }, headers={"Referer": IVAS_LOGIN_URL, "Origin": IVAS_BASE_URL},
       timeout=15, allow_redirects=True)
    if "portal" not in r.url:
        print(f"[iVAS SMS] ❌ فشل الدخول → {r.url}")
        _ivas_logged_in = False
        return False
    _ivas_last_login = time.time()
    _ivas_token = tv
    _ivas_logged_in = True
    _ivas_refresh_token()
    print("[iVAS SMS] ✅ تسجيل دخول ناجح")
    return True

def _ivas_ensure_session():
    refresh_interval = 600
    if _ivas_session is None or (time.time() - _ivas_last_login) > refresh_interval:
        _ivas_do_login()
    else:
        _ivas_refresh_token()

def _ivas_fetch_all():
    global _ivas_token
    today = datetime.now().strftime("%Y-%m-%d")
    all_sms = []
    try:
        r = _ivas_session.post(IVAS_URL_RANGES,
            data={"_token": _ivas_token, "from": today, "to": today},
            headers=IVAS_AJAX_HDRS, timeout=15)
        if r.status_code != 200:
            return all_sms
        soup = BeautifulSoup(r.text, "html.parser")
        ranges = []
        for div in soup.find_all("div", class_="rng"):
            onclick = div.get("onclick", "")
            m = re.search(r"toggleRange\('([^']+)','([^']+)'\)", onclick)
            if m: ranges.append(m.group(1))
        m2 = re.search(r'_token["\s:,]+["\']([a-zA-Z0-9]{20,})["\']', r.text)
        if m2: _ivas_token = m2.group(1)
    except Exception as e:
        print(f"[iVAS SMS] ❌ fetch_ranges: {e}")
        return all_sms

    for range_name in ranges:
        try:
            r = _ivas_session.post(IVAS_URL_NUMBERS,
                data={"_token": _ivas_token, "start": today, "end": today, "range": range_name},
                headers=IVAS_AJAX_HDRS, timeout=15)
            numbers = re.findall(r"toggleNum\w+\('(\d{7,15})'", r.text)
            if not numbers:
                numbers = list(set(re.findall(r"\b(\d{9,15})\b", r.text)))
            m2 = re.search(r'_token["\s:,]+["\']([a-zA-Z0-9]{20,})["\']', r.text)
            if m2: _ivas_token = m2.group(1)
        except Exception as e:
            print(f"[iVAS SMS] ❌ fetch_numbers ({range_name}): {e}")
            continue

        for number in set(numbers):
            try:
                r = _ivas_session.post(IVAS_URL_SMS,
                    data={"_token": _ivas_token, "start": today, "end": today,
                          "Number": number, "Range": range_name},
                    headers=IVAS_AJAX_HDRS, timeout=15)
                m2 = re.search(r'_token["\s:,]+["\']([a-zA-Z0-9]{20,})["\']', r.text)
                if m2: _ivas_token = m2.group(1)
                soup2 = BeautifulSoup(r.text, "html.parser")
                for row in soup2.find_all("tr"):
                    cells = row.find_all("td")
                    if len(cells) < 3:
                        continue
                    sender_tag = cells[0].find(class_="cli-tag")
                    sender = sender_tag.get_text(strip=True) if sender_tag else cells[0].get_text(strip=True)
                    msg_tag = cells[1].find(class_="msg-text")
                    message = msg_tag.get_text(strip=True) if msg_tag else cells[1].get_text(strip=True)
                    t_str = cells[2].get_text(strip=True)
                    if not message:
                        continue
                    sms_id = hashlib.md5(f"{number}|{sender}|{message}|{t_str}".encode()).hexdigest()
                    all_sms.append({"id": sms_id, "number": number,
                                    "sender": sender, "message": message,
                                    "time_str": t_str, "range_name": range_name})
            except Exception as e:
                print(f"[iVAS SMS] ❌ fetch_sms ({number}): {e}")

    return all_sms

def ivas_monitor_loop():
    global _ivas_processed, _ivas_logged_in
    poll = 10
    print("[iVAS SMS] 🚀 بدء مراقبة iVAS SMS...")
    try:
        _ivas_do_login()
    except Exception as e:
        print(f"[iVAS SMS] ❌ فشل الدخول الأولي: {e}")
        _ivas_logged_in = False

    errors = 0
    while True:
        time.sleep(poll)
        try:
            _ivas_ensure_session()
            all_sms = _ivas_fetch_all()
            new_count = 0
            for rec in all_sms:
                if rec["id"] in _ivas_processed:
                    continue
                _ivas_processed.add(rec["id"])
                new_count += 1
                number = rec["number"]
                message = rec["message"]
                t_str = rec.get("time_str", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                sender = rec.get("sender", "")
                print(f"[iVAS SMS] 📩 {number[:6]}*** | {sender} | {message[:40]}")
                _panel_box("iVAS SMS", f"{number[:6]}***", message[:60], status="NEW")
                send_otp_to_user_and_group(t_str, number, message, panel_name="iVAS SMS", short_bold=to_bold("IV"))
            if len(_ivas_processed) > 20000:
                _ivas_processed = set(list(_ivas_processed)[-10000:])
            errors = 0
        except Exception as e:
            print(f"[iVAS SMS] ❌ خطأ: {e}")
            errors += 1
            if errors >= 5:
                print("[iVAS SMS] 🔄 إعادة تسجيل الدخول...")
                try:
                    _ivas_do_login()
                except:
                    pass
                errors = 0

PLATFORM_EMOJI_MAP = {
    "whatsapp":    "<tg-emoji emoji-id='5188683998125106802'>📞</tg-emoji>",
    "واتساب":      "<tg-emoji emoji-id='5188683998125106802'>📞</tg-emoji>",
    "واتس":        "<tg-emoji emoji-id='5188683998125106802'>📞</tg-emoji>",
    "facebook":    "<tg-emoji emoji-id='5323261730283863478'>📱</tg-emoji>",
    "فيسبوك":      "<tg-emoji emoji-id='5323261730283863478'>📱</tg-emoji>",
    "meta":        "<tg-emoji emoji-id='5323261730283863478'>📱</tg-emoji>",
    "instagram":   "<tg-emoji emoji-id='5319160079465857105'>📱</tg-emoji>",
    "انستقرام":    "<tg-emoji emoji-id='5319160079465857105'>📱</tg-emoji>",
    "انستا":       "<tg-emoji emoji-id='5319160079465857105'>📱</tg-emoji>",
    "telegram":    "<tg-emoji emoji-id='5471949924658588235'>👉</tg-emoji>",
    "تيليجرام":   "<tg-emoji emoji-id='5471949924658588235'>👉</tg-emoji>",
    "تلجرام":      "<tg-emoji emoji-id='5471949924658588235'>👉</tg-emoji>",
    "twitter":     "TW",
    "تويتر":       "TW",
    "x.com":       "TW",
    "snapchat":    "<tg-emoji emoji-id='5330248916224983855'>📱</tg-emoji>",
    "سناب":        "<tg-emoji emoji-id='5330248916224983855'>📱</tg-emoji>",
    "tiktok":      "<tg-emoji emoji-id='5327982530702359565'>📱</tg-emoji>",
    "تيك توك":    "<tg-emoji emoji-id='5327982530702359565'>📱</tg-emoji>",
    "google":      "GG",
    "جوجل":        "GG",
    "gmail":       "GG",
    "linkedin":    "LN",
    "لينكد":       "LN",
    "discord":     "DC",
    "ديسكورد":     "DC",
    "uber":        "UB",
    "bolt":        "BT",
    "careem":      "CR",
    "amazon":      "AZ",
    "netflix":     "<tg-emoji emoji-id='5318911503938634641'>📱</tg-emoji>",
    "spotify":     "SP",
    "apple":       "<tg-emoji emoji-id='5334955749409834455'>📱</tg-emoji>",
    "microsoft":   "MS",
    "paypal":      "<tg-emoji emoji-id='5364111181415996352'>📱</tg-emoji>",
    "binance":     "BN",
    "coinbase":    "CB",
}

def get_platform_emoji(sms_text):
    sms_lower = sms_text.lower()
    for keyword, emoji in PLATFORM_EMOJI_MAP.items():
        if keyword.lower() in sms_lower:
            return emoji
    return ""

def build_short_tag(number, country_upper):
    num_clean = number.strip().replace("+","").replace(" ","").replace("-","")
    if len(num_clean) >= 6:
        masked = num_clean[:3] + "●" * (len(num_clean) - 6) + num_clean[-3:]
    else:
        masked = num_clean
    first_letter = country_upper[0] if country_upper else "?"
    last_letter  = country_upper[-1] if country_upper else "?"
    return f"{first_letter}{last_letter}{masked}"

def mask_number(number):
    number = number.strip()
    if len(number) >= 6:
        start = number[:3]
        end = number[-3:]
        start_bold = to_bold(start)
        end_bold = to_bold(end)
        middle = "●" * (len(number) - 6)
        return f"{start_bold}{middle}{end_bold}"
    else:
        return number

def get_country_info(number, html=True):
    number = number.strip().replace("+","").replace(" ","").replace("-","")
    for code, (name, flag, upper_name) in sorted(COUNTRY_CODES.items(), key=lambda x: len(x[0]), reverse=True):
        if number.startswith(code):
            final_flag = get_flag_html(flag) if html else get_flag_plain(flag)
            return name, final_flag, upper_name
    return "Unknown", "🌍", "UNKNOWN"

def extract_otp(message):
    patterns = [
        r'(?:code|رمز|كود|verification|تحقق|otp|pin)[:\s]+[‎]?(\d{3,8}(?:[- ]\d{3,4})?)',
        r'(\d{3})[- ](\d{3,4})',
        r'\b(\d{4,8})\b',
        r'[‎](\d{3,8})',
    ]
    for pattern in patterns:
        match = re.search(pattern, message, re.IGNORECASE)
        if match:
            if len(match.groups()) > 1:
                return ''.join(match.groups())
            return match.group(1).replace(' ', '').replace('-', '')
    all_numbers = re.findall(r'\d{4,8}', message)
    if all_numbers:
        return all_numbers[0]
    return "N/A"

def clean_html(text):
    if not text: return ""
    return re.sub(r'<[^>]+>', '', str(text)).strip()

def clean_number(number):
    if not number: return ""
    return re.sub(r'\D', '', str(number))

def _make_colored_btn(text, color=None, **kwargs):
    return types.InlineKeyboardButton(text, **kwargs)

def _send_number_msg(chat_id, text, number, file_id, user_id, parse_mode="HTML"):
    """إرسال رسالة الرقم المُعين بـ raw API لضمان عمل CopyTextButton على زر نسخ الرقم"""
    import json as _json
    display_number = "+" + str(number).lstrip("+")
    keyboard = {
        "inline_keyboard": [
            [{"text": t("copy_number", user_id), "copy_text": {"text": display_number}, "icon_custom_emoji_id": "5793900849260400939"}],
            [{"text": t("change_number", user_id), "callback_data": f"change_num_{file_id}", "icon_custom_emoji_id": "5796690095511703420"}],
            [{"text": t("otp_group", user_id), "url": get_otp_group_link(), "icon_custom_emoji_id": "5990240193955765054"}],
            [{"text": t("back", user_id), "callback_data": "back_to_main", "icon_custom_emoji_id": "5386340832628462681"}],
        ]
    }
    payload = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": _json.dumps(keyboard),
        "parse_mode": parse_mode,
    }
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json=payload, timeout=15
        )
        return r.status_code == 200
    except Exception as e:
        print(f"[number_msg] ⚠️ {e}")
        return False

def _make_copy_btn(label, copy_value):
    """زر ينسخ القيمة مباشرة للكليبورد بدون popup"""
    try:
        return types.InlineKeyboardButton(
            label,
            copy_text=types.CopyTextButton(text=str(copy_value))
        )
    except Exception:
        return types.InlineKeyboardButton(label, callback_data=f"copy_fallback_{copy_value[:50]}")

def _send_copy_msg(chat_id, text, otp_code, extra_markup_rows=None, parse_mode="HTML", photo_bytes=None, number=None, voice_bytes=None):
    """إرسال رسالة مع زر COPY CODE + COPY NUMBER يعملان بالـ raw API لضمان عمل CopyTextButton"""
    first_row = [{"text": "𝗖𝗢𝗣𝗬 𝗖𝗢𝗗𝗘", "copy_text": {"text": str(otp_code)}, "icon_custom_emoji_id": "4938635821105284442"}]
    keyboard = {
        "inline_keyboard": [first_row]
    }
    if extra_markup_rows:
        for row in extra_markup_rows:
            keyboard["inline_keyboard"].append(row)
    import json as _json
    import io as _io
    payload = {
        "chat_id": chat_id,
        "reply_markup": _json.dumps(keyboard),
        "parse_mode": parse_mode,
    }
    try:
        if voice_bytes:
            # ── فويس + caption + كيبورد في رسالة واحدة ──
            r = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendVoice",
                data={**payload, "caption": text},
                files={"voice": ("otp.mp3", _io.BytesIO(voice_bytes), "audio/mpeg")},
                timeout=20
            )
        elif photo_bytes:
            r = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                data={**payload, "caption": text},
                files={"photo": ("img.jpg", _io.BytesIO(photo_bytes), "image/jpeg")},
                timeout=15
            )
        else:
            payload["text"] = text
            r = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                json=payload, timeout=15
            )
        if r.status_code == 200:
            return r.json().get("result", {})
    except Exception as e:
        print(f"[copy_btn] ⚠️ {e}")
    return None

def generate_otp_voice(otp_code, bot_name="NUMBER_X"):
    """
    توليد صوت AI يقرأ الكود بالإنجليزي + ترحيب في الآخر
    باستخدام Google TTS API مباشرة بدون مكتبات إضافية
    """
    try:
        # تحضير النص بشكل واضح للقراءة
        digits = " ".join(list(str(otp_code)))
        text = f"Your verification code is: {digits}. Welcome to {bot_name} bot."

        # Google TTS API
        import urllib.parse
        encoded = urllib.parse.quote(text)
        tts_url = (
            f"https://translate.google.com/translate_tts"
            f"?ie=UTF-8&q={encoded}&tl=en&client=tw-ob"
        )
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Referer": "https://translate.google.com/",
        }
        resp = requests.get(tts_url, headers=headers, timeout=15)
        if resp.status_code == 200 and len(resp.content) > 1000:
            return io.BytesIO(resp.content)
        return None
    except Exception as e:
        print(f"[voice] ⚠️ خطأ في توليد الصوت: {e}")
        return None


def send_otp_to_user_and_group(date_str, number, sms, panel_name="", short_bold=""):
    otp_code = extract_otp(sms)
    user_id = get_user_by_number(number)
    log_otp(number, otp_code, sms, user_id)

    country_name, country_flag, country_upper = get_country_info(number, html=True)
    platform_emoji = get_platform_emoji(sms)
    number_masked = mask_number(number)
    country_short = to_bold(country_upper[:2]) if country_upper else to_bold("??")
    if not short_bold:
        short_bold = to_bold("??")

    if user_id:
        try:
            try:
                bot_info = bot.get_me()
                bot_url = f"https://t.me/{bot_info.username}"
            except Exception:
                bot_url = "https://t.me/FK_AY"
            custom_btns_all = get_custom_buttons()
            channel_url = custom_btns_all[0][2] if custom_btns_all else bot_url
            msg_text = t("otp_user", user_id,
                         country_flag=country_flag,
                         platform_emoji=platform_emoji,
                         country_short=country_short,
                         number_masked=number_masked,
                         otp=otp_code)
            # بناء الكيبورد
            keyboard_rows = [
                [{"text": t("copy", user_id), "copy_text": {"text": str(otp_code)}, "icon_custom_emoji_id": "4938635821105284442"}],
                [{"text": "𝗙𝗨𝗟𝗟 𝗠𝗘𝗦𝗦𝗔𝗚𝗘", "copy_text": {"text": str(sms)}, "icon_custom_emoji_id": "5454386656628991407"}],
            ]
            group_btns = get_otp_group_buttons()
            for gbtn in group_btns:
                keyboard_rows.append([{"text": gbtn["text"], "url": gbtn["url"]}])
            import json as _json
            user_payload = {
                "chat_id": user_id,
                "reply_markup": _json.dumps({"inline_keyboard": keyboard_rows}),
                "parse_mode": "HTML",
            }
            user_msg_id = None
            import io as _io
            voice_buf = generate_otp_voice(otp_code, bot_name="NUMBER X")
            if voice_buf:
                # ── فويس + نص + كيبورد في رسالة واحدة ──
                _ures = requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendVoice",
                    data={**user_payload, "caption": msg_text},
                    files={"voice": ("otp.mp3", voice_buf, "audio/mpeg")},
                    timeout=20
                )
            elif BOT_IMAGE_BYTES:
                _ures = requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
                    data={**user_payload, "caption": msg_text},
                    files={"photo": ("img.jpg", _io.BytesIO(BOT_IMAGE_BYTES), "image/jpeg")},
                    timeout=15
                )
            else:
                user_payload["text"] = msg_text
                _ures = requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    json=user_payload, timeout=15
                )
            try:
                user_msg_id = _ures.json().get("result", {}).get("message_id")
            except Exception:
                pass
        except Exception as e:
            print(f"[!] خطأ إرسال OTP للمستخدم {user_id}: {e}")
            user_msg_id = None

    group_msg = t("new_otp_group", None,
                   country_flag=country_flag,
                   platform_emoji=platform_emoji,
                   country_short=country_short,
                   number_masked=number_masked)
    try:
        bot_info = bot.get_me()
        bot_url = f"https://t.me/{bot_info.username}"
    except Exception:
        bot_url = "https://t.me/FK_AY"
    custom_btns_all = get_custom_buttons()
    channel_url = custom_btns_all[0][2] if custom_btns_all else bot_url
    for chat_id in CHAT_IDS:
        try:
            extra_rows = []
            extra_rows.append([{"text": "📋 𝗙𝗨𝗟𝗟 𝗠𝗘𝗦𝗦𝗔𝗚𝗘", "copy_text": {"text": str(sms)}, "icon_custom_emoji_id": "5454386656628991407"}])
            group_btns = get_otp_group_buttons()
            for gbtn in group_btns:
                extra_rows.append([{"text": gbtn["text"], "url": gbtn["url"]}])
            group_voice_buf = generate_otp_voice(otp_code, bot_name="NUMBER X")
            group_voice_bytes = group_voice_buf.read() if group_voice_buf else None
            result = _send_copy_msg(
                chat_id=chat_id,
                text=group_msg,
                otp_code=otp_code,
                extra_markup_rows=extra_rows,
                parse_mode="HTML",
                photo_bytes=BOT_IMAGE_BYTES if not group_voice_bytes else None,
                number=number,
                voice_bytes=group_voice_bytes
            )
            if result and result.get("message_id"):
                track_otp_tg_message(chat_id, result["message_id"])
        except Exception as e:
            print(f"[group_send] ⚠️ {e}")

def track_otp_tg_message(chat_id, message_id):
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    c = conn.cursor()
    c.execute("INSERT INTO otp_tg_messages (chat_id, message_id, sent_at) VALUES (?, ?, ?)",
              (str(chat_id), message_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

@bot.callback_query_handler(func=lambda call: call.data == "admin_panel_accounts")
def admin_panel_accounts(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup(row_width=2)
    btns = []
    for sk, site in PANEL_SITES.items():
        accounts = get_panel_accounts(sk)
        btns.append(types.InlineKeyboardButton(
            f"{site['name']} ({len(accounts)})",
            callback_data=f"panel_site_{sk}"
        ))
    for i in range(0, len(btns), 2):
        markup.row(*btns[i:i+2])
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call,
        "👥 <b>إدارة حسابات اللوحات</b>\n\nاختر اللوحة:",
        markup=markup, parse_mode="HTML"
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("panel_site_"))
def panel_site_callback(call):
    if not is_admin(call.from_user.id): return
    site_key = call.data.replace("panel_site_", "")
    if site_key not in PANEL_SITES:
        bot.answer_callback_query(call.id, "❌ لوحة غير موجودة", show_alert=True)
        return
    site = PANEL_SITES[site_key]
    accounts = get_panel_accounts(site_key)
    text = f"👥 <b>{site['name']}</b>\n\n"
    if accounts:
        for i, acc in enumerate(accounts, 1):
            running = _panel_threads.get(f"{site_key}_{acc['id']}", None)
            status = "🟢" if running and running.is_alive() else "🔴"
            src_label = " 📌" if acc.get("source") == "default" else " 👤"
            text += f"{i}. {status}{src_label} <code>{acc['username']}</code>\n"
    else:
        text += "⚠️ لا توجد حسابات\nأضف من الأدمن أو عدّل default_accounts في الملف\n"
    text += "\n📌 = من الملف | 👤 = مضاف من الأدمن"
    if PANEL_SITES.get(site_key, {}).get("type") == "api":
        text += "\n⚡ لوحة API - التوكن من الملف مباشرة"
    markup = types.InlineKeyboardMarkup()
    for acc in accounts:
        if acc.get("source") != "default":
            markup.add(types.InlineKeyboardButton(
                f"🗑️ حذف {acc['username']}",
                callback_data=f"del_panel_acc_{site_key}_{acc['id']}"
            ))
    markup.add(types.InlineKeyboardButton("➕ إضافة حساب", callback_data=f"add_panel_acc_{site_key}"))
    markup.add(types.InlineKeyboardButton("رجوع", callback_data="admin_panel_accounts", icon_custom_emoji_id="5386340832628462681"))
    safe_edit_or_delete(call, text, markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("add_panel_acc_"))
def add_panel_acc_step1(call):
    if not is_admin(call.from_user.id): return
    site_key = call.data.replace("add_panel_acc_", "")
    site = PANEL_SITES[site_key]
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("❌ إلغاء", callback_data=f"panel_site_{site_key}"))
    if site.get("type") in ("api_token", "api"):
        user_states[call.from_user.id] = {"action": "panel_acc_api_token", "site_key": site_key}
        safe_edit_or_delete(call,
            f"➕ <b>إضافة حساب - {site['name']}</b>\n\n🔑 أرسل API Token:",
            markup=markup, parse_mode="HTML"
        )
    else:
        user_states[call.from_user.id] = {"action": "panel_acc_username", "site_key": site_key}
        safe_edit_or_delete(call,
            f"➕ <b>إضافة حساب - {site['name']}</b>\n\n📝 أرسل اسم المستخدم:",
            markup=markup, parse_mode="HTML"
        )

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_panel_acc_"))
def del_panel_acc(call):
    if not is_admin(call.from_user.id): return
    parts = call.data.replace("del_panel_acc_", "").rsplit("_", 1)
    if len(parts) < 2: return
    site_key, account_id = parts[0], parts[1]
    if delete_panel_account(site_key, account_id):
        bot.answer_callback_query(call.id, "✅ تم حذف الحساب وإيقاف المراقبة", show_alert=True)
    else:
        bot.answer_callback_query(call.id, "❌ فشل الحذف", show_alert=True)
    panel_site_callback(call)

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("action") == "panel_acc_username")
def panel_acc_username(message):
    user_id = message.from_user.id
    user_states[user_id]["username"] = message.text.strip()
    user_states[user_id]["action"] = "panel_acc_password"
    bot.reply_to(message, "🔑 أرسل كلمة المرور:")

@bot.message_handler(func=lambda msg: isinstance(user_states.get(msg.from_user.id), dict) and
                     user_states[msg.from_user.id].get("action") == "panel_acc_password")
def panel_acc_password(message):
    user_id = message.from_user.id
    state = user_states.pop(user_id)
    site_key = state["site_key"]
    username = state["username"]
    password = message.text.strip()
    account = add_panel_account(site_key, username, password)
    start_panel_account_monitor(site_key, account)
    bot.reply_to(message,
        f"✅ <b>تم إضافة الحساب وبدء المراقبة!</b>\n\n"
        f"🏦 اللوحة: {PANEL_SITES[site_key]['name']}\n"
        f"👤 اليوزر: <code>{username}</code>",
        parse_mode="HTML"
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_fallback_"))
def copy_fallback_handler(call):
    value = call.data[len("copy_fallback_"):]
    bot.answer_callback_query(call.id, f"📋 {value}", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_num_"))
def copy_num_callback(call):
    number = call.data[9:]
    bot.answer_callback_query(call.id, f"📋 {number}", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data.startswith("copy_"))
def copy_callback(call):
    otp = call.data[5:]
    bot.answer_callback_query(call.id, f"📋 {otp}", show_alert=True)

COUNTRY_CODES = {
    "1": ("USA/Canada", "<tg-emoji emoji-id='5976694588658686266'>🇺🇸</tg-emoji>", "USA/CANADA"),
    "7": ("Russia", "<tg-emoji emoji-id='5976725997754521724'>🇷🇺</tg-emoji>", "RUSSIA"),
    "20": ("Egypt", "<tg-emoji emoji-id='5222161185138292290'>🇪🇬</tg-emoji>", "EGYPT"),
    "27": ("South Africa", "<tg-emoji emoji-id='5976697079739718234'>🇿🇦</tg-emoji>", "SOUTH AFRICA"),
    "30": ("Greece", "<tg-emoji emoji-id='5976335971774372579'>🇬🇷</tg-emoji>", "GREECE"),
    "31": ("Netherlands", "<tg-emoji emoji-id='5976438003017456076'>🇳🇱</tg-emoji>", "NETHERLANDS"),
    "32": ("Belgium", "<tg-emoji emoji-id='5976300439509932178'>🇧🇪</tg-emoji>", "BELGIUM"),
    "33": ("France", "<tg-emoji emoji-id='5976706494308030299'>🇫🇷</tg-emoji>", "FRANCE"),
    "34": ("Spain", "<tg-emoji emoji-id='5976424031488843687'>🇪🇸</tg-emoji>", "SPAIN"),
    "36": ("Hungary", "<tg-emoji emoji-id='5976789975587363092'>🇭🇺</tg-emoji>", "HUNGARY"),
    "39": ("Italy", "<tg-emoji emoji-id='5976298085867854649'>🇮🇹</tg-emoji>", "ITALY"),
    "40": ("Romania", "<tg-emoji emoji-id='5976646540859546652'>🇷🇴</tg-emoji>", "ROMANIA"),
    "41": ("Switzerland", "<tg-emoji emoji-id='5976561599291333244'>🇨🇭</tg-emoji>", "SWITZERLAND"),
    "43": ("Austria", "<tg-emoji emoji-id='5976586982548051976'>🇦🇹</tg-emoji>", "AUSTRIA"),
    "44": ("UK", "<tg-emoji emoji-id='5976531856642807659'>🇬🇧</tg-emoji>", "UK"),
    "45": ("Denmark", "<tg-emoji emoji-id='5976380446160723453'>🇩🇰</tg-emoji>", "DENMARK"),
    "46": ("Sweden", "<tg-emoji emoji-id='5976775179425028923'>🇸🇪</tg-emoji>", "SWEDEN"),
    "47": ("Norway", "<tg-emoji emoji-id='5976327557933439693'>🇳🇴</tg-emoji>", "NORWAY"),
    "48": ("Poland", "<tg-emoji emoji-id='5976482692152170488'>🇵🇱</tg-emoji>", "POLAND"),
    "49": ("Germany", "<tg-emoji emoji-id='5976493356555968244'>🇩🇪</tg-emoji>", "GERMANY"),
    "51": ("Peru", "<tg-emoji emoji-id='5976420350701869282'>🇵🇪</tg-emoji>", "PERU"),
    "52": ("Mexico", "<tg-emoji emoji-id='5976658300480002579'>🇲🇽</tg-emoji>", "MEXICO"),
    "53": ("Cuba", "<tg-emoji emoji-id='5357035553508308603'>🇨🇺</tg-emoji>", "CUBA"),
    "54": ("Argentina", "<tg-emoji emoji-id='5976803839741799351'>🇦🇷</tg-emoji>", "ARGENTINA"),
    "55": ("Brazil", "<tg-emoji emoji-id='5976287034917001256'>🇧🇷</tg-emoji>", "BRAZIL"),
    "56": ("Chile", "<tg-emoji emoji-id='5978610156957603801'>🇨🇱</tg-emoji>", "CHILE"),
    "57": ("Colombia", "<tg-emoji emoji-id='5976555951409339416'>🇨🇴</tg-emoji>", "COLOMBIA"),
    "58": ("Venezuela", "<tg-emoji emoji-id='5228751795274136090'>🇻🇪</tg-emoji>", "VENEZUELA"),
    "60": ("Malaysia", "<tg-emoji emoji-id='5976838031976437927'>🇲🇾</tg-emoji>", "MALAYSIA"),
    "61": ("Australia", "<tg-emoji emoji-id='5976552377996548545'>🇦🇺</tg-emoji>", "AUSTRALIA"),
    "62": ("Indonesia", "<tg-emoji emoji-id='5224405893960969756'>🇮🇩</tg-emoji>", "INDONESIA"),
    "63": ("Philippines", "<tg-emoji emoji-id='5976772181537858123'>🇵🇭</tg-emoji>", "PHILIPPINES"),
    "64": ("New Zealand", "<tg-emoji emoji-id='5976512722563503846'>🇳🇿</tg-emoji>", "NEW ZEALAND"),
    "65": ("Singapore", "<tg-emoji emoji-id='5976545437329399582'>🇸🇬</tg-emoji>", "SINGAPORE"),
    "66": ("Thailand", "<tg-emoji emoji-id='5976342573139106020'>🇹🇭</tg-emoji>", "THAILAND"),
    "81": ("Japan", "<tg-emoji emoji-id='5976688764683033429'>🇯🇵</tg-emoji>", "JAPAN"),
    "82": ("South Korea", "<tg-emoji emoji-id='5976617773168597444'>🇰🇷</tg-emoji>", "SOUTH KOREA"),
    "84": ("Vietnam", "<tg-emoji emoji-id='5976537109387810524'>🇻🇳</tg-emoji>", "VIETNAM"),
    "86": ("China", "<tg-emoji emoji-id='5976702693261975275'>🇨🇳</tg-emoji>", "CHINA"),
    "90": ("Turkey", "<tg-emoji emoji-id='5976491638569048813'>🇹🇷</tg-emoji>", "TURKEY"),
    "91": ("India", "<tg-emoji emoji-id='5976491823252642237'>🇮🇳</tg-emoji>", "INDIA"),
    "92": ("Pakistan", "<tg-emoji emoji-id='5976723210320748190'>🇵🇰</tg-emoji>", "PAKISTAN"),
    "93": ("Afghanistan", "<tg-emoji emoji-id='5976277263866403415'>🇦🇫</tg-emoji>", "AFGHANISTAN"),
    "94": ("Sri Lanka", "<tg-emoji emoji-id='5976302702957697673'>🇱🇰</tg-emoji>", "SRI LANKA"),
    "95": ("Myanmar", "<tg-emoji emoji-id='5188162778073935826'>🇲🇲</tg-emoji>", "MYANMAR"),
    "98": ("Iran", "<tg-emoji emoji-id='5976430585608935514'>🇮🇷</tg-emoji>", "IRAN"),
    "212": ("Morocco", "<tg-emoji emoji-id='5224530035695693965'>🇲🇦</tg-emoji>", "MOROCCO"),
    "213": ("Algeria", "<tg-emoji emoji-id='5976325273010837563'>🇩🇿</tg-emoji>", "ALGERIA"),
    "216": ("Tunisia", "<tg-emoji emoji-id='5976645965333929511'>🇹🇳</tg-emoji>", "TUNISIA"),
    "218": ("Libya", "<tg-emoji emoji-id='5893101223564810175'>🇱🇾</tg-emoji>", "LIBYA"),
    "220": ("Gambia", "<tg-emoji emoji-id='5976483297742559352'>🇬🇲</tg-emoji>", "GAMBIA"),
    "221": ("Senegal", "<tg-emoji emoji-id='5976483722944320690'>🇸🇳</tg-emoji>", "SENEGAL"),
    "222": ("Mauritania", "<tg-emoji emoji-id='5422465115360345921'>🇲🇷</tg-emoji>", "MAURITANIA"),
    "223": ("Mali", "<tg-emoji emoji-id='5976768376196831695'>🇲🇱</tg-emoji>", "MALI"),
    "224": ("Guinea", "<tg-emoji emoji-id='5976350888195791241'>🇬🇳</tg-emoji>", "GUINEA"),
    "225": ("Ivory Coast", "<tg-emoji emoji-id='5411283953984218884'>🇨🇮</tg-emoji>", "IVORY COAST"),
    "226": ("Burkina Faso", "<tg-emoji emoji-id='5976557308619003946'>🇧🇫</tg-emoji>", "BURKINA FASO"),
    "227": ("Niger", "<tg-emoji emoji-id='5976647932428950438'>🇳🇪</tg-emoji>", "NIGER"),
    "228": ("Togo", "<tg-emoji emoji-id='5976576434108372678'>🇹🇬</tg-emoji>", "TOGO"),
    "229": ("Benin", "<tg-emoji emoji-id='5976420385061608425'>🇧🇯</tg-emoji>", "BENIN"),
    "230": ("Mauritius", "<tg-emoji emoji-id='5976482670677333747'>🇲🇺</tg-emoji>", "MAURITIUS"),
    "231": ("Liberia", "<tg-emoji emoji-id='5976577718303595873'>🇱🇷</tg-emoji>", "LIBERIA"),
    "232": ("Sierra Leone", "<tg-emoji emoji-id='5976596925397342449'>🇸🇱</tg-emoji>", "SIERRA LEONE"),
    "233": ("Ghana", "<tg-emoji emoji-id='5976787188153588017'>🇬🇭</tg-emoji>", "GHANA"),
    "234": ("Nigeria", "<tg-emoji emoji-id='5976523777809323703'>🇳🇬</tg-emoji>", "NIGERIA"),
    "235": ("Chad", "<tg-emoji emoji-id='5979044524180117852'>🇹🇩</tg-emoji>", "CHAD"),
    "236": ("C. African Rep", "<tg-emoji emoji-id='5976451437675156826'>🇨🇫</tg-emoji>", "CENTRAL AFRICAN REPUBLIC"),
    "237": ("Cameroon", "<tg-emoji emoji-id='5976324706075154689'>🇨🇲</tg-emoji>", "CAMEROON"),
    "238": ("Cape Verde", "<tg-emoji emoji-id='5976548697209575812'>🇨🇻</tg-emoji>", "CAPE VERDE"),
    "239": ("Sao Tome", "<tg-emoji emoji-id='5976699343187482779'>🇸🇹</tg-emoji>", "SAO TOME"),
    "240": ("Eq. Guinea", "<tg-emoji emoji-id='5976814525620426462'>🇬🇶</tg-emoji>", "EQUATORIAL GUINEA"),
    "241": ("Gabon", "<tg-emoji emoji-id='5976396341834684925'>🇬🇦</tg-emoji>", "GABON"),
    "242": ("Congo", "<tg-emoji emoji-id='5976332205088054604'>🇨🇬</tg-emoji>", "CONGO"),
    "243": ("DR Congo", "<tg-emoji emoji-id='5976337234494757335'>🇨🇩</tg-emoji>", "DR CONGO"),
    "244": ("Angola", "<tg-emoji emoji-id='5976833878743063435'>🇦🇴</tg-emoji>", "ANGOLA"),
    "245": ("Guinea-Bissau", "<tg-emoji emoji-id='5976526294660159661'>🇬🇼</tg-emoji>", "GUINEA-BISSAU"),
    "248": ("Seychelles", "<tg-emoji emoji-id='5978929268732729465'>🇸🇨</tg-emoji>", "SEYCHELLES"),
    "249": ("Sudan", "<tg-emoji emoji-id='5224372990216514135'>🇸🇩</tg-emoji>", "SUDAN"),
    "250": ("Rwanda", "<tg-emoji emoji-id='5976558287871547862'>🇷🇼</tg-emoji>", "RWANDA"),
    "251": ("Ethiopia", "<tg-emoji emoji-id='5976492471792703601'>🇪🇹</tg-emoji>", "ETHIOPIA"),
    "252": ("Somalia", "<tg-emoji emoji-id='5976732113787966649'>🇸🇴</tg-emoji>", "SOMALIA"),
    "253": ("Djibouti", "<tg-emoji emoji-id='5976613946352736850'>🇩🇯</tg-emoji>", "DJIBOUTI"),
    "254": ("Kenya", "<tg-emoji emoji-id='5976393060479669497'>🇰🇪</tg-emoji>", "KENYA"),
    "255": ("Tanzania", "<tg-emoji emoji-id='5976297192514656545'>🇹🇿</tg-emoji>", "TANZANIA"),
    "256": ("Uganda", "<tg-emoji emoji-id='5976539578994006362'>🇺🇬</tg-emoji>", "UGANDA"),
    "257": ("Burundi", "<tg-emoji emoji-id='5976742099586914503'>🇧🇮</tg-emoji>", "BURUNDI"),
    "258": ("Mozambique", "<tg-emoji emoji-id='5976389130584594356'>🇲🇿</tg-emoji>", "MOZAMBIQUE"),
    "260": ("Zambia", "<tg-emoji emoji-id='5976750457593272380'>🇿🇲</tg-emoji>", "ZAMBIA"),
    "261": ("Madagascar", "<tg-emoji emoji-id='5976827191478983649'>🇲🇬</tg-emoji>", "MADAGASCAR"),
    "263": ("Zimbabwe", "<tg-emoji emoji-id='5976829738394589975'>🇿🇼</tg-emoji>", "ZIMBABWE"),
    "264": ("Namibia", "<tg-emoji emoji-id='5976603874654426417'>🇳🇦</tg-emoji>", "NAMIBIA"),
    "265": ("Malawi", "<tg-emoji emoji-id='5341341330691863561'>🇲🇼</tg-emoji>", "MALAWI"),
    "266": ("Lesotho", "<tg-emoji emoji-id='5976620972919232666'>🇱🇸</tg-emoji>", "LESOTHO"),
    "267": ("Botswana", "<tg-emoji emoji-id='5976363541169445780'>🇧🇼</tg-emoji>", "BOTSWANA"),
    "268": ("Eswatini", "<tg-emoji emoji-id='5976741725924759442'>🇸🇿</tg-emoji>", "ESWATINI"),
    "269": ("Comoros", "<tg-emoji emoji-id='5976698870741083962'>🇰🇲</tg-emoji>", "COMOROS"),
    "350": ("Gibraltar", "<tg-emoji emoji-id='5226496954623603888'>🇬🇮</tg-emoji>", "GIBRALTAR"),
    "351": ("Portugal", "<tg-emoji emoji-id='5976327106961873123'>🇵🇹</tg-emoji>", "PORTUGAL"),
    "352": ("Luxembourg", "<tg-emoji emoji-id='5976285484433807436'>🇱🇺</tg-emoji>", "LUXEMBOURG"),
    "353": ("Ireland", "<tg-emoji emoji-id='5978894629821487879'>🇮🇪</tg-emoji>", "IRELAND"),
    "354": ("Iceland", "<tg-emoji emoji-id='5976698802021604508'>🇮🇸</tg-emoji>", "ICELAND"),
    "355": ("Albania", "<tg-emoji emoji-id='5976498841229203219'>🇦🇱</tg-emoji>", "ALBANIA"),
    "356": ("Malta", "<tg-emoji emoji-id='5976479762984475758'>🇲🇹</tg-emoji>", "MALTA"),
    "357": ("Cyprus", "<tg-emoji emoji-id='5976803616403495510'>🇨🇾</tg-emoji>", "CYPRUS"),
    "358": ("Finland", "<tg-emoji emoji-id='5976510158468028132'>🇫🇮</tg-emoji>", "FINLAND"),
    "359": ("Bulgaria", "<tg-emoji emoji-id='5976616970009712457'>🇧🇬</tg-emoji>", "BULGARIA"),
    "370": ("Lithuania", "<tg-emoji emoji-id='5976837881652582376'>🇱🇹</tg-emoji>", "LITHUANIA"),
    "371": ("Latvia", "<tg-emoji emoji-id='5976740978600451694'>🇱🇻</tg-emoji>", "LATVIA"),
    "372": ("Estonia", "<tg-emoji emoji-id='5976277392715423938'>🇪🇪</tg-emoji>", "ESTONIA"),
    "373": ("Moldova", "<tg-emoji emoji-id='5976792247625064355'>🇲🇩</tg-emoji>", "MOLDOVA"),
    "374": ("Armenia", "<tg-emoji emoji-id='5411455658186778270'>🇦🇲</tg-emoji>", "ARMENIA"),
    "375": ("Belarus", "<tg-emoji emoji-id='5976363304946245889'>🇧🇾</tg-emoji>", "BELARUS"),
    "376": ("Andorra", "<tg-emoji emoji-id='5978725575613749734'>🇦🇩</tg-emoji>", "ANDORRA"),
    "377": ("Monaco", "<tg-emoji emoji-id='5976425521842494767'>🇲🇨</tg-emoji>", "MONACO"),
    "378": ("San Marino", "<tg-emoji emoji-id='5976790357839452073'>🇸🇲</tg-emoji>", "SAN MARINO"),
    "380": ("Ukraine", "<tg-emoji emoji-id='5976654508023880370'>🇺🇦</tg-emoji>", "UKRAINE"),
    "381": ("Serbia", "<tg-emoji emoji-id='5976463012612020480'>🇷🇸</tg-emoji>", "SERBIA"),
    "382": ("Montenegro", "<tg-emoji emoji-id='5976333948844776590'>🇲🇪</tg-emoji>", "MONTENEGRO"),
    "385": ("Croatia", "<tg-emoji emoji-id='5976744921380428432'>🇭🇷</tg-emoji>", "CROATIA"),
    "386": ("Slovenia", "<tg-emoji emoji-id='5978926704637253502'>🇸🇮</tg-emoji>", "SLOVENIA"),
    "387": ("Bosnia", "<tg-emoji emoji-id='5976670657100913091'>🇧🇦</tg-emoji>", "BOSNIA"),
    "389": ("N. Macedonia", "<tg-emoji emoji-id='5976441816948417573'>🇲🇰</tg-emoji>", "NORTH MACEDONIA"),
    "420": ("Czech Rep", "<tg-emoji emoji-id='5976659369926859099'>🇨🇿</tg-emoji>", "CZECH REPUBLIC"),
    "421": ("Slovakia", "<tg-emoji emoji-id='5976365662883290025'>🇸🇰</tg-emoji>", "SLOVAKIA"),
    "501": ("Belize", "<tg-emoji emoji-id='5976828144961722583'>🇧🇿</tg-emoji>", "BELIZE"),
    "502": ("Guatemala", "<tg-emoji emoji-id='5976766731224358097'>🇬🇹</tg-emoji>", "GUATEMALA"),
    "503": ("El Salvador", "<tg-emoji emoji-id='5427301849831061043'>🇸🇻</tg-emoji>", "EL SALVADOR"),
    "504": ("Honduras", "<tg-emoji emoji-id='5976504755399170515'>🇭🇳</tg-emoji>", "HONDURAS"),
    "505": ("Nicaragua", "<tg-emoji emoji-id='5426842228200847679'>🇳🇮</tg-emoji>", "NICARAGUA"),
    "506": ("Costa Rica", "<tg-emoji emoji-id='5976659120818755766'>🇨🇷</tg-emoji>", "COSTA RICA"),
    "507": ("Panama", "<tg-emoji emoji-id='5976690366705834196'>🇵🇦</tg-emoji>", "PANAMA"),
    "509": ("Haiti", "<tg-emoji emoji-id='5976439987292346381'>🇭🇹</tg-emoji>", "HAITI"),
    "591": ("Bolivia", "<tg-emoji emoji-id='5976750775420852685'>🇧🇴</tg-emoji>", "BOLIVIA"),
    "592": ("Guyana", "<tg-emoji emoji-id='5978986473402144429'>🇬🇾</tg-emoji>", "GUYANA"),
    "593": ("Ecuador", "<tg-emoji emoji-id='5976442048876648469'>🇪🇨</tg-emoji>", "ECUADOR"),
    "595": ("Paraguay", "<tg-emoji emoji-id='5976609745874721028'>🇵🇾</tg-emoji>", "PARAGUAY"),
    "597": ("Suriname", "<tg-emoji emoji-id='5976300113092417676'>🇸🇷</tg-emoji>", "SURINAME"),
    "598": ("Uruguay", "<tg-emoji emoji-id='5976387133424803250'>🇺🇾</tg-emoji>", "URUGUAY"),
    "670": ("Timor-Leste", "<tg-emoji emoji-id='5422602597263489621'>🇹🇱</tg-emoji>", "TIMOR-LESTE"),
    "673": ("Brunei", "<tg-emoji emoji-id='5976686076033506746'>🇧🇳</tg-emoji>", "BRUNEI"),
    "675": ("Papua N. Guinea", "<tg-emoji emoji-id='5976504321607475018'>🇵🇬</tg-emoji>", "PAPUA NEW GUINEA"),
    "680": ("Palau", "<tg-emoji emoji-id='5976497857681693092'>🇵🇼</tg-emoji>", "PALAU"),
    "685": ("Samoa", "<tg-emoji emoji-id='5976637886500444833'>🇼🇸</tg-emoji>", "SAMOA"),
    "686": ("Kiribati", "<tg-emoji emoji-id='5976401719133739607'>🇰🇮</tg-emoji>", "KIRIBATI"),
    "691": ("Micronesia", "<tg-emoji emoji-id='5976430375155538302'>🇫🇲</tg-emoji>", "MICRONESIA"),
    "850": ("North Korea", "<tg-emoji emoji-id='5341271404329317987'>🇰🇵</tg-emoji>", "NORTH KOREA"),
    "852": ("Hong Kong", "<tg-emoji emoji-id='5222395857856374392'>🇭🇰</tg-emoji>", "HONG KONG"),
    "855": ("Cambodia", "<tg-emoji emoji-id='5976742700882335535'>🇰🇭</tg-emoji>", "CAMBODIA"),
    "856": ("Laos", "<tg-emoji emoji-id='5976399640369568284'>🇱🇦</tg-emoji>", "LAOS"),
    "880": ("Bangladesh", "<tg-emoji emoji-id='5976473818749737592'>🇧🇩</tg-emoji>", "BANGLADESH"),
    "886": ("Taiwan", "<tg-emoji emoji-id='5222365101595568847'>🇹🇼</tg-emoji>", "TAIWAN"),
    "960": ("Maldives", "<tg-emoji emoji-id='5976363386550622337'>🇲🇻</tg-emoji>", "MALDIVES"),
    "961": ("Lebanon", "<tg-emoji emoji-id='5976529279662430823'>🇱🇧</tg-emoji>", "LEBANON"),
    "962": ("Jordan", "<tg-emoji emoji-id='5976421677846764717'>🇯🇴</tg-emoji>", "JORDAN"),
    "963": ("Syria", "<tg-emoji emoji-id='5308002793812955097'>🇸🇾</tg-emoji>", "SYRIA"),
    "964": ("Iraq", "<tg-emoji emoji-id='5976458232313420307'>🇮🇶</tg-emoji>", "IRAQ"),
    "965": ("Kuwait", "<tg-emoji emoji-id='5976679732366809576'>🇰🇼</tg-emoji>", "KUWAIT"),
    "966": ("Saudi Arabia", "<tg-emoji emoji-id='5976726495970729818'>🇸🇦</tg-emoji>", "SAUDI ARABIA"),
    "967": ("Yemen", "<tg-emoji emoji-id='5976685311529327157'>🇾🇪</tg-emoji>", "YEMEN"),
    "968": ("Oman", "<tg-emoji emoji-id='5976284621145381432'>🇴🇲</tg-emoji>", "OMAN"),
    "970": ("Palestine", "<tg-emoji emoji-id='5976410742860027765'>🇵🇸</tg-emoji>", "PALESTINE"),
    "971": ("UAE", "<tg-emoji emoji-id='5976594713489185156'>🇦🇪</tg-emoji>", "UAE"),
    "972": ("Israel", "<tg-emoji emoji-id='5224720599099648709'>🇮🇱</tg-emoji>", "ISRAEL"),
    "973": ("Bahrain", "<tg-emoji emoji-id='5976668522502166844'>🇧🇭</tg-emoji>", "BAHRAIN"),
    "974": ("Qatar", "<tg-emoji emoji-id='5222225596762830469'>🇶🇦</tg-emoji>", "QATAR"),
    "975": ("Bhutan", "<tg-emoji emoji-id='5976318160544994744'>🇧🇹</tg-emoji>", "BHUTAN"),
    "976": ("Mongolia", "<tg-emoji emoji-id='5224192257992701543'>🇲🇳</tg-emoji>", "MONGOLIA"),
    "977": ("Nepal", "<tg-emoji emoji-id='5976563609336026965'>🇳🇵</tg-emoji>", "NEPAL"),
    "992": ("Tajikistan", "<tg-emoji emoji-id='5976597573937404746'>🇹🇯</tg-emoji>", "TAJIKISTAN"),
    "993": ("Turkmenistan", "<tg-emoji emoji-id='5978875276698851977'>🇹🇲</tg-emoji>", "TURKMENISTAN"),
    "994": ("Azerbaijan", "<tg-emoji emoji-id='5976582940983827573'>🇦🇿</tg-emoji>", "AZERBAIJAN"),
    "995": ("Georgia", "<tg-emoji emoji-id='5976431775314876794'>🇬🇪</tg-emoji>", "GEORGIA"),
    "996": ("Kyrgyzstan", "<tg-emoji emoji-id='5976533712068679686'>🇰🇬</tg-emoji>", "KYRGYZSTAN"),
    "998": ("Uzbekistan", "<tg-emoji emoji-id='5976637328154696110'>🇺🇿</tg-emoji>", "UZBEKISTAN"),
}

def get_flag_html(flag_str):
    return flag_str

def get_flag_plain(flag_str):
    import re as _re
    if not flag_str:
        return "🌍"
    match = _re.search(r'<tg-emoji[^>]*>(.*?)</tg-emoji>', flag_str)
    if match:
        return match.group(1).strip()
    return flag_str

def periodic_group_message():
    while True:
        for chat_id in CHAT_IDS:
            try:
                msg = t("group_periodic", None)
                sent = bot.send_message(chat_id, msg)
                track_otp_tg_message(chat_id, sent.message_id)
            except:
                pass
        time.sleep(300)

def auto_delete_otp_logs():
    while True:
        try:
            conn = sqlite3.connect(DB_PATH, check_same_thread=False)
            c = conn.cursor()
            c.execute("SELECT id, chat_id, message_id, sent_at FROM otp_tg_messages")
            messages = c.fetchall()
            now = datetime.now()
            for row_id, chat_id, message_id, sent_at_str in messages:
                sent_at = datetime.strptime(sent_at_str, "%Y-%m-%d %H:%M:%S")
                delete_after = get_auto_delete_time(chat_id)
                delta = (now - sent_at).total_seconds()
                if delta > delete_after:
                    try:
                        bot.delete_message(chat_id, message_id)
                    except:
                        pass
                    c.execute("DELETE FROM otp_tg_messages WHERE id=?", (row_id,))
            otp_del = get_otp_delete_global()
            c.execute("""
                DELETE FROM otp_logs
                WHERE (julianday('now') - julianday(timestamp)) * 86400 > ?
            """, (otp_del,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[auto_delete] ⚠️ {e}")
        time.sleep(30)

def run_bot():
    while True:
        try:
            print("[sendako] 🤖 \033[92mتشغيل البوت...\033[0m")
            # تعيين أوامر البوت
            try:
                bot.set_my_commands([
                    types.BotCommand("/start", "ابدأ البوت / Start The Bot"),
                    types.BotCommand("/language", "تغيير اللغة / Change Language"),
                ])
            except Exception as _e:
                print(f"[commands] ⚠️ {_e}")
            bot.infinity_polling(timeout=30, long_polling_timeout=15)
        except Exception as e:
            print(f"[sendako] ⚠️ توقف البوت - إعادة التشغيل بعد 5 ثوانٍ: {e}")
            time.sleep(5)

def safe_main_loop():
    while True:
        try:
            main_loop()
        except Exception as e:
            print(f"[tenjiko] ⚠️ خطأ في main_loop - إعادة التشغيل بعد 10 ثوانٍ: {e}")
            time.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    threading.Thread(target=ivas_monitor_loop, daemon=True).start()
    threading.Thread(target=start_all_panel_monitors, daemon=True).start()
    threading.Thread(target=auto_delete_otp_logs, daemon=True).start()
    threading.Thread(target=periodic_group_message, daemon=True).start()
    safe_main_loop()
