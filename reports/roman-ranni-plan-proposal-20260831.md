# Ranní redakční plán V6.5 pro 31. 8. 2026

DATA GATE: GSC PASS | GA4 PASS | Manticore PASS

Fallbacky: `Google SERP Search API`, `Google SERP Trends Search API`, `Competitor Research`, `seo-content` a `humanizer` nebyly v tomto běhu přímo callable, takže fallback byl `web_search` + `web_fetch` + live `Manticore` + live `GSC/GA4` + `pytrends`.

Dnes je slabší ranní okno a neprotlačuji slabé sloty. Po duplicate, intent overlap a reality checku mají méně než 5 čistých `CREATE` všechny tři weby:
- LSA: 1
- Android Magazine: 3
- Samsung Magazine: 0

## Vrstva 1 — Priority
Jen silné nové `CREATE` sloty k napsání teď.

### LSA

#### 1. Apple Watch Series 12: leak na always-on měření tepu a novou Fitness app
- Proč teď: 9to5Mac v ranním okně rozebral čerstvý Gurman/Bloomberg leak před zářijovým Apple eventem.
- Proč beru: je to dnešní Apple health peg s jasným dopadem pro běžné uživatele; live `pytrends` ukazuje `apple watch` CZ `latest 30 / max 89` za 7 dní.
- Data backbone: live GSC 28 dní ukazuje pro cluster `apple watch ultra 4` `25 274` impresí, `2 759` kliků, `10,92 %` CTR a pozici `2,87`.
- Duplicate / intent: Manticore nenašel stejný intent jako samostatný kus.
- Titulek 1 (`Discover`) [DOPORUČENO]: Apple Watch má dostat funkci, kterou fitness náramky umí lépe už dnes. Apple to chce konečně otočit
- Titulek 2 (`Search`): Apple Watch Series 12 možná nabídne nepřetržité měření tepu a novou Fitness aplikaci
- Titulek 3 (`Balanced`): Apple chystá pro Apple Watch velký health upgrade. Co naznačuje nový únik
- Proč doporučený: zdůrazňuje praktický dopad místo samotného leak labelu.

### Android Magazine

#### 1. Android 17 QPR2 Beta 4
- Proč teď: Google posunul další betu s opravami pro Pixely a 9to5Google má zároveň rollout i seznam změn.
- Proč beru: čistý systémový peg s jasným uživatelským dopadem a bez stejného intentu v Manticore.
- Titulek 1 (`Discover`) [DOPORUČENO]: Android 17 QPR2 Beta 4 je venku. Google opravuje věci, které Pixelům lezly na nervy
- Titulek 2 (`Search`): Android 17 QPR2 Beta 4: seznam novinek, oprav a podporovaných Pixelů
- Titulek 3 (`Balanced`): Nová beta Androidu 17 míří na Pixely. Co opravuje a co přidává
- Proč doporučený: prodává konkrétní užitek z oprav místo interního názvu buildu.

#### 2. Gemini Notebook mění usage limity
- Proč teď: Google oficiálně potvrdil přechod na compute-based limity s rolloutem od 2. září.
- Proč beru: je to reálná změna pravidel používání, ne marketingový AI přepis; live `pytrends` ukazuje `gemini` CZ `latest 52 / max 100`.
- Duplicate / intent: Manticore bez stejného intentu.
- Titulek 1 (`Discover`) [DOPORUČENO]: Gemini Notebook mění pravidla používání. Denní limit končí a přichází něco chytřejšího
- Titulek 2 (`Search`): Gemini Notebook zavádí compute-based usage limits od 2. září
- Titulek 3 (`Balanced`): Google mění limity v Gemini Notebooku. Co to znamená pro běžné používání
- Proč doporučený: překládá interní změnu do jasného user dopadu.

