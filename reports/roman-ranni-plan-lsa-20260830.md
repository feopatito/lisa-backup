# LSA — Ranní redakční plán 30.8.2026

Web: letemsvetemapplem.eu
Datum: 30. 8. 2026
DATA GATE: PASS | live GSC + GA4 + Manticore ověřeno 30.8.2026 ráno
Schválený export: PDF na žádost Romana

Dnes je slabší ranní okno a neprotlačuji slabé sloty. Po duplicate, intent overlap a reality checku vyšel pro LSA jeden čistý `CREATE`.

## Vrstva 1 — Priority
Jen silné nové `CREATE` sloty k napsání teď.

### 1. Meta AI míří do Apple CarPlay
- Action: `CREATE`
- Lane: `Discovery / Current Demand`
- Proč teď: 9to5Mac v ranním okně potvrdilo, že Meta AI nově vstupuje do CarPlay jako další AI chatbot ještě před veřejným nástupem Siri AI.
- Proč beru: čistý Apple-user angle pro řidiče s iPhonem; Manticore nenašel stejný intent na webu.
- Hard evidence: 9to5Mac + live fetch článku; zatím jde o limitovaný test, ne plošný rollout.
- FINAL_WRITE_GATE: `PASS`
- Titulek 1 (`Discover`) [DOPORUČENO]: Do CarPlay míří další AI. Meta předbíhá Siri a zkouší vlastní chatbot přímo v autě
- Titulek 2 (`Search`): Meta AI přichází do Apple CarPlay. Co umí a jaké má limity
- Titulek 3 (`Balanced`): CarPlay získává Meta AI dřív než Siri AI. Co z toho dnes opravdu funguje
- Proč doporučený: spojuje novost i střet se Siri, takže má vyšší click potential než čistě utilitární formulace.

## Vrstva 2 — Inspirace a updaty
Kurátorovaný doplněk, ne odpad po vrstvě 1.

### 1. Apple Health s AI coachem
- Action: `MONITOR`
- Důvod: `WAIT_FOR_PEG`
- Proč je tady: follow-up na Gurman/9to5Mac, ale bez primárního potvrzení a zatím spíš keynote spekulace.

### 2. Apple smart glasses roundup
- Action: `MONITOR`
- Důvod: `WAIT_FOR_PEG`
- Proč je tady: nový je detail funkcí a designů, ale intent už LSA pokrývá a zatím jde pořád o rumor cluster.

### 3. Apple Card novinky
- Action: `DROP`
- Důvod: `US_ONLY`
- Proč je tady: produktově zajímavé, ale pro českého čtenáře slabý lokální dopad.

### 4. iPhone 18 Pro předobjednávky
- Action: `MONITOR`
- Důvod: `TOO_CLOSE_TO_EXISTING`
- Proč je tady: stejná potřeba čtenáře už na LSA běží ve velmi blízkém intentu.

### 5. iCloud tarify v ČR
- Action: `UPDATE`
- Důvod: `DATA_BACKBONE`
- Proč je tady: silná GSC vrstva pro update/rewrite, vhodné jako search slot mimo ranní breaking linku.

### 6. WhatsApp podvody na iPhonu
- Action: `UPDATE`
- Důvod: `DATA_BACKBONE`
- Proč je tady: GSC backbone + dnešní bezpečnostní signál z WhatsApp vrstvy.

## Source Coverage Audit
- WordPress: CHECKED
- GSC: CHECKED live
- GA4: CHECKED live
- Manticore: CHECKED live
- Google Trends: CHECKED via `pytrends` fallback
- Google News / search vrstva: CHECKED via `web_search`
- 9to5Mac: CHECKED
- Apple Newsroom: CHECKED / NO RELEVANT SIGNAL
- WhatsApp Blog / Meta Newsroom: CHECKED
- GitHub: NOT CHECKED - REASON `v tomto běhu nepřinesl rychlejší consumer-ready vrstvu než live news + data backbone`
- Reddit RSS: UNAVAILABLE (`403` i přes RSS fallback)
