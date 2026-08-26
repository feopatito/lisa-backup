# Letem světem Applem - redakční plán 26. 8. 2026

Status: opožděný recovery výstup po ranním heartbeat triggeru. Pre-flight prošel živě v 7:13 CEST.

Web: letemsvetemapplem.eu  
Priorita webu: Discover-first, Apple + širší tech  
Publikace: pouze po schválení Romana nebo Toma

## Data Gate

- GA4: PASS
- GSC: PASS
- Manticore: PASS
- WordPress auth/read: PASS
- Google Trends: UNAVAILABLE - JustSerpAPI vracel `code=500`, nenahrazuji odhadem

## Doporučené pořadí

1. CREATE - iOS 27 release date
2. CREATE - WhatsApp security features
3. FOLLOW-UP - Mac mini M6

## Sloty

### 1. CREATE - iOS 27 release date

Candidate ID: LSA-IOS27  
Exact topic: iOS 27 release date and update timing  
Proposed title: Kdy vyjde iOS 27: očekávaný termín vydání a co hlídat  
Primary lane: SEO  
Timing: dopoledne  
Reality status: PASS  
Information age: CURRENT  
WP check: CHECKED - one old iOS 18.3 article, no same intent  
Opportunity score: 86  
Predictive score: 79  
Confidence: HIGH  
Final write gate: PASS

Evidence:
- GSC LSA: `ios 27` 77 800 impresí, 4 643 kliků, pozice 2.0, CTR 5.97 %
- 9to5Mac RSS: "iOS 27 release date: Here's when the new iPhone update will launch", 25. 8. 20:45 UTC
- Manticore: jen starý článek `Kdy vyjde iOS 18.3`, žádný stejný intent pro iOS 27

Unique value: český harmonogram, zařízení, rizika bety, co si pohlídat před instalací.

### 2. CREATE - WhatsApp security features

Candidate ID: LSA-WHATSAPP  
Exact topic: WhatsApp announces three account security features  
Proposed title: WhatsApp přidává tři novinky pro bezpečnější účet. Tohle si zapněte  
Primary lane: Current Demand  
Timing: po iOS 27 / odpoledne  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - no duplicate  
Opportunity score: 78  
Predictive score: 66  
Confidence: MEDIUM  
Final write gate: PASS

Evidence:
- 9to5Mac RSS: 25. 8. 20:10 UTC
- GSC LSA: `whatsapp` 173 406 impresí, pozice 5.2
- Manticore: no duplicate

Unique value: prakticky popsat tři bezpečnostní novinky, co si uživatel má zapnout a co je jen informativní změna. Cross-platform téma, ale LSA dává smysl kvůli velké poptávce.

### 3. FOLLOW-UP - Mac mini M6

Candidate ID: LSA-MACMINI  
Exact topic: New Mac mini with M6 and M5 Pro  
Proposed title: Nový Mac mini s M6: co doplnit po prvním vydání  
Primary lane: Current Demand  
Timing: jen pokud je redakčně užitečné doplnění  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - same intent published 2026-08-25, follow-up only  
Opportunity score: 74  
Predictive score: 62  
Confidence: HIGH  
Final write gate: PASS jen jako FOLLOW-UP, ne CREATE

Evidence:
- Apple Newsroom 25. 8.
- 9to5Mac a GSMArena pokrytí
- Manticore našel LSA článek z 25. 8.

Unique value: nepsat duplicitu. Doplnit jen nové technické detaily, dostupnost, český kontext nebo navazující výklad.

## Drop / Monitor pro LSA

- Mac Studio M5 Max / M5 Ultra: DROP jako nový článek. Manticore našel publikovaný článek z 25. 8.; možný jen technický follow-up, pokud redakce má nové informace.
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

