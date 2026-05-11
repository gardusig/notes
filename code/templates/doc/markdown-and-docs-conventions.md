# Markdown and docs conventions

**Upstream:** [`index.md`](index.md).

Use across **`docs/`**, **wikis**, and **`.cursor/templates`** when you want consistent navigation without external dependencies.

## Indexes (`## Contents`, hub pages)

1. **Lexicographic** order for children (folders then files, or one combined list—**pick one** per repo and stay consistent).
2. **Do not** use markdown **tables** for pure navigation indexes—use **numbered nested lists** instead.
3. Link to the **canonical** source file for each topic (relative paths from the current file).

**Skeleton:** see [`index.md`](index.md).

## Reference tables (data-heavy sections)

1. Use **after** the narrative index—not as the only “contents” for a page.
2. **Sort rows** by the **first column** lexicographically unless another order carries meaning.
3. After the table, add a **short callout** for the **largest** or riskiest row.

**Skeleton:** see [`table.md`](table.md).

## Explanation pages (one topic per page)

1. **What it is** — one short paragraph.
2. **When to use** — bullets or scenarios.
3. **Do and do not** — boundaries for contributors or agents.
4. **Related** — links to other pages in the same repo.

**Skeleton:** see [`explanation.md`](explanation.md).
