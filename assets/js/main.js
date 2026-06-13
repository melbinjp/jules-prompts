/**
 * main.js — Core UI logic for jules-prompts Jekyll site
 *
 * Features:
 *   • Theme toggle (light / dark / system)
 *   • Mobile sidebar toggle
 *   • Active-page highlighting in sidebar
 *   • Sidebar search / filter
 *   • Toast notification system
 *
 * Wrapped in an IIFE to avoid polluting the global scope.
 * Initialises on both 'DOMContentLoaded' and 'turbo:load' for
 * compatibility with Turbo Drive navigation.
 */
(() => {
  'use strict';

  /* ===================================================================
   *  SVG Icon Definitions
   * =================================================================== */

  const ICONS = {
    sun: `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
              viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"/>
            <line x1="12" y1="1"  x2="12" y2="3"/>
            <line x1="12" y1="21" x2="12" y2="23"/>
            <line x1="4.22"  y1="4.22"  x2="5.64"  y2="5.64"/>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
            <line x1="1"  y1="12" x2="3"  y2="12"/>
            <line x1="21" y1="12" x2="23" y2="12"/>
            <line x1="4.22"  y1="19.78" x2="5.64"  y2="18.36"/>
            <line x1="18.36" y1="5.64"  x2="19.78" y2="4.22"/>
          </svg>`,

    moon: `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
              viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3
                     A7 7 0 0 0 21 12.79z"/>
          </svg>`,

    system: `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"
                viewBox="0 0 24 24" fill="none" stroke="currentColor"
                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
              <line x1="8"  y1="21" x2="16" y2="21"/>
              <line x1="12" y1="17" x2="12" y2="21"/>
            </svg>`
  };

  /* ===================================================================
   *  Theme Toggle  (system → light → dark → system)
   * =================================================================== */

  /** Media query for OS-level dark preference */
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');

  /**
   * Apply the given theme to the document.
   * @param {'light'|'dark'|'system'} theme
   */
  function applyTheme(theme) {
    const html = document.documentElement;

    if (theme === 'dark') {
      html.setAttribute('data-theme', 'dark');
    } else if (theme === 'light') {
      html.removeAttribute('data-theme');
    } else {
      // 'system' — follow the OS preference
      if (prefersDark.matches) {
        html.setAttribute('data-theme', 'dark');
      } else {
        html.removeAttribute('data-theme');
      }
    }
  }

  /**
   * Update the toggle button's inner icon to reflect the current theme.
   * @param {HTMLElement} btn
   * @param {'light'|'dark'|'system'} theme
   */
  function updateToggleIcon(btn, theme) {
    if (!btn) return;

    switch (theme) {
      case 'light':
        btn.innerHTML = ICONS.sun;
        btn.setAttribute('aria-label', 'Switch to dark theme');
        break;
      case 'dark':
        btn.innerHTML = ICONS.moon;
        btn.setAttribute('aria-label', 'Switch to system theme');
        break;
      default: // 'system'
        btn.innerHTML = ICONS.system;
        btn.setAttribute('aria-label', 'Switch to light theme');
    }
  }

  /**
   * Initialise the theme toggle button behaviour.
   */
  function initThemeToggle() {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;

    // Read persisted preference or default to 'system'
    let current = localStorage.getItem('theme') || 'system';
    applyTheme(current);
    updateToggleIcon(btn, current);

    // Cycle: system → light → dark → system
    btn.addEventListener('click', () => {
      if (current === 'system') {
        current = 'light';
      } else if (current === 'light') {
        current = 'dark';
      } else {
        current = 'system';
      }

      localStorage.setItem('theme', current);
      applyTheme(current);
      updateToggleIcon(btn, current);
    });

    // React to OS theme changes while in 'system' mode
    prefersDark.addEventListener('change', () => {
      if ((localStorage.getItem('theme') || 'system') === 'system') {
        applyTheme('system');
      }
    });
  }

  /* ===================================================================
   *  Sidebar Toggle  (mobile hamburger menu)
   * =================================================================== */

  function initSidebarToggle() {
    const menuBtn = document.getElementById('menu-toggle');
    const overlay = document.getElementById('sidebar-overlay');

    if (menuBtn) {
      menuBtn.addEventListener('click', () => {
        document.body.classList.toggle('sidebar-open');
      });
    }

    // Close sidebar when the overlay is tapped
    if (overlay) {
      overlay.addEventListener('click', () => {
        document.body.classList.remove('sidebar-open');
      });
    }

    // Close sidebar when any sidebar link is clicked (mobile UX)
    document.querySelectorAll('.sidebar a').forEach((link) => {
      link.addEventListener('click', () => {
        document.body.classList.remove('sidebar-open');
      });
    });
  }

  /* ===================================================================
   *  Active Page Highlighting
   * =================================================================== */

  function highlightActivePage() {
    const currentPath = window.location.pathname.replace(/\/$/, '') || '/';

    document.querySelectorAll('.sidebar a').forEach((link) => {
      const linkPath = new URL(link.href, window.location.origin)
        .pathname.replace(/\/$/, '') || '/';

      if (linkPath === currentPath) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  /* ===================================================================
   *  Sidebar Search / Filter
   * =================================================================== */

  function initSidebarSearch() {
    const input = document.getElementById('search-input');
    if (!input) return;

    input.addEventListener('input', () => {
      const query = input.value.toLowerCase().trim();

      // Target only <li> items inside the sidebar prompt list
      document.querySelectorAll('.sidebar-prompts li').forEach((li) => {
        const link = li.querySelector('a');
        if (!link) return;

        const text = link.textContent.toLowerCase();
        li.style.display = text.includes(query) ? '' : 'none';
      });
    });
  }

  /* ===================================================================
   *  Toast Notification System
   * =================================================================== */

  /**
   * Show a brief toast message at the bottom of the viewport.
   * @param {string} message — Text to display
   * @param {number} [duration=2500] — Time in ms before the toast fades out
   */
  window.showToast = function showToast(message, duration = 2500) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    document.body.appendChild(toast);

    // Trigger the entrance animation on the next frame
    setTimeout(() => toast.classList.add('show'), 10);

    // Remove after the specified duration
    setTimeout(() => {
      toast.classList.remove('show');
      // Wait for the CSS fade-out transition before removing the element
      toast.addEventListener('transitionend', () => toast.remove(), { once: true });
      // Fallback removal in case transitionend never fires
      setTimeout(() => toast.remove(), 400);
    }, duration);
  };

  /* ===================================================================
   *  Bootstrap — run on every page load (standard + Turbo)
   * =================================================================== */

  function init() {
    initThemeToggle();
    initSidebarToggle();
    highlightActivePage();
    initSidebarSearch();
  }

  document.addEventListener('DOMContentLoaded', init);
  document.addEventListener('turbo:load', init);
})();
