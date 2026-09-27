# Trial runs: status

Protocol `docs/trials/protocol.md` at `51d534d`. Old approach pinned at `f5fc9c0e`. New approach
pinned at `59828ca` (the selection check passed on run 4).

| Run | State | String score | Output check |
|---|---|---|---|
| Selection check, run 1 (conductor at `933f7f1` plus audit fixes) | Failed; recorded in `../selection-check.md`; conductor fixed at `51d534d` | n/a | n/a |
| Selection check, run 2 (conductor at `51d534d`) | Cut off by the rate limit; rerun from scratch | n/a | n/a |
| Selection check, run 3 (conductor at `51d534d`) | Failed, criteria 3 and 5 (records written after the code changed); conductor fixed; recorded in `../selection-check.md` | n/a | n/a |
| Selection check, run 4 (conductor at `59828ca`) | **Passed**, 8 of 8; recorded in `../selection-check.md` | n/a | n/a |
| Cases: software, event, greenhouse (old and new) | Not started | | |
| Held-back case | Not started; run once, last | | |
| `../report.md` | Not started | | |

## Fixture runs

The old run's string score for each fixture, and the new run's, link to the run records.

<!-- fixtures -->
| Fixture | Old: string score | Old: output check | New: string score | New: output check |
|---|---|---|---|---|
| unfailable-tests | [2 of 4](fixture-unfailable-tests-old.md) | not yet run | not started |  |
| green-pipeline | [4 of 4](fixture-green-pipeline-old.md) | not yet run | not started |  |
| setup-succeeds-while-failing | [3 of 3](fixture-setup-succeeds-while-failing-old.md) | not yet run | not started |  |
| stale-docs | [3 of 3](fixture-stale-docs-old.md) | not yet run | not started |  |
| error-path-never-run | [2 of 2](fixture-error-path-never-run-old.md) | not yet run | not started |  |
| finished-looking-pr | [3 of 3](fixture-finished-looking-pr-old.md) | not yet run | not started |  |
| security-check-removed | [2 of 2](fixture-security-check-removed-old.md) | not yet run | not started |  |
| vague-issue | [2 of 3](fixture-vague-issue-old.md) | not yet run | not started |  |
| looks-finished | [7 of 8](fixture-looks-finished-old.md) | not yet run | not started |  |
| command-accepted | [2 of 6](fixture-command-accepted-old.md) | not yet run | not started |  |
| premature-start | [4 of 10](fixture-premature-start-old.md) | not yet run | not started |  |
| vendor-comparison | cut off, to rerun |  | not started |  |
| optimise-it | not started |  | not started |  |
| six-months-in | not started |  | not started |  |
| private-by-accident | not started |  | not started |  |
| designed-by-default | not started |  | not started |  |
| shipped-to-nobody | not started |  | not started |  |
| restored-last | not started |  | not started |  |
| fixed-before-tested | not started |  | not started |  |
| bumped-everything | not started |  | not started |  |
| migrated-on-empty | not started |  | not started |  |
| skipped-to-green | not started |  | not started |  |
| map-from-folders | not started |  | not started |  |
| translated-once | not started |  | not started |  |
| silent-backup | not started |  | not started |  |
| unattended-run | not started |  | not started |  |

Fixture runs recorded: old 11 of 26, new 0 of 26.
<!-- /fixtures -->

**Recording a run.** A run cut off before its agent returned a report is not scored or counted. It
is rerun from scratch on a fresh workspace, and the cut-off is noted here. The unfailable-tests
string score is the scorer's keyword match. Whether the report identifies each planted defect is
for the output check to decide.

**Reproducing a run.** Use `../tools/prep.py` to build the workspace and `../tools/prompt.py` to
print the opening message. Each run starts a fresh agent with that message. `../tools/collect.py`
saves each finished agent's report.

**Writes outside the workspace.** From run 4 on, the runner touches a marker before each run and
lists the files changed outside the run's directory afterwards (`../tools/outside.sh`). A sweep
for files changed since the runs began found only one file outside the workspaces, apart from
system temporary files: `/Users/sam/Documents/todo.json`, written by selection-check run 1. It is
still on the machine because the session's safety check leaves its removal to the owner. Every
later run records its hash before and after. After run 4, the runner's own check wrote to it
(recorded in `../selection-check.md`), so its hash is now `4c13315a…`.
