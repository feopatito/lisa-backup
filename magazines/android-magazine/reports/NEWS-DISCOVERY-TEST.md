# LISA V6.5 multi-source orchestrator test

- Created at: 2026-08-20T06:38:43Z
- Normalized signals: 2999
- Clusters: 2149
- Qualified clusters: 18
- Final portfolio: 10
- Portfolio capacity: 10
- API calls used: 0
- LLM calls used: 0
- Watchlist persistence: PASS
- Structured Trends store: PASS
- News implementation: PASS
- News propagation: PASS
- Production data unchanged: PASS
- GitHub evidence propagation: PASS
- GitHub raw clusters: 54
- GitHub candidate universe: 41
- GitHub lane-scored: 41
- GitHub rejected: 41
- GitHub qualified: 0
- GitHub final: 0
- News raw signals: 134
- News underlying event clusters: 44
- News candidate universe: 44
- News qualified: 3
- News final: 1

## Source Coverage Audit
- GSC: CHECKED
- GA4: CHECKED
- WordPress: CHECKED
- GitHub: CHECKED
- Google Trends: CHECKED
- Google News / News: CHECKED
- Reddit: NOT IMPLEMENTED
- X: NOT IMPLEMENTED
- YouTube / community: NOT IMPLEMENTED
- AdSense: NOT IMPLEMENTED

## Rejections
- Stale / saturated: 875
- No unique value: 831
- Weak demand/evidence: 425

## Lane counts
- Qualified by lane: {"SEO / SEARCH OPPORTUNITY": 6, "UPDATE / REWRITE": 10, "BREAKING / CURRENT NEWS": 1, "CURRENT DEMAND / TREND": 1}
- Selected by lane: {"BREAKING / CURRENT NEWS": 1, "CURRENT DEMAND / TREND": 1, "SEO / SEARCH OPPORTUNITY": 4, "UPDATE / REWRITE": 4}
- News by lane: {"DISCOVERY / PREDICTIVE": 1, "CURRENT DEMAND / TREND": 16, "BREAKING / CURRENT NEWS": 3}
- News qualified by lane: {"BREAKING / CURRENT NEWS": 1, "SEO / SEARCH OPPORTUNITY": 1, "UPDATE / REWRITE": 1}

## News Discovery Events
- Raw signals: 134
- Event clusters: 44
- Entering candidate universe: 44
- Rejected: 41
- Qualified: 3
- Final portfolio: 1
- Implementation: PASS
- Propagation: PASS
- Production unchanged: PASS

### Top 20 pre-gate events
#### 1. Sideloading on Android: What it is, why it’s risky, and how to do it more safely - Malwarebytes
- first_public_time: 2026-08-19T15:43:22Z
- source: ["Cybernews", "Droid Life", "Forbes", "Malwarebytes", "TechRadar", "The Hacker News", "blog.google", "nokiapoweruser.com"]
- primary_source: blog.google
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 8, "external_independent_publishers": 7, "official_primary_sources": 1, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 8, "age_days": 0}
- proposed_lane: DISCOVERY / PREDICTIVE
- why_it_may_matter: EVENT: Android security coverage is repeating across multiple publishers -> PRODUCT/USER CHANGE: the practical impact is usually sideloading, permissions or risk reduction -> AUDIENCE RELEVANCE: broad Android readership cares when the warning changes behavior or settings -> ANDROIDMAGAZINE OPPORTUNITY: only publish if you can turn the warning into a concrete user-facing guide or decision aid.

#### 2. Survey says this fundamental Play Store change has many readers excited - Android Authority
- first_public_time: 2026-08-11T01:49:52
- source: ["9News", "9to5Google", "Android Authority", "Ars Technica", "Gadget Hacks", "KREM", "androidmagazine.eu", "blog.google"]
- primary_source: blog.google
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 9, "external_independent_publishers": 6, "official_primary_sources": 1, "internal_evidence_sources": 1, "search_demand_sources": 0, "external_source_diversity": 7, "age_days": 9}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Play Store policy or product changes are being amplified by several publishers -> PRODUCT/USER CHANGE: users may notice app discovery, install, or store-navigation differences -> AUDIENCE RELEVANCE: Play Store changes hit almost every Android user, so search demand rises quickly -> ANDROIDMAGAZINE OPPORTUNITY: turn the story into a practical guide to what exactly changed and who should care.

#### 3. HONOR MagicOS 11 выйдет 6 августа вместе с Android 17 – Android Magazine
- first_public_time: 2026-08-13T13:42:04.728Z
- source: ["9to5Google", "Android Authority", "Android Central", "Android Headlines", "Deccan Herald", "Droid Life", "GSMArena.com", "Help Net Security", "PhoneArena", "TechRepublic", "androidmagazine.eu", "cnet.com", "heise online", "nokiapoweruser.com", "properties/361709661", "sc-domain:androidmagazine.eu"]
- primary_source: 9to5Google
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 90, "external_independent_publishers": 13, "official_primary_sources": 0, "internal_evidence_sources": 3, "search_demand_sources": 2, "external_source_diversity": 13, "age_days": 6}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Android 17 is being discussed across rollout, device and feature stories -> PRODUCT/USER CHANGE: users want to know what changes in compatibility, UI and updates -> AUDIENCE RELEVANCE: the audience is already search-heavy and comparison-driven -> ANDROIDMAGAZINE OPPORTUNITY: update the existing Android 17 coverage with a clearer, current-angle consolidation.

#### 4. Google Wallet throws its boring old pass design out the window - Android Headlines
- first_public_time: 2026-08-06T07:00:00Z
- source: ["Android Authority", "Android Headlines", "Android Police", "Mashable", "PR Newswire", "TechCrunch", "ZDNET", "blog.google"]
- primary_source: blog.google
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 8, "external_independent_publishers": 7, "official_primary_sources": 1, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 8, "age_days": 13}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Google Wallet design or pass handling is changing across coverage -> PRODUCT/USER CHANGE: users may see different passes, quicker access or changed payment flows -> AUDIENCE RELEVANCE: wallet changes matter to everyday Android owners and commuters using tap-to-pay -> ANDROIDMAGAZINE OPPORTUNITY: explain the new Wallet behavior and show whether it changes day-to-day use or only the UI.

#### 5. Google Messages RCS is currently broken for some users - MobileSyrup
- first_public_time: 2026-08-19T16:26:00Z
- source: ["9to5Google", "Android Authority", "Android Central", "Android Police", "Droid Life", "MobileSyrup", "PhoneArena"]
- primary_source: 9to5Google
- user_impact: TECHNICAL CHANGE -> INTERNAL TOOLING / MAINTENANCE -> NO CLEAR USER IMPACT
- mainstream_saturation: {"signals": 8, "external_independent_publishers": 7, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 7, "age_days": 0}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Google Messages RCS issues or feature changes are showing up across multiple publishers -> PRODUCT/USER CHANGE: users may lose messaging reliability, RCS availability or pairing behavior -> AUDIENCE RELEVANCE: chat failures are high-frequency pain points and trigger search fast -> ANDROIDMAGAZINE OPPORTUNITY: publish a concrete troubleshooting/update piece that tells readers what broke, what is confirmed and what to try next.

#### 6. An Experimental Switch Back To iPhone - Forbes
- first_public_time: 2026-08-16T20:30:00Z
- source: ["Android Authority", "Engadget", "Forbes", "PCMag", "Thurrott.com", "bgr.com", "nokiapoweruser.com"]
- primary_source: Android Authority
- user_impact: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- mainstream_saturation: {"signals": 7, "external_independent_publishers": 7, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 7, "age_days": 3}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: OnePlus coverage is converging on a future device / feature rumor -> PRODUCT/USER CHANGE: buyers want refresh-rate, launch timing and hardware certainty -> AUDIENCE RELEVANCE: OnePlus readers compare rumors quickly and want the plain-English summary -> ANDROIDMAGAZINE OPPORTUNITY: consolidate the rumor into one buyer-facing explainer with a confirmed-vs-speculative split.

