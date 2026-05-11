# Skeleton: doc page index / navigation

**Conventions:** [`markdown-and-docs-conventions.md`](markdown-and-docs-conventions.md)

Use for **`docs/.../README.md`**, module hub pages, and similar **navigation blocks**. **Do not** use markdown **tables** for pure indexes—**numbered nested lists** only.

---

## Rules (short)

1. **Lexicographic** order for children (folders then files, or one combined list—pick one per repo and stay consistent).
2. **No tables** in **`## Contents`** or **See also** index sections.
3. Link to the **canonical** doc or source file for each entry (adjust relative paths from the current file).

---

## Skeleton

```markdown
## Contents

1. **Subfolders** (lexicographic)
   1. [child-a/](child-a/) — one-line gloss
2. **Files**
   1. [`topic.md`](topic.md) — invocable or reference doc
```

**More detail:** [`markdown-and-docs-conventions.md`](markdown-and-docs-conventions.md).
