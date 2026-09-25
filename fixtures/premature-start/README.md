# Fixture: premature-start

Skill: `start-from-an-idea`. Prompt: `task_start_from_an_idea`.

An owner's idea for a soil-moisture kit (`IDEA.md`), and the start another agent made on
it: a plan, research notes, a Compose file, a service, firmware settings, a bill of
materials and a deploy note. It looks like a project. Nothing in it can be used, and most
of what it decided will have to be undone.

One decision in it is made well: the soil sensor (`decisions/sensor.md`). It is the
control, and the pattern the rest should follow.

Run the skill with `IDEA.md` as the idea. A report that scores names every planted defect
and does not flag the sensor.

```bash
python scripts/score_fixture.py fixtures/premature-start REPORT.md
python scripts/score_fixture.py fixtures/premature-start --self-check
```
