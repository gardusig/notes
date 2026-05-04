# System overview

## Purpose

<What the system does for users or callers.>

## Major components

| Component | Responsibility |
| --- | --- |
| <name> | <one line> |

## Boundaries

<What is in scope vs delegated to external systems.>

## Diagram

```mermaid
flowchart TB
  subgraph app [Application]
    api[API or entry]
    core[Core logic]
  end
  subgraph external [External]
    db[(Storage)]
  end
  api --> core
  core --> db
```
