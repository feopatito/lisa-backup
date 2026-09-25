# 🔧 OpenClaw Skills Installation — Lisa Setup

Generated: 2026-08-16  
Target: Text Factory Editorial Workflow (Phase 1)

---

## Pre-Installation Checklist

- [ ] Lisa workspace is set up (`~/.openclaw/workspace/skills/`)
- [ ] OpenClaw `gateway` is running
- [ ] ClawHub access available (for skill registry)
- [ ] Service account credentials ready for GA4
- [ ] WordPress REST API tokens ready (at least androidmagazine.eu)
- [ ] Tom/Roman approved Phase 1 scope

---

## Phase 1: MVP Installation (Week 1)

### Step 1: Verify existing skills (LOCAL)

```bash
# Check what's already installed locally
ls -la ~/.openclaw/workspace/skills/ | grep -E "^d" | wc -l
# Should show ~84+ directories

# Quick test — skills should load without error
openclaw skills check --verbose
```

### Step 2: Verify GA4 Credentials

Lisa already has offline CSVs. For live API:

```bash
# Create/verify .env in workspace root
cat > ~/.openclaw/workspace/.env << EOF
GA4_PROPERTY_ID=361709661
GA4_CLIENT_EMAIL=your-service-account@project.iam.gserviceaccount.com
GA4_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
SEARCH_CONSOLE_SITE_URL=https://androidmagazine.eu
GA4_DEFAULT_DATE_RANGE=30d
EOF

# Test GA4 connection
cd ~/.openclaw/workspace/skills/ga4-analytics/scripts
npm install
npx tsx src/index.ts
# Should print usage or test data
```

### Step 3: Verify WordPress Credentials

**Current:** androidmagazine.eu only  
**TODO:** Add credentials for jablickar.cz, samsungmagazine.eu, vytukej.cz, letemsvetemapplem.eu

```bash
# Create WordPress tokens file
cat > ~/.openclaw/workspace/.env.wordpress << EOF
# androidmagazine.eu (READY)
WP_BASE_URL_ANDROID=https://androidmagazine.eu
WP_BASIC_TOKEN_ANDROID=base64(user:app_password)

# TODO: Add when credentials ready
# WP_BASE_URL_JABLICKAR=https://jablickar.cz
# WP_BASIC_TOKEN_JABLICKAR=base64(user:app_password)
# ... etc
EOF

# Test WordPress connection
cd ~/.openclaw/workspace/skills/wordpress
npm install
node scripts/wp-cli.js posts:list \
  --query per_page=5
# Should list recent posts from androidmagazine.eu
```

### Step 4: Verify GSC (ClawLink OAuth)

```bash
# ClawLink is managed OAuth — user flow required
# Once connected via dashboard, verify:

# Test GSC connection (requires ClawLink plugin)
openclaw plugins list | grep -i clawlink
# Should show clawlink-plugin in list

# If missing, install:
openclaw plugins install clawhub:clawlink-plugin
openclaw config set tools.alsoAllow '["clawlink-plugin"]' --strict-json
openclaw gateway restart
```

### Step 5: Verify Fact-Checker (Tavily)

```bash
# Fact-checker uses Tavily API
# Verify credentials in env:

echo "TAVILY_API_KEY should be set"
# If missing:
cat >> ~/.openclaw/workspace/.env << EOF
TAVILY_API_KEY=your_tavily_key_here
EOF

# Test Tavily (fact-checker will test on first use)
# No separate command needed — skill auto-tests
```

### Step 6: Verify AI Model Access

```bash
# Check which model Lisa uses
openclaw config get models.default
# Should show: anthropic/claude-haiku-4-5 (or higher tier)

# If using local Ollama:
ollama list | grep -i "neural\|mistral\|llama"
# Should show installed models

# Test inference
openclaw config get models.allowed | head
# Should list available models
```

---

## Phase 1 Skills — Load into Workspace

All Phase 1 skills are already in `~/.openclaw/workspace/skills/`. No install needed, just verify they work.

### Quick Load Test (Run in OpenClaw Chat)

```bash
# Test each skill with minimal prompt

/skill seo-content
"Analyze E-E-A-T of https://example.com"

/skill content-research-and-sourcing
"Verify fact: 'The iPhone 15 battery lasts 24 hours' for an article"

/skill ga4-analytics
"Show me site overview for last 30 days"

/skill google-search-console-seo
"List my verified sites"

/skill wordpress
"Show me last 5 posts from androidmagazine.eu"

/skill ai-writing-agent
"Write a blog post about iPhone 15 battery life"

/skill fact-checker
"Check: 'Apple sold 200M iPhones in 2023'"

/skill content-extraction
"Extract content from https://appleinsider.com"

/skill crawl4ai-skill
"Search for 'iPhone 15 battery life'"

/skill brand-voice
"What is the brand voice for Text Factory?"

/skill editorial-content-strategy
"What audience are we writing for?"
```

