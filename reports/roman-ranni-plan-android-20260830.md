# Android Magazine — Ranní redakční plán 30.8.2026

Web: androidmagazine.eu
Datum: 30. 8. 2026
DATA GATE: PASS | live GSC + GA4 + Manticore ověřeno 30.8.2026 ráno
Schválený export: PDF na žádost Romana

Dnes je slabší ranní okno a neprotlačuji slabé sloty. Po duplicate, intent overlap a reality checku vyšly pro Android Magazine čtyři čisté `CREATE`.

## Vrstva 1 — Priority
Jen silné nové `CREATE` sloty k napsání teď.

### 1. Android 17 QPR2 Beta 4
- Action: `CREATE`
- Lane: `Current Demand / Beta rollout`
- Proč teď: rollout i detailní seznam oprav vyšly v aktuálním okně; build dosáhl `Platform Stability`.
- Proč beru: silný Pixel/Android systémový peg, bez stejného intentu na webu.
- Hard evidence: 9to5Google `Android 17 QPR2 Beta 4 rolling out with many Pixel bug fixes` + `Here’s everything new in Android 17 QPR2 Beta 4`
- FINAL_WRITE_GATE: `PASS`
- Titulek 1 (`Discover`) [DOPORUČENO]: Android 17 QPR2 Beta 4 je venku. Google opravuje věci, které Pixelům lezly na nervy
- Titulek 2 (`Search`): Android 17 QPR2 Beta 4: seznam novinek, oprav a podporovaných Pixelů
- Titulek 3 (`Balanced`): Nová beta Androidu 17 míří na Pixely. Co opravuje a co přidává
- Proč doporučený: prodává konkrétní užitek z oprav místo interního názvu buildu.

### 2. Google Messages zavádí novou várku funkcí
- Action: `CREATE`
- Lane: `Current Demand / Utility`
- Proč teď: 9to5Google aktualizovalo velký rollout přehled k 29. 8. a přibyly jasné user-facing změny.
- Proč beru: široký Android zásah, dobrý explain kus, Manticore nenašel stejný intent.
- Hard evidence: 9to5Google `What new Google Messages features are rolling out [August 2026]`
- FINAL_WRITE_GATE: `PASS`
- Titulek 1 (`Discover`): Zprávy Google se tiše mění. Tohle jsou funkce, které vám mohou dorazit jako další
- Titulek 2 (`Search`): Google Messages: jaké nové funkce se právě zavádějí v srpnu 2026
- Titulek 3 (`Balanced`) [DOPORUČENO]: Google postupně mění Zprávy. Přehled novinek, které už běží nebo se testují
- Proč doporučený: funguje pro klik i search intent a dovolí jasně filtrovat, co je live a co jen beta.

### 3. Gemini Notebook mění usage limity
- Action: `CREATE`
- Lane: `Current Demand / Product change`
- Proč teď: Google potvrdil nový model limitů s rolloutem od 2. září a 9to5Google ho rozebral.
- Proč beru: jde o reálnou změnu pravidel používání, ne marketingové AI mlžení.
- Hard evidence: Google Blog `We’re introducing flexible usage limits for Gemini Notebook` + 9to5Google
- FINAL_WRITE_GATE: `PASS`
- Titulek 1 (`Discover`) [DOPORUČENO]: Gemini Notebook mění pravidla používání. Denní limit končí a přichází něco chytřejšího
- Titulek 2 (`Search`): Gemini Notebook zavádí compute-based usage limits od 2. září
- Titulek 3 (`Balanced`): Google mění limity v Gemini Notebooku. Co to znamená pro běžné používání
- Proč doporučený: srozumitelně říká, že se mění pravidla používání, ne jen interní terminologie Googlu.

### 4. WhatsApp Scam Alert vstupuje do Android bety
- Action: `CREATE`
- Lane: `Current Demand / Security`
- Proč teď: GSMArena ráno potvrdila dostupnost pro beta uživatele Androidu po dřívějším oznámení Meta.
- Proč beru: bezpečnostní, praktický a klikatelný kus s jasným user dopadem.
- Hard evidence: GSMArena + dřívější WhatsApp Blog / Meta Newsroom post o security features
- FINAL_WRITE_GATE: `PASS`
- Titulek 1 (`Discover`) [DOPORUČENO]: WhatsApp na Androidu zkouší ochranu proti podvodům. Nová funkce vás varuje dřív, než naletíte
- Titulek 2 (`Search`): WhatsApp Scam Alert pro Android: jak funguje a kde se zapíná
- Titulek 3 (`Balanced`): WhatsApp přidává na Androidu Scam Alert. Umí varovat před podezřelou zprávou
- Proč doporučený: bezpečnostní promise je jasný hned z titulku a není závislý na znalosti názvu funkce.

## Vrstva 2 — Inspirace a updaty
Kurátorovaný doplněk, ne odpad po vrstvě 1.

### 1. Android Auto po aktualizaci nefunguje
- Action: `UPDATE`
- Důvod: `DATA_BACKBONE`
- Proč je tady: dlouhodobě silný troubleshooting intent, vhodné na dnešní search slot.

### 2. Stažené soubory v Androidu: kde jsou
- Action: `UPDATE`
- Důvod: `DATA_BACKBONE`
- Proč je tady: nejsilnější evergreen z GSC, vhodné pro update s lepší SERP defensibility.

### 3. Tovární nastavení Androidu bez ztráty dat
- Action: `UPDATE`
- Důvod: `DATA_BACKBONE`
- Proč je tady: silný praktický dotaz s dobrou šancí na klik navzdory AI answers.

### 4. Google Zprávy: RCS a nastavení
- Action: `UPDATE`
- Důvod: `UPDATE_BASE`
- Proč je tady: může navázat na dnešní Messages peg utilitárním kusem.

### 5. Play Books v Gemini Notebooku přes Expert Intelligence
- Action: `FOLLOW-UP`
- Důvod: `FOLLOW-UP`
- Proč je tady: dobrý produktový signál, ale hlavní peg neleží v dnešním okně.

### 6. Gboard / APKMirror buildy
- Action: `MONITOR`
- Důvod: `WAIT_FOR_PEG`
- Proč je tady: release samotný nestačí bez teardownu nebo potvrzené nové funkce.

## Source Coverage Audit
- WordPress: CHECKED
- GSC: CHECKED live
- GA4: CHECKED live
- Manticore: CHECKED live
- Google Trends: CHECKED via `pytrends` fallback
- Google News / search vrstva: CHECKED via `web_search`
- 9to5Google: CHECKED
- Google Blog: CHECKED
- GSMArena: CHECKED
- WhatsApp Blog / Meta Newsroom: CHECKED
- GitHub: NOT CHECKED - REASON `v tomto běhu nepřinesl rychlejší consumer-ready vrstvu než live news + data backbone`
- Reddit RSS: UNAVAILABLE (`403` i přes RSS fallback)
