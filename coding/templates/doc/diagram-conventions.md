# Diagram conventions (mermaid)

**Upstream:** [`index.md`](index.md).

Portable rules for **flowcharts**, **subgraphs**, and **`classDef`** colors. **Copy** with your diagrams into any repo.

## Spine

- Pick **one primary path** (user journey, request lifecycle, or pipeline). Readers should see the story in **one glance**.
- Put the **most important** outcome on a **strong** node (see ramps in [`../diagrams/palette.md`](../diagrams/palette.md)).

## Leaf-strong variant

When the story **ends** at a clear outcome (merge, deploy, “done”):

- Put the **strongest** `classDef` on the **terminal** node.
- Use **lighter** fills on **ancestors** along the same hue so the eye walks **toward** the leaf.

## Examples

- Full fenced samples: [`../diagrams/examples.md`](../diagrams/examples.md).
- Template list: [`../diagrams/README.md`](../diagrams/README.md).

## Preview

Validate in **Cursor markdown preview** and your **GitHub** (or docs site) renderer—`classDef` support varies slightly by diagram type (e.g. some **`sequenceDiagram`** styling is limited).
