# Git diff summary (commit message or PR prep)

Reusable shape for summarizing **`git diff`** or **`$BASE_GIT..HEAD`** before writing a **commit message** or **PR body**.

---

## Steps (human or agent)

1. **Inventory** — List changed **areas** (top-level dirs or subsystems), not every file, unless the branch is tiny. Run **`git diff --name-status "$BASE_GIT...HEAD"`** and group by concern.
2. **Themes** — From **`git log --oneline "$BASE_GIT..HEAD"`**, group into **2–5 bullets** (what readers must know).
3. **Risk** — One line: **merge risk**, **behavior change**, or **none**.
4. **Omit** — Noise renames, generated lockfile-only churn unless that *is* the story.

---

## Shell recipes (PR delta)

Use **`$BASE_GIT`** and **`HEAD`**. **Two-dot** for commits, **three-dot** for file list.

```bash
git log --oneline "$BASE_GIT..HEAD"
```

```bash
git diff --name-status "$BASE_GIT...HEAD"
```

Optional:

```bash
git merge-base --is-ancestor "$BASE_GIT" HEAD
git log --reverse --oneline "$BASE_GIT..HEAD"
```

---

## Commit message skeleton (short)

```
<area>: <imperative outcome>

- <bullet tied to diff>
- <bullet>

Refs: #n
```

Use **50–72** char first line when possible; body wraps at ~72.

---

## Hand-off

- **PR / issue title:** [`../shared/title.md`](../shared/title.md).
- **PR body:** [`../pr/body-skeleton.md`](../pr/body-skeleton.md).
