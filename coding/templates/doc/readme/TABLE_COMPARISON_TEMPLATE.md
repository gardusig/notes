# Table and comparison matrix template

## 📇 Index

1. [🧭 When to use this pattern](#-when-to-use-this-pattern)
2. [🧱 Workflow (domain first)](#-workflow-domain-first)
3. [🎨 Row vs column emphasis](#-row-vs-column-emphasis)
4. [📋 Copy-paste patterns](#-copy-paste-patterns)
5. [⚠️ Rendering and accessibility](#table-rendering-caveats)
6. [🔗 Related](#-related)

## 🧭 When to use this pattern

- You are comparing **many similar things** (options, vendors, services, tasks, releases).
- The reader must scan **status**, **risk**, or **priority** quickly.
- A single paragraph would hide structure; a table keeps **axes** explicit.

## 🧱 Workflow (domain first)

1. **List entities** — one row per thing being compared (or one column if you transpose; rows are usually easier).
2. **Extract domain** — if items cluster (for example “Cloud”, “On-prem”, “Finance”), add a **Domain** or **Category** column *or* split into one small table per domain. That reduces noise before you add color.
3. **Choose axes** — columns are **attributes** that vary (cost, security, owner, date, status). Drop columns that repeat the same value everywhere.
4. **Fill cells** — short phrases; avoid long prose in cells.
5. **Add emphasis last** — spans or bold **after** the table is structurally correct.

## 🎨 Row vs column emphasis

| Situation | Prefer |
| --- | --- |
| Importance is tied to **one entity** (this vendor, this task, this release) | **Per-row** emphasis: tint the **name**, **status**, or **risk** cell for that row only. |
| Importance is tied to **one attribute** for all entities (“Security”, “Blocker”, “Cost”) | **Per-column** emphasis: use a clear header and/or a **Notes** column; put `<span style="color:…">` in that column’s cells consistently. |
| Both matter | Use a **Domain** column for grouping and keep **status** as the row-level signal. |

Keep emphasis **predictable**: same column means the same kind of signal (for example, only the Status column uses color).

## 📋 Copy-paste patterns

### Plain comparison (no HTML)

| Name | Fit | Cost | Notes |
| --- | --- | --- | --- |
| Option A | | | |
| Option B | | | |

### Status column with color (GitHub-flavored Markdown)

Many GitHub surfaces render inline HTML in table cells. Example:

| Name | Status |
| --- | --- |
| Task A | <span style="color:lightgreen">Done</span> |
| Task B | <span style="color:orange">Pending</span> |

### Domain column + status

| Domain | Name | Status |
| --- | --- | --- |
| Backend | Service X | <span style="color:orange">Pending</span> |
| Frontend | App Y | <span style="color:lightgreen">Done</span> |

<a id="table-rendering-caveats"></a>

## ⚠️ Rendering and accessibility

- **GitHub** (issues, many README views) often renders `<span style="color:…">`. **Cursor or VS Code Markdown preview** may strip or differ — keep **words** (“Done”, “Blocked”) in the cell, not color alone.
- Prefer a **small palette** (for example green / orange / red) and use it **sparingly**.
- Do not encode secrets or personal data in tables you paste into **public** tickets or chats.

## 🔗 Related

- Global table rules: [`STYLE_GUIDE.md`](STYLE_GUIDE.md)
- Templates hub: [`README.md`](README.md)
- Operational pages with an optional mini-table: [`NOTE_TEMPLATE.md`](NOTE_TEMPLATE.md)
