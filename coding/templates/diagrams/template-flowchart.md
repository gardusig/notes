# Template: flowchart (top-down pipeline)

**Portable copy:** When pasting only the **`mermaid`** block, remove this header and links. Ramps: [`palette.md`](palette.md) (`hueGh*`). Rules: [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md).

Copy the **fenced `mermaid` block below** into a **`docs/`** page or PR body. Replace node labels; keep **`classDef`** and **`class`** in the **same** block.

```mermaid
flowchart TB
  classDef hueGh0 fill:#1b5e20,color:#fff
  classDef hueGh1 fill:#2e7d32,color:#fff
  classDef hueGh2 fill:#388e3c,color:#fff
  classDef hueGh4 fill:#c8e6c9,color:#111
  entryNode["Entry step"] --> midNode["Middle step"]
  midNode --> exitNode["Outcome"]
  class entryNode hueGh0
  class midNode hueGh1
  class exitNode hueGh4
```
