# Android Magazine — androidmagazine.eu — 20 článků na dnešní den

# Trend články na dnešní den — 26.8.2026
Interní redakční PDF pro Romana. Nejde o SEO top 50, ale o dnešní trendové články vybrané kombinací live GA4, GSC, Google Trends fallbacku, Manticore/WP kontroly a živých zdrojů.

## Datový stav
- GSC: CHECKED live, rozsah 28d `2026-07-27..2026-08-23`, poslední dostupný den kvůli zpoždění GSC `2026-08-23`.
- GA4: CHECKED live, `7daysAgo..today`, top stránky pro všechny 3 weby.
- Manticore/WP duplicate: CHECKED live přes `/results` pro všech 60 finálních intentů.
- Google Trends: JustSerpAPI primárně selhal (`500 Failed, retry later`), fallback pytrends: CHECKED (`now 7-d`, `CZ`).
- RSS/newsrooms: Apple Newsroom, MacRumors, 9to5Mac, 9to5Google, Android Central, SamMobile, Samsung Newsroom CHECKED; Android Authority RSS UNAVAILABLE, konkrétní Android Authority témata ověřena webovou vrstvou dříve.


## Google Trends via pytrends — přímý přístup, CZ, 7d
JustSerpAPI dnes nefunkční, proto použit povinný fallback pytrends. Hodnoty níže jsou konkrétní finální dotazy od Mouly, ne širší topic skupiny.

### LSA
- ChatGPT: 50/100 — potvrzuje dnešní LSA příležitost.
- WhatsApp: 26/100 — solidní sekundární trend, vhodný jen pokud bude aktuální hard source.
- iPhone 18: 10/100 — nízký CZ zájem teď, očekávaný růst po keynote 9.9.; dnes spíš příprava/servis než masivní CZ trend.
- Mac mini: 0/100 — držet kvůli official Apple Newsroom + LSA publiku, ne kvůli CZ Trends.
- iOS 27: 0/100 — bez trend momentum, pouze pokud existuje silný news hook.

### Samsung
- Samsung Galaxy S26: 0/100; One UI 9: 0/100; Galaxy Watch Ultra: 0/100; Gemini Samsung: 0/100.
- Interpretace: pro Samsung dnes rozhoduje GSC/GA4 + newsroom/RSS, ne CZ Google Trends.

### Android
- Pixel 11: 55/100 — potvrzuje Android/Pixel příležitost.
- Android Pulse: 0/100; Android tips: 0/100 — použít jen při silném news/GA4/GSC důvodu.

## Trend snapshot
### LSA
Top GSC dotazy: iphone 18 (680779 imp, pos 1.35); iphone 18 pro (241556 imp, pos 1.23); iphone 18 pro max (273604 imp, pos 1.25); iphone ultra (71011 imp, pos 1.55); iphone (724193 imp, pos 2.91); ios 27 (77800 imp, pos 2.0); letem světem applem (4444 imp, pos 1.12); apple watch ultra 4 (27231 imp, pos 2.52)
Pytrends CZ: iPhone avg 38.1 / max 100; Apple avg 18.8 / max 36; ChatGPT avg 20.2 / max 42; LEGO avg 19.1 / max 84; Mac mini avg 0.3 / max 5; iOS avg 20.3 / max 88; Apple Watch avg 33.1 / max 100; AirPods avg 29.9 / max 98; Apple Maps avg 0.0 / max 7; iCloud avg 13.2 / max 34

### Samsung
Top GSC dotazy: samsung (281731 imp, pos 3.89); エミュレータ (56017 imp, pos 1.13); ポケットモンスター 赤緑 (34729 imp, pos 1.26); one ui (135824 imp, pos 4.02); android auto (124797 imp, pos 5.04); samsung galaxy (222261 imp, pos 3.7); サムスン (51479 imp, pos 3.76); ニンテンドーds (38697 imp, pos 2.76)
Pytrends CZ: Samsung avg 45.6 / max 100; One UI avg 0.4 / max 6; Gemini avg 37.1 / max 57; Galaxy S26 avg 0.6 / max 4; Galaxy Watch avg 1.3 / max 4; Android Auto avg 15.2 / max 100; Google Wallet avg 5.0 / max 90; Galaxy AI avg 0.1 / max 15; Galaxy Buds avg 0.3 / max 21; Galaxy Z Fold avg 0.4 / max 30

