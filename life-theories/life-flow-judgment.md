# Life flow and final judgment

A **personal lifecycle model**: optional simulation framing where an author spawns the first human like a video game, then the world runs hands-off and the same loop is a **stable, self-managed** birth–death–judgment cycle. Layers in the diagram: **birth queue** (append and wait until a mother can give birth); **embodied life** (from birth through death); **after death** (cemetery, then accounting and judgment, then back to the queue). **Harm and penalty time (human-involved)** is described in a separate runbook (not in this repo) as a table sorted by typical duration of cost, not here. Everyday analogies (“like an Uber,” “like jail or an Airbnb”) are explicit nodes on purpose.

Mermaid uses `classDef` fills for readability; some renderers ignore subgraph styling.

**See also:** [Life game structure (nested instance, pills, daily loop)](life-game-structure.md) · [Lineage descent (endowment, IV/IQ, graph)](lineage-descent.md)

## Main loop and judgment branch

```mermaid
flowchart TD
  subgraph cosmology [Simulation cosmology]
    authorSpawner["Author spawns first human video-game style"]
    stableRuntime["Hands off stable self-managed world same loop below"]
  end

  authorSpawner --> stableRuntime
  stableRuntime --> enqueue

  subgraph birth_queue [Birth queue before embodiment]
    enqueue["Append to birth queue"]
    waitMother["Keep waiting for a mother → slot to give birth"]
  end

  subgraph embodied [Embodied life from birth]
    born["Be born"]
    live["Live life and register events"]
    priceAlive["Pay some price while alive"]
    transitionUber["Transition: like an Uber"]
    death["Die"]
  end

  enqueue --> waitMother
  waitMother --> born
  born --> live --> priceAlive --> transitionUber --> death

  cemetery["Cemetery / body and chapter closed"]
  death --> cemetery
  cemetery --> summarize["Summarize life events"]
  summarize --> evaluateDebt["Evaluate remaining debt"]
  evaluateDebt --> paySummary["Pay for the price of your life summary"]

  paySummary --> heaven[Heaven]
  paySummary --> something[Something]
  paySummary --> hell[Hell]

  jailAirbnb["Like a jail or an Airbnb"]
  something --> jailAirbnb
  hell --> jailAirbnb

  heaven --> enqueue
  jailAirbnb --> enqueue

  style cosmology fill:#e8eaf6,stroke:#5c6bc0,color:#283593
  style birth_queue fill:#eceff1,stroke:#78909c,color:#37474f
  style embodied fill:#f5f5f5,stroke:#9e9e9e,color:#424242

  classDef cMeta fill:#3949ab,stroke:#1a237e,color:#e8eaf6
  classDef cQueue fill:#546e7a,stroke:#37474f,color:#eceff1
  classDef cBirth fill:#1976d2,stroke:#0d47a1,color:#fff
  classDef cLive fill:#fbc02d,stroke:#f9a825,color:#212121
  classDef cTeal fill:#00897b,stroke:#00695c,color:#fff
  classDef cPinkNote fill:#f8bbd9,stroke:#c2185b,color:#4a148c
  classDef cDeath fill:#78909c,stroke:#546e7a,color:#fff
  classDef cCemetery fill:#5d6d5e,stroke:#3e4544,color:#eceff1
  classDef cSummarize fill:#c62828,stroke:#b71c1c,color:#fff
  classDef cEvaluate fill:#8e24aa,stroke:#6a1b9a,color:#fff
  classDef cJudgment fill:#4527a0,stroke:#311b92,color:#fff
  classDef cHeaven fill:#fafafa,stroke:#424242,color:#212121
  classDef cSomething fill:#b3e5fc,stroke:#0288d1,color:#01579b
  classDef cHell fill:#263238,stroke:#102027,color:#eceff1
  classDef cJailPink fill:#f48fb1,stroke:#ad1457,color:#3e2723

  class authorSpawner,stableRuntime cMeta
  class enqueue,waitMother cQueue
  class born cBirth
  class live cLive
  class priceAlive cTeal
  class transitionUber cPinkNote
  class jailAirbnb cJailPink
  class death cDeath
  class cemetery cCemetery
  class summarize cSummarize
  class evaluateDebt cEvaluate
  class paySummary cJudgment
  class heaven cHeaven
  class something cSomething
  class hell cHell
```

