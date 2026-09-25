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

# LSA — letemsvetemapplem.eu
Zdrojové signály: Apple Newsroom: Apple introduces new Mac Studio with M5 Max and M5 Ultra; Apple unveils a more powerful Mac mini featuring the all-new M6 and M5 Pro; Apple introduces M6 and M5 Ultra for a big leap in performance and AI compute | MacRumors: BenQ's New iScreenBar is a Monitor Light Bar Made for the iMac; Apple Maps Ads Are Here, and There's No Way to Turn Them Off; New Mac Mini and Mac Studio: 13 Things You Might Have Missed | 9to5Mac: Apple renews push for expedited discovery in OpenAI trade secret misappropriation lawsuit; Apple shares behind-the-scenes video for its fun new Mac mini ad; Notability can now organize meeting recordings, transcriptions, and notes around your calendar

## LSA-01. Mac mini s M6: co Apple skutečně změnil a komu se vyplatí
```
candidate_id: LSA-01
exact_topic: mac mini m6
proposed_title: Mac mini s M6: co Apple skutečně změnil a komu se vyplatí
action: CREATE
primary_lane: CURRENT DEMAND
why_now: Apple Newsroom + MacRumors/9to5Mac, čerstvé uvedení Mac mini.; GSC 8495 imp / pos 2.11 / CTR 9.59 %; GA4 1669 sessions / 8120 views
hard_evidence: Apple Newsroom + MacRumors/9to5Mac, čerstvé uvedení Mac mini.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Nový M6 je vůbec první 2nm Apple čip, přináší obrovský skok hlavně v AI | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
unique_value: Rozebrat konfigurace, AI výkon a český nákupní kontext.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Nový M6 je vůbec první 2nm Apple čip, přináší obrovský skok hlavně v AI | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## LSA-02. Mac Studio s M5 Max a M5 Ultra: tichý upgrade pro profesionály
```
candidate_id: LSA-02
exact_topic: mac studio m5 ultra
proposed_title: Mac Studio s M5 Max a M5 Ultra: tichý upgrade pro profesionály
action: CREATE
primary_lane: CURRENT DEMAND
why_now: Apple Newsroom: nový Mac Studio s M5 Max/M5 Ultra.; GSC 8495 imp / pos 2.11 / CTR 9.59 %; GA4 1669 sessions / 8120 views
hard_evidence: Apple Newsroom: nový Mac Studio s M5 Max/M5 Ultra.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Nový M5 Ultra je dosud nejvýkonnější Apple čip, zvládne až 512 GB RAM | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
unique_value: Srovnat proti Mac mini M6 a vysvětlit pro koho je Studio.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Nový M5 Ultra je dosud nejvýkonnější Apple čip, zvládne až 512 GB RAM | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## LSA-03. M6 a M5 Ultra: proč Apple tlačí AI výkon do Maců
```
candidate_id: LSA-03
exact_topic: m6 m5 ultra ai compute
proposed_title: M6 a M5 Ultra: proč Apple tlačí AI výkon do Maců
action: CREATE
primary_lane: DISCOVERY
why_now: Apple Newsroom: nové čipy M6/M5 Ultra a AI compute.; GA4 1160 sessions / 2219 views
hard_evidence: Apple Newsroom: nové čipy M6/M5 Ultra a AI compute.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Přeložit technický čipový launch do uživatelských dopadů.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-04. Jak sledovat Apple Keynote 9. září v Česku
```
candidate_id: LSA-04
exact_topic: jak sledovat apple keynote
proposed_title: Jak sledovat Apple Keynote 9. září v Česku
action: FOLLOW-UP
primary_lane: SEO + CURRENT DEMAND
why_now: Google Trends via pytrends iPhone 18 10/100 teď nízko, ale GSC iPhone 18 silný; MacRumors/9to5Mac sledují zářijové okno.; GA4 5495 sessions / 14566 views
hard_evidence: GSC iPhone 18 silný; MacRumors/9to5Mac sledují zářijové okno.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v  | Unikla krabička iPhone 18 Pro Max. Apple na ní odhaluje největší novinku fotoapa
unique_value: Praktický servis: čas v ČR, stream, co čekat, co je zatím spekulace.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v  | Unikla krabička iPhone 18 Pro Max. Apple na ní odhaluje největší novinku fotoapa
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-05. iPhone 18 Pro: co víme, co jsou úniky a co neříkat jako fakt
```
candidate_id: LSA-05
exact_topic: iphone 18 pro
proposed_title: iPhone 18 Pro: co víme, co jsou úniky a co neříkat jako fakt
action: UPDATE
primary_lane: CURRENT DEMAND
why_now: GSC: iPhone 18 Pro patří mezi nejsilnější LSA dotazy.; GSC 680779 imp / pos 1.35 / CTR 4.89 %; GA4 4712 sessions / 51935 views
hard_evidence: GSC: iPhone 18 Pro patří mezi nejsilnější LSA dotazy.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v 
unique_value: Oddělit ověřené informace od leaků, vyčistit záměny intentu.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v 
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-06. iPhone Ultra: proč skládací iPhone táhne Discover
```
candidate_id: LSA-06
exact_topic: iphone ultra
proposed_title: iPhone Ultra: proč skládací iPhone táhne Discover
action: FOLLOW-UP
primary_lane: DISCOVER
why_now: GA4: skládací iPhone Ultra měl vysoké pageviews; GSC iPhone Ultra silný.; GSC 680779 imp / pos 1.35 / CTR 4.89 %; GA4 4712 sessions / 51935 views
hard_evidence: GA4: skládací iPhone Ultra měl vysoké pageviews; GSC iPhone Ultra silný.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
unique_value: Cena/dostupnost/komu dává smysl, ne opakování prvních dojmů.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-07. Apple Maps reklamy jsou živé: kde se zobrazí a proč nejdou vypnout
```
candidate_id: LSA-07
exact_topic: apple maps ads reklamy
proposed_title: Apple Maps reklamy jsou živé: kde se zobrazí a proč nejdou vypnout
action: UPDATE
primary_lane: CURRENT DEMAND
why_now: MacRumors/AppleInsider: reklamy Apple Maps live v USA/Kanadě.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
hard_evidence: MacRumors/AppleInsider: reklamy Apple Maps live v USA/Kanadě.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple Maps zaplaví reklamy a to už letos v létě! | Apple může slavit! Apple Maps i Apple Ads vyvázly regulaci ze strany EU
unique_value: Navázat na starší článek; vysvětlit praktický dopad pro uživatele.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Apple Maps zaplaví reklamy a to už letos v létě! | Apple může slavit! Apple Maps i Apple Ads vyvázly regulaci ze strany EU
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-08. ChatGPT na Macu a iMessage: co je reálně možné a kde jsou rizika
```
candidate_id: LSA-08
exact_topic: chatgpt imessage mac
proposed_title: ChatGPT na Macu a iMessage: co je reálně možné a kde jsou rizika
action: UPDATE
primary_lane: CURRENT DEMAND
why_now: Google Trends via pytrends ChatGPT 50/100 + Moula/GSC: ChatGPT 32k imp, slabý CTR; Manticore našel fresh články.; GA4 1669 sessions / 8120 views
hard_evidence: Moula/GSC: ChatGPT 32k imp, slabý CTR; Manticore našel fresh články.; WP/Manticore: SIMILAR_EXISTS přes Manticore: ChatGPT dostal na Mac přístup k iMessage. Umí zprávy číst, analyzovat je i odesí | iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těšit
unique_value: Zlepšit CTR konkrétním bezpečnostním a praktickým úhlem.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: ChatGPT dostal na Mac přístup k iMessage. Umí zprávy číst, analyzovat je i odesí | iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těšit
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-09. LEGO PlayStation 1 a proč LEGO teď funguje na LSA
```
candidate_id: LSA-09
exact_topic: lego playstation 1
proposed_title: LEGO PlayStation 1 a proč LEGO teď funguje na LSA
action: FOLLOW-UP
primary_lane: DISCOVER
why_now: GSC LEGO 68k imp; GA4 LEGO články vysoké views.; GSC 71079 imp / pos 6.48 / CTR 3.71 %; GA4 5111 sessions / 54080 views
hard_evidence: GSC LEGO 68k imp; GA4 LEGO články vysoké views.; WP/Manticore: SIMILAR_EXISTS přes Manticore: LEGO PlayStation 1 bude pořádná nostalgická pecka. Má být stejně velký jako orig | LEGO a Sony chystají senzaci. Vedle stavebnicového PlayStationu dorazí i legendá
unique_value: Zachytit nostalgii/popkulturu, ověřit intent před publikací.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: LEGO PlayStation 1 bude pořádná nostalgická pecka. Má být stejně velký jako orig | LEGO a Sony chystají senzaci. Vedle stavebnicového PlayStationu dorazí i legendá
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-10. iCloud trik na fotky: co ještě funguje a co Apple brzy utne
```
candidate_id: LSA-10
exact_topic: icloud uloziste fotky
proposed_title: iCloud trik na fotky: co ještě funguje a co Apple brzy utne
action: UPDATE
primary_lane: DISCOVER
why_now: GA4: iCloud storage článek jeden z top výkonů týdne.; GSC 2570 imp / pos 4.49 / CTR 17.16 %; GA4 5495 sessions / 14566 views
hard_evidence: GA4: iCloud storage článek jeden z top výkonů týdne.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Tajný trik, jak na iCloudu získat neomezené úložiště pro vaše fotky zdarma. Appl | Apple vám v iOS 27 vezme další místo na iCloudu. Tohle se vyplatí vědět
unique_value: Praktická kontrola aktuálnosti a limitů, interní link na původní článek.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Tajný trik, jak na iCloudu získat neomezené úložiště pro vaše fotky zdarma. Appl | Apple vám v iOS 27 vezme další místo na iCloudu. Tohle se vyplatí vědět
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-11. CarPlay v iOS 27: změny, které řidiči uvidí jako první
```
candidate_id: LSA-11
exact_topic: carplay ios 27
proposed_title: CarPlay v iOS 27: změny, které řidiči uvidí jako první
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: GA4: CarPlay/iOS 27 článek ve výkonu týdne.; GA4 3251 sessions / 5918 views
hard_evidence: GA4: CarPlay/iOS 27 článek ve výkonu týdne.; WP/Manticore: SIMILAR_EXISTS přes Manticore: CarPlay se v iOS 27 pořádně mění. Apple přidá funkce, které jsme chtěli roky | Apple CarPlay dostane v iOS 27 dvě nové funkce, které potěší miliony řidičů
unique_value: Konkrétní use-cases místo obecného výčtu funkcí.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: CarPlay se v iOS 27 pořádně mění. Apple přidá funkce, které jsme chtěli roky | Apple CarPlay dostane v iOS 27 dvě nové funkce, které potěší miliony řidičů
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-12. Apple Watch 12: šest očekávání před keynote, jasně oddělená od faktů
```
candidate_id: LSA-12
exact_topic: apple watch 12
proposed_title: Apple Watch 12: šest očekávání před keynote, jasně oddělená od faktů
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: Manticore ukazuje fresh článek; Apple event proximity.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
hard_evidence: Manticore ukazuje fresh článek; Apple event proximity.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v 
unique_value: Checklist fakt/leak/spekulace, nepovyšovat úniky na potvrzení.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v 
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-13. AirPods 5 před zářím: co dává smysl čekat a co je jen rumor
```
candidate_id: LSA-13
exact_topic: airpods 5
proposed_title: AirPods 5 před zářím: co dává smysl čekat a co je jen rumor
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: Manticore fresh AirPods 5 zmínky; Apple event proximity.; GA4 1463 sessions / 4997 views
hard_evidence: Manticore fresh AirPods 5 zmínky; Apple event proximity.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Nejen iPhone 18 Pro a Ultra. Apple v září představí i nové AirPods 5 | Recenze FIXED Zen 10 Loop: 10 000 mAh, 30 W a dost energie i pro MacBook Air
unique_value: Vysvětlit pravděpodobnost a praktický dopad pro nákup.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Nejen iPhone 18 Pro a Ultra. Apple v září představí i nové AirPods 5 | Recenze FIXED Zen 10 Loop: 10 000 mAh, 30 W a dost energie i pro MacBook Air
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-14. iPhone 20 design: proč už teď zajímá čtenáře víc než by měl
```
candidate_id: LSA-14
exact_topic: iphone 20 design
proposed_title: iPhone 20 design: proč už teď zajímá čtenáře víc než by měl
action: FOLLOW-UP
primary_lane: DISCOVER
why_now: GA4: iPhone 20 design článek má silné views.; GSC 680779 imp / pos 1.35 / CTR 4.89 %; GA4 4712 sessions / 51935 views
hard_evidence: GA4: iPhone 20 design článek má silné views.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple chystá něco opravdu velkého. Nové úniky ukazují, jak může vypadat iPhone b | Bloomberg: Revoluční iPhone 20 není zrušen, bude ale vypadat jinak než původně m
unique_value: Trendový follow-up s opatrným rámováním vzdálené budoucnosti.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Apple chystá něco opravdu velkého. Nové úniky ukazují, jak může vypadat iPhone b | Bloomberg: Revoluční iPhone 20 není zrušen, bude ale vypadat jinak než původně m
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-15. Nová Apple TV 4K a Siri Remote: malý update, velký dopad v obýváku
```
candidate_id: LSA-15
exact_topic: apple tv 4k siri remote
proposed_title: Nová Apple TV 4K a Siri Remote: malý update, velký dopad v obýváku
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: GA4: Apple TV/Siri Remote článek fungoval.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
hard_evidence: GA4: Apple TV/Siri Remote článek fungoval.; WP/Manticore: SIMILAR_EXISTS přes Manticore: S novou Apple TV dorazí i vylepšený ovladač. Tohle je jedna z jeho nejžádanějšíc | Čekání končí. Nová Apple TV 4K dorazí na podzim a přinese chytřejší Siri i přepr
unique_value: Praktický dopad ovladače, Wi-Fi, HomeKit, cena.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: S novou Apple TV dorazí i vylepšený ovladač. Tohle je jedna z jeho nejžádanějšíc | Čekání končí. Nová Apple TV 4K dorazí na podzim a přinese chytřejší Siri i přepr
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-16. Apple mění pravidla pro aplikace v EU: co to znamená pro majitele iPhonů
```
candidate_id: LSA-16
exact_topic: apple european union apps changes
proposed_title: Apple mění pravidla pro aplikace v EU: co to znamená pro majitele iPhonů
action: CREATE
primary_lane: CURRENT DEMAND
why_now: Apple Newsroom: changes for apps in EU.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
hard_evidence: Apple Newsroom: changes for apps in EU.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Přeložit regulatorní změnu do češtiny a praktických dopadů.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-17. Která Apple zařízení už mají plnou podporu Wi-Fi 7
```
candidate_id: LSA-17
exact_topic: wifi 7 apple devices
proposed_title: Která Apple zařízení už mají plnou podporu Wi-Fi 7
action: CREATE
primary_lane: SEO + CURRENT DEMAND
why_now: 9to5Mac: přehled zařízení s Wi-Fi 7.; GA4 3251 sessions / 5918 views
hard_evidence: 9to5Mac: přehled zařízení s Wi-Fi 7.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Kompetní historie Apple iPhone: jak vznikal hudební přehrávač, telefon a interne
unique_value: Nákupní přehled pro iPhone/Mac/iPad uživatele.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Kompetní historie Apple iPhone: jak vznikal hudební přehrávač, telefon a interne
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## LSA-18. BenQ iScreenBar pro iMac: doplněk, který Apple nikdy neudělal
```
candidate_id: LSA-18
exact_topic: benq iscreenbar imac
proposed_title: BenQ iScreenBar pro iMac: doplněk, který Apple nikdy neudělal
action: CREATE
primary_lane: DISCOVERY
why_now: MacRumors: BenQ iScreenBar for iMac.
hard_evidence: MacRumors: BenQ iScreenBar for iMac.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Produktový praktický tip pro LSA publikum.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## LSA-19. Apple 40W Dynamic Power Adapter míří do dalších zemí: proč je zajímavý
```
candidate_id: LSA-19
exact_topic: 40w dynamic power adapter
proposed_title: Apple 40W Dynamic Power Adapter míří do dalších zemí: proč je zajímavý
action: CREATE
primary_lane: CURRENT DEMAND
why_now: MacRumors: adaptér expanduje do dalších zemí.
hard_evidence: MacRumors: adaptér expanduje do dalších zemí.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkodobě a | iPad Pro M5 v prvních recenzích! Jaký je nejvýkonnější tablet současnosti v reál
unique_value: Vysvětlit nabíjení, kompatibilitu a zda čekat CZ dostupnost.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkodobě a | iPad Pro M5 v prvních recenzích! Jaký je nejvýkonnější tablet současnosti v reál
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## LSA-20. Apple otevřel Advanced Manufacturing Center v Houstonu: proč to není jen PR
```
candidate_id: LSA-20
exact_topic: apple manufacturing center houston
proposed_title: Apple otevřel Advanced Manufacturing Center v Houstonu: proč to není jen PR
action: CREATE
primary_lane: DISCOVERY
why_now: Apple Newsroom: nové manufacturing centrum.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
hard_evidence: Apple Newsroom: nové manufacturing centrum.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Sklo pro iPhone a Apple Watch bude již brzy 100% z USA
unique_value: Napojit na čipy, dodavatelský řetězec a Apple Intelligence.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Sklo pro iPhone a Apple Watch bude již brzy 100% z USA
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

