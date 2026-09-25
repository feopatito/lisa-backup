# Android Magazine — Ranni redakcni plan — 2. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS

Format:
- `Vrstva 1` = silne `CREATE` k napsani ted
- `Vrstva 2` = follow-upy, updaty a inspirace bez umeleho nafukovani

## Vrstva 1 — Priority

### 1. Zariovy Android Drop je venku
- Action: `CREATE`
- Why now: primarni zdroj je `Google Blog`, coverage okamzite naskocila pres `9to5Google`, `Android Authority` i `Google News`.
- Titulky: `Discover` Google potichu poslal do Androidu pet novinek, ktere si vsimnete hned dnes | `Search` September Android Drop 2026: pet novych funkci pro Android a Pixel | `Balanced` Android dostal zariovy Drop. Tohle je pet novinek, ktere maji nejvetsi smysl
- Doporucena: `Balanced` - nejlip prodava konkretni uzitek bez ztraty search srozumitelnosti.

### 2. Pixel 11 dostava ranny zariovy update misto Android 17 QPR1
- Action: `CREATE`
- Why now: cerstvy Pixel servisni peg z `9to5Google`, cisty user-impact kus.
- Titulky: `Discover` Pixel 11 dostal necekany update a neni to Android 17 QPR1 | `Search` Pixel 11 September 2026 update: co Google vydal misto Android 17 QPR1 | `Balanced` Google poslal Pixelu 11 prekvapivy zariovy update. QPR1 to ale neni
- Doporucena: `Balanced` - ma prekvapeni i vysvetleni v jednom radku.

### 3. YouTube meni app-to-TV propojeni a uz nepotrebuje stejnou Wi-Fi sit
- Action: `CREATE`
- Why now: velka uzitkova zmena z `9to5Google`, kterou bezny ctenar okamzite pochopi.
- Titulky: `Discover` YouTube zabil jednu z nejotravnejsich prekazek pri posilani videa do televize | `Search` YouTube app to TV uz nevyzaduje stejnou Wi-Fi sit | `Balanced` Posilat YouTube z mobilu do TV bude snazsi. Stejna Wi-Fi uz neni nutna
- Doporucena: `Discover` - nejlip prodava odstraneni konkretni frustrace.

### 4. Google rozjizdi novy prehled baterie pro Pixely
- Action: `CREATE`
- Why now: `Android Authority` popisuje live rollout a jde o praktickou funkci s realnym dopadem.
- Titulky: `Discover` Pixely dostavaji bateriovou novinku, ktera konecne dava smysl | `Search` Pixel battery usage summaries: Google spousti novou funkci baterie | `Balanced` Google pridal Pixelum novy prehled baterie. Ukaze vic nez dosud
- Doporucena: `Balanced` - je nejcitelnejsi pro siroke publikum i pro search.

## Vrstva 2 — Inspirace a updaty

### 5. Android 17 QPR2 Beta 4 uz dnes nelezi jako cisty CREATE
- Action: `UPDATE`
- Proc je tady: Manticore nasel vcerejsi publikovany Android Magazine kus, novy slot by byl jen recyklace.

### 6. Android Auto testuje Quick Settings a drobny weather easter egg
- Action: `FOLLOW-UP`
- Proc je tady: signal je zajimavy, ale na samostatny hlavni slot je dnes slabsi nez Android Drop.

### 7. Google Clock ma novy timer UI
- Action: `FOLLOW-UP`
- Proc je tady: uzivatelsky srozumitelne, ale mensi peg nez hlavni systemove novinky.

### 8. Google Meet hardware opousti ChromeOS a prechazi na Android
- Action: `FOLLOW-UP`
- Proc je tady: solidni produktovy signal, ale vic B2B nez mainstreamovy mobilni tahak.

### 9. Google Pics
- Action: `INSPIRATION_ONLY`
- Proc je tady: tema je silne pro Workspace/AI, ale pro Android Magazine dnes nema tak cisty mobilni peg.

## Datova opora

- `GSC`: `vypnout telefon` `1 043 imp`, `jak vypnout telefon` `286 imp`, `google pixel 11` `45 imp`, `google pixel` `41 imp`
- `GA4`: nejsilnejsi utility backbone dnes drzi domovska stranka a starsi navodove kusy; Android data pool je rano citelne slabsi nez LSA/Samsung.

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
