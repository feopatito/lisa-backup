# Ranni redakcni plan V6.5 pro 4. 9. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS

Skill vrstva:
- Google SERP Search API: FAIL (`402 insufficient credits`) -> fallback `live RSS + Google News RSS`
- Google SERP Trends Search API: FAIL (`402 insufficient credits`) -> fallback `pytrends`
- Competitor Research: skill nepouzity -> fallback `Manticore + source cross-check`
- seo-content: skill nepouzity -> fallback `Roman Test + Manticore + manual uniqueness gate`
- humanizer: nechavam az na PDF po schvaleni

Poznamka ke kvalite:
- LSA ma dnes jen `2` ciste overnight `CREATE`.
- Android Magazine ma dnes jen `3` ciste overnight `CREATE`.
- Samsung Magazine ma dnes jen `1` cisty overnight `CREATE`.
- Samsung je dnes nejslabsi; dalsi kusy jsem nechala ve `Vrstva 2`, protoze nemaji dost silny novy samostatny peg.

## LSA

### Vrstva 1 - Priority

1. `CREATE` Kalendar v iOS 27 dostava viditelny redesign klicovych funkci.
   Why now: `9to5Mac` publikovalo detail v `21:02 CEST`, tema je cerstve, uzivatelsky srozumitelne a Manticore nenasel stejny intent. `GSC` zaroven drzi `ios 27` na `30 474 imp`, takze software cluster zije.
   Titulky: `Discover` Kalendar v iOS 27 projde zmenou, kterou poznate hned pri prvnim otevreni | `Search` Apple meni Kalendar v iOS 27. Tohle jsou nove designove zmeny klicovych funkci | `Balanced` iOS 27 predelava Kalendar. Zmeny jsou videt presne tam, kde ho pouzivate nejvic
   Doporucena: `Balanced` - spojuje jasnou utilitu i konkretni produktovy peg a nepusobi jako interni changelog.

2. `CREATE` OpenAI pustilo GPT-6 Astra do ChatGPT a Codexu.
   Why now: mame `OpenAI` primarni oznameni i nasledny `9to5Mac` kus v rannim okne; na LSA neni stejny intent a siri se to jako velka produktova novinka pro lidi, kteri jedou AI workflow na iPhonu a Macu.
   Titulky: `Discover` ChatGPT a Codex dostaly nejvetsi upgrade za rok. Na Macu a iPhonu to poznate hned | `Search` GPT-6 Astra je venku. Co se meni pro ChatGPT a Codex | `Balanced` OpenAI pustilo GPT-6 Astra do ChatGPT a Codexu. Tohle jsou zmeny, ktere dava smysl resit i na Apple zarizenich
   Doporucena: `Discover` - nejlip prodava realny dopad na Apple workflow a neni to jen abstraktni AI zprava.

### Vrstva 2 - Inspirace a updaty

3. `FOLLOW-UP` iPhone 18 Pro a Pro Max maji dostat dve nove display novinky uz pristi tyden.
   Proc je tady: `GSC` pro `iphone 18` (`229 566 imp`) a `iphone 18 pro` (`121 408 imp`) je brutalne silne, ale stejny ctenarsky intent uz na LSA bezi v aktualnim iPhone 18 clusteru.

4. `FOLLOW-UP` Vision Pro se objevil pri dalsi operaci.
   Proc je tady: novy peg existuje, ale Manticore nasel starsi LSA kus se stejnou zakladni potrebou ctenare (`Vision Pro v chirurgii`), takze novy solo slot by byl moc tesny.

5. `GOOD_SIGNAL_WEAK_TODAY` MacBook Neo 2: everything we know so far.
   Proc je tady: signal je cerstvy, ale spis roundup/ocekavani nez silny dnesni samostatny pribeh.

### Datova opora

- `GSC`: `iphone 18` `229 566 imp`, `iphone 18 pro` `121 408 imp`, `ios 27` `30 474 imp`
- `GA4`: nejvic rano drzi aktivni `iPhone 18` cluster a `Apple Watch Ultra 4` kusy, takze LSA muze bezpecne stavet na pred-event Apple demandu.

## Android Magazine

### Vrstva 1 - Priority

1. `CREATE` Google Clock meni Timery a pridava presety.
   Why now: `9to5Google` to pustilo ve `01:44 CEST`, Manticore nevraci stejny intent a jde o praktickou drobnost, kterou bezny androidak pochopi bez dalsiho vysvetlovani.
   Titulky: `Discover` Google konecne opravilo jednu z nejotravnejsich casti aplikace Hodiny | `Search` Google Clock na Androidu meni Timery a pridava presety | `Balanced` Hodiny v Androidu dostavaji nove Timery s presety. Tahle zmena dava smysl hned
   Doporucena: `Discover` - prodava odstraneni konkretni frustrace a ma vyssi click potencial nez suchy popis UI.

2. `CREATE` Gemini Spark uz umi ovladat Google Photos pro upravy, sdileni a dalsi kroky.
   Why now: `9to5Google` publikovalo rollout ve `23:44 CEST`, Google News potvrdil rychly coverage cluster a Android Magazine na to nema stejny intent.
   Titulky: `Discover` Gemini uz umi sahat do Fotek a delat za vas upravy i sdileni | `Search` Gemini Spark dostava ovladani Google Photos pro editaci a sdileni | `Balanced` Google pousti Gemini do aplikace Fotky. Zvladne upravy, sdileni i dalsi kroky
   Doporucena: `Discover` - nejlip prevadi AI funkci do srozumitelneho uzitku, ktery ctenar vidi hned.

