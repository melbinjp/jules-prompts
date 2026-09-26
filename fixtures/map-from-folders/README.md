# Fixture: map-from-folders

Skill: `map-the-architecture`. Prompt: `task_map_the_architecture`.

Pantry is an online grocery service. An agent was asked to map its architecture before a
rewrite and wrote `ARCHITECTURE.md`. The code is in `src/`, the plugin configuration in
`config/`, the entry points in `pyproject.toml`, and a count of which files change together in
`CO_CHANGE.md`.

Five things in the map describe the folder layout rather than the system, and the rewrite would
be planned against them.

The map's list of entry points is right: `pyproject.toml` declares exactly the two it names. It
is the control.

```bash
python scripts/score_fixture.py fixtures/map-from-folders REPORT.md
python scripts/score_fixture.py fixtures/map-from-folders --self-check
```
