#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
• DVED-X | SMS Bot V6
Panels: TimeSMS x2, IMS SMS x2
Services: Telegram, WhatsApp (with counts)
"""

import re, sys, time, hashlib, sqlite3, requests, threading, traceback
from datetime import datetime
from bs4 import BeautifulSoup

# ═══════════════════════════════════════════════════
#                   CONFIGURATION
# ═══════════════════════════════════════════════════

BOT_TOKEN      = "8516176029:AAFzOmU6HpjlQ8--imSgsWImdoklFJpd9aY"
OWNER_ID = 8065884629
OTP_GROUP_ID   = -1002915550218
BOT_NAME       = "Fadi sms"
CHANNEL_LINK   = "https://t.me/fv_mv"
BOT_LINK       = "https://t.me/fadifvambot"
DEVELOPER      = "https://t.me/fvamv"
GROUP_LINK     = "https://t.me/fv_sd"

REQUIRED_CHANNELS = [
    {"link": "https://t.me/fvamv", "name": "Fadi Channel"}, 
    {"link": "https://t.me/fv_sd", "name": "Fadi Group"},
]

TIMESMS_ACCOUNTS = [ 
    {"username": "a68038587@gmail.com", "password": "moamei2008", "label": "T#1"},
    {"username": "a68038587@gmail.com", "password": "moamei2008", "label": "T#2"},
]

IMSSMS_ACCOUNTS = [
    {"username": "a68038587@gmail.com", "password": "moamei2008", "label": "S#1"},
    {"username": "a68038587@gmail.com", "password": "moamei2008", "label": " S#2"},
]

TIMESMS_BASE = "https://timesms.org"
IMSSMS_BASE  = "https://imssms.org"

# ===== GREEN SMS PANEL =====
GREEN_ACCOUNTS = [
    {"username": "a68038587@gmail.com", "password": "moamei2008", "label": "G#1"},
]

GREEN_BASE = "http://139.99.9.4/ints"


POLL_INTERVAL   = 1
SESSION_REFRESH = 600
DB_FILE         = "dvedx_v6.db"

# ── Services shown to users ─────────────────────────
SERVICES = [
    {"app": "telegram", "icon": "🌐", "name": "Telegram", "path": "/telegram", "style": "success"},
    {"app": "whatsapp", "icon": "💬", "name": "WhatsApp", "path": "/whatsapp", "style": "success"}
]

# ═══════════════════════════════════════════════════
#                  COUNTRY CODES
# ═══════════════════════════════════════════════════

COUNTRY_CODES = {
    "1":("USA/Canada","🇺🇸","US"), "7":("Russia","🇷🇺","RU"),
    "20":("Egypt","🇪🇬","EG"),     "27":("South Africa","🇿🇦","ZA"),
    "30":("Greece","🇬🇷","GR"),    "31":("Netherlands","🇳🇱","NL"),
    "32":("Belgium","🇧🇪","BE"),   "33":("France","🇫🇷","FR"),
    "34":("Spain","🇪🇸","ES"),     "36":("Hungary","🇭🇺","HU"),
    "39":("Italy","🇮🇹","IT"),     "40":("Romania","🇷🇴","RO"),
    "41":("Switzerland","🇨🇭","CH"),"43":("Austria","🇦🇹","AT"),
    "44":("United Kingdom","🇬🇧","GB"),"45":("Denmark","🇩🇰","DK"),
    "46":("Sweden","🇸🇪","SE"),    "47":("Norway","🇳🇴","NO"),
    "48":("Poland","🇵🇱","PL"),    "49":("Germany","🇩🇪","DE"),
    "51":("Peru","🇵🇪","PE"),      "52":("Mexico","🇲🇽","MX"),
    "53":("Cuba","🇨🇺","CU"),      "54":("Argentina","🇦🇷","AR"),
    "55":("Brazil","🇧🇷","BR"),    "56":("Chile","🇨🇱","CL"),
    "57":("Colombia","🇨🇴","CO"),  "58":("Venezuela","🇻🇪","VE"),
    "60":("Malaysia","🇲🇾","MY"),  "61":("Australia","🇦🇺","AU"),
    "62":("Indonesia","🇮🇩","ID"), "63":("Philippines","🇵🇭","PH"),
    "64":("New Zealand","🇳🇿","NZ"),"65":("Singapore","🇸🇬","SG"),
    "66":("Thailand","🇹🇭","TH"),  "81":("Japan","🇯🇵","JP"),
    "82":("South Korea","🇰🇷","KR"),"84":("Vietnam","🇻🇳","VN"),
    "86":("China","🇨🇳","CN"),     "90":("Turkey","🇹🇷","TR"),
    "91":("India","🇮🇳","IN"),     "92":("Pakistan","🇵🇰","PK"),
    "93":("Afghanistan","🇦🇫","AF"),"94":("Sri Lanka","🇱🇰","LK"),
    "95":("Myanmar","🇲🇲","MM"),   "98":("Iran","🇮🇷","IR"),
    "211":("South Sudan","🇸🇸","SS"),"212":("Morocco","🇲🇦","MA"),
    "213":("Algeria","🇩🇿","DZ"),  "216":("Tunisia","🇹🇳","TN"),
    "218":("Libya","🇱🇾","LY"),    "220":("Gambia","🇬🇲","GM"),
    "221":("Senegal","🇸🇳","SN"),  "222":("Mauritania","🇲🇷","MR"),
    "223":("Mali","🇲🇱","ML"),     "224":("Guinea","🇬🇳","GN"),
    "225":("Ivory Coast","🇨🇮","CI"),"226":("Burkina Faso","🇧🇫","BF"),
    "227":("Niger","🇳🇪","NE"),    "228":("Togo","🇹🇬","TG"),
    "229":("Benin","🇧🇯","BJ"),    "230":("Mauritius","🇲🇺","MU"),
    "231":("Liberia","🇱🇷","LR"),  "232":("Sierra Leone","🇸🇱","SL"),
    "233":("Ghana","🇬🇭","GH"),    "234":("Nigeria","🇳🇬","NG"),
    "235":("Chad","🇹🇩","TD"),     "236":("Central Africa","🇨🇫","CF"),
    "237":("Cameroon","🇨🇲","CM"), "238":("Cape Verde","🇨🇻","CV"),
    "239":("Sao Tome","🇸🇹","ST"), "240":("Eq. Guinea","🇬🇶","GQ"),
    "241":("Gabon","🇬🇦","GA"),    "242":("Congo","🇨🇬","CG"),
    "243":("DR Congo","🇨🇩","CD"), "244":("Angola","🇦🇴","AO"),
    "245":("Guinea-Bissau","🇬🇼","GW"),"246":("Diego Garcia","🇮🇴","IO"),
    "248":("Seychelles","🇸🇨","SC"),"249":("Sudan","🇸🇩","SD"),
    "250":("Rwanda","🇷🇼","RW"),   "251":("Ethiopia","🇪🇹","ET"),
    "252":("Somalia","🇸🇴","SO"),  "253":("Djibouti","🇩🇯","DJ"),
    "254":("Kenya","🇰🇪","KE"),    "255":("Tanzania","🇹🇿","TZ"),
    "256":("Uganda","🇺🇬","UG"),   "257":("Burundi","🇧🇮","BI"),
    "258":("Mozambique","🇲🇿","MZ"),"260":("Zambia","🇿🇲","ZM"),
    "261":("Madagascar","🇲🇬","MG"),"263":("Zimbabwe","🇿🇼","ZW"),
    "264":("Namibia","🇳🇦","NA"),  "265":("Malawi","🇲🇼","MW"),
    "266":("Lesotho","🇱🇸","LS"),  "267":("Botswana","🇧🇼","BW"),
    "268":("Eswatini","🇸🇿","SZ"), "269":("Comoros","🇰🇲","KM"),
    "290":("St Helena","🇸🇭","SH"),"291":("Eritrea","🇪🇷","ER"),
    "298":("Faroe Islands","🇫🇴","FO"),"299":("Greenland","🇬🇱","GL"),
    "350":("Gibraltar","🇬🇮","GI"),"351":("Portugal","🇵🇹","PT"),
    "352":("Luxembourg","🇱🇺","LU"),"353":("Ireland","🇮🇪","IE"),
    "354":("Iceland","🇮🇸","IS"),  "355":("Albania","🇦🇱","AL"),
    "356":("Malta","🇲🇹","MT"),    "357":("Cyprus","🇨🇾","CY"),
    "358":("Finland","🇫🇮","FI"),  "359":("Bulgaria","🇧🇬","BG"),
    "370":("Lithuania","🇱🇹","LT"),"371":("Latvia","🇱🇻","LV"),
    "372":("Estonia","🇪🇪","EE"),  "373":("Moldova","🇲🇩","MD"),
    "374":("Armenia","🇦🇲","AM"),  "375":("Belarus","🇧🇾","BY"),
    "376":("Andorra","🇦🇩","AD"),  "377":("Monaco","🇲🇨","MC"),
    "378":("San Marino","🇸🇲","SM"),"379":("Vatican","🇻🇦","VA"),
    "380":("Ukraine","🇺🇦","UA"),  "381":("Serbia","🇷🇸","RS"),
    "382":("Montenegro","🇲🇪","ME"),"383":("Kosovo","🇽🇰","XK"),
    "385":("Croatia","🇭🇷","HR"),  "386":("Slovenia","🇸🇮","SI"),
    "387":("Bosnia","🇧🇦","BA"),   "389":("North Macedonia","🇲🇰","MK"),
    "420":("Czechia","🇨🇿","CZ"),  "421":("Slovakia","🇸🇰","SK"),
    "423":("Liechtenstein","🇱🇮","LI"),"500":("Falkland","🇫🇰","FK"),
    "501":("Belize","🇧🇿","BZ"),   "502":("Guatemala","🇬🇹","GT"),
    "503":("El Salvador","🇸🇻","SV"),"504":("Honduras","🇭🇳","HN"),
    "505":("Nicaragua","🇳🇮","NI"),"506":("Costa Rica","🇨🇷","CR"),
    "507":("Panama","🇵🇦","PA"),   "508":("St Pierre","🇵🇲","PM"),
    "509":("Haiti","🇭🇹","HT"),    "590":("Guadeloupe","🇬🇵","GP"),
    "591":("Bolivia","🇧🇴","BO"),  "592":("Guyana","🇬🇾","GY"),
    "593":("Ecuador","🇪🇨","EC"),  "594":("French Guiana","🇬🇫","GF"),
    "595":("Paraguay","🇵🇾","PY"),  "596":("Martinique","🇲🇶","MQ"),
    "597":("Suriname","🇸🇷","SR"),  "598":("Uruguay","🇺🇾","UY"),
    "599":("Caribbean","🇨🇼","CW"), "670":("Timor-Leste","🇹🇱","TL"),
    "672":("Antarctica","🇦🇶","AQ"),"673":("Brunei","🇧🇳","BN"),
    "674":("Nauru","🇳🇷","NR"),    "675":("Papua New Guinea","🇵🇬","PG"),
    "676":("Tonga","🇹🇴","TO"),    "677":("Solomon Islands","🇸🇧","SB"),
    "678":("Vanuatu","🇻🇺","VU"),  "679":("Fiji","🇫🇯","FJ"),
    "680":("Palau","🇵🇼","PW"),    "681":("Wallis","🇼🇫","WF"),
    "682":("Cook Islands","🇨🇰","CK"),"683":("Niue","🇳🇺","NU"),
    "685":("Samoa","🇼🇸","WS"),    "686":("Kiribati","🇰🇮","KI"),
    "687":("New Caledonia","🇳🇨","NC"),"688":("Tuvalu","🇹🇻","TV"),
    "689":("French Polynesia","🇵🇫","PF"),"690":("Tokelau","🇹🇰","TK"),
    "691":("Micronesia","🇫🇲","FM"),"692":("Marshall Islands","🇲🇭","MH"),
    "850":("North Korea","🇰🇵","KP"),"852":("Hong Kong","🇭🇰","HK"),
    "853":("Macau","🇲🇴","MO"),    "855":("Cambodia","🇰🇭","KH"),
    "856":("Laos","🇱🇦","LA"),     "880":("Bangladesh","🇧🇩","BD"),
    "886":("Taiwan","🇹🇼","TW"),   "960":("Maldives","🇲🇻","MV"),
    "961":("Lebanon","🇱🇧","LB"),  "962":("Jordan","🇯🇴","JO"),
    "963":("Syria","🇸🇾","SY"),    "964":("Iraq","🇮🇶","IQ"),
    "965":("Kuwait","🇰🇼","KW"),   "966":("Saudi Arabia","🇸🇦","SA"),
    "967":("Yemen","🇾🇪","YE"),    "968":("Oman","🇴🇲","OM"),
    "970":("Palestine","🇵🇸","PS"),"971":("UAE","🇦🇪","AE"),
    "972":("Israel","🇮🇱","IL"),   "973":("Bahrain","🇧🇭","BH"),
    "974":("Qatar","🇶🇦","QA"),    "975":("Bhutan","🇧🇹","BT"),
    "976":("Mongolia","🇲🇳","MN"), "977":("Nepal","🇳🇵","NP"),
    "992":("Tajikistan","🇹🇯","TJ"),"993":("Turkmenistan","🇹🇲","TM"),
    "994":("Azerbaijan","🇦🇿","AZ"),"995":("Georgia","🇬🇪","GE"),
    "996":("Kyrgyzstan","🇰🇬","KG"),"998":("Uzbekistan","🇺🇿","UZ"),
}

SVC_ICONS = {
    "apple":"🍎","facebook":"💙","instagram":"💜","microsoft":"💎",
    "telegram":"🌐","whatsapp":"💬",
    "Apple":"🍎","Facebook":"💙","Instagram":"💜","Microsoft":"💎",
    "Telegram":"🌐","WhatsApp":"💬","SMS":"💬",
}

# ═══════════════════════════════════════════════════
#                    DATABASE
# ═══════════════════════════════════════════════════

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def init_db():
    with sqlite3.connect(DB_FILE) as c:
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id    INTEGER PRIMARY KEY,
            username   TEXT DEFAULT '',
            fname      TEXT DEFAULT '',
            banned     INTEGER DEFAULT 0,
            is_admin   INTEGER DEFAULT 0,
            subscribed INTEGER DEFAULT 0,
            created_at TEXT
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS numbers (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            number       TEXT NOT NULL,
            country_code TEXT NOT NULL,
            country_name TEXT NOT NULL,
            flag         TEXT DEFAULT '🌍',
            service_tag  TEXT DEFAULT 'all',
            in_use       INTEGER DEFAULT 0,
            used_by      INTEGER DEFAULT 0,
            used_count   INTEGER DEFAULT 0,
            added_at     TEXT,
            UNIQUE(number, service_tag)
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS pending_otps (
            user_id      INTEGER PRIMARY KEY,
            number       TEXT NOT NULL,
            country_code TEXT DEFAULT '',
            service_tag  TEXT DEFAULT 'all',
            msg_id       INTEGER DEFAULT 0,
            asked_at     TEXT
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS sub_channels (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            channel_link TEXT NOT NULL,
            channel_name TEXT NOT NULL
        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS sms_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sms_hash TEXT UNIQUE,
            date TEXT, source TEXT, number TEXT, cli TEXT,
            sms_text TEXT, otp_code TEXT, service TEXT, received_at TEXT
        )""")
        c.commit()

        def add_col(table, col, typedef):
            cols = [r[1] for r in c.execute(f"PRAGMA table_info({table})").fetchall()]
            if col not in cols:
                try:
                    c.execute(f"ALTER TABLE {table} ADD COLUMN {col} {typedef}")
                    c.commit()
                except: pass

        add_col("users",    "fname",       "TEXT DEFAULT ''")
        add_col("users",    "username",    "TEXT DEFAULT ''")
        add_col("users",    "banned",      "INTEGER DEFAULT 0")
        add_col("users",    "is_admin",    "INTEGER DEFAULT 0")
        add_col("users",    "subscribed",  "INTEGER DEFAULT 0")
        add_col("users",    "created_at",  "TEXT DEFAULT ''")
        add_col("numbers",  "used_count",  "INTEGER DEFAULT 0")
        add_col("numbers",  "service_tag", "TEXT DEFAULT 'all'")
        add_col("pending_otps", "msg_id",  "INTEGER DEFAULT 0")

        for ch in REQUIRED_CHANNELS:
            if not c.execute("SELECT 1 FROM sub_channels WHERE channel_link=?", (ch["link"],)).fetchone():
                c.execute("INSERT INTO sub_channels (channel_link,channel_name) VALUES (?,?)", (ch["link"], ch["name"]))
        c.execute("INSERT OR IGNORE INTO users (user_id,fname,is_admin,subscribed,created_at) VALUES (?,?,1,1,?)",
                  (OWNER_ID, "Owner", now()))
        c.commit()
    print("✅ DB ready")

