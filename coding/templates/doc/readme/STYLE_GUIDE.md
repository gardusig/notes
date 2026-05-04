# Markdown style guide

## 📇 Index

1. [Scope](#-scope)
2. [Global writing rules (`*.md`)](#-global-writing-rules-md)
3. [README template roles (`README.md`)](#-readme-template-roles-readmemd)
4. [README hub rules (`README.md`)](#-readme-hub-rules-readmemd)
5. [Section and list rules](#-section-and-list-rules)
6. [Table rules](#-table-rules)
7. [Linking and navigation rules](#-linking-and-navigation-rules)
8. [Definition of done](#-definition-of-done)

## Scope

- This guide applies to every markdown file in the repository where you adopt these templates.
- `README.md` files are hubs and follow stricter navigation structure.
- Non-README notes are usage-first operational or reference pages.

## Global writing rules (`*.md`)

- Use simple, clear, slightly formal language.
- Use emoji in section titles (`##`, `###`) for scanability.
- Start with one `#` title that states the file purpose.
- Keep instructions actionable and specific.
- Prefer concise paragraphs and explicit next actions.
- For non-README markdown files, this style guide is authoritative; template choice is secondary.

## README template roles (`README.md`)

- Use [`README_ROOT_TEMPLATE.md`](README_ROOT_TEMPLATE.md) for the repository root `README.md`.
- Use [`README_HUB_TEMPLATE.md`](README_HUB_TEMPLATE.md) for generic non-root folder hubs.
- Use [`README_LEAF_TEMPLATE.md`](README_LEAF_TEMPLATE.md) for compact deep/leaf folders.
- Use [`ARCHIVE_README_TEMPLATE.md`](ARCHIVE_README_TEMPLATE.md) for archive-heavy folders with year/entity buckets.

## README hub rules (`README.md`)

- Follow this order:
  1. `#` title
  2. `## 📇 Index` with ordered links
  3. `## 🗺️ Diagram` (navigation diagram; usually Mermaid)
  4. Main hub sections
  5. `## 🔗 Related` as the final section
- README should answer:
  - what exists in this folder
  - when to open each child file or folder
  - where to go next for common reader intents

## Section and list rules

- Ordered lists (`1.`, `2.`) for sequence, priority, or procedures.
- Bullets (`-`) for unordered facts and options.
- Keep nested list depth to 3 levels max.
- For non-README files, include early:
  - `## 🧭 When to use this file`
  - `## 🔄 When to update this file`

## Table rules

- Use tables for:
  - comparisons
  - options with trade-offs
  - structured objects (category, status, owner, amount, date)
- Avoid tables for long prose.
- For **many similar rows** or comparison matrices, define **domain or category** first (column or grouped sections), then add columns for varying attributes. See [`TABLE_COMPARISON_TEMPLATE.md`](TABLE_COMPARISON_TEMPLATE.md).
- Put **visual emphasis** (for example `<span style="color:…">`) in a **consistent** place—usually one **column** (status, risk) or the **name** cell per row—not scattered random cells.

## Linking and navigation rules

- Prefer relative links.
- Keep one source of truth per concept and point other files to it.
- End files with `## 🔗 Related` when cross-navigation helps.
- Hubs should include reciprocal links to sibling hubs.

## Definition of done

1. Structure matches this guide.
2. Index links work.
3. README has diagram after index.
4. Related section is last in README.
5. Language is simple and clear.
6. Correct README template role was used (root, hub, leaf, or archive).
