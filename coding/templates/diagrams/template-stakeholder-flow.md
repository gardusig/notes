# Template: stakeholder / lane flow (service view)

**Portable copy:** When pasting only the **`mermaid`** block, remove this header and links. Colors: [`palette.md`](palette.md) (`op*` spine, `uxOff` / `opOff` for side lanes). Rules: [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md).

Copy the **fenced `mermaid` block**. Keep **one primary story** across subgraphs; **muted** classes for background systems.

```mermaid
flowchart TB
  classDef opH fill:#004d40,color:#fff
  classDef op2 fill:#00897b,color:#fff
  classDef opT fill:#b2dfdb,color:#111
  classDef opOff fill:#eceff1,color:#111
  subgraph cust [Customer]
    need["Need"] --> act["Action"]
  end
  subgraph product [Product]
    ui["Surface"] --> logic["Core flow"]
  end
  subgraph ops [Support]
    ticket["Ticket"] --> resolve["Resolve"]
  end
  need --> ui
  act --> logic
  logic --> opOffNode["Background job"]
  logic --> ticket
  resolve --> act
  class need opH
  class logic op2
  class resolve opT
  class opOffNode opOff
  class ui op2
  class ticket opOff
```
