# Dev setup — parity by domain

Maps **what you need** (by concern) to **typical Mac vs Windows** choices. Same job, different product—pick your column. **Install order and Mac-only detail:** **[macOS.md](./macOS.md)**. **How you work day to day:** **[work.md](./work.md)**.

**Related:** **[windows.md](./windows.md)** is **gaming/media software** on Windows (not a dev image); **[desktop.md](./desktop.md)** is the **tower hardware** for that build. All **device** guides share a common outline; see **[README.md](README.md)**.

# Index

- [Dev setup — parity by domain](#dev-setup--parity-by-domain)
- [Index](#index)
- [Basic and desktop](#basic-and-desktop)

# Basic and desktop

Everyday machine surface: how you arrange windows, keep the screen on, install apps, browse, and join calls.

| Domain                                              | macOS (typical in this repo)                                                               | Windows (typical)                                                                                                                                   |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Keep display awake** (long builds, presenting)    | **Amphetamine** (Mac App Store) or **`caffeinate`**                                        | **PowerToys → Awake**, or **Settings → System → Power** while plugged in                                                                            |
| **Meetings**                                        | **Zoom** / **Teams** / Meet — §3 in **[macOS.md](./macOS.md)**                             | `winget install Zoom.Zoom` or `winget install Microsoft.Teams`                                                                                      |
| **OS privacy** (camera, mic, screen share)          | **[macOS.md](./macOS.md)** — [6. Privacy & permissions](./macOS.md#6-privacy--permissions) | **Settings → Privacy & security** — enable camera, microphone, and screen capture for your meeting app                                              |
| **Package manager** (CLI app installs)              | **Homebrew**                                                                               | **winget** (built into recent Windows 10/11), or **Chocolatey** / **Scoop** if IT allows                                                            |
| **Window management** (tiling, snap, multi-monitor) | **[Rectangle](https://rectangleapp.com)** — `brew install --cask rectangle`                | **Snap Layouts** (Windows 11, built-in) + **PowerToys [FancyZones](https://github.com/microsoft/PowerToys)** — `winget install Microsoft.PowerToys` |
| **Work browser**                                    | **Chrome** (or policy browser) — §3 in **[macOS.md](./macOS.md)**                          | `winget install Google.Chrome`                                                                                                                      |