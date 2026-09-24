# The bar for this library

This library, held to its own [take-to-production](_prompts/task_take_to_production.md) skill. Update the verdicts when something here changes.

## The bar

- **The one job:** an agent or a person finds the procedure for their task, loads exactly that text, and can prove the procedure catches what it claims to.
- **Who, on what:** agents of every harness, reading `SKILL.md`, `AGENTS.md`, MCP or plain HTTP; people on phones from 320 px wide and on desktops, in light and dark, by mouse, touch and keyboard. Hosted by GitHub Pages, which builds with Jekyll 3.10 and the old Ruby Sass.
- **Journeys that must never fail:**
  1. An agent given only the domain finds a skill and loads it.
  2. A person finds a skill and copies, downloads or installs it.
  3. An MCP client lists the prompts and gets one with its placeholders filled.
  4. A maintainer changes a procedure, and every form follows or CI goes red.
- **Never corrupted:** the procedure text. Every form an agent loads is byte for byte its source.
- **Budgets:** stylesheet under 24 KB, script under 8 KB, every page under 120 KB. No script, stylesheet or font from another origin; only the shared favicon.

## Verdicts

Checked on the branch that introduced this file. `scripts/check_site.py` covers the rows marked CI on every push and pull request.

| item | evidence | verdict |
|---|---|---|
| agent, from `llms.txt` | every skill listed; every link resolves in the built site (CI) | holds |
| agent, from the discovery index | 27 of 27 `SKILL.md` served byte for byte, digests match (CI) | holds |
| agent that fetched a skill's HTML page | each carries `<link rel="alternate" type="text/markdown">` to its `SKILL.md` (CI) | holds |
| MCP client | smoke test: every procedure served, placeholder substituted, reading only GitHub (CI) | holds |
| MCP client where the site is unreachable | before: exited with a 403 from the site. After: starts, index and bodies from GitHub | holds |
| person, desktop, light and dark | screenshots of home, skills, a skill, workflow, guide | holds |
| person, 320 px phone | document width 320 on home, skills, a skill, workflow and guide (was 359 and 915) | holds |
| person, keyboard | skip link is the first stop and moves focus to the content; 2 px focus outline | holds |
| contrast, WCAG AA | text 16.3:1, secondary 6.1:1, accent 5.4:1 light and 9.0:1 dark (old accent 3.0:1) | holds |
| copy and download | copied text equals the snippet; `SKILL.md` downloads as `text/markdown` | holds |
| every page whole and titled | one `<h1>` and a `<title>` on every page; no fragments (CI; was 26 skill pages with no heading, and 50 fragments) | holds |
| no prompt text rendered as a table | (CI; was 2 pages) | holds |
| every form matches its source | `emit.py --check`, and the served bytes (CI) | holds |
| every core skill can go red | each fixture's expected report scores; the scorer exits 1 on a report that misses a defect | holds |
| budgets | stylesheet 13.3 KB, script 3.3 KB, largest page 39 KB (CI) | holds |
| Safari and Firefox engines | only Chromium was available to run | skipped |
| a real screen reader | labels, a live region and landmarks are in the markup; not heard with a screen reader | skipped |
| the live deployment | checked on a local build with the GitHub Pages gem set; CI builds with the Pages action | skipped |

## Removed

Turbo and two Google Fonts (three requests to other origins, for a static site). `copy.js`, folded into the one script. Two unused layouts and the empty Commands page. Fifty layout-less `plugin/` pages from the site and its sitemap (84 URLs to 35). The pull-request path filter, which let changes to the MCP server skip CI.

## Refused

A search box: 27 skills in named groups fit on one page. A JavaScript framework or a build step beyond the one GitHub Pages runs. Moving the site to a different host to serve `SKILL.md` directly: wrapping each file as a plain-text collection document does it on Pages, and the site check proves the bytes.

18 items: 15 holds, 0 broken, 3 skipped.
