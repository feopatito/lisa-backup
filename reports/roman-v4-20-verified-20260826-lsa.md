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

## Errata po Romanově kontrole 09:36
- LSA-04 byl chybně označen jako fact-check PASS. Správně: Apple keynote 2026 zatím není oficiálně oznámená, proto servisní článek „jak sledovat" = FINAL_WRITE_GATE FAIL.
- Příčina chyby: sezónní odhad `~9. září` byl povýšen na fakt.

## Tvrdá oprava
Pokud Manticore nebo WP ukazuje publikovaný nebo velmi podobný intent, `CREATE povoleno` je `NO` a akce je UPDATE/FOLLOW-UP/MERGE/MONITOR. To je rozdíl proti předchozí chybné verzi.

# LSA — letemsvetemapplem.eu — 20 slotů po WP kontrole

| # | Akce | CREATE povoleno | Titulek / intent | Global Trends | WP/Manticore verdict | Fact-check |
|---|---|---|---|---|---|---|
| LSA-01 | UPDATE | NO | Mac mini s M6: co Apple skutečně změnil a komu se vyplatí | global max 30/100, avg 2.4, last 26 | PUBLISHED/SIMILAR_EXISTS: Alza spustila předobjednávky Macu mini M6 a M5 Pro, objednávejte než se vyprodají / Nový M6 je vůbec první 2nm Apple čip, přináší obrovský skok hlavně v AI | PASS |
| LSA-02 | UPDATE | NO | Mac Studio s M5 Max a M5 Ultra: tichý upgrade pro profesionály | global max 8/100, avg 0.6, last 5 | PUBLISHED/SIMILAR_EXISTS: Pohled do útrob AI serverů Apple. Uniklé fotografie odhalují čip M5 a precizní chlazení / Nový M5 Ultra je dosud nejvýkonnější Apple čip, zvládne až 512 GB RAM | PASS |
| LSA-03 | CREATE | YES | M6 a M5 Ultra: proč Apple tlačí AI výkon do Maců | global max 0/100, avg 0.0, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| LSA-04 | MONITOR | NO | Apple keynote 2026: pouze monitoring, Apple ji oficiálně neoznámil | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS + NO_OFFICIAL_APPLE_INVITE: servisní článek jak sledovat je předčasný | FAIL |
| LSA-05 | UPDATE | NO | iPhone 18 Pro: co víme, co jsou úniky a co neříkat jako fakt | global max 100/100, avg 81.3, last 70 | PUBLISHED/SIMILAR_EXISTS: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme / Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v tento den | PASS |
| LSA-06 | FOLLOW-UP | NO | iPhone Ultra: proč skládací iPhone táhne Discover | global max 100/100, avg 78.9, last 96 | PUBLISHED/SIMILAR_EXISTS: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme / Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výrazně méně | PASS |
| LSA-07 | UPDATE | NO | Apple Maps reklamy jsou živé: kde se zobrazí a proč nejdou vypnout | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: Apple Maps zaplaví reklamy a to už letos v létě! / Apple může slavit! Apple Maps i Apple Ads vyvázly regulaci ze strany EU | PASS |
| LSA-08 | UPDATE | NO | ChatGPT na Macu a iMessage: co je reálně možné a kde jsou rizika | global max 1/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: ChatGPT dostal na Mac přístup k iMessage. Umí zprávy číst, analyzovat je i odesílat / iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těši | PASS |
| LSA-09 | FOLLOW-UP | NO | LEGO PlayStation 1 a proč LEGO teď funguje na LSA | global max 1/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: LEGO PlayStation 1 bude pořádná nostalgická pecka. Má být stejně velký jako originál a ukrývat herní překvapení / LEGO a Sony chystají senzaci. Vedle stavebnicového | PASS |
| LSA-10 | UPDATE | NO | iCloud trik na fotky: co ještě funguje a co Apple brzy utne | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: Tajný trik, jak na iCloudu získat neomezené úložiště pro vaše fotky zdarma. Apple ho brzy zatrhne / Apple vám v iOS 27 vezme další místo na iCloudu. Tohle se vyplat | PASS |
| LSA-11 | FOLLOW-UP | NO | CarPlay v iOS 27: změny, které řidiči uvidí jako první | global max 25/100, avg 3.4, last 0 | PUBLISHED/SIMILAR_EXISTS: CarPlay se v iOS 27 pořádně mění. Apple přidá funkce, které jsme chtěli roky / Apple CarPlay dostane v iOS 27 dvě nové funkce, které potěší miliony řidičů | PASS |
| LSA-12 | FOLLOW-UP | NO | Apple Watch 12: šest očekávání před keynote, jasně oddělená od faktů | global max 100/100, avg 61.1, last 75 | PUBLISHED/SIMILAR_EXISTS: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme / Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v tento den | PASS |
| LSA-13 | FOLLOW-UP | NO | AirPods 5 před zářím: co dává smysl čekat a co je jen rumor | global max 65/100, avg 35.2, last 51 | PUBLISHED/SIMILAR_EXISTS: Nejen iPhone 18 Pro a Ultra. Apple v září představí i nové AirPods 5 / Recenze FIXED Zen 10 Loop: 10 000 mAh, 30 W a dost energie i pro MacBook Air | PASS |
| LSA-14 | FOLLOW-UP | NO | iPhone 20 design: proč už teď zajímá čtenáře víc než by měl | global max 25/100, avg 3.6, last 0 | PUBLISHED/SIMILAR_EXISTS: Recenze MacBook Air M3: Velmi příjemný krok vpřed / Apple chystá něco opravdu velkého. Nové úniky ukazují, jak může vypadat iPhone budoucnosti | PASS |
| LSA-15 | FOLLOW-UP | NO | Nová Apple TV 4K a Siri Remote: malý update, velký dopad v obýváku | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: S novou Apple TV dorazí i vylepšený ovladač. Tohle je jedna z jeho nejžádanějších funkcí / Čekání končí. Nová Apple TV 4K dorazí na podzim a přinese chytřejší Siri  | PASS |
| LSA-16 | UPDATE | NO | Apple mění pravidla pro aplikace v EU: co to znamená pro majitele iPhonů | global max 68/100, avg 0.7, last 0 | PUBLISHED/SIMILAR_EXISTS: iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těšit / Historie a budoucnost nativních aplikací Applu | PASS |
| LSA-17 | UPDATE | NO | Která Apple zařízení už mají plnou podporu Wi-Fi 7 | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: Takto Apple oficiálně představil nové iPady 11 a iPady Air M3 / Apple oficiálně představil iPhone 16e: Výkonný přírůstek do rodiny iPhonů 16! | PASS |
| LSA-18 | CREATE | YES | BenQ iScreenBar pro iMac: doplněk, který Apple nikdy neudělal | global max 85/100, avg 0.5, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| LSA-19 | UPDATE | NO | Apple 40W Dynamic Power Adapter míří do dalších zemí: proč je zajímavý | global max 100/100, avg 10.5, last 0 | PUBLISHED/SIMILAR_EXISTS: Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkodobě až 60 W / Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkod | PASS |
| LSA-20 | UPDATE | NO | Apple otevřel Advanced Manufacturing Center v Houstonu: proč to není jen PR | global max 60/100, avg 0.4, last 0 | PUBLISHED/SIMILAR_EXISTS: Sklo pro iPhone a Apple Watch bude již brzy 100% z USA | PASS |

