# Commit and push (after local review)

Use after **format, lint, and tests** pass (or whatever your repo documents). **Confirm** with a human or your team’s checklist before **`git commit`** / **`git push`** when the change is large or destructive.

1. `BRANCH=$(git branch --show-current)` — fail if detached.
2. Stage: prefer `git add <paths>`; `git add .` only when appropriate.
3. Show `git status --short`, `git diff --stat`, one-line commit subject; get explicit **Proceed** before `git commit` / `git push` when policy requires it.
4. `git commit -m "…"` when index has staged changes.
5. **Push:** if ahead of `@{u}` → `git push`; if no upstream → `git push -u origin "$BRANCH"`.
6. Remove ephemeral scratch dirs the agent created this run if your conventions say so.

**Never** push secrets, credentials, or large generated artifacts your `.gitignore` is meant to exclude.
