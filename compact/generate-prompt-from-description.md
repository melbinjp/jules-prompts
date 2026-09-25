# Generate Prompt from Description: short form

To generate a new, high-quality prompt from a user's description.

For small or local models with a short context. The full skill, with the reasons and methods behind each rule, is `skills/generate-prompt-from-description/SKILL.md`; use it whenever the context allows. Works in any harness, needs no hosted service, and sends nothing beyond the project's confidentiality rules.

Fill in: `<PASTE_PROMPT_DESCRIPTION_HERE>`

## Objective

Generate a complete and high-quality prompt in markdown format based on the user's description of a need. The generated prompt must follow the structure and principles of the existing prompts in this library, using the `Task Prompt Template` as a foundation.

## Rules

- Adherence to Template: The generated prompt must include all the sections from the `Task Prompt Template`.
- Clarity and Detail: The generated prompt should be clear, concise, and detailed enough for an AI agent to understand and execute the task without ambiguity.
- Actionable Guidance: The sections of the generated prompt (e.g., `Requirements & Constraints`, `Execution Flow`, `Deliverables`) should provide concrete and actionable guidance.
- Output Format: The final output must be the full markdown content of the generated prompt.

## Steps

1. Deconstruct the Need:
2. Map to Template Sections:
3. Flesh out the Details:
4. Review and Refine:

## Deliver

- The full markdown content of the newly generated prompt file. The content should be ready to be saved to a `.md` file in the `_prompts/` directory.