## Detailní sloty

### LSA-01 — Mac mini s M6: co Apple skutečně změnil a komu se vyplatí

- action: UPDATE
- create_allowed: NO
- exact_topic: mac mini m6
- primary_lane: CURRENT DEMAND
- why_now: Apple Newsroom + MacRumors/9to5Mac, čerstvé uvedení Mac mini.; GSC 8495 imp / pos 2.11 / CTR 9.59 %; GA4 1669 sessions / 8120 views
- hard_evidence: Apple Newsroom + MacRumors/9to5Mac, čerstvé uvedení Mac mini.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Nový M6 je vůbec první 2nm Apple čip, přináší obrovský skok hlavně v AI | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
- global_trends: global max 30/100, avg 2.4, last 26
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Alza spustila předobjednávky Macu mini M6 a M5 Pro, objednávejte než se vyprodají | Nový M6 je vůbec první 2nm Apple čip, přináší obrovský skok hlavně v AI
- matching_articles:
  - 2026-08-26T07:28:19.000Z — Alza spustila předobjednávky Macu mini M6 a M5 Pro, objednávejte než se vyprodají — https://www.letemsvetemapplem.eu/2026/08/26/alza-spustila-predobjednavky-macu-mini-m6-a-m5-pro-objednavejte-nez-se-vyprodaji/
  - 2026-08-25T14:32:29.000Z — Nový M6 je vůbec první 2nm Apple čip, přináší obrovský skok hlavně v AI — https://www.letemsvetemapplem.eu/2026/08/25/novy-m6-je-vubec-prvni-2nm-apple-cip-prinasi-obrovsky-skok-hlavne-v-ai/
  - 2026-08-25T14:04:37.000Z — Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výrazně méně — https://www.letemsvetemapplem.eu/2026/08/25/apple-po-peti-letech-predstavil-novy-cistici-hadrik-a-tentokrat-za-nej-chce-vyrazne-mene/
- unique_value: Rozebrat konfigurace, AI výkon a český nákupní kontext.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-02 — Mac Studio s M5 Max a M5 Ultra: tichý upgrade pro profesionály

