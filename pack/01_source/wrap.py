#!/usr/bin/env python3
"""Markdown lesson → offline HTML with sticky nav. No external deps."""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "02_lessons"
PACK = "Atlas of the Build Loop"

NAV = [
    ("01_The_Loop", "L01 Loop"),
    ("02_Project_Management_Methodology", "L02 Methods"),
    ("03_Communicating_Intent", "L03 Intent"),
    ("04_Brainstorming", "L04 Brainstorm"),
    ("05_Prototyping", "L05 Prototype"),
    ("06_Review", "L06 Review"),
    ("07_Iteration_and_Shipping", "L07 Ship"),
]


def _fmt(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    return s


def inline(s: str) -> str:
    parts: list[str] = []
    last = 0
    for m in re.finditer(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", s):
        parts.append(_fmt(s[last:m.start()]))
        parts.append(
            f'<a class="ext" href="{html.escape(m.group(2), quote=True)}" '
            f'target="_blank" rel="noopener noreferrer">{_fmt(m.group(1))}</a>'
        )
        last = m.end()
    parts.append(_fmt(s[last:]))
    return "".join(parts)


_BLOCK_TAG = re.compile(r"^<(figure|svg|div|section)\b", re.I)
_IMG_MD = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)$")


def _html_block(lines: list[str], i: int) -> tuple[str, int]:
    raw = lines[i]
    m = _BLOCK_TAG.match(raw.lstrip())
    if not m:
        return "", i
    tag = m.group(1)
    open_re = re.compile(rf"<{tag}\b", re.I)
    close_re = re.compile(rf"</{tag}>", re.I)
    buf = [raw]
    depth = len(open_re.findall(raw)) - len(close_re.findall(raw))
    i += 1
    while i < len(lines) and depth > 0:
        buf.append(lines[i])
        depth += len(open_re.findall(lines[i])) - len(close_re.findall(lines[i]))
        i += 1
    return "\n".join(buf), i


def convert(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    in_ul = in_ol = in_table = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def close_table():
        nonlocal in_table
        if in_table:
            out.append("</tbody></table>")
            in_table = False

    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()

        if _BLOCK_TAG.match(line.lstrip()):
            close_lists()
            close_table()
            block, i = _html_block(lines, i)
            out.append(block)
            continue

        img = _IMG_MD.match(line.strip())
        if img:
            close_lists()
            close_table()
            alt, src = img.group(1), img.group(2)
            out.append(
                f'<figure class="fig pic"><img src="{html.escape(src, quote=True)}" '
                f'alt="{html.escape(alt)}"/></figure>'
            )
            i += 1
            continue

        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*-+", lines[i + 1]):
            close_lists()
            close_table()
            headers = [c.strip() for c in line.strip("|").split("|")]
            i += 2
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(h)}</th>" for h in headers) + "</tr></thead><tbody>")
            in_table = True
            continue

        if in_table:
            if line.startswith("|"):
                cells = [c.strip() for c in line.strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
                i += 1
                continue
            close_table()

        if not line.strip():
            close_lists()
            i += 1
            continue

        if line.startswith("```"):
            close_lists()
            close_table()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(html.escape(lines[i]))
                i += 1
            i += 1
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>")
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            close_lists()
            close_table()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            i += 1
            continue

        if re.match(r"^[-*]\s+", line):
            close_table()
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append("<li>" + inline(re.sub(r"^[-*]\s+", "", line)) + "</li>")
            i += 1
            continue

        if re.match(r"^\d+\.\s+", line):
            close_table()
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append("<li>" + inline(re.sub(r"^\d+\.\s+", "", line)) + "</li>")
            i += 1
            continue

        if line.startswith(">"):
            close_lists()
            close_table()
            out.append(f"<blockquote>{inline(line.lstrip('> ').strip())}</blockquote>")
            i += 1
            continue

        close_lists()
        close_table()
        out.append(f"<p>{inline(line)}</p>")
        i += 1

    close_lists()
    close_table()
    return "\n".join(out)


HERO = {
    "01_The_Loop": ("arc-a.jpg", "A builder at a whiteboard drawing a loop in morning light"),
    "02_Project_Management_Methodology": ("arc-b.jpg", "Two tracks on a table: a calendar and a brief"),
    "03_Communicating_Intent": ("arc-b.jpg", "A brief and a compass on a worktable"),
    "04_Brainstorming": ("arc-c.jpg", "Paper, notes, and analog generation tools"),
    "05_Prototyping": ("arc-c.jpg", "Cardboard and clay on a workbench"),
    "06_Review": ("arc-d.jpg", "Notebook and a closed package in late light"),
    "07_Iteration_and_Shipping": ("arc-d.jpg", "A package ready to leave the bench"),
}


def wrap(stem: str, title: str, body_html: str) -> str:
    stems = [s for s, _ in NAV]
    idx = stems.index(stem)
    prev_h = f'<a href="{stems[idx-1]}.html">← Prev</a>' if idx > 0 else ""
    next_h = f'<a href="{stems[idx+1]}.html">Next →</a>' if idx < len(stems) - 1 else ""
    hero = ""
    if stem in HERO:
        src, alt = HERO[stem]
        hero = f'<figure class="lesson-hero"><img src="../assets/{src}" alt="{html.escape(alt)}"/></figure>'
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{html.escape(title)} — {html.escape(PACK)}</title>
<link rel="stylesheet" href="../assets/pack.css"/>
</head><body>
<div class="lesson-wrap">
<nav class="lesson-nav"><a href="../index.html">Cover</a> <a href="../contents.html">Contents</a> <a href="../decks.html">Quiz</a> <a href="../04_labs/index.html">Labs</a> <a href="../dashboard.html">Dashboard</a> {prev_h} {next_h} <button type="button" class="theme-btn" data-theme-toggle>Dim mode</button><div class="mark">{html.escape(PACK)}</div></nav>
{hero}
<article class="lesson">
<div class="badge">Dense lesson · professional practice · educational only</div>
{body_html}
<div class="footer">Offline study pack. Progress is stored in this browser only. Optional “Learn more” links open the public homes of named methods.</div>
</article>
</div>
<script src="../assets/theme.js"></script>
</body></html>
"""


def main() -> None:
    for stem, _ in NAV:
        md_path = LESSONS / f"{stem}.md"
        md = md_path.read_text(encoding="utf-8")
        title = md.splitlines()[0].lstrip("# ").strip()
        html_doc = wrap(stem, title, convert(md))
        (LESSONS / f"{stem}.html").write_text(html_doc, encoding="utf-8")
        print("wrote", stem)


if __name__ == "__main__":
    main()