# Samsung Magazine — samsungmagazine.eu
Zdrojové signály: Samsung Newsroom US: An Easier Way to Switch to the New Galaxy Z Fold8; Samsung Galaxy Buds4 Pro’s Superior Hi-Fi Sound Recognized by Audio Experts; Samsung Research America Expands Academic Collaboration Through the 2026 START Program | SamMobile: Samsung updates Galaxy M55 with August 2026 security patch; Hot take, but I wish my Galaxy Z Fold 8 had one fewer selfie camera; Galaxy S27 Ultra leak reveals a massive horizontal camera bar redesign | Android Central: Yep, One UI 9 Beta 6 is rolling out now on the Galaxy S26: here's what's in it; Waiting for GrapheneOS? Motorola's 2027 phones are up first, then it's on to foldables; My favorite writing tablet just scored a rare discount at Best Buy — but it won't last long

## SAM-01. One UI 9 Beta 6: co opravuje a kdo ji dostává
```
candidate_id: SAM-01
exact_topic: one ui 9 beta 6
proposed_title: One UI 9 Beta 6: co opravuje a kdo ji dostává
action: UPDATE
primary_lane: CURRENT DEMAND
why_now: Android Central + Samsung/One UI signály; GSC one ui 132k+ imp.; GSC 135824 imp / pos 4.02 / CTR 16.78 %; GA4 15000 sessions / 24381 views
hard_evidence: Android Central + Samsung/One UI signály; GSC one ui 132k+ imp.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Samsung vydává 6. betu One UI 9 pro Galaxy S26. Opravuje fotoaparát i rozbité wi | Ostrá verze One UI 9 má zpoždění. Samsung pro Galaxy S26 chystá další betu
unique_value: Přesný stav bety, opravy, dostupnost, interní linky.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Samsung vydává 6. betu One UI 9 pro Galaxy S26. Opravuje fotoaparát i rozbité wi | Ostrá verze One UI 9 má zpoždění. Samsung pro Galaxy S26 chystá další betu
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-02. Gemini na Samsungu: obří zájem, mizerný CTR, praktický návod
```
candidate_id: SAM-02
exact_topic: gemini samsung
proposed_title: Gemini na Samsungu: obří zájem, mizerný CTR, praktický návod
action: UPDATE
primary_lane: SEO
why_now: GSC/Moula: 224k imp, CTR 0.1 %.; GA4 22735 sessions / 29358 views
hard_evidence: GSC/Moula: 224k imp, CTR 0.1 %.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Gemini Intelligence přináší do Androidu autonomii. Známe seznam telefonů, které  | Stabilní verze One UI 9: Na která zařízení dorazí jako první a jak se liší od be
unique_value: Přepsat angle na uživatelské otázky: kde je Gemini, co umí, vypnutí.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Gemini Intelligence přináší do Androidu autonomii. Známe seznam telefonů, které  | Stabilní verze One UI 9: Na která zařízení dorazí jako první a jak se liší od be
opportunity_score: 78
predictive_score: 72
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-03. Galaxy S26 vs S25: má upgrade smysl?
```
candidate_id: SAM-03
exact_topic: galaxy s26 s25 upgrade
proposed_title: Galaxy S26 vs S25: má upgrade smysl?
action: CREATE
primary_lane: SEO + CURRENT DEMAND
why_now: GSC Samsung Galaxy/S26 silné dotazy.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
hard_evidence: GSC Samsung Galaxy/S26 silné dotazy.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Galaxy Z Fold8 Ultra dostane nečekaný upgrade displeje. Nejde jen o méně viditel | Čeká nás po čtyřech letech změna? Galaxy S27 Pro a Ultra dostanou novinku, ktero
unique_value: Jasný nákupní checklist místo obecné novinky.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Galaxy Z Fold8 Ultra dostane nečekaný upgrade displeje. Nejde jen o méně viditel | Čeká nás po čtyřech letech změna? Galaxy S27 Pro a Ultra dostanou novinku, ktero
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## SAM-04. Galaxy S26 FE: co sledovat po eventu 27. srpna
```
candidate_id: SAM-04
exact_topic: galaxy s26 fe event
proposed_title: Galaxy S26 FE: co sledovat po eventu 27. srpna
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: Samsung Newsroom invitation; existující články před eventem.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
hard_evidence: Samsung Newsroom invitation; existující články před eventem.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Samsung Galaxy S26 FE: cena, datum a co čekat od Galaxy Event August 2026 | Zapište si toto datum. Samsung prozradil, kdy představí Galaxy S26 FE a další no
unique_value: Po eventu doplnit cenu, dostupnost, odlišnosti od spekulací.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Samsung Galaxy S26 FE: cena, datum a co čekat od Galaxy Event August 2026 | Zapište si toto datum. Samsung prozradil, kdy představí Galaxy S26 FE a další no
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-05. Galaxy Watch Ultra 2: recenze a srovnání s Watch Ultra a Garminem
```
candidate_id: SAM-05
exact_topic: galaxy watch ultra 2 recenze
proposed_title: Galaxy Watch Ultra 2: recenze a srovnání s Watch Ultra a Garminem
action: CREATE
primary_lane: CURRENT DEMAND
why_now: Moula: hype fáze; Manticore bez přesné recenze Ultra 2.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
hard_evidence: Moula: hype fáze; Manticore bez přesné recenze Ultra 2.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Samsung Galaxy Z Fold8 Ultra recenze: Je to špička, ale trochu nuda | Nové skládačky od Samsungu stojí ranec. Tímto trikem ale můžete ušetřit desítky 
unique_value: CZ recenze/srovnání, ne jen přepis specifikací.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Samsung Galaxy Z Fold8 Ultra recenze: Je to špička, ale trochu nuda | Nové skládačky od Samsungu stojí ranec. Tímto trikem ale můžete ušetřit desítky 
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## SAM-06. Jak snadno přejít na Galaxy Z Fold8
```
candidate_id: SAM-06
exact_topic: switch to galaxy z fold8
proposed_title: Jak snadno přejít na Galaxy Z Fold8
action: CREATE
primary_lane: CURRENT DEMAND
why_now: Samsung Newsroom: Easier Way to Switch to New Galaxy Z Fold8.; GA4 2097 sessions / 5703 views
hard_evidence: Samsung Newsroom: Easier Way to Switch to New Galaxy Z Fold8.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové | Skvělá aplikace od Samsungu má velký problém. Uživatelům po přechodu na nový tel
unique_value: Praktický migrační návod pro iPhone/Samsung uživatele.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové | Skvělá aplikace od Samsungu má velký problém. Uživatelům po přechodu na nový tel
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## SAM-07. Galaxy Buds4 Pro mají uznaný Hi-Fi zvuk: co to znamená v praxi
```
candidate_id: SAM-07
exact_topic: galaxy buds4 pro hi-fi sound
proposed_title: Galaxy Buds4 Pro mají uznaný Hi-Fi zvuk: co to znamená v praxi
action: CREATE
primary_lane: CURRENT DEMAND
why_now: Samsung Newsroom: audio experts recognition.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
hard_evidence: Samsung Newsroom: audio experts recognition.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Oddělit certifikaci/marketing od reálného poslechu.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-08. Srpnové bezpečnostní aktualizace Galaxy: kdo je dostává
```
candidate_id: SAM-08
exact_topic: august 2026 security patch galaxy
proposed_title: Srpnové bezpečnostní aktualizace Galaxy: kdo je dostává
action: CREATE
primary_lane: CURRENT DEMAND
why_now: SamMobile: August 2026 security patch pro Galaxy M55 + patch vlna.; GA4 2134 sessions / 3271 views
hard_evidence: SamMobile: August 2026 security patch pro Galaxy M55 + patch vlna.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Krátký servisní roundup s modely a postupem kontroly.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-09. Galaxy S27 Ultra leak: vodorovný fotomodul a riziko iPhone looku
```
candidate_id: SAM-09
exact_topic: galaxy s27 ultra camera bar
proposed_title: Galaxy S27 Ultra leak: vodorovný fotomodul a riziko iPhone looku
action: CREATE
primary_lane: DISCOVERY
why_now: Android Central/SamMobile: S27 Ultra redesign leak.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
hard_evidence: Android Central/SamMobile: S27 Ultra redesign leak.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Jasně označit leak; porovnat designový směr a očekávání.
reality_status: UNCERTAIN - leak/spekulace jasně označit
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-10. Good Lock MultiStar/FlipShot: malá funkce pro skládačky, velký rozdíl
```
candidate_id: SAM-10
exact_topic: good lock multistar flipshot
proposed_title: Good Lock MultiStar/FlipShot: malá funkce pro skládačky, velký rozdíl
action: CREATE
primary_lane: DISCOVERY
why_now: Samsung specialist media signály z 24.–25.8.
hard_evidence: Samsung specialist media signály z 24.–25.8.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Praktický návod pro Fold/Flip majitele.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-11. Samsung na Gamescomu 2026: proč to zajímá i majitele Galaxy
```
candidate_id: SAM-11
exact_topic: samsung gamescom 2026
proposed_title: Samsung na Gamescomu 2026: proč to zajímá i majitele Galaxy
action: CREATE
primary_lane: DISCOVERY
why_now: Samsung Newsroom Global: Gamescom 2026 gaming solutions.; GSC 281731 imp / pos 3.89 / CTR 23.64 %; GA4 22735 sessions / 29358 views
hard_evidence: Samsung Newsroom Global: Gamescom 2026 gaming solutions.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Napojit na gaming monitory, Galaxy, cloud gaming.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-12. Čínská odpověď na Galaxy Z TriFold přijde příští měsíc
```
candidate_id: SAM-12
exact_topic: galaxy z trifold china
proposed_title: Čínská odpověď na Galaxy Z TriFold přijde příští měsíc
action: CREATE
primary_lane: DISCOVERY
why_now: SamMobile: China answer to Galaxy Z TriFold coming next month.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
hard_evidence: SamMobile: China answer to Galaxy Z TriFold coming next month.; WP/Manticore: NO_DUPLICATE přes Manticore
unique_value: Konkurence jako tlak na Samsung; jasně označit jako konkurenční signál.
reality_status: PASS
information_age_status: FRESH
wp_check_status: NO_DUPLICATE přes Manticore
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-13. Galaxy Z Fold8 má možná až moc selfie kamer
```
candidate_id: SAM-13
exact_topic: galaxy z fold 8 selfie camera
proposed_title: Galaxy Z Fold8 má možná až moc selfie kamer
action: FOLLOW-UP
primary_lane: DISCOVER
why_now: SamMobile hot take; Fold8 témata běží v GA4.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
hard_evidence: SamMobile hot take; Fold8 témata běží v GA4.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Pixel 11 Pro vyzval Galaxy S26 Ultra. Která vlajková loď vám nabídne více?
unique_value: Názorový/analytický úhel pro redaktora, ne AI hotový článek.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Pixel 11 Pro vyzval Galaxy S26 Ultra. Která vlajková loď vám nabídne více?
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-14. Android Auto na Samsungu: tři nastavení, která dnes řeší nejvíc lidí
```
candidate_id: SAM-14
exact_topic: android auto samsung
proposed_title: Android Auto na Samsungu: tři nastavení, která dnes řeší nejvíc lidí
action: CREATE
primary_lane: SEO + CURRENT DEMAND
why_now: GSC android auto 124k imp; GA4 Android Auto články silné.; GSC 124797 imp / pos 5.04 / CTR 17.62 %; GA4 13421 sessions / 16605 views
hard_evidence: GSC android auto 124k imp; GA4 Android Auto články silné.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Android Auto se zbavuje té nejotravnější chyby. Bude připojení konečně stabilní? | Epic, Google a Samsung hlásí mír. Do Androidu míří snadnější instalace obchodů, 
unique_value: Praktický návod s odkazy na existující články.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Android Auto se zbavuje té nejotravnější chyby. Bude připojení konečně stabilní? | Epic, Google a Samsung hlásí mír. Do Androidu míří snadnější instalace obchodů, 
opportunity_score: 78
predictive_score: 80
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

