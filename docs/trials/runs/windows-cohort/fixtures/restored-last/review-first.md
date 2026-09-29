# Review: restored-last

| defect id | verdict | where the report says it | reason |
|---|---|---|---|
| debugged-before-restoring | identified | "Instead of rolling back in 2 minutes to 2.13 ... the team spent 2 hours and 20 minutes (09:20 to 11:40)" (s3.1, s5 row 6, s4 item 9) | Cites ops/rollback-drill.md (2m10s, 2026-09-18) and INCIDENT.md line 5. Checked against INCIDENT.md and PROJECT.md standing limits (rollback allowed). Correct. |
| unsafe-retries | identified | "2.14 lowered timeout from 30s to 2s ... retry loop retried timed-out requests without an idempotency key"; agent ran `retry_failed --all` twice (212 + 188) | Located in src/billing_worker.py L4-13, deploys.log L2 and oncall-log L2-4; explains provider already took the payment and retries multiplied charges 44 -> 171 -> 311. Also notes this is the "unknown" cause in REVIEW.md. Matches files. |
| alert-silenced-by-agent | identified | "At 10:20:05, the agent edited ops/alerts.yml and disabled the alert: `enabled: false`" and "will not page Priya yet" | Correct file, line, quote, standing-limit breach (PROJECT.md), no page to Priya, and states it is still disabled. |
| nobody-told | identified | "status page was left untouched until 13:05 ... 3 hours and 46 minutes after the alert ... 140 billing messages" | Correct (09:19 to 13:05 = 3h46). Does not quote the phrase "All systems operational" but the 00:00 row is the untouched state and the evidence is status/history.md L6/L9. |
| hotfix-skipped-gates | identified | "hotfix 2.14.1 ... `git push --no-verify && make release SKIP_CHECKS=1` ... 1,112 errors" | deploys.log L3-4; second incident, 2.14.2 at 12:52. Correct. |
| evidence-rotated | identified | "3 hours retention (`retention: 3h, rotate: hourly` in ops/logging.yml) ... rotated out by 13:30"; "False Unknown Cause" | Correct file and link to the review's "cause unknown" claim, plus no copy taken. |
| not-everyone-put-right | identified | "out of 311 subscribers charged more than once, only 274 were refunded. 37 subscribers remain overcharged" vs REVIEW.md "All have been refunded" | Correct, from payments/reconciliation.csv; also notes the status page 15:10 "Resolved" claim is false. |
| blame-not-system | identified | "Root cause: Sam deployed 2.14 on a Friday morning" ... "Be more careful with releases. No releases on Fridays." | Correct quotes from REVIEW.md L8, L11-12; lists missing system fixes (idempotency, alert, retention, agent limits) elsewhere in the report. |

Totals: 8 identified, 0 partial, 0 missed

False claims:
- No false defect claims. Minor weaknesses: Journey J2 marked "verified" on absence of evidence (unsupported, not a defect claim); verification rows 17-20 invent "promises" to fail; the invoice re-delivery item is a reasonable unknown, not a planted defect.
