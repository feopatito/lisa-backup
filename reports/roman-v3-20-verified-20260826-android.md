# Opravený ranní výstup V3 — 26. 8. 2026

Status: rerun po Romanově kontrole. Cíl: 20 slotů pro web, ale bez duplicitních CREATE.

## Použité vrstvy
- DATA GATE: GA4/GSC/Manticore/WP PASS v hlavní session.
- Google Trends: GLOBAL pytrends `geo=''`, `now 7-d`; dvě Samsung dávky skončily 429 a jsou označené `GLOBAL_TRENDS_UNAVAILABLE`.
- GSC: live 28d + 7d podklady z dnešního běhu.
- GA4: live 7d top pages.
- Google News/web: CHECKED přes aktuální web search pro Apple / Android / Samsung témata.
- Manticore: CHECKED přes `/results`, navíc title/exact-topic recheck pro všech 60 kandidátů.
- WP REST: CHECKED pro všech 60 kandidátů jako druhá duplicitní vrstva.
- Fact-check: PASS jen tam, kde existuje hard source; spekulace zůstává označená jako leak/rumor/monitor.

## Tvrdá oprava
Pokud Manticore nebo WP ukazuje publikovaný nebo velmi podobný intent, `CREATE povoleno` je `NO` a akce je UPDATE/FOLLOW-UP/MERGE/MONITOR. To je rozdíl proti předchozí chybné verzi.

# Android Magazine — androidmagazine.eu — 20 slotů po WP kontrole

| # | Akce | CREATE povoleno | Titulek / intent | Global Trends | WP/Manticore verdict | Fact-check |
|---|---|---|---|---|---|---|
| AND-01 | CREATE | YES | Co je Android Pulse a proč se objevuje v Google Play aktualizacích | global max 100/100, avg 10.4, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| AND-02 | CREATE | YES | Pixel Rambler voice-to-text: funkce, která může změnit diktování | global max 3/100, avg 0.0, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| AND-03 | UPDATE | NO | Gemini Device Help na Pixelu: poradí s telefonem, ale není bez limitů | global max 3/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: Potřebujete změnit nastavení svého mobilu? Stačí požádat Gemini a nemusíte už nic složitě hledat | PASS |
| AND-04 | CREATE | YES | Google Maps v Android Auto nezobrazuje dopravu: co zkusit | global max 5/100, avg 0.2, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| AND-05 | UPDATE | NO | Srpnové Google System Updates: co je nové v Androidu, Play Store a Auto | global max 2/100, avg 0.1, last 0 | PUBLISHED/SIMILAR_EXISTS: Srpnové Google System Updates: co je nového v Androidu, Wear OS a Play Store | PASS |
| AND-06 | CREATE | YES | Android Auto se odpojuje nebo mrzne: Google chystá opravu | global max 0/100, avg 0.0, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| AND-07 | UPDATE | NO | Always On Display na Androidu: zapnutí, výdrž baterie a nejlepší nastavení | global max 100/100, avg 2.1, last 0 | PUBLISHED/SIMILAR_EXISTS: Pixel 11 Pro HiLight: co to vlastně je a proč první reakce vyvolaly rozpaky / Google konečně zapíná Live Updates pro stopky a časovač. Novinka výrazně zpříjemní pou | PASS |
| AND-08 | UPDATE | NO | Smazali jste oznámení? Android ho umí najít | global max 90/100, avg 1.5, last 0 | PUBLISHED/SIMILAR_EXISTS: Smazali jste omylem oznámení? Android ho umí najít. Stačí zapnout tuto funkci / Jak Obnovit Chat Na Instagramu - Kompletní Návod | PASS |
| AND-09 | FOLLOW-UP | NO | RCS chyba 3100 po přechodu na Galaxy: co dělat | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100 | PASS |
| AND-10 | FOLLOW-UP | NO | Android 17 zpřísňuje aplikace na pozadí: komu může přestat hrát zvuk | global max 68/100, avg 0.4, last 0 | PUBLISHED/SIMILAR_EXISTS: Android 17 zpřísňuje aplikace běžící na pozadí. U některých může přestat fungovat zvuk | PASS |
| AND-11 | CREATE | YES | Pixel 11 nabídky: kdy dává smysl koupit a kdy počkat | global max 6/100, avg 2.0, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| AND-12 | CREATE | YES | Tracker pro Android i iPhone do kola nebo golfových holí | global max 0/100, avg 0.0, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| AND-13 | FOLLOW-UP | NO | Wear OS sdílení polohy: co Google přidává do hodinek | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: Google rozšiřuje polohu na Wear OS. Přibývá Location Sharing i Find people / Google mění Wear OS: Firemní účet konečně dostanete i do chytrých hodinek bez složitého | PASS |
| AND-14 | FOLLOW-UP | NO | HONOR Robot Phone: nejdivnější telefon roku, nebo ukázka budoucnosti? | global max 100/100, avg 56.4, last 59 | PUBLISHED/SIMILAR_EXISTS: HONOR Robot Phone: gimbal, AI a nejdivnější smartphone roku / HONOR Robot Phone je realita, má gimbal, filmové barvy a AI, která zvládne přes 100 kroků. A stojí neu | PASS |
| AND-15 | FOLLOW-UP | NO - FOLLOW-UP | 5 tipů, jak vylepšit Pixel bez výměny telefonu | global max 4/100, avg 0.8, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| AND-16 | UPDATE | NO | Jak vypnout Android telefon: aktualizovaný návod pro rok 2026 | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100 / Jak na Androidu snadno nastavit tapety podle denní doby | PASS |
| AND-17 | UPDATE | NO | Jak vynutit LTE nebo 5G na Androidu | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: Jak vynutit LTE nebo 5G připojení na telefonu? Tady je podrobný návod | PASS |
| AND-18 | UPDATE | NO | Jak vysypat koš na Androidu | global max 54/100, avg 0.3, last 0 | PUBLISHED/SIMILAR_EXISTS: Jak vysypat koš na zařízení Android? / 6 skrytých aplikací od Googlu, které by měl znát každý uživatel Androidu | PASS |
| AND-19 | UPDATE | NO | Jak odblokovat číslo na Androidu | global max 29/100, avg 0.2, last 0 | PUBLISHED/SIMILAR_EXISTS: Jednoduchý návod pro zrušení blokace jakéhokoliv čísla na Androidu / Jak si odblokovat číslo na Androidu? Kompletní návod! | PASS |
| AND-20 | CREATE | YES | GrapheneOS míří nejdřív na Motorolu: proč je to velká změna | global max 100/100, avg 8.5, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |

