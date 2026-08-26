#!/bin/bash
set -e

echo "🚀 Setup: Lisa běží 24/7"
echo ""

# 1. LaunchAgent (HOTOV)
echo "✅ LaunchAgent ai.openclaw.continuous — AKTIVNÍ"
echo ""

# 2. SSH key (bez sudo)
echo "📝 Generuji SSH klíč..."
mkdir -p ~/.ssh
if [ ! -f ~/.ssh/id_ed25519 ]; then
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "lisa@$(hostname)" >/dev/null 2>&1
    echo "   ✅ SSH klíč vytvořen"
else
    echo "   ℹ️  SSH klíč už existuje"
fi

# 3. Info
echo ""
echo "=================================="
echo "✅ SETUP — ČÁST 1 HOTOVA"
echo "=================================="
echo ""
echo "HOTOVO:"
echo "  ✅ LaunchAgent (automatic restart)"
echo "  ✅ SSH key (pro remote control)"
echo ""
echo "ZBÝVÁ (vyžaduje sudo heslo):"
echo "  ⏳ Sleep mode disable"
echo "  ⏳ Wake-on-LAN"
echo "  ⏳ SSH server enable"
echo ""
echo "🌐 Tvoje SSH public key:"
echo "---"
cat ~/.ssh/id_ed25519.pub
echo "---"
echo ""
echo "👉 TEĎKA SPUSŤ:"
echo ""
echo "   sudo pmset -a disablesleep 1"
echo "   sudo pmset -a womp 1"
echo "   sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist"
echo ""
echo "Nebo zkopíruj tohle:"
cat << 'SUDOCMD'
sudo pmset -a disablesleep 1 && sudo pmset -a womp 1 && sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist && echo "✅ HOTOVO"
SUDOCMD
echo ""