def qone(sql, p=()):
    with sqlite3.connect(DB_FILE) as c:
        c.row_factory = sqlite3.Row
        return c.execute(sql, p).fetchone()

def qall(sql, p=()):
    with sqlite3.connect(DB_FILE) as c:
        c.row_factory = sqlite3.Row
        return c.execute(sql, p).fetchall()

def qrun(sql, p=()):
    with sqlite3.connect(DB_FILE) as c:
        c.execute(sql, p); c.commit()

def upsert_user(uid, username="", fname=""):
    with sqlite3.connect(DB_FILE) as c:
        c.execute("INSERT OR IGNORE INTO users (user_id,username,fname,created_at) VALUES (?,?,?,?)",
                  (uid, username, fname, now()))
        c.execute("UPDATE users SET username=?,fname=? WHERE user_id=?", (username, fname, uid))
        c.commit()

def is_banned(uid):
    r = qone("SELECT banned FROM users WHERE user_id=?", (uid,)); return bool(r and r["banned"])
def is_admin(uid):
    if uid == OWNER_ID: return True
    r = qone("SELECT is_admin FROM users WHERE user_id=?", (uid,)); return bool(r and r["is_admin"])
def is_subscribed(uid):
    if uid == OWNER_ID: return True
    r = qone("SELECT subscribed FROM users WHERE user_id=?", (uid,)); return bool(r and r["subscribed"])
