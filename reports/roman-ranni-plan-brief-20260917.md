# Ranni redakcni plan V6.5 pro 17. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: UNAVAILABLE (`JSON code=500 Internal Server Error`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`JSON code=500 Internal Server Error`) -> fallback `pytrends`
- `pytrends`: CHECKED; Apple / Android / Samsung shortlist bez ranni akcelerace v CZ
- Reddit RSS: UNAVAILABLE - `r/apple`, `r/Android` i `r/samsung` vraci `HTTP 403 Blocked`

## LSA
- Vrstva 1: `0` cistych overnight CREATE.
- LSA dnes nema cisty overnight CREATE. 9to5Mac sice poslalo iOS 27.2 detaily a viral freeze bug, ale CZ pytrends je bez akcelerace a vlastni nocni coverage na LSA uz je na Apple software/iPhone 18 hodne husta, takze rano drzim follow-up + evergreen vrstvu.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Android Magazine dnes nema cisty overnight CREATE. Android 17 QPR2 Beta 5 i Google Home MCP jsou overene, ale pytrends je bez ranni akcelerace a Android 17 / smart-home intenty jsou pro tenhle web rano bezpecnejsi jako follow-up vrstva.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Samsung Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Samsung Magazine dnes nema cisty overnight CREATE. Samsung Newsroom sice spustil oficialni rollout One UI 9, ale web uz v noci publikoval vlastni support/list kus a dalsi fresh signaly zustavaji jen ve follow-up vrstve.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live API dostupne a 28denni query snapshot uspel
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - direct probe vratil HTTP 200 s JSON code=500; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - direct probe vratil HTTP 200 s JSON code=500; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - shortlist probehl bez ranni akcelerace v CZ
- Reddit RSS: UNAVAILABLE - r/apple, r/Android i r/samsung dnes vraci HTTP 403 Blocked i s browser User-Agent
- Competitor Research: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- seo-content: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- humanizer: NOT CHECKED - skill/tool v tomhle behu nebyl callable
- Apple / Google / Samsung official + Tier S RSS: CHECKED - overnight signaly prosly reality checkem a duplicate logikou
- GSMArena + The Verge: CHECKED - pouzito jako sekundarni potvrzeni u hrancnich follow-upu
- GitHub: NOT CHECKED - dnesni portfolio rozhodly silnejsi newsroom/RSS signaly a evergreen backbone
- APK / teardown layer: NOT CHECKED - fallback zustal na 9to5Google + GSMArena
- developer docs / support docs / changelogs: CHECKED - bez dalsiho overnight winneru pro Vrstva 1
- regulatory / certifikace: NOT CHECKED - bez overnight hardware/cert signalu pro portfolio
- X / leakers: NOT CHECKED - rano drzim na overitelnych public zdrojich
- YouTube: NOT CHECKED - bez potreby proti silnejsim zdrojum
- smaller specialist media: NOT CHECKED - priorita sla do Tier S + verified backbone