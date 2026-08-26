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

# Samsung Magazine — samsungmagazine.eu — 20 slotů po WP kontrole

| # | Akce | CREATE povoleno | Titulek / intent | Global Trends | WP/Manticore verdict | Fact-check |
|---|---|---|---|---|---|---|
| SAM-01 | UPDATE | NO | One UI 9 Beta 6: co opravuje a kdo ji dostává | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? / Samsung vydává 6. betu One UI 9 pro Galaxy S26. Opravuje fotoaparát i rozb | PASS |
| SAM-02 | UPDATE | NO | Gemini na Samsungu: obří zájem, mizerný CTR, praktický návod | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Gemini Intelligence přináší do Androidu autonomii. Známe seznam telefonů, které ji dostanou / Stabilní verze One UI 9: Na která zařízení dorazí jako první a jak se  | PASS |
| SAM-03 | UPDATE | NO | Galaxy S26 vs S25: má upgrade smysl? | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Galaxy S26 vs. S25: Vyplatí se upgrade na novou vlajku, když Samsung šetřil na inovacích? / Galaxy Z Fold8 Ultra dostane nečekaný upgrade displeje. Nejde jen o méně | PASS |
| SAM-04 | FOLLOW-UP | NO | Galaxy S26 FE: co sledovat po eventu 27. srpna | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Samsung Galaxy S26 FE: cena, datum a co čekat od Galaxy Event August 2026 / Zapište si toto datum. Samsung prozradil, kdy představí Galaxy S26 FE a další novinky | PASS |
| SAM-05 | UPDATE | NO | Galaxy Watch Ultra 2: recenze a srovnání s Watch Ultra a Garminem | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Samsung Galaxy Z Fold8 Ultra recenze: Je to špička, ale trochu nuda / Nové skládačky od Samsungu stojí ranec. Tímto trikem ale můžete ušetřit desítky tisíc | PASS |
| SAM-06 | UPDATE | NO | Jak snadno přejít na Galaxy Z Fold8 | global max 100/100, avg 0.6, last 0 | PUBLISHED/SIMILAR_EXISTS: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? / Skvělá aplikace od Samsungu má velký problém. Uživatelům po přechodu na no | PASS |
| SAM-07 | CREATE | YES | Galaxy Buds4 Pro mají uznaný Hi-Fi zvuk: co to znamená v praxi | global max 0/100, avg 0.0, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| SAM-08 | UPDATE | NO | Srpnové bezpečnostní aktualizace Galaxy: kdo je dostává | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? / Tato Samsung zařízení právě dostávají srpnovou bezpečnostní aktualizaci 20 | PASS |
| SAM-09 | CREATE | YES | Galaxy S27 Ultra leak: vodorovný fotomodul a riziko iPhone looku | global max 0/100, avg 0.0, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| SAM-10 | UPDATE | NO | Good Lock MultiStar/FlipShot: malá funkce pro skládačky, velký rozdíl | global max 0/100, avg 0.0, last 0 | PUBLISHED/SIMILAR_EXISTS: Manticore hit | PASS |
| SAM-11 | CREATE | YES | Samsung na Gamescomu 2026: proč to zajímá i majitele Galaxy | global max 17/100, avg 0.2, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| SAM-12 | CREATE | YES | Čínská odpověď na Galaxy Z TriFold přijde příští měsíc | global max 0/100, avg 0.0, last 0 | MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS | PASS |
| SAM-13 | FOLLOW-UP | NO | Galaxy Z Fold8 má možná až moc selfie kamer | global max 14/100, avg 0.1, last 0 | PUBLISHED/SIMILAR_EXISTS: Recenze Samsung Galaxy Z Flip8: Baví mě víc než kdy dřív, i tak mě na něm ale něco štve / Pixel 11 Pro vyzval Galaxy S26 Ultra. Která vlajková loď vám nabídne více? | PASS |
| SAM-14 | UPDATE | NO | Android Auto na Samsungu: tři nastavení, která dnes řeší nejvíc lidí | global max 100/100, avg 49.3, last 46 | PUBLISHED/SIMILAR_EXISTS: Android Auto se zbavuje té nejotravnější chyby. Bude připojení konečně stabilní? / Epic, Google a Samsung hlásí mír. Do Androidu míří snadnější instalace obchodů, a | PASS |
| SAM-15 | FOLLOW-UP | NO | Jak uvolnit místo na Samsungu bez mazání aplikací | global max 18/100, avg 0.2, last 0 | PUBLISHED/SIMILAR_EXISTS: Co jsou na Samsung telefonu Ostatní soubory? S One UI 8 je konečně můžete smazat / Jak v Galerii na Samsung telefonu odstranit duplicitní obrázky | PASS |
| SAM-16 | FOLLOW-UP | NO | Google Wallet redesign na Samsungu: co se změnilo | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Peněženka Google spouští velký redesign, na který všichni čekali. Podívejte se, jaké novinky konečně dorazily | PASS |
| SAM-17 | FOLLOW-UP | NO | Samsung zdražuje čipy: zdraží i telefony střední třídy? | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Příští telefon vás přijde draho. Samsung v tichosti chystá krok, který zničí dostupné smartphony / Samsung plošně zdražuje modely řad Galaxy M a F. Nejvíc to dopadn | PASS |
| SAM-18 | UPDATE | NO | Které Galaxy telefony letos končí s podporou | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Nenechte se zmást papírovou kapacitou. Baterie Galaxy S26 Ultra funguje úplně jinak, než si myslíte / Samsung definitivně pohřbívá S Pen, v Galaxy Z Fold8 ho nejspí | PASS |
| SAM-19 | FOLLOW-UP | NO | SwiftKey v One UI 9: proč ho půjde odstranit a koho se to týká | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy nechtěli / Každý Samsung obsahuje umělou inteligenci. Ano, i ten váš | PASS |
| SAM-20 | UPDATE | NO | Zamrzlé Galaxy Watch: proč nedělat tovární reset jako první | GLOBAL_TRENDS_UNAVAILABLE | PUBLISHED/SIMILAR_EXISTS: Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji | PASS |

