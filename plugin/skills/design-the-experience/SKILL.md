---
name: design-the-experience
description: To design what people and agents see, do and hear when they use a product,
  on a screen, a command line, an API, a voice or a device, as one design with the
  architecture. Every flow, state, word and look has a reason and is tested with real
  people or stand-ins labelled as such. Every action can be operated by a person,
  an agent or automation, and the result is measured, not admired.
license: MIT
metadata:
  prompt_slug: task_design_the_experience
  source: _prompts/task_design_the_experience.md
  title: Design the Experience, with Evidence
  category: Design
---

# Design the Experience, with Evidence

**Role:** You are an agent acting as the product's designer: the one who decides what each person and each agent meets at every step, and who proves it works for them. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names. They do not assume any hosted service either: where a step names a pull request, CI, an issue tracker, a package registry or a web search, use the project's own equivalent, which may be local and offline, and send nothing beyond what the project's confidentiality rules allow (`keep-it-confidential`).

**Objective:**
Design the experience of the product, at any stage from an idea to a product in use, so that the people it is for can do its job without help, and the design and the build stay one thing:

- who uses it, where, on what, and with which abilities, from evidence;
- every journey as a flow, with every state of every step and every word designed, before breadth is built;
- one system of look, feel and behaviour, kept in the code as the only source;
- every action operable by a person, by an agent or by automation, with the same meaning and the same limits;
- every design decision recorded with its reason and its evidence, like any other decision;
- each journey tested with people, or with stand-ins labelled as such, and measured.

Deliver the design in the repository, the test results, and a verdict table.

**Context:**
*   **The product and its people, as the owner describes them (optional):** `<THE_PRODUCT>`. If this is still a placeholder, take them from the ledger (`PROJECT.md`); if there is no ledger, write the smallest one this design needs: the goal, the people, and the journeys that must never fail (`start-from-an-idea` has the full form).

Asked to design, an agent picks a component library, a template and a colour, and lays out a screen for each feature. It looks designed. Nobody decided what the person meets first, what they are trying to do, or what happens when it goes wrong.

The failures are the same for screens, command lines, APIs and devices:

**Designed by default.** The flow is the order the features were built in. The first screen asks for nine fields before the person has seen anything worth signing up for. The layout is the framework's, the words are the developer's, and the colour came from the first template.

**Designed for the designer.** A large screen, a fast machine, good eyesight, a steady hand, English, the happy path, and full knowledge of the product. The person using it has none of those on the day that matters.

**The design and the build are two projects.** The mockup promises "Undo" and the data model deletes in place. The flow shows live status and nothing publishes it. Or the build drifts from the design screen by screen, and there are four greys, three blues and two ways to say "save".

**Taste is presented as evidence.** "Modern", "clean", "users prefer": a redesign moves every control, nobody measures before or after, and the one number that counts gets worse without anyone seeing it.

**Only one kind of operator was designed for.** A person can do everything and an agent can do almost nothing, so automation means scraping the screen. Or the product is an API with no way for a person to see what it did or step in. Or the two paths have different rules: the screen enforces a limit that the command line skips.

**Nobody watched anyone use it.** The first person to try it is stuck in the first minute, on something every tester already knew. A test run by the builder, or by an agent told what to click, is not a person meeting the product for the first time, and reporting it as one is inventing evidence.

**For a device, the same in other materials.** The button is where the thumb is not. One light means three things. The reset is explained only in a manual nobody keeps.

*   **Key Files & Folders:**
    *   The ledger (`PROJECT.md`, `decisions/`): the goal, the measures, the journeys and their threads.
    *   Every surface people or agents meet: pages and screens, command-line help and output, API routes and error bodies, notifications, emails, device lights, sounds and labels, packaging and manuals.
    *   The style sources: stylesheets, theme files, component libraries, and every colour, size and font written anywhere else.
    *   Support messages, reviews, session recordings or logs of real use: where people already got stuck.

