# Ranni redakcni plan V6.5 pro 14. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: UNAVAILABLE (`JSON code=402 No active subscription found`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`JSON code=402 No active subscription found`) -> fallback `pytrends`
- `pytrends`: CHECKED s castecnym omezenim (`Galaxy S26 FE` narazil na 429); Apple termy bez noveho ranního spike
- Reddit RSS: PARTIAL - `r/apple` bez relevant signalu, `r/Android` a `r/samsung` vratily `429`

## LSA
- Vrstva 1: `0` cistych overnight CREATE.
- LSA dnes nema zadny cisty overnight CREATE. Jediny cerstvy signal je retail-store follow-up z 9to5Mac, ale bez dost silneho samostatneho pegu pro Vrstva 1.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Android Magazine dnes nema zadny cisty overnight CREATE. Discovery okno bylo na Android-only signaly prazdne, proto portfolio stoji na poctivem evergreen/GSC backbone.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Samsung Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Samsung Magazine dnes nema zadny cisty overnight CREATE. Samsung Newsroom ani feedy neprinesly novy user-facing winner, proto drzim silnou One UI / evergreen zakladnu.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live API dostupne a 28denni query snapshot uspel
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - direct probe vratil JSON code=402; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - direct probe vratil JSON code=402; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - Apple termy probehly, Galaxy S26 FE narazil na 429, One UI 9.5 bez dat
- Apple Newsroom: CHECKED - no relevant overnight signal
- 9to5Mac: CHECKED - 1 overnight Apple follow-up, ale ne CREATE winner
- 9to5Google: CHECKED - no relevant overnight signal
- Samsung Newsroom: CHECKED - no relevant overnight signal
- GSMArena: CHECKED - Apple week-in-review bez samostatneho fresh pegu
- The Verge: CHECKED - no relevant overnight signal
- Google Blog / Workspace Updates: CHECKED - no relevant overnight signal
- Reddit RSS: PARTIAL - r/apple bez relevant signalu, r/Android a r/samsung HTTP 429
- GitHub: CHECKED - chromium mel jen technicke commity bez editorial winneru
