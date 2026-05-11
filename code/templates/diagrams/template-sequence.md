# Template: sequence diagram

**Portable copy:** When pasting only the **`mermaid`** block, remove this header and links. (`sequenceDiagram` uses participant styling—not `classDef` in all renderers.) Rules: [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md).

Copy the **fenced `mermaid` block** into your doc. Rename participants and messages.

```mermaid
sequenceDiagram
  participant U as UserOrClient
  participant P as PublicSkill
  participant I as InternalBatch
  U->>P: invoke
  P->>I: delegate
  I-->>P: result
  P-->>U: report
```
