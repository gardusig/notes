# README + folder scaffold

Use this when **adding a new subtree** or **normalizing** an existing folder so every level has the right `README.md` shape and navigation stays predictable.

## 📇 Index

1. [🎯 Purpose](#scaffold-purpose)
2. [📁 Folder conventions](#scaffold-folder-conventions)
3. [🧭 Template pick matrix](#scaffold-template-pick-matrix)
4. [🧱 Minimum heading contract](#scaffold-minimum-heading-contract)
5. [🧪 Worked example (generic)](#scaffold-worked-example-generic)
6. [🗺️ Reference shape](#scaffold-reference-shape)
7. [🔗 Related](#scaffold-related)

<a id="scaffold-purpose"></a>

## 🎯 Purpose

- Pick the correct README template **before** creating files.
- Create folders and READMEs in an order that keeps **parent links** valid from day one.
- When reshaping a tree, use [`README_TEMPLATE_MERGE_PLAYBOOK.md`](README_TEMPLATE_MERGE_PLAYBOOK.md) so human-owned content is not wiped by structural refresh.

<a id="scaffold-folder-conventions"></a>

## 📁 Folder conventions

- If humans navigate the directory as a **hub** (multiple children, “where do I go next?”), add **`README.md`** at that level.
- **Small** folders with few artifacts can stay a **leaf** hub ([`README_LEAF_TEMPLATE.md`](README_LEAF_TEMPLATE.md)); if the folder grows tables, routers, or many children, **promote** it to a full hub ([`README_HUB_TEMPLATE.md`](README_HUB_TEMPLATE.md)).
- **Year or entity buckets** under evidence-style trees use [`ARCHIVE_README_TEMPLATE.md`](ARCHIVE_README_TEMPLATE.md) at the archive hub.
- Non-README operational pages use [`NOTE_TEMPLATE.md`](NOTE_TEMPLATE.md); authoritative prose rules live in [`STYLE_GUIDE.md`](STYLE_GUIDE.md).
- Prefer **relative** links; each concept should have **one** canonical file—others link to it.

<a id="scaffold-template-pick-matrix"></a>

## 🧭 Template pick matrix

| If you are writing… | Use | Typical child folders or files |
| --- | --- | --- |
| Repository root `README.md` | [`README_ROOT_TEMPLATE.md`](README_ROOT_TEMPLATE.md) | `docs/`, `src/`, top-level modules |
| Non-root folder hub `README.md` | [`README_HUB_TEMPLATE.md`](README_HUB_TEMPLATE.md) | Thematic subfolders each with `README.md` or key `*.md` leaves |
| Compact deep folder `README.md` | [`README_LEAF_TEMPLATE.md`](README_LEAF_TEMPLATE.md) | A handful of files; short contents table |
| Archive hub (years or entities) | [`ARCHIVE_README_TEMPLATE.md`](ARCHIVE_README_TEMPLATE.md) | `2024/`, `2025/`, entity buckets |
| Operational or reference `*.md` (not README) | [`NOTE_TEMPLATE.md`](NOTE_TEMPLATE.md) | N/A (file sits beside README or under a runbook path) |

<a id="scaffold-minimum-heading-contract"></a>

## 🧱 Minimum heading contract

Section **order** for README hubs follows [`STYLE_GUIDE.md`](STYLE_GUIDE.md) (Index → Diagram → body → Related last). When fixing a broken README, **restore missing** blocks from the template for its role.

| Role | Minimum `##` sections (from templates) |
| --- | --- |
| **Root** | Index; About; Diagram; Quick start; Project layout; Contributing or support; Related |
| **Hub** | Index; Folder summary; Diagram; Where to open what; Folder map; Related |
| **Leaf** | Index; Scope; Contents; Usage notes; Related |
| **Archive** | Index; Diagram; When to open this archive; Contents summary; Maintenance rules; Related |

Root READMEs may add extra subsections when the project needs them; keep **Index**, **Diagram**, and **Related** coherent with [`STYLE_GUIDE.md`](STYLE_GUIDE.md).

<a id="scaffold-worked-example-generic"></a>

## 🧪 Worked example (generic)

**Goal:** new area `area/` with a topic subfolder and one runbook file.

**Target tree (text):**

```text
area/
  README.md              ← hub (parent-facing)
  topic/
    README.md            ← leaf or small hub
    runbook.md           ← NOTE_TEMPLATE page (optional)
```

**Creation order**

1. Create `area/` and `area/README.md` from [`README_HUB_TEMPLATE.md`](README_HUB_TEMPLATE.md) (stub links to `topic/README.md`).
2. Create `area/topic/` and `area/topic/README.md` from [`README_LEAF_TEMPLATE.md`](README_LEAF_TEMPLATE.md) (or hub template if you already know it will sprawl).
3. Add `area/topic/runbook.md` from [`NOTE_TEMPLATE.md`](NOTE_TEMPLATE.md) if needed; link it from `area/topic/README.md` and, if important, from `area/README.md`.
4. Update **parent** `README.md` folder map and diagram when children change.

<a id="scaffold-reference-shape"></a>

## 🗺️ Reference shape

For a **multi-layer documentation** tree with a single entrypoint and nested hubs, mirror the **layout** (not necessarily the prose) of a mature open-source repo: root `README.md` → `docs/README.md` → topic hubs, each with Index, optional diagram, and Related.

<a id="scaffold-related"></a>

## 🔗 Related

- [`README.md`](README.md) (template index)
- [`STYLE_GUIDE.md`](STYLE_GUIDE.md)
- [`README_TEMPLATE_MERGE_PLAYBOOK.md`](README_TEMPLATE_MERGE_PLAYBOOK.md)
