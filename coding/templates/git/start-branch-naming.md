# Branch naming (git-only)

Derive **`BRANCH`** from user context. If you need the **live** GitHub issue title, run **`gh issue view N`** (or the web UI) before naming the branch.

1. **Jira** — key `PROJ-123` → `proj-123`; optional short slug from title: `proj-123-add-login`.
2. **GitHub issue (number from user)** — `#42` or `42` → `42` or `42-short-slug` if user supplied slug; do not guess the title without `gh` or a link.
3. **Activity phrase** — kebab-case, lowercase, no spaces: `add user login` → `add-user-login`.
4. Validate branch name (no `..`, `~`, `^`, `:`, spaces).

Then: checkout **`main`** (or your team’s base), **`git pull`** as policy requires, **`git checkout -b "$BRANCH"`**, and **push** when ready (set upstream on first push).