def set_subscribed(uid): qrun("UPDATE users SET subscribed=1 WHERE user_id=?", (uid,))

def ban_user(uid):
    with sqlite3.connect(DB_FILE) as c:
        c.execute("INSERT OR IGNORE INTO users (user_id,created_at) VALUES (?,?)", (uid, now()))
        c.execute("UPDATE users SET banned=1 WHERE user_id=?", (uid,)); c.commit()
def unban_user(uid): qrun("UPDATE users SET banned=0 WHERE user_id=?", (uid,))
def promote_admin(uid):
    with sqlite3.connect(DB_FILE) as c:
        c.execute("INSERT OR IGNORE INTO users (user_id,created_at) VALUES (?,?)", (uid, now()))
        c.execute("UPDATE users SET is_admin=1 WHERE user_id=?", (uid,)); c.commit()
def demote_admin(uid): qrun("UPDATE users SET is_admin=0 WHERE user_id=?", (uid,))

def count_by_service(svc):
    r = qone("SELECT COUNT(*) cnt FROM numbers WHERE in_use=0 AND (service_tag=? OR service_tag='all')", (svc,))
    return r["cnt"] if r else 0

def get_countries(svc="all"):
    if svc == "all":
        return qall("SELECT country_code,country_name,flag,COUNT(*) cnt FROM numbers WHERE in_use=0 GROUP BY country_code ORDER BY country_name")
    return qall("SELECT country_code,country_name,flag,COUNT(*) cnt FROM numbers WHERE in_use=0 AND (service_tag=? OR service_tag='all') GROUP BY country_code ORDER BY country_name", (svc,))

def assign_number(uid, cc, svc="all"):
    with sqlite3.connect(DB_FILE) as c:
        row = c.execute("SELECT number FROM numbers WHERE used_by=? AND country_code=? AND in_use=1 LIMIT 1", (uid, cc)).fetchone()
        if row: return row[0]
        row = c.execute("SELECT number FROM numbers WHERE country_code=? AND (service_tag=? OR service_tag='all') AND in_use=0 LIMIT 1", (cc, svc)).fetchone()
        if not row: return None
        c.execute("UPDATE numbers SET in_use=1, used_by=? WHERE number=? AND country_code=?", (uid, row[0], cc))
        c.commit(); return row[0]

def change_number(uid, cc, svc="all"):
    with sqlite3.connect(DB_FILE) as c:
        cur = c.execute(
            "SELECT id, number FROM numbers WHERE used_by=? AND country_code=? AND in_use=1 LIMIT 1",
            (uid, cc)
        ).fetchone()
        cur_id  = cur[0] if cur else 0

        c.execute("UPDATE numbers SET in_use=0, used_by=0 WHERE used_by=? AND country_code=?", (uid, cc))
        c.commit()

        row = c.execute(
            """SELECT id, number FROM numbers
               WHERE country_code=? AND (service_tag=? OR service_tag='all')
               AND in_use=0 AND id > ?
               ORDER BY id ASC LIMIT 1""",
            (cc, svc, cur_id)
        ).fetchone()

        if not row:
            row = c.execute(
                """SELECT id, number FROM numbers
                   WHERE country_code=? AND (service_tag=? OR service_tag='all')
                   AND in_use=0
                   ORDER BY id ASC LIMIT 1""",
                (cc, svc)
            ).fetchone()

        if row:
            c.execute("UPDATE numbers SET in_use=1, used_by=? WHERE id=?", (uid, row[0]))
            c.commit()
            return row[1]
    return None

def add_numbers_bulk(lines, svc="all"):
    added = 0; by_country = {}
    with sqlite3.connect(DB_FILE) as c:
        for line in lines:
            num = re.sub(r'[^\d]', '', line.strip())
            if len(num) < 7: continue
            flag, name, code, _ = get_country_info(num)
            try:
                cur = c.execute("INSERT OR IGNORE INTO numbers (number,country_code,country_name,flag,service_tag,added_at) VALUES (?,?,?,?,?,?)",
                                (num, code, name, flag, svc, now()))
                if cur.rowcount > 0:
                    added += 1; k = f"{flag} {name}"; by_country[k] = by_country.get(k, 0) + 1
            except: pass
        c.commit()
    return added, by_country

def delete_numbers_by_service(svc):
    qrun("DELETE FROM numbers WHERE service_tag=? AND in_use=0", (svc,))

def get_sub_channels(): return qall("SELECT id,channel_link,channel_name FROM sub_channels")
def add_sub_channel(link, name):
    with sqlite3.connect(DB_FILE) as c:
        c.execute("INSERT OR IGNORE INTO sub_channels (channel_link,channel_name) VALUES (?,?)", (link, name)); c.commit()
def del_sub_channel(ch_id): qrun("DELETE FROM sub_channels WHERE id=?", (ch_id,))

def set_pending(uid, number, cc="", svc="all", msg_id=0):
    with sqlite3.connect(DB_FILE) as c:
        c.execute("INSERT OR REPLACE INTO pending_otps (user_id,number,country_code,service_tag,msg_id,asked_at) VALUES (?,?,?,?,?,?)",
                  (uid, number, cc, svc, msg_id, now())); c.commit()

def get_pending_by_number(number):
    r = qone("SELECT user_id,country_code,service_tag,msg_id FROM pending_otps WHERE number=?", (number,))
    return (r["user_id"], r["country_code"], r["service_tag"], r["msg_id"]) if r else None

def clear_pending(uid): qrun("DELETE FROM pending_otps WHERE user_id=?", (uid,))

processed_sms = set()

def load_processed():
    global processed_sms
    rows = qall("SELECT sms_hash FROM sms_records")
    processed_sms = {r["sms_hash"] for r in rows}
    print(f"📝 Loaded {len(processed_sms)} records")

def save_sms(record):
    h = hashlib.md5(f"{record.get('date','')}{record.get('number','')}{record.get('sms','')}".encode()).hexdigest()
    if h in processed_sms: return False
    processed_sms.add(h)
    try:
        with sqlite3.connect(DB_FILE) as c:
            c.execute("INSERT OR IGNORE INTO sms_records (sms_hash,date,source,number,cli,sms_text,otp_code,service,received_at) VALUES (?,?,?,?,?,?,?,?,?)",
                      (h, record.get('date',''), record.get('source',''), record.get('number',''),
                       record.get('cli',''), record.get('sms',''), record.get('otp',''),
                       record.get('service',''), now())); c.commit()
        return True
    except: return False

# ═══════════════════════════════════════════════════
#                    HELPERS
# ═══════════════════════════════════════════════════

def get_country_info(number):
    clean = re.sub(r'[^\d]', '', str(number)).lstrip('0')
    for length in range(5, 0, -1):
        p = clean[:length]
        if p in COUNTRY_CODES:
            name, flag, code = COUNTRY_CODES[p]
            return flag, name, code, p
    return "🌍", "Unknown", "?", ""

def mask_number(number):
    n = str(number).lstrip('+')
    if len(n) <= 6: return f"+{n}"
    half = len(n) // 2
    visible_start = n[:half - 1]
    visible_end   = n[-(3):]
    stars = '*' * (len(n) - len(visible_start) - len(visible_end))
    return f"+{visible_start}{stars}{visible_end}"

