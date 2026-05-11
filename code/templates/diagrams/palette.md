# Mermaid color palette (copy-paste `classDef` ramps)

**Portable copy:** If you paste only a **`mermaid`** block into another repo, omit the links below. Layout rules: [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md).

This file is the **single table of named ramps** for this pack: **hero** (flashiest / most important), **mid** steps (same hue, gradient), **tail** (light outcome), **muted** (side lanes, legend, “out of scope”).

---

## How to use

1. Pick **one spine** (`A → … → B`). Put the **strongest** fill on the node that must win attention (user “aha”, risk, or primary outcome).
2. Assign **2–5** `classDef` steps along that spine; **middle** nodes should visibly **shift** hue/lightness—not identical boxes.
3. Use **`color:#fff`** on dark fills and **`color:#111`** on light fills for label contrast. Preview in Cursor and GitHub.
4. **Leaf-strong variant** — When the story is **convergent** (“done” at the end of the spine), put the **strongest** token on the **terminal** node and **lighter** tokens on ancestors (**same hue**, walking **toward** the leaf). See [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md) and **UX examples** in [`examples.md`](examples.md).

### Leaf-strong (semantic order, same hex as tables)

Reuse the **`classDef` names** above—only the **`class node …`** assignments change.

| Family | Upstream / prelude (light) | … | **Leaf / outcome (strong)** |
| ------ | -------------------------- | --- | --------------------------- |
| **`ux*`** | `uxOff` or `uxT` for resets / legend | `ux3` → `ux2` → `ux1` | **`uxH`** on merge, publish, or primary “done” moment |
| **`hueGh*`** | `hueGhM` / `hueGh4` for optional / git prelude | `hueGh3` → `hueGh2` → `hueGh1` | **`hueGh0`** on terminal **`gh`** / verify outcome when that is the hero |
| **`op*`** | `opT` / `op3` for early pipeline | `op2` → `op1` | **`opH`** on CI green, approval gate, or the named “all checks passed” node |

---

## Family A — UX / product (`ux*`)

Violet ramp for journeys, usability, and “human moment” diagrams (not git machinery).

| Class   | Role        | Fill      | Label text |
| ------- | ----------- | --------- | ---------- |
| `uxH`   | Hero        | `#4527a0` | `#fff`     |
| `ux1`   | Mid-strong  | `#5e35b1` | `#fff`     |
| `ux2`   | Mid         | `#7e57c2` | `#fff`     |
| `ux3`   | Mid-soft    | `#b39ddb` | `#111`     |
| `uxT`   | Tail/outcome| `#ede7f6` | `#111`     |
| `uxOff` | Muted/side  | `#eceff1` | `#111`     |

**Copy-paste `classDef` block:**

```text
  classDef uxH fill:#4527a0,color:#fff
  classDef ux1 fill:#5e35b1,color:#fff
  classDef ux2 fill:#7e57c2,color:#fff
  classDef ux3 fill:#b39ddb,color:#111
  classDef uxT fill:#ede7f6,color:#111
  classDef uxOff fill:#eceff1,color:#111
```

---

## Family B — Workflow / ops (`op*`)

Teal ramp for hand-offs, SLAs, and operational flows without implying “git green.”

| Class   | Role        | Fill      | Label text |
| ------- | ----------- | --------- | ---------- |
| `opH`   | Hero        | `#004d40` | `#fff`     |
| `op1`   | Mid-strong  | `#00695c` | `#fff`     |
| `op2`   | Mid         | `#00897b` | `#fff`     |
| `op3`   | Mid-soft    | `#4db6ac` | `#111`     |
| `opT`   | Tail/outcome| `#b2dfdb` | `#111`     |
| `opOff` | Muted/side  | `#eceff1` | `#111`     |

**Copy-paste `classDef` block:**

```text
  classDef opH fill:#004d40,color:#fff
  classDef op1 fill:#00695c,color:#fff
  classDef op2 fill:#00897b,color:#fff
  classDef op3 fill:#4db6ac,color:#111
  classDef opT fill:#b2dfdb,color:#111
  classDef opOff fill:#eceff1,color:#111
```

---

## Family C — Dev / git (`hueGh*`)

Green ramp aligned with existing examples; use for toolchain and repo-lifecycle figures.

| Class    | Role | Fill      | Label text |
| -------- | ---- | --------- | ---------- |
| `hueGh0` | **Darkest** — entry **or** leaf (pick **one** story per figure; see **Leaf-strong** above) | `#1b5e20` | `#fff`     |
| `hueGh1` | Mid-strong   | `#2e7d32` | `#fff`     |
| `hueGh2` | Mid          | `#388e3c` | `#fff`     |
| `hueGh3` | Mid-soft     | `#66bb6a` | `#111`     |
| `hueGh4` | Light / near-muted | `#c8e6c9` | `#111`     |
| `hueGhM` | Muted / prelude | `#eceff1` | `#111`     |

**Copy-paste `classDef` block:**

```text
  classDef hueGh0 fill:#1b5e20,color:#fff
  classDef hueGh1 fill:#2e7d32,color:#fff
  classDef hueGh2 fill:#388e3c,color:#fff
  classDef hueGh3 fill:#66bb6a,color:#111
  classDef hueGh4 fill:#c8e6c9,color:#111
  classDef hueGhM fill:#eceff1,color:#111
```

---

## See also

- [`examples.md`](examples.md) — full fenced examples
- [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md) — spine-first and leaf-strong rules