---

## Phase 2 Skills — (Week 2-3)

### These are already installed, just ensure credentials:

```bash
# Keyword analyzer — uses local models or free APIs
cd ~/.openclaw/workspace/skills/seo-keyword-analyzer
# No external credentials needed

# News monitor (buzz) — RSS based, free
cd ~/.openclaw/workspace/skills/news-monitor
# Verify RSS feeds in config (if any)

# Trend spotter — Google Trends, free
cd ~/.openclaw/workspace/skills/rend-spotter
# No credentials needed

# RSS digest — local, no credentials
cd ~/.openclaw/workspace/skills/rss-feed-digest
npm install
# Works out of box

# Marketing analytics — uses GA4 credentials (already set)
cd ~/.openclaw/workspace/skills/marketing-analytics
# Reuses GA4 env from Phase 1

# Technical SEO checker — free
cd ~/.openclaw/workspace/skills/technical-seo-checker
# No external API needed

# Schema markup — local, no credentials
cd ~/.openclaw/workspace/skills/schema-markup
# Works out of box

# Web perf — uses Google PageSpeed Insights (free)
cd ~/.openclaw/workspace/skills/web-perf
# Public API, no key needed

# Competitive intel — uses public web sources
cd ~/.openclaw/workspace/skills/competitive-intel-agent
# Uses crawl4ai + web_search (free)
```

---

## Orchestration Setup (Lisa's Daily Workflow)

### Create daily schedule script

```bash
# Create workflow orchestrator
mkdir -p ~/.openclaw/workspace/workflows
cat > ~/.openclaw/workspace/workflows/daily_editorial.sh << 'EOF'
#!/bin/bash
# Daily Editorial Workflow for Lisa
# Run: 7 AM every day (via cron)

DATE=$(date +%Y-%m-%d)
LOG="~/.openclaw/workspace/logs/daily_editorial_${DATE}.log"

echo "=== Daily Editorial Workflow ===" >> $LOG
echo "Time: $(date)" >> $LOG

# 1. Fetch GA4 data
echo "1. Fetching GA4 + GSC data..." >> $LOG
cd ~/.openclaw/workspace/skills/ga4-analytics/scripts
npx tsx src/index.ts >> $LOG 2>&1

# 2. Keyword opportunities
echo "2. Generating keyword opportunities..." >> $LOG
# (This would call seo-keyword-analyzer — requires LangGraph wrapper)

# 3. Competitive check
echo "3. Checking competitor updates..." >> $LOG
# (Requires crawl4ai monitoring — Phase 2 custom)

# 4. Generate editorial plan
echo "4. Editorial plan ready for Lisa review" >> $LOG
echo "Check: ~/.openclaw/workspace/reports/editorial_plan_${DATE}.md" >> $LOG

# 5. Alert Lisa
echo "✅ Daily workflow complete" >> $LOG
# TODO: Send Discord alert to Lisa

EOF

chmod +x ~/.openclaw/workspace/workflows/daily_editorial.sh

# Test run
bash ~/.openclaw/workspace/workflows/daily_editorial.sh
```

### Schedule via cron (Mac/Linux)

```bash
# Edit crontab
crontab -e

# Add line:
0 7 * * * bash ~/.openclaw/workspace/workflows/daily_editorial.sh

# Verify
crontab -l
```

---

## Approval Workflow Setup

Create decision tree for Lisa → Roman approval:

```bash
mkdir -p ~/.openclaw/workspace/approvals
cat > ~/.openclaw/workspace/approvals/publish_workflow.md << 'EOF'
# Publishing Workflow for Text Factory

## When Lisa drafts article:

1. **Lisa writes** (AI-generated or human)
2. **Fact-check** → skill runs tavily-factcheck
3. **E-E-A-T audit** → skill runs seo-content
4. **Draft ready** → Lisa marks as ready in WordPress (status=draft)
5. **Notify Roman** → Slack/Discord message with:
   - Link to draft
   - Fact-check results
   - E-E-A-T score
   - Suggested publish time
   - Competitive context
6. **Roman approves** → Manually (reply "Approve")
7. **Publish** → Lisa or automation moves to status=publish

## Escalations:

- Fact-check FAILS → Roman must review before publish
- E-E-A-T score < 60 → Human must rewrite
- Competitive conflict → Roman decides
EOF

cat ~/.openclaw/workspace/approvals/publish_workflow.md
```

