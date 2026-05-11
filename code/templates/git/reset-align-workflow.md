# Reset current branch to a target ref

Align the **working tree** of the **current branch** to **`$TARGET`** (a remote branch or tag) after fetch. **Confirm** before any **`reset --hard`** or **`git clean`** — data loss is possible.

1. `git fetch --all` (or at least origins needed).
2. Resolve **`$TARGET`** with the user (e.g. `origin/main`, `upstream/main`, a release tag). For forks, prefer the ref your merge policy names as canonical.
3. If the tree is dirty, either **stash**, **commit**, or **discard** per team rules before reset.
4. `git reset --hard "$TARGET"` (or `git checkout "$TARGET" -- .` if your runbook prefers that pattern).
5. **No** `git push` in this snippet unless you intend to update a remote branch (usually **not** for local realign only).
