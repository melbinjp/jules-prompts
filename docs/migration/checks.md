# What happened to every check of the 26-skill library

Each check that guarded the old library is classified as **retained** (same behaviour, same or
adapted code), **replaced** (the behaviour is still protected, by something else) or **retired** (the
thing it protected no longer exists). A check is not kept so that an old check can pass.

The old library is the tag `library-26-final`.

## CI workflow steps (`.github/workflows/library-integrity.yml`)

| Step | Class | Behaviour it protects | Now |
|---|---|---|---|
| Library integrity (`check_library_integrity.py`) | replaced | the pieces of the library agree with each other | rewritten for the conductor and fixtures; see the function table below |
| Conductor check tests (`test_check_conductor.py`) | retained | the package check rejects broken installs and references | unchanged; runs in the same job |
| `emit.py --check` | retained | every generated form is byte for byte its source | source is `conductor/`; targets are skills, plugin, marketplace, index, agent-skills, archive, site, pages, redirects |
| `test_emit_bytes.py` | retained, changed | a CRLF checkout cannot silently invalidate published digests | rewritten (see below) and extended to the archive |
| `test_trial_prep.py` | retained | trial preparation never deletes interrupted evidence | unchanged |
| `inventory_map.py --destinations` | retained | every mapped destination in the coverage map exists | unchanged; it reads the old library from the baseline commit, not the working tree |
| `test_check_trace.py` | retained | `check_trace.py` catches each way of breaking a ledger | unchanged; the harness stays for projects that keep the ledger |
| `test_conformance.py` | retained | the conformance test tells a good harness from a broken one | unchanged |
| Site job: build with `jekyll-build-pages`, then `check_site.py` | retained | the built site serves what it claims | same build; `check_site.py` rewritten (below); PyYAML installed because it now reads the conductor the way `emit.py` does |
| MCP job: `npm ci`, `npm audit`, smoke test, smoke test from a local copy | retained | the server speaks MCP, has no known high vulnerabilities, and refuses the network in local mode | smoke test rewritten (below) |
| (new) `check_conductor.py` as its own step | new | the package is complete and its references resolve, reported on its own | previously only inside library integrity |

Kept as they were: pinned actions, no `continue-on-error`, both operating systems, no path filter.

## `check_library_integrity.py`

