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
