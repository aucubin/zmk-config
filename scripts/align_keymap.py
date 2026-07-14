#!/usr/bin/env python3
"""Align ZMK `bindings = < ... >;` key-layout arrays into neat columns.

ZMK keymap files are hand formatted with extra spaces so that keys that sit
in the same physical column line up visually across rows (and usually across
layers too). Editing a single binding (e.g. swapping `&lt` for a longer
behavior name) easily throws that alignment off, and re-aligning everything
by hand is tedious and error prone.

This script re-derives the column layout directly from the existing spacing
in the file (so it works for any keyboard shape, not just simple grids) and
rewrites every multi-line `bindings = < ... >;` array with consistent,
minimal padding:

 1. Every binding ("&kp Q", "&hm LSHIFT T", "&lt NAV SPACE", ...) in the file
    is located, together with the character column it currently starts at.
 2. Columns that start at (almost) the same character offset anywhere in the
    file are treated as the same logical "column" (this naturally captures
    things like thumb keys lining up with the innermost finger columns).
 3. For each logical column, the width is the length of its longest
    occupant, so every row can be reformatted with a fixed, minimal gap
    between columns while keeping everything aligned.

Usage:
    python3 scripts/align_keymap.py                 # format every *.keymap
                                                       # file under config/
    python3 scripts/align_keymap.py path/to/a.keymap [more.keymap ...]
    python3 scripts/align_keymap.py --check ...      # exit 1 if files would
                                                       # change, without
                                                       # writing anything
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

GAP = 2  # minimum spaces inserted between two adjacent columns
CLUSTER_TOLERANCE = 4  # max character distance to treat two offsets as the same column

REPO_ROOT = Path(__file__).resolve().parent.parent

_BINDINGS_START_RE = re.compile(r"bindings\s*=\s*<\s*$")


def _find_blocks(lines: list[str]) -> list[tuple[int, int]]:
    """Return (start, end) inclusive line-index ranges of every row inside a
    multi-line `bindings = < ... >;` array (excluding the `bindings = <` and
    `>;` lines themselves)."""
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        if _BINDINGS_START_RE.search(lines[i]):
            j = i + 1
            while j < n and lines[j].strip() != ">;":
                j += 1
            if j < n:
                if j - 1 >= i + 1:
                    blocks.append((i + 1, j - 1))
                i = j + 1
                continue
        i += 1
    return blocks


def _tokenize_row(line: str) -> list[tuple[int, str]]:
    """Split a row into (start_column, binding_text) groups. A group starts
    at a token beginning with '&' and swallows any following tokens that
    don't start with '&' (so multi-word bindings like `&hm LSHIFT T` stay
    together)."""
    tokens: list[tuple[int, str]] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i].isspace():
            i += 1
            continue
        start = i
        while i < n and not line[i].isspace():
            i += 1
        tokens.append((start, line[start:i]))

    groups: list[tuple[int, str]] = []
    idx = 0
    while idx < len(tokens):
        start, text = tokens[idx]
        if text.startswith("&"):
            parts = [text]
            idx += 1
            while idx < len(tokens) and not tokens[idx][1].startswith("&"):
                parts.append(tokens[idx][1])
                idx += 1
            groups.append((start, " ".join(parts)))
        else:
            # Stray token that isn't part of any binding group; ignore.
            idx += 1
    return groups


def align_text(text: str) -> str:
    trailing_newline = text.endswith("\n")
    lines = text.split("\n")

    blocks = _find_blocks(lines)
    if not blocks:
        return text

    # Collect every binding group across all blocks, with its row and column.
    all_groups = []
    for start, end in blocks:
        for row_idx in range(start, end + 1):
            line = lines[row_idx]
            if not line.strip():
                continue
            for offset, group_text in _tokenize_row(line):
                all_groups.append({"row": row_idx, "offset": offset, "text": group_text})

    if not all_groups:
        return text

    base_indent = min(g["offset"] for g in all_groups)
    for g in all_groups:
        g["rel"] = g["offset"] - base_indent

    distinct_offsets = sorted(set(g["rel"] for g in all_groups))
    clusters: list[list[int]] = []
    for off in distinct_offsets:
        if clusters and off - clusters[-1][-1] <= CLUSTER_TOLERANCE:
            clusters[-1].append(off)
        else:
            clusters.append([off])

    offset_to_cluster = {}
    for cluster_idx, cluster_offsets in enumerate(clusters):
        for off in cluster_offsets:
            offset_to_cluster[off] = cluster_idx

    cluster_width = [0] * len(clusters)
    for g in all_groups:
        c = offset_to_cluster[g["rel"]]
        g["cluster"] = c
        cluster_width[c] = max(cluster_width[c], len(g["text"]))

    row_map: dict[int, dict[int, str]] = {}
    for g in all_groups:
        row_map.setdefault(g["row"], {})[g["cluster"]] = g["text"]

    indent_str = " " * base_indent
    new_lines = list(lines)
    for row_idx, cmap in row_map.items():
        last_cluster = max(cmap.keys())
        fields = []
        for c in range(last_cluster + 1):
            width = cluster_width[c]
            field = cmap.get(c, "")
            fields.append(field.ljust(width))
        row_text = indent_str + (" " * GAP).join(fields)
        new_lines[row_idx] = row_text.rstrip()

    new_text = "\n".join(new_lines)
    if trailing_newline and not new_text.endswith("\n"):
        new_text += "\n"
    return new_text


def align_file(path: Path) -> bool:
    """Align a single file in place. Returns True if the file changed."""
    original = path.read_text()
    aligned = align_text(original)
    if aligned != original:
        path.write_text(aligned)
        return True
    return False


def discover_keymap_files() -> list[Path]:
    config_dir = REPO_ROOT / "config"
    return sorted(config_dir.rglob("*.keymap"))


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    file_args = [a for a in argv if a != "--check"]

    if file_args:
        files = [Path(a) for a in file_args]
    else:
        files = discover_keymap_files()

    if not files:
        print("No .keymap files found.")
        return 0

    changed_any = False
    for path in files:
        original = path.read_text()
        aligned = align_text(original)
        changed = aligned != original
        if changed:
            changed_any = True
            if check_only:
                print(f"would reformat: {path}")
            else:
                path.write_text(aligned)
                print(f"reformatted: {path}")
        else:
            print(f"unchanged: {path}")

    if check_only and changed_any:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