## SAM-15. Jak uvolnit místo na Samsungu bez mazání aplikací
```
candidate_id: SAM-15
exact_topic: uvolnit misto samsung
proposed_title: Jak uvolnit místo na Samsungu bez mazání aplikací
action: FOLLOW-UP
primary_lane: DISCOVER
why_now: GA4 CZ článek 7 908 sessions / 32 547 views.; GA4 7912 sessions / 32560 views
hard_evidence: GA4 CZ článek 7 908 sessions / 32 547 views.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji | Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy
unique_value: Navazující tipy, ne duplicitní rewrite.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji | Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-16. Google Wallet redesign na Samsungu: co se změnilo
```
candidate_id: SAM-16
exact_topic: google wallet redesign
proposed_title: Google Wallet redesign na Samsungu: co se změnilo
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: GA4: Google Wallet redesign 7 007 sessions / 50 799 views.; GSC 10118 imp / pos 4.89 / CTR 24.85 %; GA4 7007 sessions / 50799 views
hard_evidence: GA4: Google Wallet redesign 7 007 sessions / 50 799 views.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Peněženka Google spouští velký redesign, na který všichni čekali. Podívejte se, 
unique_value: Aktualizovat s praktickými screenshot/body.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Peněženka Google spouští velký redesign, na který všichni čekali. Podívejte se, 
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-17. Samsung zdražuje čipy: zdraží i telefony střední třídy?
```
candidate_id: SAM-17
exact_topic: samsung chip price midrange
proposed_title: Samsung zdražuje čipy: zdraží i telefony střední třídy?
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: GA4 CZ článek 13 820 sessions.; GSC 281731 imp / pos 3.89 / CTR 23.64 %; GA4 22735 sessions / 29358 views
hard_evidence: GA4 CZ článek 13 820 sessions.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Příští telefon vás přijde draho. Samsung v tichosti chystá krok, který zničí dos
unique_value: Follow-up s dopadem na S26 FE a A řadu.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Příští telefon vás přijde draho. Samsung v tichosti chystá krok, který zničí dos
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-18. Které Galaxy telefony letos končí s podporou
```
candidate_id: SAM-18
exact_topic: galaxy end of life support
proposed_title: Které Galaxy telefony letos končí s podporou
action: UPDATE
primary_lane: SEO
why_now: GA4 lifecycle/support obsah silný globálně.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
hard_evidence: GA4 lifecycle/support obsah silný globálně.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Těmto telefonům Samsung Galaxy dochází čas. Zkontrolujte, zda mezi nimi není i t
unique_value: Aktualizovat modely, interní linky, FAQ.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Těmto telefonům Samsung Galaxy dochází čas. Zkontrolujte, zda mezi nimi není i t
opportunity_score: 78
predictive_score: 72
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-19. SwiftKey v One UI 9: proč ho půjde odstranit a koho se to týká
```
candidate_id: SAM-19
exact_topic: swiftkey samsung one ui 9
proposed_title: SwiftKey v One UI 9: proč ho půjde odstranit a koho se to týká
action: FOLLOW-UP
primary_lane: CURRENT DEMAND
why_now: GA4: SwiftKey/One UI 9 článek silný v JA.; GSC 8481 imp / pos 1 / CTR 56.18 %; GA4 8897 sessions / 13704 views
hard_evidence: GA4: SwiftKey/One UI 9 článek silný v JA.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy | Každý Samsung obsahuje umělou inteligenci. Ano, i ten váš
unique_value: CZ verze prakticky a stručně.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy | Každý Samsung obsahuje umělou inteligenci. Ano, i ten váš
opportunity_score: 78
predictive_score: 80
confidence: HIGH
final_write_gate: PASS
fail_reasons: -
```

