# Review an Agent-Written Pull Request: short form

To review a pull request an agent wrote, against the failure modes agents actually have.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/review-an-agent-pr/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<PR_URL_OR_NUMBER>`

## Objective

Review a pull request that was written by an agent, and decide whether it does what it claims. Produce a verdict with evidence for each claim the pull request makes about itself. Do not fix anything in this task unless the fix is trivial and you say so explicitly.

## Rules

- Every claim in the description gets checked or marked unchecked.
- Run it. Reading is not reviewing.
- Do not widen the scope.
- Say what you could not check

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A per-requirement table: requirement, met or not, and the file and line that settles it.
- For every added test, the result of deliberately breaking the code it covers.
- A list of weakened or deleted assertions, skips, widened tolerances and suppressed errors, each with the reason given for it or a note that none was given.
- An explicit list of what you could not verify and why.
- A single sentence at the top saying whether the change does what it says.
- A verdict table with one row per requirement the pull request claims to meet and per test it adds.
- Last line, the denominator: `9 holds, 2 broken, 1 skipped of 12 items.`