- action: UPDATE
- create_allowed: NO
- exact_topic: mac studio m5 ultra
- primary_lane: CURRENT DEMAND
- why_now: Apple Newsroom: nový Mac Studio s M5 Max/M5 Ultra.; GSC 8495 imp / pos 2.11 / CTR 9.59 %; GA4 1669 sessions / 8120 views
- hard_evidence: Apple Newsroom: nový Mac Studio s M5 Max/M5 Ultra.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Nový M5 Ultra je dosud nejvýkonnější Apple čip, zvládne až 512 GB RAM | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
- global_trends: global max 8/100, avg 0.6, last 5
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Pohled do útrob AI serverů Apple. Uniklé fotografie odhalují čip M5 a precizní chlazení | Nový M5 Ultra je dosud nejvýkonnější Apple čip, zvládne až 512 GB RAM
- matching_articles:
  - 2026-08-26T07:15:16.000Z — Pohled do útrob AI serverů Apple. Uniklé fotografie odhalují čip M5 a precizní chlazení — https://www.letemsvetemapplem.eu/2026/08/26/pohled-do-utrob-ai-serveru-apple-unikle-fotografie-odhaluji-cip-m5-a-precizni-chlazeni/
  - 2026-08-25T15:06:53.000Z — Nový M5 Ultra je dosud nejvýkonnější Apple čip, zvládne až 512 GB RAM — https://www.letemsvetemapplem.eu/2026/08/25/novy-m5-ultra-je-dosud-nejvykonnejsi-apple-cip-zvladne-az-512-gb-ram/
  - 2026-08-25T14:04:37.000Z — Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výrazně méně — https://www.letemsvetemapplem.eu/2026/08/25/apple-po-peti-letech-predstavil-novy-cistici-hadrik-a-tentokrat-za-nej-chce-vyrazne-mene/
- unique_value: Srovnat proti Mac mini M6 a vysvětlit pro koho je Studio.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-03 — M6 a M5 Ultra: proč Apple tlačí AI výkon do Maců

- action: CREATE
- create_allowed: YES
- exact_topic: m6 m5 ultra ai compute
- primary_lane: DISCOVERY
- why_now: Apple Newsroom: nové čipy M6/M5 Ultra a AI compute.; GA4 1160 sessions / 2219 views
- hard_evidence: Apple Newsroom: nové čipy M6/M5 Ultra a AI compute.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Přeložit technický čipový launch do uživatelských dopadů.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-04 — Apple keynote 2026: pouze monitoring, ne článek „jak sledovat"

- action: MONITOR
- create_allowed: NO
- exact_topic: Apple September/iPhone keynote 2026 status
- primary_lane: MONITOR / predictive lane
- why_now: Apple zatím neposlal oficiální pozvánku. Existuje jen sezónní okno a odhady médií.
- hard_evidence: Apple Newsroom search nevrátil oficiální September/iPhone event invite; 9to5Mac výslovně píše, že Apple invitations ještě neodeslal.
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS + NO_OFFICIAL_APPLE_INVITE. Servisní článek „jak sledovat" je předčasný a nesmí projít fact-checkem.
- matching_articles:
  - 2026-08-25T10:02:49.000Z — Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v tento den — https://www.letemsvetemapplem.eu/2026/08/25/apple-uz-brzy-rozesle-pozvanky-na-nejvetsi-keynote-roku-iphone-18-pro-dorazi-v-tento-den/
- unique_value: Až po oficiální pozvánce připravit servisní článek s časem v ČR a streamem. Do té doby jen monitor.
- reality_status: FAIL_FOR_CREATE
- information_age_status: UNCERTAIN
- final_write_gate: FAIL

### LSA-05 — iPhone 18 Pro: co víme, co jsou úniky a co neříkat jako fakt

- action: UPDATE
- create_allowed: NO
- exact_topic: iphone 18 pro
- primary_lane: CURRENT DEMAND
- why_now: GSC: iPhone 18 Pro patří mezi nejsilnější LSA dotazy.; GSC 680779 imp / pos 1.35 / CTR 4.89 %; GA4 4712 sessions / 51935 views
- hard_evidence: GSC: iPhone 18 Pro patří mezi nejsilnější LSA dotazy.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v 
- global_trends: global max 100/100, avg 81.3, last 70
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v tento den
- matching_articles:
  - 2026-08-25T18:02:53.000Z — Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme — https://www.letemsvetemapplem.eu/2026/08/25/apple-watch-12-se-blizi-techto-6-veci-od-nich-ocekavame/
  - 2026-08-25T10:02:49.000Z — Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v tento den — https://www.letemsvetemapplem.eu/2026/08/25/apple-uz-brzy-rozesle-pozvanky-na-nejvetsi-keynote-roku-iphone-18-pro-dorazi-v-tento-den/
  - 2026-08-25T09:02:07.000Z — Nejen iPhone 18 Pro a Ultra. Apple v září představí i nové AirPods 5 — https://www.letemsvetemapplem.eu/2026/08/25/nejen-iphone-18-pro-a-ultra-apple-v-zari-predstavi-i-nove-airpods-5/
