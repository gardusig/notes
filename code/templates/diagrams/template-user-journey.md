# Template: user journey (usability / product)

**Portable copy:** When pasting only the **`mermaid`** block, remove this header and links. Colors: [`palette.md`](palette.md) (`ux*` family). Rules: [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md).

Copy the **fenced `mermaid` block** into your doc. Put the **hero** (`uxH`) on the step that must grab attention (first success, pain point, or “aha”).

```mermaid
flowchart TB
  classDef uxH fill:#4527a0,color:#fff
  classDef ux1 fill:#5e35b1,color:#fff
  classDef ux2 fill:#7e57c2,color:#fff
  classDef ux3 fill:#b39ddb,color:#111
  classDef uxT fill:#ede7f6,color:#111
  classDef uxOff fill:#eceff1,color:#111
  discover["Discover"] --> consider["Consider"]
  consider --> firstTry["First try"]
  firstTry --> friction{"Friction?"}
  friction -->|no| value["Value moment"]
  friction -->|yes| recover["Recovery / help"]
  recover --> value
  value --> habit["Repeat / habit"]
  class discover uxH
  class consider ux1
  class firstTry ux2
  class value ux2
  class habit uxT
  class recover uxOff
```
