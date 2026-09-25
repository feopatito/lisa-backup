# Android Magazine - redakční plán 26. 8. 2026

Status: opožděný recovery výstup po ranním heartbeat triggeru. Pre-flight prošel živě v 7:13 CEST.

Web: androidmagazine.eu  
Priorita webu: Android / Google / Pixel, mix Search + Discover  
Publikace: pouze po schválení Romana nebo Toma

## Data Gate

- GA4: PASS
- GSC: PASS
- Manticore: PASS
- WordPress auth/read: PASS
- Google Trends: UNAVAILABLE - JustSerpAPI vracel `code=500`, nenahrazuji odhadem

## Doporučené pořadí

1. CREATE - Android Pulse
2. CREATE - Pixel 11 availability

## Sloty

### 1. CREATE - Android Pulse

Candidate ID: AND-PULSE  
Exact topic: Android Pulse app in Google Play Store updates  
Proposed title: V Google Play se objevuje Android Pulse. Co to je a proč si toho všimnout  
Primary lane: Discovery  
Timing: dopoledne  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - no duplicate  
Opportunity score: 68  
Predictive score: 74  
Confidence: MEDIUM  
Final write gate: PASS

Evidence:
- 9to5Google RSS: "What is the 'Android Pulse' app that just appeared in Google Play Store updates?", 26. 8. 02:25 UTC
- Manticore Android: no duplicate
- GA4 Android: fungují praktické Android explainery (`android-notification`, `google-system-updates`, `pixel-google`)

Unique value: vysvětlit, jestli uživatel musí něco dělat, jak poznat legitimní Google komponentu a kdy článek aktualizovat podle dalšího potvrzení.

### 2. CREATE - Pixel 11 availability

Candidate ID: AND-PIXEL11  
Exact topic: Pixel 11 phones and Pixel Watch 5 official availability  
Proposed title: Pixel 11 je oficiálně v prodeji. Google zároveň spouští Pixel Watch 5  
Primary lane: Current Demand  
Timing: po Android Pulse  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - no duplicate  
Opportunity score: 71  
Predictive score: 69  
Confidence: MEDIUM  
Final write gate: PASS

Evidence:
- Google Blog 25. 8. 20:00 UTC
- Manticore Android: no duplicate

Unique value: držet se dostupnosti a oficiálních informací, nepsat českou cenu bez ověření. Přidat praktický kontext pro českého čtenáře: kde je produkt relevantní, co je globální oznámení a co zatím není potvrzené pro CZ.

## Monitor pro Android Magazine

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

