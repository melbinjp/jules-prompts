# Map the Architecture: short form

To describe how the system actually works, by deriving it from what runs and what imports what rather than from the folder names.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/map-the-architecture/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Produce a description of this system's real structure: its entry points, what calls what, where its genuine boundaries are, and where the complexity actually sits. Derive every part of it from the code and the history rather than from the layout, and say for each claim how you established it.

## Rules

- Find the entry points; do not guess them.
- Build the import graph from imports.
- Name the real boundaries, which are the ones that fail separately.
- Use co-change to find the modules.
- Say how you know, per claim.
- Do not draw a diagram the code does not support.
- Report what you could not establish.

## Steps

1. Entry points. Every way the system starts or is called, found by running or resolving, not by guessing.
2. Graphs. The import graph from the imports, the data each component reads and writes, and co-change from the history.
3. Boundaries. The parts that fail separately, and the coupling nobody intended.
4. Write it. Each claim with how it was established; what could not be established, named.
5. Check it predicts. Pick two recent changes from the history and see whether the map says where they landed and what they touched.
6. Verdict. The table.

## Deliver

- The map: entry points, components, boundaries, where state lives and who writes it, and the coupling nobody intended, each claim with how it was established.
- The counts behind it: imports in and out per module, commits per path, how many places construct the central objects.
- What could not be established statically (dynamic dispatch, reflection, plugins, configuration wiring), named.
- A verdict table with one row per claim in the map, and one for the prediction check.
- Last line, the denominator: `24 holds, 3 broken, 2 skipped of 29 items.`
