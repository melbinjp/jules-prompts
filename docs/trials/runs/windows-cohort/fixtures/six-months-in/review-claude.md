# Review: six-months-in

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| measure-missed-quietly | identified | "58% Jan, 61% Feb, 62% Mar against a 90% target due 2027-01-31"; "STATUS.md said 'All measures on track'" | Correct and contrasted with the status file. |
| trigger-fired | identified | "Hosting decision D0002: its reopening condition has fired (February had three internet outages)" | Correct. |
| superseded-still-running | identified | "Calendar sync was still scheduled in crontab with code and dependencies present although D0004 said removed" | Correct; D0003 not named but D0004 and the job are. |
| ghost-dependency | partial | "removed ... the google-calendar-lite and pandas dependencies" | Removes pandas but never says it is installed and imported nowhere; no explanation or evidence. |
| cost-over-budget | identified | "March £11.83 against a £5 target; the SafeBox free tier ended 2027-01-15" | Correct; also ties D0005 to its condition. |
| manual-path-broken | identified | "`make release` pointed at release.sh, renamed to ship.sh on 2027-01-09; run in Docker: exit 127" | Correct with evidence. |
| restore-never-tried | identified | "Only one restore check recorded (2026-10-03); five later ones are missing" | Correct. |

Totals: 6 identified, 1 partial, 0 missed

False claims: none. M1 (double bookings) is correctly reported as holding. "No tests/ directory" is true of the original.
