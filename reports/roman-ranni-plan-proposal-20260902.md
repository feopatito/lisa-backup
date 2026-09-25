# Ranni redakcni plan V6.5 pro 2. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS

Skill vrstva:
- Google SERP Search API: FAIL (`402 insufficient credits`) -> fallback `Google News RSS + live RSS/web`
- Google SERP Trends Search API: FAIL (`402 insufficient credits`) -> fallback `pytrends`; po prvnim dotazu caste `429`
- Competitor Research: nepouzito, rano nebyl potreba hlubsi market audit
- seo-content: nepouzito jako URL audit; uniqueness jsem overila pres Manticore + intent overlap check
- humanizer: nechavam az na PDF po schvaleni

Poznamka ke kvalite:
- LSA ma dnes jen `1` cisty overnight `CREATE`.
- Android Magazine ma dnes `4` ciste overnight `CREATE`.
- Samsung Magazine ma dnes `4` ciste overnight `CREATE`.
- Slabe nebo intentove prekrvajici se kusy jsem presunula do `Vrstva 2`.

## LSA

### Vrstva 1 — Priority

1. `CREATE` Apple rika vyvojarum Mac App Storu, ze uz mohou odstrihnout Intel Macy.
   Why now: cerstvy developer peg z `9to5Mac` a jasny dopad na realne majitele starsich Macu.
   Titulky: `Discover` Apple definitivne otaci list. Aplikace pro Macy uz mohou odstrihnout Intel | `Search` Apple dovolil vyvojarum v Mac App Storu ukoncit podporu Intel Macu | `Balanced` Intel Macy dostaly dalsi stopku. Apple povolil vyvojarum ukoncit jejich podporu
   Doporucena: `Balanced` - spojuje emoci i jasnou zpravu a neni to jen sucha developerska veta.

### Vrstva 2 — Inspirace a updaty

2. `FOLLOW-UP` Ford vysvetlil, proc v novych elektromobilech zvolil Apple Maps misto Googlu.
   Proc je tady: na LSA uz existuje starsi Ford/Apple Maps coverage, novy kus je silny spis jako follow-up s novym vysvetlenim.
3. `FOLLOW-UP` John Ternus rozeslal prvni memo a zaroven se objevily detaily jeho odmeny.
   Proc je tady: management cluster je zivy, ale zakladni John Ternus intent uz web pokryva.
4. `FOLLOW-UP` Apple Watch Series 12: tri nove funkce pred pristi tydennim uvedenim.
   Proc je tady: novy peg existuje, ale intent se prekryva se starsimi expectation kusy.
5. `FOLLOW-UP` Dorazily dalsi detaily k iPhone Ultra.
   Proc je tady: GSC cluster je silny, ale intent overlap na LSA je uz moc tesny na dalsi cisty CREATE.
6. `UPDATE` Lake America / Apple Maps cluster neotevirat jako novy slot.
   Proc je tady: Manticore uz ukazuje dnesni publikovany LSA kus, takze dalsi CREATE by byl duplicitni.

### Datova opora

- `GSC`: iPhone 18 `505 678 imp`, iPhone 18 Pro `190 590 imp`, iPhone 18 Pro Max `207 557 imp`, iPhone Ultra `57 295 imp`
- Z toho plyne: LSA backbone dnes stoji vic na update/follow-up Apple hardware clusterech nez na mnoha cistych overnight novinkach.

## Android Magazine

### Vrstva 1 — Priority

1. `CREATE` Zariovy Android Drop je venku.
   Why now: primarni zdroj je `Google Blog`, coverage okamzite naskocila pres `9to5Google`, `Android Authority` i `Google News`.
   Titulky: `Discover` Google potichu poslal do Androidu pet novinek, ktere si vsimnete hned dnes | `Search` September Android Drop 2026: pet novych funkci pro Android a Pixel | `Balanced` Android dostal zariovy Drop. Tohle je pet novinek, ktere maji nejvetsi smysl
   Doporucena: `Balanced` - nejlip prodava konkretni uzitek bez ztraty search srozumitelnosti.