#### 7. https://androidmagazine.eu/fr/2025/10/10/whatsapp-prestal-fungovat-na-hodinkach-s-wear-os-tady-je-navod-jak-to-vyresit/
- first_public_time: 2026-08-13T13:42:04.728Z
- source: ["9to5Google", "Android Authority", "Android Police", "Droid Life", "androidmagazine.eu", "blog.google", "properties/361709661", "sc-domain:androidmagazine.eu"]
- primary_source: blog.google
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 18, "external_independent_publishers": 4, "official_primary_sources": 1, "internal_evidence_sources": 3, "search_demand_sources": 2, "external_source_diversity": 5, "age_days": 6}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Wear OS coverage is mixing app, platform and rollout updates -> PRODUCT/USER CHANGE: watch owners care about feature availability, setup and compatibility -> AUDIENCE RELEVANCE: Wear OS readers typically search for practical how-tos and update implications -> ANDROIDMAGAZINE OPPORTUNITY: refresh the Wear OS hub with the latest user-facing change instead of another generic recap.

#### 8. Pixel 11
- first_public_time: 2026-08-13T13:42:04.728Z
- source: ["9to5Google", "Bloomberg.com", "TechCrunch", "Tom's Guide", "ZDNET", "androidmagazine.eu", "local editorial report cache", "properties/361709661", "sc-domain:androidmagazine.eu"]
- primary_source: 9to5Google
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 80, "external_independent_publishers": 5, "official_primary_sources": 0, "internal_evidence_sources": 4, "search_demand_sources": 3, "external_source_diversity": 5, "age_days": 6}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Pixel 11 coverage is maturing from rumors into repeat reporting and product context -> PRODUCT/USER CHANGE: readers want to know whether the device is imminent, what changes, and whether to wait -> AUDIENCE RELEVANCE: Pixel buyers search hard before launch and after major rumor cycles -> ANDROIDMAGAZINE OPPORTUNITY: keep one living Pixel 11 explainer that merges current signals, buying advice and what is actually confirmed.

#### 9. 58 Xiaomi, Redmi, and Poco Devices Just Got the July 2026 Security Patch - Gizchina.com
- first_public_time: 2026-07-24T07:00:00Z
- source: ["Android Headlines", "GSMArena.com", "Gadget Flow", "Gizchina.com", "Nikkei Asia", "Notebookcheck", "trustedreviews.com"]
- primary_source: Android Headlines
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 7, "external_independent_publishers": 7, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 7, "age_days": 26}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Xiaomi/Redmi/Poco patch and rollout coverage is clustering around a device family update story -> PRODUCT/USER CHANGE: readers may need to know whether their model is updated, supported or affected -> AUDIENCE RELEVANCE: owners search for model lists and update impact, not brand headlines -> ANDROIDMAGAZINE OPPORTUNITY: turn the update into a clear model-by-model practical article.

#### 10. New Pixel Search App is Here for Pixel 11, Galaxy Z Fold 8 - Droid Life
- first_public_time: 2026-08-19T19:55:43Z
- source: ["Ars Technica", "Droid Life", "Forbes", "Mashable", "PhoneArena"]
- primary_source: Ars Technica
- user_impact: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- mainstream_saturation: {"signals": 5, "external_independent_publishers": 5, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 5, "age_days": 0}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Galaxy Z Fold 8 rumor and promo coverage is converging around the same foldable launch cycle -> PRODUCT/USER CHANGE: readers want design, pricing and upgrade timing clarity before buying -> AUDIENCE RELEVANCE: foldable buyers are comparison-heavy and respond fast to rumor consolidation -> ANDROIDMAGAZINE OPPORTUNITY: publish one foldable roundup that separates tease, leak and confirmed detail.

#### 11. This Deal Is Everything: Save $200 on an Unlocked Nothing Phone at Amazon - PCMag
- first_public_time: 2026-08-19T20:05:04Z
- source: ["AndroidGuys", "Good Housekeeping", "PCMag", "PhoneArena", "bgr.com"]
- primary_source: AndroidGuys
- user_impact: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- mainstream_saturation: {"signals": 5, "external_independent_publishers": 5, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 5, "age_days": 0}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Nothing Phone coverage is tied to price, promotion or model chatter -> PRODUCT/USER CHANGE: buyers may see a different deal, price or model naming situation -> AUDIENCE RELEVANCE: Nothing readers are deal-sensitive and compare aggressively -> ANDROIDMAGAZINE OPPORTUNITY: publish a short buyer guide that explains whether the story is about the phone itself or just a sale.

#### 12. Samsung Galaxy Tab S12 Ultra render leaks - GSMArena.com news - GSMArena.com
- first_public_time: 2026-08-18T19:30:59Z
- source: ["Android Headlines", "GSMArena.com", "PhoneArena"]
- primary_source: Android Headlines
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 3, "external_independent_publishers": 3, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 3, "age_days": 1}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Galaxy Tab S12 Ultra coverage is converging across leaks, renders and official material -> PRODUCT/USER CHANGE: readers can separate rumor from official design/timing signals -> AUDIENCE RELEVANCE: Samsung tablet watchers and upgrade buyers are deciding whether to wait or buy -> ANDROIDMAGAZINE OPPORTUNITY: publish one consolidated explainer/update that ties together Android Headlines, GSMArena.com, PhoneArena and keeps the story current.

#### 13. Never mind OnePlus 15: OnePlus 16 could finally get true 165Hz refresh rate - Android Authority
- first_public_time: 2026-08-19T07:54:00Z
- source: ["Android Authority", "Android Headlines", "PhoneArena"]
- primary_source: Android Authority
- user_impact: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- mainstream_saturation: {"signals": 3, "external_independent_publishers": 3, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 3, "age_days": 0}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: OnePlus coverage is converging on a future device / feature rumor -> PRODUCT/USER CHANGE: buyers want refresh-rate, launch timing and hardware certainty -> AUDIENCE RELEVANCE: OnePlus readers compare rumors quickly and want the plain-English summary -> ANDROIDMAGAZINE OPPORTUNITY: consolidate the rumor into one buyer-facing explainer with a confirmed-vs-speculative split.

#### 14. The Nothing Phone (4a) Pro Is a Solid Alternative to the Pixel 10a, and It's on Sale for $449 - Lifehacker
- first_public_time: 2026-08-19T13:00:09Z
- source: ["Android Police", "Lifehacker", "cnet.com"]
- primary_source: Android Police
- user_impact: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- mainstream_saturation: {"signals": 3, "external_independent_publishers": 3, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 3, "age_days": 0}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Nothing Phone coverage is tied to price, promotion or model chatter -> PRODUCT/USER CHANGE: buyers may see a different deal, price or model naming situation -> AUDIENCE RELEVANCE: Nothing readers are deal-sensitive and compare aggressively -> ANDROIDMAGAZINE OPPORTUNITY: publish a short buyer guide that explains whether the story is about the phone itself or just a sale.

#### 15. Pixel Watch 5 unikly i se všemi reklamními materiály, podívejte se na vzhled, funkce i největší novinky – Android Magazine
- first_public_time: 2026-08-13T13:41:53Z
- source: ["androidmagazine.eu", "blog.google", "properties/361709661"]
- primary_source: blog.google
- user_impact: TECHNICAL CHANGE: platform/app behavior or support/docs update -> PRODUCT/SERVICE EFFECT: feature, compatibility, security, or workflow changes in a consumer-facing product -> USER IMPACT: users may notice new behavior, setup steps, or troubleshooting issues.
- mainstream_saturation: {"signals": 11, "external_independent_publishers": 0, "official_primary_sources": 1, "internal_evidence_sources": 2, "search_demand_sources": 1, "external_source_diversity": 1, "age_days": 6}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: Pixel Watch 5 leak/coverage cluster is converging on a single watch release -> PRODUCT/USER CHANGE: buyers want to know whether the new watch changes battery life, features or launch timing -> AUDIENCE RELEVANCE: watch upgrade decisions are tightly time-sensitive and comparison-heavy -> ANDROIDMAGAZINE OPPORTUNITY: consolidate leaks and official crumbs into one buying-oriented explainer.

