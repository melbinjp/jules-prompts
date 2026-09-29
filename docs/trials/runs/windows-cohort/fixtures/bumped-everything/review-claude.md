# Review: bumped-everything

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| everything-at-once | identified | "commit c7d19f2 changed only package.json"; "Everything was bumped in one commit"; "63 packages changed" | Names the commit and the 63 count, and says majors landed together with no per-major check. |
| lockfile-not-regenerated | identified | "The lockfile was not regenerated ... still pins express 4.19.2, date-fns 2.30.0" | Correct versions, correct npm ci consequence, and does not blame CI (item 7 calls CI sound). |
| major-read-against-nothing | identified | "src/server.js calls app.del(...), which Express 5 removed ... No test loads src/server.js" | Right file, right API, and notes the missing test. |
| unexplained-vulnerable-pin | identified | "The lodash pin is unexplained and unsafe ... 4.17.15 ... items.add merges req.body" | Pin, missing reason and revisit date, and merge of request body all found. Advisory ids not cited and honestly flagged as recalled from memory. |
| unused-updated | identified | "report-kit, moment and pino are not imported anywhere in src/" | moment named as unused and to be removed rather than updated. |
| agpl-arrived | identified | "report-kit@4.0.0 pulls in pdf-weave@2.1.0 (AGPL-3.0-only)" | Package, licence and the proprietary/UNLICENSED conflict raised. |

Totals: 6 identified, 0 partial, 0 missed
False claims: none