- unique_value: Oddělit ověřené informace od leaků, vyčistit záměny intentu.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-06 — iPhone Ultra: proč skládací iPhone táhne Discover

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: iphone ultra
- primary_lane: DISCOVER
- why_now: GA4: skládací iPhone Ultra měl vysoké pageviews; GSC iPhone Ultra silný.; GSC 680779 imp / pos 1.35 / CTR 4.89 %; GA4 4712 sessions / 51935 views
- hard_evidence: GA4: skládací iPhone Ultra měl vysoké pageviews; GSC iPhone Ultra silný.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výr
- global_trends: global max 100/100, avg 78.9, last 96
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výrazně méně
- matching_articles:
  - 2026-08-25T18:02:53.000Z — Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme — https://www.letemsvetemapplem.eu/2026/08/25/apple-watch-12-se-blizi-techto-6-veci-od-nich-ocekavame/
  - 2026-08-25T14:04:37.000Z — Apple po pěti letech představil nový čisticí hadřík. A tentokrát za něj chce výrazně méně — https://www.letemsvetemapplem.eu/2026/08/25/apple-po-peti-letech-predstavil-novy-cistici-hadrik-a-tentokrat-za-nej-chce-vyrazne-mene/
  - 2026-08-25T11:04:48.000Z — Apple Watch Ultra 3 chystají satelitní revoluci. Co přinese zářijový update? — https://www.letemsvetemapplem.eu/2026/08/25/apple-watch-ultra-3-update/
- unique_value: Cena/dostupnost/komu dává smysl, ne opakování prvních dojmů.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-07 — Apple Maps reklamy jsou živé: kde se zobrazí a proč nejdou vypnout

- action: UPDATE
- create_allowed: NO
- exact_topic: apple maps ads reklamy
- primary_lane: CURRENT DEMAND
- why_now: MacRumors/AppleInsider: reklamy Apple Maps live v USA/Kanadě.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
- hard_evidence: MacRumors/AppleInsider: reklamy Apple Maps live v USA/Kanadě.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple Maps zaplaví reklamy a to už letos v létě! | Apple může slavit! Apple Maps i Apple Ads vyvázly regulaci ze strany EU
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Apple Maps zaplaví reklamy a to už letos v létě! | Apple může slavit! Apple Maps i Apple Ads vyvázly regulaci ze strany EU
- matching_articles:
  - 2026-03-24T11:04:16.000Z — Apple Maps zaplaví reklamy a to už letos v létě! — https://www.letemsvetemapplem.eu/2026/03/24/apple-maps-zaplavi-reklamy-a-to-uz-letos-v-lete/
  - 2026-02-09T14:00:40.000Z — Apple může slavit! Apple Maps i Apple Ads vyvázly regulaci ze strany EU — https://www.letemsvetemapplem.eu/2026/02/09/apple-muze-slavit-apple-maps-i-apple-ads-vyvazly-regulaci-ze-strany-eu/
  - 2026-01-23T20:00:28.000Z — Apple začne v App Store od března 2026 zobrazovat více reklam a změní způsob, jak hledáme aplikace — https://www.letemsvetemapplem.eu/2026/01/23/apple-zacne-v-app-store-od-brezna-2026-zobrazovat-vice-reklam-a-zmeni-zpusob-jak-hledame-aplikace/
- unique_value: Navázat na starší článek; vysvětlit praktický dopad pro uživatele.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-08 — ChatGPT na Macu a iMessage: co je reálně možné a kde jsou rizika

- action: UPDATE
- create_allowed: NO
- exact_topic: chatgpt imessage mac
- primary_lane: CURRENT DEMAND
- why_now: Google Trends via pytrends ChatGPT 50/100 + Moula/GSC: ChatGPT 32k imp, slabý CTR; Manticore našel fresh články.; GA4 1669 sessions / 8120 views
- hard_evidence: Moula/GSC: ChatGPT 32k imp, slabý CTR; Manticore našel fresh články.; WP/Manticore: SIMILAR_EXISTS přes Manticore: ChatGPT dostal na Mac přístup k iMessage. Umí zprávy číst, analyzovat je i odesí | iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těšit
- global_trends: global max 1/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: ChatGPT dostal na Mac přístup k iMessage. Umí zprávy číst, analyzovat je i odesílat | iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těšit
- matching_articles:
  - 2026-08-21T09:06:01.000Z — ChatGPT dostal na Mac přístup k iMessage. Umí zprávy číst, analyzovat je i odesílat — https://www.letemsvetemapplem.eu/2026/08/21/chatgpt-dostal-na-mac-pristup-k-imessage-umi-zpravy-cist-analyzovat-je-i-odesilat/
  - 2024-03-23T23:01:16.000Z — iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těšit — https://www.letemsvetemapplem.eu/2024/03/24/ios-18-mozne-datum-vydani-nove-funkce-podporovana-zarizeni-a-na-co-dalsiho-se-muzeme-tesit/