#### 16. I thought this Motorola app was bloatware — now I can't live without it - Android Authority
- first_public_time: 2026-08-17T11:18:54Z
- source: ["Android Authority", "GSMArena.com", "PhoneArena"]
- primary_source: Android Authority
- user_impact: TECHNICAL CHANGE: platform/app behavior or support/docs update -> PRODUCT/SERVICE EFFECT: feature, compatibility, security, or workflow changes in a consumer-facing product -> USER IMPACT: users may notice new behavior, setup steps, or troubleshooting issues.
- mainstream_saturation: {"signals": 3, "external_independent_publishers": 3, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 3, "age_days": 2}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: a Motorola-related hardware or feature rumor is gaining repeat mention -> PRODUCT/USER CHANGE: readers want to know whether it changes charging, accessories or phone choice -> AUDIENCE RELEVANCE: Motorola buyers and Android accessory shoppers need a clear practical summary -> ANDROIDMAGAZINE OPPORTUNITY: publish a single explainer that resolves the rumor and states what is actually confirmed.

#### 17. I just tried this privacy-focused version of Android for Pixel phones — and I'm very impressed - Tom's Guide
- first_public_time: 2026-08-15T09:00:00Z
- source: ["Android Authority", "Electronic Frontier Foundation", "Tom's Guide"]
- primary_source: Android Authority
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 3, "external_independent_publishers": 3, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 3, "age_days": 4}
- proposed_lane: CURRENT DEMAND / TREND
- why_it_may_matter: EVENT: android privacy has enough external attention to justify monitoring -> PRODUCT/USER CHANGE: the underlying story may alter device behavior, launch timing or feature availability -> AUDIENCE RELEVANCE: Android readers only care if it changes buying, setup or troubleshooting decisions -> ANDROIDMAGAZINE OPPORTUNITY: turn the event into a concrete reader decision rather than a generic news recap.

#### 18. HyperOS 4: Xiaomi Reveals Which Devices Will Receive The Soft Light Glass UI - Ubergizmo
- first_public_time: 2026-08-18T15:00:46Z
- source: ["Nokiamob", "Ubergizmo"]
- primary_source: Nokiamob
- user_impact: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- mainstream_saturation: {"signals": 2, "external_independent_publishers": 2, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 2, "age_days": 1}
- proposed_lane: BREAKING / CURRENT NEWS
- why_it_may_matter: EVENT: HyperOS 4 is being framed as a device rollout story rather than a rumor -> PRODUCT/USER CHANGE: eligible Xiaomi/Redmi/Poco owners need to know if and when they receive the update -> AUDIENCE RELEVANCE: update lists and rollout timing are the part readers actually search for -> ANDROIDMAGAZINE OPPORTUNITY: produce a model list and rollout explainer instead of a generic news recap.

#### 19. Finally, an Android maker besides Google is embracing magnetic charging - How-To Geek
- first_public_time: 2026-08-19T15:59:51Z
- source: ["Android Central", "How-To Geek"]
- primary_source: Android Central
- user_impact: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- mainstream_saturation: {"signals": 2, "external_independent_publishers": 2, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 2, "age_days": 0}
- proposed_lane: BREAKING / CURRENT NEWS
- why_it_may_matter: EVENT: Motorola magnetic charging moved from teaser/leak into repeat coverage -> PRODUCT/USER CHANGE: buyers may see Qi2-style accessory compatibility and a new charging behavior -> AUDIENCE RELEVANCE: Motorola owners and accessory buyers need practical compatibility guidance -> ANDROIDMAGAZINE OPPORTUNITY: explain what changes, which phones/accessories are affected, and whether the feature is real enough to matter.

#### 20. After using the Honor Robot Phone's "basically peerless" gimbal camera, I can't work out if it's the future or not - t3.com
- first_public_time: 2026-08-19T15:00:00Z
- source: ["TechRadar", "t3.com"]
- primary_source: TechRadar
- user_impact: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- mainstream_saturation: {"signals": 2, "external_independent_publishers": 2, "official_primary_sources": 0, "internal_evidence_sources": 0, "search_demand_sources": 0, "external_source_diversity": 2, "age_days": 0}
- proposed_lane: BREAKING / CURRENT NEWS
- why_it_may_matter: EVENT: Honor Robot Phone concept coverage is generating reaction around the camera/industrial design idea -> PRODUCT/USER CHANGE: the question is whether the odd hardware translates into real user value or just spectacle -> AUDIENCE RELEVANCE: readers want to know if this is future hardware or pure tease -> ANDROIDMAGAZINE OPPORTUNITY: frame it as a practical assessment of whether the concept changes the buying picture.

## TOP 10 diversified candidates
### 1. pixel 11
- repository: gsc
- primary_lane: BREAKING / CURRENT NEWS
- lane_score: 65.0
- lane_scores: {"BREAKING / CURRENT NEWS": 65.0, "DISCOVERY / PREDICTIVE": 44.9, "CURRENT DEMAND / TREND": 73.5, "SEO / SEARCH OPPORTUNITY": 77.3, "UPDATE / REWRITE": 93.3}
- representative_signal: {"signal_id": "1d269a384f4f2f1e4fa5bfe47dd4059cd37acc80fd40b69c2204bbc16351e615", "source_family": "trends", "source": "local editorial report cache", "signal_type": "trend", "entity": "pixel 11", "topic": "pixel 11", "title": "Pixel 11", "url": "", "published_at": "2026-08-18T04:49:34Z", "first_seen_at": "2026-08-18T04:49:34Z", "latest_activity": "2026-08-18T04:49:34Z", "evidence": "Structured Google Trends cache", "confidence": "HIGH", "user_impact": "trend momentum / breakout proxy", "raw_source_reference": "b09dab1e483a8d499d72241cd3ed08aca1bb65e0bcc0fdf742a55e14c26ab1b2", "processing_status": "normalized", "metadata": {"query": "Pixel 11", "geo": "UNAVAILABLE", "trend_value": 69.0, "previous_value": 100.0, "velocity": -31.0, "acceleration": -103.0, "peak": 100.0, "periods": ["Aug 2 – 8, 2026", "Aug 9 – 15, 2026", "Aug 16 – 22, 2026"], "values": [28, 100, 69], "fetched_at": "2026-08-18T04:49:34Z"}}
- supporting_events_count: 80
- first_seen: 2026-07-13T13:55:07
- source_record_first_seen_at: 2026-07-13T13:55:07
- story_first_seen_at: 2026-07-13T13:55:07
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-19T17:45:00Z
- editorial_potential: HIGH
- why_it_may_matter: EVENT: Pixel 11 coverage is maturing from rumors into repeat reporting and product context -> PRODUCT/USER CHANGE: readers want to know whether the device is imminent, what changes, and whether to wait -> AUDIENCE RELEVANCE: Pixel buyers search hard before launch and after major rumor cycles -> ANDROIDMAGAZINE OPPORTUNITY: keep one living Pixel 11 explainer that merges current signals, buying advice and what is actually confirmed.
- user_impact_reason: NEWS SIGNAL -> PRODUCT / SERVICE CHANGE -> USER IMPACT: a news-covered Android ecosystem event may affect access, behavior, availability, or troubleshooting.
- user_impact_confidence: MEDIUM
- editorial_opportunity: Why pixel 11 is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
- opportunity_score: 97.3
- predictive_score: 64.2
- signal_score: 60.3
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/3-nejzajimavejsi-druhy-prislusenstvi-pro-nove-telefony-pixel-11-hraji-vsemi-barvami-a-podporuji-qi2-nabijeni/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "78478", "title": "3 nejzajímavější druhy příslušenství pro nové telefony Pixel 11: hrají všemi barvami a podporují Qi2 nabíjení", "slug": "3-nejzajimavejsi-druhy-prislusenstvi-pro-nove-telefony-pixel-11-hraji-vsemi-barvami-a-podporuji-qi2-nabijeni", "status": "publish", "date": "2026-08-13T16:40:37", "url": "https://androidmagazine.eu/3-nejzajimavejsi-druhy-prislusenstvi-pro-nove-telefony-pixel-11-hraji-vsemi-barvami-a-podporuji-qi2-nabijeni/"}, {"id": "78458", "title": "Galaxy Z Fold8 dostal tvrdého soupeře, Pixel 11 Pro Fold je tenký, neuvěřitelně odolný a s vylepšeným displejem", "slug": "galaxy-z-fold8-dostal-tvrdeho-soupere-pixel-11-pro-fold-je-tenky-neuveritelne-odolny-a-s-vylepsenym-displejem", "status": "publish", "date": "2026-08-13T11:55:26", "url": "https://androidmagazine.eu/galaxy-z-fold8-dostal-tvrdeho-soupere-pixel-11-pro-fold-je-tenky-neuveritelne-odolny-a-s-vylepsenym-displejem/"}, {"id": "78450", "title": "Google konečně překonal svou největší slabinu, Pixel 11 má nový režim pro extrémně rychlé nabíjení", "slug": "google-konecne-prekonal-svou-nejvetsi-slabinu-pixel-11-ma-novy-rezim-pro-extremne-rychle-nabijeni", "status": "publish", "date": "2026-08-13T09:16:57", "url": "https://androidmagazine.eu/google-konecne-prekonal-svou-nejvetsi-slabinu-pixel-11-ma-novy-rezim-pro-extremne-rychle-nabijeni/"}, {"id": "78431", "title": "12 zásadních novinek z Made by Google, které mění Pixely i celý Google ekosystém", "slug": "pixel-11-je-venku-a-prinasi-12-zasadnich-novinek-ktere-meni-pixely-i-cely-google-ekosystem", "status": "publish", "date": "2026-08-13T08:16:02", "url": "https://androidmagazine.eu/pixel-11-je-venku-a-prinasi-12-zasadnich-novinek-ktere-meni-pixely-i-cely-google-ekosystem/"}, {"id": "78340", "title": "Pixel 11 přichází. Tohle je 9 novinek, které Google ukáže už 12. srpna", "slug": "pixel-11-prichazi-tohle-je-9-novinek-ktere-google-ukaze-uz-12-srpna", "status": "publish", "date": "2026-08-11T19:20:20", "url": "https://androidmagazine.eu/pixel-11-prichazi-tohle-je-9-novinek-ktere-google-ukaze-uz-12-srpna/"}]}