## SAM-20. Zamrzlé Galaxy Watch: proč nedělat tovární reset jako první
```
candidate_id: SAM-20
exact_topic: frozen galaxy watch reset
proposed_title: Zamrzlé Galaxy Watch: proč nedělat tovární reset jako první
action: CREATE
primary_lane: SEO
why_now: Manticore/signály na Galaxy Watch problémy; evergreen řešení.; GA4 15000 sessions / 24381 views
hard_evidence: Manticore/signály na Galaxy Watch problémy; evergreen řešení.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji
unique_value: Servisní návod s jasnými kroky.
reality_status: PASS
information_age_status: FRESH
wp_check_status: SIMILAR_EXISTS přes Manticore: Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji
opportunity_score: 78
predictive_score: 72
confidence: MEDIUM
final_write_gate: PASS_CONDITIONAL
fail_reasons: -
```

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
- GitHub: NOT CHECKED - REASON — dnešní zadání trend článků, bez cred subagentů; GitHub vrstva neprimární
- beta programs: PARTIAL CHECKED — One UI beta přes media/news
- APK changes: NOT CHECKED - REASON — není v dnešním rozsahu
- regulatory/certification: PARTIAL CHECKED — Apple EU změny
- Reddit/forums/X/YouTube: NOT CHECKED - REASON — nepoužito jako hard evidence
- smaller specialist media: CHECKED — SamMobile, 9to5Google, MacRumors