# Per-repo `.cursor/` bundle (reference)

**Upstream:** [`../README.md`](../README.md) (template hub)

This path is **documentation only**: it does **not** duplicate the markdown under [`../`](../). Use it as an **all-in-one map** for what to create under **another repo’s** `.cursor/` so agents, rules, and pasteables stay predictable.

## Purpose

| Goal | How this helps |
| --- | --- |
| **One mental model** for `.cursor/` | Same layout in every project you care about. |
| **Clear split** | **Rules** = always-on behavior; **templates** = optional pasteables (PRs, issues, docs). |
| **No secret sprawl** | Rules and templates reference placeholders; real URLs stay in private notes or team runbooks. |

Paths below name folders **inside the target repo** (e.g. `my-service/.cursor/…`). Sources are **relative to** `code/templates/` in **this** notes repo (sibling folders: `doc/`, `gh/`, …).

---

## Recommended tree (target repo)

```text
.cursor/
├── rules/              # optional: stack guardrails (author per repo)
├── hooks/              # optional: repo-local automation; document each script
└── templates/          # optional: pasteables copied from your template pack
    ├── diagrams/
    ├── doc/
    ├── fullstack/
    ├── git/
    ├── gh/
    ├── md/
    ├── plan/
    ├── pr/
    └── shared/
```

**`AGENTS.md`** at the **repo root** is outside `.cursor/` but pairs with it: build, test, branch naming—see [`../../craft-issue/maintenance/repo-bootstrap.md`](../../craft-issue/maintenance/repo-bootstrap.md).

---

## What goes where

| Location in target repo | Role | Populate how |
| --- | --- | --- |
| **`.cursor/rules/`** | Formatter, test command, “do not edit generated,” security, path-scoped conventions. | **Author per repo** (small files). Not shipped as generic copies from this pack. |
| **`.cursor/hooks/`** | Pre-commit-style or Cursor hook scripts the team agrees on. | Add only with team buy-in; one-line README per hook or a folder README. |
| **`.cursor/templates/`** | Markdown you paste into PRs, issues, plans, or `docs/`. | **Copy** from [`../`](../) using the [bundles](#bundles-minimal--standard--docs-heavy) below. |
| **Root `AGENTS.md`** | Human + model onboarding: install, verify, architecture pointers. | Short; link to README / CONTRIBUTING. |

---

## Map: template pack → `.cursor/templates/`

All sources live under **`code/templates/`** in this notes repo.

| Bundle use | Source (copy recursively or file-wise) | Target under `.cursor/templates/` |
| --- | --- | --- |
| **Titles** (PR + issue) | [`../shared/title.md`](../shared/title.md) | `shared/title.md` (keep `shared/` for imports from other snippets) |
| **Pull requests** | [`../pr/`](../pr/) | `pr/` |
| **GitHub issues** | [`../gh/issues/`](../gh/issues/) | `gh/issues/` |
| **Git narratives / workflows** | [`../git/`](../git/) | `git/` |
| **Plans** (issue-linked work plans) | [`../plan/`](../plan/) | `plan/` |
| **Mermaid + palette** | [`../diagrams/`](../diagrams/) | `diagrams/` |
| **Doc helpers** (index, table, explanation) | [`../doc/index.md`](../doc/index.md), [`../doc/table.md`](../doc/table.md), [`../doc/explanation.md`](../doc/explanation.md) | `doc/` |
| **README / note scaffolds** | [`../doc/readme/`](../doc/readme/README.md) | `doc/readme/` |
| **Full stack + study** | [`../fullstack/`](../fullstack/README.md) | `fullstack/` |
| **Wiki profile stubs** | [`../doc/wiki/`](../doc/wiki/) | `doc/wiki/` (large; copy only profiles you use) |
| **GitHub PR/issue orchestration** (long-form) | [`../gh/pr-orchestration.md`](../gh/pr-orchestration.md), [`../gh/pr/`](../gh/pr/) | `gh/` |
| **Wiki template guides** | [`../md/`](../md/README.md) | `md/` (optional, docs-only guidance) |

After copying, add one line in the target repo **README** or **CONTRIBUTING**: “Pasteables live under `.cursor/templates/`.”

**Wiki vs full stack vs hybrid:** see the **Pick by repo archetype** table in [`../README.md`](../README.md#pick-by-repo-archetype) before choosing a bundle.

---

## Bundles (minimal → standard → docs-heavy)

### Minimal (issues + PRs only)

Good for small libs: fast PR/issue hygiene without doc wiki weight.

```bash
REPO_ROOT=/path/to/target/repo
T="$REPO_ROOT/.cursor/templates"
mkdir -p "$T/pr" "$T/gh/issues" "$T/shared"
cp code/templates/pr/*.md "$T/pr/"
cp code/templates/gh/issues/*.md "$T/gh/issues/"
cp code/templates/shared/title.md "$T/shared/"
```

Adjust `code/templates/` prefix if your clone layout differs.

### Standard (minimal + git + diagrams + readme/doc helpers)

Good default for services you ship from often.

```bash
REPO_ROOT=/path/to/target/repo
T="$REPO_ROOT/.cursor/templates"
# … run minimal block first, then:
mkdir -p "$T/git" "$T/diagrams" "$T/doc/readme"
cp code/templates/git/*.md "$T/git/"
cp -R code/templates/diagrams/* "$T/diagrams/"
cp -R code/templates/doc/readme "$T/doc/"
cp code/templates/doc/index.md code/templates/doc/table.md code/templates/doc/explanation.md code/templates/doc/diagram-conventions.md code/templates/doc/markdown-and-docs-conventions.md code/templates/doc/merge-conflicts-playbook.md "$T/doc/"
mkdir -p "$T/plan"
cp code/templates/plan/*.md "$T/plan/"
cp code/templates/gh/pr-orchestration.md "$T/gh/" 2>/dev/null || true
mkdir -p "$T/gh/pr"
cp code/templates/gh/pr/*.md "$T/gh/pr/" 2>/dev/null || true
mkdir -p "$T/fullstack"
cp code/templates/fullstack/*.md "$T/fullstack/"
```

### Docs-heavy (+ wiki profiles + API stubs)

Copy only the **profiles** you need from [`../doc/wiki/profiles/`](../doc/wiki/profiles/) to avoid noise.

```bash
T="$REPO_ROOT/.cursor/templates"
mkdir -p "$T/doc/wiki"
cp -R code/templates/doc/wiki/* "$T/doc/wiki/"
```

Trim unused profile folders after copy.

---

## Rules of thumb

1. **Prefer small rule files** over one megabyte rule—match [`../../craft-issue/maintenance/repo-bootstrap.md`](../../craft-issue/maintenance/repo-bootstrap.md).
2. **Templates are optional**; rules matter more for consistent agent behavior.
3. **Re-copy after pack updates** if you want parity with [`../README.md`](../README.md).
4. **Do not** put API keys, session cookies, or credential-bearing URLs in `.cursor/`—placeholders only.

---

## See also

- [`../../craft-issue/maintenance/repo-bootstrap.md`](../../craft-issue/maintenance/repo-bootstrap.md) — full `.cursor/` checklist, terminal pin, `AGENTS.md`.
- [`../README.md`](../README.md) — numbered **template areas** and human-oriented index of pasteables.
