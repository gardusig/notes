# Merge conflict playbook (after `git merge` / `git pull`)

Use when a merge stops with **conflicted** files. Adapt to your team’s review rules.

1. **See state:** `git status` — note **both modified** and **deleted by us/them** paths.
2. **Open each conflicted file** — search for `<<<<<<<`, `=======`, `>>>>>>>`.
3. **Resolve** — keep the correct combined code; **remove all conflict markers**.
4. **Stage:** `git add <path>` for each fixed file (including deletes you intend to keep).
5. **Continue:** `git merge --continue` (or `git commit` if merge commit message editor opens). If you must abort: `git merge --abort`.
6. **Run tests** your repo expects before pushing.