def solve_captcha(html):
    m = re.search(r'(\d+)\s*([+\-*/])\s*(\d+)\s*=?\s*\?', html)
    if m:
        a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
        return str({'+': a+b, '-': a-b, '*': a*b, '/': (a//b if b else 0)}.get(op, 0))
    return None

def extract_otp(text):
    for p in [r'(\d{3}[\-\s]\d{3})', r'(?:code|OTP|verify)[:\s]*(\d{4,8})', r'\b(\d{6})\b', r'\b(\d{4,8})\b']:
        m = re.search(p, text, re.IGNORECASE)
        if m: return m.group(1).replace(' ', '').replace('-', '')
    return None

def detect_service(cli, sms=''):
    combined = f"{cli} {sms}".lower()
    for svc, kws in [
        ('WhatsApp',  ['whatsapp', 'wa.me']),
        ('Telegram',  ['telegram']),
        ('Facebook',  ['facebook', 'meta', 'fb']),
        ('Instagram', ['instagram', 'ig']),
        ('Apple',     ['apple', 'icloud', 'appleid']),
        ('Microsoft', ['microsoft', 'outlook', 'msn']),
        ('Google',    ['google', 'gmail']),
        ('TikTok',    ['tiktok']),
        ('Twitter',   ['twitter', 'x.com']),
        ('Snapchat',  ['snapchat']),
        ('Amazon',    ['amazon']),
        ('Netflix',   ['netflix']),
    ]:
        if any(k in combined for k in kws): return svc
    return cli.strip() or 'SMS'

# ═══════════════════════════════════════════════════
#                  TELEGRAM API
# ═══════════════════════════════════════════════════

TG_BASE = f"https://api.telegram.org/bot{BOT_TOKEN}"
_sess = requests.Session()

def tg(method, **kw):
    try:
        r = _sess.post(f"{TG_BASE}/{method}", json=kw, timeout=10)
        return r.json()
    except Exception as e:
        print(f"  tg.{method}: {e}"); return {"ok": False}

def send(cid, text, markup=None):
    p = {"chat_id": cid, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if markup: p["reply_markup"] = markup
    return tg("sendMessage", **p)

def edit(cid, mid, text, markup=None):
    p = {"chat_id": cid, "message_id": mid, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if markup: p["reply_markup"] = markup
    return tg("editMessageText", **p)

def answer_cb(cb_id, text="", alert=False):
    tg("answerCallbackQuery", callback_query_id=cb_id, text=text, show_alert=alert)

# ═══════════════════════════════════════════════════
#                   KEYBOARDS
# ═══════════════════════════════════════════════════

def kb_sub():
    chs = get_sub_channels()
    rows = [[{"text": f"📢 {ch['channel_name']}", "url": ch["channel_link"], "style": "success"}] for ch in chs]
    rows.append([{"text": "✅ I Joined — Check", "callback_data": "sub_check", "style": "primary"}])
    return {"inline_keyboard": rows}

def kb_home():
    return {"inline_keyboard": [[{"text": "🏠 Home", "callback_data": "home", "style": "primary"}]]}

def kb_services():
    rows = []
    for svc in SERVICES:
        svc_id = svc["app"]
        emoji = svc["icon"]
        name = svc["name"]
        cnt = count_by_service(svc_id)
        rows.append([{"text": f"{emoji} {name} [{cnt}]", "callback_data": f"svc_{svc_id}", "style": "primary"}])
    if is_admin(OWNER_ID):
        rows.append([{"text": "⚙️ Admin Panel", "callback_data": "adm_menu", "style": "success"}])
    return {"inline_keyboard": rows}

def kb_services_for_user(uid):
    rows = []
    for svc in SERVICES:
        svc_id = svc["app"]
        emoji = svc["icon"]
        name = svc["name"]
        cnt = count_by_service(svc_id)
        rows.append([{"text": f"{emoji} {name} [{cnt}]", "callback_data": f"svc_{svc_id}", "style": "primary"}])
    if is_admin(uid):
        rows.append([{"text": "⚙️ Admin Panel", "callback_data": "adm_menu", "style": "success"}])
    return {"inline_keyboard": rows}

def kb_countries(svc="all"):
    ccs = get_countries(svc)
    rows = []
    row = []
    for c in ccs:
        row.append({"text": f"{c['flag']} {c['country_name']} ({c['cnt']})", "callback_data": f"cc_{svc}_{c['country_code']}", "style": "primary"})
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    if not rows:
        rows = [[{"text": "❌ No numbers available", "callback_data": "noop", "style": "danger"}]]
    rows.append([{"text": "◀️ Back", "callback_data": "home", "style": "primary"}])
    return {"inline_keyboard": rows}

def kb_number(number, cc, svc="all"):
    return {"inline_keyboard": [
        [{"text": f"📋 {number}", "callback_data": f"copyn_{number}", "style": "primary"}],
        [{"text": "🔄 Change Number", "callback_data": f"chnum_{svc}_{cc}", "style": "danger"}],
        [{"text": "📢 OTP Group", "callback_data": f"otp_group", "style": "primary"}],
        [{"text": "◀️ Back", "callback_data": f"back_cc_{svc}", "style": "primary"}],
    ]}

def kb_waiting(svc, cc):
    return {"inline_keyboard": [
        [{"text": "◀️ Back", "callback_data": f"back_cc_{svc}", "style": "primary"}]
    ]}

def kb_admin():
    return {"inline_keyboard": [
        [{"text": "➕ Add Numbers", "callback_data": "adm_add", "style": "success"},
         {"text": "🗑 Delete Numbers", "callback_data": "adm_del", "style": "danger"}],
        [{"text": "🚫 Ban User", "callback_data": "adm_ban", "style": "danger"},
         {"text": "✅ Unban User", "callback_data": "adm_unban", "style": "success"}],
        [{"text": "⬆️ Promote", "callback_data": "adm_promote", "style": "success"},
         {"text": "⬇️ Demote", "callback_data": "adm_demote", "style": "danger"}],
        [{"text": "📢 Add Channel", "callback_data": "adm_addch", "style": "success"},
         {"text": "❌ Del Channel", "callback_data": "adm_delch", "style": "danger"}],
        [{"text": "📢 Broadcast", "callback_data": "adm_broadcast", "style": "primary"},
         {"text": "📊 Statistics", "callback_data": "adm_stats", "style": "primary"}],
        [{"text": "🏠 Home", "callback_data": "home", "style": "primary"}],
    ]}

def kb_back_admin():
    return {"inline_keyboard": [[{"text": "◀️ Back to Admin", "callback_data": "adm_menu", "style": "success"}]]}

def kb_svc_picker(action):
    rows = []
    for svc in SERVICES:
        svc_id = svc["app"]
        emoji = svc["icon"]
        name = svc["name"]
        rows.append([{"text": f"{emoji} {name}", "callback_data": f"{action}_{svc_id}", "style": "primary"}])
    rows.append([{"text": "◀️ Back", "callback_data": "adm_menu", "style": "success"}])
    return {"inline_keyboard": rows}

def kb_del_ccs(svc):
    rows = qall("SELECT country_code,country_name,flag,COUNT(*) cnt FROM numbers WHERE in_use=0 AND (service_tag=? OR service_tag='all') GROUP BY country_code ORDER BY country_name", (svc,))
    if not rows: return None
    btns = [[{"text": f"{r['flag']} {r['country_name']} ({r['cnt']})", "callback_data": f"adm_dcc_{svc}_{r['country_code']}", "style": "danger"}] for r in rows]
    btns.append([{"text": "◀️ Back", "callback_data": "adm_del", "style": "success"}])
    return {"inline_keyboard": btns}

def kb_del_channels():
    chs = get_sub_channels()
    if not chs: return None
    rows = [[{"text": ch["channel_name"], "callback_data": f"adm_delchid_{ch['id']}", "style": "danger"}] for ch in chs]
    rows.append([{"text": "◀️ Back", "callback_data": "adm_menu", "style": "primary"}])
    return {"inline_keyboard": rows}

# ═══════════════════════════════════════════════════
#              OTP MESSAGE FORMAT
# ═══════════════════════════════════════════════════

def format_otp_group(record):
    flag, country, code, _ = get_country_info(record.get('number', ''))
    otp     = record.get('otp', '---')
    service = record.get('service', 'SMS')
    icon    = SVC_ICONS.get(service, '💬')
    source  = record.get('source', '')
    date    = record.get('date', now())
    masked  = mask_number(record.get('number', ''))

    text = (
        f"• <b>Alichbahalmjal◞౪◟𝗢𝗧𝗣</b> ◞౪◟\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"→ {flag} <b>#{code}</b>  {icon}  <code>{masked}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"<blockquote>🔑 {service} Code: <b>{otp}</b>\n"
        f"⚠️ Do not share this code</blockquote>\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"• 🕐 ~ {date}  🏷 <i>{source}</i>"
    )
    markup = {"inline_keyboard": [
        [{"text": f"🟩 🔑 {otp}  —  tap to copy", "callback_data": f"otpcopy_{otp}", "style": "primary"}],
        [{"text": "• 🤖 pot  •", "url": GROUP_LINK, "style": "success"}],
    ]}
    return text, markup

def format_otp_private(record):
    flag, country, code, _ = get_country_info(record.get('number', ''))
    otp     = record.get('otp', '---')
    service = record.get('service', 'SMS')
    icon    = SVC_ICONS.get(service, '💬')
    source  = record.get('source', '')
    date    = record.get('date', now())
    number  = record.get('number', '')

    text = (
        f"✅ <b>OTP Received!</b>\n\n"
        f"• <b>Alichbahalmjal◞౪◟𝗢𝗧𝗣</b> ◞౪◟\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"→ {flag} <b>#{code}</b>  {icon}  <code>{number}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"<blockquote>🔑 {service} Code: <b>{otp}</b>\n"
        f"⚠️ Do not share this code</blockquote>\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"• 🕐 ~ {date}  🏷 <i>{source}</i>"
    )
    
    markup = {"inline_keyboard": [
        [{"text": f"🔑 {otp}  —  tap to copy", "callback_data": f"otpcopy_{otp}", "style": "primary"}],
        [{"text": "• 🤖 pot  •", "url": GROUP_LINK, "style": "success"}]
    ]}
    
    return text, markup

# ═══════════════════════════════════════════════════
#              BROADCAST & STATISTICS
# ═══════════════════════════════════════════════════

def get_user_count():
    r = qone("SELECT COUNT(*) as cnt FROM users")
    return r["cnt"] if r else 0

def get_banned_count():
    r = qone("SELECT COUNT(*) as cnt FROM users WHERE banned=1")
    return r["cnt"] if r else 0

def get_admin_count():
    r = qone("SELECT COUNT(*) as cnt FROM users WHERE is_admin=1")
    return r["cnt"] if r else 0

def get_total_otps():
    r = qone("SELECT COUNT(*) as cnt FROM sms_records")
    return r["cnt"] if r else 0

def get_today_otps():
    today = datetime.now().strftime("%Y-%m-%d")
    r = qone("SELECT COUNT(*) as cnt FROM sms_records WHERE date LIKE ?", (f"{today}%",))
    return r["cnt"] if r else 0

def get_total_numbers():
    r = qone("SELECT COUNT(*) as cnt FROM numbers")
    return r["cnt"] if r else 0

def get_available_numbers():
    r = qone("SELECT COUNT(*) as cnt FROM numbers WHERE in_use=0")
    return r["cnt"] if r else 0

def get_inuse_numbers():
    r = qone("SELECT COUNT(*) as cnt FROM numbers WHERE in_use=1")
    return r["cnt"] if r else 0

def get_all_users():
    rows = qall("SELECT user_id FROM users")
    return [row["user_id"] for row in rows]

def send_broadcast(admin_id, message):
    users = get_all_users()
    success = 0
    failed = 0
    
    for uid in users:
        try:
            send(uid, message)
            success += 1
        except:
            failed += 1
        time.sleep(0.05)
    
    return success, failed

# ═══════════════════════════════════════════════════
#               USER STATE MACHINE
# ═══════════════════════════════════════════════════

_STATES = {}

def set_state(uid, step, **data): _STATES[uid] = {"step": step, "data": data}
def get_state(uid): return _STATES.get(uid, {})
def clear_state(uid): _STATES.pop(uid, None)

# ═══════════════════════════════════════════════════
#                 BOT HANDLERS
# ═══════════════════════════════════════════════════

def home_text():
    return (
        f"~ <b>{BOT_NAME}</b>\n\n"
        f"• ✅ Developer ~ <a href='tg://user?id={OWNER_ID}'>{DEVELOPER}</a>\n\n"
        f"• 📦 <b>Choose Service Category</b> ~"
    )

def handle_start(uid, username, fname):
    upsert_user(uid, username, fname)
    if is_banned(uid): send(uid, "🚫 You are banned."); return
    clear_state(uid)
    chs = get_sub_channels()
    if chs and not is_subscribed(uid):
        send(uid, "━━━━━━━━━━━━━━━━━━━━\n📢 <b>Join Required</b>\n━━━━━━━━━━━━━━━━━━━━\nJoin the channel below first:", markup=kb_sub())
        return
    send(uid, home_text(), markup=kb_services_for_user(uid))

def handle_help(uid):
    upsert_user(uid)
    svc_cmds = "\n".join(f"  {svc['path']}  —  {svc['icon']} {svc['name']}" for svc in SERVICES)
    text = (
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"<b>{BOT_NAME}</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "<b>How to use:</b>\n"
        "① /start — Main menu\n"
        "② Choose service\n"
        "③ Choose country\n"
        "④ Press Copy Number button → copied!\n"
        "⑤ Code arrives here automatically ⚡\n\n"
        "<b>Service Commands:</b>\n"
        f"{svc_cmds}\n\n"
        "<b>Other Commands:</b>\n"
        "/help — This message\n"
        "/getnumber — Choose service\n"
        "/admin — Admin panel\n"
        f"/Developer — Dev info"
    )
    send(uid, text, markup=kb_home())

def handle_developer(uid):
    upsert_user(uid)
    text = (
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "✅ <b>@HAMOO_2009 Info</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Bot: <b>{BOT_NAME}</b>\n"
        f"Version: <b>V6</b>\n"
        f"Developer: <b>{DEVELOPER}</b>\n\n"
        f"📢 <a href='{CHANNEL_LINK}'>Evan Channel</a>"
    )
    send(uid, text, markup=kb_home())

def handle_getnumber(uid, username="", fname=""):
    upsert_user(uid, username, fname)
    if is_banned(uid): send(uid, "🚫 You are banned."); return
    if not is_subscribed(uid):
        send(uid, "━━━━━━━━━━━━━━━━━━━━\n📢 <b>Join Required</b>\n━━━━━━━━━━━━━━━━━━━━\nJoin the channel below first:", markup=kb_sub()); return
    send(uid, home_text(), markup=kb_services_for_user(uid))

def handle_service_cmd(uid, svc_id, username="", fname=""):
    upsert_user(uid, username, fname)
    if is_banned(uid): send(uid, "🚫 You are banned."); return
    if not is_subscribed(uid):
        send(uid, "━━━━━━━━━━━━━━━━━━━━\n📢 <b>Join Required</b>\n━━━━━━━━━━━━━━━━━━━━\nJoin the channel below first:", markup=kb_sub()); return
    svc_info = next((s for s in SERVICES if s["app"] == svc_id), None)
    if not svc_info: return
    emoji = svc_info["icon"]
    name = svc_info["name"]
    cnt = count_by_service(svc_id)
    text = f"{emoji} <b>{name}</b>\n\nAvailable numbers: <b>{cnt}</b>\n\n🌍 Choose a country:"
    send(uid, text, markup=kb_countries(svc_id))

def handle_admin_cmd(uid):
    upsert_user(uid)
    if not is_admin(uid): send(uid, "❌ Not authorized."); return
    send(uid, "⚙️ <b>Admin Panel</b>", markup=kb_admin())

def handle_callback(cb_id, uid, data, mid, username="", fname=""):
    upsert_user(uid, username, fname)
    if is_banned(uid): answer_cb(cb_id, "🚫 Banned", alert=True); return

    if data.startswith("otpcopy_"):
        otp_val = data[8:]
        answer_cb(cb_id, "✅ Tap the code below to copy!", alert=False)
        send(uid, f"🔑 <b>Your OTP Code:</b>\n<code>{otp_val}</code>\n\n👆 Tap the code above to copy it")
        return

    if data.startswith("copyn_"):
        num = data[6:]
        answer_cb(cb_id, f"✅ Tap the number below to copy!", alert=False)
        send(uid, f"📋 <b>Your Number:</b>\n<code>{num}</code>\n\n👆 Tap the number above to copy it")
        return
    
    if data == "otp_group":
        answer_cb(cb_id, "📢 Opening OTP Group...", alert=False)
        send(uid, f"📢 <b>Join OTP Group</b>\n\n🔑 All OTP codes will appear here:\n<a href='{GROUP_LINK}'>🔗 Click to join</a>", markup=kb_home())
        return

    if data == "noop": answer_cb(cb_id); return

    answer_cb(cb_id)

    if data == "home":
        clear_state(uid)
        chs = get_sub_channels()
        if chs and not is_subscribed(uid):
            edit(uid, mid, "📢 Join required:", markup=kb_sub()); return
        edit(uid, mid, home_text(), markup=kb_services_for_user(uid)); return

    if data == "sub_check":
        set_subscribed(uid)
        edit(uid, mid, home_text(), markup=kb_services_for_user(uid)); return

    if not is_subscribed(uid):
        chs = get_sub_channels()
        if chs: send(uid, "📢 Join required:", markup=kb_sub()); return

    if data.startswith("svc_"):
        svc = data[4:]
        svc_info = next((s for s in SERVICES if s["app"] == svc), None)
        emoji = svc_info["icon"] if svc_info else "📦"
        name  = svc_info["name"] if svc_info else svc
        cnt   = count_by_service(svc)
        text  = f"{emoji} <b>{name}</b>\n\nAvailable: <b>{cnt}</b> numbers\n\n🌍 Choose a country:"
        edit(uid, mid, text, markup=kb_countries(svc)); return

    if data.startswith("back_cc_"):
        svc = data[8:]
        svc_info = next((s for s in SERVICES if s["app"] == svc), None)
        emoji = svc_info["icon"] if svc_info else "📦"
        name  = svc_info["name"] if svc_info else svc
        cnt   = count_by_service(svc)
        text  = f"{emoji} <b>{name}</b>\n\nAvailable: <b>{cnt}</b>\n\n🌍 Choose a country:"
        edit(uid, mid, text, markup=kb_countries(svc)); return

    if data.startswith("cc_"):
        parts = data.split("_", 2)
        if len(parts) < 3: return
        svc, cc = parts[1], parts[2]
        number = assign_number(uid, cc, svc)
        if not number:
            answer_cb(cb_id, "❌ No numbers available", alert=True); return
        flag, cname, _, _ = get_country_info(number)
        svc_info = next((s for s in SERVICES if s["app"] == svc), None)
        emoji = svc_info["icon"] if svc_info else "📦"
        name  = svc_info["name"] if svc_info else svc
        text = (
            f"{emoji} <b>{name}</b>\n"
            f"━━━━━━━━━━━━━━━━━\n"
            f"📱 {flag} <b>{cname}</b>\n"
            f"<code>{number}</code>\n"
            f"━━━━━━━━━━━━━━━━━\n"
            f"☝️ Tap number above OR button below to copy\n\n"
            f"⚡ <b>OTP will arrive automatically!</b>"
        )
        edit(uid, mid, text, markup=kb_number(number, cc, svc)); return

    if data.startswith("chnum_"):
        parts = data.split("_", 2)
        if len(parts) < 3: return
        svc, cc = parts[1], parts[2]
        number = change_number(uid, cc, svc)
        if not number:
            answer_cb(cb_id, "❌ No more numbers available", alert=True); return
        flag, cname, _, _ = get_country_info(number)
        svc_info = next((s for s in SERVICES if s["app"] == svc), None)
        emoji = svc_info["icon"] if svc_info else "📦"
        name  = svc_info["name"] if svc_info else svc
        text = (
            f"{emoji} <b>{name}</b>\n"
            f"━━━━━━━━━━━━━━━━━\n"
            f"📱 {flag} <b>{cname}</b>\n"
            f"<code>{number}</code>\n"
            f"━━━━━━━━━━━━━━━━━\n"
            f"🔄 New number! ☝️ Tap above to copy\n\n"
            f"⚡ <b>OTP will arrive automatically!</b>"
        )
        edit(uid, mid, text, markup=kb_number(number, cc, svc)); return

    # Broadcast
    if data == "adm_broadcast":
        set_state(uid, "wait_broadcast")
        edit(uid, mid, "📢 <b>Send the message to broadcast</b>\n\nSend any text message to send to all users:", markup=kb_back_admin())
        return

    # Statistics
    if data == "adm_stats":
        total_users = get_user_count()
        banned_users = get_banned_count()
        admin_users = get_admin_count()
        active_users = total_users - banned_users
        total_otps = get_total_otps()
        today_otps = get_today_otps()
        total_numbers = get_total_numbers()
        available_numbers = get_available_numbers()
        inuse_numbers = get_inuse_numbers()
        
        stats_text = (
            "📊 <b>Bot Statistics</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            f"👥 <b>Users:</b>\n"
            f"   • Total: {total_users}\n"
            f"   • Active: {active_users}\n"
            f"   • Banned: {banned_users}\n"
            f"   • Admins: {admin_users}\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            f"🔑 <b>OTP Statistics:</b>\n"
            f"   • Total OTPs: {total_otps}\n"
            f"   • Today: {today_otps}\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            f"📱 <b>Numbers:</b>\n"
            f"   • Total: {total_numbers}\n"
            f"   • Available: {available_numbers}\n"
            f"   • In Use: {inuse_numbers}\n"
            "━━━━━━━━━━━━━━━━━━━━━"
        )
        edit(uid, mid, stats_text, markup=kb_admin())
        return

    if not is_admin(uid): return

    if data == "adm_menu":
        clear_state(uid)
        edit(uid, mid, "⚙️ <b>Admin Panel</b>", markup=kb_admin()); return

    if data == "adm_add":
        edit(uid, mid, "🎯 <b>Choose service to add numbers for:</b>", markup=kb_svc_picker("adm_asvc")); return

    if data.startswith("adm_asvc_"):
        svc = data[9:]
        set_state(uid, "waiting_file", svc=svc)
        svc_info = next((s for s in SERVICES if s["app"] == svc), None)
        name = svc_info["name"] if svc_info else svc
        edit(uid, mid, f"🎯 <b>{name}</b>\n\n📂 Send <b>.txt</b> file (one number per line):", markup=kb_back_admin()); return

    if data == "adm_del":
        edit(uid, mid, "🗑 <b>Choose service to delete from:</b>", markup=kb_svc_picker("adm_dsvc")); return

    if data.startswith("adm_dsvc_"):
        svc = data[9:]
        kb = kb_del_ccs(svc)
        if not kb: answer_cb(cb_id, "No numbers found.", alert=True); return
        edit(uid, mid, "🌍 <b>Choose country to delete:</b>", markup=kb); return

    if data.startswith("adm_dcc_"):
        rest = data[8:]
        parts = rest.split("_", 1)
        if len(parts) < 2: return
        svc, cc = parts[0], parts[1]
        qrun("DELETE FROM numbers WHERE country_code=? AND service_tag=? AND in_use=0", (cc, svc))
        send(uid, f"✅ Deleted <b>{cc}</b> numbers from <b>{svc}</b>")
        edit(uid, mid, "⚙️ <b>Admin Panel</b>", markup=kb_admin()); return

    if data == "adm_ban":    set_state(uid, "wait_ban");     edit(uid, mid, "🚫 Send User ID to ban:",     markup=kb_back_admin()); return
    if data == "adm_unban":  set_state(uid, "wait_unban");   edit(uid, mid, "✅ Send User ID to unban:",   markup=kb_back_admin()); return
    if data == "adm_promote":set_state(uid, "wait_promote"); edit(uid, mid, "⬆️ Send User ID to promote:", markup=kb_back_admin()); return
    if data == "adm_demote": set_state(uid, "wait_demote");  edit(uid, mid, "⬇️ Send User ID to demote:",  markup=kb_back_admin()); return
    if data == "adm_addch":  set_state(uid, "wait_addch");   edit(uid, mid, "📢 Send @channel or link:",   markup=kb_back_admin()); return

    if data == "adm_delch":
        kb = kb_del_channels()
        if not kb: answer_cb(cb_id, "No channels.", alert=True); return
        edit(uid, mid, "❌ Choose channel to remove:", markup=kb); return

    if data.startswith("adm_delchid_"):
        ch_id = int(data[12:]); del_sub_channel(ch_id)
        send(uid, "✅ Channel removed.")
        edit(uid, mid, "⚙️ <b>Admin Panel</b>", markup=kb_admin()); return

def handle_text(uid, text, username="", fname=""):
    upsert_user(uid, username, fname)
    if is_banned(uid): return
    state = get_state(uid); step = state.get("step", "")
    if not step: return
    text = text.strip()

    def id_action(fn, ok_msg):
        try:
            target = int(text); fn(target)
            send(uid, ok_msg.format(id=target), markup=kb_back_admin())
        except ValueError:
            send(uid, "❌ Invalid ID. Send a number.", markup=kb_back_admin())
        finally: clear_state(uid)

    if step == "wait_broadcast":
        success, failed = send_broadcast(uid, text)
        send(uid, f"📢 <b>Broadcast Complete!</b>\n\n✅ Sent: {success}\n❌ Failed: {failed}\n📊 Total users: {success + failed}", markup=kb_back_admin())
        clear_state(uid)
    elif step == "wait_ban":     id_action(ban_user,     "✅ Banned <code>{id}</code>")
    elif step == "wait_unban":   id_action(unban_user,   "✅ Unbanned <code>{id}</code>")
    elif step == "wait_promote": id_action(promote_admin,"✅ Promoted <code>{id}</code>")
    elif step == "wait_demote":  id_action(demote_admin, "✅ Demoted <code>{id}</code>")
    elif step == "wait_addch":
        m = re.search(r't\.me/([A-Za-z0-9_]+)', text)
        if m:    link, name = f"https://t.me/+rKps8WMdwb5mZjA0{m.group(1)}", f"@{m.group(1)}"
        elif text.startswith('@'): link, name = f"https://t.me/{text.lstrip('@')}", text
        else:    link, name = text, text
        add_sub_channel(link, name)
        send(uid, "✅ Channel added.", markup=kb_back_admin()); clear_state(uid)
    elif step == "waiting_file":
        lines = text.splitlines(); svc = state["data"].get("svc", "all")
        added, by_c = add_numbers_bulk(lines, svc)
        summary = "\n".join(f"  {c}: {n}" for c, n in by_c.items()) or "  None"
        send(uid, f"✅ <b>Added {added} numbers</b> for <b>{svc}</b>\n\n{summary}", markup=kb_back_admin())
        clear_state(uid)

def handle_document(uid, file_id, file_name="file.txt", username="", fname=""):
    upsert_user(uid, username, fname)
    if is_banned(uid): return
    state = get_state(uid)
    if state.get("step") != "waiting_file":
        send(uid, "ℹ️ Use Admin Panel → Add Numbers first."); return
    svc = state["data"].get("svc", "all")
    try:
        r = tg("getFile", file_id=file_id)
        if not r.get("ok"): send(uid, "❌ Cannot download file.", markup=kb_back_admin()); clear_state(uid); return
        fp = r["result"]["file_path"]
        dl = requests.get(f"https://api.telegram.org/file/bot{BOT_TOKEN}/{fp}", timeout=30); dl.raise_for_status()
        lines = [l.strip() for l in dl.text.splitlines() if l.strip()]
        if not lines: send(uid, "❌ Empty file.", markup=kb_back_admin()); clear_state(uid); return
        added, by_c = add_numbers_bulk(lines, svc)
        summary = "\n".join(f"  {c}: {n}" for c, n in by_c.items()) or "  None"
        send(uid, f"✅ <b>File processed!</b>\n📊 Added: <b>{added}</b>\n📂 <code>{file_name}</code>\n🎯 Service: <b>{svc}</b>\n\n{summary}", markup=kb_back_admin())
    except Exception as e:
        send(uid, f"❌ Error: <code>{e}</code>", markup=kb_back_admin())
    finally: clear_state(uid)

# ═══════════════════════════════════════════════════
#               OTP DISPATCHER
# ═══════════════════════════════════════════════════

def dispatch_otp(record):
    number = record.get('number', '')

    group_text, group_markup = format_otp_group(record)
    if OTP_GROUP_ID:
        tg("sendMessage", chat_id=OTP_GROUP_ID, text=group_text,
           parse_mode="HTML", reply_markup=group_markup,
           disable_web_page_preview=True)

    pending = get_pending_by_number(number)
    if pending:
        user_id, cc, svc, old_msg_id = pending
        priv_text, priv_markup = format_otp_private(record)

        if old_msg_id:
            tg("deleteMessage", chat_id=user_id, message_id=old_msg_id)

        send(user_id, priv_text, markup=priv_markup)
        clear_pending(user_id)
    else:
        # Even if no pending request, try to find which user is using this number
        with sqlite3.connect(DB_FILE) as c:
            row = c.execute("SELECT used_by FROM numbers WHERE number=?", (number,)).fetchone()
            if row and row[0]:
                user_id = row[0]
                priv_text, priv_markup = format_otp_private(record)
                send(user_id, priv_text, markup=priv_markup)

# ═══════════════════════════════════════════════════
#               SMS CLIENTS
# ═══════════════════════════════════════════════════

class TimeSMSClient:
    def __init__(self, username, password, label):
        self.username = username; self.password = password; self.label = label
        self.base = TIMESMS_BASE
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        self.session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
        self.session.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))
        self.logged_in = False; self.last_login = 0; self.ajax_url = None
        self._lock = threading.Lock()

    def login(self):
        with self._lock:
            if self.logged_in and (time.time() - self.last_login) < SESSION_REFRESH: return True
            for attempt in range(3):
                try:
                    r = self.session.get(f"{self.base}/login", timeout=15)
                    cap = solve_captcha(r.text)
                    data = {'username': self.username, 'password': self.password}
                    if cap: data['capt'] = cap
                    lr = self.session.post(f"{self.base}/signin", data=data,
                                           headers={'Referer': f"{self.base}/login"},
                                           timeout=15, allow_redirects=True)
                    if 'login' not in str(lr.url).lower():
                        self.logged_in = True; self.last_login = time.time(); self.ajax_url = None
                        print(f"   ✅ [{self.label}] Login OK"); return True
                except Exception as e:
                    print(f"   ⚠️ [{self.label}] attempt {attempt+1}: {e}")
                time.sleep(1)
            self.logged_in = False; return False

    def fetch_sms(self):
        if not self.login(): return None
        try:
            if not self.ajax_url:
                r = self.session.get(f"{self.base}/agent/SMSCDRReports", timeout=15)
                if 'login' in str(r.url).lower(): self.logged_in = False; return None
                m = re.search(r'sAjaxSource["\s:]+["\']([^"\']+data_smscdr\.php[^"\']*)["\']', r.text)
                if m:
                    self.ajax_url = f"{self.base}/agent/{m.group(1)}"
                else:
                    d = datetime.now().strftime('%Y-%m-%d')
                    self.ajax_url = f"{self.base}/agent/res/data_smscdr.php?fdate1={d} 00:00:00&fdate2={d} 23:59:59&fg=0"

            sep = '&' if '?' in self.ajax_url else '?'
            url = f"{self.ajax_url}{sep}sEcho=1&iDisplayStart=0&iDisplayLength=500"
            r = self.session.get(url, headers={
                'Referer': f"{self.base}/agent/SMSCDRReports",
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            }, timeout=15)
            if r.status_code != 200: return None
            rows = r.json().get('aaData', [])
            records = []
            for row in rows:
                if not row or str(row[0]) in ('0', ''): continue
                num   = str(row[2]) if len(row) > 2 else ''
                cli_v = str(row[3]) if len(row) > 3 else ''
                sms_v = str(row[5]) if len(row) > 5 else ''
                if not num or not re.search(r'\d{7,}', num): continue
                records.append({
                    'date': str(row[0]), 'number': re.sub(r'[^\d]', '', num),
                    'cli': cli_v, 'sms': sms_v,
                    'otp': extract_otp(sms_v),
                    'service': detect_service(cli_v, sms_v),
                    'source': self.label
                })
            return records
        except Exception as e:
            print(f"   ❌ [{self.label}] fetch: {e}"); self.ajax_url = None; return None

    def force_refresh(self):
        self.logged_in = False; self.last_login = 0; self.ajax_url = None
        self.session.cookies.clear()



class GreenSMSClient:
    def __init__(self, username, password, label):
        self.username = username
        self.password = password
        self.label = label
        self.base = GREEN_BASE
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})
        self.logged_in = False

    def login(self):
        try:
            r = self.session.get(f"{self.base}/login", timeout=15)
            cap = solve_captcha(r.text)

            data = {
                'username': self.username,
                'password': self.password,
            }

            if cap:
                data['capt'] = cap

            lr = self.session.post(f"{self.base}/login", data=data, timeout=15)

            if "login" not in lr.url.lower():
                self.logged_in = True
                return True
        except:
            pass

        self.logged_in = False
        return False

    def fetch_sms(self):
        if not self.login():
            return None

        try:
            url = f"{self.base}/agent/res/data_smscdr.php?sEcho=1&iDisplayStart=0&iDisplayLength=200"
            r = self.session.get(url, timeout=15)

            if r.status_code != 200:
                return None

            data = r.json().get("aaData", [])
            records = []

            for row in data:
                if not row:
                    continue

                num = str(row[2]) if len(row) > 2 else ''
                cli_v = str(row[3]) if len(row) > 3 else ''
                sms_v = str(row[5]) if len(row) > 5 else ''

                if not num:
                    continue

                records.append({
                    'date': str(row[0]),
                    'number': re.sub(r'[^\d]', '', num),
                    'cli': cli_v,
                    'sms': sms_v,
                    'otp': extract_otp(sms_v),
                    'service': detect_service(cli_v, sms_v),
                    'source': self.label
                })

            return records

        except:
            return None


class IMSSMSClient:
    def __init__(self, username, password, label):
        self.username = username; self.password = password; self.label = label
        self.base = IMSSMS_BASE
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        })
        self.session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
        self.session.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))
        self.logged_in = False; self.last_login = 0
        self._lock = threading.Lock()

    def login(self):
        with self._lock:
            if self.logged_in and (time.time() - self.last_login) < SESSION_REFRESH: return True
            login_url = f"{self.base}/login"
            for attempt in range(3):
                try:
                    r = self.session.get(login_url, timeout=15)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    data = {}
                    for inp in soup.find_all('input'):
                        nm  = inp.get('name', ''); tp = inp.get('type', '').lower()
                        val = inp.get('value', '')
                        if not nm: continue
                        if tp == 'hidden':
                            data[nm] = val
                        elif tp in ('text', 'email') or re.search(r'user|login|email', nm, re.I):
                            data[nm] = self.username
                        elif tp == 'password':
                            data[nm] = self.password
                    if not any(v == self.username for v in data.values()):
                        data['username'] = self.username
                    if not any(v == self.password for v in data.values()):
                        data['password'] = self.password
                    cap = solve_captcha(r.text)
                    if cap: data['capt'] = cap

                    lr = self.session.post(login_url, data=data,
                                           headers={'Referer': login_url, 'Content-Type': 'application/x-www-form-urlencoded'},
                                           timeout=15, allow_redirects=True)
                    if lr.status_code == 200 and 'login' not in lr.url.lower():
                        self.logged_in = True; self.last_login = time.time()
                        print(f"   ✅ [{self.label}] Login OK"); return True
                    if any('session' in k.lower() or 'auth' in k.lower() for k in self.session.cookies.keys()):
                        self.logged_in = True; self.last_login = time.time()
                        print(f"   ✅ [{self.label}] Login OK (cookie)"); return True
                except Exception as e:
                    print(f"   ⚠️ [{self.label}] attempt {attempt+1}: {e}")
                time.sleep(2)
            self.logged_in = False; return False

    def fetch_sms(self):
        if not self.login(): return None
        today = datetime.now().strftime('%Y-%m-%d')
        endpoints = [
            f"{self.base}/agent/res/data_smscdr.php?fdate1={today} 00:00:00&fdate2={today} 23:59:59&sEcho=1&iDisplayStart=0&iDisplayLength=500",
            f"{self.base}/agent/SMSCDRReports",
            f"{self.base}/reports",
            f"{self.base}/sms",
            f"{self.base}/api/sms?date={today}",
            f"{self.base}/inbox",
        ]
        for url in endpoints:
            try:
                r = self.session.get(url, timeout=12, headers={
                    'Accept': 'application/json,text/html',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Referer': self.base,
                })
                if r.status_code != 200: continue
                if 'login' in r.url.lower(): self.logged_in = False; continue

                try:
                    js = r.json()
                    rows = (js.get('aaData') or js.get('data') or
                            js.get('sms') or js.get('records') or
                            js.get('messages') or [])
                    if rows:
                        return self._parse_rows(rows)
                except: pass

                soup = BeautifulSoup(r.text, 'html.parser')
                trs = soup.select('table tbody tr') or soup.select('table tr')
                if len(trs) > 1:
                    records = []
                    for row in trs:
                        cols = [td.get_text(strip=True) for td in row.find_all('td')]
                        if len(cols) >= 3:
                            num   = re.sub(r'[^\d]', '', cols[1] if len(cols) > 1 else '')
                            cli_v = cols[2] if len(cols) > 2 else ''
                            sms_v = cols[3] if len(cols) > 3 else (cols[-1] if cols else '')
                            if len(num) < 7: continue
                            records.append({
                                'date': cols[0], 'number': num, 'cli': cli_v,
                                'sms': sms_v, 'otp': extract_otp(sms_v),
                                'service': detect_service(cli_v, sms_v),
                                'source': self.label
                            })
                    if records: return records
            except Exception as e:
                pass
        return []

    def _parse_rows(self, rows):
        records = []
        for row in rows:
            if isinstance(row, dict):
                num   = str(row.get('number', row.get('phone', row.get('to', ''))))
                cli_v = str(row.get('sender', row.get('cli',  row.get('from', ''))))
                sms_v = str(row.get('message',row.get('sms',  row.get('text', ''))))
                date  = str(row.get('date',   row.get('time', row.get('created_at', ''))))
            elif isinstance(row, list) and len(row) >= 3:
                num   = str(row[2]) if len(row) > 2 else ''
                cli_v = str(row[3]) if len(row) > 3 else ''
                sms_v = str(row[5]) if len(row) > 5 else ''
                date  = str(row[0])
            else: continue
            num = re.sub(r'[^\d]', '', num)
            if len(num) < 7: continue
            records.append({
                'date': date, 'number': num, 'cli': cli_v,
                'sms': sms_v, 'otp': extract_otp(sms_v),
                'service': detect_service(cli_v, sms_v),
                'source': self.label
            })
        return records

    def force_refresh(self):
        self.logged_in = False; self.last_login = 0; self.session.cookies.clear()

