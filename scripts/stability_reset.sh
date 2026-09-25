#!/bin/bash
# Stability breaker reset — spustit pokud gateway neběží po pádu
STABILITY_DIR=~/.openclaw/logs/stability
BUNDLE_COUNT=0

if [ "" -gt "0" ]; then
    echo "[Thu Aug 27 12:07:09 CEST 2026] Mažu  stability bundlů..."
    rm -f ""/*.json
    echo "[Thu Aug 27 12:07:09 CEST 2026] Smazáno. Restartuji gateway..."
    launchctl kickstart -k gui/$(id -u)/ai.openclaw.gateway
    sleep 5
    PID=$(ps aux | grep 'node.*openclaw.*dist' | grep -v grep | awk '{print $2}')
    if [ -n "$PID" ]; then
        echo "[Thu Aug 27 12:07:09 CEST 2026] Gateway běží (PID $PID)"
    else
        echo "[Thu Aug 27 12:07:09 CEST 2026] WARN: Gateway PID nenalezen"
    fi
else
    echo "[Thu Aug 27 12:07:09 CEST 2026] Žádné stability bundly — gateway by měl běžet OK"
fi