- unique_value: Zlepšit CTR konkrétním bezpečnostním a praktickým úhlem.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-09 — LEGO PlayStation 1 a proč LEGO teď funguje na LSA

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: lego playstation 1
- primary_lane: DISCOVER
- why_now: GSC LEGO 68k imp; GA4 LEGO články vysoké views.; GSC 71079 imp / pos 6.48 / CTR 3.71 %; GA4 5111 sessions / 54080 views
- hard_evidence: GSC LEGO 68k imp; GA4 LEGO články vysoké views.; WP/Manticore: SIMILAR_EXISTS přes Manticore: LEGO PlayStation 1 bude pořádná nostalgická pecka. Má být stejně velký jako orig | LEGO a Sony chystají senzaci. Vedle stavebnicového PlayStationu dorazí i legendá
- global_trends: global max 1/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: LEGO PlayStation 1 bude pořádná nostalgická pecka. Má být stejně velký jako originál a ukrývat herní překvapení | LEGO a Sony chystají senzaci. Vedle stavebnicového PlayStationu do
- matching_articles:
  - 2026-08-24T16:03:55.000Z — LEGO PlayStation 1 bude pořádná nostalgická pecka. Má být stejně velký jako originál a ukrývat herní překvapení — https://www.letemsvetemapplem.eu/2026/08/24/lego-playstation-1-bude-poradna-nostalgicka-pecka-ma-byt-stejne-velky-jako-original-a-ukryvat-herni-prekvapeni/
  - 2026-08-04T16:03:20.000Z — LEGO a Sony chystají senzaci. Vedle stavebnicového PlayStationu dorazí i legendární Astro Bot a bude zdarma — https://www.letemsvetemapplem.eu/2026/08/04/lego-a-sony-chystaji-senzaci-vedle-stavebnicoveho-playstationu-dorazi-i-legendarni-astro-bot-a-bude-zdarma/
  - 2026-03-16T19:04:25.000Z — LEGO prý chystá PlayStation 1, legendární konzole by mohla dorazit už letos na Vánoce — https://www.letemsvetemapplem.eu/2026/03/16/lego-72306-playstation-1/
- unique_value: Zachytit nostalgii/popkulturu, ověřit intent před publikací.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-10 — iCloud trik na fotky: co ještě funguje a co Apple brzy utne

- action: UPDATE
- create_allowed: NO
- exact_topic: icloud uloziste fotky
- primary_lane: DISCOVER
- why_now: GA4: iCloud storage článek jeden z top výkonů týdne.; GSC 2570 imp / pos 4.49 / CTR 17.16 %; GA4 5495 sessions / 14566 views
- hard_evidence: GA4: iCloud storage článek jeden z top výkonů týdne.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Tajný trik, jak na iCloudu získat neomezené úložiště pro vaše fotky zdarma. Appl | Apple vám v iOS 27 vezme další místo na iCloudu. Tohle se vyplatí vědět
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Tajný trik, jak na iCloudu získat neomezené úložiště pro vaše fotky zdarma. Apple ho brzy zatrhne | Apple vám v iOS 27 vezme další místo na iCloudu. Tohle se vyplatí vědět
- matching_articles:
  - 2026-08-21T22:01:17.000Z — Tajný trik, jak na iCloudu získat neomezené úložiště pro vaše fotky zdarma. Apple ho brzy zatrhne — https://www.letemsvetemapplem.eu/2026/08/22/tajny-trik-jak-na-icloudu-ziskat-neomezene-uloziste-pro-vase-fotky-zdarma-apple-ho-brzy-zatrhne/
  - 2026-08-21T18:04:42.000Z — Apple vám v iOS 27 vezme další místo na iCloudu. Tohle se vyplatí vědět — https://www.letemsvetemapplem.eu/2026/08/21/apple-vam-v-ios-27-vezme-dalsi-misto-na-icloudu-tohle-se-vyplati-vedet/
  - 2026-06-27T11:01:02.000Z — Co je NAS a proč může být lepší volbou než cloud — https://www.letemsvetemapplem.eu/2026/06/27/co-je-nas-a-proc-muze-byt-lepsi-volbou-nez-cloud/