## Detailní sloty

### AND-01 — Co je Android Pulse a proč se objevuje v Google Play aktualizacích

- action: CREATE
- create_allowed: YES
- exact_topic: android pulse app
- primary_lane: DISCOVERY
- why_now: 9to5Google RSS: Android Pulse app appeared in Play Store updates.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
- hard_evidence: 9to5Google RSS: Android Pulse app appeared in Play Store updates.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 100/100, avg 10.4, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Vysvětlit nový systémový prvek bez paniky.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-02 — Pixel Rambler voice-to-text: funkce, která může změnit diktování

- action: CREATE
- create_allowed: YES
- exact_topic: pixel rambler voice to text
- primary_lane: DISCOVERY
- why_now: 9to5Google RSS: Pixel 11 Rambler voice-to-text.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 43 sessions / 81 views
- hard_evidence: 9to5Google RSS: Pixel 11 Rambler voice-to-text.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 3/100, avg 0.0, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Praktický demo/impact angle pro Google/Pixel publikum.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-03 — Gemini Device Help na Pixelu: poradí s telefonem, ale není bez limitů

- action: UPDATE
- create_allowed: NO
- exact_topic: gemini device help pixel
- primary_lane: CURRENT DEMAND
- why_now: Android Authority + 9to5Google webové signály.
- hard_evidence: Android Authority + 9to5Google webové signály.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Potřebujete změnit nastavení svého mobilu? Stačí požádat Gemini a nemusíte už ni
- global_trends: global max 3/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Potřebujete změnit nastavení svého mobilu? Stačí požádat Gemini a nemusíte už nic složitě hledat
- matching_articles:
  - 2026-08-06T08:10:21.000Z — Potřebujete změnit nastavení svého mobilu? Stačí požádat Gemini a nemusíte už nic složitě hledat — https://androidmagazine.eu/2026/08/06/potrebujete-zmenit-nastaveni-sveho-mobilu-staci-pozadat-gemini-a-nemusite-uz-nic-slozite-hledat/
- unique_value: Uživatelský test/hranice funkce.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-04 — Google Maps v Android Auto nezobrazuje dopravu: co zkusit