2. `CREATE` Pixel 11 dostava ranny zariovy update misto Android 17 QPR1.
   Why now: cerstvy Pixel servisni peg z `9to5Google`, cisty user-impact kus.
   Titulky: `Discover` Pixel 11 dostal necekany update a neni to Android 17 QPR1 | `Search` Pixel 11 September 2026 update: co Google vydal misto Android 17 QPR1 | `Balanced` Google poslal Pixelu 11 prekvapivy zariovy update. QPR1 to ale neni
   Doporucena: `Balanced` - ma prekvapeni i vysvetleni v jednom radku.
3. `CREATE` YouTube meni app-to-TV propojeni a uz nepotrebuje stejnou Wi-Fi sit.
   Why now: velka uzitkova zmena z `9to5Google`, kterou bezny ctenar okamzite pochopi.
   Titulky: `Discover` YouTube zabil jednu z nejotravnejsich prekazek pri posilani videa do televize | `Search` YouTube app to TV uz nevyzaduje stejnou Wi-Fi sit | `Balanced` Posilat YouTube z mobilu do TV bude snazsi. Stejna Wi-Fi uz neni nutna
   Doporucena: `Discover` - nejlip prodava odstraneni konkretni frustrace.
4. `CREATE` Google rozjizdi novy prehled baterie pro Pixely.
   Why now: `Android Authority` popisuje live rollout a jde o praktickou funkci s realnym dopadem.
   Titulky: `Discover` Pixely dostavaji bateriovou novinku, ktera konecne dava smysl | `Search` Pixel battery usage summaries: Google spousti novou funkci baterie | `Balanced` Google pridal Pixelum novy prehled baterie. Ukaze vic nez dosud
   Doporucena: `Balanced` - je nejcitelnejsi pro siroke publikum i pro search.

### Vrstva 2 — Inspirace a updaty

5. `UPDATE` Android 17 QPR2 Beta 4 uz dnes nelezi jako cisty CREATE.
   Proc je tady: Manticore nasel vcerejsi publikovany Android Magazine kus, novy slot by byl jen recyklace.
6. `FOLLOW-UP` Android Auto testuje Quick Settings a drobny weather easter egg.
   Proc je tady: signal je zajimavy, ale na samostatny hlavni slot je dnes slabsi nez Android Drop.
7. `FOLLOW-UP` Google Clock ma novy timer UI.
   Proc je tady: uzivatelsky srozumitelne, ale mensi peg nez hlavni systemove novinky.
8. `FOLLOW-UP` Google Meet hardware opousti ChromeOS a prechazi na Android.
   Proc je tady: solidni produktovy signal, ale vic B2B nez mainstreamovy mobilni tahak.
9. `INSPIRATION_ONLY` Google Pics.
   Proc je tady: tema je silne pro Workspace/AI, ale pro Android Magazine dnes nema tak cisty mobilni peg.

### Datova opora

- `GSC`: `vypnout telefon` `1 043 imp`, `jak vypnout telefon` `286 imp`, `google pixel 11` `45 imp`, `google pixel` `41 imp`
- `GA4`: nejsilnejsi utility backbone dnes drzi domovska stranka a starsi navodove kusy; Android data pool je rano citelne slabsi nez LSA/Samsung.

## Samsung Magazine

### Vrstva 1 — Priority

1. `CREATE` Samsung nekterym lidem nahodne deaktivuje ucty kvuli "security reasons".
   Why now: cerstvy user-pain kus z `9to5Google`, cisty prakticky problem a Manticore nevraci stejny intent.
   Titulky: `Discover` Samsung lidem vypina ucty a jako duvod hlasi bezpecnost | `Search` Samsung account deactivated for security reasons: co se deje a co zkusit | `Balanced` Samsung nekterym uzivatelum deaktivuje ucet. Duvod ma byt bezpecnost
   Doporucena: `Balanced` - je nejsrozumitelnejsi a okamzite rika, koho se problem tyka.
