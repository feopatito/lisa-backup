#!/usr/bin/env python3
"""
Daily Learning Loop — Lisa
Spouštět na konci každého ranního cyklu.
"""
import json, datetime, os, sys

CACHE_DIR = os.path.expanduser('~/.openclaw/workspace/cache')
TODAY = datetime.date.today().strftime('%Y-%m-%d')
OUTPUT = os.path.join(CACHE_DIR, f'session_learnings_{TODAY}.md')

def load_yesterday():
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    path = os.path.join(CACHE_DIR, f'session_learnings_{yesterday}.md')
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return None

def write_learning(approved=None, rejected=None, rule=None, notes=None):
    yesterday_ctx = load_yesterday()
    content = f"""# Session Learnings — {TODAY}

## Co Roman schválil dnes
{chr(10).join(f"- {a}" for a in (approved or ["(nic zaznamenáno)"]))}

## Co Roman odmítl (s důvodem)
{chr(10).join(f"- {r}" for r in (rejected or ["(nic zaznamenáno)"]))}

## Pravidlo pro zítřek
{rule or "(nenaučila jsem se nic nového)"}

## Poznámky
{notes or "-"}

## Kontext z včerejška
{yesterday_ctx[:500] if yesterday_ctx else "(první den nebo po resetu)"}
"""
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(OUTPUT, 'w') as f:
        f.write(content)
    print(f'Learning soubor zapsán: {OUTPUT}')
    return OUTPUT

if __name__ == '__main__':
    approved = sys.argv[1].split(',') if len(sys.argv) > 1 and sys.argv[1] else []
    rejected = sys.argv[2].split(',') if len(sys.argv) > 2 and sys.argv[2] else []
    rule = sys.argv[3] if len(sys.argv) > 3 else None
    notes = sys.argv[4] if len(sys.argv) > 4 else None
    write_learning(approved, rejected, rule, notes)
