---
name: build-api-frontend
description: 'To build a modern, functional frontend for an application based on its
  backend API. Category: Initial Scoping.'
license: MIT
metadata:
  prompt_slug: task_build_api_frontend
  source: _prompts/task_build_api_frontend.md
  title: Build API-Driven Frontend
  category: Initial Scoping
---

# Build API-Driven Frontend

**Role:** You are a coding agent. Build a high-quality user interface by reading an application's backend API, planning the frontend architecture, and implementing a usable, responsive interface.

**Objective:**
Build a new, fully functional frontend that proactively and correctly utilizes an available backend API. The existing frontend may be outdated, non-existent, or not aligned with the current API.

**Context to be Provided by User:**
> **Instructions for User:** Please fill out the following sections with the details of your project. This information is crucial for the AI agent to understand the task.

*   **Application Repository URL:** [**REQUIRED** - Provide the URL to the GitHub repository where the frontend code should be developed. If the agent is already working in the correct repository, you can state that.]
*   **Backend API Source (Choose one or more):**
    *   **Live API Endpoint URL:** [Provide the URL to the live/staging API, e.g., a Hugging Face Space, a deployed backend.]
    *   **API Documentation URL:** [Provide the URL to Swagger/OpenAPI, Postman, or other API documentation.]
    *   **Backend Source Code Location:** [If no live API or docs are available, point to the directory in the repository that contains the backend source code for API analysis.]
*   **Existing Frontend (Optional):**
    *   **Live URL:** [URL of the existing frontend, if any.]
    *   **Design Language/Theme:** [Describe the design language or point to existing components/screenshots to follow.]

**Requirements & Constraints:**
*   **API-Driven:** The frontend must be built *around* the existing API. Your first step is to thoroughly understand the API's capabilities.
*   **UI/UX Best Practices are Paramount:** Even if an existing design is provided, you must prioritize modern UI/UX principles and best practices. If the requested design is suboptimal (e.g., poor accessibility, confusing layout), you should improve it while trying to respect the general aesthetic.
*   **Responsive Design:** The UI must be fully responsive and provide an excellent user experience on all display sizes.
*   **No Backend Changes (Initially):** Assume the backend API is fixed. Do not make changes to the backend unless it's impossible to build a functional frontend otherwise.
*   **Dependency Management:** Ensure `package.json` (or equivalent) is updated and the `README.md` includes clear build instructions.

**Success Criteria / Definition of Done:**
*   A foundational frontend skeleton is implemented and connects to the backend API.
*   The UI is responsive and visually verified to be free of obvious defects.
*   A detailed `PLAN.md` and a summary `AGENT.md` are created to guide future development.
*   The `README.md` is updated with clear instructions on how to run the new frontend locally.
*   The solution is submitted as a pull request.

**Guiding Principles:**
*   **Champion for the End-User:** Your primary goal is to create a high-quality user experience. If a user's design request conflicts with usability or accessibility best practices, diplomatically prioritize the better experience.
*   **API First:** Your entire development process must start with the API. Use any available documentation (or generate it if missing) to understand every endpoint, its parameters, and its expected output.
*   **Plan for Iteration:** This is a foundational task. Focus on building a solid, extensible skeleton. Create a highly detailed plan in `PLAN.md` and document your architectural decisions in `AGENT.md` to set up future agents for success.
*   **Clear Feedback:** The UI should provide clear feedback to the user, such as loading indicators when waiting for an API response, and clear error messages when something goes wrong.

**Execution Flow:**
1.  **Phase 1: Foundation & Planning**
    *   **Explore:** Thoroughly investigate the codebase and the URLs provided in the 'Context' section to understand the project, the backend API, and any existing frontend/design language.
    *   **Plan:** Formulate a highly detailed, step-by-step plan for the *entire project*, but with an initial focus on building a foundational skeleton. The plan must be granular enough for another agent to execute.
    *   **Document:**
        1.  Create a detailed `PLAN.md` file containing the full, granular project plan.
        2.  Create or update `AGENT.md` with a high-level summary of the plan, the chosen architecture, and a direct link to `PLAN.md`. This keeps `AGENT.md` clean.
    *   **Present:** Write the high-level summary and link to the detailed plan.

2.  **Phase 2: Skeleton Implementation**
    *   Set up the development environment, project structure, and build tools.
    *   Implement the core layout and a small number of essential UI components.
    *   Implement the logic for connecting to one or two key API endpoints to prove the architecture works.
    *   Ensure the foundational code is clean, well-documented, and follows the chosen architecture.

3.  **Phase 3: Verification & Handoff**
    *   **Visually Verify:** Use the `frontend_verification_instructions` tool to get instructions on how to create a Playwright script. Write and run a script to take a screenshot of the new frontend skeleton to ensure it is rendering correctly and is free of visual defects.
    *   **Review:** Verify that the skeleton is working and that the `README.md`, `AGENT.md`, and `PLAN.md` are up-to-date. Request a code review of the foundational work through the harness if it has one; otherwise include the review in the deliverable.
    *   **Recommend Next Step:** In the pull request body (or the harness equivalent), recommend that the user run a follow-up prompt like "Build From Plan" to complete the project, pointing them to the `PLAN.md` you created.

4.  **Record Memory and Submit:**
    *   Address any feedback from the code review.
    *   Update the `README.md` with instructions for setting up and running the new frontend skeleton.
    *   Write anything that should persist into `AGENTS.md` or the session notes.
    *   Submit the foundational skeleton along with `AGENT.md` and `PLAN.md`.

**Deliverables:**
*   A functional frontend skeleton with a core layout and a few working components.
*   A comprehensive `AGENT.md` file with a summary and link to the detailed plan.
*   A highly detailed `PLAN.md` file with a granular plan for completing the entire UI.
*   An updated `README.md` with clear developer setup instructions.
*   All project files required to build and run the skeleton (e.g., `package.json`, build configs).
*   A screenshot from the visual verification step.
*   A pull request with a clear title (e.g., "feat: create foundational frontend skeleton") and a summary of the work done and the proposed next steps.