3. `CREATE` Google predstavil WeatherNext 3 a slibuje presnejsi dest v Search i Gemini.
   Why now: mame primarni zdroj `Google Blog` a sekundarni coverage `9to5Google` v okne; Manticore nenasel overlap a je to citelna AI zmena, kterou jde prodat pres realny denni dopad.
   Titulky: `Discover` Google slibuje presnejsi dest v Search i Gemini. Nasadilo novy AI model | `Search` Google predstavil WeatherNext 3. Co meni v Search a Gemini | `Balanced` Search i Gemini dostaly novy pocasi model od Googlu. Slibuje o polovinu presnejsi srazky
   Doporucena: `Balanced` - spojuje silny slib se srozumitelnym produktem a porad drzi dobry search tvar.

### Vrstva 2 - Inspirace a updaty

4. `FOLLOW-UP` Motion Assist se uz realne roluje na telefony s Androidem 17.
   Proc je tady: rollout je skutecny, ale Manticore nasel uz publikovany Android Magazine kus o zariovem Android dropu, takze na cisty CREATE je overlap prilis tesny.

5. `FOLLOW-UP` Google Home update opravuje budiky a hlasove ovladani smart home.
   Proc je tady: silny user-pain signal, ale dnes je to vic Home ekosystem nez top telefonni slot.

6. `INSPIRATION_ONLY` Ma smysl prejit z Pixelu 9 na Pixel 11?
   Proc je tady: dobry servisni/comparison kus, ale rano nema dostatecne tvrdy `why now`.

### Datova opora

- `GSC`: `google pixel` `6 imp`, `gemini` `6 imp`, `google clock` `4 imp` -> rano je tady slaba search kostra a rozhoduje cerstvost signalu, ne SEO backbone
- `GA4`: Androidu rano tahnou spis starsi utilitni kusy a lokalizovane clanky, proto jsem nechala jen tri opravdu ciste overnight sloty

## Samsung Magazine

### Vrstva 1 - Priority

1. `CREATE` Samsung spustil One UI 9 Watch beta pro Galaxy Watch 7 a Galaxy Watch Ultra.
   Why now: `SamMobile` to pustilo v `05:01 CEST`, Google News okamzite ukazuje dalsi coverage a `GSC` pro `galaxy watch` drzi `3 246 imp`. Na webu sice mame starsi kus k `Watch 8`, ale ne stejny intent pro `Watch 7` a `Ultra`.
   Titulky: `Discover` Samsung pustil novou betu do dalsich Galaxy Watch a prinesla i dve zdravi novinky | `Search` One UI 9 Watch beta je venku pro Galaxy Watch 7 a Galaxy Watch Ultra | `Balanced` One UI 9 Watch miri na dalsi hodinky Samsungu. Tohle dostaly Galaxy Watch 7 a Ultra
   Doporucena: `Balanced` - nejlip spojuje sirku zasahu i konkretni modely bez zbytecneho technickeho tonu.

### Vrstva 2 - Inspirace a updaty

2. `FOLLOW-UP` One UI 9 obecny rollout hub.
   Proc je tady: `GSC` pro `one ui 9` drzi `8 116 imp`, ale core intent uz Samsung Magazine pokryva a potrebuje spis update backbone nez novy solo clanek.

3. `FOLLOW-UP` Galaxy A36 dostal prekvapive One UI 9 beta program.
   Proc je tady: signal je validni, ale spadl mimo ranni overnight okno a navic se prilepuje k sirokemu rollout clustru.

4. `UPDATE` Gemini na Samsungu.
   Proc je tady: obri `GSC` poptavka (`65 637 imp`), ale dnes bez noveho dost silneho samostatneho pegu na CREATE.

5. `INSPIRATION_ONLY` Samsung posiluje pozici v HBM trhu.
   Proc je tady: realny byznys signal, ale pro mobilni rano nema dost silny click story.

6. `INSPIRATION_ONLY` Samsung vs. Apple foldable angle pred keynote.
   Proc je tady: redakcne zajimave jako komentar nebo priprava follow-upu na keynote tyden, ale ne jako dnesni tvrdy novy slot.

### Datova opora

- `GSC`: `one ui 9` `8 116 imp`, `galaxy watch` `3 246 imp`, `galaxy a36` `79 imp`, `gemini` `65 637 imp`
- `GA4`: utility backbone drzi One UI a navodove kusy; dnes se neukazal dost silny druhy overnight Samsung peg pro dalsi cisty CREATE

## Source Coverage Audit

- WordPress / Manticore: `CHECKED`
- GSC: `CHECKED`
- GA4: `CHECKED`
- Google SERP Search API: `UNAVAILABLE - 402 insufficient credits`
- Google SERP Trends Search API: `UNAVAILABLE - 402 insufficient credits`
- Google Trends fallback (`pytrends`): `PARTIAL - probehl jen uzky shortlist, jasny spike vysel hlavne pro one ui 9 watch; ostatni specificke dotazy byly slabe nebo prilis uzke`
- Google News RSS: `CHECKED`
- major tech media: `CHECKED - 9to5Mac, 9to5Google, GSMArena, SamMobile`
- official newsrooms: `CHECKED - Apple Newsroom: no relevant overnight signal, Samsung Newsroom: no relevant mobile overnight signal, Google Blog: relevant WeatherNext 3 signal`
- Reddit RSS: `UNAVAILABLE - blocked despite browser UA`
- GitHub: `NOT CHECKED - dnes nevyhral zadny commit/docs peg nad silnejsimi overnight user-facing signaly`
- APK / teardown layer: `NOT CHECKED - dnes neporazily silnejsi overnight user-facing signaly`

Je to pro vas vyhovujici?
