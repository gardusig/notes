# Template hub (`templates/`)

**Pasteables** for docs, diagrams, PRs, git narratives, GitHub issues, work plans that embed issues, and generic README scaffolds. Copy into **`docs/`**, PR/issue bodies, or any repo’s **`.cursor/templates/`**—no other repository is required.

## Per-repo `.cursor/` (all-in-one reference)

**Start here** when you want a **recommended layout** for `.cursor/rules`, `.cursor/templates`, hooks, and how that ties to **`AGENTS.md`**:

→ **[`.cursor/README.md`](.cursor/README.md)** — map from this pack to `.cursor/` in any repo, plus **minimal / standard / docs-heavy** copy bundles.

For a shorter **bootstrap** checklist (terminal pin, hygiene), see **[`../repo-bootstrap.md`](../repo-bootstrap.md)** if you keep notes next to this tree, or copy only the **`.cursor/README.md`** section into your project handbook.

---

## Installing into any repo

Copy the subtree you need. From the directory that **contains** `diagrams/`, `doc/`, `git/`, … (this **`templates/`** root):

```bash
cd /path/to/templates   # folder that contains diagrams/, doc/, …
DEST=/path/to/your/repo/.cursor/templates
mkdir -p "$DEST"
cp -R diagrams doc git gh plan pr shared fullstack "$DEST/" 2>/dev/null || true
# Trim folders you do not want; see .cursor/README.md for tiered sets.
```

Keep **relative links** inside copied files valid, or use a flat copy and fix links once.

---

## Template areas

1. **[`diagrams/`](diagrams/README.md)** — Fenced mermaid scaffolds and palette.
2. **[`doc/`](doc/index.md)** — Page indexes, explanations, reference tables, merge playbook, diagram conventions.
3. **[`doc/readme/`](doc/readme/README.md)** — Generic README, note, archive, comparison-table starters for any repo.
4. **[`doc/wiki/`](doc/wiki/)** — Profile-based wiki stubs (coding, knowledge, **tooling-pack**).
5. **[`fullstack/`](fullstack/README.md)** — Split app layout, FE/BE contracts, study sheets; pairs with `diagrams/`.
6. **[`git/`](git/diff-summary.md)** — Commit / range narrative helpers and [full-tree zip backup naming](git/zip-git-project-backup.md).
7. **[`gh/`](gh/pr-orchestration.md)** — GitHub CLI orchestration and issue templates.
8. **[`plan/`](plan/work-plan-with-issue.md)** — Local markdown plan that embeds a tracked issue.
9. **[`pr/`](pr/body-skeleton.md)** — PR body skeleton; title rules → **[`shared/title.md`](shared/title.md)**.
10. **[`shared/`](shared/title.md)** — Cross-surface rules (PR + issue **titles**).

---

## Copy into another repo (quick)

See **[`.cursor/README.md`](.cursor/README.md)** for tiered **`cp`** recipes. One-liner (readme + diagrams only):

```bash
TARGET=/path/to/your/repo/.cursor/templates
mkdir -p "$TARGET"
cp -R doc/readme "$TARGET/doc/"
mkdir -p "$TARGET/diagrams"
cp -R diagrams/* "$TARGET/diagrams/"
```

After copy, link from the target repo’s root **`README.md`** or **`CONTRIBUTING.md`** to **`.cursor/templates/doc/readme/README.md`** (or your chosen subtree).

---

## Related

- **Per-repo Cursor layout:** [`.cursor/README.md`](.cursor/README.md).
