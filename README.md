# 📝 Notes

This repo is a **personal wiki**: runbooks, recommendation lists, in-progress organization, and light procedural notes—not a product or advice for others.

Personal runbooks: device notes (`configure/`), personal inventory, shopping and recipes (`buy/`), active play, listening habits, diagram notes, and AI-assisted coding playbooks.

## 📑 Index

- **[buy/](buy/README.md)** — shopping: eat (recipes, pantry rhythm), drink, pharmacy, bathroom (personal care), cleaning / laundry
- **[code/](code/README.md)** — Cursor, agents, per-repo bootstrap, tasks, debugging UI flows, models, personal `@` skills
- **[configure/](configure/README.md)** — computers and phones: macOS, Windows, desktop hardware, parity, SDE2 work runbook, Android
- **[listen/](listen/README.md)** — music playlists (YouTube Music stubs + track tables by mood / theme)
- **[plan/](plan/README.md)** — practical task system: surfaces, **routine** (sleep, meals, weekly rhythm), **rules** ([`plan/rules/README.md`](plan/rules/README.md): governance, priority P0–P4, plan-making, emotional routing, risk A–E)
- **[play/](play/README.md)** — instruments, video games, puzzles
- **[read/](read/README.md)** — books (finished + queue) and **library-links** (wikis aligned to the watch library)
- **[watch/](watch/README.md)** — passive video: watched logs (movies, TV, anime) and **to-watch** queue by medium and kind
- **[wear/](wear/README.md)** — personal inventory: clothing, daily carry, tech backpack
- **[wonder/](wonder/README.md)** — conceptual models hub (lifecycle, metaphors, life arc / HUD, tactical HUD, philosophical vigilance); entry points include [life-flow-judgment.md](wonder/life-flow-judgment.md), [life-arc.md](wonder/life-arc.md), [life-game-structure.md](wonder/life-game-structure.md#tactical-hud)

## 🧭 Cross-domain quick paths

| If you are… | Start here |
| --- | --- |
| Capturing the day / picking the next task | [`plan/routine/README.md`](plan/routine/README.md), [`plan/rules/priority.md`](plan/rules/priority.md) |
| Stuck on a task (patience vs motion vs novelty) | [`play/README.md`](play/README.md) |
| Shipping code with agents | [`code/README.md`](code/README.md) |
| Machine install or employer runbook stubs | [`configure/README.md`](configure/README.md) → [`macOS.md`](configure/macOS.md) / [`work.md`](configure/work.md) |
| Reality HUD / meaning framing | [`wonder/life-arc.md`](wonder/life-arc.md), [`wonder/life-game-structure.md`](wonder/life-game-structure.md) |

## 🔧 Repo maintenance (links and headings)

Tooling lives at the **repo root** (no `scripts/` folder).

- **Link review** — export or diff browser bookmarks as [`bookmarks.html`](bookmarks.html); prune dead or duplicate URLs, then fold survivors into the nearest subtree (`read/`, `watch/`, `listen/`, `buy/`, `configure/`, …) via each folder’s **📑 Index**.
- **Heading emoji pass** — from the repo root: `python3 add_heading_emojis.py` ([`add_heading_emojis.py`](add_heading_emojis.py)) walks tracked `*.md` under this repo and adds emoji prefixes to ATX headings when missing. Run after substantive markdown edits and **before** opening or updating a GitHub PR (`@gh-pr` after `@git-pull` / `@git-push` per your skills workflow).

## ☀️ Daily capture and modes

Lightweight capture for **what happened**, **body state**, and **which cognitive mode** you are in (review vs execute vs play). **Habits and body-clock spine** (sleep window, meals, weekly matrix, bounded puzzles) — [`plan/routine/README.md`](plan/routine/README.md). Picking rules at [`plan/rules/priority.md`](plan/rules/priority.md); **plan-making efficiency** at [`plan/rules/plan-making.md`](plan/rules/plan-making.md).

## 📌 Current snapshot

One-screen **reality HUD**: where you are living/working, main commitments this month, and the top risk. Update when reality shifts. Longer-lived tactical detail can also live in **[wonder/life-game-structure.md § Tactical HUD](wonder/life-game-structure.md#tactical-hud)**; slow meaning and quest framing in **[wonder/life-arc.md](wonder/life-arc.md)**.

## 📚 Debug library (instruments, games, puzzles)

When a task jams, match the **type** of stuck (patience vs motion vs novelty) to the right play lane — see **[play/](play/README.md)** and puzzle runbooks under **[play/puzzles/](play/puzzles/README.md)**.

## 🎛️ Cognitive modes (review, plan, creativity)

**Review** — task lists, calendar, inbox triage. **Plan** — break down the next task. **Creativity / play** — instruments, games, puzzles as recovery or deliberate practice — not as a substitute for P0–P1 when those are due.
