# Ranni redakcni plan V6.5 pro 15. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: UNAVAILABLE (`JSON code=500 Internal Server Error`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`JSON code=500 Internal Server Error`) -> fallback `pytrends`
- `pytrends`: CHECKED; `Siri AI` bez noveho spike, `iOS 27` drzi dozvuk, `One UI 9.5` bez dat, `Google Find Hub` bez akcelerace
- Reddit RSS: PARTIAL - `r/apple` checked bez winneru, `r/Android` a `r/samsung` blocked/429

## LSA
- Vrstva 1: `0` cistych overnight CREATE.
- Apple Newsroom prinesl official availability balicek kolem Siri AI a systemovych updatu, ale stejny user intent uz LSA vcera pokryl, proto rano zustava jen update/follow-up vrstva.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- 9to5Google prineslo Google System Updates i Googlebook pre-orders, ale bez dost silneho ceskeho samostatneho pegu a bez potvrzeneho spike pro hlavni slot.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Samsung Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- One UI 9 Beta 2 pro S24 uz ma stejnointentovou coverage na SamsungMagazine a zbyvajici fresh signaly jsou rumor nebo US-only, proto rano zustava jen One UI / evergreen backbone.
- Vrstva 2: `20` temat. Backbone stoji na verified evergreen/GSC vrstve a current-demand updatech.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live API dostupne a 28denni query snapshot uspel
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - direct probe vratil JSON code=500; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - direct probe vratil JSON code=500; fallback = pytrends
- Apple Newsroom / 9to5Mac / 9to5Google / Samsung Newsroom / GSMArena / The Verge / Google Blog: CHECKED
- Reddit RSS: PARTIAL - r/apple checked, r/Android a r/samsung blocked/429
- GitHub: CHECKED - technicke commity bez editorial winneru
- APK / teardown layer: NOT CHECKED - fallback na 9to5Google + GSMArena