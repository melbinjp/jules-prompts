# Update Dependencies: short form

To update a project's dependencies to their latest compatible versions.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/update-dependencies/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Update the dependencies of this repository to their latest compatible versions while ensuring that all tests pass and the project remains stable.

## Rules

- No Breaking Changes: You must not introduce any breaking changes to the project's functionality.
- Tests Must Pass: All existing tests must pass after the dependency update.
- Application Stability: You must verify that the application or library builds and runs correctly after the update.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A pull request with updated dependency files (`package.json`, `package-lock.json`, etc.).
- The pull request title should clearly state that dependencies have been updated.
- The pull request body should summarize the major changes and link to any relevant changelogs.
