# Take a Project to Production Quality: short form

To take a project in any state, software or physical, to production quality. It does its one job dependably and securely on every platform its people use, loses and leaks nothing, feels finished, carries nothing it does not need, and every area that decides this, from security and privacy to operations, is checked rather than assumed.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/take-to-production/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<WHAT_IT_IS_FOR>`

## Objective

Bring the project to production quality from whatever state it is in: an idea, a prototype, something that works until it doesn't, or a mature system with gaps. Production quality here means four things, and you will check each rather than claim it:

1.  It does the one job it exists for, on every platform its people actually use.
2.  It never loses, corrupts or exposes what people trusted it with, whatever the environment or an attacker does.
3.  It feels finished to use: nothing rough, nothing unexplained, nothing unreachable.
4.  It carries nothing it does not need.

Deliver the changes, and a verdict table that shows each of those item by item.

## Rules

- Write the bar before changing anything.
- Walk every area, and say which ones do not apply.
- Fix in order of cost to the person.
- Scope by the job, not by a rule about features.
- Run every platform in the bar, for real.
- Cause the environment's failures on purpose.
- Hold a craft standard, and check it like any other requirement.
- Turn budgets into checks that fail.
- Hold a complexity budget. Every dependency, service, build step, abstraction layer and document must name what breaks without it.
- Make it operable. The running product can report its version.
- Prove each fix can fail.
- Do not claim what you did not check.

## Steps

1. Intake.
2. Write the bar. As above: short, specific, and in the repository.
3. Measure the gap. Walk every journey on every platform in the bar. Walk every area, and attempt every attack in the threat model. Cause every failure on the never-lost list. Check every surface against the craft standard. Measure every budget. List every dependency with what it costs. Record each finding with its level from 1 to 7.
4. Close the gap, highest level first. Small, reviewable commits, each with the test that proves it and the reason in its message. Re-walk the affected journeys after each one.
5. Lock it in. Budgets and platform runs in CI, tests that were seen to fail, and the bar updated to what now holds.
6. Verdict. Re-run everything from cold and fill in the verdict table. Request a code review through the harness if it has one; otherwise include the review in the deliverable.

## Deliver

- The bar, committed.
- The changes, as a pull request (or the harness equivalent) whose description lists each fix with its level and the evidence that it worked.
- A verdict table with one row per item in the bar: each journey on each platform, each area's items, each attempted attack, each never-lost item under each failure, each craft item, each budget.
- The areas and items that do not apply, each with its one-line reason, so a reader can tell a considered omission from a forgotten one.
- What was removed, and which additions were refused, each with its reason.
- Last line, the denominator: `31 holds, 2 broken, 5 skipped of 38 items.`
