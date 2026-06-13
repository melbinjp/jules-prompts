/**
 * copy.js — Copy-to-clipboard functionality for jules-prompts
 *
 * Attaches click handlers to every `.copy-btn` element.
 * Copies the text content of `#main-content` to the clipboard
 * using the Clipboard API, then provides visual feedback via
 * a button state change and a toast notification.
 *
 * Re-initialises on both 'DOMContentLoaded' and 'turbo:load'
 * so it works seamlessly with Turbo Drive page transitions.
 */
(() => {
  'use strict';

  /* ===================================================================
   *  SVG Icons
   * =================================================================== */

  /** Checkmark icon shown after a successful copy */
  const CHECK_ICON = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                          viewBox="0 0 24 24" fill="none" stroke="currentColor"
                          stroke-width="2.5" stroke-linecap="round"
                          stroke-linejoin="round">
                        <polyline points="20 6 9 17 4 12"/>
                      </svg>`;

  /* ===================================================================
   *  Initialisation
   * =================================================================== */

  function initCopyButtons() {
    const buttons = document.querySelectorAll('.copy-btn');

    buttons.forEach((btn) => {
      // Save the original button markup so we can restore it later
      const originalHTML = btn.innerHTML;

      // Clone the button to strip any previously attached listeners
      // (prevents duplicate handlers after Turbo re-renders)
      const freshBtn = btn.cloneNode(true);
      btn.parentNode.replaceChild(freshBtn, btn);

      freshBtn.addEventListener('click', async () => {
        // Grab the prompt text from the prompt body if it exists, otherwise main content
        let content = document.getElementById('prompt-body');
        if (!content) {
          content = document.getElementById('main-content');
        }
        if (!content) return;

        const text = content.innerText.trim();

        try {
          await navigator.clipboard.writeText(text);

          // --- Success feedback ---
          freshBtn.innerHTML = `${CHECK_ICON} <span>Copied!</span>`;
          freshBtn.classList.add('copied');

          // Show a toast notification (defined in main.js)
          if (typeof window.showToast === 'function') {
            window.showToast('Prompt copied to clipboard!');
          }

          // Reset button after 2 seconds
          setTimeout(() => {
            freshBtn.innerHTML = originalHTML;
            freshBtn.classList.remove('copied');
          }, 2000);

        } catch (err) {
          console.error('Clipboard write failed:', err);

          // Show an error toast
          if (typeof window.showToast === 'function') {
            window.showToast('Failed to copy — please try again.');
          }
        }
      });
    });
  }

  /* ===================================================================
   *  Bootstrap — run on every page load (standard + Turbo)
   * =================================================================== */

  document.addEventListener('DOMContentLoaded', initCopyButtons);
  document.addEventListener('turbo:load', initCopyButtons);
})();