### Android
Top GSC dotazy: vypnout telefon (1129 imp, pos 3.5); android magazin (37 imp, pos 10.16); android magazine (80 imp, pos 8.94); jak vypnout telefon (318 imp, pos 3.54); フィットネス用トラッカ (126 imp, pos 1); izklop telefona (94 imp, pos 1.66); odblokiranje številke (60 imp, pos 3.12); ako zistim svoje telefonne cislo (46 imp, pos 1.87)
Pytrends CZ: Android avg 28.6 / max 60; Google Maps avg 48.6 / max 88; Android Auto avg 2.3 / max 15; Pixel avg 16.8 / max 55; Gemini avg 65.5 / max 100; Wear OS avg 0.0 / max 0; Always On Display avg 0.1 / max 21; RCS avg 0.1 / max 11; HONOR avg 25.5 / max 100; GrapheneOS avg 0.0 / max 0


## Rerun correction 09:15
- DATA GATE byl znovu spuštěn po Romanově připomínce: GA4/GSC/Manticore/WP PASS pro všechny tři weby.
- GitHub vrstva byla dodatečně CHECKED read-only v hlavní session: Gemini CLI a Perfetto releases nalezeny, ale bez kvalifikovaného běžného user-impact slotu pro dnešní portfolio.
- Tento soubor obsahuje plných 20 slotů pro daný web, ne pouze top priority výběr.


# Android Magazine — androidmagazine.eu
Zdrojové signály: 9to5Google: What is the ‘Android Pulse’ app that just appeared in Google Play Store updates? [U]; The Fitbit Air would be S-tier if anyone made a band half as decent as Whoop’s; The Sideload 042: A genderless Pixel experience; Pixel 11’s ‘Rambler’ voice-to-text is a game-changer, but it should copy this feature [Video] | Android Central: Yep, One UI 9 Beta 6 is rolling out now on the Galaxy S26: here's what's in it; Waiting for GrapheneOS? Motorola's 2027 phones are up first, then it's on to foldables; My favorite writing tablet just scored a rare discount at Best Buy — but it won't last long

