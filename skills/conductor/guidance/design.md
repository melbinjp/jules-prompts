# Design: what people and agents see, hear and operate

Load whenever the output has anything people or agents meet: screens, a command line, an API,
notifications, a voice, a device's controls, lights and sounds, packaging, manuals, signage, a
venue's flow. Design is deciding; every screen, word and control is decided on purpose, with a
reason, or by default, by accident.

Asked to design, an agent picks a component library, a template and a colour, and lays out a
screen for each feature. It looks designed. Nobody decided what the person meets first, what they
are trying to do, or what happens when it goes wrong.

## What design covers

- **Who uses it, where, on what, with which abilities,** from evidence.
- **Every critical journey as a flow,** with every state of every step and every word designed,
  before breadth is built.
- **One system of look, feel and behaviour,** kept in the source as the only source.
- **Every action operable by a person, an agent or automation,** with the same meaning and limits.
- **Every design decision recorded** with its reason and evidence (`decisions.md`).
- **Each journey tested with people,** or with stand-ins labelled as such, and measured.
- **The design record** (where the project keeps documents): the people and their situations
  with the evidence, the principles for this product, the operators and each action's level of
  automation, and the surfaces nobody has looked at yet.

Gate for a critical journey: a flow with every state and word designed, operable by a person and
an agent with the same limits, threaded to the architecture with no empty cell, and tested with
people, or labelled stand-ins, until its target holds.

## People and their situation

- **Take the product and its people from the objective and records;** with none, write the
  smallest this design needs: the objective, the people, the critical journeys.
- **For each kind of person (and each kind of agent) that uses it:** what they are trying to get
  done, how often, where, on what device or machine, with what abilities, languages and
  constraints, and what they use today. Each point names its source (a conversation, the support
  queue, logs, observation, the owner's experience stated as such). Where there is no evidence,
  write the assumption and the cheapest way to check it.
- **Include the person who is new, the one in a hurry, the one on the oldest supported device, and
  the one using a screen reader, a switch or a keyboard.** Design for the person with the least
  time, the smallest screen, the least experience and the least ability to see, hear or hold;
  what works for them works for everyone. Designing for a large screen, a fast machine, good
  eyesight, a steady hand, English and full knowledge of the product is the default failure.
- **Read every surface people or agents already meet,** every style source (stylesheets, themes,
  component libraries, stray values), and where people already got stuck (support messages,
  reviews, recordings, logs).

## Flows, states and words

- **Design each critical journey as one flow** from the moment the person arrives to the moment
  the job is done: each step, the decision they make there, and what they see or hear.
- **The flow is the shortest one that does the job:** count its steps and justify each. Where a
  step asks for something, name what it is used for; a field nothing uses is removed. "Designed
  by default" puts nine fields before anything worth signing up for, and orders the flow by
  build order.
- **Design every state of every step:** empty, loading, partial, error, offline, slow, disabled,
  success, and the first time.
- **Write every word as part of the design:** every label, button, message and piece of help.
  Every error says what happened and what to do next, in the person's words, not the exception's
  ("That time was just taken. Here are the nearest free times.", not "Error 409: CONFLICT").
- **For a device, the same in other materials:** the button where the thumb is; one meaning per
  light; the reset explained on the device, not only in a manual nobody keeps.

## Threads to the architecture

- **The design and the build are one design seen from three sides:** the flow, the architecture
  and the data. A gap between them is a defect in all three.
- **Every state in the design has a component and data that can produce it; every promise the
  design makes (undo, live status, sync, offline) has the data model and the interface to keep
  it.** A mockup that promises "Undo" over a delete that removes the row in place is a broken
  design.
- **Fill each journey thread's design cells** (`product.md §Journeys and threads`): what the
  person does, the state they see, the component and interface, the data written. Check each
  promise against the data model and interfaces; a design the architecture cannot hold is changed
  now, one side or the other, with a decision record, not discovered in the build.

## Every operator

For each action the product offers:

- **a person's interface** (a screen, a voice, a control) **and a machine interface** (a
  command-line call with machine-readable output, an API, a tool for agents, a file format) that
  do the same thing, with the same names, the same permissions and the same limits, **enforced in
  one place both paths pass through** (a limit checked only in the page's script is bypassed by
  every other caller);
