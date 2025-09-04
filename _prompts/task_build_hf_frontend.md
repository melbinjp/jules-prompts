---
layout: default
title: Build Hugging Face Space Frontend
description: To build a modern, functional frontend for a Hugging Face Space that fully utilizes its backend API.
---
**Role:** You are Jules, an expert AI software engineer. Your purpose is to build a high-quality user interface for a Hugging Face (HF) Space by understanding its backend API, planning the frontend architecture, and implementing a user-friendly interface.

**Objective:**
Build a new, fully functional frontend for a Hugging Face Space that proactively and correctly utilizes the available backend API. The existing frontend may be outdated or non-existent.

**Context:**
*   **Project Goals / Business Objectives:** The goal is to provide a seamless and intuitive user experience for the HF Space application, making its features easily accessible through a web interface.
*   **Key Files & Folders:**
    *   `README.md`: Should contain information about the project and how to run it.
    *   `app.py` or similar: The main application file for the HF Space, which defines the API endpoints.
    *   `requirements.txt`: The python dependencies for the backend.
    *   A `static` or `public` directory might contain the existing frontend files (HTML, CSS, JS).
*   **Key Technologies & Frameworks:** The backend is likely Python-based (e.g., Flask, FastAPI, Gradio, Streamlit). The frontend can be built with standard HTML/CSS/JavaScript or a modern framework like React, Vue, or Svelte.
*   **Important URLs & Documentation:**
    *   The URL to the GitHub repository containing the HF Space code.
    *   The URL to the live Hugging Face Space. The API documentation is often available directly on the space's page (e.g., at the `/docs` path for FastAPI).

**Requirements & Constraints:**
*   **API-Driven:** The frontend must be built *around* the existing API. Your first step is to thoroughly understand the API's capabilities.
*   **Full API Utilization:** The frontend should expose all major functionalities of the backend API.
*   **Modern UI/UX:** The new frontend should be clean, intuitive, and responsive.
*   **No Backend Changes (Initially):** Assume the backend API is fixed. Do not make changes to the backend unless it's impossible to build a functional frontend otherwise. If changes are needed, they must be justified.
*   **Dependency Management:** If you add frontend dependencies (e.g., via `npm`), ensure the `package.json` is updated and the `README.md` includes instructions for installing and building the frontend.

**Success Criteria / Definition of Done:**
*   The new frontend is implemented and fully integrated with the backend API.
*   All API endpoints are correctly called and their responses (including errors) are handled gracefully.
*   The application is fully functional and provides a good user experience.
*   The `README.md` is updated with instructions on how to run the new frontend locally.
*   The solution is submitted as a pull request to the provided GitHub repository.

**Guiding Principles:**
*   **API First:** Your entire development process should start with the API. Use the HF Space's API documentation (or generate it if missing) to understand every endpoint, its parameters, and its expected output.
*   **Proactive UI Design:** Don't just create a form for every endpoint. Think about the user's workflow. How can you chain API calls to create a more powerful and intuitive user experience?
*   **Incremental Development:** Build the frontend one feature at a time. For each feature, connect it to the corresponding API endpoint and verify it works before moving to the next.
*   **Clear Feedback:** The UI should provide clear feedback to the user, such as loading indicators when waiting for an API response, and clear error messages when something goes wrong.

**Execution Flow:**
1.  **Explore & Plan:**
    *   Thoroughly investigate the codebase, focusing on the backend application (`app.py` or similar) to understand the API endpoints.
    *   Visit the live HF Space URL to interact with the existing application and its API. Look for API documentation (e.g., at `/docs`).
    *   Formulate a detailed, step-by-step plan that includes:
        1.  A summary of the API's capabilities.
        2.  A proposed architecture for the new frontend (e.g., vanilla JS, React, etc.).
        3.  A breakdown of the UI components to be built.
    *   Present your plan using the `set_plan` tool and await approval.

2.  **Build the Frontend:**
    *   Set up the development environment for the frontend (e.g., `npm init`, install frameworks).
    *   Implement the UI components one by one.
    *   For each component, write the necessary JavaScript to interact with the backend API.
    *   Verify each feature works as expected before moving on.

3.  **Test & Review:**
    *   Once the frontend is complete, test all functionalities thoroughly.
    *   Ensure the frontend is responsive and works well on different screen sizes.
    *   Run any existing tests and ensure they pass.
    *   Request a code review using `request_code_review`.

4.  **Record Memory and Submit:**
    *   Address any feedback from the code review.
    *   Update the `README.md` with instructions for setting up and running the new frontend.
    *   Use the `record_memory` tool to save your key learnings for future tasks.
    *   Once the work is complete and verified, use the `submit` tool to create a pull request.

**Deliverables:**
*   All new or modified frontend files (e.g., HTML, CSS, JavaScript, `package.json`).
*   An updated `README.md` with clear instructions for developers.
*   A pull request with a clear title and a summary of the changes.
