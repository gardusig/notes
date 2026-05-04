# `gh pr list` / `gh pr view` — agent checklist

Read-only inventory and inspection. **No** default confirmation prompt unless the user must pick among ambiguous PRs.

**Forks:** set **`--repo owner/name`** when viewing or listing against a different GitHub repo than `origin` (e.g. upstream).

---

## List (current repo)

Open PRs for the **current branch** (same-repo):

```bash
gh pr list --head "$(git branch --show-current)" --state open --json number,title,url --limit 20
```

All open PRs (cap output in chat):

```bash
gh pr list --state open --limit 30
```

---

## View (single PR)

By number:

```bash
gh pr view 42 --json title,body,state,url,headRefName,baseRefName
```

Body to terminal:

```bash
gh pr view 42 --json title,body
```

Optional diff stat:

```bash
gh pr diff 42 --stat
```

---

## Example — input / output

**Input:** “Do I already have a PR from this branch?”

**Commands:**

```bash
BRANCH=$(git branch --show-current)
gh pr list --head "$BRANCH" --base main --state open --json number,title,url
```

**Output (sample JSON line):** `{"number":7,"title":"Add issue label playbook","url":"https://example.com/org/repo/pull/7"}`

---

## Example — view before edit

**Input:** “Show PR 7 title and base.”

```bash
gh pr view 7 --json number,title,baseRefName,headRefName,state
```

Use **`gh pr create`** / **`gh pr edit`** only after the branch is pushed and PR body/title are ready; this file is for **read-only** inspection.