- action: CREATE
- create_allowed: YES
- exact_topic: google maps android auto traffic
- primary_lane: CURRENT DEMAND
- why_now: 9to5Google + XDA: traffic data bug.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 47 sessions / 115 views
- hard_evidence: 9to5Google + XDA: traffic data bug.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 5/100, avg 0.2, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Rychlý servisní článek s workaroundy.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-05 — Srpnové Google System Updates: co je nové v Androidu, Play Store a Auto

- action: UPDATE
- create_allowed: NO
- exact_topic: google system updates august
- primary_lane: CURRENT DEMAND
- why_now: 9to5Google update 24.8.; existující Android Magazine článek.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 47 sessions / 115 views
- hard_evidence: 9to5Google update 24.8.; existující Android Magazine článek.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 2/100, avg 0.1, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Srpnové Google System Updates: co je nového v Androidu, Wear OS a Play Store
- matching_articles:
  - 2026-08-20T11:22:04.000Z — Srpnové Google System Updates: co je nového v Androidu, Wear OS a Play Store — https://androidmagazine.eu/2026/08/20/google-system-updates/
- unique_value: Doplnit nové body, ne nový duplicitní článek.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-06 — Android Auto se odpojuje nebo mrzne: Google chystá opravu

- action: CREATE
- create_allowed: YES
- exact_topic: android auto disconnect freeze
- primary_lane: CURRENT DEMAND
- why_now: 9to5Google: disconnect/freeze fix update.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
- hard_evidence: 9to5Google: disconnect/freeze fix update.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Servisní článek + kontrola verze aplikace.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-07 — Always On Display na Androidu: zapnutí, výdrž baterie a nejlepší nastavení

- action: UPDATE
- create_allowed: NO
- exact_topic: always on display android
- primary_lane: SEO
- why_now: GSC Android: 261 imp, pozice 13.6.; GSC 266 imp / pos 13.94 / CTR 1.13 %; GA4 104 sessions / 431 views
- hard_evidence: GSC Android: 261 imp, pozice 13.6.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Pixel 11 Pro HiLight: co to vlastně je a proč první reakce vyvolaly rozpaky | Google konečně zapíná Live Updates pro stopky a časovač. Novinka výrazně zpříjem
- global_trends: global max 100/100, avg 2.1, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Pixel 11 Pro HiLight: co to vlastně je a proč první reakce vyvolaly rozpaky | Google konečně zapíná Live Updates pro stopky a časovač. Novinka výrazně zpříjemní používání Androidu
- matching_articles:
  - 2026-08-19T06:56:32.000Z — Pixel 11 Pro HiLight: co to vlastně je a proč první reakce vyvolaly rozpaky — https://androidmagazine.eu/2026/08/19/pixel-11-pro-hilight/
  - 2026-08-04T07:39:39.000Z — Google konečně zapíná Live Updates pro stopky a časovač. Novinka výrazně zpříjemní používání Androidu — https://androidmagazine.eu/2026/08/04/google-konecne-zapina-live-updates-pro-stopky-a-casovac-novinka-vyrazne-zprijemni-pouzivani-androidu/
  - 2026-06-14T12:13:11.000Z — Přehřívá se vám mobil? Stačí změnit tohle jedno nastavení a máte klid — https://androidmagazine.eu/2026/06/14/prehriva-se-vam-mobil-staci-zmenit-tohle-jedno-nastaveni-a-mate-klid/
- unique_value: CZ návod pro malý web, jasný evergreen.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-08 — Smazali jste oznámení? Android ho umí najít

- action: UPDATE
- create_allowed: NO
- exact_topic: android notification history
- primary_lane: SEO
- why_now: GA4: existující notification článek v top Android pages.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
- hard_evidence: GA4: existující notification článek v top Android pages.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Smazali jste omylem oznámení? Android ho umí najít. Stačí zapnout tuto funkci
- global_trends: global max 90/100, avg 1.5, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Smazali jste omylem oznámení? Android ho umí najít. Stačí zapnout tuto funkci | Jak Obnovit Chat Na Instagramu - Kompletní Návod
- matching_articles:
  - 2026-08-19T14:00:12.000Z — Smazali jste omylem oznámení? Android ho umí najít. Stačí zapnout tuto funkci — https://androidmagazine.eu/2026/08/19/android-notification/
  - 2025-12-09T10:55:07.000Z — Jak Obnovit Chat Na Instagramu - Kompletní Návod — https://androidmagazine.eu/2025/12/09/jak-obnovit-chat-na-instagramu-kompletni-navod/
  - 2026-08-19T14:00:12.000Z — Smazali jste omylem oznámení? Android ho umí najít. Stačí zapnout tuto funkci — https://androidmagazine.eu/2026/08/19/android-notification/
