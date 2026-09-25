# ✅ Lisa Skills Implementation Checklist

**Owner:** Tom Repa + Roman Zavřel  
**Timeline:** Week 1-4 (MVP → Scale → Advanced)  
**Updated:** 2026-08-16

---

## PRE-LAUNCH CHECKLIST (This Week)

### Access & Permissions
- [ ] Lisa has access to ~/.openclaw/workspace/skills/ (verify)
- [ ] Lisa can read SOUL.md + USER.md + MEMORY.md (baseline)
- [ ] Roman has Discord #text-factory access for approvals
- [ ] Tom has SSH access to workspace for troubleshooting

### Credentials Inventory
- [ ] GA4 property ID: `361709661` ✅ (documented)
- [ ] GA4 service account JSON ready ✅
- [ ] Search Console credentials ready ✅
- [ ] WordPress REST API token for androidmagazine.eu ✅
- [ ] Tavily API key for fact-checker ⏳ (needs verification)
- [ ] ClawLink OAuth setup ready (for GSC) ⏳

### Documentation Review
- [ ] Roman reads: AUDIT_SUMMARY_FOR_ROMAN_TOM.md
- [ ] Tom reads: audit_lisa_skills_2026-08-16.md + INSTALLATION_COMMANDS.md
- [ ] Lisa reads: SKILLS_QUICK_REFERENCE.md + E-E-A-T framework
- [ ] Approval workflow documented (Lisa → Roman → Publish)

### Team Alignment
- [ ] Kickoff meeting: Roman + Tom + Lisa (scope + timeline)
- [ ] Approval workflow agreed (who, how, Discord vs. WP draft)
- [ ] Success metrics defined (time saved, articles/week, cost/article)
- [ ] Escalation path clear (who to contact if skill fails)

---

## PHASE 1: MVP SETUP (Week 1 — Monday to Friday)

### Monday: Core Infrastructure

#### Credentials Setup
- [ ] Create ~/.env with GA4 credentials
  ```bash
  GA4_PROPERTY_ID=361709661
  GA4_CLIENT_EMAIL=...
  GA4_PRIVATE_KEY=...
  ```
- [ ] Test GA4 API connection (skill test)
- [ ] Create ~/.env.wordpress with WP token (androidmagazine.eu)
  ```bash
  WP_BASE_URL_ANDROID=https://androidmagazine.eu
  WP_BASIC_TOKEN_ANDROID=...
  ```
- [ ] Test WordPress API (list posts)

#### Skill Verification
- [ ] ga4-analytics loads without error
- [ ] google-search-console-seo loads without error
- [ ] wordpress loads without error

**Success Criteria:** Lisa can read GA4 data + WordPress from command line

---

### Tuesday: Quality Gate

#### Fact-Checking Setup
- [ ] Tavily API key available (check with Tom)
- [ ] fact-checker skill loads
- [ ] Test fact-check on sample claim:
  ```
  Claim: "iPhone 15 has 48MP main camera"
  Expected: ✅ VERIFIED (true)
  ```
- [ ] Test fact-check on false claim:
  ```
  Claim: "iPhone 15 has 200MP main camera"
  Expected: ❌ FAILED (false)
  ```

#### E-E-A-T Audit Setup
- [ ] seo-content skill loads
- [ ] content-research-and-sourcing skill loads
- [ ] Test E-E-A-T audit on sample article:
  - URL: Any recent androidmagazine.eu post
  - Expected output: E-E-A-T score + recommendations

#### Approval Workflow
- [ ] Define approval process:
  - Draft → Lisa marks ready in WordPress
  - Notification → Discord #text-factory (Lisa mentions Roman)
  - Roman reviews draft URL
  - Roman approves (via reaction or comment)
  - Publish (Lisa or automation)
- [ ] Test workflow on test article

**Success Criteria:** Fact-check + E-E-A-T audit work end-to-end

---

### Wednesday: Content Creation

#### AI Writing Setup
- [ ] ai-writing-agent skill loads
- [ ] Test AI draft generation:
  ```
  Topic: "iPhone 15 battery improvements"
  Expected: 500+ word article draft (Markdown)
  ```
