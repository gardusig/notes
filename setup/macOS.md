# macOS — Apple Silicon laptop (portable dev)

## Purpose

This note is for a **portable Apple Silicon Mac** used as a **daily dev laptop**: clone repos, edit in **Cursor**, run **Docker**, and get through a workday on **battery** without chasing the most expensive SKU. It is **not** a desktop workstation guide—optimize for **mobility**, **runtime**, and **cost-aware** choices.

**Stack:** **ARM64** only—prefer **native** builds (**Homebrew** in `/opt/homebrew`, **arm64** container images) for speed and battery.

**See also:** **[parity.md](./parity.md)** maps the same jobs on **Windows**. **[work.md](./work.md)** is the SDE2 workflow on top of this OS setup. Folder outline: **[README.md](README.md)**.

---

## Summary

- **Hardware goal:** **Cheapest current portable** that still has **strong battery life** for mixed terminal + browser + light Docker—usually the **entry MacBook Air**; weigh the **entry MacBook Pro** if you need **sustained** performance or more **ports**.
- **Software end state:** **Homebrew**, **Git**, **GitHub CLI (`gh`)**, **Docker Desktop**, and **Cursor** installed and verified; optional **Node.js** and employer CLIs (**AWS**, **`kubectl`**, etc.) per onboarding. **Chrome**, **Docker**, and **Cursor** can be installed like normal Mac apps from the vendor (DMG → **Applications**) — see **[§2.0](#20-install-chrome-docker-desktop--cursor-gui--applications)**.
- **Shopping detail:** **[What to buy & price expectations](#what-to-buy--price-expectations)** compares **entry Air vs entry Pro** and calls out **RAM** / **SSD** minimums for dev.

---

## Index

- [Purpose](#purpose)
- [Summary](#summary)
- [Index](#index)
- [Setup & installation](#setup--installation)
  - [1. System preparation](#1-system-preparation)
  - [2. Terminal \& CLI setup](#2-terminal--cli-setup)
  - [2.0 Install Chrome, Docker Desktop \& Cursor (GUI — Applications)](#20-install-chrome-docker-desktop--cursor-gui--applications)
  - [2.1 Install Xcode Command Line Tools](#21-install-xcode-command-line-tools)
  - [2.2 Install Homebrew (ARM64)](#22-install-homebrew-arm64)
  - [2.3 Install Git](#23-install-git)
  - [2.4 Configure Git](#24-configure-git)
  - [2.5 Install Docker Desktop](#25-install-docker-desktop)
  - [2.6 Install Cursor](#26-install-cursor)
  - [2.7 Optional: Node.js](#27-optional-nodejs)
  - [2.8 GitHub CLI and onboarding helpers](#28-github-cli-and-onboarding-helpers)
  - [3. Browsers \& communication](#3-browsers--communication)
  - [4. Productivity \& system](#4-productivity--system)
  - [5. Local coding workflow](#5-local-coding-workflow)
  - [6. Privacy \& permissions](#6-privacy--permissions)
- [What to buy \& price expectations](#what-to-buy--price-expectations)
  - [Cheapest portable Mac (battery-first)](#cheapest-portable-mac-battery-first)
  - [Entry MacBook Air vs entry MacBook Pro](#entry-macbook-air-vs-entry-macbook-pro)
  - [Money and timing](#money-and-timing)

---

## Setup & installation

### 1. System preparation

Before installing tools:

1. **Update macOS** — **System Settings → General → Software Update**
2. Sign in with your **Apple ID** (App Store, iCloud, Find My)
3. Tweak basics:

**System Settings → Trackpad**  
- Enable **Tap to click**

**System Settings → Keyboard**  
- Increase **Key Repeat Rate** (optional)

**System Settings → Desktop & Dock**  
- Enable **Automatically hide and show Dock** (optional)

### 2. Terminal & CLI setup

Do this **in order**. Open **Terminal**: **Applications → Utilities → Terminal**

| Step | What you get |
| ---- | ---------------- |
| **2.0** | **Chrome**, **Docker Desktop**, **Cursor** via **browser + DMG** (normal apps in **Applications**) — optional if you use **Homebrew casks** in §2.5–2.6 and §3 instead |
| 2.1 | Compilers, `git` foundation, Homebrew prerequisites |
| 2.2 | **Homebrew** (`brew`) |
| 2.3 | **Git** from Homebrew (predictable upgrades) |
| 2.4 | Your name and email on every commit |
| 2.5 | **Docker** for local containers |
| 2.6 | **Cursor** editor |
| 2.7 | **Node.js** (only if you need it) |
| 2.8 | **`gh`**, **`jq`**, optional **`glab`** and cloud/k8s CLIs for onboarding |

### 2.0 Install Chrome, Docker Desktop & Cursor (GUI — Applications)

Use this when you want **real Mac applications**—download in a browser, open a **`.dmg`**, drag into **Applications**—instead of installing those three only from the terminal.

You can still use **Homebrew** for **Git**, **`gh`**, and everything else in §2.2 onward. **Chrome** is listed first so you have a familiar browser for the other downloads if **Safari** is not your default.

#### Google Chrome (browser)

1. Open **Safari** (**Applications → Safari**) or another browser already on the Mac.
2. Go to **[google.com/chrome](https://www.google.com/chrome/)** and choose **Download Chrome**.
3. If the site asks, pick **Mac with Apple chip** (Apple Silicon) or **Mac with Intel chip** only on Intel Macs.
4. In **Finder**, open **Downloads** and double-click **`googlechrome.dmg`**.
5. In the window that opens, **drag the Chrome icon** onto the **Applications** folder shortcut.
6. **Eject** the installer disk (click the disk on the desktop or sidebar, then **Eject**), or drag it to **Trash** (it acts as eject).
7. Open **Chrome** from **Launchpad** or **Finder → Applications → Google Chrome**.  
   - If macOS says the app can’t be opened because it’s from an unidentified developer: **Control-click (right-click) the app → Open → Open** once to approve.

#### Docker Desktop

1. In **Chrome** (or **Safari**), open **[Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)** (official download buttons for **Apple silicon** vs **Intel**) or **[docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)** and download **Docker Desktop for Mac**.
2. On **Apple Silicon**, choose the **Apple Silicon** / **ARM64** build—not the Intel-only installer.
3. Double-click **`Docker.dmg`** in **Downloads**.
4. **Drag Docker** (whale icon) into **Applications**, then **eject** the disk image.
5. Open **Finder → Applications → Docker** (double-click). Accept prompts (privileged helper, networking, **OK** on security dialogs). Wait until the **whale icon** in the menu bar shows Docker is **running** (not “Starting…”).

#### Cursor

1. Open **[cursor.com](https://cursor.com)** in your browser and use **Download** for **macOS** (Apple Silicon vs Intel matches your Mac; Apple Silicon laptops use the **Apple Silicon** build).
2. Open the downloaded **`.dmg`** from **Downloads**.
3. **Drag Cursor** into **Applications**, then **eject** the disk image.
4. Open **Applications → Cursor**. Complete first-run sign-in if prompted, then **File → Open Folder** to open a project. Extensions and keybindings behave like a VS Code–style editor; use the in-app marketplace for language support.

**Updates:** **Chrome** and **Docker** usually update in-app (**Chrome → About Google Chrome**; **Docker → Check for updates**). **Cursor** prompts for updates or checks automatically—same idea as other desktop editors.

---

### 2.1 Install Xcode Command Line Tools

Required for Git, compilers, Homebrew, and many dev tools.

```bash
xcode-select --install
```

Accept the prompt and wait for the install to finish.

Verify:

```bash
xcode-select -p
```

You should see a path under `/Library/Developer/CommandLineTools` or inside Xcode.

### 2.2 Install Homebrew (ARM64)

Install:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

On **Apple Silicon**, Homebrew lives under **`/opt/homebrew`**. Add it to your shell:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Verify:

```bash
brew --version
```

Keep things current over time:

```bash
brew update
brew upgrade
```

### 2.3 Install Git

Use Homebrew’s Git so updates are simple:

```bash
brew install git
```

Confirm **Homebrew’s** binary wins on your `PATH` (after `brew shellenv`):

```bash
which git
git --version
```

### 2.4 Configure Git

Set your identity (use the same email as **GitHub** / your host if you push there):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Useful defaults:

```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
```

Optional: **SSH keys** for GitHub/GitLab — generate with `ssh-keygen`, add the **public** key to the host, then clone with `git@...` URLs.

### 2.5 Install Docker Desktop

**Docker Desktop** is the straightforward way to run **Docker** and **Docker Compose** on macOS.

**GUI path:** If you already dragged **Docker** into **Applications** using **[§2.0](#20-install-chrome-docker-desktop--cursor-gui--applications)**, skip the `brew` line below and go straight to the numbered steps.

**Homebrew alternative (also installs the same app in Applications):**

```bash
brew install --cask docker
```

Then:

1. Open **Docker** from **Applications** (first launch installs helpers and asks for permissions).
2. Wait until the whale icon in the menu bar says Docker is **running**.
3. Smoke test (after **Terminal** + **Homebrew** shell setup in §2.2 if `docker` is not on your `PATH` yet):

```bash
docker run --rm hello-world
```

If the command prints a success message, containers work. For Apple Silicon, prefer images that publish **arm64** (or multi-arch) variants to avoid slow emulation.

### 2.6 Install Cursor

**Cursor** is the editor this guide standardizes on (instead of VS Code).

**GUI path:** Use **[§2.0 — Cursor](#cursor)** (download from **[cursor.com](https://cursor.com)**, drag to **Applications**).

**Homebrew alternative:**

```bash
brew install --cask cursor
```

Open **Cursor** from **Applications**, complete any first-run sign-in, and open a folder (**File → Open Folder**). Treat it like a VS Code–compatible editor: extensions and keybindings carry the same ideas; use the in-app marketplace for language support (e.g. Python, Go, ESLint).

If the cask name ever changes, install from **[cursor.com](https://cursor.com)** via the GUI; you can still use **`brew upgrade --cask cursor`** later when the cask exists.

### 2.7 Optional: Node.js

Handy for JavaScript/TypeScript, front-end tooling, and many CLIs:

```bash
brew install node
```

Verify:

```bash
node --version
npm --version
```

For **per-project** Node versions, consider **nvm** or **fnm** later; Homebrew’s `node` is enough to get started.

### 2.8 GitHub CLI and onboarding helpers

These tools support everyday SDE workflows (clone, PRs, CI checks) and match the **terminal + review** loop described in **[work.md](./work.md)**.

#### GitHub CLI (`gh`)

Install and sign in (browser or token—follow the prompts):

```bash
brew install gh
gh auth login
```

Verify:

```bash
gh auth status
```

**Typical commands after onboarding:** `gh repo clone org/repo`, `gh pr list`, `gh pr create`, `gh pr checkout 123`, `gh pr view --web`. Use **`gh api`** when you need data the subcommands do not expose.

If **`gh`** is missing in scripts or Cursor tasks, ensure Homebrew’s `brew shellenv` is in **`~/.zprofile`** (§2.2) so non-interactive shells see `gh` on your `PATH`.

#### GitLab CLI (`glab`)

If your company uses **GitLab** instead of (or in addition to) GitHub:

```bash
brew install glab
glab auth login
```

#### `jq` (JSON on the command line)

Handy for parsing **`gh api`** output, internal tooling, and one-off scripts:

```bash
brew install jq
```

#### Cloud, Kubernetes, and org-specific CLIs

Install **when your team’s onboarding doc says so**—examples: **AWS CLI**, **Google Cloud SDK**, **Azure CLI**, **`kubectl`**, **Terraform**. Prefer formulae or installers your security team approves; keep versions aligned with what production uses.

**Tip:** After SSO or VPN changes, re-run **`gh auth login`** (or refresh tokens) if commands start returning **401** or **permission denied**.

### 3. Browsers & communication

| App        | Description                                |
| ---------- | ------------------------------------------ |
| **Chrome** | Web browser with Google account sync.      |
| **Zoom**   | Video conferencing for meetings and calls. |

**Chrome (GUI):** Follow **[§2.0 — Google Chrome](#google-chrome-browser)** (download **`.dmg`**, drag to **Applications**).  
**Chrome (Homebrew):** `brew install --cask google-chrome`

**Zoom:** Download the **Mac** installer from **[zoom.us/download](https://zoom.us/download)** and run the **`.pkg`**, or `brew install --cask zoom`.

For **camera**, **microphone**, and **screen sharing** in meeting apps, approve the prompts on first use and verify entries under **System Settings → Privacy & Security** (see [§6](#6-privacy--permissions)).

### 4. Productivity & system

| Role | App (this guide) | Description |
| ---- | ---------------- | ----------- |
| **Keep awake** | **Amphetamine** | Keeps the Mac awake on triggers or schedules. Cross-OS → **[parity — Basic and desktop](./parity.md#basic-and-desktop)**. |
| **Window manager** | **Rectangle** | Tiling, snapping, and multi-display layouts. Cross-OS → **[parity — Basic and desktop](./parity.md#basic-and-desktop)**. |

Install **Rectangle** with `brew install --cask rectangle`. **Amphetamine** is usually installed from the **Mac App Store** (search “Amphetamine”).

### 5. Local coding workflow

You now have **brew**, **git**, **`gh`** (if you followed §2.8), **Docker**, and **Cursor**. A typical loop:

1. **Clone:** `git clone <repo-url>` or **`gh repo clone org/repo`** (HTTPS or SSH, matching your auth from §2.4 / `gh auth login`).
2. **Open in Cursor:** **File → Open** the repo folder.
3. **Run stack:** follow the project README — often `docker compose up` or a `Makefile` / script that uses Docker.
4. **Branch and PR:** create a branch, push, then **`gh pr create`** or open a PR from the host’s web UI; list and check reviews with **`gh pr list`** / **`gh pr view`**.
5. **Commit:** use Cursor’s **Source Control** view or the terminal; commits use the Git identity from §2.4.

If a project needs a language runtime not covered here (Python, Go, Rust), install with **Homebrew** (`brew install python@3.12`, `brew install go`, etc.) or use a **devcontainer** in Cursor/Docker when the repo provides one.

### 6. Privacy & permissions

macOS gates sensitive capabilities behind **System Settings → Privacy & Security**. Many apps only prompt the **first time** they need something; if something silently fails (containers, camera, screen share), check this pane and the app’s own settings.

Open **System Settings → Privacy & Security** and review the categories below. Toggle **on** for the app that should have access (e.g. **Terminal**, **Cursor**, **Docker**, **Zoom**).

#### Coding and dev tools

| Permission | Typical use |
| ---------- | ----------- |
| **Accessibility** | Some editors or terminal tools use it for global shortcuts or automation; only enable if you trust the app and it asks. |
| **Developer tools** | Appears for some dev workflows; allow when Xcode or related tooling requests it. |
| **Files and Folders** / **Full Disk Access** | Editors and **Terminal** reading project trees, dotfiles, or volumes outside the default sandbox when tools complain. Grant narrowly (e.g. Terminal, Cursor) only if needed. |
| **Local Network** | **Docker Desktop**, local APIs, phone/simulator pairing, `localhost` discovery—enable if the app cannot reach services on your LAN. |

**Docker Desktop** usually asks on first launch (networking, file sharing); accept so bind mounts and VM helpers work. **Cursor** may request folder access when you open a repo—use **Allow** for the intended directories.

#### Meeting and communication apps

| Permission | Typical use |
| ---------- | ----------- |
| **Camera** | Video in **Zoom**, **Google Meet**, **Microsoft Teams**, etc. |
| **Microphone** | Voice in the same apps; also used by some recording or dictation features. |
| **Screen Recording** | **Screen share** in meetings; without it, others may see a black screen when you present. |

Open each meeting app once, start a test call or screen share, and **approve** the macOS prompts. If sharing still fails, return to **Privacy & Security** and confirm the app is listed and enabled for **Screen Recording** and **Camera**.

---

## What to buy & price expectations

### Cheapest portable Mac (battery-first)

For **software development** on the go, bias toward:

- **Entry MacBook Air** with **Apple Silicon** — usually the **best blend** of **price**, **weight**, and **all-day** light-to-mixed use (terminal, browser, occasional Docker).
- **Unified memory:** **16 GB** if you can afford it (Docker + IDE + browser tabs adds up fast); **8 GB** can work for very light stacks but gets tight.
- **Storage:** **512 GB** is a comfortable floor if you keep local repos and container layers; **256 GB** is workable with discipline and external storage.

Check **current** generations and prices on [apple.com](https://www.apple.com); this note does not pin chip generation (M2/M3/M4, etc.) because Apple refreshes SKUs often.

### Entry MacBook Air vs entry MacBook Pro

Use this when both lines offer **Apple Silicon** at the **low end** of each family—verify **screen size**, **chip**, and **port** layout for the exact models you are comparing.

| Topic | Entry MacBook Air (typical) | Entry MacBook Pro (typical) |
| ----- | --------------------------- | --------------------------- |
| **Battery (mixed dev use)** | Often **class-leading** for light/medium loads | Excellent; **sustained** heavy compile / VM load holds up longer before thermal limits |
| **Cooling** | **Fanless** on some Air models (silent; throttle under long max CPU) | **Active cooling**—better for **long builds**, heavy Docker, or video encode |
| **Display** | Very good **LCD**; notch on recent models | Often **brighter** and **ProMotion** on **14"**+ tiers—**entry** 14" may still beat Air for HDR/brightness |
| **Ports** | **MagSafe** + **2× Thunderbolt** on many models | **MagSafe** + **more Thunderbolt**, sometimes **HDMI** / **SD** on larger Pros—**confirm** the generation |
| **Portability** | **Lighter**, easier one-hand carry | **Heavier**; still portable but more “desk to café” than “all-day in a bag” |
| **Who should pick it** | **Default** for **cheapest** + **long battery** + normal dev | You **routinely** peg CPU for long stretches, want **more ports**, or strongly prefer the **Pro** display |

If the **price gap** is small during a promo, an **entry Pro** can be rational; if **budget and battery on light work** matter most, **Air** usually wins.

### Money and timing

- **Apple Refurbished** and **education** pricing can narrow the gap—worth checking before paying list price.
- After purchase, follow **[Setup & installation](#setup--installation)** on a clean macOS install.
