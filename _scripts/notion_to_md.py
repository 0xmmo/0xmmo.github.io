#!/usr/bin/env python3
"""Convert a public Notion page to a Jekyll-flavored Markdown post.

Usage:
    python3 _scripts/notion_to_md.py <page-id-or-url> [slug]

Output is written to _posts/<YYYY-MM-DD>-<slug>.md relative to the repo
root. If no slug is given, one is derived from the page title.

Block types supported: text, header, sub_header, sub_sub_header,
bulleted_list, numbered_list, code, divider, quote. Inline
annotations: bold (b), italic (i), code (c), strikethrough (s),
link (a).
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "https://www.notion.so/api/v3/loadPageChunk"


def _hyphenate(pid: str) -> str:
    pid = pid.replace("-", "")
    if len(pid) != 32:
        raise SystemExit(f"bad page id: {pid!r}")
    return f"{pid[0:8]}-{pid[8:12]}-{pid[12:16]}-{pid[16:20]}-{pid[20:32]}"


def _id_from_arg(arg: str) -> str:
    m = re.search(r"([0-9a-f]{32})", arg, re.IGNORECASE)
    if not m:
        raise SystemExit(f"could not find page id in {arg!r}")
    return _hyphenate(m.group(1))


def _fetch_chunks(page_id: str) -> dict:
    merged: dict = {}
    cursor = {"stack": []}
    chunk_no = 0
    while True:
        body = json.dumps({
            "pageId": page_id, "limit": 100, "cursor": cursor,
            "chunkNumber": chunk_no, "verticalColumns": False,
        }).encode("utf-8")
        req = urllib.request.Request(
            API, data=body,
            headers={"Content-Type": "application/json", "User-Agent": "mmoustafa-blog/1"},
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read())
        for bid, val in (data.get("recordMap", {}).get("block") or {}).items():
            merged[bid] = val
        cur = data.get("cursor", {})
        if not cur.get("stack"):
            break
        cursor = cur
        chunk_no += 1
    return merged


def _val(block_map: dict, bid: str) -> dict | None:
    b = block_map.get(bid)
    return (b.get("value", {}).get("value") if b else None) or None


def _plain(title_array: list) -> str:
    return "".join(seg[0] if seg else "" for seg in (title_array or []))


def _md_inline(title_array: list) -> str:
    """Notion inline → Markdown. Order matters because some annotations
    nest (e.g. a bold link). Notion annotations on a segment apply to the
    whole segment, so we wrap from innermost out."""
    if not title_array:
        return ""
    parts: list[str] = []
    for seg in title_array:
        text = seg[0] if seg else ""
        ann = seg[1] if len(seg) > 1 else []
        # Escape characters that would otherwise be interpreted as Markdown
        # syntax inside this run. Keep it minimal so prose stays readable.
        # We don't escape inside links/code (handled below).
        out = text

        link_url: str | None = None
        wraps: list[tuple[str, str]] = []  # innermost-first
        for a in ann or []:
            kind = a[0]
            if kind == "c":
                wraps.append(("`", "`"))
            elif kind == "b":
                wraps.append(("**", "**"))
            elif kind == "i":
                wraps.append(("*", "*"))
            elif kind == "s":
                wraps.append(("~~", "~~"))
            elif kind == "a":
                link_url = a[1] if len(a) > 1 else None

        # If the run is inline code, do NOT escape — code spans are verbatim.
        is_code = any(w[0] == "`" for w in wraps)
        if not is_code:
            out = re.sub(r"([\\`*_\[\]])", r"\\\1", out)

        for open_t, close_t in wraps:
            out = f"{open_t}{out}{close_t}"
        if link_url:
            out = f"[{out}]({link_url})"
        parts.append(out)
    return "".join(parts)


HEADER_HASH = {"header": "## ", "sub_header": "### ", "sub_sub_header": "#### "}


def _render_blocks(block_map: dict, content_ids: list[str]) -> str:
    out: list[str] = []
    list_kind: str | None = None  # "bulleted_list" | "numbered_list"
    list_index = 0

    def flush_list():
        nonlocal list_kind, list_index
        list_kind = None
        list_index = 0

    for bid in content_ids:
        v = _val(block_map, bid)
        if not v:
            continue
        t = v.get("type")
        title = v.get("properties", {}).get("title", [])

        if t in ("bulleted_list", "numbered_list"):
            if list_kind != t:
                flush_list()
                list_kind = t
                list_index = 0
            list_index += 1
            marker = "-" if t == "bulleted_list" else f"{list_index}."
            out.append(f"{marker} {_md_inline(title)}")
            continue
        flush_list()

        if t == "text":
            inline = _md_inline(title)
            if inline.strip():
                out.append(inline)
                out.append("")  # blank line between paragraphs
        elif t in HEADER_HASH:
            out.append(f"{HEADER_HASH[t]}{_md_inline(title)}")
            out.append("")
        elif t == "code":
            lang_arr = v.get("properties", {}).get("language", [])
            lang = (lang_arr[0][0] if lang_arr else "").lower()
            # Languages with spaces (e.g. "plain text") aren't valid fence infostrings
            lang = re.sub(r"[^a-z0-9+\-]+", "", lang) if lang else ""
            code = _plain(title).rstrip("\n")
            out.append(f"```{lang}")
            out.append(code)
            out.append("```")
            out.append("")
        elif t == "divider":
            out.append("---")
            out.append("")
        elif t == "quote":
            for line in _md_inline(title).splitlines() or [""]:
                out.append(f"> {line}")
            out.append("")
        else:
            out.append(f"<!-- unsupported block type: {t} -->")
    return "\n".join(out).rstrip() + "\n"


def _slugify(title: str) -> str:
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "post"


def render(page_arg: str, slug_override: str | None, posts_dir: Path) -> Path:
    page_id = _id_from_arg(page_arg)
    block_map = _fetch_chunks(page_id)
    page = _val(block_map, page_id)
    if not page or page.get("type") != "page":
        raise SystemExit(f"page block not found for {page_id}")

    title = _plain(page.get("properties", {}).get("title", []))
    icon = page.get("format", {}).get("page_icon") or ""
    created_ms = page.get("created_time") or 0
    edited_ms = page.get("last_edited_time") or 0
    dt = datetime.fromtimestamp(created_ms / 1000, tz=timezone.utc)
    date_yaml = dt.strftime("%Y-%m-%d %H:%M:%S %z")
    date_fname = dt.strftime("%Y-%m-%d")

    body = _render_blocks(block_map, page.get("content", []))
    slug = slug_override or _slugify(title)

    # Build excerpt: first non-empty paragraph, trimmed.
    excerpt = ""
    for bid in page.get("content", []):
        v = _val(block_map, bid)
        if v and v.get("type") == "text":
            t = _plain(v.get("properties", {}).get("title", [])).strip()
            if t:
                excerpt = t
                break
    excerpt = re.sub(r"\s+", " ", excerpt)[:200]
    if len(excerpt) >= 200:
        excerpt = excerpt.rsplit(" ", 1)[0] + "…"

    fm_lines = ["---", "layout: post"]
    # Quote the title — Notion titles can include colons and quotes
    safe_title = title.replace('"', '\\"')
    fm_lines.append(f'title: "{safe_title}"')
    fm_lines.append(f"date: {date_yaml}")
    if icon:
        fm_lines.append(f"icon: {icon}")
    if excerpt:
        safe_excerpt = excerpt.replace('"', '\\"')
        fm_lines.append(f'excerpt: "{safe_excerpt}"')
    fm_lines.append(f"notion_id: {page_id}")
    fm_lines.append("---")

    out_text = "\n".join(fm_lines) + "\n\n" + body
    out_path = posts_dir / f"{date_fname}-{slug}.md"
    out_path.write_text(out_text, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("usage: notion_to_md.py <page-url-or-id> [slug]", file=sys.stderr)
        raise SystemExit(2)
    repo_root = Path(__file__).resolve().parent.parent
    posts_dir = repo_root / "_posts"
    posts_dir.mkdir(parents=True, exist_ok=True)
    slug = sys.argv[2] if len(sys.argv) == 3 else None
    p = render(sys.argv[1], slug, posts_dir)
    print(f"wrote {p}")
