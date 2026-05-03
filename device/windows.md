# Windows PC — Gaming & Media (no dev stack)

## Purpose

This note is **software and workflow** for a **Windows 11 64-bit** desktop used as a **gaming and media station**: **games**, **movies**, and **torrents**. It is **not** a primary developer machine—no emphasis on Docker or a full coding stack (see **[parity.md](./parity.md)** for work/dev parity on Windows).

**Hardware—parts, assembly, monitors, GPU tiers:** **[desktop.md](./desktop.md)**. Other device guides use the same outline pattern; folder index: **[README.md](README.md)**.

---

## Summary

- **Role:** Play games, watch local or streamed media, handle torrents and large libraries—**without** treating the box as your primary dev environment.
- **OS target:** **Windows 11** on the **AM5 APU tower** described in **desktop.md** (or any similar PC).
- **Software:** Update Windows, **AMD** chipset + **Adrenalin** while on APU; **Steam** / other launchers; **VLC** + **qBittorrent**; optional **terminal** / **winget** installs; optional **ML** notes if you experiment with **game-playing agents**.
- **Shopping / build:** **[desktop.md](./desktop.md)** — tower, peripherals, BRL ballparks.

---

## Index

- [Purpose](#purpose)
- [Summary](#summary)
- [Index](#index)
- [Setup & installation](#setup--installation)
  - [Before you boot (hardware)](#before-you-boot-hardware)
  - [First boot & Windows install](#first-boot--windows-install)
  - [Windows tuning (gaming-focused)](#windows-tuning-gaming-focused)
  - [Terminal & command-line installs](#terminal--command-line-installs)
  - [Optional: training an AI agent on games](#optional-training-an-ai-agent-on-games)
  - [Games & launchers](#games--launchers)
  - [Movies & torrents](#movies--torrents)
- [Hardware assumptions](#hardware-assumptions)

---

## Setup & installation

### Before you boot (hardware)

If you are **assembling** the tower, follow **[Physical build](./desktop.md#physical-build-short-checklist)** in **desktop.md**, then return here for **Windows** and **apps**.

### First boot & Windows install

1. Create **Windows 11** install media (**Microsoft** media creation tool) on a **USB** drive.  
2. Boot from **USB**; install **Windows** on the **NVMe** (not the **HDD**).  
3. After login, run **Windows Update** until **Settings → Windows Update** is **clear** (may need **reboots**).  
4. Install **AMD** **chipset** drivers from **AMD** or the **board** vendor page, then **Adrenalin** for the **APU** graphics.  
5. **Format** the **HDD** in **Disk Management** if it is **raw**; assign a **drive letter** for **games / torrents / media**.

### Windows tuning (gaming-focused)

1. **Power** — **High performance** or **Balanced**; avoid **aggressive** eco modes while gaming.  
2. **Game Mode** — **Settings → Gaming → Game Mode** **on**.  
3. **Disk habit** — **SSD** = **Windows** + **heavy** games; **HDD** = **torrents**, **media**, **backup**, **light** games.  
4. **Microsoft account** — optional; useful for **Xbox** / **Store** / **Game Pass**.  
5. After a **dGPU**: plug the **monitor** into the **GPU**; install **NVIDIA** or **AMD** **GPU** drivers; you can keep **chipset** from **AMD**.

No **WSL** / **Docker** unless you change your mind.

### Terminal & command-line installs

Use the terminal when you want **repeatable** installs, **scripted** setup, or to match docs that show **CLI** commands.

**Open a terminal**

- **Windows Terminal** (recommended): press **Win**, type **Terminal**, open **Windows Terminal**.  
- **PowerShell**: **Win + X** → **Terminal** or **Windows PowerShell** (menu varies by Windows build).

**Administrator** (needed for some drivers, **DISK** operations, or machine-wide installs)

- **Start** → type **Terminal** → **Run as administrator**, or right-click **Terminal** → **Run as administrator**.  
- **User Account Control** prompts are normal when elevating.

**Run scripts from the internet** (only if you trust the source)

PowerShell may block local scripts until you relax policy for your user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Package installs with winget** (built into recent Windows 11)

Update sources and search:

```powershell
winget source update
winget search Steam
```

Examples (names can change—use `winget search` to confirm **Id**):

```powershell
winget install Valve.Steam
winget install VideoLAN.VLC
winget install qBittorrent.qBittorrent
```

**PATH** — After installing **Python** or other dev tools for experiments (see below), reopen the terminal so **PATH** updates from the installer take effect. Prefer **“Add Python to PATH”** on the official **python.org** Windows installer if you use that route.

### Optional: training an AI agent on games

Sketch of **what this PC might need** if you go beyond casual play and try **reinforcement learning**, **imitation learning**, or **bots** that **sense** the screen. This is **not** a full ML tutorial.

**Legal and ToS**

- Train and automate only where you **own the game** and the **EULA** allows it. **Online** titles with **anti-cheat** often **forbid** memory injection, **bots**, or **unauthorized** clients—assume **no** unless the publisher documents otherwise.  
- **ROMs** / **BIOS** for emulators: use **legal** dumps you are entitled to; do not use this guide as an excuse to pirate.

**Compute**

- **Discrete NVIDIA GPU** is the **default** path on Windows for **PyTorch** / **CUDA** tutorials and prebuilt wheels. An **APU alone** is only enough for **tiny** experiments or **CPU**-only demos.  
- **VRAM:** **8 GB** is a **tight** floor for small CNNs + environment overhead; **12 GB+** is more comfortable for **vision**-based agents at **1080p**-class frame sizes.

**Memory and disk**

- **32 GB RAM** (already the target in **desktop.md**) helps when holding **replay buffers**, **datasets**, or **multiple** processes (game + capture + trainer).  
- Put **checkpoints**, **logs**, and **conda/env** folders on the **SSD**; use the **HDD** for **bulk** video captures if you record lots of rollouts.

**Software stack (typical)**

- **Python 3.11+** from **[python.org](https://www.python.org/downloads/windows/)** or **winget** (`Python.Python.3.12`, etc.—verify with `winget search Python`).  
- **PyTorch** with the **CUDA** build that matches your driver (see **[pytorch.org](https://pytorch.org)** install selector).  
- Libraries such as **Gymnasium**, **Stable-Baselines3**, or game-specific APIs—many examples assume **Linux**; **WSL2** with GPU passthrough is an **advanced** option if you hit tooling gaps on bare Windows.

**Getting pixels into the model**

- Prefer **official** APIs, **headless** builds, or **env** wrappers the game or modding community supports.  
- **Screen capture** (OBS, DXGI-based tools) works for **research prototypes** but adds **latency** and **encoding** load; match **resolution** and **FPS** to what your **GPU** can sustain.  
- **Determinism** (fixed seed, fixed timestep) matters for **reproducible** RL runs.

**Anti-cheat and injection**

Assume **blocked** on competitive online games. **Single-player** / **local** sandboxes and **open** games are the realistic training ground unless you have a **commercial** or **research** agreement.

### Games & launchers

| App / platform | Description |
| -------------- | ----------- |
| **Epic Games Store** | Free weekly titles. |
| **GOG Galaxy** | DRM-friendly classics. |
| **RetroArch** | **2D** / retro cores (legal ROMs only). |
| **Steam** | Main library; strong **indie** / **2D**. |
| **Xbox** (Microsoft Store) | **Game Pass** if you subscribe. |

**Discord** for voice if you play online.

### Movies & torrents

| App | Description |
| --- | ----------- |
| **Jellyfin** / **Plex** (optional) | **Media server** clients if you use a **NAS** / other PC. |
| **MPC-BE** or **mpv** | Minimal players. |
| **qBittorrent** | **Torrent** client; prefer **legal** sources. |
| **VLC** | Plays most local files. |

**Stremio**-style apps depend on **add-ons** and rights—use judgment. For **4K** / **HDR**, prefer **Ethernet** or **strong Wi‑Fi**; **Bluetooth** is for **audio**, not **huge** file transfers.

---

## Hardware assumptions

This guide assumes a **gaming-oriented desktop** similar to the **AM5 APU** reference build in **[desktop.md](./desktop.md)** (parts list, peripherals, **GPU** upgrade tiers, BRL notes). If your machine differs, keep the **same disk split** idea: **fast SSD** for **Windows** and heavy games, **HDD** (or second SSD) for **media** and **torrents**.
