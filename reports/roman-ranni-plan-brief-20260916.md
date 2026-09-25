# Ranni redakcni plan V6.5 pro 16. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: UNAVAILABLE (`JSON code=402 No active subscription found`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`JSON code=500 Internal Server Error`) -> fallback `pytrends`
- `pytrends`: CHECKED; `iphone duo`, `android 17`, `gemini live`, `google photos samsung`, `pixel watch` bez ranni akcelerace v CZ
- Reddit RSS: UNAVAILABLE - `r/apple`, `r/Android` i `r/samsung` dnes blokuje anti-bot/network policy wall

## LSA
- Vrstva 1: `0` cistych overnight CREATE.
- 9to5Mac prineslo Reference Image detail a Car Keys follow-up, ale rano uz je na LSA cerstva Apple AI/Home coverage a foto/AI intent je prilis blizko existujicim kusum.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Google poslal Android 17 QPR1, Pixel Drop i Gemini 3.8 Live, ale pytrends neukazuje ranni spike a Manticore vraci blizke Android 17 / Gemini intenty, takze rano zustava update vrstva.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Samsung Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Samsung uz ve 02:05 CEST publikoval One UI 9 availability kus pro S26 a dalsi fresh signaly jako Samsung Gallery -> Google Photos backup nebo S27 Ultra rumor zustavaji jen ve follow-up vrstve.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live API dostupne a 28denni query snapshot uspel
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - direct probe vratil JSON code=402; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - direct probe vratil JSON code=500; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - probe na Apple / Android / Samsung termy probehly bez ranni akcelerace
- Apple Newsroom: CHECKED - v aktivnim okne bez noveho user-facing Apple hardware/software winneru pro tato media
- 9to5Mac: CHECKED - Reference Image mode + Car Keys follow-upy prosly duplicate logikou
- 9to5Google: CHECKED - Android 17 QPR1, Gemini 3.8 Live a Samsung Gallery -> Google Photos backup prosly reality checkem
- Samsung Newsroom: CHECKED - v aktivnim okne bez user-facing overnight winneru; rano jen pozdejsi interview mimo okno
- GSMArena: CHECKED - iPhone Duo availability, S27 Ultra kamery a NAND/DRAM pricing zkontrolovany jako rumor/follow-up vrstva
- The Verge: CHECKED - bez relevantniho Apple/Android/Samsung overnight winneru pro Priority vrstvu
- Google Blog / Workspace Updates: CHECKED - Pixel Drop + Gemini 3.8 Live potvrzeny, ale rano bez samostatneho CREATE winneru
- Reddit RSS: UNAVAILABLE - vsechny tri feedy blokovany anti-bot/network policy wall
- GitHub: NOT CHECKED - dnesni portfolio rozhodly silnejsi newsroom/RSS signaly a evergreen backbone
- APK / teardown layer: NOT CHECKED - fallback zustal na 9to5Google + GSMArena
- developer docs / support docs / changelogs: CHECKED - Apple a Google oficialni vrstvy prosly bez dalsiho overnight winneru
- regulatory / certifikace: NOT CHECKED - bez overnight hardware/cert signalu pro portfolio
- X / leakers: NOT CHECKED - rano drzim na overitelnych public zdrojich
- YouTube: NOT CHECKED - bez potreby proti silnejsim zdrojum
- smaller specialist media: NOT CHECKED - priorita sla do Tier S + verified backbone
