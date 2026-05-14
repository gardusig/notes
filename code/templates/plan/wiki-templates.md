# 📋 Plan wiki templates

Wiki-first templates for plan shaping and execution handoff.

## 🗂️ Hub

Use these templates to shape execution plans before coding.

## 📋 Plan brief template

```markdown
## Goal
<1-2 paragraphs describing intended outcome>

## Ship mode
- [ ] Work now
- [ ] Defer and create/update GitHub issue

## Assumptions
- [ ] Confirmed: ...
- [ ] Needs confirmation: ...

## Uncertainties and Q&A
- Question: ...
  - Why it matters: ...
  - Default if unanswered: ...

## Recommended approach
1. Primary approach: ...
2. Fallback approach: ...

## Todo items
- [ ] ...
- [ ] ...

## Domain sections
### <Domain A>
- [ ] Minimal independent task ...

### <Domain B>
- [ ] Minimal independent task ...

## What we are not doing
- ...

## Verification
- [ ] ...
```

## 📋 Pre-write QA template

```markdown
## Assumptions
- ...

## Uncertainties to resolve
- Question: ...
  - Why this blocks safe mutation: ...
  - Options to choose from: ...

## Proceed criteria
- [ ] Assumptions confirmed.
- [ ] Mutation scope is explicit.
- [ ] Safety checks are satisfied.

## Action after proceed
- Execute the confirmed write operations.
```

## 📋 Domain templates

Use the same shape across domains:

```markdown
## Goal
...

## Scope
...

## Verification
- [ ] ...

## Risks / unknowns
...

## Next action
...
```

Apply this to:

- bug fixes
- dependency and maintenance work
- documentation updates
- enhancements
- integration tests
- unit tests

## 📌 Related

- [`README.md`](README.md)
- [`work-plan-with-issue.md`](work-plan-with-issue.md)