## Detailní sloty

### SAM-01 — One UI 9 Beta 6: co opravuje a kdo ji dostává

- action: UPDATE
- create_allowed: NO
- exact_topic: one ui 9 beta 6
- primary_lane: CURRENT DEMAND
- why_now: Android Central + Samsung/One UI signály; GSC one ui 132k+ imp.; GSC 135824 imp / pos 4.02 / CTR 16.78 %; GA4 15000 sessions / 24381 views
- hard_evidence: Android Central + Samsung/One UI signály; GSC one ui 132k+ imp.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Samsung vydává 6. betu One UI 9 pro Galaxy S26. Opravuje fotoaparát i rozbité wi | Ostrá verze One UI 9 má zpoždění. Samsung pro Galaxy S26 chystá další betu
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? | Samsung vydává 6. betu One UI 9 pro Galaxy S26. Opravuje fotoaparát i rozbité widgety (Akt
- matching_articles:
  - 2026-08-24T04:03:04.000Z — Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? — https://samsungmagazine.eu/2026/08/24/prehled-aktualizaci-samsung/
  - 2026-08-25T10:49:40.000Z — Samsung vydává 6. betu One UI 9 pro Galaxy S26. Opravuje fotoaparát i rozbité widgety (Aktualizováno) — https://samsungmagazine.eu/2026/08/25/samsung-vydava-6-betu-one-ui-9-pro-galaxy-s26-opravuje-fotoaparat-i-rozbite-widgety/
  - 2026-08-25T09:04:59.000Z — Ostrá verze One UI 9 má zpoždění. Samsung pro Galaxy S26 chystá další betu — https://samsungmagazine.eu/2026/08/25/samsung-galaxy-s26-one-ui-9-beta-6-delay/
- unique_value: Přesný stav bety, opravy, dostupnost, interní linky.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-02 — Gemini na Samsungu: obří zájem, mizerný CTR, praktický návod

- action: UPDATE
- create_allowed: NO
- exact_topic: gemini samsung
- primary_lane: SEO
- why_now: GSC/Moula: 224k imp, CTR 0.1 %.; GA4 22735 sessions / 29358 views
- hard_evidence: GSC/Moula: 224k imp, CTR 0.1 %.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Gemini Intelligence přináší do Androidu autonomii. Známe seznam telefonů, které  | Stabilní verze One UI 9: Na která zařízení dorazí jako první a jak se liší od be
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Gemini Intelligence přináší do Androidu autonomii. Známe seznam telefonů, které ji dostanou | Stabilní verze One UI 9: Na která zařízení dorazí jako první a jak se liší od bety? Ko
- matching_articles:
  - 2026-08-25T10:05:00.000Z — Gemini Intelligence přináší do Androidu autonomii. Známe seznam telefonů, které ji dostanou — https://samsungmagazine.eu/2026/08/25/samsung-gemini-intelligence/
  - 2026-08-25T05:55:27.000Z — Stabilní verze One UI 9: Na která zařízení dorazí jako první a jak se liší od bety? Kompletní přehled rolloutu — https://samsungmagazine.eu/2026/08/25/one-ui-9-update-list-features-samsung/
  - 2026-08-24T13:54:41.000Z — Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji — https://samsungmagazine.eu/2026/08/24/how-to-fix-frozen-galaxy-watch/
- unique_value: Přepsat angle na uživatelské otázky: kde je Gemini, co umí, vypnutí.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-03 — Galaxy S26 vs S25: má upgrade smysl?

- action: UPDATE
- create_allowed: NO
- exact_topic: galaxy s26 s25 upgrade
- primary_lane: SEO + CURRENT DEMAND
- why_now: GSC Samsung Galaxy/S26 silné dotazy.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
- hard_evidence: GSC Samsung Galaxy/S26 silné dotazy.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Galaxy Z Fold8 Ultra dostane nečekaný upgrade displeje. Nejde jen o méně viditel | Čeká nás po čtyřech letech změna? Galaxy S27 Pro a Ultra dostanou novinku, ktero
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Galaxy S26 vs. S25: Vyplatí se upgrade na novou vlajku, když Samsung šetřil na inovacích? | Galaxy Z Fold8 Ultra dostane nečekaný upgrade displeje. Nejde jen o méně viditelný ohyb
- matching_articles:
  - 2026-03-08T19:02:25.000Z — Galaxy S26 vs. S25: Vyplatí se upgrade na novou vlajku, když Samsung šetřil na inovacích? — https://samsungmagazine.eu/2026/03/08/galaxy-s26-ma-sice-vetsi-baterii-nabiji-se-ale-stejne-pomalu/
  - 2026-07-13T06:06:05.000Z — Galaxy Z Fold8 Ultra dostane nečekaný upgrade displeje. Nejde jen o méně viditelný ohyb — https://samsungmagazine.eu/2026/07/13/galaxy-z-fold8-ultra-dostane-necekany-upgrade-displeje-nejde-jen-o-mene-viditelny-ohyb/
  - 2026-07-03T06:04:08.000Z — Čeká nás po čtyřech letech změna? Galaxy S27 Pro a Ultra dostanou novinku, kterou už Apple má — https://samsungmagazine.eu/2026/07/03/ceka-nas-po-ctyrech-letech-zmena-galaxy-s27-pro-a-ultra-dostanou-novinku-kterou-uz-apple-ma/
- unique_value: Jasný nákupní checklist místo obecné novinky.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-04 — Galaxy S26 FE: co sledovat po eventu 27. srpna

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: galaxy s26 fe event
- primary_lane: CURRENT DEMAND
- why_now: Samsung Newsroom invitation; existující články před eventem.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
- hard_evidence: Samsung Newsroom invitation; existující články před eventem.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Samsung Galaxy S26 FE: cena, datum a co čekat od Galaxy Event August 2026 | Zapište si toto datum. Samsung prozradil, kdy představí Galaxy S26 FE a další no
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Samsung Galaxy S26 FE: cena, datum a co čekat od Galaxy Event August 2026 | Zapište si toto datum. Samsung prozradil, kdy představí Galaxy S26 FE a další novinky
- matching_articles:
  - 2026-08-25T13:59:15.000Z — Samsung Galaxy S26 FE: cena, datum a co čekat od Galaxy Event August 2026 — https://samsungmagazine.eu/2026/08/25/samsung-galaxy-s26-fe-cena-datum-a-co-cekat-od-galaxy-event-august-2026/
  - 2026-08-20T05:09:22.000Z — Zapište si toto datum. Samsung prozradil, kdy představí Galaxy S26 FE a další novinky — https://samsungmagazine.eu/2026/08/20/galaxy-event-august-2026-galaxy-s26-fe/
  - 2025-09-04T19:00:10.000Z — Galaxy Tri-Fold potvrzen, dostane se i na globální trh. Kdy se ho dočkáme? — https://samsungmagazine.eu/2025/09/04/galaxy-tri-fold-potvrzen-dostane-se-i-na-globalni-trh-kdy-se-ho-dockame/
- unique_value: Po eventu doplnit cenu, dostupnost, odlišnosti od spekulací.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-05 — Galaxy Watch Ultra 2: recenze a srovnání s Watch Ultra a Garminem

- action: UPDATE
- create_allowed: NO
- exact_topic: galaxy watch ultra 2 recenze
- primary_lane: CURRENT DEMAND
- why_now: Moula: hype fáze; Manticore bez přesné recenze Ultra 2.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
- hard_evidence: Moula: hype fáze; Manticore bez přesné recenze Ultra 2.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Samsung Galaxy Z Fold8 Ultra recenze: Je to špička, ale trochu nuda | Nové skládačky od Samsungu stojí ranec. Tímto trikem ale můžete ušetřit desítky 
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Samsung Galaxy Z Fold8 Ultra recenze: Je to špička, ale trochu nuda | Nové skládačky od Samsungu stojí ranec. Tímto trikem ale můžete ušetřit desítky tisíc
- matching_articles:
  - 2026-08-09T17:56:54.000Z — Samsung Galaxy Z Fold8 Ultra recenze: Je to špička, ale trochu nuda — https://samsungmagazine.eu/2026/08/09/samsung-galaxy-z-fold8-ultra-recenze/
  - 2026-07-22T13:10:16.000Z — Nové skládačky od Samsungu stojí ranec. Tímto trikem ale můžete ušetřit desítky tisíc — https://samsungmagazine.eu/2026/07/22/kolik-stoji-galaxy-z-fold8-flip8-a-watch9-kompletni-cenik/
  - 2025-09-21T18:00:55.000Z — Recenze Galaxy Watch8 Classic: Skvělé chytré hodinky v nevábném obalu — https://samsungmagazine.eu/2025/09/21/recenze-galaxy-watch8-classic/
- unique_value: CZ recenze/srovnání, ne jen přepis specifikací.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-06 — Jak snadno přejít na Galaxy Z Fold8

- action: UPDATE
- create_allowed: NO
- exact_topic: switch to galaxy z fold8
- primary_lane: CURRENT DEMAND
- why_now: Samsung Newsroom: Easier Way to Switch to New Galaxy Z Fold8.; GA4 2097 sessions / 5703 views
- hard_evidence: Samsung Newsroom: Easier Way to Switch to New Galaxy Z Fold8.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové | Skvělá aplikace od Samsungu má velký problém. Uživatelům po přechodu na nový tel
- global_trends: global max 100/100, avg 0.6, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? | Skvělá aplikace od Samsungu má velký problém. Uživatelům po přechodu na nový telefon nefun
- matching_articles:
  - 2026-08-24T04:03:04.000Z — Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? — https://samsungmagazine.eu/2026/08/24/prehled-aktualizaci-samsung/
  - 2026-08-20T08:55:00.000Z — Skvělá aplikace od Samsungu má velký problém. Uživatelům po přechodu na nový telefon nefungují RCS chaty — https://samsungmagazine.eu/2026/08/20/samsung-smart-switch-block-rcs/
- unique_value: Praktický migrační návod pro iPhone/Samsung uživatele.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-07 — Galaxy Buds4 Pro mají uznaný Hi-Fi zvuk: co to znamená v praxi

- action: CREATE
- create_allowed: YES
- exact_topic: galaxy buds4 pro hi-fi sound
- primary_lane: CURRENT DEMAND
- why_now: Samsung Newsroom: audio experts recognition.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
- hard_evidence: Samsung Newsroom: audio experts recognition.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Oddělit certifikaci/marketing od reálného poslechu.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-08 — Srpnové bezpečnostní aktualizace Galaxy: kdo je dostává

- action: UPDATE
- create_allowed: NO
- exact_topic: august 2026 security patch galaxy
- primary_lane: CURRENT DEMAND
- why_now: SamMobile: August 2026 security patch pro Galaxy M55 + patch vlna.; GA4 2134 sessions / 3271 views
- hard_evidence: SamMobile: August 2026 security patch pro Galaxy M55 + patch vlna.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? | Tato Samsung zařízení právě dostávají srpnovou bezpečnostní aktualizaci 2026. A nejsou to 
- matching_articles:
  - 2026-08-24T04:03:04.000Z — Přehled aktualizací Samsung: Která zařízení obdržela ve 34. týdnu roku 2026 nové verze? — https://samsungmagazine.eu/2026/08/24/prehled-aktualizaci-samsung/
  - 2026-08-19T09:02:42.000Z — Tato Samsung zařízení právě dostávají srpnovou bezpečnostní aktualizaci 2026. A nejsou to ta, která čekáte (Aktualizováno) — https://samsungmagazine.eu/2026/08/19/samsung-update-galaxy-watch4-buds3-pro/
  - 2026-08-13T13:03:44.000Z — Samsung spustil srpnovou aktualizaci. Která zařízení ji dostávají jako první? — https://samsungmagazine.eu/2026/08/13/samsung-spustil-srpnovou-aktualizaci-ktera-zarizeni-ji-dostavaji-jako-prvni/
- unique_value: Krátký servisní roundup s modely a postupem kontroly.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-09 — Galaxy S27 Ultra leak: vodorovný fotomodul a riziko iPhone looku

- action: CREATE
- create_allowed: YES
- exact_topic: galaxy s27 ultra camera bar
- primary_lane: DISCOVERY
- why_now: Android Central/SamMobile: S27 Ultra redesign leak.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
- hard_evidence: Android Central/SamMobile: S27 Ultra redesign leak.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Jasně označit leak; porovnat designový směr a očekávání.
- reality_status: UNCERTAIN - leak/spekulace jasně označit
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-10 — Good Lock MultiStar/FlipShot: malá funkce pro skládačky, velký rozdíl

- action: UPDATE
- create_allowed: NO
- exact_topic: good lock multistar flipshot
- primary_lane: DISCOVERY
- why_now: Samsung specialist media signály z 24.–25.8.
- hard_evidence: Samsung specialist media signály z 24.–25.8.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Manticore hit
- matching_articles:
- unique_value: Praktický návod pro Fold/Flip majitele.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-11 — Samsung na Gamescomu 2026: proč to zajímá i majitele Galaxy

- action: CREATE
- create_allowed: YES
- exact_topic: samsung gamescom 2026
- primary_lane: DISCOVERY
- why_now: Samsung Newsroom Global: Gamescom 2026 gaming solutions.; GSC 281731 imp / pos 3.89 / CTR 23.64 %; GA4 22735 sessions / 29358 views
- hard_evidence: Samsung Newsroom Global: Gamescom 2026 gaming solutions.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 17/100, avg 0.2, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Napojit na gaming monitory, Galaxy, cloud gaming.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-12 — Čínská odpověď na Galaxy Z TriFold přijde příští měsíc

- action: CREATE
- create_allowed: YES
- exact_topic: galaxy z trifold china
- primary_lane: DISCOVERY
- why_now: SamMobile: China answer to Galaxy Z TriFold coming next month.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
- hard_evidence: SamMobile: China answer to Galaxy Z TriFold coming next month.; WP/Manticore: NO_DUPLICATE přes Manticore
- global_trends: global max 0/100, avg 0.0, last 0
- wp_manticore_check: MANTICORE_NO_EXACT_DUPLICATE; WP_REST_RELATED_HITS
- unique_value: Konkurence jako tlak na Samsung; jasně označit jako konkurenční signál.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-13 — Galaxy Z Fold8 má možná až moc selfie kamer

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: galaxy z fold 8 selfie camera
- primary_lane: DISCOVER
- why_now: SamMobile hot take; Fold8 témata běží v GA4.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
- hard_evidence: SamMobile hot take; Fold8 témata běží v GA4.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Pixel 11 Pro vyzval Galaxy S26 Ultra. Která vlajková loď vám nabídne více?
- global_trends: global max 14/100, avg 0.1, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Recenze Samsung Galaxy Z Flip8: Baví mě víc než kdy dřív, i tak mě na něm ale něco štve | Pixel 11 Pro vyzval Galaxy S26 Ultra. Která vlajková loď vám nabídne více?
- matching_articles:
  - 2026-08-15T18:04:06.000Z — Recenze Samsung Galaxy Z Flip8: Baví mě víc než kdy dřív, i tak mě na něm ale něco štve — https://samsungmagazine.eu/2026/08/15/recenze-samsung-galaxy-z-flip8/
  - 2026-08-14T12:04:07.000Z — Pixel 11 Pro vyzval Galaxy S26 Ultra. Která vlajková loď vám nabídne více? — https://samsungmagazine.eu/2026/08/14/pixel-11-pro-vs-samsung-galaxy-s26-ultra/
- unique_value: Názorový/analytický úhel pro redaktora, ne AI hotový článek.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-14 — Android Auto na Samsungu: tři nastavení, která dnes řeší nejvíc lidí

- action: UPDATE
- create_allowed: NO
- exact_topic: android auto samsung
- primary_lane: SEO + CURRENT DEMAND
- why_now: GSC android auto 124k imp; GA4 Android Auto články silné.; GSC 124797 imp / pos 5.04 / CTR 17.62 %; GA4 13421 sessions / 16605 views
- hard_evidence: GSC android auto 124k imp; GA4 Android Auto články silné.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Android Auto se zbavuje té nejotravnější chyby. Bude připojení konečně stabilní? | Epic, Google a Samsung hlásí mír. Do Androidu míří snadnější instalace obchodů, 
- global_trends: global max 100/100, avg 49.3, last 46
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Android Auto se zbavuje té nejotravnější chyby. Bude připojení konečně stabilní? | Epic, Google a Samsung hlásí mír. Do Androidu míří snadnější instalace obchodů, ale i přísnější s
- matching_articles:
  - 2026-08-21T07:59:15.000Z — Android Auto se zbavuje té nejotravnější chyby. Bude připojení konečně stabilní? — https://samsungmagazine.eu/2026/08/21/android-auto-17-4-fixes-connection-issue/
  - 2026-08-20T20:03:48.000Z — Epic, Google a Samsung hlásí mír. Do Androidu míří snadnější instalace obchodů, ale i přísnější správa RAM — https://samsungmagazine.eu/2026/08/20/epic-google-partnership-android-ram-limits/
  - 2026-07-17T04:01:53.000Z — Padá vám Android Auto? Google odhalil, co za tím stojí, a vydává záplatu — https://samsungmagazine.eu/2026/07/17/pada-vam-android-auto-google-odhalil-co-za-tim-stoji-a-vydava-zaplatu/
- unique_value: Praktický návod s odkazy na existující články.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-15 — Jak uvolnit místo na Samsungu bez mazání aplikací

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: uvolnit misto samsung
- primary_lane: DISCOVER
- why_now: GA4 CZ článek 7 908 sessions / 32 547 views.; GA4 7912 sessions / 32560 views
- hard_evidence: GA4 CZ článek 7 908 sessions / 32 547 views.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji | Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy
- global_trends: global max 18/100, avg 0.2, last 0
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Co jsou na Samsung telefonu Ostatní soubory? S One UI 8 je konečně můžete smazat | Jak v Galerii na Samsung telefonu odstranit duplicitní obrázky
- matching_articles:
  - 2025-11-10T14:00:54.000Z — Co jsou na Samsung telefonu Ostatní soubory? S One UI 8 je konečně můžete smazat — https://samsungmagazine.eu/2025/11/10/co-jsou-na-samsung-telefonu-ostatni-soubory/
  - 2025-09-08T13:00:19.000Z — Jak v Galerii na Samsung telefonu odstranit duplicitní obrázky — https://samsungmagazine.eu/2025/09/08/jak-v-galerii-na-samsung-telefonu-odstranit-duplicitni-obrazky/
  - 2025-05-23T13:00:58.000Z — Jak uvolnit místo v Samsung telefonu bez nutnosti mazat fotky či videa? Není to tak složité — https://samsungmagazine.eu/2025/05/23/jak-uvolnit-misto-v-telefonu-samsung-bez-nutnosti-mazat-fotky-ci-videa/
- unique_value: Navazující tipy, ne duplicitní rewrite.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-16 — Google Wallet redesign na Samsungu: co se změnilo

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: google wallet redesign
- primary_lane: CURRENT DEMAND
- why_now: GA4: Google Wallet redesign 7 007 sessions / 50 799 views.; GSC 10118 imp / pos 4.89 / CTR 24.85 %; GA4 7007 sessions / 50799 views
- hard_evidence: GA4: Google Wallet redesign 7 007 sessions / 50 799 views.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Peněženka Google spouští velký redesign, na který všichni čekali. Podívejte se, 
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Peněženka Google spouští velký redesign, na který všichni čekali. Podívejte se, jaké novinky konečně dorazily
- matching_articles:
  - 2026-08-19T06:59:08.000Z — Peněženka Google spouští velký redesign, na který všichni čekali. Podívejte se, jaké novinky konečně dorazily — https://samsungmagazine.eu/2026/08/19/google-wallet-redesign/
- unique_value: Aktualizovat s praktickými screenshot/body.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-17 — Samsung zdražuje čipy: zdraží i telefony střední třídy?

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: samsung chip price midrange
- primary_lane: CURRENT DEMAND
- why_now: GA4 CZ článek 13 820 sessions.; GSC 281731 imp / pos 3.89 / CTR 23.64 %; GA4 22735 sessions / 29358 views
- hard_evidence: GA4 CZ článek 13 820 sessions.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Příští telefon vás přijde draho. Samsung v tichosti chystá krok, který zničí dos
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Příští telefon vás přijde draho. Samsung v tichosti chystá krok, který zničí dostupné smartphony | Samsung plošně zdražuje modely řad Galaxy M a F. Nejvíc to dopadne na indické fan
- matching_articles:
  - 2026-08-21T06:06:31.000Z — Příští telefon vás přijde draho. Samsung v tichosti chystá krok, který zničí dostupné smartphony — https://samsungmagazine.eu/2026/08/21/samsung-chip-price-hike-midrange-smartphones/
  - 2026-04-08T08:12:53.000Z — Samsung plošně zdražuje modely řad Galaxy M a F. Nejvíc to dopadne na indické fanoušky — https://samsungmagazine.eu/2026/04/08/samsung-plosne-zdrazuje-modely-rad-galaxy-m-a-f/
  - 2026-02-07T01:00:43.000Z — Tipněte si, kolik se v roce 2025 se prodalo smartphonů — https://samsungmagazine.eu/2026/02/07/tipnete-si-kolik-se-v-roce-2025-se-prodalo-smartphonu/
- unique_value: Follow-up s dopadem na S26 FE a A řadu.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-18 — Které Galaxy telefony letos končí s podporou

- action: UPDATE
- create_allowed: NO
- exact_topic: galaxy end of life support
- primary_lane: SEO
- why_now: GA4 lifecycle/support obsah silný globálně.; GSC 222261 imp / pos 3.7 / CTR 6.31 %; GA4 15000 sessions / 24381 views
- hard_evidence: GA4 lifecycle/support obsah silný globálně.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Těmto telefonům Samsung Galaxy dochází čas. Zkontrolujte, zda mezi nimi není i t
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Nenechte se zmást papírovou kapacitou. Baterie Galaxy S26 Ultra funguje úplně jinak, než si myslíte | Samsung definitivně pohřbívá S Pen, v Galaxy Z Fold8 ho nejspíš nenajdeme. Smů
- matching_articles:
  - 2026-07-12T06:54:28.000Z — Nenechte se zmást papírovou kapacitou. Baterie Galaxy S26 Ultra funguje úplně jinak, než si myslíte — https://samsungmagazine.eu/2026/07/12/baterie-galaxy-s26-ultra-funguje/
  - 2026-06-24T06:54:20.000Z — Samsung definitivně pohřbívá S Pen, v Galaxy Z Fold8 ho nejspíš nenajdeme. Smůlu mají ale i majitelé starších modelů — https://samsungmagazine.eu/2026/06/24/samsung-definitivne-pohrbiva-s-pen-v-galaxy-z-fold8-ho-nejspis-nenajdeme-smulu-maji-ale-i-majitele-starsich-modelu/
  - 2026-06-17T17:57:34.000Z — Nová éra odstartovala. Kompletní průvodce Androidem 17 ukazuje, v čem je skutečná síla systému — https://samsungmagazine.eu/2026/06/17/nova-era-odstartovala-kompletni-pruvodce-androidem-17-ukazuje-v-cem-je-skutecna-sila-systemu/
- unique_value: Aktualizovat modely, interní linky, FAQ.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-19 — SwiftKey v One UI 9: proč ho půjde odstranit a koho se to týká

- action: FOLLOW-UP
- create_allowed: NO
- exact_topic: swiftkey samsung one ui 9
- primary_lane: CURRENT DEMAND
- why_now: GA4: SwiftKey/One UI 9 článek silný v JA.; GSC 8481 imp / pos 1 / CTR 56.18 %; GA4 8897 sessions / 13704 views
- hard_evidence: GA4: SwiftKey/One UI 9 článek silný v JA.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy | Každý Samsung obsahuje umělou inteligenci. Ano, i ten váš
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy nechtěli | Každý Samsung obsahuje umělou inteligenci. Ano, i ten váš
- matching_articles:
  - 2026-08-18T23:56:23.000Z — Majitelé telefonů Samsung oslavují. Konečně z nich smažou aplikaci, kterou nikdy nechtěli — https://samsungmagazine.eu/2026/08/19/samsung-swiftkey/
  - 2023-05-03T19:00:59.000Z — Každý Samsung obsahuje umělou inteligenci. Ano, i ten váš — https://samsungmagazine.eu/2023/05/03/kazdy-uzivatel-galaxy-ma-nyni-ve-svem-telefonu-a-tabletu-nastroj-bing-ai/
- unique_value: CZ verze prakticky a stručně.
- reality_status: PASS
- information_age_status: FRESH
- final_write_gate: PASS

### SAM-20 — Zamrzlé Galaxy Watch: proč nedělat tovární reset jako první

- action: UPDATE
- create_allowed: NO
- exact_topic: frozen galaxy watch reset
- primary_lane: SEO
- why_now: Manticore/signály na Galaxy Watch problémy; evergreen řešení.; GA4 15000 sessions / 24381 views
- hard_evidence: Manticore/signály na Galaxy Watch problémy; evergreen řešení.; WP/Manticore: SIMILAR_EXISTS přes Manticore: Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji
- global_trends: GLOBAL_TRENDS_UNAVAILABLE
- wp_manticore_check: PUBLISHED/SIMILAR_EXISTS: Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji
- matching_articles:
  - 2026-08-24T13:54:41.000Z — Zlobí vás Galaxy Watch? Tovární reset nedělejte, problém vyřešíte jednodušeji — https://samsungmagazine.eu/2026/08/24/how-to-fix-frozen-galaxy-watch/
- unique_value: Servisní návod s jasnými kroky.
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