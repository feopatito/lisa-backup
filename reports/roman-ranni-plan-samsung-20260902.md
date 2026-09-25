# Samsung Magazine — Ranni redakcni plan — 2. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS

Format:
- `Vrstva 1` = silne `CREATE` k napsani ted
- `Vrstva 2` = follow-upy, updaty a inspirace bez umeleho nafukovani

## Vrstva 1 — Priority

### 1. Samsung nekterym lidem nahodne deaktivuje ucty kvuli "security reasons"
- Action: `CREATE`
- Why now: cerstvy user-pain kus z `9to5Google`, cisty prakticky problem a Manticore nevraci stejny intent.
- Titulky: `Discover` Samsung lidem vypina ucty a jako duvod hlasi bezpecnost | `Search` Samsung account deactivated for security reasons: co se deje a co zkusit | `Balanced` Samsung nekterym uzivatelum deaktivuje ucet. Duvod ma byt bezpecnost
- Doporucena: `Balanced` - je nejsrozumitelnejsi a okamzite rika, koho se problem tyka.

### 2. One UI 9 beta se tento mesic siri na dalsi Galaxy telefony
- Action: `CREATE`
- Why now: novy rollout cluster z `9to5Google` + `Android Authority`, silny aktualni Samsung intent.
- Titulky: `Discover` One UI 9 miri na dalsi Galaxy telefony a nektere dorazi uz tenhle mesic | `Search` One UI 9 beta expands to more Galaxy phones in September 2026 | `Balanced` Samsung rozsiruje One UI 9 beta. Tyhle Galaxy telefony maji byt dalsi na rade
- Doporucena: `Balanced` - nejlip spojuje seznamovy search intent s klikavou nalehavosti.

### 3. Galaxy S25 dostava pres One UI 9 beta jeden z nejzajimavejsich foto triku ze S26
- Action: `CREATE`
- Why now: `Android Authority` popsalo konkretni feature spillover, ktery unese vlastni Samsung pribeh.
- Titulky: `Discover` Samsung posila do Galaxy S25 foto trik, ktery si nechaval pro S26 | `Search` Galaxy S25 One UI 9 beta adds S26 camera trick | `Balanced` Galaxy S25 dostava v One UI 9 beta jednu z nejlepsich foto novinek ze S26
- Doporucena: `Discover` - ma nejsilnejsi click potential, protoze prodava prenos funkce z novejsi rady.

### 4. Samsung store reklamy v telefonu: jak je zastavit
- Action: `CREATE`
- Why now: `SamMobile` otevrel konkretni user pain s okamzite uzitelnym resenim.
- Titulky: `Discover` Chodite do Samsung prodejny? Telefon vam pak muze zacit cpat reklamy | `Search` How to stop Samsung store ads on Galaxy phone | `Balanced` Samsung umi posilat reklamy po navsteve prodejny. Takhle je vypnete
- Doporucena: `Balanced` - propojuje sokovy hook s okamzitym resenim.

## Vrstva 2 — Inspirace a updaty

### 5. Gemini na Samsungu
- Action: `UPDATE`
- Proc je tady: silny GSC cluster, ale dnes bez dost silneho noveho pegu na CREATE.

### 6. One UI 9 obecny rozcestnik
- Action: `UPDATE`
- Proc je tady: obrovsky demand, vhodne drzet jako servisni/update backbone.

### 7. Android Auto na Samsungu
- Action: `UPDATE`
- Proc je tady: vysoky dlouhodoby zajem a silny utility intent.

### 8. One UI 9 pro starsi foldables
- Action: `GOOD_SIGNAL_WEAK_TODAY`
- Proc je tady: dobry signal, ale dnes ho radsi drzim pod sirsim rollout clustrem nez jako separatni hlavni slot.

### 9. My FanCam / feature story kolem Z8
- Action: `INSPIRATION_ONLY`
- Proc je tady: zajimave zakulisi, ale bez dostatecneho why now pro solo clanek.

## Datova opora

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
