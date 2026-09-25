# Ranni redakcni plan V6.5 pro 18. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: UNAVAILABLE (`JSON code=402 No active subscription found`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`JSON code=402 No active subscription found`) -> fallback `pytrends`
- `pytrends`: CHECKED; `ios 27` drzi jen baseline, Android/Samsung shortlist bez ranni akcelerace
- Reddit RSS: UNAVAILABLE - `r/apple`, `r/Android` i `r/samsung` vraci `HTTP 403 Blocked`

## LSA
- Vrstva 1: `0` cistych overnight CREATE.
- LSA dnes nema cisty overnight CREATE. Nejcerstvejsi user-facing Apple signal je WhatsApp search button na iOS, ale bez trend akcelerace a vedle silne vlastni nocni coverage je to rano bezpecnejsi jako follow-up.
- Vrstva 2 stoji na Apple utility backbone + silnych query clusterech kolem iPhonu, iOS a Apple Watch.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-upech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Android Magazine dnes nema cisty overnight CREATE. Pixel Now Playing a Google Keep widget jsou overene, ale jsou to male produktove tweaky bez sirokeho ranního pegu.
- Vrstva 2 drzi verified evergreen a utility intenty, protoze live Android-only okno dnes neprineslo silnejsi samostatny winner.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-upech.

## Samsung Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Samsung Magazine dnes nema cisty overnight CREATE. Relevantni overnight signal je hlavne One UI 9 timing recap, ale ten ma jasny overlap s uz existujici coverage.
- Vrstva 2 proto drzi One UI / Samsung utility backbone a jen kuratorovane weak-signal follow-upy.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-upech.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live API dostupne a 28denni query snapshot uspel
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - direct probe vratil HTTP 200 s JSON code=402; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - direct probe vratil HTTP 200 s JSON code=402; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - `ios 27` jen baseline, Android/Samsung shortlist bez ranni akcelerace
- Reddit RSS: UNAVAILABLE - `r/apple`, `r/Android` i `r/samsung` dnes vraci HTTP 403 Blocked i s browser User-Agent
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
