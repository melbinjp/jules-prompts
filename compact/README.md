# Short forms

One file per core skill, generated from `_prompts/` by `python scripts/emit.py`, and checked
byte for byte in CI like every other generated form. Do not edit them here.

Each keeps the objective, the lead sentence of every rule, the steps and the deliverables, and
drops the reasons and the methods: a few hundred words where the full skill runs to a few
thousand. They are for small local models whose context cannot hold a full skill next to the
code, which is the usual case on a private or offline project.

A short form is a checklist, not the whole method. Use the full skill (`skills/<name>/SKILL.md`)
whenever the context allows, and before trusting a model with either, run it on the skill's
fixture and score it:

```bash
python scripts/score_fixture.py fixtures/<fixture> path/to/REPORT.md
```
