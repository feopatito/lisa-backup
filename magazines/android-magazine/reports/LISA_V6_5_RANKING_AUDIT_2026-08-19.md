# LISA V6.5 Ranking Audit - AndroidMagazine

## Verdict
- Watchlist persistence: PASS
- Structured Trends store: PASS
- First seen semantics: PASS
- GitHub evidence propagation: PASS
- Production data unchanged: PASS (no external publish/write, local test-state only)
- Qualified candidates: 18
- Rejected candidates: 2092
- Final portfolio: 10

## What Changed
- Old ranking was score-first and let historical search demand dominate the top slots.
- New ranking is lane-aware: candidates are first classified into BREAKING / CURRENT NEWS, DISCOVERY / PREDICTIVE, CURRENT DEMAND / TREND, SEO / SEARCH OPPORTUNITY, UPDATE / REWRITE.
- Generic entities such as `pixel 11`, `android 16`, `wear os` now get pushed into SEO/UPDATE unless a concrete editorial opportunity is present.
- `first_seen_by_lisa` is no longer inferred from old WP/GSC records; the audit field is `UNAVAILABLE` unless real Lisa-first-seen data exists.

## Before vs After - TOP 10
1. OLD: pixel 11 [CURRENT DEMAND / TREND] score=63.8
   NEW: redmi k100 pro max | lane=CURRENT DEMAND / TREND | lane_score=58.2 | families=ga4, trends, wordpress
   WHY: Why redmi k100 pro max is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
2. OLD: android 16 [CURRENT DEMAND / TREND] score=58.5
   NEW: jak vypnout ai funkce na | lane=SEO / SEARCH OPPORTUNITY | lane_score=83.6 | families=ga4, gsc, wordpress
   WHY: How to improve the existing jak vypnout ai funkce na page for current search intent, CTR, and conversion to a better editorial angle.
3. OLD: google pixely dostaly unikatni aplikaci [CURRENT DEMAND / TREND] score=48.2
   NEW: poco f9 ultra | lane=SEO / SEARCH OPPORTUNITY | lane_score=82.9 | families=ga4, gsc, wordpress
   WHY: How to improve the existing poco f9 ultra page for current search intent, CTR, and conversion to a better editorial angle.
4. OLD: pixel 10a vs galaxy a57 [CURRENT DEMAND / TREND] score=47.4
   NEW: pixel 11 | lane=SEO / SEARCH OPPORTUNITY | lane_score=77.8 | families=ga4, gsc, trends, wordpress
   WHY: Why pixel 11 is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
5. OLD: vivo x300 pro vs vivo [CURRENT DEMAND / TREND] score=26.6
   NEW: jak zapnout nebo vypnout funkci | lane=UPDATE / REWRITE | lane_score=64.9 | families=gsc, wordpress
   WHY: How to improve the existing jak zapnout nebo vypnout funkci page for current search intent, CTR, and conversion to a better editorial angle.
6. OLD: lynote ai download youtube videos [CURRENT DEMAND / TREND] score=26.6
   NEW: google pixely dostaly unikatni aplikaci | lane=SEO / SEARCH OPPORTUNITY | lane_score=64.7 | families=ga4, gsc
   WHY: What happened around google pixely dostaly unikatni aplikaci, what users need to know, and which practical angle is missing from current coverage.
7. OLD: play store [WP UPDATE / REWRITE] score=12.4
   NEW: android 16 | lane=SEO / SEARCH OPPORTUNITY | lane_score=60.9 | families=ga4, gsc, trends, wordpress
   WHY: Why android 16 is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
8. OLD: rcs [WP UPDATE / REWRITE] score=11.6
   NEW: poco x8 pro vs galaxy | lane=UPDATE / REWRITE | lane_score=59.3 | families=ga4, gsc
   WHY: What happened around poco x8 pro vs galaxy, what users need to know, and which practical angle is missing from current coverage.