| Old check | Class | Behaviour it protected | Now |
|---|---|---|---|
| No prompt files found: refuse to pass | replaced | a check that finds nothing must not pass | same refusal when no conductor files are found |
| Front matter present and valid YAML | replaced | a page must render with its metadata | `check_conductor.py` validates `SKILL.md` front matter (name, description length); `emit.py` refuses a file with no title or first paragraph |
| Required fields `layout title description category type` | retired | Jekyll collection fields of prompt pages | pages are generated with fixed fields by `emit.py`; no hand-written page has them |
| Jules-specific harness text (`FORBIDDEN_IN_PROMPTS`) | retained | the instructions do not depend on one product's tools | same list, applied to every conductor file |
| Skill Template sections (`Objective`, `Context`, and so on) | retired | every skill had the same six sections | there are no skills; the package check requires one title per file and resolvable section references |
| Ends in holds, broken, skipped with a denominator | replaced | every report ends with its counts | the rule is `SKILL.md` section 10; its presence is protected by section-reference validation, and its effect by the fixtures and trials |
| States that it assumes no hosted service (exact phrase) | retained, adapted | a private or offline project never reads a step as needing a hosted service | `SKILL.md` must say so once, in the file read first |
| Prompt layout is `skill` | retired | prompt pages had a title and install panel | page layout is set by the emitter |
| Bare `\|` in a list item | retained | kramdown renders it as a table | applied to conductor files, outside code fences |
| `_config.yml` parses | retained | Jekyll can build | unchanged |
| `_data/*.yml` parses | retained | Jekyll can build (the FAQ had an unquoted colon; it caught mine again while writing this) | unchanged |
| `workflow.json` steps exist, have gates, are ordered, branches exist | retired | the eleven-step path was consistent | the file is removed; the path became the control loop, which `check_conductor.py` validates as text |
| Workflow entries start on the path, have notes; an existing project starts by being founded again on paper | retired | every project state had a way in | replaced by `SKILL.md` section 1 (an existing project's records are written first); no structural check remains, the behaviour is exercised by the fixtures and trials |
| `throughout` names real skills | retired | as above | as above |
| `skills/` agrees with `_prompts/` (`generate_skills.check`) | replaced | the Agent Skills copy is not drifted | `emit.py --check`, target `skills`, now an exact copy of `conductor/` |
| Fixture index entries have directories, `defects.json`, `EXPECTED_REPORT.md` | retained | a fixture is scorable | unchanged |
| Index skill equals `defects.json` skill; skill is a generated skill | retired | fixtures belonged to skills | the `skill` field is provenance only |
| Expected report names every planted defect, invents none | retained | a fixture can fail | unchanged |
| Every fixture on disk is in the index | retained | no orphan fixture | unchanged |
| Every skill has a fixture | replaced | nothing was unseen to fail | every fixture has a request in `requests.json`, none is extra, and `planted` in the index equals `defects.json` |
| Conductor package check | retained | package complete | unchanged |
| (new) retired paths are absent | new | two sources of truth do not return | `_prompts`, `workflow.json`, `compact`, `generate_skills.py` |
| (new) `docs/RELEASE.md` has its four sections | new | the release statement exists | headings only; the content is reviewed |

## `check_site.py`

| Old check | Class | Now |
|---|---|---|
| Discovery index served, `$schema` correct | retained | unchanged |
| Every skill in the index is served, equals `skills/<name>/SKILL.md`, digest matches; every procedure has an entry; no entry for a non-procedure | replaced | exactly one entry, `conductor`, of type `archive`; the served archive equals the one built from `conductor/`, has its digest, holds exactly the files of `conductor/` at its root with no unsafe paths; every file is also served byte for byte |
| `llms.txt` served, lists every skill, every link resolves | retained, adapted | lists every file, states the archive and `SKILL.md` digests, every link resolves |
| Page is whole, has a title and one `<h1>`; loads nothing from another origin; under the page budget | retained | unchanged |
| `og:image` is served and 1200 by 630; structured data parses; home page has WebSite and FAQPage | retained | unchanged |
| Skill page: `<h1>` equals title, no extra tables, points at its `SKILL.md`, TechArticle names title and `SKILL.md` | replaced | the same checks on every `/conductor/` page, against the file it shows |
| Budgets (stylesheet, script, image), no web font | retained | unchanged |
| (new) every retired page is served and redirects to a page that exists; every old skill `SKILL.md` address serves a notice naming the conductor and the guidance file that holds its content; `/workflow.json` is a notice; none of them in the sitemap; the sitemap has the conductor | new | protects saved links |

## `mcp/smoke-test.mjs`

| Old check | Class | Now |
|---|---|---|
| Prompts capability declared | retained | plus the resources capability |
| Every procedure in the index is served | replaced | every file in `library.json` is served as a prompt, by name |
| Local copy served with no network | retained | unchanged |
| A prompt exposes a placeholder; the argument is substituted; body is not front matter | replaced | the conductor has no placeholders, so substitution is retired. Replaced by: the `conductor` prompt is `SKILL.md` without front matter, every guidance and template prompt equals its file, resources list and read, and an unknown prompt is refused |
| Coverage on stderr | retained | text updated |

## `test_emit_bytes.py`

Its expectation changed, and only because its subject did. It used to take a generated `SKILL.md` from
`generate_skills.planned()`; that function no longer exists. The CRLF test now uses the conductor's own
`SKILL.md` through `emit.write`, and the digest expectation is unchanged in kind. The second test (the
skill generator itself) is retired with the generator. Added: an archive that is rejected when altered and
repaired by regeneration, and a conductor with CR characters that is refused. Also the archive identical across
builds, file times and checkout location, its layout, the index digest equal to the served archive, and the
served `SKILL.md` equal to the source.

## Scripts removed

| Removed | Why | Search before removal |
|---|---|---|
| `scripts/generate_skills.py` | wrote `skills/` from `_prompts/`; `emit.py` writes `skills/` from `conductor/` | used only by `emit.py`, `check_library_integrity.py` and `test_emit_bytes.py`, all rewritten |
| `emit.py` function `emit_compact` and the `compact` target | short forms of 26 skills; the conductor says how to load one guidance file at a time | `compact/` was referenced only by docs and the site exclude list |
| `emit.py` workflow renderers and the skills-page groups | rendered `workflow.json` and the skill list | inputs no longer exist |

Kept though they may look old: `scripts/reference_agent.py` (used by `test_conformance.py`),
`scripts/score_fixture.py` (every fixture), `scripts/og-image.html` (makes `assets/og.png`),
`scripts/inventory_map.py` (coverage map).

## Files removed

`_prompts/` (26 skills and the template), `workflow.json`, `compact/` (26 short forms and its README),
`tasks.html`, `workflow.html` (now generated redirects), `_layouts/skill.html`, `_includes/entry-states.html`,
`path-steps.html`, `skill-groups.html`, `workflow-lede.html`, `workflow-steps.html`, and the generated
`skills/<name>/`, `plugin/skills/<name>/` and `_agent_skills/<name>.txt` of the 26 skills. All are in
`library-26-final`.
