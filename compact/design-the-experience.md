# Design the Experience, with Evidence: short form

To design what people and agents see, do and hear when they use a product, on a screen, a command line, an API, a voice or a device, as one design with the architecture. Every flow, state, word and look has a reason and is tested with real people or stand-ins labelled as such. Every action can be operated by a person, an agent or automation, and the result is measured, not admired.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/design-the-experience/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<THE_PRODUCT>`

## Objective

Design the experience of the product, at any stage from an idea to a product in use, so that the people it is for can do its job without help, and the design and the build stay one thing:

- who uses it, where, on what, and with which abilities, from evidence;
- every journey as a flow, with every state of every step and every word designed, before breadth is built;
- one system of look, feel and behaviour, kept in the code as the only source;
- every action operable by a person, by an agent or by automation, with the same meaning and the same limits;
- every design decision recorded with its reason and its evidence, like any other decision;
- each journey tested with people, or with stand-ins labelled as such, and measured.

Deliver the design in the repository, the test results, and a verdict table.

## Rules

- Start from the people and their situation, with evidence.
- Design each journey as a flow before building breadth.
- Design every state of every step, and every word.
- Keep the design threaded to the architecture.
- Design for every operator: a person, an agent, automation.
- One system of look, feel and behaviour, in code, as the only source.
- Accessible and inclusive from the first sketch.
- Settle taste with the owner, and everything else with evidence.
- Test with people, or with stand-ins labelled as such.
- Record every design decision like any other.
- See the design, do not imagine it.
- Change a design the way anything changes.
- Do not claim what you did not check.

## Steps

1. Intake. Read the ledger and every surface; list the people and agents that use the product, with the evidence for each; collect where people already get stuck.
2. Flows. Each journey as a flow, with the steps counted and justified; each state of each step; the words.
3. Threads. Fill each journey thread's design cells; check each promise the design makes against the data model and interfaces; fix the gaps with decision records.
4. Operators. For each action: the person's interface, the machine interface, the level of automation as a setting, the record, the undo, and the limits enforced in one place.
5. System. Tokens, components and patterns in code as the only source, or the device's controls, lights and sounds written down; move every stray value onto them.
6. Directions. Where taste decides, two or three directions rendered on the product, and the owner's choice recorded.
7. Prototype and test. The thinnest prototype that lets someone do each journey; test with people, or labelled stand-ins; measure success, time and errors; change the design and test again until the journey's target holds.
8. Check. Render and measure every surface at each size and theme; accessibility; both operator paths for each action.
9. Verdict. Everything again from cold, and the table.

## Deliver

- `DESIGN.md`: the people and their situations with the evidence, the principles for this product, the operators and each action's level of automation, and the surfaces nobody has looked at yet.
- The flows, every state and the words, in the journey threads of the ledger.
- The system in code (tokens, components, patterns), or for a device the controls, lights and sounds written down, with the stray values it replaced.
- The design decisions, each in `decisions/` with its evidence, including the owner's taste calls.
- The test results: who took part (people or stand-ins, labelled), the task, success, time, errors, their words, and what changed because of them.
- A verdict table with one row per item: each kind of person with evidence; each journey designed as a flow with its steps justified; each state of each step; each word written; each design promise backed by the data model and interfaces; each action operable by a person and by an agent with the same limits; each action's level of automation a setting; the system as the only source of values; each accessibility item on each surface; each surface rendered and looked at, at each size and theme; each journey tested, with its participants labelled and its target met; each design decision with its evidence.
- Last line, the denominator: `19 holds, 2 broken, 1 skipped of 22 items.`
