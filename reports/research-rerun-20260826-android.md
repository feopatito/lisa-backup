# Android Magazine - research rerun 26. 8. 2026

Status: čerstvý rerun po požadavku Toma. DATA GATE prošel živě v 8:50 CEST.

Web: androidmagazine.eu  
Priorita: Android / Google / Pixel, mix Search + Discover  
Publikace: pouze po schválení Romana nebo Toma

## Data Gate

- GA4: PASS
- GSC: PASS
- Manticore: PASS
- WordPress read/auth: PASS
- Google Trends: CHECKED přes pytrends fallback
- GitHub: CHECKED read-only, bez kvalifikovaného user-impact slotu

## Doporučené pořadí

1. CREATE - Android Pulse explainery
2. CREATE - Google Play App Bundles / August System Updates
3. MONITOR/UPDATE - Pixel 11 post-launch deals, ne nový článek bez CZ relevance

## Sloty

### 1. CREATE - Android Pulse

Candidate ID: AND-RR-260826-PULSE  
Exact topic: Android Pulse jako Google system service, proč se objevuje v Google Play a jestli je bezpečný  
Proposed title: V Google Play se objevuje Android Pulse. Co to je a proč ho nemažte  
Primary lane: Discovery  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - Manticore nenašel stejný Android Pulse intent; vrácené výsledky jsou obecné Pixel/Android články  
Opportunity score: 68  
Predictive score: 73  
Confidence: MEDIUM  
Final write gate: PASS

Evidence:
- 9to5Google 25.8. update: Google potvrdil, že Android Pulse je Google system service
- Play Store popis: pravidla pro anomaly detection v kritické spotřebě systémových prostředků
- 9to5Google uvádí 10M+ instalací a že zobrazení v Play Storu bylo omylem/viditelnostní změna
- Trends CZ: slabé (`android pulse` max 17/100, aktuálně 0) - Discovery, ne Search
- GA4 Android: praktické Android explainery fungují, např. `/android-notification/` 57 sessions za 7 dní

Unique value: uklidnit uživatele, že nejde o malware; vysvětlit, kde službu najde, co nedělat, a že nemá běžné uživatelské rozhraní.

### 2. CREATE - Google Play App Bundles / System Updates

Candidate ID: AND-RR-260826-GPLAY-BUNDLES  
Exact topic: Google Play Store v52.9 přidává App Bundles a další změny v srpnových Google System Updates  
Proposed title: Google Play nabídne balíčky aplikací. Srpnové systémové aktualizace přidávají i lepší ochranu  
Primary lane: Current Demand + SEO  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - Manticore našel jen starý článek z 2024 o instalaci mimo obchod Play; ne stejný App Bundles intent  
Opportunity score: 66  
Predictive score: 68  
Confidence: MEDIUM  
Final write gate: PASS

Evidence:
- Google Support official release notes: Google Play Store v52.9 (2026-08-24) přidává App Bundles, video highlights v Ask Play, lepší Play Protect detekci a další položky
- 9to5Google 24.8. přebírá a vysvětluje August 2026 Google System Updates
- Trends CZ: `google play` max 100/100, poslední nenulový bod 40
- GSC Android: Google Play refund queries mají malé objemy, ale web má existující Google Play topical footprint
- GA4 Android: `/2026/08/20/google-system-updates/` 51 sessions za 7 dní

Unique value: vytáhnout z dlouhého changelogu jen věci pro běžného uživatele, ne developer noise; jasně říct, že rollout může být postupný.

### 3. MONITOR/UPDATE - Pixel 11 post-launch deals

Candidate ID: AND-RR-260826-PIXEL11-DEALS  
Exact topic: Pixel 11 post-launch offers and Pixel Watch 5 bundled deals  
Proposed title: Pixel 11 má poslední launch nabídky. Co z toho má smysl sledovat v Evropě  
Primary lane: Current Demand  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - Android Magazine už má Pixel 11 a Pixel Watch 5 pokrytí z 11.-21.8.  
Opportunity score: 58  
Predictive score: 56  
Confidence: MEDIUM  
Final write gate: PASS jen jako UPDATE/MONITOR, ne CREATE bez CZ dostupnosti

Evidence:
- 9to5Google 25.8.: US Google Store launch deals končí 27.8.; Amazon/Best Buy gift cards a trade-in stacking
- GSC Android: `pixel 11` 52 impresí, pozice 44.3; `google pixel 11` 42 impresí, pozice 58.0
- Trends CZ: `pixel 11` max 61/100, poslední nenulový bod 40
- Manticore: existují Pixel 11 / Pixel Watch 5 články, nejde o čistý CREATE

Unique value: zatím nepsat nový článek na US slevy. Udržet jako monitor nebo update existujícího Pixel 11 coverage, až bude CZ/EU dostupnost nebo cena ověřená.

## Drop / Monitor

- Android 17 memory limits: MONITOR. V tomto rerunu se nepodařilo ověřit nový primární Android Developers zdroj.
- Pixel 11 dostupnost/ceny: bez ověřené CZ/EU ceny nepsat jako nový článek.

## Source Coverage Audit

- WordPress/Manticore: CHECKED
- GSC: CHECKED live, 28denní query data
- GA4: CHECKED live, 7denní top pages
- Google Trends: CHECKED přes pytrends
- Major tech media: CHECKED - 9to5Google, PhoneArena/Cybernews jako sekundární cross-check
- Official docs: CHECKED - Google System Services release notes
- GitHub: CHECKED read-only - Gemini CLI/Perfetto bez běžného user-impact slotu
- Reddit/X/YouTube/community: NOT CHECKED - bez přímé vrstvy v tomto rerunu

