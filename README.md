# Jules Prompts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/melbinjp/jules-prompts?style=social)](https://github.com/melbinjp/jules-prompts)

A curated library of pre-made, machine-readable task prompts that let Jules (or any agent) — and humans — turn intent into production-grade work.

## Getting Started

To learn about the prompts in this library and how to use them together, please see the [Jules Prompt Library Guide](PROMPTS_GUIDE.md).

## Environment Setup for Jules

To ensure Jules can work effectively with your repository, it's crucial to have a well-defined environment setup. This helps in cloning, installing dependencies, and running tests reliably. For a detailed guide on how to configure your repository for Jules, please see the [Environment Setup Guide](ENVIRONMENT_SETUP.md).

## How to Use

The prompts in this repository are designed to be used in two primary ways:

### For Humans (Copy-Paste)

If you are a human interacting with an AI agent, the simplest way to use a prompt is to:
1.  Navigate to the prompt file you want to use (e.g., [`task_audit_repo.md`](_prompts/task_audit_repo.md)).
2.  Copy the entire content of the file.
3.  Paste it into your agent's instruction input.

### For Agents (Programmatic Access)

AI agents can use the `prompts.json` file to discover and fetch prompts.

1.  **Discover:** Fetch and parse `prompts.json` to get a list of available prompts.
2.  **Select:** Choose a prompt based on its title and description.
3.  **Execute:** Fetch the content of the markdown file specified in the `path` field and use it as the master instruction.

## Contributing

Contributions to this prompt library are welcome! The goal is to create a set of high-quality, general-purpose prompts that act as a "guiding light" for agents and developers, encoding best practices for common software engineering tasks.

If you have an idea for a new prompt or an improvement to an existing one, please open an issue to discuss it.