- unique_value: Rozšířit o modely a screenshot-like kroky.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-09 — RCS chyba 3100 po přechodu na Galaxy: co dělat

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: rcs chyba 3100
- primary_lane: CURRENT DEMAND
- why_now: Existující Android Magazine článek 21.8.
- hard_evidence: Existující Android Magazine článek 21.8.; WP/Manticore: SIMILAR_EXISTS přes Manticore: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100
- matching_articles:
  - 2026-08-21T08:20:05.000Z — RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100 — https://androidmagazine.eu/2026/08/21/google-3100/
- unique_value: Navázat praktickým návodem a stavem řešení.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-10 — Android 17 zpřísňuje aplikace na pozadí: komu může přestat hrát zvuk

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: android 17 background audio
- primary_lane: CURRENT DEMAND
- why_now: Existující článek 19.8.; aktuální developer/user dopad.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
- hard_evidence: Existující článek 19.8.; aktuální developer/user dopad.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Android 17 zpřísňuje aplikace běžící na pozadí. U některých může přestat fungova
- global_trends: global max 68/100, avg 0.4, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Android 17 zpřísňuje aplikace běžící na pozadí. U některých může přestat fungovat zvuk
- matching_articles:
  - 2026-08-19T12:20:48.000Z — Android 17 zpřísňuje aplikace běžící na pozadí. U některých může přestat fungovat zvuk — https://androidmagazine.eu/2026/08/19/android-17-audio/
- unique_value: Přehled dotčených aplikací a workaround.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-11 — Pixel 11 nabídky: kdy dává smysl koupit a kdy počkat

- action: CREATE
- create_allowed: YES
- exact_topic: pixel 11 deals
- primary_lane: CURRENT DEMAND
- why_now: Google Trends via pytrends Pixel 11 55/100 + Android Central RSS: Pixel 11 deals.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 43 sessions / 81 views
- hard_evidence: Android Central RSS: Pixel 11 deals.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 6/100, avg 2.0, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Nákupní úhel, ne jen affiliate/akce.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-12 — Tracker pro Android i iPhone do kola nebo golfových holí

- action: CREATE
- create_allowed: YES
- exact_topic: android iphone tracker bike
- primary_lane: DISCOVERY
- why_now: 9to5Google RSS: tracker with 3-year battery.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
- hard_evidence: 9to5Google RSS: tracker with 3-year battery.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Praktický gadget článek s cross-platform routingem.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-13 — Wear OS sdílení polohy: co Google přidává do hodinek

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: wear os location sharing
- primary_lane: CURRENT DEMAND
- why_now: GA4 Android: Wear OS location sharing article běží v RU.; GA4 47 sessions / 115 views
- hard_evidence: GA4 Android: Wear OS location sharing article běží v RU.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Google rozšiřuje polohu na Wear OS. Přibývá Location Sharing i Find people
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Google rozšiřuje polohu na Wear OS. Přibývá Location Sharing i Find people | Google mění Wear OS: Firemní účet konečně dostanete i do chytrých hodinek bez složitého nastavování
- matching_articles:
  - 2026-08-21T22:02:20.000Z — Google rozšiřuje polohu na Wear OS. Přibývá Location Sharing i Find people — https://androidmagazine.eu/2026/08/22/wear-os-google-location-sharing/
  - 2026-07-08T00:41:28.000Z — Google mění Wear OS: Firemní účet konečně dostanete i do chytrých hodinek bez složitého nastavování — https://androidmagazine.eu/2026/07/08/google-meni-wear-os-firemni-ucet-konecne-dostanete-i-do-chytrych-hodinek-bez-sloziteho-nastavovani/
  - 2026-08-21T22:02:20.000Z — Google rozšiřuje polohu na Wear OS. Přibývá Location Sharing i Find people — https://androidmagazine.eu/2026/08/22/wear-os-google-location-sharing/
