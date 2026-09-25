# Ranní redakční plán V6.5 pro 30. 8. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS  
Fallbacky: `Google SERP Search API`, `Google SERP Trends Search API`, `Competitor Research`, `seo-content` a `humanizer` nebyly v tomto běhu aktivně ready jako přímé callable nástroje, takže fallback byl `web_search` + `web_fetch` + RSS + live `Manticore` + `pytrends`.

Dnes je to slabší ráno a neprotlačuji slabé sloty. Po duplicate, intent overlap a reality checku mají méně než 5 čistých `CREATE` všechny tři weby:
- LSA: 1
- Android Magazine: 4
- Samsung Magazine: 0

## Vrstva 1 — Priority
Jen silné nové `CREATE` sloty k napsání teď.

### LSA

#### 1. Meta AI míří do Apple CarPlay
- Proč teď: 9to5Mac publikovalo v ranním okně potvrzení, že Meta AI nově vstupuje do CarPlay jako čtvrtý AI chatbot před veřejným nástupem Siri AI.
- Proč beru: čistý Apple-user angle pro řidiče s iPhonem, Manticore bez stejného intentu.
- Evidence: 9to5Mac + live fetch článku; stav je zatím limitovaný test, ne plošný rollout.
- Titulek 1 (`Discover`) [DOPORUČENO]: Do CarPlay míří další AI. Meta předbíhá Siri a zkouší vlastní chatbot přímo v autě
- Titulek 2 (`Search`): Meta AI přichází do Apple CarPlay. Co umí a jaké má limity
- Titulek 3 (`Balanced`): CarPlay získává Meta AI dřív než Siri AI. Co z toho dnes opravdu funguje
- Proč doporučený: je v něm novost i střet s Siri, takže má vyšší click potential než čistě utilitární formulace.

### Android Magazine

#### 1. Android 17 QPR2 Beta 4
- Proč teď: rollout i detailní seznam oprav vyšly v rámci aktuálního okna; build dosáhl `Platform Stability`.
- Proč beru: silný Pixel/Android systémový peg, bez stejného intentu na webu.
- Evidence: 9to5Google `Android 17 QPR2 Beta 4 rolling out with many Pixel bug fixes` + `Here’s everything new in Android 17 QPR2 Beta 4`.
- Titulek 1 (`Discover`) [DOPORUČENO]: Android 17 QPR2 Beta 4 je venku. Google opravuje věci, které Pixelům lezly na nervy
- Titulek 2 (`Search`): Android 17 QPR2 Beta 4: seznam novinek, oprav a podporovaných Pixelů
- Titulek 3 (`Balanced`): Nová beta Androidu 17 míří na Pixely. Co opravuje a co přidává
- Proč doporučený: prodává konkrétní užitek z oprav místo interního názvu buildu.

#### 2. Google Messages zavádí novou várku funkcí
- Proč teď: 9to5Google aktualizovalo velký rollout přehled k 29. 8. a přibyly jasné user-facing změny.
- Proč beru: široký Android zásah, dobrý explain kus, Manticore nenašel stejný intent.
- Evidence: 9to5Google `What new Google Messages features are rolling out [August 2026]`.
- Titulek 1 (`Discover`): Zprávy Google se tiše mění. Tohle jsou funkce, které vám mohou dorazit jako další
- Titulek 2 (`Search`): Google Messages: jaké nové funkce se právě zavádějí v srpnu 2026
- Titulek 3 (`Balanced`) [DOPORUČENO]: Google postupně mění Zprávy. Přehled novinek, které už běží nebo se testují
- Proč doporučený: funguje pro klik i search intent a dovolí jasně filtrovat, co je live a co jen beta.

#### 3. Gemini Notebook mění usage limity
- Proč teď: Google potvrdil nový model limitů s rolloutem od 2. září a 9to5Google ho rozebral.
- Proč beru: jde o reálnou změnu pravidel používání, ne marketingové AI mlžení.
- Evidence: Google Blog `We’re introducing flexible usage limits for Gemini Notebook` + 9to5Google.
- Titulek 1 (`Discover`) [DOPORUČENO]: Gemini Notebook mění pravidla používání. Denní limit končí a přichází něco chytřejšího
- Titulek 2 (`Search`): Gemini Notebook zavádí compute-based usage limits od 2. září
- Titulek 3 (`Balanced`): Google mění limity v Gemini Notebooku. Co to znamená pro běžné používání
- Proč doporučený: srozumitelně říká, že se mění pravidla používání, ne jen interní terminologie Googlu.

#### 4. WhatsApp Scam Alert vstupuje do Android bety
- Proč teď: GSMArena dnes ráno potvrdila dostupnost pro beta uživatele Androidu po dřívějším oznámení Meta.
- Proč beru: bezpečnostní, praktický a klikatelný kus s jasným user dopadem.
- Evidence: GSMArena + dřívější WhatsApp Blog / Meta Newsroom post o security features.
- Titulek 1 (`Discover`) [DOPORUČENO]: WhatsApp na Androidu zkouší ochranu proti podvodům. Nová funkce vás varuje dřív, než naletíte
- Titulek 2 (`Search`): WhatsApp Scam Alert pro Android: jak funguje a kde se zapíná
- Titulek 3 (`Balanced`): WhatsApp přidává na Androidu Scam Alert. Umí varovat před podezřelou zprávou
- Proč doporučený: bezpečnostní promise je jasný hned z titulku a není závislý na znalosti názvu funkce.

