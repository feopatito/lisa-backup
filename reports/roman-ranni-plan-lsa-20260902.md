# LSA — Ranni redakcni plan — 2. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS

Format:
- `Vrstva 1` = silne `CREATE` k napsani ted
- `Vrstva 2` = follow-upy, updaty a inspirace bez umeleho nafukovani

## Vrstva 1 — Priority

### 1. Apple rika vyvojarum Mac App Storu, ze uz mohou odstrihnout Intel Macy
- Action: `CREATE`
- Why now: cerstvy developer peg z `9to5Mac` a jasny dopad na realne majitele starsich Macu.
- Titulky: `Discover` Apple definitivne otaci list. Aplikace pro Macy uz mohou odstrihnout Intel | `Search` Apple dovolil vyvojarum v Mac App Storu ukoncit podporu Intel Macu | `Balanced` Intel Macy dostaly dalsi stopku. Apple povolil vyvojarum ukoncit jejich podporu
- Doporucena: `Balanced` - spojuje emoci i jasnou zpravu a neni to jen sucha developerska veta.

## Vrstva 2 — Inspirace a updaty

### 2. Ford vysvetlil, proc v novych elektromobilech zvolil Apple Maps misto Googlu
- Action: `FOLLOW-UP`
- Proc je tady: na LSA uz existuje starsi Ford/Apple Maps coverage, novy kus je silny spis jako follow-up s novym vysvetlenim.

### 3. John Ternus rozeslal prvni memo a zaroven se objevily detaily jeho odmeny
- Action: `FOLLOW-UP`
- Proc je tady: management cluster je zivy, ale zakladni John Ternus intent uz web pokryva.

### 4. Apple Watch Series 12: tri nove funkce pred pristi tydennim uvedenim
- Action: `FOLLOW-UP`
- Proc je tady: novy peg existuje, ale intent se prekryva se starsimi expectation kusy.

### 5. Dorazily dalsi detaily k iPhone Ultra
- Action: `FOLLOW-UP`
- Proc je tady: GSC cluster je silny, ale intent overlap na LSA je uz moc tesny na dalsi cisty CREATE.

### 6. Lake America / Apple Maps cluster neotevirat jako novy slot
- Action: `UPDATE`
- Proc je tady: Manticore uz ukazuje dnesni publikovany LSA kus, takze dalsi CREATE by byl duplicitni.

## Datova opora

- `GSC`: iPhone 18 `505 678 imp`, iPhone 18 Pro `190 590 imp`, iPhone 18 Pro Max `207 557 imp`, iPhone Ultra `57 295 imp`
- Z toho plyne: LSA backbone dnes stoji vic na update/follow-up Apple hardware clusterech nez na mnoha cistych overnight novinkach.

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
