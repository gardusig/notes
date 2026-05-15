# 📋 Template hub (`templates/`)

**Pasteables** for docs, diagrams, PRs, git narratives, GitHub issues, work plans that embed issues, and generic README scaffolds. Copy into **`docs/`**, PR/issue bodies, or any repo’s **`.cursor/templates/`**—no other repository is required. Wiki-style guidance lives directly in **[`gh/wiki-templates.md`](gh/wiki-templates.md)**, **[`plan/wiki-templates.md`](plan/wiki-templates.md)**, and **[`md/`](md/README.md)**.

## 📑 Index

1. **[`diagrams/`](diagrams/README.md)** — Fenced mermaid scaffolds and palette.
2. **[`doc/`](doc/README.md)** — Folder index; page indexes, explanations, reference tables, merge playbook, diagram conventions (pasteable index skeleton in **[`doc/index.md`](doc/index.md)**).
3. **[`doc/readme/`](doc/readme/README.md)** — Generic README, note, archive, comparison-table starters for any repo.
4. **[`doc/wiki/`](doc/wiki/README.md)** — Profile-based wiki stubs (coding, knowledge, **tooling-pack**).
5. **[`fullstack/`](fullstack/README.md)** — Split app layout, FE/BE contracts, study sheets; pairs with `diagrams/`.
6. **[`git/`](git/README.md)** — Commit / range narrative helpers and [full-tree zip backup naming](git/zip-git-project-backup.md).
7. **[`gh/`](gh/README.md)** — GitHub CLI orchestration and issue templates.
8. **[`plan/`](plan/README.md)** — Local markdown plan that embeds a tracked issue.
9. **[`pr/`](pr/README.md)** — PR body skeleton; title rules → **[`shared/title.md`](shared/title.md)**.
10. **[`shared/`](shared/README.md)** — Cross-surface rules (PR + issue **titles**).
11. **[`md/`](md/README.md)** — Wiki-style markdown template guidance (index/table/explanation + diagram pointers).
12. **[`.cursor/README.md`](.cursor/README.md)** — Per-repo `.cursor/` layout, bundles, and `AGENTS.md` pairing.

## 📌 Per-repo `.cursor/` (all-in-one reference)

**Start here** when you want a **recommended layout** for `.cursor/rules`, `.cursor/templates`, hooks, and how that ties to **`AGENTS.md`**:

→ **[`.cursor/README.md`](.cursor/README.md)** — map from this pack to `.cursor/` in any repo, plus **minimal / standard / docs-heavy** copy bundles.

For a shorter **bootstrap** checklist (terminal pin, hygiene), see **[`../craft-issue/maintenance/repo-bootstrap.md`](../craft-issue/maintenance/repo-bootstrap.md)** if you keep notes next to this tree, or copy only the **`.cursor/README.md`** section into your project handbook.

## 📌 Pick by repo archetype

Use **[`.cursor/README.md`](.cursor/README.md)** bundles (**minimal** → **standard** → **docs-heavy**). Rough mapping:

| Archetype | Primary pain | Favor under `templates/` | Start with bundle |
| --- | --- | --- | --- |
| **Wiki / docs-first** | Structure, indexes, cross-links, diagrams in long prose | `doc/wiki/`, `doc/`, `diagrams/`; light `gh/` if issues track doc work | **Docs-heavy** (trim unused wiki profiles) |
| **Full stack app** | FE/BE contracts, boundaries, deploy narrative | `fullstack/`, `diagrams/`, `git/`, `gh/`, `pr/` | **Standard** |
| **Hybrid** (product code + large handbook) | Drift between code and docs | **Standard**, then add **selective** wiki profiles (not the whole tree) | **Standard** + partial **docs-heavy** |

“Minimal” fits thin-`docs/` libs and small tools—see bundle recipes in [`.cursor/README.md`](.cursor/README.md).

---

## 📌 Installing into any repo

Copy the subtree you need. From the directory that **contains** `diagrams/`, `doc/`, `git/`, … (this **`templates/`** root):

```bash
cd /path/to/templates   # folder that contains diagrams/, doc/, …
DEST=/path/to/your/repo/.cursor/templates
mkdir -p "$DEST"
cp -R diagrams doc git gh plan pr shared fullstack "$DEST/" 2>/dev/null || true
# Optionally include md/ if you want wiki-style markdown template guides.
# Trim folders you do not want; see .cursor/README.md for tiered sets.
```

Keep **relative links** inside copied files valid, or use a flat copy and fix links once.

---

## 📌 Copy into another repo (quick)

See **[`.cursor/README.md`](.cursor/README.md)** for tiered **`cp`** recipes. One-liner (readme + diagrams only):

```bash
TARGET=/path/to/your/repo/.cursor/templates
mkdir -p "$TARGET"
cp -R doc/readme "$TARGET/doc/"
mkdir -p "$TARGET/diagrams"
cp -R diagrams/* "$TARGET/diagrams/"
```

After copy, link from the target repo’s root **`README.md`** or **`CONTRIBUTING.md`** to **`.cursor/templates/doc/readme/README.md`** (or your chosen subtree).
