# Deployment topology (environments + split services)

Sketch **where** each piece runs: local, staging, production. Useful for **full stack** onboarding and **study** (compare PaaS vs k8s vs serverless). Keep boxes coarse—this is not a replacement for IaC.

## Multi-environment

```mermaid
flowchart TB
  subgraph dev [Local / dev]
    devWeb[Web dev server]
    devApi[API process]
    devDb[(Docker DB)]
  end
  subgraph staging [Staging]
    stWeb[Web bucket or host]
    stApi[API deploy]
    stDb[(Managed DB)]
  end
  subgraph prod [Production]
    prWeb[CDN + static]
    prApi[API scale set]
    prDb[(Primary + replica)]
  end
  devWeb --> devApi --> devDb
  stWeb --> stApi --> stDb
  prWeb --> prApi --> prDb
```

## Single environment — logical zones

```mermaid
flowchart LR
  subgraph public [Public edge]
    lb[Load balancer]
  end
  subgraph compute [Compute]
    api[Stateless API pods]
    worker[Workers]
  end
  subgraph data [Managed data]
    db[(DB)]
    cache[(Redis)]
    bucket[Object store]
  end
  lb --> api
  api --> db
  api --> cache
  worker --> bucket
  worker --> db
```

## Related

- Operations deployment prose: [`../doc/wiki/profiles/coding/operations-deployment.md`](../doc/wiki/profiles/coding/operations-deployment.md)
- Layered app vs services: [`template-layers.md`](template-layers.md)
