# The bar for this library

This library, held to its own [take-to-production](_prompts/task_take_to_production.md) skill. Update the verdicts when something here changes.

## The bar

- **The one job:** an agent or a person finds the procedure for their task, loads exactly that text, and can prove the procedure catches what it claims to.
- **Who, on what:** agents of every harness, reading `SKILL.md`, `AGENTS.md`, MCP or plain HTTP, online or on a machine with no network, including small local models; people on phones from 320 px wide and on desktops, in light and dark, by mouse, touch and keyboard. Hosted by GitHub Pages, which builds with Jekyll 3.10 and the old Ruby Sass.
- **Journeys that must never fail:**
  1. An agent given only the domain finds a skill and loads it.
  2. A person finds a skill and copies, downloads or installs it.
  3. An MCP client lists the prompts and gets one with its placeholders filled.
  4. A maintainer changes a procedure, and every form follows or CI goes red.
  5. An agent on a machine with no network loads the skills, and the MCP server, from a copy.
  6. A model with no harness builds its own from the specification, and proves it before starting.
  7. A person or an agent arriving with a project in any state finds where to start, and every start leads onto the same path.
- **Never corrupted:** the procedure text. Every form an agent loads is byte for byte its source.
- **Found:** a person or an assistant searching for Agent Skills, or for a skill's job, lands on the page for it, and a shared link shows what it is.
- **Budgets:** stylesheet under 24 KB, script under 8 KB, font under 40 KB, preview image under 150 KB, every page under 120 KB. No script, stylesheet or font from another origin; only the shared favicon.

## Areas walked

- **Security:** a static site with no input, no cookies and no server. No secrets anywhere in the history. The MCP server fetches only from GitHub over HTTPS; its dependencies are audited in CI; CI actions are pinned to commits. The real exposure is the trust root: whatever is on `main` is what every agent that loads these skills is told to do, so who can push to `main` matters more than anything on the site. The discovery digests detect a changed file in transit, not a bad commit.
- **Privacy:** no analytics, cookies or third-party scripts. The shared favicon host sees visitors' addresses. Fetching a skill from the site tells its host which skill someone wanted; installing from a copy of the repository tells nobody, and the README says so.
- **Reliability:** the MCP server depends on GitHub alone (it depended on the site as well).
- **Compatibility, accessibility and craft:** rows below.
- **Legal:** MIT. One font, Martian Mono, self-hosted under the SIL Open Font License, with the licence beside it in `assets/fonts/OFL.txt`. The name began as prompts for Google's Jules; the site says it is not affiliated with Google, in the footer and in its questions.
- **Not applicable:** a content security policy (nothing on the site takes input or runs third-party code; add one if that changes), capacity, monitoring and backups (static hosting, and the repository is the data), physical safety.

## Verdicts

Checked on the branch that introduced this file. CI covers the rows marked CI on every push and pull request.

