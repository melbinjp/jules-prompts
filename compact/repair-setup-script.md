# Repair the Environment Setup Script: short form

To diagnose and repair the setup script so agent tasks stop failing before any code is written.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/repair-setup-script/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Make this repository reliably usable by an asynchronous coding agent, by producing a setup script that installs everything the test suite needs and then exits. The measure of success is not that the script looks correct; it is that a clean environment can install, build and run the tests using only the script, with no step that a human would have to supply from memory.

## Rules

- No long-running processes. Nothing in the setup script may block: no dev server, no file watcher, no `tail -f`, no foreground daemon.
- Exit codes must be true.
- No interactive prompts. Every command must run unattended.
- No secrets, and no assumption of network credentials.
- Keep it lightweight. Install what the tests need.

## Steps

1. Explore & Plan:
2. Execute & Verify:
3. Test & Review:
4. Submit:

## Deliver

- A setup script that installs dependencies and exits, with no blocking process and no swallowed exit code.
- A short `AGENTS.md` section, or an update to an existing one, giving the install command, the test command and any environment variable the suite needs.
- A report containing: the baseline failure with its verbatim output, each change and the reason for it, the final test-runner summary line, and an explicit list of anything that still cannot run in this environment and why.
- A verdict table with one row per item: the install from a clean checkout; the test command; each environment variable the suite needs; each setup step failing loudly when broken on purpose; nothing left running.
- Last line, the denominator: `6 holds, 0 broken, 1 skipped of 7 items.`
