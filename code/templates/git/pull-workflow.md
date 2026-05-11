# Git pull workflow (merge, no push)

Merge latest from **remotes** into the **current branch** without pushing. **Conflicts:** follow [`../doc/merge-conflicts-playbook.md`](../doc/merge-conflicts-playbook.md).

1. `BRANCH=$(git branch --show-current)` — fail if detached.
2. **Fetch:** `git fetch origin`; if `upstream` remote exists, `git fetch upstream` (or at least `git fetch upstream main` if constrained).
3. **Tracking merge:** if branch has upstream, `git merge "@{u}"` (or `git pull --no-rebase "@{u}"`). On conflict → resolve per playbook; then continue. No upstream → skip.
4. **Canonical main:** set `ROOT_BRANCH` to **`upstream/main`** if remote `upstream` exists, otherwise **`origin/main`**.
5. **Merge root:** `git merge "$ROOT_BRANCH"`. On `main`, prefer `git merge --ff-only "$ROOT_BRANCH"` when applicable. On conflict → playbook.
6. **Stop** — do not `git push` here unless your team’s flow explicitly combines pull and push.

**Do not** re-order fetch before merges. Abort merge: `git merge --abort`.
