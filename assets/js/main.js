(function() {
  const sunIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`;
  const moonIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`;
  const systemIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>`;

  function getSystemTheme() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
  }

  function getInitialTheme() {
    return localStorage.getItem('theme') || 'system';
  }

  function updateIcon(theme, toggleBtn) {
    if (!toggleBtn) return;
    if (theme === 'system') {
      toggleBtn.innerHTML = systemIcon;
    } else if (theme === 'dark') {
      toggleBtn.innerHTML = moonIcon;
    } else {
      toggleBtn.innerHTML = sunIcon;
    }
  }

  let currentTheme = getInitialTheme();

  if (currentTheme === 'system') {
    applyTheme(getSystemTheme());
  } else {
    applyTheme(currentTheme);
  }

  function initialize() {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
      updateIcon(currentTheme, themeToggle);

      themeToggle.addEventListener('click', () => {
        let newTheme;
        if (currentTheme === 'system') {
          newTheme = getSystemTheme() === 'dark' ? 'light' : 'dark';
        } else {
          newTheme = 'system';
        }

        localStorage.setItem('theme', newTheme);
        currentTheme = newTheme;

        if (newTheme === 'system') {
          applyTheme(getSystemTheme());
        } else {
          applyTheme(newTheme);
        }
        updateIcon(newTheme, themeToggle);
      });
    }
  }

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    if (currentTheme === 'system') {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });

  document.addEventListener('DOMContentLoaded', initialize);
  document.addEventListener('turbo:load', initialize);
})();