- [ ] Review output for:
  - Clear structure (H2 headings)
  - Relevant claims
  - Natural tone (not robotic)

#### Image Generation Setup
- [ ] ai-image-generation skill loads
- [ ] Test image generation:
  ```
  Prompt: "iPhone 15, professional product photography"
  Expected: 1 image download
  ```
- [ ] Save to ~/workspace/assets/generated/

#### Brand Voice Setup
- [ ] brand-voice skill loads
- [ ] Verify tone profiles:
  - Android magazine tone?
  - iPhone/Apple tone?
  - Tech for beginners tone?
- [ ] Document voice guidelines in MEMORY.md

**Success Criteria:** Lisa can generate draft article + image in <5 minutes

---

### Thursday: Research & Competitive

#### Web Extraction
- [ ] content-extraction skill loads
- [ ] crawl4ai-skill loads
- [ ] Test content extraction:
  ```
  URL: https://appleinsider.com
  Expected: Extracted Markdown + title + author
  ```
- [ ] Test web search:
  ```
  Query: "iPhone 15 battery life reviews"
  Expected: Top 5 results from DuckDuckGo
  ```

#### Competitive Monitoring
- [ ] competitive-intel-agent skill loads
- [ ] Identify competitor websites to monitor:
  - samsungmagazine.eu
  - androidmagazine.eu (yours)
  - tech competitor X?
  - tech competitor Y?
- [ ] Document in workspace/competitors.md

#### Keyword Research
- [ ] seo-keyword-analyzer skill loads
- [ ] Test keyword analysis:
  ```
  Topic: "iPhone battery life"
  Expected: Volume, difficulty, long-tail suggestions
  ```

**Success Criteria:** Lisa can research competitor + keywords in <10 minutes

---

### Friday: Integration & Quality Testing

#### Analytics Integration
- [ ] marketing-analytics skill loads
- [ ] Create sample GA4 + GSC combined report
- [ ] Verify data types (sessions, clicks, impressions, etc.)

#### Technical SEO
- [ ] schema-markup skill loads
- [ ] technical-seo-checker skill loads
- [ ] Run tech audit on androidmagazine.eu:
  - Core Web Vitals status
  - Hreflang setup (if needed)
  - Schema markup coverage

#### End-to-End Test
- [ ] Run complete workflow on test topic:
  1. Lisa picks topic (e.g., "iPhone 15 features")
  2. Keyword research → 3 keywords identified
  3. Competitor check → Samsung Magazine competitor URLs
  4. AI draft generated
  5. Fact-check passed (no red flags)
  6. E-E-A-T score >70
  7. Image generated
  8. Draft published to WordPress
  9. Analytics recorded
- [ ] Document time taken (should be <30 min)

#### Documentation
- [ ] Update MEMORY.md with Phase 1 results
- [ ] Document any failures + solutions
- [ ] List "known issues" for Tom to fix
- [ ] Create daily workflow script

**Success Criteria:** Lisa can go from topic → published article in 30 minutes

---

## PHASE 2: SCALE (Week 2-3)

### Week 2: Keyword + Trend Skills

#### Monday: Keywords
- [ ] seo-keyword-analyzer skill verified in production
- [ ] Create "keyword opportunity" monthly report template
- [ ] Identify 5-10 high-opportunity keywords for each site

#### Tuesday-Wednesday: Trends
- [ ] news-monitor (buzz) skill verified
- [ ] rss-feed-digest skill verified (configure RSS feeds)
- [ ] trend-spotter skill verified (Google Trends integration)
- [ ] Set up daily trend report (7 AM delivery to Lisa)

#### Thursday: Analytics Deep-Dive
- [ ] marketing-analytics dashboard created
  - GA4 traffic chart
  - Top pages
  - GSC top queries
  - WordPress published count
- [ ] Set up automated email to Roman (weekly summary)

#### Friday: Testing
- [ ] Run Phase 2 skills on all 5 sites
- [ ] Measure time reduction vs. manual baseline

### Week 3: Custom Development Kickoff

