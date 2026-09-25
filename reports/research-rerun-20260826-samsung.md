# Samsung Magazine - research rerun 26. 8. 2026

Status: čerstvý rerun po požadavku Toma. DATA GATE prošel živě v 8:50 CEST.

Web: samsungmagazine.eu  
Priorita: Samsung / One UI / Galaxy, primárně Search  
Publikace: pouze po schválení Romana nebo Toma

## Data Gate

- GA4: PASS
- GSC: PASS
- Manticore: PASS
- WordPress read/auth: PASS
- Google Trends: CHECKED přes pytrends fallback
- GitHub: CHECKED read-only, bez kvalifikovaného Samsung slotu

## Doporučené pořadí

1. UPDATE - One UI 9 beta 6
2. CREATE - Smart Switch / přechod z iPhonu na Galaxy
3. UPDATE - Galaxy S27 Ultra CAD renders

## Sloty

### 1. UPDATE - One UI 9 beta 6

Candidate ID: SAM-RR-260826-ONEUI9-BETA6  
Exact topic: One UI 9 beta 6 pro Galaxy S26, opravy Now Brief, Home screen, camera widget a Expert RAW  
Proposed title: One UI 9 beta 6 opravuje fotoaparát i widgety. Co doplnit do existujícího článku  
Primary lane: Search + Current Demand  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - Samsung Magazine už má článek z 25.8. a další navazující One UI 9 článek  
Opportunity score: 84  
Predictive score: 70  
Confidence: HIGH  
Final write gate: PASS jen jako UPDATE, ne CREATE

Evidence:
- GSMArena 26.8.: beta 6 má 851 MB, build ZZHE, Německo/Indie/Polsko/UK/Korea, opravy Now Brief, home screen, Expert RAW 24MP a camera widget
- SamMobile 25.8.: firmware S94xBXXU4ZZHC, oficiální changelog se čtyřmi změnami
- GSC Samsung: `one ui` 132 630 impresí, 21 927 kliků, pozice 4.0; `one ui 9` 68 272 impresí, 2 992 kliků, pozice 2.3
- Manticore: existující článek `Samsung vydává 6. betu One UI 9...` z 25.8.

Unique value: doplnit existující článek o regiony, build, přesný changelog, nový AI Select toggle a dopad pro běžné uživatele.

### 2. CREATE - Smart Switch / iOS to Galaxy

Candidate ID: SAM-RR-260826-SMARTSWITCH  
Exact topic: Smart Switch v One UI 9 usnadňuje přechod z iPhonu na Galaxy Z Fold8/Z Flip8 a přenáší více dat  
Proposed title: Přechod z iPhonu na Galaxy má být jednodušší. Samsung rozšířil Smart Switch  
Primary lane: Current Demand + practical guide  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - Manticore našel starší Smart Switch/RCS článek, ne stejný pozitivní transfer intent  
Opportunity score: 74  
Predictive score: 68  
Confidence: HIGH  
Final write gate: PASS

Evidence:
- Samsung Global Newsroom: Smart Switch přes QR kód, bez nutnosti instalace iOS aplikace; přenos hesel/passkeys, historie hovorů, accessibility settings a eSIM; Quick Share kompatibilita s iOS zařízeními
- GSC Samsung má silný obecný Samsung/Galaxy demand; specifický Smart Switch trend je slabý, proto praktický Current Demand, ne čisté SEO
- Manticore: podobný článek z 20.8. řeší problém s RCS po přechodu, nikoli nové rozšíření Smart Switch

Unique value: checklist co se přenese, co se nepřenese, podmínky Android 17/iOS 26.6, regionální opatrnost, oddělit Smart Switch od Quick Share.

### 3. UPDATE - Galaxy S27 Ultra CAD renders

Candidate ID: SAM-RR-260826-S27ULTRA-RENDERS  
Exact topic: Galaxy S27 Ultra CAD renders a designové změny  
Proposed title: Galaxy S27 Ultra rendery: doplnit existující článek, nepsat duplicitu  
Primary lane: Discovery + Search  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - Samsung Magazine má článek z 26.8. 03:58 UTC a starší z 24.8.  
Opportunity score: 78  
Predictive score: 69  
Confidence: HIGH  
Final write gate: PASS jen jako UPDATE

Evidence:
- GSC Samsung: `s27 ultra` 24 726 impresí, 1 185 kliků, pozice 2.6; `samsung galaxy s27 ultra` 13 155 impresí, pozice 2.6; `galaxy s27 ultra` 8 215 impresí, CTR 7.5 %
- Manticore: existující článek `První a skutečně detailní pohled na Galaxy S27 Ultra...` z 26.8.
- Search relevance je vysoká, ale duplicita má veto

Unique value: přidat nové detaily jen pokud se liší od už vydaného článku; jinak MONITOR.

## Drop / Monitor

- Galaxy S26 FE event: DROP jako CREATE. Manticore našel články z 20.8. a 25.8.
- Quick Share Apple devices: zahrnout do Smart Switch článku, ne samostatný slot bez silnějšího signálu.

## Source Coverage Audit

- WordPress/Manticore: CHECKED
- GSC: CHECKED live, 28denní query data
- GA4: CHECKED live, 7denní top pages
- Google Trends: CHECKED přes pytrends
- Major tech media: CHECKED - GSMArena, SamMobile, Android Central/Authority jako cross-check
- Official newsroom: CHECKED - Samsung Global Newsroom
- GitHub: CHECKED read-only, no Samsung shortlist
- Reddit/X/YouTube/community: NOT CHECKED - bez přímé vrstvy v tomto rerunu

