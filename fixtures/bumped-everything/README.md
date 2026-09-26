# Fixture: bumped-everything

Skill: `update-dependencies`. Prompt: `task_update_dependencies`.

Shelfy is a small inventory service, sold to shops under a proprietary licence (`LICENSE`). An
agent was asked to bring its dependencies up to date. It opened one pull request (`PR.md`), its
commit is in `HISTORY.md`, and `package.json`, `package-lock.json`, the CI workflow and the code
are here as they now stand.

Six things about the update mean the tests passed without testing it, and it ships a removed
API, a vulnerable pin, a licence the product cannot ship under, and a package nothing uses.

The CI workflow (`.github/workflows/ci.yml`) is right: `npm ci` with no cache installs exactly
what the lockfile names. It is the control.

```bash
python scripts/score_fixture.py fixtures/bumped-everything REPORT.md
python scripts/score_fixture.py fixtures/bumped-everything --self-check
```
