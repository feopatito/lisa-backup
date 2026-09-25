# GitHub Discovery Monitor

Lokální read-only monitor pro AndroidMagazine.

## Co dělá

- používá pouze veřejné GitHub REST API
- autentizuje se přes `GITHUB_TOKEN`
- sleduje curated whitelist Android / Google repozitářů
- stahuje jen delta změny od `last_successful_sync`
- ukládá raw signály lokálně do SQLite
- deduplikuje podle `repo + event + entity`
- klasifikuje signály na `LOW / MEDIUM / HIGH EDITORIAL POTENTIAL`
- do LLM posílá jen shortlist kandidátů

## Ukládané soubory

- `data/github_signals.db` - raw signály a run log
- `data/github_state.json` - `last_successful_sync`

## Spuštění

```bash
export GITHUB_TOKEN=...
python3 magazines/android-magazine/monitoring/github_discovery_monitor.py
```

## Whitelist

Počáteční whitelist je záměrně úzký a orientovaný na Android / Google / Pixel / Wear OS / Play / docs / security.

### Repozitáře

- `android/nowinandroid`
- `android/compose-samples`
- `android/platform-samples`
- `android/sunflower`
- `android/architecture-samples`
- `android/codelab-android-compose`
- `android/CameraXBasic`
- `googlemaps/android-maps-utils`
- `firebase/quickstart-android`
- `GoogleChrome/android-browser-helper`
- `material-components/material-components-android`
- `googleads/google-ads-mobile-android-examples`

### Organizace

- `android`
- `google`
- `GoogleChrome`
- `firebase`
- `material-components`
- `googleads`
- `googlemaps`

## Jak se používá

GitHub signál sám o sobě nikdy není důvod `CREATE`.
Nejdřív musí projít:

1. `V6.5 Reality Check`
2. `Information Age`
3. `Source Diversity`
4. `WP Check`
5. `Unique Value`

## Co jde do LLM

Jen shortlist:

- releasey
- commit změny s user-facing dopadem
- docs / changelog / release note změny
- issues s jasným dopadem na Android / Google služby / Pixel / Samsung / bezpečnost

Vše ostatní zůstává v raw signálech lokálně.

## Multi-source orchestrator

Pokud chceš jeden společný candidate universe nad všemi lokálními zdroji,
použij:

```bash
python3 magazines/android-magazine/monitoring/multi_source_orchestrator.py
```

Co čte:

- GitHub raw signály a watchlist z `monitoring/data/github_signals.db`
- GSC CSV exporty z `analytics/gsc/`
- GA4 CSV exporty z `analytics/ga4/`
- WordPress CSV exporty z `wordpress/`
- Google Trends cache z posledního editorial reportu

Poznámky:

- běh je read-only vůči GitHubu i ostatním remote API
- `Google News / News`, `Reddit`, `X`, `YouTube / community` a `AdSense` jsou v auditní sekci explicitně označené jako `NOT IMPLEMENTED`
- výstup ukládá markdown i JSON report do `reports/`
