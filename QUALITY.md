# The bar for this repository

The conductor and its distribution, held to the conductor's own [quality guidance](conductor/guidance/quality.md).
Update the verdicts when something here changes. Results use the conductor's terms: verified, failed, not
verified.

## The bar

- **The one job:** an agent or a person finds the conductor, loads it whole, and can show that it catches what
  it claims to.
- **Who, on what:** agents of every harness, reading `SKILL.md`, `AGENTS.md` or plain HTTP, online or on a
  machine with no network, including small local models that load one guidance file at a time. People on phones
  from 320 px wide and on desktops, in light and dark, by mouse, touch and keyboard. Hosted by GitHub Pages,
  which builds with Jekyll 3.10 and the old Ruby Sass.
- **Journeys that must never fail:**
  1. An agent given only the domain finds the conductor, gets the whole folder and verifies its digest.
  2. A person finds it and copies, downloads or installs the whole folder.
  3. A maintainer changes `conductor/`, and every generated form follows or CI goes red.
  4. An agent on a machine with no network loads the conductor from a copy.
  5. A saved link to any page or `SKILL.md` address of the retired library lands somewhere useful.
  6. A project that already keeps the older ledger keeps running `check_trace.py`.
- **Never corrupted:** the conductor's text. Every form an agent loads is byte for byte its source.
- **Found:** a person or an assistant searching for Agent Skills lands on the page for the conductor, and a
  shared link shows what it is.
- **Budgets:** stylesheet under 16 KB, script under 8 KB, no web font, preview image under 150 KB, every page
  under 120 KB. No script, stylesheet or font from another origin; only the shared favicon.

## Areas walked

- **Security:** a static site with no input, no cookies and no server. There is no code that runs for a user and no
  dependency to audit; CI actions are pinned to commits. The real exposure is the
  trust root: whatever is on `main` is what every agent that loads the conductor is told to do, so who can push
  to `main` matters more than anything on the site. The digests detect a changed file in transit, not a bad commit.
- **Privacy:** no analytics, cookies or third-party scripts. The shared favicon host sees visitors' addresses.
  Fetching a file from the site tells its host which file someone wanted; installing from a copy tells nobody.
- **Compatibility:** old page and `SKILL.md` addresses redirect or serve a notice; the older ledger check is unchanged.
- **Legal:** MIT. No web font. The name began as prompts for Google's Jules; the site says it is not affiliated
  with Google, in the footer and in its questions.
- **Not applicable:** a content security policy (nothing on the site takes input or runs third-party code; add
  one if that changes), capacity, monitoring and backups (static hosting, and the repository is the data),
  physical safety.

## Verdicts

Checked on the branch that made the conductor the one entry point. CI covers the rows marked CI on every push and
pull request.

| item | evidence | verdict |
|---|---|---|
| every generated form matches `conductor/` | `emit.py --check` across six targets (CI) | verified |
| the archive is the same bytes anywhere | stored zip, fixed times and modes; tests rebuild it in another directory with other file times and compare (CI) | verified |
| agent, from the discovery index | one `archive` entry; the served zip equals the built one, holds exactly the 15 source files at its root (including the optional state-view template), and its digest matches (CI) | verified |
| agent, from `llms.txt` | every file listed with its digest; every link resolves in the built site (CI) | verified |
| a saved link to a retired page or skill address | 41 retired pages redirect, 26 old `SKILL.md` addresses serve a notice, `/workflow.json` serves a notice; checked on a build (CI) | verified |
| the package installs whole | `check_conductor.py` on the repository and on a copied install; mutation tests for broken copies (CI) | verified |
| every fixture can go red | 26 fixtures, each with `defects.json`, an expected report naming every planted defect, and a request (CI) | verified |
| an agent delivers a project | not shown by structural checks; recorded in `docs/trials/runs/status.md` | not verified |
| the ledger check other projects copy | the worked example passes; each of the 29 ways of breaking a ledger fails it by name (CI) | verified |
| a self-built harness | `conformance.py` passes the reference and fails each of 12 broken copies (CI) | verified |
| every page whole and titled | one `<h1>` and a `<title>` on every page (CI) | verified |
| budgets | stylesheet, script, preview image and pages within budget; no web font (CI) | verified |
| a search engine or assistant reading a page | structured data parses on every page; the home page has WebSite and FAQPage, each conductor page a TechArticle naming its file (CI) | verified |
| a link shared in a chat | every page names a 1200 by 630 preview image the site serves (CI) | verified |
| the report on the home page | generated from the fixture's expected report; the generator refuses a total that disagrees with the table | verified |
| CI actions pinned | each pinned to a commit, tag in a comment | verified |
| who can change what agents are told | depends on `main`'s branch protection, which this repository cannot read | not verified |
| Safari and Firefox engines, a real screen reader | not run for this change | not verified |
| the live deployment | checked on a local build with the GitHub Pages image; CI builds with the Pages action | not verified |
| found in search results | a fresh crawl can only be requested by the owner in the search consoles | not verified |
