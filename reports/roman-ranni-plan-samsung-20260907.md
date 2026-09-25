# Samsung Magazine — Ranni redakcni plan — 7. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS
Morning context: regenerated today and applied before pre-flight + portfolio selection.

Skill / fallback vrstva:
- Google SERP Search API: UNAVAILABLE (`402 insufficient credits`) -> fallback `prime RSS/web zdroje`
- Google SERP Trends Search API: UNAVAILABLE (`402 insufficient credits`) -> fallback `pytrends`
- Competitor Research: nepouzito, rano nebyl potreba hlubsi hrancni audit
- seo-content: nepouzito jako samostatny tool gate; uniqueness jsem oprela o Manticore + intent overlap logiku z predchoziho PASS poolu
- humanizer: nepouzito, drzim rano na faktickem a stabilnim artefaktu

Format:
- `Vrstva 1` = jen ciste `CREATE now`
- `Vrstva 2` = evergreen / GSC backbone + kuratorovane follow-upy bez umeleho nafukovani

## Vrstva 1 — Priority

### 1. Galaxy S26 FE skryva tri sikovne foto rezimy. Staci je jen znovu zapnout
- Action: `CREATE`
- Why now: SamMobile publikovalo clanek v 02:20 CEST uvnitr aktivniho 18:00-06:00 okna a jde o okamzite pouzitelny tip pro cerstve majitele noveho Galaxy modelu.
- Titulky: `Discover` Galaxy S26 FE skryva tri sikovne foto rezimy. Staci je jen znovu zapnout | `Search` Galaxy S26 FE: jak zapnout Night, Single Take a Dual Rec pres Camera Assistant | `Balanced` Na Galaxy S26 FE chybi tri zname foto rezimy jen naoko. Takhle je vratite zpet
- Doporucena: `Discover` - Discover varianta spojuje skrytou funkci s rychlym resenim a ma nejvyssi sanci na klik bez ztraty srozumitelnosti.

## Vrstva 2 — Evergreen / GSC zakladna

### 1. Samsung nejde restartovat nebo se sám restartuje
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 2. Samsung Account: co to je, přihlášení a zapomenuté heslo
- Action: `REWRITE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 3. Mezipaměť v Samsungu: kdy ji mazat a kdy ne
- Action: `REWRITE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 4. Jak vyfotit zatmění Slunce mobilem Samsung
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 5. Samsung Wallet / Pay v ČR: co funguje a co ne
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 6. Jak vyčistit zažloutlý kryt na mobil
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 7. Zabezpečená složka Samsung: nastavení a zapomenuté heslo
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 8. Galaxy Store: co to je a kdy ho použít místo Obchodu Play
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 9. SmartThings: nastavení chytré domácnosti Samsung
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 10. RCS zprávy na Samsungu: zapnout, vypnout, přepnout na SMS
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 11. Stav baterie Samsung: kondice, diagnostika a kalibrace
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 12. Bluetooth na Samsungu: párování, Dual Audio a dosah
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 13. Galaxy Watch ciferníky zdarma: kde je hledat bezpečně
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 14. Google úložiště na Samsungu: co zabírá místo a jak ho uvolnit
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 15. Samsung Cloud: co zálohuje a co už ne
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 16. Quick Share na Samsungu: sdílení souborů a problémy
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 17. Galaxy Watch nejdou restartovat nebo nereagují
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 18. Samsung TV se sama vypíná nebo zapíná
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 19. Wi‑Fi volání na Samsungu: kdy ho zapnout a proč nefunguje
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

### 20. Always On Display na Samsungu: nastaveni, spotreba baterie a co delat, kdyz prestane fungovat
- Action: `UPDATE`
- Proc je tady: evergreen/GSC backbone: overeny search intent s existujici nebo jasne updateovatelnou coverage

## Transparentni stav overnightu

- Samsung ma dnes jen 1 cisty overnight CREATE; dalsi overnight signaly jsem radeji nechala ve vrstve backbone nebo mimo vyber.
- Samsung Newsroom Tizen 10 appliance update je overeny, ale pro SamsungMagazine je to dnes slabsi nez cisty Galaxy user-help kus pro S26 FE.

## Datova opora

- `GA4` quick snapshot PASS: top path je japonsky Android Auto kus `5141` sessions, dale tamilsky storage advertorial `4309` a cesky tydenni update kus `3074`.
- `GSC` yesterday query snapshot vratil prazdne rows; Samsung backbone proto zustava postaveny na poslednim validovanem One UI / utility poolu.

## Source Coverage Audit

- WordPress: CHECKED
- Manticore: CHECKED
- GSC: CHECKED - live API dostupne, ale quick query snapshot za vcerejsek vratil prazdne rows
- GA4: CHECKED - live property snapshots prosly pro vsechny 3 weby
- Google SERP Search API: UNAVAILABLE - JustSerpAPI vratilo `402 insufficient credits`; fallback = prime RSS/web zdroje
- Google SERP Trends Search API: UNAVAILABLE - JustSerpAPI vratilo `402 insufficient credits`; fallback = `pytrends`
- Google Trends fallback (`pytrends`): CHECKED - vybrane termy bez viditelneho CZ spike nebo empty return
- Google News: NOT CHECKED - prednost mely prime source feedy
- major tech media: CHECKED - 9to5Mac, 9to5Google, GSMArena, SamMobile, The Verge
- official newsrooms: CHECKED - Google Blog, Samsung Newsroom Global; bez silnejsiho mobilniho overnight winneru pro LSA/Android
- Reddit RSS: UNAVAILABLE - network policy block i s browser User-Agent fallbackem
- GitHub: NOT CHECKED - dnes nevyhral proti silnejsim verified public signalum
- APK / teardown layer: NOT CHECKED - bez silnejsiho overnight winneru
- developer docs / support docs / changelogs: NOT CHECKED - dnes negenerovaly lepsi solo slot
- regulatory / certifikace: NOT CHECKED - bez jasneho overnight winneru
- X / leakers: NOT CHECKED - drzela jsem se overitelnych public zdroju
- YouTube: NOT CHECKED - bez potreby proti silnejsim zdrojum
- smaller specialist media: NOT CHECKED - priorita sla do Tier S/A + verified backbone
