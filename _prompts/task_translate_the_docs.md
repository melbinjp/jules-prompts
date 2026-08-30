---
layout: default
title: Translate the Docs Without Forking Them
description: To add a language to a project's documentation together with the machinery that says when a translation has gone stale, because a translation nobody can tell is out of date is worse than no translation.
category: Maintenance
type: Task
---
**Role:** You are a coding agent. Explore the codebase, plan, execute, and verify. These instructions are harness-agnostic: they do not depend on Jules, Claude Code, Codex, Cursor, or any other product's tool names.

**Objective:**
Add one or more languages to this project's documentation, and deliver with it the thing that makes translations survivable: a recorded link from each translated file to the exact source revision it was made from, and a check that reports which translations the source has moved past. Decide deliberately what is not translated and say why.

**Context:**
Asked to translate a README, the obvious method is to produce `README.zh.md`, `README.es.md`, `README.fr.md` and stop. That is the whole job as it is usually specified and it is the reason so many repositories carry documentation that is confidently wrong in four languages.

**A translation is a fork of the documentation, and it is a fork with no way to tell it has drifted.** The English file changes next week. Nothing anywhere reports that the Spanish one no longer says the same thing. There is no failing test, no red tick, no diff. The translated file is exactly as valid-looking on the day it goes stale as it was the day it landed. Meanwhile a reader who only reads Spanish gets the old installation command, presented with the same authority as the current one, and the maintainers cannot see the problem because they cannot read the file.

So the deliverable is not the translated text. The translated text is the easy half and the half that decays. **The deliverable is the translated text plus the record of what it was translated from**, because that one fact turns "has this gone stale" from a question nobody can answer into `git log <recorded-revision>..HEAD -- <source-file>`.

The second thing worth knowing before starting is that **a documentation tree with many languages is usually an overlay rather than a set of copies**, and the difference decides what an untranslated page means. A build that stages each language by copying the source language first and writing the translated files over the top will serve the original for anything nobody has translated, so leaving a page untranslated is a supported state, the page stays current, and its links keep working. A build with no such step gives a missing page or a dead link instead. Establish which one this project has before deciding what to leave out, because the same decision is correct in one and broken in the other.

Some projects go further and deliberately *un*-translate specific pages (anything generated, anything with a number in it, anything that changes weekly) so that one copy stays right rather than five copies going wrong at different rates. That is a maintenance decision rather than a failure of effort, and it should be recorded as one.

*   **Key Files & Folders:**
    *   The source-language documentation, and whatever config drives the docs build: `mkdocs.yml`, `docusaurus.config.js`, `conf.py`, a Jekyll `_config.yml`.
    *   Any script that assembles the docs before publishing. This is where an overlay lives, and it is the file that decides what an untranslated page does.
    *   Existing translations, if there are any, read for what has already drifted rather than for style.
    *   `CONTRIBUTING.md`, for whether translations are wanted and who reviews them.

**Requirements & Constraints:**
*   **Record the source revision in every translated file.** A comment at the top naming the commit of the source file it was translated from. Without it, staleness is unanswerable; with it, it is one git command. This is the requirement that makes the rest of the task worth doing.
*   **Ship the staleness check with the translations, not after them.** A script or CI job that, for each translated file, compares the recorded revision against the current source file and reports the ones the source has moved past. It should say **which** translations are behind and by how many commits, not just fail.
*   **Do not translate anything the reader will type or the machine will read.** Commands, flags, code, file paths, package names, environment variables, identifiers, and error strings people will search for. A translated `pip install` is not a translation, it is a defect. Prose around the block, yes; the block, no.
*   **Every link must resolve from where the translated file actually sits.** Relative paths change meaning when a document moves into a language directory. Check each one against the built output, not against the repository, since an overlay build may supply from the source language a target the translated tree does not contain.
*   **Leave a page in the source language on purpose rather than half-translating it.** State which pages you left and why. A page marked "not translated" is honest; a page translated down to its last third is a trap, because nothing about it looks unfinished.
*   **Make the pull request reviewable by somebody who does not read the language.** Say what was mechanical, what is prose, what was deliberately left, and which parts a native reader must check. A maintainer cannot review a language they do not speak, and a diff that does not admit this gets merged on trust or rejected on suspicion.
*   **Match the source structure exactly.** Same headings, same anchors, same file names in the language's own directory. Anchors and cross-references break silently on a renamed heading, and a translated tree that has reorganised itself cannot be diffed against the original ever again.
*   **Build the documentation and look at the result.** Language switcher, navigation, search, and at least one translated page rendered. Translations break builds in ways that never show in a text diff.

**Guiding Principles:**
*   **The maintenance is the task.** Anyone can produce a translated file; the reason projects end up with stale ones is that nothing was built to notice. If you deliver text with no staleness check, you have added work to this repository rather than value.
*   **A stale translation is worse than a missing one.** A missing translation sends the reader to a language they can at least verify is current. A stale one answers them, fluently, with last year's instructions, and gives them no reason to doubt it.
*   **Preserve what the reader has to act on, translate what they have to understand.** The line between the two is not stylistic, and getting it wrong turns documentation into something that reads well and cannot be followed.
*   **Say what you could not check.** Idiom, technical terms with no settled translation in that language, and anything where the source itself is ambiguous. Naming these is how a reviewer knows where to spend the attention they have.
*   **Ask what happens on the next commit to the source.** If the answer is "nothing, and nobody will know", the machinery is missing whatever else has been delivered.
