# Repository topology (tooling / meta)

High-level map of how **docs**, **automation**, and **source** relate.

| Area | Typical path | Role |
| --- | --- | --- |
| **Human docs** | `docs/**` | Narrative, indexes, ADRs |
| **Agent rules** | `.cursor/rules/**` | Short, repo-local guardrails |
| **Pasteables** | `.cursor/templates/**` (optional) | PR/issue/doc snippets |
| **Source / packages** | `src/**`, `packages/**`, or language default | Runnable code and tests |
| **CI** | `.github/workflows/`, `Makefile`, etc. | Verify on every change |

Human docs and code **both** change over time—link bidirectionally from root **`README.md`**.

## Related

- [Manifest](manifest.md)
