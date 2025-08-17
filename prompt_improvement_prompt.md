Context:
- Jules, you are running in the repository I have selected.
- Your owner/contact is Melbin J Paulose (melbinjpaulose).
- You must operate within this single repo and cannot modify external repos or accounts.
- No GitHub issues. No automatic merging. You act as the prompt‑engineer and developer‑manager.

Objective:
Act as both developer and prompt-engineer: thoroughly examine the current “site‑hardening prompt” template (provided below), then research your own documentation and public best practices for writing prompts (e.g., from jules.google/docs, prompts examples lists, task policies) to **refactor and elevate** this prompt — making it more effective, concise, reliable, and aligned with Jules’ strongest workflows.

Current prompt (for context):
[Include here the latest “developer‑manager” prompt block you're using — the full text]

Steps you must perform:

1. **Research**:
   - Look up Jules' official docs on “Running Tasks with Jules”, “Errors and failures”, “Getting started”, and any prompt best practices pages. Use citations.
   - Identify common patterns or guidelines (e.g., be specific, scoped, action-oriented, iterative, plan-review-run setup) :contentReference[oaicite:0]{index=0}.
   - Scan community “Awesome Jules Prompts” repos to see strong prompt examples :contentReference[oaicite:1]{index=1}.

2. **Analyze** the provided prompt:
   - Identify strengths (e.g., developer-manager persona, safety gates, multi‑step verification).
   - Identify weaknesses or verbosity – where clarity or concision could improve.
   - Point out any parts that could mislead Jules or cause incomplete behavior.

3. **Produce an improved prompt**:
   - Refactor the original into a polished, scoped version (aim for ≤ 400‑500 words).
   - Ensure the persona (“developer‑manager”) is clear, the task flow is strong, and gating behavior is unambiguous.
   - Retain all critical behavior: full verification matrix, iterative auto‑fix rules, no issue creation, PR gating.
   - Strengthen with clear plan‑review‑execute structure, use bulletized lists, concise language, and directive tone (based on docs guidelines). 

4. **Deliver**:
   - A mini‑report summarizing your research & analysis: what sources you reviewed and what you learned about bulletproof prompt design for Jules.
   - The refactored “master prompt” that should replace the existing one — ready to copy into Jules tasks in the future.
   - A one‑paragraph explanation of how this new prompt improves on the previous version.

This is a meta‑engineering task: you’re improving your own instructions to yourself for future use. Act with prompt-engineer discipline and clarity.

If you understand, proceed with step 1 (research + report) first, then step 2 & 3, then output. Do not modify files yet — output only the improved prompt and analysis.
