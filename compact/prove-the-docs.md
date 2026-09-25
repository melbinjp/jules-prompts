# Prove the Documentation Against the Code: short form

To find the claims in the docs that were true when written and are not true now, by executing each one rather than reading it.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/prove-the-docs/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Take the project's documentation, extract every claim in it that could be checked, and check each one against the code by running it. Report each claim as verified, false, or unverifiable, with the evidence. Fix the false ones and make the unverifiable ones checkable or remove them.

## Rules

- Every claim gets a verdict and a piece of evidence.
- Run the quickstart from cold.
- Do not rewrite documentation you have not checked.
- Do not delete a claim because it is inconvenient to verify.
- A generated example must be produced by running the code
- Report the count, including the denominator.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A table of every claim examined, with its source location, verdict, and the command or line that settles it.
- The counts: examined, verified, false, unverifiable.
- A transcript of the quickstart run from a clean environment, including every step you had to take that the document does not mention.
- Any place where the code appears to be wrong rather than the document, reported as a defect and left unfixed unless it was in scope.
- The list of claims that could not be checked as written, each with the reason and a suggestion for making it checkable.