#### Editorial Orchestration Skill
- [ ] Specification document written (Tom)
- [ ] Architecture diagram created (Tom)
- [ ] Development started (Tom or outsource)
- [ ] Estimated completion: 2-3 weeks

**Deliverable:** By end of Week 4-5

---

## PHASE 3: ADVANCED (Month 2+)

### Custom Skills Development (Parallel)

- [ ] A/B Testing Auto-Tuner
- [ ] Real-time Competitor Monitoring
- [ ] Topic Clustering & Gaps Analyzer

### Integration
- [ ] Deploy orchestration skill
- [ ] Connect to approval workflow
- [ ] Set up automated publishing (with safeguards)
- [ ] Create monitoring dashboard

**Deliverable:** By end of Month 2

---

## ONGOING: MONITORING & HEALTH

### Weekly Health Checks
- [ ] Run health_check.sh script
- [ ] Verify all credentials valid
- [ ] Check API rate limits (Tavily, GA4, etc.)
- [ ] Review error logs
- [ ] Spot-check fact-checking accuracy

### Monthly Reviews
- [ ] ROI report (time saved, cost per article)
- [ ] Accuracy metrics (fact-check false negatives)
- [ ] Skill performance (which skills help most)
- [ ] User feedback (Lisa's comments, Roman's feedback)

### Quarterly Planning
- [ ] Review Phase 3 priorities
- [ ] Plan custom skill updates
- [ ] Assess new skills to install
- [ ] Update documentation

---

## RISK MITIGATION

### Potential Issues & Responses

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Fact-check false negative** | Wrong claim published | Disable auto-publish, require human review |
| **E-E-A-T score wrong** | Low-quality article scores high | Tune thresholds, review scoring logic |
| **API rate limit hit** | Skill fails mid-workflow | Add delays, implement queuing |
| **WordPress API down** | Can't publish | Fallback to manual publishing |
| **GA4 data delayed** | Yesterday's data only | Accept 24-48h delay, document in report |
| **Tavily API key expires** | Fact-checker stops working | Auto-alert when approaching limit |

### Escalation Path
1. **Lisa notices issue** → Document in #text-factory Discord
2. **Roman reviews** → Decide if critical
3. **Tom investigates** → Fix or downgrade to Phase 1
4. **Resume publication** → After fix confirmed

---

## SUCCESS METRICS (Measure at End of Week 1, 3, 4)

### Time Savings
- [ ] Editorial planning: 3h → 20min (measure via time logs)
- [ ] Fact-checking: 2h → 40min per article
- [ ] Keyword research: 2h → 30min
- [ ] Total weekly: 10.5h → <2h

### Content Quality
- [ ] E-E-A-T score: All articles >70
- [ ] Fact-check accuracy: 95%+ claims verified
- [ ] Zero false facts published
- [ ] All articles have proper attribution

### Output Volume
- [ ] Week 1: 8 articles (baseline)
- [ ] Week 2: 12 articles (50% increase)
- [ ] Week 3: 16 articles (100% increase)
- [ ] Target Week 4: 20+ articles (2.5x)

### Cost per Article
- [ ] Human-only: 1,220 CZK (baseline)
- [ ] Phase 1 (AI): 154 CZK (87% reduction)
- [ ] Phase 2 (automated): 154-300 CZK (75-87% reduction)

---

## GO-LIVE SIGNOFF

When all Phase 1 checklist items are ✅:

```
[ ] Tom: "All systems green, ready to publish"
[ ] Roman: "Approval workflow clear, ready to review"
[ ] Lisa: "I understand the workflow and tools, ready to go"

Date launched: _______________
First article published: _______________
```

---

## DOCUMENTATION REFERENCES

- **Audit:** `audit_lisa_skills_2026-08-16.md`
- **Quick ref:** `SKILLS_QUICK_REFERENCE.md`
- **Installation:** `INSTALLATION_COMMANDS.md`
- **Summary:** `AUDIT_SUMMARY_FOR_ROMAN_TOM.md`
- **Inventory:** `COMPLETE_SKILLS_INVENTORY.md`

---

**Next step:** Schedule kickoff meeting (Roman + Tom + Lisa)  
**Target launch:** Week 1 go-live
