# Skeleton: data table (reference section only)

**Conventions:** [`markdown-and-docs-conventions.md`](markdown-and-docs-conventions.md)

Use **inside** a **`docs/`** page **after** the index—**never** as the **Contents** list. **Sort rows** by the **first column lexicographically**. After the table, add a **short callout** for the **largest** row(s).

## When to use

- Many sibling **types** (DTOs, models, messages, config keys) where **per-row size or cost** helps reviewers.

## Column pattern (adapt labels)

| Type / name | Required payload (avg) | Optional (est.) | Notes |
| --- | --- | --- | --- |
| `ExampleDto` | 0.5 KB | +0.2 KB | … |

**Largest:** *Name* — *metric* — *why it matters (hot path, cache, etc.)*

**Summary (optional):** Required fields dominate *X*; optional add *Y* on average—*caveat about double-counting*.

**More detail:** [`markdown-and-docs-conventions.md`](markdown-and-docs-conventions.md).
