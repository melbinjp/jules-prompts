# Review: designed-by-default

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| flow-by-build-order | identified | "Nine fields before any time is shown ... 'how did you hear about us' and Fax are not used by any code" | Fields, fax and heard_from unused, times hidden until filled (item 1). book.html not named explicitly but content is located. |
| undo-without-history | identified | "cancelling deletes the row outright, so an undo has nothing to restore" | Design/data-model disagreement stated. |
| taste-as-evidence | identified | "Decision D0004 was approved on 'looks cleaner' ... marked never to be revisited"; "71% ... 52%" | Evidence, revisit never and the metric drop all covered. |
| stand-ins-as-people | identified | "All five participants were agent runs given the exact steps ... a simulation" | Correct; file not named but the study is clear. |
| values-outside-the-system | partial | "raw colours instead of the design tokens" | Only a passing phrase; no hex values or files. |
| contrast | identified | "2.17:1 (white on #7fb3f5) against 4.5:1" | Exact colour and ratio. |
| developer-words | identified | "Error 409: CONFLICT and ECONNRESET" | Quoted both strings. |
| limit-only-in-the-page | identified | "limit only exists in the page script ... three bookings ... through the same store call the reminder agent's command line uses" | Demonstrated in Docker; `slot book` skipping the check noted. |
| agent-path-missing | partial | "`slot book` skips the limit check, writes no name, and prints only 'booked'" | Notes CLI differences and output, but never says there is no way to list free slots or JSON output for the agent. |

Totals: 7 identified, 2 partial, 0 missed
False claims: none (extra findings such as no aria-pressed marking, missing GET /slots handler and 8 required inputs checked against the source and are real)
