# Letem světem Applem - research rerun 26. 8. 2026

Status: čerstvý rerun po požadavku Toma. DATA GATE prošel živě v 8:50 CEST.

Web: letemsvetemapplem.eu  
Priorita: Discover-first + Apple Search demand  
Publikace: pouze po schválení Romana nebo Toma

## Data Gate

- GA4: PASS
- GSC: PASS
- Manticore: PASS
- WordPress read/auth: PASS
- Google Trends: CHECKED přes pytrends fallback
- GitHub: CHECKED read-only, bez silného LSA user-impact signálu

## Doporučené pořadí

1. CREATE - iOS 27 release date
2. CREATE - WhatsApp account security
3. UPDATE/FOLLOW-UP - Mac mini M6, pouze doplnění existujícího článku

## Sloty

### 1. CREATE - iOS 27 release date

Candidate ID: LSA-RR-260826-IOS27  
Exact topic: kdy vyjde iOS 27 a kdy Apple pravděpodobně oznámí ostrý release  
Proposed title: Kdy vyjde iOS 27: očekávaný termín vydání a co hlídat  
Primary lane: SEO  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - Manticore našel jen starý článek `Kdy vyjde iOS 18.3`, ne stejný iOS 27 intent  
Opportunity score: 86  
Predictive score: 78  
Confidence: HIGH  
Final write gate: PASS

Evidence:
- GSC LSA 28 dní: `ios 27` 68 805 impresí, 4 158 kliků, pozice 2.0, CTR 6.0 %
- GSC LSA: `kdy vyjde ios 27` 488 impresí, 98 kliků, pozice 2.3, CTR 20.1 %
- 9to5Mac 25.8.: iOS 27 public release očekávaný v září, pravděpodobně kolem pondělí 14.9.; oficiální datum obvykle na iPhone eventu
- Trends CZ: slabý, ale existující signál (`ios 27` max 14/100); GSC je hlavní důkaz

Unique value: český harmonogram, rozdíl beta vs. ostrá verze, podporované iPhony, co udělat před instalací, jasně označit odhad jako odhad.

### 2. CREATE - WhatsApp account security

Candidate ID: LSA-RR-260826-WHATSAPP  
Exact topic: WhatsApp přidal silnější dvoufázové ověření, víc passkeys a kontext u neznámých hovorů  
Proposed title: WhatsApp přidává tři bezpečnostní novinky. Tohle si zkontrolujte hned  
Primary lane: Current Demand  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - Manticore no duplicate pro WhatsApp security/passkeys intent  
Opportunity score: 82  
Predictive score: 70  
Confidence: HIGH  
Final write gate: PASS

Evidence:
- Official Meta / WhatsApp 25.8.: full password pro two-step verification, více passkeys na účet, Android kontext u neznámých hovorů
- 9to5Mac 25.8. potvrzuje stejné tři funkce
- GSC LSA 28 dní: `whatsapp` 173 406 impresí, pozice 5.2; `whatsapp web` 255 397 impresí, pozice 5.6
- Trends CZ pytrends: `whatsapp` max 100/100, poslední nenulový bod 92

Unique value: praktický checklist co si zapnout, co je pouze pro Android, co platí pro iPhone, jak neplést passkey s heslem.

### 3. UPDATE/FOLLOW-UP - Mac mini M6

Candidate ID: LSA-RR-260826-MACMINI  
Exact topic: Mac mini M6 a M5 Pro - Wi-Fi 7, Bluetooth 6, 2.5Gb Ethernet, dostupnost a ceny  
Proposed title: Nový Mac mini M6 má Wi-Fi 7 a vyšší cenu. Co doplnit po představení  
Primary lane: Current Demand  
Reality status: PASS  
Information age: FRESH  
WP check: CHECKED - LSA už má článek z 25.8. `Apple právě představil nový Mac mini...`  
Opportunity score: 74  
Predictive score: 63  
Confidence: HIGH  
Final write gate: PASS jen jako UPDATE/FOLLOW-UP, ne CREATE

Evidence:
- Apple Newsroom 25.8.: Mac mini M6/M5 Pro, Wi-Fi 7, Bluetooth 6, 2.5Gb Ethernet, dostupnost od 22.9.
- MacRumors 25.8.: ceny od $899 / $1 699, předobjednávky běží
- GSC LSA: `mac mini` 4 510 impresí, pozice 12.8; `mac mini m6` 2 192 impresí, pozice 8.0
- Trends CZ: `mac mini` max 41/100

Unique value: doplnit existující článek o cenu, dostupnost, Wi-Fi 7/Bluetooth 6, rozdíl M6 vs. M5 Pro. Nepsat nový duplicitní článek.

## Drop / Monitor

- Mac Studio M5 Max/M5 Ultra: DROP jako CREATE. LSA má článek z 25.8. `Mac Studio M5 Ultra`; možný jen UPDATE.
- Wi-Fi 7 u nových Maců: ne samostatně, jen jako update k Mac mini/Mac Studio.

## Source Coverage Audit

- WordPress/Manticore: CHECKED
- GSC: CHECKED live, 28denní query data
- GA4: CHECKED live, 7denní top pages
- Google Trends: CHECKED přes pytrends
- Major tech media: CHECKED - 9to5Mac, MacRumors
- Official newsrooms/docs: CHECKED - Apple Newsroom, Meta/WhatsApp
- GitHub: CHECKED read-only, no LSA shortlist
- Reddit/X/YouTube/community: NOT CHECKED - bez přímé vrstvy v tomto rerunu