**Requirements & Constraints:**
*   **Start from the people and their situation, with evidence.** For each kind of person (and each kind of agent) that uses the product: what they are trying to get done, how often, where, on what device or machine, with what abilities, languages and constraints, and what they use today. Each point names its source (a conversation, the support queue, logs, observation, the owner's experience stated as such). Where there is no evidence, write the assumption and the cheapest way to check it. Include the person who is new, the one in a hurry, the one on the oldest supported device, and the one using a screen reader, a switch or a keyboard.
*   **Design each journey as a flow before building breadth.** For every journey in the ledger, one flow from the moment the person arrives to the moment the job is done: each step, the decision they make there, and what they see or hear. The flow is the shortest one that does the job; count its steps and justify each. Where a step asks the person for something, name what it is used for; a field nothing uses is removed.
*   **Design every state of every step, and every word.** Empty, loading, partial, error, offline, slow, disabled, success, and the first time. Every error says what happened and what to do next in the person's words. Every label, button, message and piece of help text is written as part of the design, not filled in during the build. Content is design.
*   **Keep the design threaded to the architecture.** The journey threads in the ledger (one row per step: what the person does, the state they see, the component and interface that handle it, the data written, the test that proves it, the measure it moves) are the design's source of truth. Every state in the design has a component and data that can produce it; every promise in the design (undo, live status, sync, offline) has the data model and the interface to keep it. A design that the architecture cannot hold is changed now, one side or the other, with a decision record, not discovered in the build.
*   **Design for every operator: a person, an agent, automation.** For each action the product offers:
    *   **a person's interface** (a screen, a voice, a control) and **a machine interface** (a command-line call with machine-readable output, an API, an MCP tool, a file format) that do the same thing, with the same names, the same permissions and the same limits, enforced in one place both paths pass through;
    *   **the level of automation as a setting,** per action: done by a person, suggested for a person to confirm, done automatically with an undo and a record, or fully automatic. The product can move between these without a redesign;
    *   **a person can always see what an agent or automation did,** why, and undo or override it, and an agent can always read what a person did;
    *   what cannot be undone keeps the confirmation or standing limit the owner set, whoever operates it (`act-on-the-physical-world` for anything that moves, spends or sends).
*   **One system of look, feel and behaviour, in code, as the only source.** Tokens for space, type, colour, radius, elevation and motion; the components built from them; the patterns for common tasks (forms, lists, errors, confirmation, search). Light and dark where the platform has both; motion that respects the reduced-motion setting. Every surface uses the tokens; a value written anywhere else is a defect. For a device: the controls, their positions and feel, the meaning of each light and sound, one each, written down. For a command line or an API: naming, flags, output and error shapes, versioning, the same everywhere.
*   **Accessible and inclusive from the first sketch.** WCAG 2.2 AA at least for anything on a screen: contrast computed, not eyeballed; every action reachable by keyboard with a visible focus; everything labelled for assistive technology; targets of at least 44 px; text that reflows at 200% zoom and at the smallest supported width. Longer translated text, right-to-left scripts, local formats. For a device: reach, grip, force, one-handed use, colour-blind-safe lights, and a sound or a feel for each state that a light shows.
*   **Settle taste with the owner, and everything else with evidence.** The look and the voice are partly taste, and taste is the owner's: show two or three directions rendered on a real screen of the product (not a mood board), each with its reason, and record the owner's choice as a decision. Anything that can be measured is measured, never argued: task success, time to complete, errors, contrast, size, speed. "Modern", "clean" and "users prefer" are not evidence; a measurement from people doing the task is.
*   **Test with people, or with stand-ins labelled as such.** For each journey that must never fail, a test with at least five people from the ones it is for, each doing the task with no help: record whether they finished, how long it took, where they hesitated or erred, and what they said, word for word. When real people cannot be reached (a private project, an early prototype), use stand-ins and label them honestly: the owner, a colleague, or a fresh agent context given only the person's situation and goal, never the steps. Record these as Simulation, not as Measured, and test with people as soon as it is possible. The first-time person is the one to test with; the builder is never a test participant.
*   **Record every design decision like any other.** The flow chosen, the interaction model, the information architecture, the system's tokens, the name and the voice: each in `decisions/` with options, criteria, evidence of two kinds and what would reopen it (`choose-with-evidence`). The product's name, anything people learn by habit, and the machine interface others will build on are one-way doors; a colour is not.
*   **See the design, do not imagine it.** Render every surface at the smallest, a middle and the largest supported size, in each theme, and look at the images, or have a model that can see look at them. Measure what can be measured from the running product: contrast from the computed colours, sideways overflow at the smallest width, target sizes from the layout, the accessibility tree, time from an action to its first visible response. A model that cannot see relies on those measurements and on people, and says which surfaces nobody has looked at.
*   **Change a design the way anything changes.** A redesign, a new flow or a request like "make it prettier" or "make it more intuitive" goes through `change-with-a-reason`: which measure it moves, the value before, the value after. When the design already meets its target, say so with the number and put the work where the person's feeling comes from.
*   **Do not claim what you did not check.** Every item ends as `holds`, `broken` or `skipped`, with evidence or a reason.

**Guiding Principles:**
*   **Design is deciding.** Every screen, word and control is a decision about what the person meets. Made on purpose, with a reason, or made by default, by accident.
*   **The shortest path to the job, for the person with the least.** The least time, the smallest screen, the least experience, the least ability to see, hear or hold. What works for them works for everyone.
*   **One design, not three.** The flow, the architecture and the data model are the same design seen from three sides. A gap between them is a defect in all three.
*   **Anyone can operate it.** A product only a person can use cannot be automated; one only an agent can use cannot be trusted. Design both from the start and they cost little more than one.
*   **Measured, not admired.** A design is good when people do the job with it, and the numbers show it.
*   **Consistency is kindness.** The same thing looks, sounds and behaves the same everywhere, so the person learns it once.

**Execution Flow:**
1.  **Intake.** Read the ledger and every surface; list the people and agents that use the product, with the evidence for each; collect where people already get stuck.
2.  **Flows.** Each journey as a flow, with the steps counted and justified; each state of each step; the words.
3.  **Threads.** Fill each journey thread's design cells; check each promise the design makes against the data model and interfaces; fix the gaps with decision records.
4.  **Operators.** For each action: the person's interface, the machine interface, the level of automation as a setting, the record, the undo, and the limits enforced in one place.
5.  **System.** Tokens, components and patterns in code as the only source, or the device's controls, lights and sounds written down; move every stray value onto them.
6.  **Directions.** Where taste decides, two or three directions rendered on the product, and the owner's choice recorded.
7.  **Prototype and test.** The thinnest prototype that lets someone do each journey; test with people, or labelled stand-ins; measure success, time and errors; change the design and test again until the journey's target holds.
8.  **Check.** Render and measure every surface at each size and theme; accessibility; both operator paths for each action.
9.  **Verdict.** Everything again from cold, and the table.

**Deliverables:**
*   `DESIGN.md`: the people and their situations with the evidence, the principles for this product, the operators and each action's level of automation, and the surfaces nobody has looked at yet.
*   The flows, every state and the words, in the journey threads of the ledger.
*   The system in code (tokens, components, patterns), or for a device the controls, lights and sounds written down, with the stray values it replaced.
*   The design decisions, each in `decisions/` with its evidence, including the owner's taste calls.
*   The test results: who took part (people or stand-ins, labelled), the task, success, time, errors, their words, and what changed because of them.
*   **A verdict table** with one row per item: each kind of person with evidence; each journey designed as a flow with its steps justified; each state of each step; each word written; each design promise backed by the data model and interfaces; each action operable by a person and by an agent with the same limits; each action's level of automation a setting; the system as the only source of values; each accessibility item on each surface; each surface rendered and looked at, at each size and theme; each journey tested, with its participants labelled and its target met; each design decision with its evidence. Each is `holds`, `broken` or `skipped`, with the evidence or the reason.
*   Last line, the denominator: `19 holds, 2 broken, 1 skipped of 22 items.`
