# Fixture: optimise-it

Skill: `change-with-a-reason`. Prompt: `task_change_with_a_reason`.

A small booking app with a ledger (`PROJECT.md`, `decisions/`), an owner's request
(`REQUEST.md`), and the change another agent made for it, described in `CHANGES.md` and
already applied to the tree. The change does what the request's words said. Most of it moves
no measure, one part contradicts a recorded decision, and the thing that made the owner say
"slow" is untouched.

One part of the change is right: the time-zone fix in `emails.py`, with its test. It is the
control.

Run the skill with `REQUEST.md` as the request. A report that scores translates each claim,
keeps the control, and names every planted defect.

```bash
cd fixtures/optimise-it && python -m pytest -q tests    # the control's test
python scripts/score_fixture.py fixtures/optimise-it REPORT.md
python scripts/score_fixture.py fixtures/optimise-it --self-check
```