### 2. redmi k100 pro max
- repository: ga4
- primary_lane: CURRENT DEMAND / TREND
- lane_score: 59.0
- lane_scores: {"BREAKING / CURRENT NEWS": 50.1, "DISCOVERY / PREDICTIVE": 37.8, "CURRENT DEMAND / TREND": 59.0, "SEO / SEARCH OPPORTUNITY": 13.0, "UPDATE / REWRITE": 29.0}
- representative_signal: {"signal_id": "3ebfbd0b9cc3bc09eec23d528671d700c0adb0f44c55246135825341ca73981f", "source_family": "trends", "source": "local editorial report cache", "signal_type": "trend", "entity": "redmi k100 pro max", "topic": "redmi k100 pro max", "title": "Redmi K100 Pro Max", "url": "", "published_at": "2026-08-18T04:49:34Z", "first_seen_at": "2026-08-18T04:49:34Z", "latest_activity": "2026-08-18T04:49:34Z", "evidence": "Structured Google Trends cache", "confidence": "HIGH", "user_impact": "trend momentum / breakout proxy", "raw_source_reference": "15144483211626a48e1254da25d86f369b097fafdc22420ad1c5faccd41fd0b2", "processing_status": "normalized", "metadata": {"query": "Redmi K100 Pro Max", "geo": "UNAVAILABLE", "trend_value": 50.0, "previous_value": 89.0, "velocity": -39.0, "acceleration": -100.0, "peak": 89.0, "periods": ["Aug 2 – 8, 2026", "Aug 9 – 15, 2026", "Aug 16 – 22, 2026"], "values": [28, 89, 50], "fetched_at": "2026-08-18T04:49:34Z"}}
- supporting_events_count: 6
- first_seen: 2026-08-04T01:17:24
- source_record_first_seen_at: 2026-08-04T01:17:24
- story_first_seen_at: 2026-08-04T01:17:24
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-18T04:49:34Z
- editorial_potential: HIGH
- why_it_may_matter: Structured Google Trends cache
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: Why redmi k100 pro max is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
- opportunity_score: 37.3
- predictive_score: 26.8
- signal_score: 33.5
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/redmi-k100-pro-max-je-konecne-tady-sokuje-baterii-9-070-mah-a-200mpx-fotoaparatem/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "78393", "title": "Redmi K100 Pro Max je konečně tady, šokuje baterií 9 070 mAh a 200Mpx fotoaparátem. A naznačuje, co nabídne Poco", "slug": "redmi-k100-pro-max-je-konecne-tady-sokuje-baterii-9-070-mah-a-200mpx-fotoaparatem", "status": "publish", "date": "2026-08-12T13:50:04", "url": "https://androidmagazine.eu/redmi-k100-pro-max-je-konecne-tady-sokuje-baterii-9-070-mah-a-200mpx-fotoaparatem/"}, {"id": "78323", "title": "Vše, co potřebujete vědět o Redmi K100 Pro Max alias Poco F9 Ultra: obří baterie, 185Hz displej a 200Mpx fotoaparát", "slug": "vse-co-potrebujete-vedet-o-redmi-k100-pro-max-alias-poco-f9-ultra-obri-baterie-185hz-displej-a-200mpx-fotoaparat", "status": "publish", "date": "2026-08-10T19:20:22", "url": "https://androidmagazine.eu/vse-co-potrebujete-vedet-o-redmi-k100-pro-max-alias-poco-f9-ultra-obri-baterie-185hz-displej-a-200mpx-fotoaparat/"}, {"id": "78227", "title": "Redmi K100 Pro Max šokuje obří baterií, extrémním nabíjením a pokročilou výbavou pro hráče", "slug": "redmi-k100-pro-max-sokuje-obri-baterii-extremnim-nabijenim-a-pokrocilou-vybavou-pro-hrace", "status": "publish", "date": "2026-08-07T01:42:21", "url": "https://androidmagazine.eu/redmi-k100-pro-max-sokuje-obri-baterii-extremnim-nabijenim-a-pokrocilou-vybavou-pro-hrace/"}, {"id": "78025", "title": "Redmi K100 Pro Max odhaluje svou sílu: obří baterie a Snapdragon nové generace míří na trh", "slug": "redmi-k100-pro-max-odhaluje-svou-silu-obri-baterie-a-snapdragon-nove-generace-miri-na-trh", "status": "publish", "date": "2026-08-04T01:17:24", "url": "https://androidmagazine.eu/redmi-k100-pro-max-odhaluje-svou-silu-obri-baterie-a-snapdragon-nove-generace-miri-na-trh/"}, {"id": "69248", "title": "Redmi K100 a Redmi K100 Pro Max plánují rozdrtit ostatní vlajkové mobily, přijdou jako POCO F9 Pro/Ultra", "slug": "redmi-k100-a-redmi-k100-pro-max-planuji-rozdrtit-ostatni-vlajkove-mobily-prijdou-jako-poco-f9-pro-ultra", "status": "publish", "date": "2026-01-19T17:00:18", "url": "https://androidmagazine.eu/redmi-k100-a-redmi-k100-pro-max-planuji-rozdrtit-ostatni-vlajkove-mobily-prijdou-jako-poco-f9-pro-ultra/"}]}

