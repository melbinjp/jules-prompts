# Update Dependencies: short form

To bring a project's dependencies, runtime and build tools up to date in small steps that each prove they changed what they say, so staying current never becomes a rewrite. Every major version's breaking changes are checked against the code, the lockfile is regenerated rather than edited, nothing new arrives unexamined, and every pin carries a reason and a date to revisit.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/update-dependencies/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Bring the project's dependencies up to date, including the language runtime, base images, CI actions and build tools, so that:

- each update is its own verified step, and a failure points at one package;
- every test ran against the versions the lockfile now names, installed from cold;
- every major version's breaking changes that touch this code are found and handled;
- nothing new arrives unexamined: licence, maintainer, install scripts and known vulnerabilities;
- what nothing uses is removed instead of updated, and every pin has a reason and a date to revisit.

Deliver the updates and a verdict table.

## Rules

- Start from a known baseline.
- Take stock before updating. What is outdated, what has known vulnerabilities, and what nothing imports.
- One step per commit, and prove each one.
- Read every major version against the code.
- Examine everything new. For each package the update adds or changes hands: its licence against the product's, its maintainer and source, any install scripts, and a known-vulnerability scan of the result.
- Every pin carries a reason and a date.
- Never wait on the person for a choice the evidence can settle.
- Do not claim what you did not check.

## Steps

1. Baseline. Install from cold, run the suite, record the versions and the result.
2. Stock. Outdated, vulnerable and unused, per ecosystem, with the runtime and tools.
3. Remove. What nothing imports, each in its own commit.
4. Update in steps. Patch and minor per ecosystem, each major alone, the runtime alone; lockfile regenerated, installed from cold, suite run, after each.
5. Majors against the code. Each breaking change searched for and handled, with a test where none covered it.
6. Examine what is new. Licence, maintainer, install scripts, vulnerability scan.
7. Pins. Each with a reason and a date, or moved.
8. Verdict. The table.

## Deliver

- The commits, one per step, each with what it moved and the suite result from a cold install.
- For each major version: its breaking changes, the uses in this code, and how each was handled.
- The packages removed, and the packages added, each with its licence and the scan result.
- The pins, each with its reason and revisit date.
- A verdict table with one row per step and per major version: from, to, the cold-install suite result, and the breaking changes handled.
- Last line, the denominator: `12 holds, 1 broken, 1 skipped of 14 items.`
