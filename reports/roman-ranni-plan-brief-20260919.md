# Ranni redakcni plan V6.5 pro 19. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: UNAVAILABLE (`env_missing`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`env_missing`) -> fallback `pytrends`
- `pytrends`: CHECKED; `iphone 18` a `pixel 11` rano bez akcelerace, `one ui 9` bez noveho CZ spike
- Reddit RSS: `r/apple` CHECKED, `r/Android` a `r/samsung` UNAVAILABLE (`HTTP 429`)

## LSA
- Vrstva 1: `0` cistych overnight CREATE.
- LSA dnes nema cisty overnight CREATE. Apple Watch Series 12 heart-rate test i jazykove zmeny v iOS 27 jsou overene, ale rano jsou silnejsi jako follow-up nez jako novy solo slot.
- Vrstva 2 stoji na Apple utility backbone + silnych query clusterech kolem iPhonu, iOS a Apple Watch.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-upech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Android Magazine dnes nema cisty overnight CREATE. Gemini na Macu s iMessage i Googlebook whisper jsou overene, ale jsou moc uzke na hlavni ranni Android slot.
- Vrstva 2 drzi verified evergreen a utility intenty, protoze live Android-only okno dnes neprineslo silnejsi samostatny winner.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-upech.

## Samsung Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Samsung Magazine dnes nema cisty overnight CREATE. One UI 9 rollout ma overlap s existujici coverage a leak baterii S27 je zatim jen watchlist signal.
- Vrstva 2 proto drzi One UI / Samsung utility backbone a jen kuratorovane weak-signal follow-upy.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a kuratorovanych follow-upech.

## Source Coverage Audit

- WordPress: CHECKED - auth probe v pre-flightu PASS pro vsechny 3 weby
- Manticore: CHECKED - pre-flight PASS pro vsechny 3 weby
- GSC: CHECKED - live API dostupne a 28denni query snapshot uspel
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - env v tomto behu nebyl ready; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - env v tomto behu nebyl ready; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - Apple/Pixel shortlist bez ranni akcelerace, `one ui 9` bez noveho CZ spike
- Reddit RSS: PARTIAL - `r/apple` CHECKED, `r/Android` a `r/samsung` vratily HTTP 429
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
