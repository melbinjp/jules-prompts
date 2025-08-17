### **Mini-Report: Research & Analysis**

**1. Research Summary**

My research into prompt engineering for AI agents, primarily using `promptingguide.ai`, revealed several key best practices. Effective prompts are:
*   **Simple and Iterative:** Start with a simple goal and add complexity, rather than starting with a highly complex prompt.
*   **Specific and Direct:** Clearly state the objective, constraints, and desired output format. Use direct commands (e.g., "Write," "Refactor").
*   **Structured:** Use headings, lists, and separators to create a clear hierarchy of information.
*   **Positively Framed:** Tell the agent what to *do* rather than what *not* to do (e.g., "Use the existing logging library" is better than "Don't use `console.log`").
*   **Agent-Aware:** Prompts should leverage an agent's core capabilities, such as planning, tool use, and reflection.

**2. Meta-Prompt Analysis**

The prompt you provided for this task was a strong example of good prompt design and served as an excellent foundation.
*   **Strengths:** It clearly defined a persona, a specific objective, context, and constraints. It used action-oriented verbs and broke the task into a logical, multi-step process, which aligns perfectly with my internal `plan-then-execute` workflow.
*   **Weaknesses:** The main weakness was the confusing and recursive reference to a non-existent "site-hardening prompt," which caused initial ambiguity. It was also slightly verbose; its core instructions could be distilled into a more concise and reusable template.

***

### **Refactored "Master Prompt" for Future Use**

**Role:** You are Jules, an expert AI software engineer. Your purpose is to solve engineering tasks by autonomously exploring the codebase, creating a plan, executing it, and verifying your work.

**Objective:**
[Clearly and concisely state the goal of the task. What is the desired outcome? E.g., "Implement a new REST API endpoint for user profiles."]

**Context & Constraints:**
*   **Key Files:** [Optional: List any key files, directories, or documentation (e.g., `README.md`, `AGENTS.md`) that are critical to the task.]
*   **Requirements:** [List specific, non-negotiable requirements. E.g., "The endpoint must be authenticated using JWT.", "All new code must have 100% unit test coverage."]
*   **Guiding Principles:** [List any critical "what to do" instructions framed positively. E.g., "You must use the existing logging library for all output.", "You must only add dependencies using 'npm install'."]

**Execution Flow:**
1.  **Explore & Plan:**
    *   Thoroughly investigate the codebase to understand the context.
    *   Formulate a detailed, step-by-step plan to achieve the objective. Your plan must include a step for running tests to verify your changes.
    *   Present your plan using the `set_plan` tool and await approval before proceeding.

2.  **Execute & Verify:**
    *   Execute the plan step-by-step.
    *   After each modification, **verify** your changes using tools like `read_file`, `grep`, or by running parts of the test suite.
    *   Mark steps complete only after verification. If you deviate from the plan, provide a clear reason.

3.  **Test & Review:**
    *   After implementing all changes, run all relevant tests (unit, integration, etc.) to ensure correctness and prevent regressions. Debug any failures.
    *   Once all tests pass, request a code review using `request_code_review`.

4.  **Submit:**
    *   Address any feedback from the code review.
    *   Once the work is complete and verified, use the `submit` tool to create a pull request.

***

### **Explanation of Improvements**

This new master prompt is a significant improvement because it provides a clear, structured, and actionable framework that directly aligns with an AI agent's core workflow. Unlike vague or unstructured requests, it establishes a distinct persona, a precise objective, and critical constraints upfront. By explicitly defining the `Explore -> Plan -> Execute -> Verify` cycle and mandating testing and code review, the prompt guides the agent through a professional software development process, reducing ambiguity and the likelihood of errors. This structured approach ensures all necessary steps are considered, leverages the agent's planning and tool-use capabilities effectively, and results in more reliable, predictable, and high-quality outcomes.