| item | evidence | verdict |
|---|---|---|
| agent, from `llms.txt` | every skill listed; every link resolves in the built site (CI) | holds |
| agent, from the discovery index | 36 of 36 `SKILL.md` served byte for byte, digests match (CI) | holds |
| agent that fetched a skill's HTML page | each carries `<link rel="alternate" type="text/markdown">` to its `SKILL.md` (CI) | holds |
| MCP client | smoke test: every procedure served, placeholder substituted, reading only GitHub (CI) | holds |
| MCP client with no network at all | `JULES_PROMPTS_DIR` serves all 36 from a copy; in that mode fetch throws, and a planted network call made the server refuse to start (CI) | holds |
| small local model | a short form of each of the 29 core skills in `compact/`, 187 to 945 words, generated and checked byte for byte (CI) | holds |
| a small local model, qualified on a fixture with a short form | no local model runtime in this session; the scorer that would do it runs offline | skipped |
| every procedure usable without hosted services | each says it assumes none, and to use the project's own equivalent; the integrity check refuses one that does not (CI) | holds |
| MCP client where the site is unreachable | before: exited with a 403 from the site. After: starts, index and bodies from GitHub | holds |
| person, desktop, light and dark | screenshots of home, skills, a skill, workflow, guide | holds |
| person, 320 px phone | document width 320 on all 44 pages (was 359 and 915 before the first redesign) | holds |
| person, touch | every list of links (the path, the routes in, the contents of a skill, each step's title and what it calls on, the breadcrumb) is at least 44 px tall on a touch screen, measured at 375 px (the contents list was 16 px, the path 20 px); links inside sentences are left inline; the copy buttons draw at 32 px with a 44 px hit area | holds |
| person reading a long skill | its sections are headings with an "On this page" list, beside the text on a wide screen; the `SKILL.md` agents load is unchanged (CI checks the bytes) | holds |
| person, keyboard | skip link is the first stop and moves focus to the content; every stop has a 2 px outline, ink in light and lime in dark | holds |
| contrast, WCAG AA | computed for every token pair on every surface. Light: text 15.8, secondary 6.1, links 8.3, labels 6.4, verdict colours at least 4.7. Dark: 14.0, 6.7, 12.6, 11.0, 7.1. Ink on the highlighter 14.2 | holds |
| copy and download | copied text equals the snippet; `SKILL.md` downloads as `text/markdown` | holds |
| every page whole and titled | one `<h1>` and a `<title>` on every page; no fragments (CI; was 26 skill pages with no heading, and 50 fragments) | holds |
| no prompt text rendered as a table | (CI; was 2 pages) | holds |
| every form matches its source | `emit.py --check`, and the served bytes (CI) | holds |
| every core skill can go red | 19 fixtures, 107 planted defects: each fixture's expected report names all of its own; the scorer exits 1 on a report that misses one | holds |
| budgets | stylesheet 19.1 KB, now shipped compressed (24.1 KB before, which broke the budget when the new sections were added), script 3.3 KB, font 23.6 KB, preview image 62.5 KB, largest page 67 KB, the guide (CI) | holds |
| a search engine or assistant reading a page | titles and descriptions name what it is and which agents read it; structured data parses on every page; the home page has WebSite and FAQPage, each skill page a TechArticle naming its title and its `SKILL.md` (CI) | holds |
| a link shared in a chat or a post | every page names a 1200 by 630 preview image the site serves (CI) | holds |
| the report on the home page | generated from the fixture's expected report; the generator refuses a total that disagrees with the table (CI) | holds |
| Claude Code plugin install | from a clean config, marketplace add and install: 36 skills, about 3.0k tokens in every session, about 82 a skill (was 54 entries and 3.5k, every skill twice; the two newest descriptions were cut from about 180 and 150 tokens to 120 each). The longest skill, `start-from-an-idea`, costs about 7.4k when loaded, and `run-autonomously` about 5.4k; their short forms in `compact/` are about 1.3k each for models that cannot hold them. Both manifests pass `claude plugin validate --strict` | holds |
| a model with no harness can build one and know it is fit | `harness/conformance.py` drives a harness with a scripted model through 25 checks (fresh bounded context, files confined, the person's file protected, choices never waited on, overrides shown, checkpoints, stop, step limit, short-form fallback, remote refused before any request and sent through the proxy when allowed); it passes a reference and catches each of 12 copies with one property broken (CI) | holds |
| a self-built harness, driven by a real model through a real build | no model runtime in this session; the conformance test and the scorer run offline on the owner's machine | skipped |
| the ledger check other projects copy | the worked example passes; each of the 29 ways of breaking a ledger fails it by name, including a decision with one backing, a decision backed only by sources, and a commit with no `Verified:` line; a checker with any of those rules weakened fails the tests (CI) | holds |
| no skill tells an agent to end or refuse a project | the integrity check refuses stop conditions, kill criteria and "should it exist" verdicts in any procedure; seen failing on a planted line (CI) | holds |
| a project in any state has a way in | `workflow.json` names eight starting states, from "broken for people right now" to "an idea and only a model"; the integrity check refuses an entry that starts off the path, and one that lets an existing project skip being founded again on paper (CI) | holds |
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

## What the owner asked for, and where it is met

The owner's requests across the sessions that built this library, abridged and grouped. Each is traced to where the library meets it, so a later change can tell a requirement from an accident.

| asked for | where it is met | verdict |
|---|---|---|
| any idea, any project, in any state, taken to production and kept there | `workflow.json` entries, one per starting state, each leading onto one path; an existing project founded again on paper first | holds |
| the whole SDLC set up from the idea: scaffolding, pipeline, a floor that later stages never regret | `start-from-an-idea`: one-way doors with evidence, every stage a command, a walking skeleton | holds |
| automated, hybrid or manual; operated by a person, an agent, or both | the pipeline's operating model (`start-from-an-idea`), and every product action operable by a person and an agent with the same limits (`design-the-experience`) | holds |
| nothing without a reason; every change backed by verified evidence of two kinds; no drift | the ledger, `Serves:`/`Verified:` trailers, and `harness/check_trace.py` in the project's CI | holds |
| the person and the agent in the dark about each other; vague requests never becoming ghost code | `change-with-a-reason`: every claim translated into a measure, built through every layer | holds |
| engineering, architecture, design and user flow moving as one | journey threads (`start-from-an-idea`) with the design threaded to them (`design-the-experience`) | holds |
| design, UI and UX, and any other missing discipline, where needed | `design-the-experience`; `release-to-people` for reaching people; `handle-an-incident` for keeping it working when it breaks | holds |
| looks good, finished, efficient, dependable, without useless complexity | the craft standard and the complexity budget (`take-to-production`); one design system in code (`design-the-experience`) | holds |
| resources and options studied, never the first one found, several combined or tried in turn | `choose-with-evidence`; the resource table (`start-from-an-idea`) | holds |
| nothing is impossible; money never stops a project; continuous optimisation | the integrity check refuses project-ending language; course changes; a budget that runs out pauses the run, not the project; `keep-it-on-course` ranks the next improvements for good | holds |
| departments working in tandem, each part of the product | every area founded with an owner, a deliverable and a measure, threaded through the journeys | holds |
| agents and harnesses differ; tools built when stock ones do not fit | routing by what an agent may see and what it scored; missing tools built into the repository with tests | holds |
| private, proprietary, offline; the internet used without revealing the work | `keep-it-confidential`, local MCP mode, short forms for local models | holds |
| one model and one person; the model builds its own harness; asked once, then no waiting | `run-autonomously`, proved by `harness/conformance.py`; `CHOICES.md` with overrides; gates, sandbox, checkpoints, standing limits | holds |
| usable by any agent, and found by search engines and chatbots | `llms.txt`, the discovery index, the plugin, the MCP server, structured data | holds |
| software and hardware | `act-on-the-physical-world`; devices in design, release and incidents | holds |
| a real model and a real person through the whole path | not run in these sessions: no model runtime here | skipped |
| commits authored by the owner alone | every commit on the branch is by melbinjp, with no co-author lines | holds |

18 requests: 17 holds, 0 broken, 1 skipped.

## Removed

The plugin's 27 slash commands, which Claude Code loaded as a second copy of every skill. Turbo and two Google Fonts (three requests to other origins, for a static site). `copy.js`, folded into the one script. Two unused layouts and the empty Commands page. Fifty layout-less `plugin/` pages from the site and its sitemap (84 URLs to 35). The pull-request path filter, which let changes to the MCP server skip CI. From the home page's first screen, the third copy of "Browse the skills"; and from its core-skill cards, all but the first sentence of each description (the full text is on the skills page), so each card reads at a glance on a phone.

## Refused

A ready-made agent harness: the model builds its own from the specification in `run-autonomously`, and the library supplies the test it must pass, not the harness. Asking the person before each action: an autonomous build is made safe by a sandbox, checkpoints and standing limits, and correct by gates. A step that decides whether an idea deserves to be built, and conditions that end a project. The first version of the lifecycle had both; the library is for making ideas happen, so a constraint gets routes around it and a blocked route gets another. A service to run the lifecycle: two folders in the project and a check in its CI do it, with nothing to host. Renaming the library. The name is where it started, and it is what people already search for; every page says what it is now, and that it is not affiliated with Google. A search box: 36 skills in named groups fit on one page, and the home page now starts from where the reader is. A skill for every discipline: marketing, manufacturing, finance, legal and support each get an area with an owner, a first deliverable and a measure in `start-from-an-idea`, and a method of their own only where the path to production cannot hold without one, as design, release and incidents could not. A JavaScript framework or a build step beyond the one GitHub Pages runs. Moving the site to a different host to serve `SKILL.md` directly: wrapping each file as a plain-text collection document does it on Pages, and the site check proves the bytes.

41 items: 33 holds, 0 broken, 8 skipped.
