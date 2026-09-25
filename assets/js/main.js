// The site's only script: the theme choice and the copy buttons. No framework and no
// third-party code. Every page reads, links and follows the system theme without it.
(function () {
  var root = document.documentElement;
  var MODES = ['system', 'light', 'dark'];
  var LABELS = { system: 'System', light: 'Light', dark: 'Dark' };

  function storedMode() {
    try {
      var mode = localStorage.getItem('theme');
      return mode === 'light' || mode === 'dark' ? mode : 'system';
    } catch (e) {
      return 'system'; // storage blocked: follow the system, which needs nothing stored
    }
  }

  function applyMode(mode) {
    if (mode === 'system') root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', mode);
    try {
      if (mode === 'system') localStorage.removeItem('theme');
      else localStorage.setItem('theme', mode);
    } catch (e) { /* the choice lasts for this page only */ }
  }

  function announce(text) {
    var live = document.getElementById('live');
    if (!live) return;
    live.textContent = '';
    setTimeout(function () { live.textContent = text; }, 50);
  }

  function initTheme() {
    var button = document.getElementById('theme-toggle');
    if (!button) return;
    var mode = storedMode();
    function show() {
      button.setAttribute('data-mode', mode);
      button.setAttribute('aria-label', 'Theme: ' + LABELS[mode] + '. Switch theme');
      button.title = 'Theme: ' + LABELS[mode];
    }
    show();
    button.addEventListener('click', function () {
      mode = MODES[(MODES.indexOf(mode) + 1) % MODES.length];
      applyMode(mode);
      show();
      announce('Theme: ' + LABELS[mode]);
    });
  }

  // Selects the element's text, so a person can copy it by hand when the clipboard is refused.
  function select(element) {
    var range = document.createRange();
    range.selectNodeContents(element);
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
  }

  function initCopy() {
    var buttons = document.querySelectorAll('[data-copy]');
    Array.prototype.forEach.call(buttons, function (button) {
      var label = button.textContent;
      var timer = null;
      function say(text) {
        button.textContent = text;
        announce(text);
        clearTimeout(timer);
        timer = setTimeout(function () { button.textContent = label; }, 2000);
      }
      button.addEventListener('click', function () {
        var target = document.querySelector(button.getAttribute('data-copy'));
        if (!target) return;
        var text = target.innerText.trim();
        function byHand() {
          select(target);
          var touch = window.matchMedia && window.matchMedia('(pointer: coarse)').matches;
          var apple = /Mac|iPhone|iPad/.test(navigator.platform || '');
          say(touch ? 'Selected' : 'Selected: press ' + (apple ? '\u2318C' : 'Ctrl+C'));
        }
        if (!navigator.clipboard || !window.isSecureContext) return byHand();
        navigator.clipboard.writeText(text).then(function () { say('Copied'); }, byHand);
      });
    });
  }

  function init() {
    initTheme();
    initCopy();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