### Samsung Magazine

Žádné čisté `CREATE` teď. Co prošlo overnight scanem, buď nemá dost silný dnešní peg, nebo naráží na intent overlap s čerstvou vlastní coverage.

## Vrstva 2 — Inspirace a updaty
Kurátorovaný doplněk, ne odpad po vrstvě 1.

### LSA
- Apple Health s AI coachem | `WAIT_FOR_PEG` | follow-up na Gurman/9to5Mac, ale bez primárního potvrzení a zatím spíš keynote spekulace.
- Apple smart glasses roundup | `WAIT_FOR_PEG` | nový je detail funkcí a designů, ale intent už LSA pokrývá a zatím jde pořád o rumor cluster.
- Apple Card novinky | `US_ONLY` | produktově zajímavé, ale pro českého čtenáře slabý lokální dopad.
- iPhone 18 Pro předobjednávky | `TOO_CLOSE_TO_EXISTING` | stejná potřeba čtenáře už na LSA běží ve velmi blízkém intentu.
- iCloud tarify v ČR | `DATA_BACKBONE` | silná GSC vrstva pro update/rewrite, vhodné jako search slot mimo ranní breaking linku.
- WhatsApp podvody na iPhonu | `DATA_BACKBONE` | GSC backbone + dnešní bezpečnostní signál z WhatsApp vrstvy.

### Android Magazine
- Android Auto po aktualizaci nefunguje | `DATA_BACKBONE` | dlouhodobě silný troubleshooting intent, vhodné na dnešní search slot.
- Stažené soubory v Androidu: kde jsou | `DATA_BACKBONE` | nejsilnější evergreen z GSC, vhodné pro update s lepší SERP defensibility.
- Tovární nastavení Androidu bez ztráty dat | `DATA_BACKBONE` | silný praktický dotaz s dobrou šancí na klik navzdory AI answers.
- Google Zprávy: RCS a nastavení | `UPDATE_BASE` | může navázat na dnešní Messages peg utilitárním kusem.
- Play Books v Gemini Notebooku přes Expert Intelligence | `FOLLOW-UP` | dobrý produktový signál, ale hlavní peg neleží v dnešním okně.
- Gboard / APKMirror buildy | `WAIT_FOR_PEG` | release samotný nestačí bez teardownu nebo potvrzené nové funkce.

### Samsung Magazine
- Samsung smartglasses a soukromí | `GOOD_SIGNAL_WEAK_TODAY` | dobrý diskusní kus, ale dnešní peg stojí hlavně na opinion textu, ne na novém oficiálním kroku Samsungu.
- Galaxy S26 FE cena a preorder | `UPDATE_ONLY` | intent overlap s čerstvou vlastní coverage na Samsung Magazine.
- One UI 9 Beta 7 pro Galaxy S26 | `UPDATE_ONLY` | stejné téma už web pokryl 28. 8.; dnes bez nového měřitelného posunu.
- Samsung Wallet / Pay v ČR | `DATA_BACKBONE` | velmi silný search slot podle GSC, vhodný na update mimo breaking vrstvu.
- Samsung nejde restartovat / restartuje se | `DATA_BACKBONE` | čistý troubleshooting evergreen se search-first potenciálem.
- Google Fotky na Samsungu: záloha a místo | `DATA_BACKBONE` | silný query cluster s praktickým dopadem.
- Zabezpečená složka Samsung | `DATA_BACKBONE` | dobrý utility update pro search publikum.

## Source Coverage Audit
- WordPress: CHECKED
- GSC: CHECKED live
- GA4: CHECKED live
- Manticore: CHECKED live
- Google Trends: CHECKED via `pytrends` fallback
- Google News / search vrstva: CHECKED via `web_search`
- 9to5Mac / 9to5Google / GSMArena / SamMobile: CHECKED
- Apple Newsroom: CHECKED / NO RELEVANT SIGNAL
- Google Blog: CHECKED
- Samsung Newsroom: CHECKED / NO NEW OVERNIGHT PEG
- WhatsApp Blog / Meta Newsroom: CHECKED
- GitHub: NOT CHECKED - REASON `v tomto běhu nepřinesl rychlejší consumer-ready vrstvu než live news + data backbone`
- Reddit RSS: UNAVAILABLE (`403` i přes RSS fallback)
- Developer forums: NOT CHECKED - REASON `nižší priorita než silnější overnight zdroje`
- X/leakers: CHECKED nepřímo přes Gurman/web search, bez nového silného CREATE pegu
- YouTube: NOT CHECKED - REASON `bez lepšího pegu než textové zdroje`

Bez explicitního schválení Romana nebo Toma nic nezapisuji na WordPress a negeneruji finální PDF.

Je to pro vás vyhovující?
