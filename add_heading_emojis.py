#!/usr/bin/env python3
"""Add emoji prefixes to Markdown ATX headings (# through ######) if missing."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


def _first_significant_char(s: str) -> str | None:
    for ch in s:
        if ch.isdigit() or ch in ". ":
            continue
        return ch
    return None


def title_has_leading_emoji(rest: str) -> bool:
    t = rest.strip()
    ch = _first_significant_char(t)
    if ch is None:
        return False
    o = ord(ch)
    if 0x1F000 <= o <= 0x1FAFF:
        return True
    if 0x2190 <= o <= 0x21FF:
        return True
    if 0x2300 <= o <= 0x25FF:
        return True
    if 0x2600 <= o <= 0x2BFF:
        return True
    if 0x1F600 <= o <= 0x1F64F:
        return True
    if 0x2654 <= o <= 0x265F:  # chess symbols etc.
        return True
    return False

# Longer phrases first
KEYWORD_EMOJI: list[tuple[str, str]] = [
    ("online supermarket", "🛒"),
    ("standard purchase", "🛍️"),
    ("store zone", "📍"),
    ("weekly batch", "📅"),
    ("soup vegetable mix", "🍲"),
    ("eating fruit", "🍎"),
    ("leafy green", "🥬"),
    ("vegetable mix", "🥗"),
    ("low calorie", "🍐"),
    ("high calorie", "🍌"),
    ("meat & eggs", "🥩"),
    ("meat and eggs", "🥩"),
    ("frozen fruit", "❄️"),
    ("filter coffee", "☕"),
    ("bean soup", "🫘"),
    ("vegetable + meat", "🍲"),
    ("pork + beans", "🐖"),
    ("tasty meal", "🍽️"),
    ("routine cooking", "🍲"),
    ("markdown and docs", "📝"),
    ("merge conflict", "🔀"),
    ("body skeleton", "📄"),
    ("title rule", "🏷️"),
    ("work plan", "📐"),
    ("diff summary", "📊"),
    ("zip git", "🤐"),
    ("close as duplicate", "🔗"),
    ("delete closed", "🗑️"),
    ("label decorate", "🏷️"),
    ("where to start", "🧭"),
    ("system overview", "🏗️"),
    ("data flow", "🌊"),
    ("coding standard", "📏"),
    ("anti-pattern", "⚠️"),
    ("when shopping", "🛒"),
    ("when to", "❓"),
    ("why this", "💡"),
    ("portioning", "🍱"),
    ("goal:", "🎯"),
    ("upstream", "⬆️"),
    ("index", "📑"),
    ("overview", "👁️"),
    ("ingredient", "🥗"),
    ("instruction", "📝"),
    ("equipment", "🔧"),
    ("calories", "🔢"),
    ("optional", "➕"),
    ("perishable", "🥬"),
    ("vegetable", "🥕"),
    ("hygiene", "🧴"),
    ("cleaning", "🧹"),
    ("laundry", "🧺"),
    ("trash", "🗑️"),
    ("dishwash", "🍽️"),
    ("bathroom", "🚿"),
    ("oral care", "🦷"),
    ("shaving", "🪒"),
    ("seasoning", "🧂"),
    ("dry powder", "🌾"),
    ("legume", "🫘"),
    ("grain", "🌾"),
    ("pasta", "🍝"),
    ("coffee", "☕"),
    ("niche", "✨"),
    ("specialty", "✨"),
    ("whey", "🥤"),
    ("vanilla", "🍦"),
    ("electronics", "🔌"),
    ("accessories", "🔌"),
    ("durables", "🛋️"),
    ("supermarket", "🏬"),
    ("e-commerce", "📦"),
    ("pharmacy", "💊"),
    ("supplement", "💊"),
    ("staple", "📌"),
    ("produce", "🥬"),
    ("frozen", "❄️"),
    ("protein", "🥩"),
    ("detox", "💚"),
    ("juice", "🧃"),
    ("drink", "🥤"),
    ("blender", "🌀"),
    ("storage", "🗄️"),
    ("cookware", "🍳"),
    ("knife", "🔪"),
    ("peeling", "🥔"),
    ("cutting board", "🪵"),
    ("eating setup", "🍽️"),
    ("routine", "🔁"),
    ("weekly", "📅"),
    ("daily", "☀️"),
    ("wake", "⏰"),
    ("sleep", "😴"),
    ("hydration", "💧"),
    ("diet", "🥗"),
    ("governance", "🏛️"),
    ("priority", "⬆️"),
    ("decision", "✅"),
    ("risk tier", "⚡"),
    ("emotional", "💭"),
    ("plan making", "📐"),
    ("recurring", "🔁"),
    ("maintenance", "🔧"),
    ("playlist", "🎵"),
    ("instrumental", "🎹"),
    ("channel", "📺"),
    ("podcast", "🎙️"),
    ("library", "📚"),
    ("book", "📖"),
    ("movie", "🎬"),
    ("anime", "🇯🇵"),
    ("tv series", "📺"),
    ("to watch", "👀"),
    ("watched", "✅"),
    ("video game", "🎮"),
    ("completed", "🏁"),
    ("owned", "📀"),
    ("puzzle", "🧩"),
    ("chess", "♟️"),
    ("instrument", "🎸"),
    ("repertoire", "📜"),
    ("clothing", "👕"),
    ("backpack", "🎒"),
    ("carry", "🎒"),
    ("android", "🤖"),
    ("windows", "🪟"),
    ("macos", "💻"),
    ("desktop", "🖥️"),
    ("work setup", "💼"),
    ("parity", "⚖️"),
    ("debug", "🐛"),
    ("deploy", "🚀"),
    ("quality", "✨"),
    ("observe", "👁️"),
    ("design", "🎨"),
    ("craft", "🛠️"),
    ("template", "📋"),
    ("diagram", "📊"),
    ("example", "💡"),
    ("palette", "🎨"),
    ("mermaid", "📊"),
    ("api", "🔌"),
    ("schema", "📐"),
    ("endpoint", "🌐"),
    ("architecture", "🏗️"),
    ("workflow", "🔁"),
    ("operation", "⚙️"),
    ("manifest", "📜"),
    ("convention", "📜"),
    ("knowledge", "🧠"),
    ("organization", "🗂️"),
    ("module", "📦"),
    ("data ", "💾"),
    ("storage", "💿"),
    ("migration", "🚚"),
    ("model", "🧩"),
    ("wonder", "✨"),
    ("metaphor", "🔗"),
    ("life ", "🌿"),
    ("philosoph", "🤔"),
    ("lineage", "🌳"),
    ("opposite", "↔️"),
    ("notes", "📝"),
    ("note", "📝"),
    ("convention", "📜"),
    ("purpose", "🎯"),
    ("table", "📊"),
    ("style guide", "✍️"),
    ("hub", "🗂️"),
    ("archive", "🗄️"),
    ("leaf", "📄"),
    ("root", "🌳"),
    ("scaffold", "🏗️"),
    ("comparison", "⚖️"),
    ("title", "🏷️"),
    ("git", "🔀"),
    ("pull", "⬇️"),
    ("push", "⬆️"),
    ("main align", "🎯"),
    ("reset", "↩️"),
    ("start branch", "🌿"),
    ("issue", "🎫"),
    ("pr ", "🔀"),
    ("fullstack", "🖥️"),
    ("frontend", "🖼️"),
    ("backend", "⚙️"),
    ("study", "📚"),
    ("topic", "📌"),
    ("checklist", "☑️"),
    ("playbook", "📕"),
    ("explanation", "💡"),
    ("index", "📑"),
    ("shared", "🔗"),
    ("tooling", "🧰"),
    ("coding", "💻"),
    ("profile", "👤"),
    ("verify", "✅"),
    ("publish", "🚀"),
    ("topology", "🕸️"),
    ("provenance", "📎"),
    ("writing style", "✍️"),
    ("linking", "🔗"),
    ("local preview", "👁️"),
    ("export", "📤"),
    ("setup", "⚙️"),
    ("how we group", "🗂️"),
    ("goal", "🎯"),
    ("portrait", "🖼️"),
    ("landscape", "🖼️"),
    ("genre", "🎭"),
    ("situation", "🎬"),
    ("queue", "📋"),
    ("to buy", "🛒"),
    ("emulation", "👾"),
    ("lanes", "🛤️"),
    ("runbook", "📓"),
    ("live channel", "📡"),
    ("soft vocal", "🎤"),
    ("reggae", "🎵"),
    ("rap", "🎤"),
    ("hypnotize", "🌀"),
    ("naruto", "🍥"),
    ("sertanejo", "🤠"),
    ("piseiro", "🤠"),
    ("funk", "🕺"),
    ("blues", "🎸"),
    ("sonic", "💨"),
    ("rock", "🎸"),
    ("happy", "😊"),
    ("calm", "🌙"),
    ("sad", "💧"),
    ("reverb", "🌊"),
    ("soundtrack", "🎬"),
    ("veigar", "🎮"),
    ("white coffee", "☕"),
    ("math remix", "🔢"),
    ("dark magician", "🃏"),
    ("synchronized", "🏊"),
    ("felix", "🐱"),
    ("orochimaru", "🐍"),
    ("uchiha", "🔥"),
    ("cursed seal", "🌀"),
    ("goal", "🎯"),
    ("storage", "🗄️"),
    ("fridge", "❄️"),
    ("freeze", "🧊"),
    ("pressure", "🫕"),
    ("brown", "🟤"),
    ("simmer", "♨️"),
    ("final", "🏁"),
    ("why ", "💡"),
    ("context", "🧩"),
    ("signals", "📡"),
    ("stops", "🛑"),
    ("lifecycle", "♻️"),
    ("shipping", "📦"),
    ("skills", "🧩"),
    ("hub", "🗂️"),
    ("bootstrap", "🚀"),
    ("triage", "🔍"),
    ("reshape", "✂️"),
    ("modes", "🎛️"),
    ("models", "🧠"),
    ("creativity", "✨"),
    ("task", "📋"),
    ("agents", "🤖"),
    ("patterns", "🔁"),
    ("calm read", "😌"),
    ("next priority", "⏭️"),
    ("split spike", "🔀"),
    ("plan mode", "📐"),
    ("execute", "▶️"),
    ("good enough", "✅"),
    ("idea", "💡"),
    ("ui context", "🖼️"),
    ("resolution", "✅"),
    ("post-merge", "✅"),
    ("quick shipping", "🚀"),
    ("prod ui", "🖥️"),
    ("flow", "🌊"),
]


def pick_emoji(title: str) -> str:
    t = title.lower()
    for kw, em in KEYWORD_EMOJI:
        if kw in t:
            return em
    return "📌"


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    fence = False
    changed = False

    for line in lines:
        raw = line.rstrip("\n\r")
        stripped = raw.lstrip()

        if stripped.startswith("```"):
            fence = not fence
            out.append(line)
            continue

        if fence:
            out.append(line)
            continue

        m = HEADING.match(raw)
        if m:
            hashes, rest = m.group(1), m.group(2)
            if title_has_leading_emoji(rest):
                out.append(line)
                continue
            # strip existing leading punctuation cluster for duplicate runs
            em = pick_emoji(rest)
            new_line = f"{hashes} {em} {rest}"
            if new_line != raw:
                changed = True
                suffix = line[len(raw) :]
                out.append(new_line + suffix)
                continue

        out.append(line)

    if changed:
        path.write_text("".join(out), encoding="utf-8")
    return changed


def main() -> int:
    md_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    n = 0
    for p in md_files:
        if "node_modules" in p.parts:
            continue
        try:
            if process_file(p):
                n += 1
                print(p.relative_to(ROOT))
        except OSError as e:
            print(f"skip {p}: {e}", file=sys.stderr)
    print(f"Updated {n} files.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
