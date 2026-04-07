# Dev setup — parity by domain

Maps **what you need** (by concern) to **typical Mac vs Windows** choices. Same job, different product—pick your column. **Install order and Mac-only detail:** **[macOS.md](./macOS.md)**. **How you work day to day:** **[work.md](./work.md)**.

**Related:** **[windows.md](./windows.md)** in this folder is a **gaming** build, not a dev image. All **device** guides share a common outline; see **[../README.md](../README.md)**.

# Index

- [Dev setup — parity by domain](#dev-setup--parity-by-domain)
- [Index](#index)
- [Basic and desktop](#basic-and-desktop)
- [Code, repos, and shipping](#code-repos-and-shipping)

---

# Basic and desktop

Everyday machine surface: how you arrange windows, keep the screen on, install apps, browse, and join calls.

| Domain | macOS (typical in this repo) | Windows (typical) |
| ------ | ---------------------------- | ------------------- |
| **Keep display awake** (long builds, presenting) | **Amphetamine** (Mac App Store) or **`caffeinate`** | **PowerToys → Awake**, or **Settings → System → Power** while plugged in |
| **Meetings** | **Zoom** / **Teams** / Meet — §3 in **[macOS.md](./macOS.md)** | `winget install Zoom.Zoom` or `winget install Microsoft.Teams` |
| **OS privacy** (camera, mic, screen share) | **[macOS.md](./macOS.md)** — [6. Privacy & permissions](./macOS.md#6-privacy--permissions) | **Settings → Privacy & security** — enable camera, microphone, and screen capture for your meeting app |
| **Package manager** (CLI app installs) | **Homebrew** | **winget** (built into recent Windows 10/11), or **Chocolatey** / **Scoop** if IT allows |
| **Window management** (tiling, snap, multi-monitor) | **[Rectangle](https://rectangleapp.com)** — `brew install --cask rectangle` | **Snap Layouts** (Windows 11, built-in) + **PowerToys [FancyZones](https://github.com/microsoft/PowerToys)** — `winget install Microsoft.PowerToys` |
| **Work browser** | **Chrome** (or policy browser) — §3 in **[macOS.md](./macOS.md)** | `winget install Google.Chrome` |

---

# Code, repos, and shipping

Toolchain for clone → edit → test → PR → deploy touchpoints.

| Domain | macOS (typical in this repo) | Windows (typical) |
| ------ | ---------------------------- | ------------------- |
| **Cloud / Kubernetes / IaC** (per employer) | brew / vendor installers — §2.8 | e.g. **AWS** `Amazon.AWSCLI`, **Azure** `Microsoft.AzureCLI`, **`kubectl`** `Kubernetes.kubectl` — match internal versions |
| **Containers** | **Docker Desktop** — §2.5 | `winget install Docker.DockerDesktop` (often **WSL 2** / features on first run) |
| **Editor** | **Cursor** — §2.6 | [cursor.com](https://cursor.com); `winget search cursor` for package ID |
| **GitHub from terminal** | **`gh`** — §2.8 | `winget install GitHub.cli` → **`gh auth login`** |
| **GitLab from terminal** (optional) | **`glab`** — §2.8 | [GitLab CLI](https://gitlab.com/gitlab-org/cli) or `winget search glab` — confirm with IT |
| **JavaScript runtime** (optional) | **Node** (Homebrew) — §2.7 | `winget install OpenJS.NodeJS.LTS` or **fnm** / **Volta** |
| **JSON in shell** | **`jq`** — §2.8 | `winget install jqlang.jq` |
| **Native build baseline** (compilers, headers when required) | **Xcode Command Line Tools** — §2.1 in **[macOS.md](./macOS.md)** | **Visual Studio Build Tools** / **Desktop development with C++** when MSVC is required; many stacks only need **Git for Windows** |
| **Version control** | **Git** (Homebrew) — §2.3–§2.4 | `winget install Git.Git` — same `git config` / SSH ideas as Mac |

**Smoke check (either OS):** `git --version`, **`docker run --rm hello-world`** (if you use Docker), **`gh auth status`**, open a repo in **Cursor**.
