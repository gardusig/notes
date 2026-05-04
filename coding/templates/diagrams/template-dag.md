# Template: DAG / fan-out (left-right)

**Portable copy:** When pasting only the **`mermaid`** block, remove this header and links. Ramps: [`palette.md`](palette.md). Rules: [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md).

Copy the **fenced `mermaid` block**. Use for delegation graphs with a root and branches.

```mermaid
flowchart LR
  classDef opH fill:#004d40,color:#fff
  classDef op2 fill:#00897b,color:#fff
  classDef opT fill:#b2dfdb,color:#111
  rootSkill[Root skill] --> a[Internal A]
  rootSkill --> b[Internal B]
  b --> c[Internal C]
  class rootSkill opH
  class a op2
  class b op2
  class c opT
```
