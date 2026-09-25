# Security Review of Agent-Written Code: short form

To review a change an agent wrote for the security defects agents specifically introduce.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/security-review-agent-code/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<PR_URL_OR_DIFF_RANGE>`

## Objective

Review a change written by an agent for security defects, and report each with the evidence that establishes it. This is not a general audit of the project. It targets the specific ways a change goes wrong when it was produced by something optimising for a green build.

## Rules

- Report, do not repair, unless a fix is one line and you say plainly that you made it.
- Every finding carries a file, a line and why it matters.
- Rate by what an attacker gains
- State what you did not examine.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A findings list ordered by impact: file, line, what an attacker gains, and the smallest change that closes it.
- For every check the change introduced, the result of deliberately making it find something, so a check that cannot fail is caught rather than counted.
- A table of new dependencies: name, version, resolved source, and the import it satisfies.
- Every credential-shaped string found, and whether it is live and whether it is in the history.
- An explicit list of what you did not examine and why.