## Reading the model

### Ledger, fairness, and irreversibility

Someone is always watching (VAR-style): unpaid costs while alive are settled after death. **Anti-hereditary:** no inheriting a dead person’s “slot”; sadness does not restore stolen happiness. **Why not delete the harm data:** without costs for harm, the “life game” loses purpose and fairness. **Irreversibility:** consequences rarely fully undo; no time-travel feature—broken bones do not always snap back.

### Free will, balance, and purpose

If everyone were controlled, the game is pointless; choices matter; rules exist for those currently in play. Desire to improve keeps the wheel turning; automation and balance read as ongoing forces.

### Simulation and spawner (metaphor)

Treats existence as a long-running process: a one-time “first character,” then autonomous queue and judgment without micromanagement—**useful metaphor, not a physics claim**.

### Operator, watching, and unequal spawn

**Security** here means *what it is reasonable to treat as stable or exogenous*: not password hygiene, but the boundary between a mostly hands-off runtime and rare, high-leverage intervention.

**“Everything is possible” vs. “anything can happen now.”** The video-game framing allows wild outcomes in principle, but it is a poor security model to expect miracles or catastrophes *with no antecedent*. A plausible companion picture is a **game operator** (or layer above the queue) that **mostly does not touch the simulation** and only acts when something in the design **strictly requires** it.

**Watching vs. intervening.** Continuous accounting is not the same as constant meddling. The ledger can run tight while the **joystick** moves only in rare, high-leverage moments.

**Forced events and disease as levers.** In that picture, the operator could **introduce or steer** things like illness and constraint—not as constant puppetry, but as **occasional** pressure when the system needs differentiation, stakes, or correction. **Metaphor unless you treat it as a claim.**

**Unfair by construction.** People do not spawn with the same stats, family, or map. Inequality of endowment is almost the default, not something optimism patches. (For **IV/IQ-style baseline vs. trained stats**, see [lineage-descent.md](lineage-descent.md).)

### Asymmetry, culture, and the discipline stack

**Roles feed on asymmetry.** Without people who are unwell, medicine has little to do; without the unknown, research loses its fuel. That is structural, not a moral endorsement.

**Cross-cultural parallel:** One culture may speak in **God and devil**; another in **judge, police, and jail** after a human complaint. The vocabularies differ, but many **rules underneath are shared**—people still coordinate on harm, consent, and enforcement. **Beliefs** shape different **blind spots and strengths**; the flowchart’s heaven / hell / “something” / jail-like nodes are one way to **map outcomes**, not a claim that one religion owns the truth.

**Mathematics** is the strongest shared baseline; **physics** and **chemistry** come next. Most of the rest of culture is **recombining** existing elements, packaging, and **selling** narratives or goods—powerful, but more contingent than the lower layers.

### Social limits and your minimap

**Proof, persuasion, and where logic stops.** In social life it is nearly impossible to **prove** much against a dedicated adversary: people lie, and rhetoric can build traps you cannot fully armor against with argument alone. **Violence** (or its threat) often appears when reasonable moves are exhausted—the ceiling on “purely logical” security.

**External memory and consistency.** What you already decided and wrote down is part of your security against self-contradiction: notes offload detail so working memory can track new situations.

**The mental bubble / partial minimap.** Each person starts like a **blank drive** loaded through family, place, and experience—a minimap of what they have actually seen. The full world map is unfinishable. Expect **large unknowns** outside your patch.

## Main quest, routine, and realism

Culture and media often script a **default main quest**: compete for grades at school and university, then for jobs, then for a “successful” child to raise, then some rest when old. That path is **linear and competitive**; it forgives **few** mistakes—a skipped year or a serious health hit can **reshape** the rest of the story. **The Sims** is a useful parallel for **staged social progression** (needs, career ladder, household), not for stat breeding—that sits with lineage.

What often separates people from what they want is **routine** plus **realism**: naming an **achievement list** (what “done” looks like) and executing toward it daily. **Lottery** goals work the same way: you only win if you play, and long shots need a **sustainable** routine so you can keep “buying tickets” for a lifetime without burning out.

For **how daily play, instances, and pills layer as metaphor**, see [life-game-structure.md](life-game-structure.md).
