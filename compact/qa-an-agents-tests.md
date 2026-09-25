# QA the Tests an Agent Wrote: short form

To find the tests that pass because they were written from the implementation rather than from the requirement, and cannot fail.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/qa-an-agents-tests/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Audit a test suite an agent wrote, and find the tests that cannot fail. For every test added or changed by agent work, prove it fails when the behaviour it names is broken. Fix or delete the ones that do not, and report the count.

## Rules

- Prove each test can fail. Do not read it and decide.
- Revert every deliberate break. Mutate, observe, restore, and verify the suite is green again before moving on.
- A test that cannot fail is either fixed or deleted, never left.
- Do not raise coverage. This task lowers it when a useless test is removed, and that is the correct direction.
- Do not change the behaviour under test.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A table of every agent-authored test with the mutation used against it and whether it caught it.
- The list of tests deleted, each with the reason it could not be made meaningful.
- The before and after collected-test counts and the coverage change, with the direction stated rather than explained away.
- Any defect found because a test became meaningful and then failed, reported and left failing.
- A note of every skip added by agent work, with its stated reason and whether that reason still holds.
