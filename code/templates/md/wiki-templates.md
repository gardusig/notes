# 📋 Markdown structure templates

Wiki-first templates for markdown structure and documentation pages.

## 📑 Doc index template

Use numbered lists for navigation blocks. Avoid tables in `Contents`.

```markdown
## Contents

1. **Subfolders**
   1. [child-a/](child-a/) - one-line gloss
2. **Files**
   1. [`README.md`](README.md) - page purpose
```

## 📋 Reference table template

Use tables inside reference sections, not for navigation:

```markdown
| Type / name | Required payload (avg) | Optional (est.) | Notes |
| --- | --- | --- | --- |
| `ExampleDto` | 0.5 KB | +0.2 KB | ... |
```

After the table, call out the largest row and why it matters.

## 📋 Explanation template

```markdown
## Overview
<What this page describes and why it exists>

## When to use
- ...

## Do and do not
- **Do:** ...
- **Do not:** ...

## Related references
- ...
```

## 📌 Related

- [`README.md`](README.md)
- [`diagram-wiki-templates.md`](diagram-wiki-templates.md)
- [`../doc/index.md`](../doc/index.md)
- [`../doc/table.md`](../doc/table.md)
- [`../doc/explanation.md`](../doc/explanation.md)
