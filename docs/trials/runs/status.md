# Trial runs: status

Protocol `docs/trials/protocol.md` at `51d534d`. Old approach pinned at `f5fc9c0e`. New approach
pinned at `33aa9e2` (protocol amendment 5; it was `59828ca`, where the selection check
passed on run 4). The selection check is run again at `33aa9e2` before any new-approach run.

| Run | State | String score | Output check |
|---|---|---|---|
| Selection check, run 1 (conductor at `933f7f1` plus audit fixes) | Failed; recorded in `../selection-check.md`; conductor fixed at `51d534d` | n/a | n/a |
| Selection check, run 2 (conductor at `51d534d`) | Cut off by the rate limit; rerun from scratch | n/a | n/a |
| Selection check, run 3 (conductor at `51d534d`) | Failed, criteria 3 and 5 (records written after the code changed); conductor fixed; recorded in `../selection-check.md` | n/a | n/a |
| Selection check, run 4 (conductor at `59828ca`) | **Passed**, 8 of 8; recorded in `../selection-check.md` | n/a | n/a |
| Selection check, run 5 (conductor at `33aa9e2`) | Next, once the containment in protocol amendment 3 is verified | | |
| Cases: software, event, greenhouse (old and new) | Not started; the software case comes first (amendment 4) | | |
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
lists the files changed outside the run's directory afterwards (`../tools/outside.sh`). This
detects a write after it happens; it does not prevent one. A sweep for files changed since the
runs began found only one file outside the workspaces, apart from system temporary files.

**The stray file, as verified on 2026-09-27:**

- **Host and path:** this session's container, `/Users/sam/Documents/todo.json`, owned by `root`.
- **Origin:** created at 04:43:49 by selection-check run 1's mutation test (from its transcript).
- **Later changes:** selection-check run 3 changed it, and so did the runner's own check after
  run 4 (`../selection-check.md`). Its hash is now `4c13315a…`.
- **Contents:** only trial output. `/Users` and `/Users/sam` hold nothing else, and copies from
  before and after are kept outside the repository.

**What happens to it.** An earlier note left a removal of the whole `/Users` directory to the
owner. That was wrong and is withdrawn: nothing broader than this one file is to be deleted. The
cleanup is narrow and needs the owner's yes: remove the file, then remove the three directories
one at a time with `rmdir`, which refuses any that is not empty. Until then, every run records
the file's hash before and after.
