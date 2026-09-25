# Ranni redakcni plan V6.5 pro 12. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: dnesni `morning_context_latest.md` byl nacten a aplikovan pred pre-flightem.

Fallbacky:
- Google SERP Search API: UNAVAILABLE (`JSON code=500`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`JSON code=500`) -> fallback `pytrends`
- `pytrends`: CHECKED, shortlist probehl bez vyrazneho CZ spike u vetsiny finalnich kusu
- Reddit RSS: UNAVAILABLE - HTTP 403 Blocked

## LSA
- Vrstva 1: `1` cistych overnight CREATE.
- Doporuceny kus: `Apple priznal odklad dvou funkci iOS 27. Po instalaci tohle spoustu lidi zklame`
- Titulky: `Discover` Apple priznal odklad dvou funkci iOS 27. Po instalaci tohle spoustu lidi zklame | `Search` iOS 27: ktere dve funkce Apple odlozil do budoucni aktualizace | `Balanced` Dve slibene funkce iOS 27 neprijdou hned. Apple je odsunul na pozdeji
- Doporucena varianta: `Discover` - Discover varianta stavi na priznane ztrate proti ocekavani a ma nejsilnejsi click potential i mimo hardcore Apple publikum.
- Vrstva 2: `19` temat. Backbone stoji na verified evergreen/GSC vrstve a na kuratorovanych watchlist signalech.

## Android Magazine
- Vrstva 1: `0` cistych overnight CREATE.
- Prioritu dnes nenafukuji; cisty samostatny overnight peg neprosel Roman Testem + overlap filtrem.
- Vrstva 2: `21` temat. Backbone stoji na verified evergreen/GSC vrstve a na kuratorovanych watchlist signalech.

## Samsung Magazine
- Vrstva 1: `1` cistych overnight CREATE.
- Doporuceny kus: `Samsung Galaxy A08 unikl pres prodejce. Zname vybavu i oficialni obrazky`
- Titulky: `Discover` Samsung Galaxy A08 unikl pres prodejce. Zname vybavu i oficialni obrazky | `Search` Samsung Galaxy A08: unikle specifikace, oficialni rendery a co cekat od novinky | `Balanced` Galaxy A08 je venku drsne brzy. Retailer listing odhalil specifikace i vzhled
- Doporucena varianta: `Discover` - Discover varianta je nejprimocarejsi, rika ze unik neni jen rumor a hned prodava dve konkretni veci: vybavu i obrazky.
- Vrstva 2: `19` temat. Backbone stoji na verified evergreen/GSC vrstve a na kuratorovanych watchlist signalech.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live API dostupne a 28denni query snapshot uspel
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - JustSerpAPI vratilo JSON code=500; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - JustSerpAPI vratilo JSON code=500; fallback = pytrends
- Google Trends fallback (pytrends): CHECKED - shortlist probehly, u casti termu bez viditelneho aktualniho spike
- Apple Newsroom: CHECKED
- 9to5Mac: CHECKED
- 9to5Google: CHECKED
- Samsung Newsroom: CHECKED - no relevant overnight signal
- GSMArena: CHECKED
- The Verge: CHECKED - bez editorial winneru pro hlavni shortlist
- Google Blog / Workspace Updates: CHECKED - bez silneho standalone pegu
- Reddit RSS: UNAVAILABLE - HTTP 403 Blocked pro r/apple, r/Android i r/samsung
- GitHub: CHECKED - chromium mel fresh engineering commity, ale bez cisteho editorial winneru; aosp/material bez winneru
- APK / teardown layer: NOT CHECKED - shortlist uz mel silnejsi verified zdroje
- developer docs / support docs / changelogs: CHECKED - Apple + Google update vrstvy prosly
- regulatory / certifikace: NOT CHECKED - bez overnight winneru
- X / leakers: NOT CHECKED - rano drzim na overitelnych public zdrojich
- YouTube: NOT CHECKED - bez potreby proti silnejsim zdrojum
- smaller specialist media: NOT CHECKED - priorita sla do Tier S/A + verified backbone
