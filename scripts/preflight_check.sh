#!/bin/bash
# Lisa Pre-flight Check — spustit PŘED každým ranním cyklem
# Verze: 1.0 — přidáno Moulou 25.8.2026

DISCORD_TOKEN=$(cat ~/.openclaw/openclaw.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('channels',{}).get('discord',{}).get('token',''))" 2>/dev/null)
CHANNEL_ID="1536678891928948830"
MANTICORE_URL="https://searchnew.tfsys.eu/results"
MANTICORE_PASS=$(cat ~/.openclaw/openclaw.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('env',{}).get('MANTICORE_PASS',''))" 2>/dev/null)

PASS=true
REPORT=""

send_discord() {
  curl -s -X POST     -H "Authorization: Bot $DISCORD_TOKEN"     -H "Content-Type: application/json"     -d "{\"content\":\"$1\"}"     "https://discord.com/api/v10/channels/$CHANNEL_ID/messages" > /dev/null
}

# 1. GSC test
echo "Testing GSC..."
GSC_SA=$(find ~/.openclaw/creds/ -name '*sa*.json' -o -name '*service*account*.json' 2>/dev/null | head -1)
if [ -z "$GSC_SA" ]; then
  REPORT+="❌ GSC: service account soubor nenalezen\n"
  PASS=false
else
  REPORT+="✅ GSC: SA soubor nalezen ($(basename $GSC_SA))\n"
fi

# 2. Manticore test
echo "Testing Manticore..."
MANTICORE_STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$MANTICORE_URL"   -H "Content-Type: application/json"   -H "Authorization: Bearer $MANTICORE_PASS"   -d '{"index":"test","query":{"match":{"*":"test"}}}'   --max-time 5 2>/dev/null)

if [ "$MANTICORE_STATUS" = "200" ] || [ "$MANTICORE_STATUS" = "400" ]; then
  REPORT+="✅ Manticore: endpoint /results odpovídá (HTTP $MANTICORE_STATUS)\n"
else
  REPORT+="⚠️ Manticore: /results vrátil HTTP $MANTICORE_STATUS — použij WP REST fallback\n"
fi

# 3. WP API test
echo "Testing WP REST..."
WP_LSA=$(curl -s -o /dev/null -w "%{http_code}" "https://www.letemsvetemapplem.eu/wp-json/wp/v2/posts?per_page=1" --max-time 5 2>/dev/null)
if [ "$WP_LSA" = "200" ]; then
  REPORT+="✅ WP LSA: REST API dostupné\n"
else
  REPORT+="❌ WP LSA: REST API nedostupné (HTTP $WP_LSA)\n"
  PASS=false
fi

# 4. Výsledek
echo -e "$REPORT"
DATE_STR=$(date '+%d.%m.%Y %H:%M')

if [ "$PASS" = true ]; then
  MSG="🟢 **Lisa Pre-flight $DATE_STR — PASS** — ranní cyklus může začít\n$REPORT"
else
  MSG="🔴 **Lisa Pre-flight $DATE_STR — FAIL** — cyklus ZASTAVEN\n$REPORT\nOpravte blokaday před spuštěním."
fi

send_discord "$MSG"
echo "Výsledek odeslán do Discord."