#### 3. WhatsApp Scam Alert vstupuje do Android bety
- Proč teď: GSMArena v okně potvrdila, že se funkce dostává k beta uživatelům Androidu po dřívějším oznámení WhatsAppu.
- Proč beru: bezpečnostní a praktický kus; live `pytrends` ukazuje `whatsapp` CZ `latest 38 / max 38`.
- Duplicate / intent: Manticore bez stejného intentu.
- Titulek 1 (`Discover`) [DOPORUČENO]: WhatsApp na Androidu zkouší ochranu proti podvodům. Nová funkce vás varuje dřív, než naletíte
- Titulek 2 (`Search`): WhatsApp Scam Alert pro Android: jak funguje a kde se zapíná
- Titulek 3 (`Balanced`): WhatsApp přidává na Androidu Scam Alert. Umí varovat před podezřelou zprávou
- Proč doporučený: bezpečnostní promise je jasný hned z titulku.

### Samsung Magazine

Žádné čisté `CREATE` teď. Co prošlo overnight scanem, buď nemá dost silný dnešní peg, nebo naráží na intent overlap s čerstvou vlastní coverage.

## Vrstva 2 — Inspirace a updaty
Kurátorovaný doplněk, ne odpad po vrstvě 1.

### LSA
- Meta AI v CarPlay | `FOLLOW-UP` | nový hráč je Meta, ale intent overlap naráží na starší Grok/CarPlay kus.
- CarPlay nově podporuje Storm Radar | `GOOD_SIGNAL_WEAK_TODAY` | praktické, ale slabší click power než Apple Watch leak.
- iPad mini na říjen | `WAIT_FOR_PEG` | rumor je nový, ale live `pytrends` už padl na nulu a na webu běží blízký rumor round-up.
- iPhone 18 keynote stream / datum | `UPDATE_BASE` | live GA4 i GSC potvrzují silný current-demand cluster, vhodné na update, ne nový slot.

### Android Magazine
- Google Messages nová várka funkcí | `UPDATE_BASE` | dobrý user kus, ale dnešní CZ trend je slabší než u ostatních tří CREATE.
- Jak vypnout telefon s Androidem | `DATA_BACKBONE` | live GSC 28 dní: `1 075` impresí / `19` kliků pro hlavní query cluster.
- Obnova smazané aplikace na Androidu | `DATA_BACKBONE` | live GSC potvrdil stabilní troubleshooting poptávku.
- Kde najít svoje telefonní číslo v Androidu | `DATA_BACKBONE` | live GSC drží několik jazykových variant téhož intentu.

### Samsung Magazine
- Smart Switch na Galaxy Z Fold8 | `UPDATE_ONLY` | Samsung Newsroom vydal oficiální text, ale Manticore našel vlastní kus z 27. 8. se stejným intentem.
- Android Auto na Samsungu | `DATA_BACKBONE` | live GSC 28 dní: `109 165` impresí / `19 133` kliků / pozice `5,16`.
- One UI / přehled aktualizací | `UPDATE_BASE` | live GSC i GA4 potvrzují stabilní zájem, ale hlavní update kus už web dnes má.
- Starý telefon jako dashcam | `FOLLOW-UP` | live GA4 drží vysokou návštěvnost, vhodné na navazující praktický update, ne nový ranní slot.

## Source Coverage Audit
- WordPress: CHECKED
- GSC: CHECKED live
- GA4: CHECKED live
- Manticore: CHECKED live
- Google Trends: CHECKED via `pytrends` fallback
- Google News / search vrstva: CHECKED via `web_search`
- 9to5Mac / 9to5Google / GSMArena / Samsung Newsroom / Google Blog: CHECKED
- Apple Newsroom: CHECKED / NO RELEVANT OVERNIGHT SIGNAL
- GitHub: CHECKED / NO RELEVANT CONSUMER-READY SIGNAL
- APKMirror: UNAVAILABLE (`403`)
- Reddit RSS: UNAVAILABLE (blocked i přes RSS fallback)

Bez explicitního schválení Romana nebo Toma nic nezapisuji na WordPress a negeneruji finální PDF.

Je to pro vás vyhovující?
