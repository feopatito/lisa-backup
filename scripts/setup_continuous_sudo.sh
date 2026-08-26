#!/bin/bash
set -e

echo "🚀 Setup: Lisa běží 24/7 + SSH remote control"
echo ""

# LaunchAgent je už hotov (bez sudo)
echo "✅ LaunchAgent: HOTOV"
echo ""

# Zbytek vyžaduje sudo heslo
read -sp "🔐 Zadej heslo pro sudo: " PASS
echo ""

# 2. Disable sleep mode
echo ""
echo "2️⃣  Vypínám sleep mode..."
echo "$PASS" | sudo -S pmset -a disablesleep 1 >/dev/null
echo "   ✅ Sleep vypnutý"

# 3. Wake-on-LAN
echo ""
echo "3️⃣  Povoluju Wake-on-LAN..."
echo "$PASS" | sudo -S pmset -a womp 1 >/dev/null
echo "   ✅ WoL aktivní"

# 4. SSH key (bez sudo)
echo ""
echo "4️⃣  Generuji SSH klíč..."
if [ ! -f ~/.ssh/id_ed25519 ]; then
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "lisa@$(hostname)" >/dev/null 2>&1
    echo "   ✅ SSH klíč vytvořen"
else
    echo "   ℹ️  SSH klíč už existuje"
fi

# 5. Enable SSH
echo ""
echo "5️⃣  Povoluju SSH server..."
echo "$PASS" | sudo -S launchctl load -w /System/Library/LaunchDaemons/ssh.plist 2>/dev/null || echo "   ℹ️  SSH už běží"
echo "   ✅ SSH server aktivní"

# 6. Info
echo ""
echo "=================================="
echo "✅ SETUP HOTOV"
echo "=================================="
echo ""
echo "📋 Status:"
echo "  • LaunchAgent: AKTIVNÍ (restart = 5s)"
echo "  • Sleep: VYPNUTÝ"
echo "  • Wake-on-LAN: AKTIVNÍ"
echo "  • SSH: AKTIVNÍ"
echo ""
echo "🌐 Pro remote přístup:"
IP=$(ipconfig getifaddr en0)
echo "  SSH: ssh $(whoami)@$IP"
echo "  nebo: ssh $(whoami)@$(hostname -s).local"
echo ""
echo "📤 Public key pro Moulu:"
echo "---"
cat ~/.ssh/id_ed25519.pub
echo "---"
