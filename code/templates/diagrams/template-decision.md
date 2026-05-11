# Template: decision / when to use (UX or policy)

**Portable copy:** When pasting only the **`mermaid`** block, remove this header and links. Colors: [`palette.md`](palette.md) (`ux*` or `op*`). Rules: [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md).

Copy the **fenced `mermaid` block**. Mark the **recommended** path with the **strongest** fill (`uxH` or `opH`).

```mermaid
flowchart LR
  classDef uxH fill:#4527a0,color:#fff
  classDef ux1 fill:#5e35b1,color:#fff
  classDef ux2 fill:#7e57c2,color:#fff
  classDef uxT fill:#ede7f6,color:#111
  classDef uxOff fill:#eceff1,color:#111
  startQ{"Need real-time?"} -->|yes| pathA["Path A — live"]
  startQ -->|no| pathB["Path B — batch"]
  pathA --> rec["Recommended default"]
  pathB --> alt["Alternative"]
  class rec uxH
  class pathA ux1
  class pathB ux2
  class alt uxOff
  class startQ uxT
```
