# Diagram examples (Mermaid only)

**Portable copy:** Paste only the fenced **`mermaid`** blocks elsewhere; drop links if the path breaks.

Small **reference figures**—copy a block into your **`docs/`** page. **No** separate render step; preview in Cursor or GitHub. Ramps: [`palette.md`](palette.md). Conventions: [`../doc/diagram-conventions.md`](../doc/diagram-conventions.md).

## UX ramp (`ux*` family — product / usability, **entry-strong**)

Hero on the **first** step; lighter toward **Done** (use **UX leaf-strong** below when the outcome should win).

```mermaid
flowchart TB
  classDef uxH fill:#4527a0,color:#fff
  classDef ux1 fill:#5e35b1,color:#fff
  classDef ux2 fill:#7e57c2,color:#fff
  classDef ux3 fill:#b39ddb,color:#111
  classDef uxT fill:#ede7f6,color:#111
  discover["Discover"] --> tryIt["Try"]
  tryIt --> valueMoment["Value moment"]
  valueMoment --> done["Done"]
  class discover uxH
  class tryIt ux1
  class valueMoment ux2
  class done uxT
```

## Spine with RGB ramp (three nodes)

```mermaid
flowchart LR
  classDef spineA fill:rgb(27,94,32),color:#fff
  classDef spineMid fill:rgb(56,142,60),color:#fff
  classDef spineB fill:rgb(200,230,201),color:#111
  nodeA[Branch created] --> nodeMid[Push + CI] --> nodeB[Review green]
  class nodeA spineA
  class nodeMid spineMid
  class nodeB spineB
```

## Green ramp (hex fills, **leaf-strong**)

```mermaid
flowchart LR
  classDef hueGh0 fill:#1b5e20,color:#fff
  classDef hueGh1 fill:#2e7d32,color:#fff
  classDef hueGh2 fill:#388e3c,color:#fff
  classDef hueGh3 fill:#66bb6a,color:#111
  classDef hueGh4 fill:#c8e6c9,color:#111
  entry[entry_A] --> mid1[mid_1] --> mid2[mid_2] --> tail[outcome_B]
  class entry hueGh4
  class mid1 hueGh2
  class mid2 hueGh1
  class tail hueGh0
```

## UX leaf-strong (workflow style)

Strong on **merge / publish** outcome; lighter upstream on the same **`ux*`** ramp; optional side path muted.

```mermaid
flowchart TB
  classDef uxH fill:#4527a0,color:#fff
  classDef ux1 fill:#5e35b1,color:#fff
  classDef ux2 fill:#7e57c2,color:#fff
  classDef ux3 fill:#b39ddb,color:#111
  classDef uxOff fill:#eceff1,color:#111
  pickNode["Triage queue"] --> viewNode["Issue triage"]
  viewNode --> workNode["Implement"]
  workNode --> pushNode["Push + checks green"]
  viewNode -.-> refineNode["Refine filters"]
  refineNode -.-> pickNode
  class pushNode uxH
  class workNode ux1
  class viewNode ux2
  class pickNode ux3
  class refineNode uxOff
```