- **the level of automation as a setting,** per action: done by a person; suggested for a person
  to confirm; done automatically with an undo and a record; or fully automatic. The product moves
  between these without a redesign;
- **a person can always see what an agent or automation did,** why, and undo or override it; an
  agent can always read what a person did;
- **what cannot be undone keeps the confirmation or standing limit the owner set,** whoever
  operates it (`physical.md §Safety states and irreversible actions`).

A product only a person can use cannot be automated; one only an agent can use cannot be
trusted. Designed together from the start, both cost little more than one.

## One system of look and behaviour

- **Tokens** for space, type, colour, radius, elevation and motion; **components** built from
  them; **patterns** for common tasks (forms, lists, errors, confirmation, search). Light and dark
  where the platform has both; motion that respects the reduced-motion setting.
- **Every surface uses the tokens; a value written anywhere else is a defect.** Move every stray
  value onto them (four greys and three blues across the stylesheets is the usual finding).
- **For a device:** the controls, their positions and feel, and the meaning of each light and
  sound, one each, written down.
- **For a command line or an API:** naming, flags, output and error shapes, and versioning, the
  same everywhere.
- The same thing looks, sounds and behaves the same everywhere, so the person learns it once.

## Accessible and inclusive

- **WCAG 2.2 AA at least for anything on a screen:** contrast computed from the actual colours, not
  eyeballed (4.5:1 for text, 3:1 for large text and interface parts); every action reachable by
  keyboard with a visible focus; everything labelled for assistive technology; targets of at least
  44 by 44 CSS pixels; text that reflows at 200% zoom and at the smallest supported width with no
  sideways scrolling.
- **Other languages:** longer translated text, right-to-left scripts, local date, number and unit
  formats.
- **For a device:** reach, grip, force, one-handed use, colour-blind-safe lights, and a sound or a
  feel for every state a light shows.

## Taste and evidence

- **Taste is the owner's.** The look and the voice are partly taste: show two or three directions
  rendered on a real screen of the product (not a mood board), each with its reason, and record the
  owner's choice as a decision.
- **Everything that can be measured is measured, never argued:** task success, time to complete,
  errors, contrast, size, speed. "Modern", "clean" and "users prefer" are not evidence; a
  measurement from people doing the task is.
- **A redesign is a change** (`../SKILL.md §7. Changes`): which measure it moves, the value before,
  the value after. When the design already meets its target, say so with the number and put the
  work where the person's feeling comes from.

## Testing with people

- **For each critical journey, test with at least five people from those it is for,** each doing
  the task with no help. Record whether they finished, how long it took, where they hesitated or
  erred, and what they said, word for word. Change the design and test again until the journey's
  target holds.
- **When real people cannot be reached** (a private project, an early prototype), use stand-ins
  and label them honestly: the owner, a colleague, or a fresh agent context given only the person's
  situation and goal, never the steps. Record these as Simulation, not as Measured, and test with
  people as soon as it is possible.
- **The builder is never a participant,** and an agent told what to click is not a person meeting
  the product for the first time; reporting either as one is inventing evidence.

## Seeing the design

- **Render every surface at the smallest, a middle and the largest supported size, in each theme,
  and look at the images,** or have a model that can see look at them.
- **Measure what can be measured from the running product:** contrast from the computed colours,
  sideways overflow at the smallest width, target sizes from the layout, the accessibility tree,
  the time from an action to its first visible response (acknowledge within 100 ms).
- **A model that cannot see relies on those measurements and on people,** and says which surfaces
  nobody has looked at.
