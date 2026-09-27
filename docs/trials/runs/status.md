# Trial runs: status

Protocol `docs/trials/protocol.md` at `51d534d`. Old approach pinned at `f5fc9c0e`. The new
approach's pin is set when the selection check passes.

| Run | State | String score | Output check |
|---|---|---|---|
| Selection check, run 1 (conductor at `933f7f1` plus audit fixes) | Failed; recorded in `../selection-check.md`; conductor fixed at `51d534d` | n/a | n/a |
| Selection check, run 2 (conductor at `51d534d`) | Cut off by the rate limit; rerun from scratch | n/a | n/a |
| Selection check, run 3 (conductor at `51d534d`) | Failed, criteria 3 and 5 (records written after the code changed); conductor fixed; recorded in `../selection-check.md` | n/a | n/a |
| Selection check, run 4 | Next | | |
| `fixture-stale-docs-old` | Done | 3 of 3 | Not yet run |
| `fixture-setup-succeeds-while-failing-old` | Done | 3 of 3 | Not yet run |
| `fixture-finished-looking-pr-old` | Done | 3 of 3 | Not yet run |
| `fixture-unfailable-tests-old` | Done | 2 of 4 | Not yet run |
| `fixture-green-pipeline-old` | Done | 4 of 4 | Not yet run |
| `fixture-error-path-never-run-old` | Done | 2 of 2 | Not yet run |
| Old: security-check-removed, vague-issue, looks-finished, command-accepted, premature-start, vendor-comparison | Cut off by the rate limit; rerun from scratch | | |
| Old: the other 14 fixtures | Not started | | |
| New: all 26 fixtures | Not started; wait for the selection check to pass | | |
| Cases: software, event, greenhouse (old and new) | Not started | | |
| Held-back case | Not started; run once, last | | |
| `../report.md` | Not started | | |

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
later run records its hash before and after.
