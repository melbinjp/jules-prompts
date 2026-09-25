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