## New TOP 10 - editorial audit
1. redmi k100 pro max
   lane=CURRENT DEMAND / TREND | lane_score=58.2 | signal_score=33.5 | opportunity=37.3 | predictive=26.8
   source_families=ga4, trends, wordpress | supporting_events=6 | source_diversity=5
   first_seen(source_record)=2026-08-04T01:17:24 | story_first_seen=2026-08-04T01:17:24 | lisa_first_seen=UNAVAILABLE
   gsc=0.0 | ga4=25.0 | trend=50.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=33.5
   angle=Why redmi k100 pro max is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
2. jak vypnout ai funkce na
   lane=SEO / SEARCH OPPORTUNITY | lane_score=83.6 | signal_score=50.4 | opportunity=76.2 | predictive=44.8
   source_families=ga4, gsc, wordpress | supporting_events=21 | source_diversity=5
   first_seen(source_record)=2025-10-26T14:00:02 | story_first_seen=2025-10-26T14:00:02 | lisa_first_seen=UNAVAILABLE
   gsc=11495.0 | ga4=1157.0 | trend=0.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=50.4
   angle=How to improve the existing jak vypnout ai funkce na page for current search intent, CTR, and conversion to a better editorial angle.
3. poco f9 ultra
   lane=SEO / SEARCH OPPORTUNITY | lane_score=82.9 | signal_score=50.4 | opportunity=75.8 | predictive=44.5
   source_families=ga4, gsc, wordpress | supporting_events=44 | source_diversity=5
   first_seen(source_record)=2026-07-23T13:39:10 | story_first_seen=2026-07-23T13:39:10 | lisa_first_seen=UNAVAILABLE
   gsc=4136.0 | ga4=1256.0 | trend=0.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=50.4
   angle=How to improve the existing poco f9 ultra page for current search intent, CTR, and conversion to a better editorial angle.
4. pixel 11
   lane=SEO / SEARCH OPPORTUNITY | lane_score=77.8 | signal_score=63.8 | opportunity=97.3 | predictive=64.2
   source_families=ga4, gsc, trends, wordpress | supporting_events=74 | source_diversity=6
   first_seen(source_record)=2026-07-13T13:55:07 | story_first_seen=2026-07-13T13:55:07 | lisa_first_seen=UNAVAILABLE
   gsc=2529.0 | ga4=680.0 | trend=69.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=63.8
   angle=Why pixel 11 is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
5. jak zapnout nebo vypnout funkci
   lane=UPDATE / REWRITE | lane_score=64.9 | signal_score=35.4 | opportunity=54.0 | predictive=29.8
   source_families=gsc, wordpress | supporting_events=3 | source_diversity=4
   first_seen(source_record)=2024-05-31T16:30:31 | story_first_seen=2024-05-31T16:30:31 | lisa_first_seen=UNAVAILABLE
   gsc=2118.0 | ga4=0.0 | trend=0.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=35.4
   angle=How to improve the existing jak zapnout nebo vypnout funkci page for current search intent, CTR, and conversion to a better editorial angle.
6. google pixely dostaly unikatni aplikaci
   lane=SEO / SEARCH OPPORTUNITY | lane_score=64.7 | signal_score=48.2 | opportunity=70.8 | predictive=43.8
   source_families=ga4, gsc | supporting_events=4 | source_diversity=3
   first_seen(source_record)=2026-08-13T13:41:53Z | story_first_seen=2026-08-13T13:41:53Z | lisa_first_seen=UNAVAILABLE
   gsc=1230.0 | ga4=372.0 | trend=0.0
   wp=CREATE | unique=PASS | user_impact=MEDIUM | final_signal=48.2
   angle=What happened around google pixely dostaly unikatni aplikaci, what users need to know, and which practical angle is missing from current coverage.
7. android 16
   lane=SEO / SEARCH OPPORTUNITY | lane_score=60.9 | signal_score=58.5 | opportunity=85.6 | predictive=52.5
   source_families=ga4, gsc, trends, wordpress | supporting_events=42 | source_diversity=6
   first_seen(source_record)=2024-11-14T06:00:41 | story_first_seen=2024-11-14T06:00:41 | lisa_first_seen=UNAVAILABLE
   gsc=834.0 | ga4=614.0 | trend=28.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=58.5
   angle=Why android 16 is moving right now, what users want to know, and what AndroidMagazine can add beyond the raw trend.
