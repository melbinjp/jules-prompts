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
| a schedule date has a source | `test_check_time_limits.py` fails the planted unsourced schedule and passes a sourced one (CI) | verified |
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

## Production-process documentation and factual draft, 8 October 2026

Commission: add every named production-process stage as a README study/build task and prepare
a development article without personal context. Subsequent owner steering requires supported
facts only, with false critiques removed. The native next work is recorded in `docs/VISION.md`.
This package changes documentation; it does not implement the proposed execution system.

| Acceptance item | Performed evidence |
|---|---|
| Complete process inventory | Both arrow inventories contain all 17 source labels once, in their original order; the README has 17 matching evidence rows. |
| Current state and next action | The README distinguishes guidance/checks from missing whole-sequence enforcement and gives a bounded failure/resumption/independent-verification demonstration. VISION carries the next work. |
| Facts-only development account | Dated native project, trial and operating records were read. Unsupported impossibility, probability, session-count, wasted-work and permission-bypass critiques were excluded. Primary research is used only for its supported scope. |
| Personal context removed | Article checks find no private project labels, local paths, secrets or personal operational identifiers in prose. The public Jules project and repository references are intentional. Raw transcripts and private provenance stay outside this repository. |
| Writing correction and publish checks | Final article and changed README section each return exit 0, no findings, from voiceproof correct and check with point/takeaway. No checker changes. |
| Audience Mirror | Final mirror commands return exit 0, no findings and all five publish gates PASS; article grade 12.7, README section 12.3. Independent reader judgment also accepts the draft and its concrete next action. |
| Independent factual/source review | Separate reviewers checked stage coverage, native records, dates, standards claims, privacy and current/proposed distinctions. Security acceptance was narrowed to material risks/missing required evidence; UI wording was narrowed to what browser checks missed. |
| Local artifact integrity | UTF-8/LF, native article front matter, README local links and VISION anchor inspected; current fixture inventory remains 168, historical trial denominator 146; git diff --check passes. The blog tree remains unchanged. |

At the conclusion of draft preparation, the article remained in the workspace's private draft
records and no push or publication had occurred. The owner subsequently authorised push and
publication on 8 October. Existing runtime/fixture behaviour was not changed, so delivery trials
were not rerun for this documentation package.

8 documentation items verified, 0 failed, 0 not verified of 8. Runtime implementation and
real-project acceptance remain separate from the authorised documentation publication.


## Authorised documentation release checks, 8 October 2026

The owner authorised push and publication. The release checkout starts at `d5bacd2` and
changes only README, VISION, RELEASE and this documentation receipt. Canonical guidance,
generated forms, archive, fixtures, scripts and workflows remain byte-identical to that
baseline. The earlier development candidate is separate.

All eleven mandatory checks pass on this exact release source: emitter agreement; library
integrity; conductor references (15 files, 190 local and 181 section references); conductor
mutation tests (18); time-limit tests (10); byte tests (9); trial-preparation tests (3);
inventory mapping (1,825/1,825); trace checks (29 mutations); harness conformance (12 mutations);
and the fresh offline Pages build's site check (62 pages, 144 checks). The installed Pages
image ran without network, with read-only source and a separate fresh output. Source, build
and index agree on archive SHA-256
`3618299c7d97b2dca238126f8aa8966fc42df16207350fc1938c3c8c32694a61`.

The publication article adds the reproducible inventory-count command, links the README
section and states the limit of private historical evidence. Its generated page was inspected
through real-browser using the existing site style. All 17 stages are retained. The writing
checks and independent factual/privacy review pass; publishing requirements does not release
runtime enforcement.

11 release gates verified, 0 failed, 0 not verified of 11. Hosted deployment and served bytes
must be observed after the push; no hosted outcome is inferred from these local gates.
