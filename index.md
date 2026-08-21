---
layout: default
body_class: "home"
---
# Jules Prompts

A curated library of pre-made, machine-readable prompts to help AI agents like Jules understand and execute software engineering tasks.

This site provides a collection of **Tasks** that you can use to guide an agent to perform a variety of development activities, from simple file refactoring to complex repository audits.

Browse the [Tasks](./tasks.html) to get started.

## Tools these prompts pair with

A prompt tells an agent what to do. These do part of the same work mechanically, so the agent
spends its judgement on the cases that need it.

- **[docproof](https://github.com/melbinjp/docproof)** reads a repository's documentation and
  reports the claims its code contradicts: paths that no longer exist, commands that are not
  there, versions that moved. It is the automated half of
  [Prove the docs](./prompts/task_prove_the_docs.html), and it runs as a GitHub Action. MIT.
- **[rigout](https://github.com/melbinjp/rigout)** is an MCP server that lets an authorised
  agent use a real machine: commands, files, Docker, persistent terminals. `pip install rigout`.

## Writing

Notes from actually running this kind of tooling now live at
**[log.wecanuseai.com](https://log.wecanuseai.com/)**, so this stays a prompt library and the
writing has somewhere of its own to accumulate. Most recently, why
[a clean verdict over five per cent of a repository](https://log.wecanuseai.com/p/a-clean-verdict-over-five-per-cent.html)
is not a clean repository.
