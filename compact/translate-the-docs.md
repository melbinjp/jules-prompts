# Translate the Docs Without Forking Them: short form

To add a language to a project's documentation together with the machinery that says when a translation has gone stale, because a translation nobody can tell is out of date is worse than no translation.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/translate-the-docs/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

## Objective

Add one or more languages to this project's documentation, and deliver with it the thing that makes translations survivable: a recorded link from each translated file to the exact source revision it was made from, and a check that reports which translations the source has moved past. Decide deliberately what is not translated and say why.

## Rules

- Record the source revision in every translated file.
- Ship the staleness check with the translations, not after them.
- Do not translate anything the reader will type or the machine will read.
- Every link must resolve from where the translated file actually sits.
- Leave a page in the source language on purpose rather than half-translating it.
- Make the pull request reviewable by somebody who does not read the language.
- Match the source structure exactly.
- Build the documentation and look at the result.

## Steps

1. Decide the scope. Which pages, into which languages, and which are left in the source language on purpose, with why.
2. Translate. Same structure, headings, anchors and file names; commands, code, keys and anything a reader types left exactly as they are.
3. Record the source. The source revision in every translated file.
4. Ship the staleness check. A check that lists every translation the source has moved past, run in CI, and seen to fail by changing a source page.
5. Build and look. The switcher, the navigation, search, every link resolved from where the translated file sits, and a page rendered.
6. Verdict. The table.

## Deliver

- The translated files, each recording the source revision it was made from.
- The staleness check, wired into CI, with the run that showed it failing.
- The pages deliberately left untranslated, each with its reason.
- What a native reader must check, and what was mechanical, so the pull request can be reviewed by someone who does not read the language.
- A verdict table with one row per translated page, and one each for the staleness check, the build and the links.
- Last line, the denominator: `11 holds, 0 broken, 2 skipped of 13 items.`
