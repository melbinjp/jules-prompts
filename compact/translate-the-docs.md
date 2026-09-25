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