## AND-01. Co je Android Pulse a proč se objevuje v Google Play aktualizacích
```
candidate_id: AND-01
exact_topic: android pulse app
proposed_title: Co je Android Pulse a proč se objevuje v Google Play aktualizacích
action: CREATE
primary_lane: DISCOVERY
why_now: 9to5Google RSS: Android Pulse app appeared in Play Store updates.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
hard_evidence: 9to5Google RSS: Android Pulse app appeared in Play Store updates.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Vysvětlit nový systémový prvek bez paniky.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-02. Pixel Rambler voice-to-text: funkce, která může změnit diktování
```
candidate_id: AND-02
exact_topic: pixel rambler voice to text
proposed_title: Pixel Rambler voice-to-text: funkce, která může změnit diktování
action: CREATE
primary_lane: DISCOVERY
why_now: 9to5Google RSS: Pixel 11 Rambler voice-to-text.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 43 sessions / 81 views
hard_evidence: 9to5Google RSS: Pixel 11 Rambler voice-to-text.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Praktický demo/impact angle pro Google/Pixel publikum.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-03. Gemini Device Help na Pixelu: poradí s telefonem, ale není bez limitů
```
candidate_id: AND-03
exact_topic: gemini device help pixel
proposed_title: Gemini Device Help na Pixelu: poradí s telefonem, ale není bez limitů
action: CREATE
primary_lane: CURRENT DEMAND
why_now: Android Authority + 9to5Google webové signály.
hard_evidence: Android Authority + 9to5Google webové signály.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Potřebujete změnit nastavení svého mobilu? Stačí požádat Gemini a nemusíte už ni
unique_value: Uživatelský test/hranice funkce.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Potřebujete změnit nastavení svého mobilu? Stačí požádat Gemini a nemusíte už ni
opportunity_score: 66
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## AND-04. Google Maps v Android Auto nezobrazuje dopravu: co zkusit
```
candidate_id: AND-04
exact_topic: google maps android auto traffic
proposed_title: Google Maps v Android Auto nezobrazuje dopravu: co zkusit
action: CREATE
primary_lane: CURRENT DEMAND
why_now: 9to5Google + XDA: traffic data bug.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 47 sessions / 115 views
hard_evidence: 9to5Google + XDA: traffic data bug.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Rychlý servisní článek s workaroundy.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-05. Srpnové Google System Updates: co je nové v Androidu, Play Store a Auto
```
candidate_id: AND-05
exact_topic: google system updates august
proposed_title: Srpnové Google System Updates: co je nové v Androidu, Play Store a Auto
action: UPDATE
primary_lane: CURRENT DEMAND
why_now: 9to5Google update 24.8.; existující Android Magazine článek.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 47 sessions / 115 views
hard_evidence: 9to5Google update 24.8.; existující Android Magazine článek.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Doplnit nové body, ne nový duplicitní článek.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-06. Android Auto se odpojuje nebo mrzne: Google chystá opravu
```
candidate_id: AND-06
exact_topic: android auto disconnect freeze
proposed_title: Android Auto se odpojuje nebo mrzne: Google chystá opravu
action: CREATE
primary_lane: CURRENT DEMAND
why_now: 9to5Google: disconnect/freeze fix update.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
hard_evidence: 9to5Google: disconnect/freeze fix update.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Servisní článek + kontrola verze aplikace.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-07. Always On Display na Androidu: zapnutí, výdrž baterie a nejlepší nastavení
```
candidate_id: AND-07
exact_topic: always on display android
proposed_title: Always On Display na Androidu: zapnutí, výdrž baterie a nejlepší nastavení
action: CREATE
primary_lane: SEO
why_now: GSC Android: 261 imp, pozice 13.6.; GSC 266 imp / pos 13.94 / CTR 1.13 %; GA4 104 sessions / 431 views
hard_evidence: GSC Android: 261 imp, pozice 13.6.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Pixel 11 Pro HiLight: co to vlastně je a proč první reakce vyvolaly rozpaky | Google konečně zapíná Live Updates pro stopky a časovač. Novinka výrazně zpříjem
unique_value: CZ návod pro malý web, jasný evergreen.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Pixel 11 Pro HiLight: co to vlastně je a proč první reakce vyvolaly rozpaky | Google konečně zapíná Live Updates pro stopky a časovač. Novinka výrazně zpříjem
opportunity_score: 66
predictive_score: 72
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## AND-08. Smazali jste oznámení? Android ho umí najít
```
candidate_id: AND-08
exact_topic: android notification history
proposed_title: Smazali jste oznámení? Android ho umí najít
action: UPDATE
primary_lane: SEO
why_now: GA4: existující notification článek v top Android pages.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
hard_evidence: GA4: existující notification článek v top Android pages.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Smazali jste omylem oznámení? Android ho umí najít. Stačí zapnout tuto funkci
unique_value: Rozšířit o modely a screenshot-like kroky.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Smazali jste omylem oznámení? Android ho umí najít. Stačí zapnout tuto funkci
opportunity_score: 66
predictive_score: 72
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-09. RCS chyba 3100 po přechodu na Galaxy: co dělat
```
candidate_id: AND-09
exact_topic: rcs chyba 3100
proposed_title: RCS chyba 3100 po přechodu na Galaxy: co dělat
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: Existující Android Magazine článek 21.8.
hard_evidence: Existující Android Magazine článek 21.8.; WP/Manticore: SIMILAR_EXISTS přes Manticore: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100
unique_value: Navázat praktickým návodem a stavem řešení.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-10. Android 17 zpřísňuje aplikace na pozadí: komu může přestat hrát zvuk
```
candidate_id: AND-10
exact_topic: android 17 background audio
proposed_title: Android 17 zpřísňuje aplikace na pozadí: komu může přestat hrát zvuk
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: Existující článek 19.8.; aktuální developer/user dopad.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
hard_evidence: Existující článek 19.8.; aktuální developer/user dopad.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Android 17 zpřísňuje aplikace běžící na pozadí. U některých může přestat fungova
unique_value: Přehled dotčených aplikací a workaround.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Android 17 zpřísňuje aplikace běžící na pozadí. U některých může přestat fungova
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-11. Pixel 11 nabídky: kdy dává smysl koupit a kdy počkat
```
candidate_id: AND-11
exact_topic: pixel 11 deals
proposed_title: Pixel 11 nabídky: kdy dává smysl koupit a kdy počkat
action: CREATE
primary_lane: CURRENT DEMAND
why_now: Google Trends via pytrends Pixel 11 55/100 + Android Central RSS: Pixel 11 deals.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 43 sessions / 81 views
hard_evidence: Android Central RSS: Pixel 11 deals.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Nákupní úhel, ne jen affiliate/akce.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-12. Tracker pro Android i iPhone do kola nebo golfových holí
```
candidate_id: AND-12
exact_topic: android iphone tracker bike
proposed_title: Tracker pro Android i iPhone do kola nebo golfových holí
action: CREATE
primary_lane: DISCOVERY
why_now: 9to5Google RSS: tracker with 3-year battery.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
hard_evidence: 9to5Google RSS: tracker with 3-year battery.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Praktický gadget článek s cross-platform routingem.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-13. Wear OS sdílení polohy: co Google přidává do hodinek
```
candidate_id: AND-13
exact_topic: wear os location sharing
proposed_title: Wear OS sdílení polohy: co Google přidává do hodinek
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: GA4 Android: Wear OS location sharing article běží v RU.; GA4 47 sessions / 115 views
hard_evidence: GA4 Android: Wear OS location sharing article běží v RU.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Google rozšiřuje polohu na Wear OS. Přibývá Location Sharing i Find people
unique_value: CZ follow-up pro Android/Wear OS.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Google rozšiřuje polohu na Wear OS. Přibývá Location Sharing i Find people
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-14. HONOR Robot Phone: nejdivnější telefon roku, nebo ukázka budoucnosti?
```
candidate_id: AND-14
exact_topic: honor robot phone
proposed_title: HONOR Robot Phone: nejdivnější telefon roku, nebo ukázka budoucnosti?
action: FOLLOW-UP
primary_lane: DISCOVER
why_now: GA4 Android: Honor Robot Phone v top.; GSC 161 imp / pos 9.12 / CTR 4.97 %; GA4 40 sessions / 246 views
hard_evidence: GA4 Android: Honor Robot Phone v top.; WP/Manticore: SIMILAR_EXISTS přes Manticore: HONOR Robot Phone: gimbal, AI a nejdivnější smartphone roku | HONOR Robot Phone je realita, má gimbal, filmové barvy a AI, která zvládne přes 
unique_value: Trendový follow-up s ověřením aktuálního stavu.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: HONOR Robot Phone: gimbal, AI a nejdivnější smartphone roku | HONOR Robot Phone je realita, má gimbal, filmové barvy a AI, která zvládne přes 
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-15. 5 tipů, jak vylepšit Pixel bez výměny telefonu
```
candidate_id: AND-15
exact_topic: pixel tips
proposed_title: 5 tipů, jak vylepšit Pixel bez výměny telefonu
action: FOLLOW-UP
primary_lane: SEO + DISCOVER
why_now: GA4 Android: Pixel tips v top.; GSC 41 imp / pos 8.17 / CTR 9.76 %; GA4 43 sessions / 81 views
hard_evidence: GA4 Android: Pixel tips v top.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Praktický evergreen s novými Android/Pixel funkcemi.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-16. Jak vypnout Android telefon: aktualizovaný návod pro rok 2026
```
candidate_id: AND-16
exact_topic: vypnout android telefon
proposed_title: Jak vypnout Android telefon: aktualizovaný návod pro rok 2026
action: UPDATE
primary_lane: SEO
why_now: GSC: 4 644 imp, pozice 5.19, CTR 1.23 %.; GSC 1129 imp / pos 3.5 / CTR 2.13 %; GA4 941 sessions / 1066 views
hard_evidence: GSC: 4 644 imp, pozice 5.19, CTR 1.23 %.; WP/Manticore: SIMILAR_EXISTS přes Manticore: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100 | Jak na Androidu snadno nastavit tapety podle denní doby
unique_value: Aktualizovat existující evergreen a titulkově zlepšit CTR.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: RCS po přechodu na nový Galaxy přestává fungovat. Google řeší chybu 3100 | Jak na Androidu snadno nastavit tapety podle denní doby
opportunity_score: 66
predictive_score: 72
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-17. Jak vynutit LTE nebo 5G na Androidu
```
candidate_id: AND-17
exact_topic: force lte 5g android
proposed_title: Jak vynutit LTE nebo 5G na Androidu
action: UPDATE
primary_lane: SEO
why_now: GA4 ukazuje historický výkon RU verze.; GA4 32 sessions / 58 views
hard_evidence: GA4 ukazuje historický výkon RU verze.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: CZ návod s upozorněním na rizika a modelové rozdíly.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 72
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-18. Jak vysypat koš na Androidu
```
candidate_id: AND-18
exact_topic: android kos
proposed_title: Jak vysypat koš na Androidu
action: UPDATE
primary_lane: SEO
why_now: GSC: související dotazy v top Android Search.; GSC 37 imp / pos 10.16 / CTR 40.54 %; GA4 941 sessions / 1066 views
hard_evidence: GSC: související dotazy v top Android Search.; WP/Manticore: SIMILAR_EXISTS přes Manticore: 6 skrytých aplikací od Googlu, které by měl znát každý uživatel Androidu | Jak obnovit smazané soubory a fotky v Androidu?
unique_value: Krátký evergreen s kroky podle Google Photos/Files/Gmail.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: 6 skrytých aplikací od Googlu, které by měl znát každý uživatel Androidu | Jak obnovit smazané soubory a fotky v Androidu?
opportunity_score: 66
predictive_score: 72
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-19. Jak odblokovat číslo na Androidu
```
candidate_id: AND-19
exact_topic: blokovani cisla android
proposed_title: Jak odblokovat číslo na Androidu
action: UPDATE
primary_lane: SEO
why_now: GSC: multilingual dotazy na odblokování čísla.; GA4 941 sessions / 1066 views
hard_evidence: GSC: multilingual dotazy na odblokování čísla.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Google Scam Detection míří mimo Pixel: jak Android pozná podvodný hovor | Konec bankovních podvodů? Google zavádí AI ochranu a biometrický zámek proti krá
unique_value: CZ návod + Samsung/Pixel/Xiaomi rozdíly.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Google Scam Detection míří mimo Pixel: jak Android pozná podvodný hovor | Konec bankovních podvodů? Google zavádí AI ochranu a biometrický zámek proti krá
opportunity_score: 66
predictive_score: 72
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## AND-20. GrapheneOS míří nejdřív na Motorolu: proč je to velká změna
```
candidate_id: AND-20
exact_topic: grapheneos motorola 2027
proposed_title: GrapheneOS míří nejdřív na Motorolu: proč je to velká změna
action: CREATE
primary_lane: DISCOVERY
why_now: Android Central RSS: GrapheneOS/Motorola 2027.
hard_evidence: Android Central RSS: GrapheneOS/Motorola 2027.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Bezpečnostní úhel pro Android publikum.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 66
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

# Source Coverage Audit
- WordPress/Manticore: CHECKED — 60 intentů přes /results
- GSC: CHECKED — 3 weby, 28d + 7d
- GA4: CHECKED — 3 weby, 7 dní
- Google Trends: CHECKED — JustSerpAPI failed, pytrends fallback OK
- Google News / major tech media: CHECKED — RSS + web search
- official newsrooms: CHECKED — Apple Newsroom, Samsung Newsroom
- product pages: PARTIAL CHECKED — jen kandidáti se zdrojovým signálem
- support docs: NOT CHECKED - REASON — trendový rychlý běh, ne support audit
- developer docs/changelogs: PARTIAL CHECKED — Google System Updates přes 9to5Google
- GitHub: CHECKED read-only v 09:15 rerunu — bez kvalifikovaného user-impact slotu
- beta programs: PARTIAL CHECKED — One UI beta přes media/news
- APK changes: NOT CHECKED - REASON — není v dnešním rozsahu
- regulatory/certification: PARTIAL CHECKED — Apple EU změny
- Reddit/forums/X/YouTube: NOT CHECKED - REASON — nepoužito jako hard evidence
- smaller specialist media: CHECKED — SamMobile, 9to5Google, MacRumors
