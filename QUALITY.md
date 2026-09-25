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
- **Found:** a person or an assistant searching for Agent Skills, or for a skill's job, lands on the page for it, and a shared link shows what it is.
- **Budgets:** stylesheet under 24 KB, script under 8 KB, font under 40 KB, preview image under 150 KB, every page under 120 KB. No script, stylesheet or font from another origin; only the shared favicon.

## Areas walked

- **Security:** a static site with no input, no cookies and no server. No secrets anywhere in the history. The MCP server fetches only from GitHub over HTTPS; its dependencies are audited in CI; CI actions are pinned to commits. The real exposure is the trust root: whatever is on `main` is what every agent that loads these skills is told to do, so who can push to `main` matters more than anything on the site. The discovery digests detect a changed file in transit, not a bad commit.
- **Privacy:** no analytics, cookies or third-party scripts. The shared favicon host sees visitors' addresses.
- **Reliability:** the MCP server depends on GitHub alone (it depended on the site as well).
- **Compatibility, accessibility and craft:** rows below.
- **Legal:** MIT. One font, Martian Mono, self-hosted under the SIL Open Font License, with the licence beside it in `assets/fonts/OFL.txt`. The name began as prompts for Google's Jules; the site says it is not affiliated with Google, in the footer and in its questions.
- **Not applicable:** a content security policy (nothing on the site takes input or runs third-party code; add one if that changes), capacity, monitoring and backups (static hosting, and the repository is the data), physical safety.

## Verdicts

Checked on the branch that introduced this file. CI covers the rows marked CI on every push and pull request.

| item | evidence | verdict |
|---|---|---|
| agent, from `llms.txt` | every skill listed; every link resolves in the built site (CI) | holds |
| agent, from the discovery index | 31 of 31 `SKILL.md` served byte for byte, digests match (CI) | holds |
| agent that fetched a skill's HTML page | each carries `<link rel="alternate" type="text/markdown">` to its `SKILL.md` (CI) | holds |
| MCP client | smoke test: every procedure served, placeholder substituted, reading only GitHub (CI) | holds |
| MCP client where the site is unreachable | before: exited with a 403 from the site. After: starts, index and bodies from GitHub | holds |
| person, desktop, light and dark | screenshots of home, skills, a skill, workflow, guide | holds |
| person, 320 px phone | document width 320 on all 41 pages (was 359 and 915 before the first redesign) | holds |
| person, keyboard | skip link is the first stop and moves focus to the content; every stop has a 2 px outline, ink in light and lime in dark | holds |
| contrast, WCAG AA | computed for every token pair on every surface. Light: text 15.8, secondary 6.1, links 8.3, labels 6.4, verdict colours at least 4.7. Dark: 14.0, 6.7, 12.6, 11.0, 7.1. Ink on the highlighter 14.2 | holds |
| copy and download | copied text equals the snippet; `SKILL.md` downloads as `text/markdown` | holds |
| every page whole and titled | one `<h1>` and a `<title>` on every page; no fragments (CI; was 26 skill pages with no heading, and 50 fragments) | holds |
| no prompt text rendered as a table | (CI; was 2 pages) | holds |
| every form matches its source | `emit.py --check`, and the served bytes (CI) | holds |
| every core skill can go red | 14 fixtures, 68 planted defects: each fixture's expected report names all of its own; the scorer exits 1 on a report that misses one | holds |
| budgets | stylesheet 19.2 KB, script 3.3 KB, font 23.6 KB, preview image 62.5 KB, largest page 54 KB, the guide (CI) | holds |
| a search engine or assistant reading a page | titles and descriptions name what it is and which agents read it; structured data parses on every page; the home page has WebSite and FAQPage, each skill page a TechArticle naming its title and its `SKILL.md` (CI) | holds |
| a link shared in a chat or a post | every page names a 1200 by 630 preview image the site serves (CI) | holds |
| the report on the home page | generated from the fixture's expected report; the generator refuses a total that disagrees with the table (CI) | holds |
| Claude Code plugin install | from a clean config, marketplace add and install: 31 skills, about 2.3k tokens in every session (was 54 entries and 3.5k, every skill twice; the four lifecycle skills add about 550). The longest skill, `start-from-an-idea`, costs about 6.6k when loaded, more than `take-to-production`'s 5.5k: it carries the funding routes, the mechanisms that keep the owner and the agent out of the dark, and the routing of work to each agent's strengths, which were cut once and put back because they are the point of it. Both manifests pass `claude plugin validate --strict` | holds |
| the ledger check other projects copy | the worked example passes; each of the 29 ways of breaking a ledger fails it by name, including a decision with one backing, a decision backed only by sources, and a commit with no `Verified:` line; a checker with any of those rules weakened fails the tests (CI) | holds |
| no skill tells an agent to end or refuse a project | the integrity check refuses stop conditions, kill criteria and "should it exist" verdicts in any procedure; seen failing on a planted line (CI) | holds |
| every workflow step says when it is done, and what it calls on | the integrity check refuses a step with no gate, or a branch that is not a procedure; seen failing on both (CI) | holds |
| a ledger check that passes is not a verdict | it passes on `vendor-comparison` and `six-months-in`, which have 13 planted defects between them; the skills and the fixtures say so | holds |
| no secrets in the history | pattern scan of every commit on every branch | holds |
| no known vulnerabilities in what the MCP server ships | `npm audit`: 0 (was 1 high, 2 moderate, in the SDK's HTTP transports); high fails CI | holds |
| CI actions pinned | each pinned to a commit, tag in a comment | holds |
| who can change what agents are told | depends on `main`'s branch protection, which this session cannot read | skipped |
| Safari and Firefox engines | only Chromium was available to run | skipped |
| a real screen reader | labels, a live region and landmarks are in the markup; not heard with a screen reader | skipped |
| the live deployment | checked on a local build with the GitHub Pages gem set; CI builds with the Pages action | skipped |
| a live agent, given each lifecycle skill, scored on its fixture | the expected reports score; no agent run on these four fixtures has been scored yet, and one run by the author, who planted the defects, would not count | skipped |
| found in search results | a web search still shows the site's old description; a fresh crawl can only be requested by the owner, in Google Search Console and Bing Webmaster Tools | skipped |

## Removed

The plugin's 27 slash commands, which Claude Code loaded as a second copy of every skill. Turbo and two Google Fonts (three requests to other origins, for a static site). `copy.js`, folded into the one script. Two unused layouts and the empty Commands page. Fifty layout-less `plugin/` pages from the site and its sitemap (84 URLs to 35). The pull-request path filter, which let changes to the MCP server skip CI.

## Refused

A step that decides whether an idea deserves to be built, and conditions that end a project. The first version of the lifecycle had both; the library is for making ideas happen, so a constraint gets routes around it and a blocked route gets another. A service to run the lifecycle: two folders in the project and a check in its CI do it, with nothing to host. Renaming the library. The name is where it started, and it is what people already search for; every page says what it is now, and that it is not affiliated with Google. A search box: 31 skills in named groups fit on one page. A JavaScript framework or a build step beyond the one GitHub Pages runs. Moving the site to a different host to serve `SKILL.md` directly: wrapping each file as a plain-text collection document does it on Pages, and the site check proves the bytes.

32 items: 26 holds, 0 broken, 6 skipped.