---

## Testing Checklist

### Pre-Launch Validation (Test on androidmagazine.eu)

```bash
# 1. Write a test article (AI)
echo "Test article for approval workflow" > /tmp/test_article.md

# 2. Run fact-check
# (Test with a few real claims)

# 3. Run E-E-A-T audit
# (Should pass for test article)

# 4. Publish to draft
npm run wp -- posts:create '@test_article.md' \
  --query status=draft

# 5. Verify in WordPress
# (Should appear as draft)

# 6. Check analytics
# (Should show updated metrics after publish)

# 7. Run technical audit
# (Should pass Core Web Vitals)
```

---

## Monitoring & Logging

```bash
# Create log structure
mkdir -p ~/.openclaw/workspace/logs
mkdir -p ~/.openclaw/workspace/reports/{daily,weekly,monthly}

# Sample log for each skill run
# Auto-saved by each skill to: 
# ~/.openclaw/workspace/logs/skill_[name]_[timestamp].log

# View recent runs
tail -f ~/.openclaw/workspace/logs/*.log
```

---

## Health Checks (Weekly)

```bash
# Create health check script
cat > ~/.openclaw/workspace/workflows/health_check.sh << 'EOF'
#!/bin/bash

echo "=== Skills Health Check ==="

# Check credentials
echo "✓ GA4 credentials..." && [[ ! -z "$GA4_PROPERTY_ID" ]] && echo "OK" || echo "FAIL"
echo "✓ WordPress token..." && [[ ! -z "$WP_BASIC_TOKEN_ANDROID" ]] && echo "OK" || echo "FAIL"
echo "✓ Tavily API key..." && [[ ! -z "$TAVILY_API_KEY" ]] && echo "OK" || echo "FAIL"

# Test each skill
echo "Testing skills..."
openclaw skills check --verbose

# Report any failures
echo "Complete!"
EOF

chmod +x ~/.openclaw/workspace/workflows/health_check.sh
bash ~/.openclaw/workspace/workflows/health_check.sh
```

---

## Next Steps

1. **Week 1 kickoff:** Run Phase 1 setup
2. **Day 1-2:** Verify GA4, WordPress, credentials
3. **Day 3:** Test each Phase 1 skill in sandbox
4. **Day 4:** Train Lisa on workflows + documentation
5. **Day 5:** Go live on androidmagazine.eu
6. **Week 2:** Expand to other 4 sites + Phase 2 skills
7. **Week 3:** Plan custom orchestration development

---

## Troubleshooting

### "Skill not found" error

```bash
# Verify skill directory exists
ls ~/.openclaw/workspace/skills/seo-content/SKILL.md

# If missing, clone from clawhub:
openclaw skills install clawhub:seo-content
```

### "Credentials missing" error

```bash
# Check env vars are loaded
printenv | grep -i "GA4_\|WP_\|TAVILY"

# If missing, source .env:
source ~/.openclaw/workspace/.env
```

### "WordPress token invalid" error

```bash
# Regenerate WordPress app password via:
# 1. WordPress Admin → Users → Your User → Edit
# 2. Scroll to "Application Passwords"
# 3. Create new password
# 4. Update WP_BASIC_TOKEN in .env
```

### "Rate limit exceeded"

```bash
# Crawl4ai is hitting DuckDuckGo limits
# Solution: Add delays between requests
# crawl4ai-skill has --delay parameter, use it

crawl4ai-skill search "keyword" --delay 5
```

---

## Credentials Checklist (SECURE)

> ⚠️ **Never commit credentials to git**

```bash
# Create .env.local (ignored by git)
cat > ~/.openclaw/workspace/.env.local << 'EOF'
# GA4 service account (JSON key)
GA4_PROPERTY_ID=361709661
GA4_CLIENT_EMAIL=service-account@project.iam.gserviceaccount.com
GA4_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"

# WordPress
WP_BASE_URL_ANDROID=https://androidmagazine.eu
WP_BASIC_TOKEN_ANDROID=base64_encoded_user:password

# Tavily (fact-checker)
TAVILY_API_KEY=tvly-...

# Verify loaded
source ~/.openclaw/workspace/.env.local
echo $GA4_PROPERTY_ID
EOF

# Add to .gitignore
echo ".env.local" >> ~/.openclaw/workspace/.gitignore
```

---

**Installation complete. Ready for Phase 1 kickoff!**
