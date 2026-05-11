# Pull request orchestration (GitHub CLI)

**Suggested order:** merge latest on the branch (see [`../git/pull-workflow.md`](../git/pull-workflow.md)) → run local **verify** your repo documents → **push** → draft PR text → **`gh pr create`** / **`gh pr edit`**.

**Inventory (optional):** use **[`pr/list-view.md`](pr/list-view.md)** when you need the open PR number, URLs, or **`gh pr diff --stat`**.

**Forks:** set **`gh ... --repo owner/name`** when the default remote is not the PR target (e.g. opening a PR against upstream from a fork clone).

**Do not** run `gh pr create` before you intend the branch to be public and CI-ready.

**PR text:** [`../pr/body-skeleton.md`](../pr/body-skeleton.md), title [`../shared/title.md`](../shared/title.md). **Delta:** [`../git/diff-summary.md`](../git/diff-summary.md).
