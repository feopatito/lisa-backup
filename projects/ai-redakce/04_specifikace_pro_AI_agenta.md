# AI REDAKČNÍ SYSTÉM — SPECIFIKACE PRO AI AGENTA
*Implementační zadání: architektura, datové modely, workflow, guardrails a milníky • v1.0 • 11. srpna 2026*

## Architektonické principy
- **Modular adapters** — každá externí služba přes vlastní interface
- **Event + job model** — dlouhé workflow rozdělit na idempotentní joby s retry
- **Structured outputs** — mezi agenty validované JSON objekty, ne volný text
- **Human gates** — schválení musí být explicitní stav workflow
- **Observability** — logovat prompt/model/token cost/latency/source IDs
- **Source provenance** — každé faktické tvrzení musí mít source reference
- **No silent failure** — chybějící data snižují confidence a jsou viditelná

## Implementační milníky
- **M0**: repository, config, schemas, database, job runner, logging, tests
- **M1**: WordPress read adapter + archive ingestion
- **M2**: Search Console + Analytics ingestion a normalized metrics
- **M3**: opportunity detectors + scoring + daily brief, bez generování textu
- **M4**: research/SEO/editor brief pipeline se structured outputs
- **M5**: writer + fact-check + review dashboard
- **M6**: WordPress create/update draft za approval gate
- **M7**: post-publish measurement + experiment tracking
- **M8**: selective autopilot pro whitelisted nízkorizikové typy obsahu

## Human approval state machine
```
DISCOVERED → SCORED → BRIEF_READY → RESEARCHED → DRAFTED
→ FACTCHECKED → NEEDS_HUMAN_APPROVAL → APPROVED
→ WP_DRAFT_CREATED → PUBLISHED → MEASURING

Failure: BLOCKED_SOURCE | BLOCKED_FACTCHECK | REJECTED | RETRYABLE_ERROR
```

## Topic scoring komponenty (0–100)
- freshness 0–15
- audience demand 0–20
- SEO opportunity 0–20
- brand relevance 0–15
- expected value 0–15
- source confidence 0–10
- strategic value 0–10
- risk penalty 0–15 (odečíst)

## SEO opportunity detektory
- **Striking distance** — pozice 4–20 s meaningful impressions
- **CTR gap** — rozdíl observed vs. expected CTR
- **Rising demand** — akcelerace impressions/query demand
- **Decay** — historicky silné stránky s poklesem
- **Cannibalization** — více URL soutěžících o stejný query cluster
- **Content gap** — relevantní dotazy bez interní landing page
- **Refresh candidate** — starý článek s autoritou kde update > nové URL

## Fact-check kontrakt
- Extrahovat materiální faktická tvrzení z draftu
- Pro každé tvrzení mapovat source_refs
- Preferovat primární/oficiální zdroje
- Flagovat nepodložené, zastaralé nebo kontradiktorní tvrzení
- Severity: info | warning | critical
- BLOCK pokud kritické tvrzení nemá dostatečnou podporu

## Bezpečnost
- Secrets jen v environment/secret manager, nikdy v promptech nebo logu
- Pilotovat s read-only Google credentials
- WordPress write credentials izolovat do publisher service
- Auditovat každou externí write operaci

## Instrukce pro coding agenta
Build incrementally. Start with M0 only.
Před kódováním: assumptions, stack, repo tree, DB schema, adapter interfaces, risks/missing credentials, acceptance tests.
Neimplementovat autonomous publishing.
Nevymýšlet nezdokumentované API capabilities.
Všechny model outputs = schema-validated.
Po M0 → stop a request approval for M1.
