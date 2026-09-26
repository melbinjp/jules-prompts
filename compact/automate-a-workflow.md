# Automate a Workflow That Can Report Its Own Failure: short form

To replace a repeated manual sequence with a script whose main job is being able to tell you whether the work actually happened, because an automation that reports success while blind is worse than doing it by hand.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/automate-a-workflow/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Take a sequence somebody runs by hand in this project and turn it into a script that is safe to run twice, safe to interrupt, and unable to report success without having done the work. Establish what the sequence actually is by finding it in the history rather than by asking, and prove the script fails loudly by making it fail.

## Rules

- Find the workflow before automating it, and say how often it runs.
- Never put a check on the left of a pipe.
- Verify each step by its effect, not by its exit code.
- Make it safe to run twice.
- Write results as they are produced.
- Make it fail, and watch it fail.
- Say what it will not do.
- Make the log say what it READ.

## Steps

1. Find it. The commands people actually run, from the history, the CI logs and the docs; how often, and what a mistake costs.
2. Script it. Each step verified by its effect; no check on the left of a pipe; safe to run twice and to interrupt; results written as they are produced; a log that says what it read.
3. Break it. Remove a dependency, a permission, an input, and interrupt it halfway; watch each failure reach the exit code and the log.
4. Hand it over. The command, what it will not do, and where its log goes.
5. Verdict. The table.

## Deliver

- The script, and the one command that runs it.
- How often the workflow runs and what a mistake costs, with the source for each, so the automation's worth is on record.
- Each failure caused on purpose, and what the script reported for it.
- What the script will not do, in one sentence per case.
- A verdict table with one row per item: each step verified by its effect; each failure caused and reported; safe to run twice; safe to interrupt and resume; the log naming what it read.
- Last line, the denominator: `8 holds, 1 broken, 1 skipped of 10 items.`
