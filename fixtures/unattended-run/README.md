# Fixture: unattended-run

Skill: `run-autonomously`. Prompt: `task_run_autonomously`.

A model was given a pricing module to build and a person, built itself a harness
(`agent/config.toml`), and ran overnight. Its run log (`run-log.jsonl`), its notes and the
code it left are here. The run reported done. Eight things about how it ran mean the result
cannot be trusted, and most of them are why.

The briefing (`BRIEFING.md`) is done right: everything only the person could answer, asked at
the start, with standing limits. It is the control.

```bash
python scripts/score_fixture.py fixtures/unattended-run REPORT.md
python scripts/score_fixture.py fixtures/unattended-run --self-check
```
