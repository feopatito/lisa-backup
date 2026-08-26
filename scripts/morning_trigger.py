#!/usr/bin/env python3
"""
Ranní trigger pro Lisa editorial cycle.
Spouští se LaunchAgentem každý všední den v 6:00.
"""
import json, requests, datetime, os, sys

LOG = '/Users/lisa/.openclaw/workspace/logs/morning-trigger.log'

def log(msg):
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG, 'a') as f:
        f.write(line + '\n')

# Víkend přeskočit
weekday = datetime.datetime.now().weekday()  # 0=Po, 6=Ne
if weekday >= 5:
    log(f"Víkend (weekday={weekday}), cycle se nespouští.")
    sys.exit(0)

# Health check — SA soubor
SA_PATH = '/Users/lisa/.openclaw/creds/android-magazine-sa.json'
WRONG_SA = '/Users/lisa/.openclaw/workspace/android-magazine-sa.json'
if not os.path.exists(SA_PATH):
    if os.path.exists(WRONG_SA):
        import shutil
        shutil.copy(WRONG_SA, SA_PATH)
        os.chmod(SA_PATH, 0o600)
        log("⚠️ SA soubor byl na špatném místě — automaticky opraveno.")
    else:
        log("❌ KRITICKÁ CHYBA: android-magazine-sa.json nenalezen v creds/!")

# Načíst Discord token
try:
    with open('/Users/lisa/.openclaw/openclaw.json') as f:
        cfg = json.load(f)
    token = cfg['channels']['discord']['token']
except Exception as e:
    log(f"❌ Nelze načíst Discord token: {e}")
    sys.exit(1)

# Odeslat trigger zprávu do #ai_nastavení_lisa
CHANNEL_ID = '1540072798062514186'
msg = "@Lisa spusť ranní editorial cycle"

r = requests.post(
    f'https://discord.com/api/v10/channels/{CHANNEL_ID}/messages',
    headers={'Authorization': f'Bot {token}', 'Content-Type': 'application/json'},
    json={'content': msg},
    timeout=15
)

if r.status_code in (200, 201):
    log(f"✅ Trigger odeslán do Discord (HTTP {r.status_code})")
else:
    log(f"❌ Discord API chyba: HTTP {r.status_code} — {r.text[:200]}")