### 3. jak vypnout ai funkce na
- repository: gsc
- primary_lane: SEO / SEARCH OPPORTUNITY
- lane_score: 84.1
- lane_scores: {"BREAKING / CURRENT NEWS": 23.4, "DISCOVERY / PREDICTIVE": 25.0, "CURRENT DEMAND / TREND": 20.6, "SEO / SEARCH OPPORTUNITY": 84.1, "UPDATE / REWRITE": 100.0}
- representative_signal: {"signal_id": "d8c9c31ac2e46b99ef61c855181c8e7f43126948b4aecd0b0ab36ba654e78f9c", "source_family": "gsc", "source": "sc-domain:androidmagazine.eu", "signal_type": "page", "entity": "https://androidmagazine.eu/hu/2025/10/26/jak-vypnout-ai-funkce-na-mobilu-s-androidem-je-to-slozite-ale-jde-to/", "topic": "jak vypnout ai funkce na", "title": "https://androidmagazine.eu/hu/2025/10/26/jak-vypnout-ai-funkce-na-mobilu-s-androidem-je-to-slozite-ale-jde-to/", "url": "https://androidmagazine.eu/hu/2025/10/26/jak-vypnout-ai-funkce-na-mobilu-s-androidem-je-to-slozite-ale-jde-to/", "published_at": null, "first_seen_at": "2026-08-13T13:42:04.728Z", "latest_activity": "2026-08-13T13:42:04.728Z", "evidence": "GSC page", "confidence": "HIGH", "user_impact": "landing-page search performance", "raw_source_reference": "2059782ba858c19135814d1216db1382c3b0748124441ba62e6c48f530816923", "processing_status": "normalized", "metadata": {"clicks": 64, "impressions": 2422, "ctr": 0.0264, "position": 7.8}}
- supporting_events_count: 21
- first_seen: 2025-10-26T14:00:02
- source_record_first_seen_at: 2025-10-26T14:00:02
- story_first_seen_at: 2025-10-26T14:00:02
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-13T13:42:04.728Z
- editorial_potential: HIGH
- why_it_may_matter: WordPress publish
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: How to improve the existing jak vypnout ai funkce na page for current search intent, CTR, and conversion to a better editorial angle.
- opportunity_score: 76.2
- predictive_score: 44.8
- signal_score: 50.4
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/jak-vypnout-ai-funkce-na-mobilu-s-androidem-je-to-slozite-ale-jde-to/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "64884", "title": "Jak vypnout AI funkce na mobilu s Androidem? Je to složité, ale jde to", "slug": "jak-vypnout-ai-funkce-na-mobilu-s-androidem-je-to-slozite-ale-jde-to", "status": "publish", "date": "2025-10-26T14:00:02", "url": "https://androidmagazine.eu/jak-vypnout-ai-funkce-na-mobilu-s-androidem-je-to-slozite-ale-jde-to/"}]}

### 4. poco f9 ultra
- repository: gsc
- primary_lane: SEO / SEARCH OPPORTUNITY
- lane_score: 83.4
- lane_scores: {"BREAKING / CURRENT NEWS": 23.4, "DISCOVERY / PREDICTIVE": 25.0, "CURRENT DEMAND / TREND": 20.6, "SEO / SEARCH OPPORTUNITY": 83.4, "UPDATE / REWRITE": 99.4}
- representative_signal: {"signal_id": "2cc1cabb413f39fcc7b873d43f0e5924f656eb95221b806ed51a6c1bc3109d48", "source_family": "gsc", "source": "sc-domain:androidmagazine.eu", "signal_type": "query_page", "entity": "poco f9", "topic": "poco f9 ultra", "title": "poco f9", "url": "https://androidmagazine.eu/fr/2026/02/10/poco-f9-pro-a-poco-f9-ultra-maji-dostat-paradni-200mpx-teleobjektiv/", "published_at": null, "first_seen_at": "2026-08-13T13:42:04.728Z", "latest_activity": "2026-08-13T13:42:04.728Z", "evidence": "GSC query+page", "confidence": "HIGH", "user_impact": "user-facing search demand / query intent", "raw_source_reference": "baf0f4425007eeed10322a34b0fe3a050fb58393aa53f68fe24a656865402035", "processing_status": "normalized", "metadata": {"clicks": 27, "impressions": 557, "ctr": 0.048499999999999995, "position": 8.0}}
- supporting_events_count: 44
- first_seen: 2026-07-23T13:39:10
- source_record_first_seen_at: 2026-07-23T13:39:10
- story_first_seen_at: 2026-07-23T13:39:10
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-13T13:42:04.728Z
- editorial_potential: HIGH
- why_it_may_matter: WordPress publish
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: How to improve the existing poco f9 ultra page for current search intent, CTR, and conversion to a better editorial angle.
- opportunity_score: 75.8
- predictive_score: 44.5
- signal_score: 50.4
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/poco-f9-ultra-a-f9-pro-odhaluji-sve-trumfy-obri-baterie-a-100w-nabijeni/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "78386", "title": "Poco F9 Ultra a F9 Pro odhalují své trumfy – obří baterie, 100W nabíjení a parádní fotoaparáty", "slug": "poco-f9-ultra-a-f9-pro-odhaluji-sve-trumfy-obri-baterie-a-100w-nabijeni", "status": "publish", "date": "2026-08-12T12:05:05", "url": "https://androidmagazine.eu/poco-f9-ultra-a-f9-pro-odhaluji-sve-trumfy-obri-baterie-a-100w-nabijeni/"}, {"id": "77589", "title": "Poco F9 Ultra a F9 Pro se blíží. Certifikace odhalily globální premiéru i nejlákavější vlastnosti", "slug": "poco-f9-ultra-a-f9-pro-se-blizi-certifikace-odhalily-globalni-premieru-i-nejlakavejsi-vlastnosti", "status": "publish", "date": "2026-07-23T13:39:10", "url": "https://androidmagazine.eu/poco-f9-ultra-a-f9-pro-se-blizi-certifikace-odhalily-globalni-premieru-i-nejlakavejsi-vlastnosti/"}, {"id": "71390", "title": "POCO F9 Ultra odhaluje parametry – 200MPx fotoaparát a 2nm čip vás dostanou do kolen", "slug": "poco-f9-ultra-odhaluje-parametry-ze-kterych-mrazi-200mpx-fotoaparat-a-2nm-cip-vas-dostanou-do-kolen", "status": "publish", "date": "2026-03-04T20:27:01", "url": "https://androidmagazine.eu/poco-f9-ultra-odhaluje-parametry-ze-kterych-mrazi-200mpx-fotoaparat-a-2nm-cip-vas-dostanou-do-kolen/"}, {"id": "70283", "title": "POCO F9 Pro a POCO F9 Ultra mají dostat parádní 200MPx teleobjektiv", "slug": "poco-f9-pro-a-poco-f9-ultra-maji-dostat-paradni-200mpx-teleobjektiv", "status": "publish", "date": "2026-02-10T10:00:08", "url": "https://androidmagazine.eu/poco-f9-pro-a-poco-f9-ultra-maji-dostat-paradni-200mpx-teleobjektiv/"}]}

### 5. jak zapnout nebo vypnout funkci
- repository: gsc
- primary_lane: UPDATE / REWRITE
- lane_score: 65.4
- lane_scores: {"BREAKING / CURRENT NEWS": 20.1, "DISCOVERY / PREDICTIVE": 21.4, "CURRENT DEMAND / TREND": 17.1, "SEO / SEARCH OPPORTUNITY": 49.4, "UPDATE / REWRITE": 65.4}
- representative_signal: {"signal_id": "1d770795b5266b0e81adee5b79cc1b05d12ba062f8fe962cc3a8398584273b2e", "source_family": "gsc", "source": "sc-domain:androidmagazine.eu", "signal_type": "page", "entity": "https://androidmagazine.eu/ru/2024/05/31/jak-zapnout-nebo-vypnout-funkci-always-on-display-na-zarizenich-android/", "topic": "jak zapnout nebo vypnout funkci", "title": "https://androidmagazine.eu/ru/2024/05/31/jak-zapnout-nebo-vypnout-funkci-always-on-display-na-zarizenich-android/", "url": "https://androidmagazine.eu/ru/2024/05/31/jak-zapnout-nebo-vypnout-funkci-always-on-display-na-zarizenich-android/", "published_at": null, "first_seen_at": "2026-08-13T13:42:04.728Z", "latest_activity": "2026-08-13T13:42:04.728Z", "evidence": "GSC page", "confidence": "HIGH", "user_impact": "landing-page search performance", "raw_source_reference": "5f56baa9ba44b1d7dccb42fce1822eaa480a94a3a9743663200a8ebd6380f343", "processing_status": "normalized", "metadata": {"clicks": 9, "impressions": 1368, "ctr": 0.66, "position": 11.5}}
- supporting_events_count: 3
- first_seen: 2024-05-31T16:30:31
- source_record_first_seen_at: 2024-05-31T16:30:31
- story_first_seen_at: 2024-05-31T16:30:31
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-13T13:42:04.728Z
- editorial_potential: HIGH
- why_it_may_matter: WordPress publish
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: How to improve the existing jak zapnout nebo vypnout funkci page for current search intent, CTR, and conversion to a better editorial angle.
- opportunity_score: 54.0
- predictive_score: 29.8
- signal_score: 35.4
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/jak-zapnout-nebo-vypnout-funkci-always-on-display-na-zarizenich-android/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "56007", "title": "Jak zapnout nebo vypnout funkci Always On Display na zařízeních Android?", "slug": "jak-zapnout-nebo-vypnout-funkci-always-on-display-na-zarizenich-android", "status": "publish", "date": "2024-05-31T16:30:31", "url": "https://androidmagazine.eu/jak-zapnout-nebo-vypnout-funkci-always-on-display-na-zarizenich-android/"}]}