- unique_value: Praktická kontrola aktuálnosti a limitů, interní link na původní článek.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-11 — CarPlay v iOS 27: změny, které řidiči uvidí jako první

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: carplay ios 27
- primary_lane: CURRENT DEMAND
- why_now: GA4: CarPlay/iOS 27 článek ve výkonu týdne.; GA4 3251 sessions / 5918 views
- hard_evidence: GA4: CarPlay/iOS 27 článek ve výkonu týdne.; WP/Manticore: SIMILAR_EXISTS přes Manticore: CarPlay se v iOS 27 pořádně mění. Apple přidá funkce, které jsme chtěli roky | Apple CarPlay dostane v iOS 27 dvě nové funkce, které potěší miliony řidičů
- global_trends: global max 25/100, avg 3.4, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: CarPlay se v iOS 27 pořádně mění. Apple přidá funkce, které jsme chtěli roky | Apple CarPlay dostane v iOS 27 dvě nové funkce, které potěší miliony řidičů
- matching_articles:
  - 2026-08-20T18:05:45.000Z — CarPlay se v iOS 27 pořádně mění. Apple přidá funkce, které jsme chtěli roky — https://www.letemsvetemapplem.eu/2026/08/20/carplay-se-v-ios-27-poradne-meni-apple-prida-funkce-ktere-jsme-chteli-roky/
  - 2026-08-09T14:06:52.000Z — Apple CarPlay dostane v iOS 27 dvě nové funkce, které potěší miliony řidičů — https://www.letemsvetemapplem.eu/2026/08/09/apple-carplay-dostane-v-ios-27-dve-nove-funkce-ktere-potesi-miliony-ridicu/
  - 2026-07-10T18:04:24.000Z — Apple odhalil všechny novinky pro CarPlay v iOS 27. Tohle jsou funkce, které ocení prakticky každý řidič — https://www.letemsvetemapplem.eu/2026/07/10/apple-odhalil-vsechny-novinky-pro-carplay-v-ios-27-tohle-jsou-funkce-ktere-oceni-prakticky-kazdy-ridic/
- unique_value: Konkrétní use-cases místo obecného výčtu funkcí.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-12 — Apple Watch 12: šest očekávání před keynote, jasně oddělená od faktů

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: apple watch 12
- primary_lane: CURRENT DEMAND
- why_now: Manticore ukazuje fresh článek; Apple event proximity.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
- hard_evidence: Manticore ukazuje fresh článek; Apple event proximity.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v 
- global_trends: global max 100/100, avg 61.1, last 75
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme | Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v tento den
- matching_articles:
  - 2026-08-25T18:02:53.000Z — Apple Watch 12 se blíží. Těchto 6 věcí od nich očekáváme — https://www.letemsvetemapplem.eu/2026/08/25/apple-watch-12-se-blizi-techto-6-veci-od-nich-ocekavame/
  - 2026-08-25T10:02:49.000Z — Apple už brzy rozešle pozvánky na největší Keynote roku. iPhone 18 Pro dorazí v tento den — https://www.letemsvetemapplem.eu/2026/08/25/apple-uz-brzy-rozesle-pozvanky-na-nejvetsi-keynote-roku-iphone-18-pro-dorazi-v-tento-den/
  - 2026-08-21T07:04:02.000Z — Apple Watch se vrací k luxusu. Apple má letos znovu nabídnout keramickou verzi — https://www.letemsvetemapplem.eu/2026/08/21/apple-watch-se-vraci-k-luxusu-apple-ma-letos-znovu-nabidnout-keramickou-verzi/
- unique_value: Checklist fakt/leak/spekulace, nepovyšovat úniky na potvrzení.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-13 — AirPods 5 před zářím: co dává smysl čekat a co je jen rumor

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: airpods 5
- primary_lane: CURRENT DEMAND
- why_now: Manticore fresh AirPods 5 zmínky; Apple event proximity.; GA4 1463 sessions / 4997 views
- hard_evidence: Manticore fresh AirPods 5 zmínky; Apple event proximity.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Nejen iPhone 18 Pro a Ultra. Apple v září představí i nové AirPods 5 | Recenze FIXED Zen 10 Loop: 10 000 mAh, 30 W a dost energie i pro MacBook Air
- global_trends: global max 65/100, avg 35.2, last 51
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Nejen iPhone 18 Pro a Ultra. Apple v září představí i nové AirPods 5 | Recenze FIXED Zen 10 Loop: 10 000 mAh, 30 W a dost energie i pro MacBook Air
- matching_articles:
  - 2026-08-25T09:02:07.000Z — Nejen iPhone 18 Pro a Ultra. Apple v září představí i nové AirPods 5 — https://www.letemsvetemapplem.eu/2026/08/25/nejen-iphone-18-pro-a-ultra-apple-v-zari-predstavi-i-nove-airpods-5/
  - 2026-08-23T10:03:56.000Z — Recenze FIXED Zen 10 Loop: 10 000 mAh, 30 W a dost energie i pro MacBook Air — https://www.letemsvetemapplem.eu/2026/08/23/recenze-fixed-zen-10-loop-10-000-mah-30-w-a-dost-energie-i-pro-macbook-air/
  - 2026-08-18T13:06:28.000Z — Apple omylem prozradil AirPods 5. Nová generace dorazí ve dvou verzích — https://www.letemsvetemapplem.eu/2026/08/18/apple-omylem-prozradil-airpods-5-nova-generace-dorazi-ve-dvou-verzich/