# ═══════════════════════════════════════════════════
#               SMS MONITOR
# ═══════════════════════════════════════════════════

class SMSMonitor:
    def __init__(self):
        self.clients = []
        for acc in TIMESMS_ACCOUNTS:
            self.clients.append(TimeSMSClient(acc["username"], acc["password"], acc["label"]))
        for acc in IMSSMS_ACCOUNTS:
            self.clients.append(IMSSMSClient(acc["username"], acc["password"], acc["label"]))
        self.running = False
        self.stats = {"fetches": 0, "new": 0}
        print(f"📡 Monitor ready — {len(self.clients)} clients:")
        for c in self.clients: print(f"   • {c.label}")

    def fetch_all(self):
        result = []; lock = threading.Lock()
        def fetch_one(client):
            try:
                recs = client.fetch_sms()
                if recs:
                    with lock: result.extend(recs)
            except Exception as e:
                print(f"   ❌ [{getattr(client,'label','?')}] {e}")
        threads = [threading.Thread(target=fetch_one, args=(c,), daemon=True) for c in self.clients]
        for th in threads: th.start()
        for th in threads: th.join(timeout=25)
        return result

    def run(self):
        errors = 0
        while self.running:
            try:
                recs = self.fetch_all(); self.stats["fetches"] += 1
                for rec in recs:
                    if rec.get('otp') and save_sms(rec):
                        self.stats["new"] += 1
                        print(f"📩 [{rec.get('source','')}] {rec.get('number','')} → OTP:{rec.get('otp','?')} [{rec.get('service','')}]")
                        dispatch_otp(rec)
                errors = 0
                if self.stats["fetches"] % 30 == 0:
                    print(f"   💚 Fetches:{self.stats['fetches']} | New OTPs:{self.stats['new']}")
            except KeyboardInterrupt:
                print("\n🛑 Monitor stopped."); break
            except Exception as e:
                errors += 1; print(f"❌ Monitor error: {e}")
                if errors > 5:
                    for c in self.clients:
                        try: c.force_refresh()
                        except: pass
                    errors = 0
            time.sleep(POLL_INTERVAL)