### 6. google pixely dostaly unikatni aplikaci
- repository: gsc
- primary_lane: SEO / SEARCH OPPORTUNITY
- lane_score: 65.2
- lane_scores: {"BREAKING / CURRENT NEWS": 20.9, "DISCOVERY / PREDICTIVE": 21.2, "CURRENT DEMAND / TREND": 17.8, "SEO / SEARCH OPPORTUNITY": 65.2, "UPDATE / REWRITE": 65.2}
- representative_signal: {"signal_id": "0ae659b6d7d26d48fa786ea723a916ad76ce2de58336191aa1cda5e8e5e8ff7b", "source_family": "gsc", "source": "sc-domain:androidmagazine.eu", "signal_type": "page", "entity": "https://androidmagazine.eu/ru/2025/11/06/google-pixely-dostaly-unikatni-aplikaci-theme-packs-pro-upravu-tapety-ikon-zvuku-i-hodin/", "topic": "google pixely dostaly unikatni aplikaci", "title": "https://androidmagazine.eu/ru/2025/11/06/google-pixely-dostaly-unikatni-aplikaci-theme-packs-pro-upravu-tapety-ikon-zvuku-i-hodin/", "url": "https://androidmagazine.eu/ru/2025/11/06/google-pixely-dostaly-unikatni-aplikaci-theme-packs-pro-upravu-tapety-ikon-zvuku-i-hodin/", "published_at": null, "first_seen_at": "2026-08-13T13:42:04.728Z", "latest_activity": "2026-08-13T13:42:04.728Z", "evidence": "GSC page", "confidence": "HIGH", "user_impact": "landing-page search performance", "raw_source_reference": "54b89505c1b003396ef3c6c520168529eae348e81421d5c196749d73385a97ae", "processing_status": "normalized", "metadata": {"clicks": 67, "impressions": 929, "ctr": 0.0721, "position": 7.5}}
- supporting_events_count: 4
- first_seen: 2026-08-13T13:41:53Z
- source_record_first_seen_at: 2026-08-13T13:41:53Z
- story_first_seen_at: 2026-08-13T13:41:53Z
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-13T13:42:04.728Z
- editorial_potential: HIGH
- why_it_may_matter: GA4 landing page performance
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: What happened around google pixely dostaly unikatni aplikaci, what users need to know, and which practical angle is missing from current coverage.
- opportunity_score: 70.8
- predictive_score: 43.8
- signal_score: 48.2
- wp_duplicate: {"existing_url": "", "draft_id": "", "action": "CREATE", "cannibalization_risk": "LOW", "matches": []}

### 7. android 16
- repository: gsc
- primary_lane: SEO / SEARCH OPPORTUNITY
- lane_score: 60.9
- lane_scores: {"BREAKING / CURRENT NEWS": 40.5, "DISCOVERY / PREDICTIVE": 18.299999999999997, "CURRENT DEMAND / TREND": 24.9, "SEO / SEARCH OPPORTUNITY": 60.9, "UPDATE / REWRITE": 76.9}
- representative_signal: {"signal_id": "7123a68dac40f77f0581bb10cc29cb3e04eda13d5827e51cef04803b99b955e3", "source_family": "gsc", "source": "sc-domain:androidmagazine.eu", "signal_type": "page", "entity": "https://androidmagazine.eu/fr/2025/09/20/stve-vas-novy-android-16-tady-je-navod-jak-se-vratit-ke-starsi-verzi-androidu/", "topic": "android 16", "title": "https://androidmagazine.eu/fr/2025/09/20/stve-vas-novy-android-16-tady-je-navod-jak-se-vratit-ke-starsi-verzi-androidu/", "url": "https://androidmagazine.eu/fr/2025/09/20/stve-vas-novy-android-16-tady-je-navod-jak-se-vratit-ke-starsi-verzi-androidu/", "published_at": null, "first_seen_at": "2026-08-13T13:42:04.728Z", "latest_activity": "2026-08-13T13:42:04.728Z", "evidence": "GSC page", "confidence": "HIGH", "user_impact": "landing-page search performance", "raw_source_reference": "47af9ab965bad46686f157d36db29165162e731e2e0d51d5685ecbe834457e3f", "processing_status": "normalized", "metadata": {"clicks": 14, "impressions": 249, "ctr": 0.0562, "position": 8.4}}
- supporting_events_count: 42
- first_seen: 2024-11-14T06:00:41
- source_record_first_seen_at: 2024-11-14T06:00:41
- story_first_seen_at: 2024-11-14T06:00:41
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-18T04:49:34Z
- editorial_potential: HIGH
- why_it_may_matter: Structured Google Trends cache
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: Why android 16 is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
- opportunity_score: 85.6
- predictive_score: 52.5
- signal_score: 58.5
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/3-skryta-nastaveni-android-16-qpr3-ktera-pomohou-vyuzivat-mobil-naplno-a-ochrani-vas/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "71695", "title": "3 skrytá nastavení Android 16 QPR3, která pomohou využívat mobil naplno a ochrání vás", "slug": "3-skryta-nastaveni-android-16-qpr3-ktera-pomohou-vyuzivat-mobil-naplno-a-ochrani-vas", "status": "publish", "date": "2026-03-09T20:25:11", "url": "https://androidmagazine.eu/3-skryta-nastaveni-android-16-qpr3-ktera-pomohou-vyuzivat-mobil-naplno-a-ochrani-vas/"}, {"id": "70085", "title": "6 nejdůležitějších změn, které v Android 16 QPR3 brzy dorazí na Pixely", "slug": "android-16-qpr3-sest-nejdulezitejsich-zmen-ktere-brzy-dorazi-na-pixely", "status": "publish", "date": "2026-02-06T08:00:44", "url": "https://androidmagazine.eu/android-16-qpr3-sest-nejdulezitejsich-zmen-ktere-brzy-dorazi-na-pixely/"}, {"id": "69151", "title": "Android 16 dostane neuvěřitelnou funkci: Aplikace vám pomohou ovládat jiné aplikace", "slug": "android-16-dostane-neuveritelnou-funkci-aplikace-vam-pomohou-ovladat-jine-aplikace", "status": "publish", "date": "2026-01-17T02:00:58", "url": "https://androidmagazine.eu/android-16-dostane-neuveritelnou-funkci-aplikace-vam-pomohou-ovladat-jine-aplikace/"}, {"id": "69082", "title": "Android 16 QPR3 Beta 2 tiše ořezává užitečnou funkci, která umožňovala efektivně pracovat s obrázky", "slug": "android-16-qpr3-beta-2-tise-orezava-uzitecnou-funkci-ktera-umoznovala-efektivne-pracovat-s-obrazky", "status": "publish", "date": "2026-01-16T02:00:22", "url": "https://androidmagazine.eu/android-16-qpr3-beta-2-tise-orezava-uzitecnou-funkci-ktera-umoznovala-efektivne-pracovat-s-obrazky/"}, {"id": "69060", "title": "Android 16 QPR 3 Beta 2 pro Pixely je tady. Opravuje spoustu chyb a řeší zamrzání i pomalé nabíjení", "slug": "android-16-qpr-3-beta-2-pro-pixely-je-tady-opravuje-spoustu-chyb-a-resi-zamrzani-i-pomale-nabijeni", "status": "publish", "date": "2026-01-15T09:00:04", "url": "https://androidmagazine.eu/android-16-qpr-3-beta-2-pro-pixely-je-tady-opravuje-spoustu-chyb-a-resi-zamrzani-i-pomale-nabijeni/"}]}