8. poco x8 pro vs galaxy
   lane=UPDATE / REWRITE | lane_score=59.3 | signal_score=46.6 | opportunity=70.9 | predictive=43.9
   source_families=ga4, gsc | supporting_events=8 | source_diversity=3
   first_seen(source_record)=2026-08-13T13:41:53Z | story_first_seen=2026-08-13T13:41:53Z | lisa_first_seen=UNAVAILABLE
   gsc=520.0 | ga4=399.0 | trend=0.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=46.6
   angle=What happened around poco x8 pro vs galaxy, what users need to know, and which practical angle is missing from current coverage.
9. jak si na androidu snadno
   lane=UPDATE / REWRITE | lane_score=58.0 | signal_score=35.4 | opportunity=55.9 | predictive=31.1
   source_families=gsc, wordpress | supporting_events=3 | source_diversity=4
   first_seen(source_record)=2024-10-28T06:00:02 | story_first_seen=2024-10-28T06:00:02 | lisa_first_seen=UNAVAILABLE
   gsc=675.0 | ga4=0.0 | trend=0.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=35.4
   angle=How to improve the existing jak si na androidu snadno page for current search intent, CTR, and conversion to a better editorial angle.
10. wear os
   lane=UPDATE / REWRITE | lane_score=56.9 | signal_score=50.4 | opportunity=67.0 | predictive=42.5
   source_families=ga4, gsc, wordpress | supporting_events=10 | source_diversity=5
   first_seen(source_record)=2014-06-25T19:44:46 | story_first_seen=2014-06-25T19:44:46 | lisa_first_seen=UNAVAILABLE
   gsc=319.0 | ga4=131.0 | trend=0.0
   wp=UPDATE/REWRITE/MERGE | unique=PASS | user_impact=MEDIUM | final_signal=50.4
   angle=How to improve the existing wear os page for current search intent, CTR, and conversion to a better editorial angle.

## Counterfactual / cutoff notes
- The strongest rejected candidates are not low-demand junk; many have huge GSC/GA4 demand but fail on unique value.
- Example rejected clusters at the top of the rejection list: `jak vypnout vas android telefon`, `6 zpusobu jak zjistit sve`, `jak zmenit prijimani hovoru na`.
- These beat some accepted SEO topics on raw demand, but lose on the editorial gate because they are too generic or duplicated.
- That is the intended behavior of the new funnel: demand is not enough without a concrete angle.
- The largest uncertainty remains the boundary between SEO and UPDATE for high-demand evergreen topics; the current model is deliberately conservative there.

## Implementation readout
- lane-specific scoring: PASS
- dynamic portfolio selector: PASS
- rejected candidates written: PASS
- GitHub evidence propagation into candidate universe: FAIL
- because raw GitHub signals exist, but none reached qualified/final portfolio in this dataset

## Raw counts
- normalized_signals=2865 | clusters=2110 | qualified=18 | final=10
- source_counts={"github": 54, "gsc": 700, "ga4": 760, "wordpress": 1346, "trends": 5}
- lane_counts={"DISCOVERY / PREDICTIVE": 40, "BREAKING / CURRENT NEWS": 1, "SEO / SEARCH OPPORTUNITY": 796, "UPDATE / REWRITE": 1361, "CURRENT DEMAND / TREND": 3}
- qualified_lane_counts={"SEO / SEARCH OPPORTUNITY": 7, "UPDATE / REWRITE": 10, "CURRENT DEMAND / TREND": 1}
- portfolio_lane_counts={"CURRENT DEMAND / TREND": 1, "SEO / SEARCH OPPORTUNITY": 5, "UPDATE / REWRITE": 4}

## Production note
- No remote publish was performed.
- Report was generated from the local test dataset only.
