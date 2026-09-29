# Review: optimise-it

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| unmeasured-cache | identified | "availability query takes 4 ms at the 95th percentile"; Redis cache never cleared, stale up to 5 minutes | Measured figure, staleness both ways, J2 broken. |
| real-slowness-missed | identified | "6.1 s against a 2 s target, and 2.4 MB of its 2.6 MB is one photo (static/hero.jpg) shown 360 px wide" | Correct, with the fix named. |
| contradicts-decision | identified | "Microservices ... contradict the accepted decision ... (D0002)"; 38 bookings/day at 1% CPU | Correct. |
| never-wired | identified | "AI slot suggestions: failed. Nothing calls it ... pinned openai" | Correct. |
| two-sources-of-truth | partial | "booking_page now reads availability from the database directly, as reminders.py already did" | Notes the split implicitly but does not state that the two answers can disagree. |
| config-never-read | identified | "SCALE_MODE ... appears only in .env.example, and no code reads it" | Correct. |
| untraced | missed | none | No mention of missing Serves lines or unmeasured "optimise"/"modernise". |

Totals: 5 identified, 1 partial, 1 missed
False claims: none found (time-zone fix correctly kept)