### 8. poco x8 pro vs galaxy
- repository: gsc
- primary_lane: UPDATE / REWRITE
- lane_score: 59.8
- lane_scores: {"BREAKING / CURRENT NEWS": 20.9, "DISCOVERY / PREDICTIVE": 21.2, "CURRENT DEMAND / TREND": 17.8, "SEO / SEARCH OPPORTUNITY": 49.8, "UPDATE / REWRITE": 59.8}
- representative_signal: {"signal_id": "c9069d99c823168292db27682f2a7e10b13562fa890504ae6fecef23de416a96", "source_family": "gsc", "source": "sc-domain:androidmagazine.eu", "signal_type": "page", "entity": "https://androidmagazine.eu/it/2026/03/28/poco-x8-pro-vs-galaxy-57-motivi-per-cui-scegliere-samsungc%27%C3%A8-pochissimo/", "topic": "poco x8 pro vs galaxy", "title": "https://androidmagazine.eu/it/2026/03/28/poco-x8-pro-vs-galaxy-57-motivi-per-cui-scegliere-samsungc%27%C3%A8-pochissimo/", "url": "https://androidmagazine.eu/it/2026/03/28/poco-x8-pro-vs-galaxy-57-motivi-per-cui-scegliere-samsungc%27%C3%A8-pochissimo/", "published_at": null, "first_seen_at": "2026-08-13T13:42:04.728Z", "latest_activity": "2026-08-13T13:42:04.728Z", "evidence": "GSC page", "confidence": "HIGH", "user_impact": "landing-page search performance", "raw_source_reference": "2316a61e94ade4289d267c06fc74de9a18960852d96998ea16cc5781f517d055", "processing_status": "normalized", "metadata": {"clicks": 21, "impressions": 280, "ctr": 0.075, "position": 7.4}}
- supporting_events_count: 8
- first_seen: 2026-08-13T13:41:53Z
- source_record_first_seen_at: 2026-08-13T13:41:53Z
- story_first_seen_at: 2026-08-13T13:41:53Z
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-13T13:42:04.728Z
- editorial_potential: HIGH
- why_it_may_matter: GA4 landing page performance
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: What happened around poco x8 pro vs galaxy, what users need to know, and which practical angle is missing from current coverage.
- opportunity_score: 70.9
- predictive_score: 43.9
- signal_score: 46.6
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/poco-x8-pro-vs-galaxy-a57-duvodu-proc-sahnout-po-samsungu-je-hodne-malo/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "72798", "title": "Poco X8 Pro vs. Galaxy A57 – důvodů, proč sáhnout po Samsungu, je hodně málo", "slug": "poco-x8-pro-vs-galaxy-a57-duvodu-proc-sahnout-po-samsungu-je-hodne-malo", "status": "publish", "date": "2026-03-28T07:45:48", "url": "https://androidmagazine.eu/poco-x8-pro-vs-galaxy-a57-duvodu-proc-sahnout-po-samsungu-je-hodne-malo/"}]}

### 9. jak si na androidu snadno
- repository: gsc
- primary_lane: UPDATE / REWRITE
- lane_score: 58.5
- lane_scores: {"BREAKING / CURRENT NEWS": 20.1, "DISCOVERY / PREDICTIVE": 21.4, "CURRENT DEMAND / TREND": 17.1, "SEO / SEARCH OPPORTUNITY": 42.5, "UPDATE / REWRITE": 58.5}
- representative_signal: {"signal_id": "277ffa7b725a10b2429e8bc0a31ff7ec9befe21a822d1c6355129ba13e5efe6e", "source_family": "gsc", "source": "sc-domain:androidmagazine.eu", "signal_type": "page", "entity": "https://androidmagazine.eu/ja/2024/10/28/jak-si-na-androidu-snadno-nastavit-tapety-ktere-se-meni-podle-denni-doby/", "topic": "jak si na androidu snadno", "title": "https://androidmagazine.eu/ja/2024/10/28/jak-si-na-androidu-snadno-nastavit-tapety-ktere-se-meni-podle-denni-doby/", "url": "https://androidmagazine.eu/ja/2024/10/28/jak-si-na-androidu-snadno-nastavit-tapety-ktere-se-meni-podle-denni-doby/", "published_at": null, "first_seen_at": "2026-08-13T13:42:04.728Z", "latest_activity": "2026-08-13T13:42:04.728Z", "evidence": "GSC page", "confidence": "HIGH", "user_impact": "landing-page search performance", "raw_source_reference": "ea316fd381a64d9dc69f1572fabf156afe6771f908324bd6b23a626de18bc523", "processing_status": "normalized", "metadata": {"clicks": 14, "impressions": 327, "ctr": 0.042800000000000005, "position": 8.7}}
- supporting_events_count: 3
- first_seen: 2024-10-28T06:00:02
- source_record_first_seen_at: 2024-10-28T06:00:02
- story_first_seen_at: 2024-10-28T06:00:02
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-13T13:42:04.728Z
- editorial_potential: HIGH
- why_it_may_matter: WordPress publish
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: How to improve the existing jak si na androidu snadno page for current search intent, CTR, and conversion to a better editorial angle.
- opportunity_score: 55.9
- predictive_score: 31.1
- signal_score: 35.4
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/jak-si-na-androidu-snadno-nastavit-tapety-ktere-se-meni-podle-denni-doby/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "58428", "title": "Jak si na Androidu snadno nastavit tapety, které se mění podle denní doby?", "slug": "jak-si-na-androidu-snadno-nastavit-tapety-ktere-se-meni-podle-denni-doby", "status": "publish", "date": "2024-10-28T06:00:02", "url": "https://androidmagazine.eu/jak-si-na-androidu-snadno-nastavit-tapety-ktere-se-meni-podle-denni-doby/"}]}