- unique_value: Vysvětlit pravděpodobnost a praktický dopad pro nákup.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-14 — iPhone 20 design: proč už teď zajímá čtenáře víc než by měl

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: iphone 20 design
- primary_lane: DISCOVER
- why_now: GA4: iPhone 20 design článek má silné views.; GSC 680779 imp / pos 1.35 / CTR 4.89 %; GA4 4712 sessions / 51935 views
- hard_evidence: GA4: iPhone 20 design článek má silné views.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple chystá něco opravdu velkého. Nové úniky ukazují, jak může vypadat iPhone b | Bloomberg: Revoluční iPhone 20 není zrušen, bude ale vypadat jinak než původně m
- global_trends: global max 25/100, avg 3.6, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Recenze MacBook Air M3: Velmi příjemný krok vpřed | Apple chystá něco opravdu velkého. Nové úniky ukazují, jak může vypadat iPhone budoucnosti
- matching_articles:
  - 2024-03-08T23:01:10.000Z — Recenze MacBook Air M3: Velmi příjemný krok vpřed — https://www.letemsvetemapplem.eu/2024/03/09/recenze-macbook-air-m3-velmi-prijemny-krok-vpred/
  - 2026-08-20T06:04:06.000Z — Apple chystá něco opravdu velkého. Nové úniky ukazují, jak může vypadat iPhone budoucnosti — https://www.letemsvetemapplem.eu/2026/08/20/apple-chysta-neco-opravdu-velkeho-nove-uniky-ukazuji-jak-muze-vypadat-iphone-budoucnosti/
  - 2026-08-11T10:05:49.000Z — Bloomberg: Revoluční iPhone 20 není zrušen, bude ale vypadat jinak než původně měl — https://www.letemsvetemapplem.eu/2026/08/11/bloomberg-revolucni-iphone-20-neni-zrusen-bude-ale-vypadat-jinak-nez-puvodne-mel/
- unique_value: Trendový follow-up s opatrným rámováním vzdálené budoucnosti.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-15 — Nová Apple TV 4K a Siri Remote: malý update, velký dopad v obýváku

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: apple tv 4k siri remote
- primary_lane: CURRENT DEMAND
- why_now: GA4: Apple TV/Siri Remote článek fungoval.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
- hard_evidence: GA4: Apple TV/Siri Remote článek fungoval.; WP/Manticore: SIMILAR_EXISTS přes Manticore: S novou Apple TV dorazí i vylepšený ovladač. Tohle je jedna z jeho nejžádanějšíc | Čekání končí. Nová Apple TV 4K dorazí na podzim a přinese chytřejší Siri i přepr
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: S novou Apple TV dorazí i vylepšený ovladač. Tohle je jedna z jeho nejžádanějších funkcí | Čekání končí. Nová Apple TV 4K dorazí na podzim a přinese chytřejší Siri i přepracovaný o
- matching_articles:
  - 2026-08-19T20:03:57.000Z — S novou Apple TV dorazí i vylepšený ovladač. Tohle je jedna z jeho nejžádanějších funkcí — https://www.letemsvetemapplem.eu/2026/08/19/s-novou-apple-tv-dorazi-i-vylepseny-ovladac-tohle-je-jedna-z-jeho-nejzadanejsich-funkci/
  - 2026-06-23T22:02:06.000Z — Čekání končí. Nová Apple TV 4K dorazí na podzim a přinese chytřejší Siri i přepracovaný ovladač — https://www.letemsvetemapplem.eu/2026/06/24/cekani-konci-nova-apple-tv-4k-dorazi-na-podzim-a-prinese-chytrejsi-siri-i-prepracovany-ovladac/
  - 2026-06-02T04:06:11.000Z — Apple chystá podzimní novinky. Konečně dorazí nová Apple TV i HomePod mini — https://www.letemsvetemapplem.eu/2026/06/02/apple-chysta-podzimni-novinky-konecne-dorazi-nova-apple-tv-i-homepod-mini/
- unique_value: Praktický dopad ovladače, Wi-Fi, HomeKit, cena.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-16 — Apple mění pravidla pro aplikace v EU: co to znamená pro majitele iPhonů

- action: UPDATE
- create_allowed: NO
- exact_topic: apple european union apps changes
- primary_lane: CURRENT DEMAND
- why_now: Apple Newsroom: changes for apps in EU.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
- hard_evidence: Apple Newsroom: changes for apps in EU.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 68/100, avg 0.7, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těšit | Historie a budoucnost nativních aplikací Applu
- matching_articles:
  - 2024-03-23T23:01:16.000Z — iOS 18: Představení, nové funkce, kompatibilita a na co dalšího se můžeme těšit — https://www.letemsvetemapplem.eu/2024/03/24/ios-18-mozne-datum-vydani-nove-funkce-podporovana-zarizeni-a-na-co-dalsiho-se-muzeme-tesit/
  - 2020-03-01T11:00:43.000Z — Historie a budoucnost nativních aplikací Applu — https://www.letemsvetemapplem.eu/2020/03/01/historie-a-budoucnost-nativnich-aplikaci-applu/
  - 2016-05-01T17:36:20.000Z — 101 nejlepších tipů a triků, které musí znát každý majitel iPhonu — https://www.letemsvetemapplem.eu/2016/05/01/101-tipu-a-triku/
