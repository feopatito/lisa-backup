# AndroidMagazine.eu — Data workspace

## Struktura
```
android-magazine/
├── analytics/
│   ├── gsc/          ← Google Search Console (historická data do 13.8.2026 + delta)
│   └── ga4/          ← Google Analytics 4 (historická data do 13.8.2026 + delta)
├── wordpress/        ← WP databáze (posty, autoři, kategorie, tagy)
├── reports/          ← Hotové reporty a editorial plány
└── tmp/              ← Pracovní soubory
```

## LOCAL-FIRST pravidlo
- Historická data (do 17.8.2026) čti vždy lokálně
- API volej POUZE pro nová data od 17.8.2026
- Po každém API volání uloži delta do příslušné složky

## API přístupy
- WordPress: https://androidmagazine.eu/wp-json/wp/v2/ (user: Lisa, env: WP_ANDROID_PASS)
- GSC: sc-domain:androidmagazine.eu (service account: ../../android-magazine-sa.json)
- GA4: Property 361709661 (service account: ../../android-magazine-sa.json)
- Trends: JustSerpAPI /google/trends/search?query= (env: JUSTSERPAPI_KEY)
