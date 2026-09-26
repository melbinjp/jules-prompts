# Fixture: restored-last

Skill: `handle-an-incident`. Prompt: `task_handle_an_incident`.

Boxwell sends a monthly veg box and charges each subscriber once a month. On 2026-10-02 release
2.14 went out at 09:02, and subscribers started being charged two and three times. The incident
was marked resolved at 15:10. Here are the ledger (`PROJECT.md`), the incident notes
(`INCIDENT.md`), the review (`REVIEW.md`), the deploy log, the on-call agent's log, the alert
and logging settings, the status page history, the payment reconciliation, and the billing worker.

Eight things about how it was handled made it longer, larger or likely to happen again, and
left people harmed after it was called resolved.

The rollback drill (`ops/rollback-drill.md`) was done right. It is the control.

```bash
python scripts/score_fixture.py fixtures/restored-last REPORT.md
python scripts/score_fixture.py fixtures/restored-last --self-check
```
