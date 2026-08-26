#!/usr/bin/env python3
"""Denní check nákladů přes Anthropic Admin API"""
import os, json, sys, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

ADMIN_KEY = os.environ.get("ANTHROPIC_ADMIN_KEY", "")
if not ADMIN_KEY:
    print("❌ ANTHROPIC_ADMIN_KEY není nastaven v env")
    sys.exit(1)

today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")

headers = {"anthropic-version": "2023-06-01", "x-api-key": ADMIN_KEY}
url = f"https://api.anthropic.com/v1/usage?start_date={yesterday}&end_date={today}&granularity=day"

try:
    r = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(r, timeout=10) as resp:
        data = json.loads(resp.read())
    total = sum(d.get("cost_usd", 0) for d in data.get("data", []))
    print(f"📊 {yesterday} → {today}")
    for d in data.get("data", []):
        print(f"  {d.get('date','?')}: ${d.get('cost_usd',0):.4f} | {d.get('input_tokens',0):,} in / {d.get('output_tokens',0):,} out")
    print(f"  CELKEM: ${total:.4f} (~{total*23:.0f} Kč)")
except urllib.error.HTTPError as e:
    print(f"❌ HTTP {e.code}: {e.read().decode()[:300]}")
except Exception as e:
    print(f"❌ {e}")