2. `CREATE` One UI 9 beta se tento mesic siri na dalsi Galaxy telefony.
   Why now: novy rollout cluster z `9to5Google` + `Android Authority`, silny aktualni Samsung intent.
   Titulky: `Discover` One UI 9 miri na dalsi Galaxy telefony a nektere dorazi uz tenhle mesic | `Search` One UI 9 beta expands to more Galaxy phones in September 2026 | `Balanced` Samsung rozsiruje One UI 9 beta. Tyhle Galaxy telefony maji byt dalsi na rade
   Doporucena: `Balanced` - nejlip spojuje seznamovy search intent s klikavou naléhavostí.
3. `CREATE` Galaxy S25 dostava pres One UI 9 beta jeden z nejzajimavejsich foto triku ze S26.
   Why now: `Android Authority` popsalo konkretní feature spillover, ktery unese vlastni Samsung pribeh.
   Titulky: `Discover` Samsung posila do Galaxy S25 foto trik, ktery si nechaval pro S26 | `Search` Galaxy S25 One UI 9 beta adds S26 camera trick | `Balanced` Galaxy S25 dostava v One UI 9 beta jednu z nejlepsich foto novinek ze S26
   Doporucena: `Discover` - ma nejsilnejsi click potential, protoze prodava prenos funkce z novejsi rady.
4. `CREATE` Samsung store reklamy v telefonu: jak je zastavit.
   Why now: `SamMobile` otevrel konkretni user pain s okamzite uzitelnym resenim.
   Titulky: `Discover` Chodite do Samsung prodejny? Telefon vam pak muze zacit cpat reklamy | `Search` How to stop Samsung store ads on Galaxy phone | `Balanced` Samsung umi posilat reklamy po navsteve prodejny. Takhle je vypnete
   Doporucena: `Balanced` - propojuje sokovy hook s okamzitym resenim.

### Vrstva 2 — Inspirace a updaty

5. `UPDATE` Gemini na Samsungu.
   Proc je tady: silny GSC cluster, ale dnes bez dost silneho noveho pegu na CREATE.
6. `UPDATE` One UI 9 obecny rozcestnik.
   Proc je tady: obrovsky demand, vhodne drzet jako servisni/update backbone.
7. `UPDATE` Android Auto na Samsungu.
   Proc je tady: vysoky dlouhodoby zajem a silny utility intent.
8. `GOOD_SIGNAL_WEAK_TODAY` One UI 9 pro starsi foldables.
   Proc je tady: dobry signal, ale dnes ho radsi drzim pod sirsim rollout clustrem nez jako separátní hlavni slot.
9. `INSPIRATION_ONLY` My FanCam / feature story kolem Z8.
   Proc je tady: zajimave zakulisi, ale bez dostatecneho why now pro solo clanek.

### Datova opora

- `GSC`: `gemini` `342 927 imp`, `one ui` `121 681 imp`, `android auto` `108 098 imp`, `one ui 9` `65 564 imp`
- `GA4`: velmi silny utility/service backbone kolem Android Auto a navodovych kusu.

## Source Coverage Audit

- WordPress / Manticore: `CHECKED`
- GSC: `CHECKED`
- GA4: `CHECKED`
- Google SERP Search API: `UNAVAILABLE - 402 insufficient credits`
- Google SERP Trends Search API: `UNAVAILABLE - 402 insufficient credits`
- Google Trends fallback (`pytrends`): `PARTIAL - prvni dotaz vratil data, dalsi dotazy narazily na 429`
- Google News RSS: `CHECKED`
- major tech media: `CHECKED - 9to5Mac, 9to5Google, GSMArena, SamMobile, Android Authority, The Verge`
- official newsrooms: `CHECKED - Google Blog`; `Apple Newsroom` a `Samsung Newsroom`: `NO RELEVANT SIGNAL`
- Reddit: `CHECKED - r/apple`; `r/android` a `r/samsung`: `UNAVAILABLE - 429`
- GitHub: `NOT CHECKED - rano bez silneho editorialniho pegu z commit vrstvy`
- APK / teardown layer: `NOT CHECKED - dnes nevyhrala proti silnejsim overnight signalum`

Je to pro vas vyhovujici?