### 10. galaxy z fold8 vs oppo
- repository: gsc
- primary_lane: UPDATE / REWRITE
- lane_score: 57.0
- lane_scores: {"BREAKING / CURRENT NEWS": 23.4, "DISCOVERY / PREDICTIVE": 25.0, "CURRENT DEMAND / TREND": 20.6, "SEO / SEARCH OPPORTUNITY": 41.0, "UPDATE / REWRITE": 57.0}
- representative_signal: {"signal_id": "35a96a7d8222d847ea60363d130ad0b1d66a5811f1fa316d706fab692ce7128b", "source_family": "gsc", "source": "sc-domain:androidmagazine.eu", "signal_type": "page", "entity": "https://androidmagazine.eu/ja/2026/07/29/galaxy-z-fold8-vs-oppo-find-n6-jeden-sazi-na-jistotu-druhy-nabizi-vic-za-mene/", "topic": "galaxy z fold8 vs oppo", "title": "https://androidmagazine.eu/ja/2026/07/29/galaxy-z-fold8-vs-oppo-find-n6-jeden-sazi-na-jistotu-druhy-nabizi-vic-za-mene/", "url": "https://androidmagazine.eu/ja/2026/07/29/galaxy-z-fold8-vs-oppo-find-n6-jeden-sazi-na-jistotu-druhy-nabizi-vic-za-mene/", "published_at": null, "first_seen_at": "2026-08-13T13:42:04.728Z", "latest_activity": "2026-08-13T13:42:04.728Z", "evidence": "GSC page", "confidence": "MEDIUM", "user_impact": "landing-page search performance", "raw_source_reference": "9019e9915900fb78803f7d3be25717a7a396f0104acb14c41b8603e9165508a4", "processing_status": "normalized", "metadata": {"clicks": 16, "impressions": 87, "ctr": 0.1839, "position": 7.4}}
- supporting_events_count: 5
- first_seen: 2026-07-29T01:29:55
- source_record_first_seen_at: 2026-07-29T01:29:55
- story_first_seen_at: 2026-07-29T01:29:55
- lisa_first_seen_at: UNAVAILABLE
- latest_activity: 2026-08-13T13:42:04.728Z
- editorial_potential: HIGH
- why_it_may_matter: WordPress publish
- user_impact_reason: TECHNICAL CHANGE: Android/Google/Samsung platform or app change -> PRODUCT/SERVICE EFFECT: product behavior, compatibility, or feature adjustments -> USER IMPACT: users may experience a visible change in the device or app.
- user_impact_confidence: MEDIUM
- editorial_opportunity: How to improve the existing galaxy z fold8 vs oppo page for current search intent, CTR, and conversion to a better editorial angle.
- opportunity_score: 52.2
- predictive_score: 39.0
- signal_score: 42.4
- wp_duplicate: {"existing_url": "https://androidmagazine.eu/galaxy-z-fold8-vs-oppo-find-n6-jeden-sazi-na-jistotu-druhy-nabizi-vic-za-mene/", "draft_id": "", "action": "UPDATE/REWRITE/MERGE", "cannibalization_risk": "HIGH", "matches": [{"id": "77778", "title": "Galaxy Z Fold8 vs. OPPO Find N6: Jeden sází na jistotu, druhý nabízí víc za méně", "slug": "galaxy-z-fold8-vs-oppo-find-n6-jeden-sazi-na-jistotu-druhy-nabizi-vic-za-mene", "status": "publish", "date": "2026-07-29T01:29:55", "url": "https://androidmagazine.eu/galaxy-z-fold8-vs-oppo-find-n6-jeden-sazi-na-jistotu-druhy-nabizi-vic-za-mene/"}]}

## Counterfactual
- TOP 1: pixel 11
- TOP 3: pixel 11, redmi k100 pro max, jak vypnout ai funkce na

## Final portfolio
- pixel 11 | lane=BREAKING / CURRENT NEWS | action=BREAKING / CURRENT NEWS | author=Jana Maxová
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / Why pixel 11 is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
  - evidence: EVENT: Pixel 11 coverage is maturing from rumors into repeat reporting and product context -> PRODUCT/USER CHANGE: readers want to know whether the device is imminent, what changes, and whether to wait -> AUDIENCE RELEVANCE: Pixel buyers search hard before launch and after major rumor cycles -> ANDROIDMAGAZINE OPPORTUNITY: keep one living Pixel 11 explainer that merges current signals, buying advice and what is actually confirmed.
  - sources: ["9to5Google", "Bloomberg.com", "TechCrunch", "Tom's Guide", "ZDNET", "androidmagazine.eu", "local editorial report cache", "properties/361709661", "sc-domain:androidmagazine.eu"]
- redmi k100 pro max | lane=CURRENT DEMAND / TREND | action=CURRENT DEMAND / TREND | author=Jana Maxová
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / Why redmi k100 pro max is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
  - evidence: Structured Google Trends cache
  - sources: ["androidmagazine.eu", "local editorial report cache", "properties/361709661"]
- jak vypnout ai funkce na | lane=SEO / SEARCH OPPORTUNITY | action=SEO / SEARCH OPPORTUNITY | author=redaktor
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / How to improve the existing jak vypnout ai funkce na page for current search intent, CTR, and conversion to a better editorial angle.
  - evidence: WordPress publish
  - sources: ["androidmagazine.eu", "properties/361709661", "sc-domain:androidmagazine.eu"]
- poco f9 ultra | lane=SEO / SEARCH OPPORTUNITY | action=SEO / SEARCH OPPORTUNITY | author=Jana Maxová
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / How to improve the existing poco f9 ultra page for current search intent, CTR, and conversion to a better editorial angle.
  - evidence: WordPress publish
  - sources: ["androidmagazine.eu", "properties/361709661", "sc-domain:androidmagazine.eu"]
- jak zapnout nebo vypnout funkci | lane=UPDATE / REWRITE | action=UPDATE / REWRITE | author=redaktor
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / How to improve the existing jak zapnout nebo vypnout funkci page for current search intent, CTR, and conversion to a better editorial angle.
  - evidence: WordPress publish
  - sources: ["androidmagazine.eu", "sc-domain:androidmagazine.eu"]
- google pixely dostaly unikatni aplikaci | lane=SEO / SEARCH OPPORTUNITY | action=SEO / SEARCH OPPORTUNITY | author=Roman Zavřel
  - reason: Clear user-facing how-to / troubleshooting / comparison angle. / What happened around google pixely dostaly unikatni aplikaci, what users need to know, and which practical angle is missing from current coverage.
  - evidence: GA4 landing page performance
  - sources: ["properties/361709661", "sc-domain:androidmagazine.eu"]
- android 16 | lane=SEO / SEARCH OPPORTUNITY | action=SEO / SEARCH OPPORTUNITY | author=redaktor
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / Why android 16 is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
  - evidence: Structured Google Trends cache
  - sources: ["androidmagazine.eu", "local editorial report cache", "properties/361709661", "sc-domain:androidmagazine.eu"]
- poco x8 pro vs galaxy | lane=UPDATE / REWRITE | action=UPDATE / REWRITE | author=Jana Maxová
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / What happened around poco x8 pro vs galaxy, what users need to know, and which practical angle is missing from current coverage.
  - evidence: GA4 landing page performance
  - sources: ["properties/361709661", "sc-domain:androidmagazine.eu"]
- jak si na androidu snadno | lane=UPDATE / REWRITE | action=UPDATE / REWRITE | author=redaktor
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / How to improve the existing jak si na androidu snadno page for current search intent, CTR, and conversion to a better editorial angle.
  - evidence: WordPress publish
  - sources: ["androidmagazine.eu", "sc-domain:androidmagazine.eu"]
- galaxy z fold8 vs oppo | lane=UPDATE / REWRITE | action=UPDATE / REWRITE | author=Jana Maxová
  - reason: UPDATE/REWRITE with added value on existing coverage, not a pure duplicate. / How to improve the existing galaxy z fold8 vs oppo page for current search intent, CTR, and conversion to a better editorial angle.
  - evidence: WordPress publish
  - sources: ["androidmagazine.eu", "properties/361709661", "sc-domain:androidmagazine.eu"]

## GitHub watchlist promotions
- None

## Implemented / Partial / Not implemented
### Implemented
- GitHub read-only delta ingestion, raw signal storage, clustering, and persisted watchlist re-evaluation
- GSC local CSV ingestion and query/page normalization
- GA4 local CSV ingestion and page/landing-page normalization
- WordPress local CSV ingestion and duplicate-baseline index
- Structured Google Trends SQLite cache with bootstrap ingestion from the local editorial report
- Opt-in Google News / News discovery RSS ingestion and pre-gate event clustering
- Cross-source normalized signal layer and unified candidate universe
- Global ranking, counterfactual top1/top3, and marginal portfolio selection
- Test-mode reporting with no remote API calls
- GitHub watchlist promotions persist back into the GitHub watchlist DB

### Partially Implemented
- Source Coverage Audit is explicit for the connected layers, while News discovery is opt-in for the controlled test path
- Reality / information age / WP / unique value gates are implemented heuristically from local evidence, not by a full newsroom model
- Structured Trends cache is seeded from the local editorial report until a dedicated live Trends ingest is available

### Not Implemented
- Reddit sensor
- X sensor
- YouTube / community sensor
- AdSense / revenue source
- Automatic WordPress publication
- Automatic multi-source remote API sync beyond existing local exports

### Failed Needs Fix