- unique_value: Přeložit regulatorní změnu do češtiny a praktických dopadů.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-17 — Která Apple zařízení už mají plnou podporu Wi-Fi 7

- action: UPDATE
- create_allowed: NO
- exact_topic: wifi 7 apple devices
- primary_lane: SEO + CURRENT DEMAND
- why_now: 9to5Mac: přehled zařízení s Wi-Fi 7.; GA4 3251 sessions / 5918 views
- hard_evidence: 9to5Mac: přehled zařízení s Wi-Fi 7.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Kompetní historie Apple iPhone: jak vznikal hudební přehrávač, telefon a interne
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Takto Apple oficiálně představil nové iPady 11 a iPady Air M3 | Apple oficiálně představil iPhone 16e: Výkonný přírůstek do rodiny iPhonů 16!
- matching_articles:
  - 2025-03-04T15:00:23.000Z — Takto Apple oficiálně představil nové iPady 11 a iPady Air M3 — https://www.letemsvetemapplem.eu/2025/03/04/takto-apple-oficialne-predstavil-nove-ipady-11-a-ipady-air-m3/
  - 2025-02-19T16:11:05.000Z — Apple oficiálně představil iPhone 16e: Výkonný přírůstek do rodiny iPhonů 16! — https://www.letemsvetemapplem.eu/2025/02/19/apple-oficialne-predstavil-iphone-16e-vykonny-prurustek-do-rodiny-iphonu-16/
  - 2024-12-14T18:00:48.000Z — Jsou levné Androidy opravdu tak špatné? Recenze Vivo V40 SE vás vyvede z omylu — https://www.letemsvetemapplem.eu/2024/12/14/vivo-v40-se-recenze/
- unique_value: Nákupní přehled pro iPhone/Mac/iPad uživatele.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-18 — BenQ iScreenBar pro iMac: doplněk, který Apple nikdy neudělal

- action: CREATE
- create_allowed: YES
- exact_topic: benq iscreenbar imac
- primary_lane: DISCOVERY
- why_now: MacRumors: BenQ iScreenBar for iMac.
- hard_evidence: MacRumors: BenQ iScreenBar for iMac.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 85/100, avg 0.5, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Produktový praktický tip pro LSA publikum.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-19 — Apple 40W Dynamic Power Adapter míří do dalších zemí: proč je zajímavý

- action: UPDATE
- create_allowed: NO
- exact_topic: 40w dynamic power adapter
- primary_lane: CURRENT DEMAND
- why_now: MacRumors: adaptér expanduje do dalších zemí.
- hard_evidence: MacRumors: adaptér expanduje do dalších zemí.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkodobě a | iPad Pro M5 v prvních recenzích! Jaký je nejvýkonnější tablet současnosti v reál
- global_trends: global max 100/100, avg 10.5, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkodobě až 60 W | Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkodobě až 60 W
- matching_articles:
  - 2026-08-26T05:52:52.000Z — Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkodobě až 60 W — https://www.letemsvetemapplem.eu/2026/08/26/apple-konecne-privezl-do-evropy-svou-supernabijecku-pro-iphone-umi-kratkodobe-az-60-w/
  - 2026-08-26T05:52:52.000Z — Apple konečně přivezl do Evropy svou supernabíječku pro iPhone. Umí krátkodobě až 60 W — https://www.letemsvetemapplem.eu/2026/08/26/apple-konecne-privezl-do-evropy-svou-supernabijecku-pro-iphone-umi-kratkodobe-az-60-w/
  - 2025-10-21T14:13:02.000Z — iPad Pro M5 v prvních recenzích! Jaký je nejvýkonnější tablet současnosti v reálu? — https://www.letemsvetemapplem.eu/2025/10/21/ipad-pro-m5-v-prvnich-recenzich-jaky-je-nejvykonnejsi-tablet-soucasnosti-v-realu/
- unique_value: Vysvětlit nabíjení, kompatibilitu a zda čekat CZ dostupnost.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### LSA-20 — Apple otevřel Advanced Manufacturing Center v Houstonu: proč to není jen PR

- action: UPDATE
- create_allowed: NO
- exact_topic: apple manufacturing center houston
- primary_lane: DISCOVERY
- why_now: Apple Newsroom: nové manufacturing centrum.; GSC 4444 imp / pos 1.12 / CTR 79.43 %; GA4 53227 sessions / 66370 views
- hard_evidence: Apple Newsroom: nové manufacturing centrum.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Sklo pro iPhone a Apple Watch bude již brzy 100% z USA
- global_trends: global max 60/100, avg 0.4, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Sklo pro iPhone a Apple Watch bude již brzy 100% z USA
- matching_articles:
  - 2025-08-08T08:00:44.000Z — Sklo pro iPhone a Apple Watch bude již brzy 100% z USA — https://www.letemsvetemapplem.eu/2025/08/08/sklo-pro-iphone-a-apple-watch-bude-brzy-100-z-usa/
- unique_value: Napojit na čipy, dodavatelský řetězec a Apple Intelligence.
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