#!/bin/bash
set -e

echo "🚀 Setup: Lisa běží 24/7 + SSH remote control"
echo ""

# 1. LaunchAgent pro automatický restart
echo "1️⃣  Vytváří LaunchAgent (automatický start po restartu)..."
mkdir -p ~/Library/LaunchAgents

cat > ~/Library/LaunchAgents/ai.openclaw.continuous.plist << 'PLISTEOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>ai.openclaw.continuous</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/openclaw</string>
        <string>gateway</string>
        <string>run</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <dict>
        <key>SuccessfulExit</key>
        <false/>
    </dict>
    <key>StandardOutPath</key>
    <string>/var/log/openclaw-gateway-out.log</string>
    <key>StandardErrorPath</key>
    <string>/var/log/openclaw-gateway-err.log</string>
    <key>RestartDelay</key>
    <integer>5</integer>
</dict>
</plist>
PLISTEOF

# Load it
launchctl unload ~/Library/LaunchAgents/ai.openclaw.continuous.plist 2>/dev/null || true
launchctl load ~/Library/LaunchAgents/ai.openclaw.continuous.plist
echo "   ✅ Načteno"

# 2. Disable sleep mode
echo ""
echo "2️⃣  Vypínám sleep mode (MacBook nebude spát)..."
sudo pmset -a disablesleep 1
echo "   ✅ Sleep vypnutý"

# 3. Wake-on-LAN
echo ""
echo "3️⃣  Povoluju Wake-on-LAN..."
sudo pmset -a womp 1
echo "   ✅ WoL aktivní"

# 4. SSH key pro remote access
echo ""
echo "4️⃣  Generuji SSH klíč pro remote management..."
if [ ! -f ~/.ssh/id_ed25519 ]; then
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "lisa@$(hostname)" >/dev/null 2>&1
    echo "   ✅ SSH klíč vytvořen"
else
    echo "   ℹ️  SSH klíč už existuje"
fi

# 5. Enable SSH na Macu
echo ""
echo "5️⃣  Povoluju SSH server..."
sudo systemsetup -setremotelogin on >/dev/null 2>&1 || sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist 2>/dev/null || true
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
echo "  SSH: ssh -i ~/.ssh/id_ed25519 $(whoami)@$IP"
echo "  nebo: ssh $(whoami)@$(hostname -s).local"
echo ""
echo "📤 Public key pro Moulu:"
echo "---"
cat ~/.ssh/id_ed25519.pub
echo "---"
echo ""
echo "📝 Logy: /var/log/openclaw-gateway-*.log"