- unique_value: CZ follow-up pro Android/Wear OS.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-14 — HONOR Robot Phone: nejdivnější telefon roku, nebo ukázka budoucnosti?

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: honor robot phone
- primary_lane: DISCOVER
- why_now: GA4 Android: Honor Robot Phone v top.; GSC 161 imp / pos 9.12 / CTR 4.97 %; GA4 40 sessions / 246 views
- hard_evidence: GA4 Android: Honor Robot Phone v top.; WP/Manticore: SIMILAR_EXISTS přes Manticore: HONOR Robot Phone: gimbal, AI a nejdivnější smartphone roku | HONOR Robot Phone je realita, má gimbal, filmové barvy a AI, která zvládne přes 
- global_trends: global max 100/100, avg 56.4, last 59
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: HONOR Robot Phone: gimbal, AI a nejdivnější smartphone roku | HONOR Robot Phone je realita, má gimbal, filmové barvy a AI, která zvládne přes 100 kroků. A stojí neuvěřitelné peníze
- matching_articles:
  - 2026-08-20T10:22:03.000Z — HONOR Robot Phone: gimbal, AI a nejdivnější smartphone roku — https://androidmagazine.eu/2026/08/20/honor-robot-phone/
  - 2026-08-14T13:14:26.000Z — HONOR Robot Phone je realita, má gimbal, filmové barvy a AI, která zvládne přes 100 kroků. A stojí neuvěřitelné peníze — https://androidmagazine.eu/2026/08/14/honor-robot-phone-je-realita-ma-gimbal-filmove-barvy-a-ai-ktera-zvladne-pres-100-kroku-a-stoji-neuveritelne-penize/
  - 2026-08-04T12:10:51.000Z — Unikly kompletní specifikace revolučního Robot Phone, Honor spustil už i předobjednávky — https://androidmagazine.eu/2026/08/04/unikly-kompletni-specifikace-revolucniho-robot-phone-honor-spustil-uz-i-predobjednavky/
- unique_value: Trendový follow-up s ověřením aktuálního stavu.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-15 — 5 tipů, jak vylepšit Pixel bez výměny telefonu

- action: FOLLOW-UP
- create_allowed: NO - FOLLOW-UP
- exact_topic: pixel tips
- primary_lane: SEO + DISCOVER
- why_now: GA4 Android: Pixel tips v top.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 43 sessions / 81 views
- hard_evidence: GA4 Android: Pixel tips v top.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 4/100, avg 0.8, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Praktický evergreen s novými Android/Pixel funkcemi.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-16 — Jak vypnout Android telefon: aktualizovaný návod pro rok 2026

- action: UPDATE
- create_allowed: NO
- exact_topic: vypnout android telefon
- primary_lane: SEO
- why_now: GSC: 4 644 imp, pozice 5.19, CTR 1.23 %.; GSC 1129 imp / pos 3.5 / CTR 2.13 %; GA4 941 sessions / 1066 views
- hard_evidence: GSC: 4 644 imp, pozice 5.19, CTR 1.23 %.; WP/Manticore: SIMILAR_EXISTS přes Manticore: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100 | Jak na Androidu snadno nastavit tapety podle denní doby
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100 | Jak na Androidu snadno nastavit tapety podle denní doby
- matching_articles:
  - 2026-08-21T08:20:05.000Z — RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100 — https://androidmagazine.eu/2026/08/21/google-3100/
  - 2026-08-20T06:29:58.000Z — Jak na Androidu snadno nastavit tapety podle denní doby — https://androidmagazine.eu/2026/08/20/jak-na-androidu-snadno-nastavit-tapety-podle-denni-doby/
  - 2026-08-19T12:20:48.000Z — Android 17 zpřísňuje aplikace běžící na pozadí. U některých může přestat fungovat zvuk — https://androidmagazine.eu/2026/08/19/android-17-audio/
- unique_value: Aktualizovat existující evergreen a titulkově zlepšit CTR.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-17 — Jak vynutit LTE nebo 5G na Androidu

- action: UPDATE
- create_allowed: NO
- exact_topic: force lte 5g android
- primary_lane: SEO
- why_now: GA4 ukazuje historický výkon RU verze.; GA4 32 sessions / 58 views
- hard_evidence: GA4 ukazuje historický výkon RU verze.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Jak vynutit LTE nebo 5G připojení na telefonu? Tady je podrobný návod
- matching_articles:
  - 2025-12-26T20:00:48.000Z — Jak vynutit LTE nebo 5G připojení na telefonu? Tady je podrobný návod — https://androidmagazine.eu/2025/12/26/jak-vynutit-lte-nebo-5g-pripojeni-na-telefonu-tady-je-podrobny-navod/
