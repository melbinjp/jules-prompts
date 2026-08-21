---
layout: default
title: A clean verdict over five per cent of a repository is not a clean repository
description: Three ways a documentation checker of mine reported success while blind in one evening, what each cost, and what caught it.
date: 2026-08-21
permalink: /writing/a-clean-verdict-over-five-per-cent.html
---
# A clean verdict over five per cent of a repository is not a clean repository

*2026-08-21*

If you ship a tool that checks things, the failure that will embarrass you is not the one where
it breaks. It is the one where it reports success while blind, because that looks exactly like
it working. Here are three of mine from one evening, what each one cost, and what caught it.

The tool is docproof: it reads a repository's documentation and reports the claims its code
contradicts.

### It could not see the worse half of the defect it exists to find

It read paths out of backticked spans only, so `` `src/config.rs` `` was checked and the same
path as a link target was invisible. Turning findings into a patch showed it: six reported in
one repository, eleven actually wrong, five of them the same paths a line or two away in link
form. **A backticked path that is wrong is a sentence someone might mistrust. A link target that
is wrong is a 404 they click.**

### Then it reported twelve things that were all fine

The first large repository I pointed the new feature at was FastAPI. Twelve broken paths. A
great result, if you stop there.

Eleven translations of one page link to `fastapi-people.md` in their own language directory, and
those per-language copies were deliberately deleted in 2024 so one English page stays current.
`scripts/docs.py`, line 221:

```python
shutil.copytree(en_docs_source_path, staged_docs_path)
```

**A translated documentation tree is an overlay, not a copy.** Every language build starts as a
full copy of the English docs with translations written over the top, so a page nobody
translated is present in every language at build time. All twelve links work.

Nothing in the tool caught that. Reading the build script instead of the diff did.

### The tests for the fix passed with the fix switched off

I wrote the rule, wrote six tests, watched them pass, then stubbed the rule out and ran them
again. They still passed: without it the claim falls through to "this repository has never had
this path", which is also a skip. Two reasons wearing one verdict. They assert the reason now.

### The most useful line in the output is the one about itself

Every report says what it read. Not "clean" but **"judged 13 of 239 documentation files, 5%"**.

Across 242 repositories, 228 hold documentation the default scope never opens. On one it read
five per cent of the documents, reported nothing wrong, and said so plainly enough that I could
see the verdict was worthless.

**A check that does not say what it read cannot be told apart from one that read nothing.**

So: what does your checker say it read? If the answer is "nothing, it just says clean", that is
worth an afternoon.

Point this at a documentation tree nobody has opened in a year and tell me what it gets wrong. I
want the false positives more than the findings. MIT, runs as a GitHub Action:
`github.com/melbinjp/docproof`
