# README template merge playbook

Use this when **re-applying** a README template to an existing file: refresh structure and navigation **without** discarding scores, facts, or curated bullets unless the task explicitly changes them.

## 📇 Index

1. [🧭 When to use this](#merge-when-to-use-this)
2. [🎯 Classify the target README](#merge-classify-the-target-readme)
3. [📋 Inventory pass](#merge-inventory-pass)
4. [🧱 Structure-owned vs content-owned](#merge-structure-owned-vs-content-owned)
5. [🔁 Merge algorithm](#merge-algorithm)
6. [🏷️ Optional region markers](#merge-optional-region-markers)
7. [✅ Definition of done](#merge-definition-of-done)
8. [🔗 Related](#merge-related)

<a id="merge-when-to-use-this"></a>

## 🧭 When to use this

- A hub `README.md` drifted: missing Index, diagram in the wrong place, or Related not last.
- You are **bulk-refreshing** navigation after moving folders.
- An agent prompt says “normalize to template” and you still need **today’s tables** to survive.

<a id="merge-classify-the-target-readme"></a>

## 🎯 Classify the target README

Pick **one** canonical template ([`README.md`](README.md) selection table):

| Role | Canonical template |
| --- | --- |
| Repo root | [`README_ROOT_TEMPLATE.md`](README_ROOT_TEMPLATE.md) |
| Non-root hub | [`README_HUB_TEMPLATE.md`](README_HUB_TEMPLATE.md) |
| Deep leaf | [`README_LEAF_TEMPLATE.md`](README_LEAF_TEMPLATE.md) |
| Archive hub | [`ARCHIVE_README_TEMPLATE.md`](ARCHIVE_README_TEMPLATE.md) |

If the folder outgrew “leaf,” switch role to **hub** or **archive** first, then merge.

<a id="merge-inventory-pass"></a>

## 📋 Inventory pass

1. List every `##` and `###` heading in the live file **in order**.
2. Note any **explicit anchors** (`<a id="..."></a>`) or stable slug links used elsewhere; **keep** those ids if anything still links to them.
3. Note tables whose **cells** hold live state (scores, budgets, names of current files)—treat as **content-owned**.

<a id="merge-structure-owned-vs-content-owned"></a>

## 🧱 Structure-owned vs content-owned

**Structure-owned** (take from the current template version; restore if missing)

- Section **titles** and **order** required by [`STYLE_GUIDE.md`](STYLE_GUIDE.md): `#` title → `## 📇 Index` → `## 🗺️ Diagram` → main sections → `## 🔗 Related` last.
- Empty **shell** tables: header rows and column names for router or folder map or “where to open what,” including placeholder rows you will repoint to real paths.
- **Diagram** fence and placeholder graph shape (update node labels to match real children).
- Index entries for each major `##` section.

**Content-owned** (copy forward from the live file unless the task edits that content)

- All **filled** table cells: metrics, anchors, release names, narrative bullets under “About” or “Current situation,” curated “folder summary” bullets.
- Extra subsections the tree accumulated **inside** an allowed region—keep unless they contradict the template contract in [`README_AND_FOLDER_SCAFFOLD.md`](README_AND_FOLDER_SCAFFOLD.md).
- Warnings, dates, and one-off notes that are not in the blank template.

**Role-specific quick map**

| Role | Structure-owned highlights | Content-owned highlights |
| --- | --- | --- |
| **Root** | About or overview block; diagram; project layout **columns** | Install commands; badge rows; layout table descriptions; support links |
| **Hub** | “Where to open what” table shape; folder map grid; diagram | Folder summary bullets; cell targets and descriptions |
| **Leaf** | Contents table columns | Each row’s notes; scope bullets |
| **Archive** | Maintenance rules; diagram buckets | Child bucket list; “when to open” nuance |

<a id="merge-algorithm"></a>

## 🔁 Merge algorithm

1. Open the **canonical template** for the classified role side-by-side with the **live** README.
2. **Restore** any missing structure-owned sections from the template (insert at the correct position per [`STYLE_GUIDE.md`](STYLE_GUIDE.md)).
3. For each structure-owned **table**, copy **header row** from template; then **merge** body rows: keep live rows; add template placeholder rows only for **new** children that exist on disk but lack a row.
4. **Re-order** sections only to match the hub rules; do not reorder Related above main body.
5. For every content-owned paragraph or cell: **preserve** unless the user story explicitly changes that fact.
6. Update **relative links** and Index anchors after moves; grep for old paths if needed.
7. Final pass: Index links resolve; diagram renders; Related is last.

<a id="merge-optional-region-markers"></a>

## 🏷️ Optional region markers

For READMEs that are **regenerated often**, you may wrap blocks so humans and tools know what may be overwritten.

Suggested pattern (HTML comments, invisible in rendered Markdown):

```markdown
<!-- template:structure:start name="folder-map" -->
## Folder map
| Entry | What it contains |
| --- | --- |
<!-- template:structure:end -->

<!-- template:content:start name="folder-map-rows" -->
| `./topic/` | … |
<!-- template:content:end -->
```

Rules:

- **Structure** regions: headings and table headers copied from templates; safe to replace wholesale when templates evolve.
- **Content** regions: user narrative and filled rows; never cleared unless the editor intends to.
- Keep region names **stable** (`slug-case`). Do not nest regions across heading boundaries.

Markers are optional tooling for high-churn files.

<a id="merge-definition-of-done"></a>

## ✅ Definition of done

1. Role matches one template; section order matches [`STYLE_GUIDE.md`](STYLE_GUIDE.md).
2. No accidental blanking of content-owned tables or bullets.
3. Stable `<a id="...">` preserved where still linked.
4. Index and Related links valid.

<a id="merge-related"></a>

## 🔗 Related

- [`README_AND_FOLDER_SCAFFOLD.md`](README_AND_FOLDER_SCAFFOLD.md)
- [`README.md`](README.md) (template index)
- [`STYLE_GUIDE.md`](STYLE_GUIDE.md)