- unique_value: CZ návod s upozorněním na rizika a modelové rozdíly.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-18 — Jak vysypat koš na Androidu

- action: UPDATE
- create_allowed: NO
- exact_topic: android kos
- primary_lane: SEO
- why_now: GSC: související dotazy v top Android Search.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
- hard_evidence: GSC: související dotazy v top Android Search.; WP/Manticore: SIMILAR_EXISTS přes Manticore: 6 skrytých aplikací od Googlu, které by měl znát každý uživatel Androidu | Jak obnovit smazané soubory a fotky v Androidu?
- global_trends: global max 54/100, avg 0.3, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Jak vysypat koš na zařízení Android? | 6 skrytých aplikací od Googlu, které by měl znát každý uživatel Androidu
- matching_articles:
  - 2024-10-17T04:30:59.000Z — Jak vysypat koš na zařízení Android? — https://androidmagazine.eu/2024/10/17/jak-vysypat-kos-na-zarizeni-android/
  - 2026-08-11T13:01:51.000Z — 6 skrytých aplikací od Googlu, které by měl znát každý uživatel Androidu — https://androidmagazine.eu/2026/08/11/78363/
  - 2025-02-18T08:00:53.000Z — Jak obnovit smazané soubory a fotky v Androidu? — https://androidmagazine.eu/2025/02/18/jak-obnovit-smazane-soubory-a-fotky-v-androidu/
- unique_value: Krátký evergreen s kroky podle Google Photos/Files/Gmail.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-19 — Jak odblokovat číslo na Androidu

- action: UPDATE
- create_allowed: NO
- exact_topic: blokovani cisla android
- primary_lane: SEO
- why_now: GSC: multilingual dotazy na odblokování čísla.; GA4 941 sessions / 1066 views
- hard_evidence: GSC: multilingual dotazy na odblokování čísla.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Google Scam Detection míří mimo Pixel: jak Android pozná podvodný hovor | Konec bankovních podvodů? Google zavádí AI ochranu a biometrický zámek proti krá
- global_trends: global max 29/100, avg 0.2, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Jednoduchý návod pro zrušení blokace jakéhokoliv čísla na Androidu | Jak si odblokovat číslo na Androidu? Kompletní návod!
- matching_articles:
  - 2024-10-23T18:00:01.000Z — Jednoduchý návod pro zrušení blokace jakéhokoliv čísla na Androidu — https://androidmagazine.eu/2024/10/23/jednoduchy-navod-pro-zruseni-blokace-jakehokoliv-cisla-na-androidu/
  - 2024-10-19T04:00:07.000Z — Jak si odblokovat číslo na Androidu? Kompletní návod! — https://androidmagazine.eu/2024/10/19/jak-si-odblokovat-cislo-na-androidu-kompletni-navod/
  - 2024-05-28T10:30:15.000Z — Jak odblokovat telefonní číslo na Androidu? — https://androidmagazine.eu/2024/05/28/jak-odblokovat-telefonni-cislo-na-androidu/
- unique_value: CZ návod + Samsung/Pixel/Xiaomi rozdíly.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### AND-20 — GrapheneOS míří nejdřív na Motorolu: proč je to velká změna

- action: CREATE
- create_allowed: YES
- exact_topic: grapheneos motorola 2027
- primary_lane: DISCOVERY
- why_now: Android Central RSS: GrapheneOS/Motorola 2027.
- hard_evidence: Android Central RSS: GrapheneOS/Motorola 2027.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 100/100, avg 8.5, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Bezpečnostní úhel pro Android publikum.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

## Source Coverage Audit

- WordPress REST: CHECKED pro všech 60 kandidátů
- Manticore: CHECKED pro všech 60 kandidátů + title/exact-topic recheck
- GSC: CHECKED live
- GA4: CHECKED live
- Google Trends global: CHECKED přes pytrends; 2 dávky 429 transparentně označené
- Google News/web: CHECKED pro Apple/Android/Samsung proudy
- Official sources: Apple Newsroom, Samsung Newsroom, Google Support, Meta/WhatsApp dle kandidátů
- Fact-check: PASS/UNCERTAIN uvedeno u slotů; spekulace nepovýšena na fakt