# ═══════════════════════════════════════════════════
#              TELEGRAM POLLING
# ═══════════════════════════════════════════════════

def poll_bot():
    print(f"🤖 {BOT_NAME} — polling started")
    offset = None; ps = requests.Session()
    while True:
        try:
            params = {"timeout": 25, "allowed_updates": ["message", "callback_query"]}
            if offset: params["offset"] = offset
            r = ps.get(f"{TG_BASE}/getUpdates", params=params, timeout=30)
            updates = r.json().get("result", [])
            for u in updates:
                offset = u["update_id"] + 1
                try: process_update(u)
                except Exception as e:
                    print(f"   ❌ Update: {e}"); traceback.print_exc()
        except KeyboardInterrupt: break
        except Exception as e:
            print(f"   ❌ Poll: {e}"); time.sleep(2)

SVC_CMD_MAP = {svc["path"]: svc["app"] for svc in SERVICES}

def process_update(u):
    if "callback_query" in u:
        cb = u["callback_query"]; uid = cb["from"]["id"]
        data = cb.get("data", ""); msg = cb.get("message", {})
        mid = msg.get("message_id")
        uname = cb["from"].get("username", ""); fname = cb["from"].get("first_name", "")
        handle_callback(cb["id"], uid, data, mid, uname, fname)
    elif "message" in u:
        msg = u["message"]; uid = msg["from"]["id"]
        uname = msg["from"].get("username", ""); fname = msg["from"].get("first_name", "")
        text = msg.get("text", ""); doc = msg.get("document")
        if   text == "/start":      handle_start(uid, uname, fname)
        elif text == "/help":       upsert_user(uid, uname, fname); handle_help(uid)
        elif text == "/admin":      upsert_user(uid, uname, fname); handle_admin_cmd(uid)
        elif text == "/getnumber":  handle_getnumber(uid, uname, fname)
        elif text == "/Developer":  upsert_user(uid, uname, fname); handle_developer(uid)
        elif text in SVC_CMD_MAP:   handle_service_cmd(uid, SVC_CMD_MAP[text], uname, fname)
        elif doc:                   handle_document(uid, doc["file_id"], doc.get("file_name","file.txt"), uname, fname)
        elif text:                  handle_text(uid, text, uname, fname)

# ═══════════════════════════════════════════════════
#                     MAIN
# ═══════════════════════════════════════════════════

def main():
    print(f"\n{'═'*55}")
    print(f"  {BOT_NAME}  V6")
    print(f"{'═'*55}\n")
    mode = sys.argv[1].lower() if len(sys.argv) > 1 else "run"
    init_db()

    if mode == "run":
        load_processed()
        mon = SMSMonitor(); mon.running = True
        threading.Thread(target=mon.run, daemon=True).start()
        poll_bot()
    elif mode == "bot":
        poll_bot()
    elif mode == "monitor":
        load_processed(); mon = SMSMonitor(); mon.running = True; mon.run()
    elif mode == "test":
        print("🧪 Testing panels...")
        mon = SMSMonitor(); recs = mon.fetch_all()
        print(f"\n📊 Total records fetched: {len(recs)}")
        for r in recs[:10]:
            flag, _, code, _ = get_country_info(r['number'])
            print(f"  [{r['source']}] {flag} +{r['number'][:4]}***  OTP:{r.get('otp','?')}  [{r.get('service','')}]")
    else:
        print("  Usage: python bot_v6.py  run | bot | monitor | test")

if __name__ == "__main__":
    main()