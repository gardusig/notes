# `gh issue create` — agent checklist (no duplicate rules)

**Before mutation:** confirm **goal**, **title**, and **body** with the user when the issue is non-trivial or destructive follow-up is possible.

**Steps**

1. **Dedupe (read-only):** search open issues for the same symptom or title keywords (`gh issue list --search "…"`).
2. Draft **title** from [`../../shared/title.md`](../../shared/title.md); **body** from [`body-skeleton.md`](body-skeleton.md). Merge any **repo issue template** your project keeps under **`.github/ISSUE_TEMPLATE/`** if applicable.
3. **Optional labels:** list candidate labels (`gh label list`); create missing labels only after explicit confirm; add **`--label "a,b"`** to **`gh issue create`** when labels are agreed.
4. On proceed: `gh issue create --title "…" --body-file …` (and **`--label`** as above).

**Do not** restate heading/emoji rules here — they live in **`body-skeleton.md`** and **`shared/title.md`**.
