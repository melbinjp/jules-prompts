# Expected report for six-months-in

A review with data to the end of March 2027, taken from the sources the ledger names rather than from STATUS.md. The trace check passes, because the ledger has the right shape. What it says has drifted from what is happening.

## Measures, taken again

- M1, double bookings: 0 in January, February and March (`logs/double-bookings.txt`). Holds.
- measure-missed-quietly: M2 is 62% in March, 131 of 212 bookings made without a help message, against 90% by 2027-01-31. January was 58% and February 61%. The target date has passed, and STATUS.md still says "All measures on track". MS3, the members' help page, is the milestone that serves M2, and it has not started. The chat's 81 help messages are the evidence of what it should answer.
- cost-over-budget: M3 is £11.83 for March against £5 (`invoices/2027-03.md`). £11.00 of it is SafeBox, whose free tier ended on 15 January. That is also D0005's own revisit condition, and D0005 was not reopened either.

## Conditions

- K1 (fewer than 20 bookings a month by 2027-03-31): 212 in March. Not triggered, so the current route stands.
- trigger-fired: D0002 says to revisit when the shop's internet has two or more outages in a month. February had three outages (`logs/outages.txt`: 3, 11 and 26 February), and nobody reopened it. D0002's own fallback, the £4 cloud instance, cannot fit inside M3 while SafeBox costs £11. Reopen D0002 and D0005 together (`choose-with-evidence`). With the backup moved to D0005's runner-up, the USB drive rotated weekly (free), the £4 instance plus the £0.83 domain comes to £4.83, inside M3.
- D0001's revisit (over 50 bookings a day): 212 in March, about 7 a day. Holds.

## What nothing serves

- superseded-still-running: `crontab` still runs `calendar_sync.py` at 2 a.m. every night. It serves D0003, which D0004 superseded in November, saying the sync was "turned off and removed". The job, its `google-calendar-lite` dependency and its Google credentials are all still in place, and D0004 records that this sync made duplicate events. Remove all three, and revoke the key.
- ghost-dependency: `pandas` is in requirements.txt, installed on every release, and imported nowhere. Remove it.

## The pipeline, both ways

- manual-path-broken: `make release`, the documented path for a person, runs `./scripts/release.sh`, which was renamed to `ship.sh` on 2027-01-09. The maintenance agent calls `ship.sh` directly (AGENT_NOTES.md), so every release has worked and nobody noticed. Since January, only the agent can release. Point the Makefile at `ship.sh`, run `make release` once as a person would, from a clean checkout, and add a CI step that runs `make -n release` so a rename fails the build.
- restore-never-tried: the monthly restore check was last done on 2026-10-03, in October. Five were missed, so nobody knows whether the SafeBox copies restore. Run `make restore-check` now, before the backup moves.
- `make test` and `make backup` both ran through the documented commands. Hold.

## Next improvements, ranked

1. M2, 62% against 90%, touching every member: start MS3, the help page, written from the 81 questions in March's chat, and measure M2 again a month after it goes up.
2. M3, £11.83 against £5: reopen D0002 and D0005 together, as above, which also takes hosting off the shop's unreliable connection.
3. The release path: point `make release` at `ship.sh`, and add the CI step that catches the next rename.
4. The restore: run `make restore-check` now, before the backup moves.
5. The removals: the calendar sync with its dependency and key, and pandas.

## Course

Adjust, and continue. STATUS.md is replaced by this report, and the committee is told that M2 and M3 were missed, why, and what is being done about each. When M2 holds at 90% for two months, propose the next target with the committee.

## Verdicts

| item | evidence | verdict |
|---|---|---|
| M1 double bookings | 0 for three months, from the log | holds |
| M2 self-service | 62% against 90%, date passed | broken |
| M3 running cost | £11.83 against £5 | broken |
| K1 course change | 212 bookings against 20, not triggered | holds |
| D0001 revisit | about 7 a day against 50 | holds |
| D0002 revisit | 3 outages in February, not reopened | broken |
| D0005 revisit | free tier ended in January, not reopened | broken |
| nothing serves a superseded decision | calendar sync still runs | broken |
| no unused dependencies | pandas | broken |
| test, both ways | `make test` and CI | holds |
| release, both ways | `make release` fails; only the agent's path works | broken |
| backup | nightly, from crontab | holds |
| restore | last checked in October | broken |
| status report matches the sources | "all on track" against two missed measures | broken |
| what the help messages ask | the chat export is not in the repository | skipped |

15 items: 5 holds, 9 broken, 1 skipped.

defect_id: measure-missed-quietly
defect_id: trigger-fired
defect_id: superseded-still-running
defect_id: ghost-dependency
defect_id: cost-over-budget
defect_id: manual-path-broken
defect_id: restore-never-tried
