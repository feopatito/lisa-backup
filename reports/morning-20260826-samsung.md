# Samsung Magazine - redakční plán 26. 8. 2026

Status: opožděný recovery výstup po ranním heartbeat triggeru. Pre-flight prošel živě v 7:13 CEST.

Web: samsungmagazine.eu  
Priorita webu: Samsung / One UI / Galaxy, primárně Search, Discover sekundárně  
Publikace: pouze po schválení Romana nebo Toma

## Data Gate

- GA4: PASS
- GSC: PASS
- Manticore: PASS
- WordPress auth/read: PASS
- Google Trends: UNAVAILABLE - JustSerpAPI vracel `code=500`, nenahrazuji odhadem

## Doporučené pořadí

1. CREATE - Smart Switch update
2. UPDATE - One UI 9 beta 6
3. UPDATE - Galaxy S27 Ultra CAD renders

## Sloty

### 1. CREATE - Smart Switch update

Candidate ID: SAM-SMARTSWITCH  
Exact topic: Samsung Smart Switch update copies more data and is easier to use  
Proposed title: Samsung vylepšil Smart Switch. Přechod na nový Galaxy má být jednodušší  
Primary lane: Current Demand  
Timing: dopoledne / po Samsung tématech  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - no duplicate  
Opportunity score: 73  
Predictive score: 70  
Confidence: MEDIUM  
Final write gate: PASS

Evidence:
- GSMArena RSS: "Samsung's updated Smart Switch is easier to use and copies more data", 25. 8. 22:02 CEST
- Samsung Newsroom: "An Easier Way To Switch to the New Galaxy Z Fold8", 25. 8. 08:00 UTC
- Manticore Samsung: no duplicate

Unique value: praktický checklist co se nově přenese, co se pořád nepřenese a pro koho má update reálný přínos.

### 2. UPDATE - One UI 9 beta 6

Candidate ID: SAM-ONEUI9  
Exact topic: One UI 9 beta 6 for Galaxy S26  
Proposed title: One UI 9 beta 6: co opravit v už existujícím článku  
Primary lane: Current Demand  
Timing: po Smart Switch / podle redakční kapacity  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - same intent already published 2026-08-25  
Opportunity score: 81  
Predictive score: 67  
Confidence: HIGH  
Final write gate: PASS jen jako UPDATE, ne CREATE

Evidence:
- GSMArena 26. 8. 04:03 CEST
- GSC Samsung: `one ui` 135 824 impresí, 22 797 kliků
- Manticore našel hotový článek z 25. 8.

Unique value: nepsat duplicitu. Doplnit existující článek o dopad oprav pro běžné uživatele, oddělit oficiální One UI 9 beta program od changelogu beta 6.

### 3. UPDATE - Galaxy S27 Ultra CAD renders

Candidate ID: SAM-S27ULTRA  
Exact topic: Galaxy S27 Ultra CAD renders  
Proposed title: Galaxy S27 Ultra rendery: nepsat duplicitu, jen doplnit existující článek  
Primary lane: Discovery  
Timing: až po ověření, že update existujícího článku dává smysl  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - same intent already published 2026-08-26  
Opportunity score: 76  
Predictive score: 71  
Confidence: HIGH  
Final write gate: PASS jen jako UPDATE

Evidence:
- GSMArena 26. 8. 01:02 CEST
- Manticore našel článek z 26. 8. 03:58 UTC

Unique value: nepsat nový článek. Dodat kontext k designovým změnám jen pokud jsou nové detaily proti existujícímu pokrytí.

## Drop / Monitor pro Samsung Magazine

- Galaxy S26 FE event: DROP jako nový článek. Samsung Magazine má články z 20. 8. a 25. 8.
- Google Trends: MONITOR. API dnes vrací chybu 500, bez dat nenahrazuji trend odhadem.

## Source Coverage Audit

- WordPress/Manticore: CHECKED
- GSC: CHECKED
- GA4: CHECKED
- AdSense: NOT CHECKED - secondary signal unavailable
- Google Trends: UNAVAILABLE - JustSerpAPI 500
- Google News: NOT CHECKED - recovery běh bez automatické News vrstvy
- Major tech media: CHECKED - 9to5Mac, 9to5Google, GSMArena, The Verge
- Official newsrooms: CHECKED - Apple Newsroom, Samsung Newsroom, Google Blog, Android Developers Blog
- Product pages/support docs: NOT CHECKED - není zapojený delta layer
- Developer docs/changelogs: PARTIAL - Android Developers Blog + GitHub releases
- GitHub: CHECKED read-only, bez silného uživatelského signálu kromě Gemini CLI releasů
- APK/beta/regulatory/Reddit/forums/X/YouTube: NOT CHECKED - není implementováno v recovery běhu

