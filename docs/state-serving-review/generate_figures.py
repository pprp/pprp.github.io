#!/usr/bin/env python3

from __future__ import annotations

import html
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
import textwrap
from typing import Iterable
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


THEME = {
    "bg": "#F8FAFC",
    "paper": "#FFFFFF",
    "grid": "#E2E8F0",
    "text": "#0F172A",
    "muted": "#475569",
    "border": "#CBD5E1",
    "navy": "#1D4ED8",
    "teal": "#0F766E",
    "amber": "#B45309",
    "violet": "#7C3AED",
    "rose": "#BE123C",
    "slate": "#64748B",
    "blue_tint": "#EFF6FF",
    "teal_tint": "#F0FDFA",
    "amber_tint": "#FFF7ED",
    "violet_tint": "#F5F3FF",
    "rose_tint": "#FFF1F2",
    "slate_tint": "#F8FAFC",
}


ACCENTS = {
    "navy": (THEME["navy"], THEME["blue_tint"]),
    "teal": (THEME["teal"], THEME["teal_tint"]),
    "amber": (THEME["amber"], THEME["amber_tint"]),
    "violet": (THEME["violet"], THEME["violet_tint"]),
    "rose": (THEME["rose"], THEME["rose_tint"]),
    "slate": (THEME["slate"], THEME["slate_tint"]),
}


@dataclass
class Box:
    id: str
    x: int
    y: int
    w: int
    h: int
    title: str
    lines: list[str] = field(default_factory=list)
    accent: str = "navy"
    kind: str = "node"
    dashed: bool = False
    align: str = "left"
    small: bool = False


@dataclass
class Arrow:
    id: str
    source: str
    target: str
    color: str = "slate"
    label: str = ""
    dashed: bool = False
    points: list[tuple[int, int]] = field(default_factory=list)


@dataclass
class Legend:
    items: list[tuple[str, str]]
    x: int
    y: int


@dataclass
class Figure:
    name: str
    title: str
    subtitle: str
    width: int
    height: int
    boxes: list[Box]
    arrows: list[Arrow]
    legends: list[Legend] = field(default_factory=list)
    footnotes: list[str] = field(default_factory=list)


def accent_colors(name: str) -> tuple[str, str]:
    return ACCENTS[name]


def rounded_rect_svg(x: int, y: int, w: int, h: int, fill: str, stroke: str, dashed: bool = False) -> str:
    dash = ' stroke-dasharray="8 6"' if dashed else ""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" ry="18" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="2"{dash}/>'
    )


def text_block_svg(box: Box) -> str:
    fill, tint = accent_colors(box.accent)
    anchor = "middle" if box.align == "center" else "start"
    tx = box.x + box.w / 2 if box.align == "center" else box.x + 28
    y = box.y + 36
    pieces = []
    title_size = 24 if (not box.small and box.w >= 280) else 20 if not box.small else 18
    body_size = 18 if (not box.small and box.w >= 260) else 16 if not box.small else 15
    title_lines = wrap_box_text(box.title, box.w, title_size)
    title_y = y
    for idx, line in enumerate(title_lines):
        pieces.append(
            f'<text x="{tx}" y="{title_y + idx * (title_size + 4)}" text-anchor="{anchor}" font-size="{title_size}" '
            f'font-weight="700" fill="{THEME["text"]}">{html.escape(line)}</text>'
        )
    body_start = title_y + len(title_lines) * (title_size + 4) + 12
    body_lines: list[str] = []
    for line in box.lines:
        body_lines.extend(wrap_box_text(line, box.w, body_size))
    for idx, line in enumerate(body_lines):
        pieces.append(
            f'<text x="{tx}" y="{body_start + idx * (body_size + 8)}" text-anchor="{anchor}" font-size="{body_size}" '
            f'font-weight="500" fill="{THEME["muted"]}">{html.escape(line)}</text>'
        )
    accent_x = box.x + 1
    accent_y = box.y + 1
    accent_w = box.w - 2
    accent_h = 8 if box.kind != "group" else 6
    pieces.insert(
        0,
        f'<rect x="{accent_x}" y="{accent_y}" width="{accent_w}" height="{accent_h}" rx="17" ry="17" fill="{fill}"/>',
    )
    return "\n".join(pieces)


def group_label_svg(box: Box) -> str:
    fill, _ = accent_colors(box.accent)
    return (
        f'<text x="{box.x + 20}" y="{box.y - 10}" font-size="16" font-weight="700" '
        f'fill="{fill}" letter-spacing="1.2">{html.escape(box.title.upper())}</text>'
    )


def arrow_path(points: list[tuple[int, int]]) -> str:
    first = points[0]
    commands = [f"M {first[0]} {first[1]}"]
    for x, y in points[1:]:
        commands.append(f"L {x} {y}")
    return " ".join(commands)


def wrap_box_text(text: str, width: int, font_size: int) -> list[str]:
    max_chars = max(12, int((width - 48) / max(font_size * 0.56, 1)))
    return textwrap.wrap(text, width=max_chars, break_long_words=False, break_on_hyphens=False) or [text]


def edge_points(fig: Figure, arrow: Arrow) -> list[tuple[int, int]]:
    box_map = {box.id: box for box in fig.boxes}
    source = box_map[arrow.source]
    target = box_map[arrow.target]
    sx = source.x + source.w
    sy = source.y + source.h / 2
    tx = target.x
    ty = target.y + target.h / 2
    if arrow.points:
        return [(int(sx), int(sy)), *arrow.points, (int(tx), int(ty))]
    return [(int(sx), int(sy)), (int((sx + tx) / 2), int(sy)), (int((sx + tx) / 2), int(ty)), (int(tx), int(ty))]


def svg_for_figure(fig: Figure) -> str:
    foot_y = fig.height - 72
    content = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{fig.width}" height="{fig.height}" '
        f'viewBox="0 0 {fig.width} {fig.height}">',
        "<defs>",
        f'<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="{THEME["grid"]}" stroke-width="1"/></pattern>',
        f'<marker id="arrow-slate" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{THEME["slate"]}"/></marker>',
        f'<marker id="arrow-navy" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{THEME["navy"]}"/></marker>',
        f'<marker id="arrow-teal" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{THEME["teal"]}"/></marker>',
        f'<marker id="arrow-amber" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{THEME["amber"]}"/></marker>',
        f'<marker id="arrow-violet" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{THEME["violet"]}"/></marker>',
        "</defs>",
        "<style>",
        "text { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif; }",
        "</style>",
        f'<rect width="{fig.width}" height="{fig.height}" fill="{THEME["bg"]}"/>',
        f'<rect width="{fig.width}" height="{fig.height}" fill="url(#grid)" opacity="0.55"/>',
        f'<rect x="36" y="28" width="{fig.width - 72}" height="{fig.height - 56}" rx="26" ry="26" fill="rgba(255,255,255,0.0)" stroke="{THEME["grid"]}" stroke-width="1.5"/>',
        f'<text x="56" y="70" font-size="32" font-weight="800" fill="{THEME["text"]}">{html.escape(fig.title)}</text>',
        f'<text x="56" y="102" font-size="18" font-weight="500" fill="{THEME["muted"]}">{html.escape(fig.subtitle)}</text>',
    ]
    for box in fig.boxes:
        fill, tint = accent_colors(box.accent)
        if box.kind == "group":
            content.append(group_label_svg(box))
            content.append(rounded_rect_svg(box.x, box.y, box.w, box.h, "none", fill, dashed=True))
        else:
            content.append(rounded_rect_svg(box.x, box.y, box.w, box.h, tint if box.kind == "note" else THEME["paper"], fill if box.kind == "note" else THEME["border"], dashed=box.dashed))
            content.append(text_block_svg(box))
    for arrow in fig.arrows:
        color = THEME[arrow.color]
        pts = edge_points(fig, arrow)
        dash = ' stroke-dasharray="10 8"' if arrow.dashed else ""
        content.append(
            f'<path d="{arrow_path(pts)}" fill="none" stroke="{color}" stroke-width="3" marker-end="url(#arrow-{arrow.color})"{dash}/>'
        )
        if arrow.label:
            mid = pts[len(pts) // 2]
            lx = mid[0] + 10
            ly = mid[1] - 10
            label_w = max(120, len(arrow.label) * 9 + 22)
            content.append(
                f'<rect x="{lx - 6}" y="{ly - 22}" width="{label_w}" height="30" rx="12" ry="12" fill="{THEME["paper"]}" stroke="{THEME["grid"]}" stroke-width="1"/>'
            )
            content.append(
                f'<text x="{lx + 8}" y="{ly - 2}" font-size="14" font-weight="600" fill="{THEME["muted"]}">{html.escape(arrow.label)}</text>'
            )
    for legend in fig.legends:
        current_y = legend.y
        for color_name, label in legend.items:
            color = THEME[color_name]
            content.append(f'<line x1="{legend.x}" y1="{current_y}" x2="{legend.x + 26}" y2="{current_y}" stroke="{color}" stroke-width="3" marker-end="url(#arrow-{color_name})"/>')
            content.append(
                f'<text x="{legend.x + 40}" y="{current_y + 5}" font-size="14" font-weight="600" fill="{THEME["muted"]}">{html.escape(label)}</text>'
            )
            current_y += 22
    for idx, note in enumerate(fig.footnotes):
        content.append(
            f'<text x="56" y="{foot_y + idx * 22}" font-size="15" font-weight="500" fill="{THEME["muted"]}">{html.escape(note)}</text>'
        )
    content.append("</svg>")
    return "\n".join(content)


def box_html_label(box: Box) -> str:
    title_lines = wrap_box_text(box.title, box.w, 22 if not box.small else 18)
    body_lines: list[str] = []
    for line in box.lines:
        body_lines.extend(wrap_box_text(line, box.w, 16 if not box.small else 14))
    title = "<b>" + "<br/>".join(html.escape(line) for line in title_lines) + "</b>"
    lines = "<br/>".join(html.escape(line) for line in body_lines)
    return title if not lines else f"{title}<br/>{lines}"


def mx_geometry(parent: ET.Element, x: int, y: int, w: int, h: int) -> None:
    geo = ET.SubElement(parent, "mxGeometry")
    geo.set("x", str(x))
    geo.set("y", str(y))
    geo.set("width", str(w))
    geo.set("height", str(h))
    geo.set("as", "geometry")


def drawio_for_figure(fig: Figure) -> ET.Element:
    diagram = ET.Element("diagram", {"id": fig.name, "name": fig.name})
    model = ET.SubElement(
        diagram,
        "mxGraphModel",
        {
            "dx": "1600",
            "dy": "900",
            "grid": "1",
            "gridSize": "16",
            "guides": "1",
            "tooltips": "1",
            "connect": "1",
            "arrows": "1",
            "fold": "1",
            "page": "1",
            "pageScale": "1",
            "pageWidth": str(fig.width),
            "pageHeight": str(fig.height),
            "math": "0",
            "shadow": "0",
        },
    )
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    title_cell = ET.SubElement(
        root,
        "mxCell",
        {
            "id": f"{fig.name}-title",
            "value": f"<b>{html.escape(fig.title)}</b><br/>{html.escape(fig.subtitle)}",
            "style": "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#e2e8f0;strokeWidth=1.5;fontColor=#0f172a;fontSize=18;spacing=10;align=left;verticalAlign=middle;",
            "vertex": "1",
            "parent": "1",
        },
    )
    mx_geometry(title_cell, 48, 36, fig.width - 96, 72)

    for box in fig.boxes:
        accent, tint = accent_colors(box.accent)
        if box.kind == "group":
            group = ET.SubElement(
                root,
                "mxCell",
                {
                    "id": box.id,
                    "value": "",
                    "style": f"rounded=1;whiteSpace=wrap;html=1;fillColor=none;strokeColor={accent};strokeWidth=1.5;dashed=1;dashPattern=8 6;",
                    "vertex": "1",
                    "parent": "1",
                },
            )
            mx_geometry(group, box.x, box.y, box.w, box.h)
            group_label = ET.SubElement(
                root,
                "mxCell",
                {
                    "id": f"{box.id}-label",
                    "value": f"<b>{html.escape(box.title.upper())}</b>",
                    "style": f"text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontColor={accent};fontSize=14;fontStyle=1;",
                    "vertex": "1",
                    "parent": "1",
                },
            )
            mx_geometry(group_label, box.x + 16, box.y - 22, 240, 20)
            continue

        body_style = (
            f"rounded=1;whiteSpace=wrap;html=1;fillColor={'#ffffff' if box.kind != 'note' else tint};"
            f"strokeColor={THEME['border'] if box.kind != 'note' else accent};strokeWidth=1.5;"
            f"fontColor={THEME['text']};fontSize={'14' if box.small else '16'};spacingTop=12;spacingLeft=18;spacingRight=18;"
            f"align={'center' if box.align == 'center' else 'left'};verticalAlign=middle;"
        )
        cell = ET.SubElement(
            root,
            "mxCell",
            {
                "id": box.id,
                "value": box_html_label(box),
                "style": body_style,
                "vertex": "1",
                "parent": "1",
            },
        )
        mx_geometry(cell, box.x, box.y, box.w, box.h)

        accent_bar = ET.SubElement(
            root,
            "mxCell",
            {
                "id": f"{box.id}-accent",
                "value": "",
                "style": f"rounded=1;whiteSpace=wrap;html=1;fillColor={accent};strokeColor={accent};strokeWidth=1;",
                "vertex": "1",
                "parent": "1",
            },
        )
        mx_geometry(accent_bar, box.x + 2, box.y + 2, box.w - 4, 8)

    for arrow in fig.arrows:
        style = (
            f"edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
            f"endArrow=block;endFill=1;strokeColor={THEME[arrow.color]};strokeWidth=2.5;"
        )
        if arrow.dashed:
            style += "dashed=1;dashPattern=8 6;"
        edge = ET.SubElement(
            root,
            "mxCell",
            {
                "id": arrow.id,
                "value": html.escape(arrow.label),
                "style": style,
                "edge": "1",
                "parent": "1",
                "source": arrow.source,
                "target": arrow.target,
            },
        )
        geo = ET.SubElement(edge, "mxGeometry", {"relative": "1", "as": "geometry"})
        if arrow.points:
            arr = ET.SubElement(geo, "Array", {"as": "points"})
            for x, y in arrow.points:
                ET.SubElement(arr, "mxPoint", {"x": str(x), "y": str(y)})

    current_y = fig.height - 72
    for idx, note in enumerate(fig.footnotes):
        foot = ET.SubElement(
            root,
            "mxCell",
            {
                "id": f"{fig.name}-foot-{idx}",
                "value": html.escape(note),
                "style": "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontColor=#475569;fontSize=13;",
                "vertex": "1",
                "parent": "1",
            },
        )
        mx_geometry(foot, 56, current_y + idx * 22, fig.width - 112, 20)

    return diagram


def write_text(path: Path, content: str) -> None:
    path.write_text(content + "\n", encoding="utf-8")


def export_png(svg_path: Path) -> None:
    png_path = svg_path.with_suffix(".png")
    subprocess.run(
        ["rsvg-convert", "-w", "1920", str(svg_path), "-o", str(png_path)],
        check=True,
    )


def figures() -> Iterable[Figure]:
    yield Figure(
        name="fig01_architecture_landscape",
        title="Figure 1. Architectural routes from long context to state-centric serving",
        subtitle="Observed system pressure, current open-model responses, and the hypothesized Linear-first end-state",
        width=1600,
        height=980,
        boxes=[
            Box("g1", 72, 150, 1440, 260, "Observed pressure", accent="slate", kind="group"),
            Box("g2", 72, 450, 1440, 360, "Competing responses", accent="navy", kind="group"),
            Box("b1", 120, 194, 360, 164, "System bottleneck", ["KV cache grows with context length", "prefill/decode bandwidth couples serving", "agent workloads turn window size into time-horizon cost"], accent="amber"),
            Box("b2", 540, 194, 420, 164, "Market signal", ["products are advertising longer service duration", "not just larger context windows", "planning + tool use + continuity matter more"], accent="teal"),
            Box("b3", 1020, 194, 420, 164, "Research question", ["when service length T → ∞,", "should memory remain token-addressable,", "or become state-preserving and externally recallable?"], accent="violet"),
            Box("b4", 120, 508, 300, 208, "Full attention", ["strong exact token recall", "best-understood infrastructure", "but memory and bandwidth scale with history"], accent="rose"),
            Box("b5", 470, 508, 300, 208, "Hybrid", ["Qwen3.6 / Kimi Linear / OLMo Hybrid", "replace most layers with recurrent or linear state", "retain attention as a precision backstop"], accent="navy"),
            Box("b6", 820, 508, 300, 208, "Sparse / MLA / SWA", ["DeepSeek-V2/V3.x / GLM / sliding-window stacks", "compress or localize attention coverage", "preserve token-level addressing with better efficiency"], accent="teal"),
            Box("b7", 1170, 508, 300, 208, "Linear-first agent stack", ["bounded live state", "retrieval-triggered external recall", "persistent memory + tools + compaction"], accent="violet"),
            Box("b8", 400, 834, 800, 84, "Thesis", ["The endgame of long context is not a bigger window; it is a longer, state-centric service horizon."], accent="amber", align="center", small=True),
        ],
        arrows=[
            Arrow("a1", "b1", "b4", color="slate", label="baseline", points=[(300, 420), (300, 460)]),
            Arrow("a2", "b1", "b5", color="navy", label="reduce slope", points=[(460, 276), (520, 276), (520, 612)]),
            Arrow("a3", "b1", "b6", color="teal", label="compress cost", points=[(460, 326), (800, 326), (800, 612)]),
            Arrow("a4", "b2", "b7", color="violet", label="time-horizon shift", points=[(980, 276), (1140, 276), (1140, 612)]),
            Arrow("a5", "b5", "b7", color="navy", label="", points=[(790, 612), (1140, 612)]),
            Arrow("a6", "b6", "b7", color="teal", label="", points=[(1140, 612)]),
            Arrow("a7", "b7", "b8", color="amber", label="thesis", points=[(1320, 740), (1320, 876), (1200, 876)]),
        ],
        legends=[Legend([("navy", "state replacement"), ("teal", "attention compression"), ("amber", "paper thesis")], 1220, 860)],
        footnotes=[
            "Observed evidence: model cards, serving papers, and product docs.",
            "The Linear-first end-state is a forward-looking synthesis rather than an announced industry consensus.",
        ],
    )

    yield Figure(
        name="fig03_memory_stack",
        title="Figure 3. A four-layer memory stack for state-centric serving",
        subtitle="The useful distinction is not just short-term vs long-term, but parameter memory vs live state vs external memory vs tool-ground truth",
        width=1600,
        height=980,
        boxes=[
            Box("g1", 120, 152, 1120, 640, "Memory hierarchy", accent="slate", kind="group"),
            Box("n1", 1320, 214, 210, 108, "Fast / scarce", ["high-value state should stay here"], accent="amber", kind="note", small=True),
            Box("n2", 1320, 690, 210, 108, "Slow / rich", ["store explicit artifacts and fetch on demand"], accent="teal", kind="note", small=True),
            Box("b1", 220, 208, 920, 110, "Layer 1. Weights / parameter memory", ["general capabilities, broad priors, model identity", "slow to update, globally shared, expensive to personalize"], accent="navy"),
            Box("b2", 220, 350, 920, 132, "Layer 2. Live state / active horizon", ["task plan, current hypotheses, local variables, recent tool outcomes", "bounded by quality-cost trade-offs, not by the ambition to remember everything"], accent="amber"),
            Box("b3", 220, 528, 920, 132, "Layer 3. External memory artifacts", ["notes, AGENTS.md, memories, plans, retrieval indexes, structured summaries", "versionable, inspectable, shareable, and cheaper to persist than raw token history"], accent="teal"),
            Box("b4", 220, 706, 920, 110, "Layer 4. Tools and environment", ["repo state, databases, browsers, APIs, observability, real-world systems", "final truth source when the model must verify instead of merely remember"], accent="violet"),
            Box("b5", 68, 384, 124, 240, "Token-preserving", ["mindset", "keep as much history as possible"], accent="rose", kind="note", align="center", small=True),
            Box("b6", 1180, 384, 132, 240, "State-preserving", ["mindset", "retain only what must stay live"], accent="teal", kind="note", align="center", small=True),
        ],
        arrows=[
            Arrow("a1", "b1", "b2", color="navy", label="initialize"),
            Arrow("a2", "b2", "b3", color="amber", label="externalize"),
            Arrow("a3", "b3", "b2", color="teal", label="retrieve"),
            Arrow("a4", "b3", "b4", color="teal", label="ground", points=[(1140, 594), (1180, 594), (1180, 760), (1140, 760)]),
            Arrow("a5", "b4", "b2", color="violet", label="feedback", points=[(1140, 760), (1260, 760), (1260, 416), (1140, 416)]),
            Arrow("a6", "b5", "b2", color="rose", label="", points=[(180, 504), (220, 504)]),
            Arrow("a7", "b2", "b6", color="teal", label="", points=[(1140, 416), (1190, 416)]),
        ],
        legends=[Legend([("amber", "live-state retention"), ("teal", "external memory flow"), ("violet", "tool-grounded correction")], 1220, 860)],
        footnotes=[
            "This hierarchy combines systems practice (compaction, memories, AGENTS) with research on memory-operating systems.",
            "The active horizon H* is the operating range that stays live before external recall becomes cheaper than internal retention.",
        ],
    )

    yield Figure(
        name="fig04_state_market",
        title="Figure 4. From reusable state to a possible state-artifact economy",
        subtitle="What could become portable is not an arbitrary prompt, but a compatibility-checked state object with provenance and policy metadata",
        width=1600,
        height=980,
        boxes=[
            Box("g1", 90, 176, 1420, 440, "Artifact lifecycle", accent="navy", kind="group"),
            Box("g2", 90, 650, 1420, 170, "What remains speculative", accent="violet", kind="group"),
            Box("b1", 130, 248, 270, 200, "Mint", ["prefill or initialize a task-specific state", "bind model hash, tokenizer, tools, safety policy"], accent="navy"),
            Box("b2", 470, 220, 320, 256, "State artifact", ["prefix / context fingerprint", "compatible model family", "task schema + persona tag", "active-horizon assumptions", "provenance + version history"], accent="amber"),
            Box("b3", 860, 220, 260, 110, "Verify", ["compatibility, provenance, safety"], accent="teal"),
            Box("b4", 860, 366, 260, 110, "Compose", ["merge with workflow state or org memory"], accent="violet"),
            Box("b5", 1180, 220, 260, 110, "Execute", ["resume agent loop with tools and retrieval"], accent="navy"),
            Box("b6", 1180, 366, 260, 110, "Settle", ["price usage, track value, log outcomes"], accent="amber"),
            Box("b7", 150, 700, 1320, 86, "Important caveat", ["This is an inference from serving constraints and memory-system design, not a current market standard."], accent="rose", align="center", small=True),
        ],
        arrows=[
            Arrow("a1", "b1", "b2", color="navy", label="create"),
            Arrow("a2", "b2", "b3", color="teal", label="check"),
            Arrow("a3", "b2", "b4", color="violet", label="merge"),
            Arrow("a4", "b3", "b5", color="navy", label="load", points=[(1120, 276), (1160, 276)]),
            Arrow("a5", "b4", "b6", color="amber", label="price / account", points=[(1120, 422), (1160, 422)]),
            Arrow("a6", "b5", "b6", color="slate", label="outcome log", points=[(1310, 330), (1310, 366)]),
        ],
        legends=[Legend([("navy", "execution path"), ("teal", "compatibility checks"), ("amber", "pricing / settlement"), ("violet", "composition")], 1110, 860)],
        footnotes=[
            "The artifact metaphor becomes plausible only if memory is explicit, versioned, and cheap to reload relative to re-creating full context.",
        ],
    )

    yield Figure(
        name="fig07_state_serving_loop",
        title="Figure 7. The state-serving loop for long-horizon agents",
        subtitle="A long-running agent is best understood as a closed-loop system that repeatedly compresses, verifies, externalizes, and resumes",
        width=1600,
        height=980,
        boxes=[
            Box("b1", 120, 390, 230, 126, "User / environment", ["new tasks, new evidence, changing world state"], accent="navy"),
            Box("b2", 430, 210, 300, 130, "Live state", ["current plan", "working memory", "open hypotheses"], accent="amber"),
            Box("b3", 430, 590, 300, 130, "Compaction + summarization", ["shrink context while carrying forward task-relevant state"], accent="teal"),
            Box("b4", 860, 210, 300, 130, "External memory", ["notes, artifacts, retrieval index, project docs"], accent="violet"),
            Box("b5", 860, 590, 300, 130, "Tools + verification", ["tests, browser, logs, metrics, APIs"], accent="navy"),
            Box("b6", 1240, 390, 240, 126, "Response / action", ["answers, code changes, decisions, tool side effects"], accent="amber"),
            Box("n1", 520, 418, 500, 92, "Design criterion", ["preserve enough state for the next competent action,", "not every token from the previous window"], accent="rose", kind="note", align="center", small=True),
        ],
        arrows=[
            Arrow("a1", "b1", "b2", color="navy", label="new input"),
            Arrow("a2", "b2", "b4", color="violet", label="memory I/O", points=[(730, 274), (796, 274)]),
            Arrow("a3", "b4", "b5", color="teal", label="retrieve"),
            Arrow("a4", "b5", "b6", color="navy", label="act"),
            Arrow("a5", "b6", "b3", color="amber", label="carry-over", points=[(1480, 454), (1520, 454), (1520, 654), (730, 654)]),
            Arrow("a6", "b3", "b2", color="teal", label="resume", points=[(580, 590), (580, 340)]),
            Arrow("a7", "b5", "b2", color="violet", label="feedback", points=[(860, 654), (812, 654), (812, 274), (730, 274)]),
        ],
        legends=[Legend([("navy", "acting"), ("violet", "memory"), ("teal", "compaction / retrieval"), ("amber", "residue / carry-over")], 1180, 840)],
        footnotes=[
            "This loop is why long-running agent systems increasingly need both memory architecture and serving architecture, not just larger windows.",
        ],
    )

    yield Figure(
        name="fig08_evaluation_map",
        title="Figure 8. Evaluation map for state-centric serving",
        subtitle="Long service requires measuring more than perplexity or window length: memory, tool-use, compaction, and recovery all matter",
        width=1600,
        height=980,
        boxes=[
            Box("g1", 70, 150, 1460, 700, "Benchmarks and missing metrics", accent="slate", kind="group"),
            Box("b1", 120, 212, 290, 120, "LoCoMo", ["300-turn, multi-session benchmark", "temporal + causal memory"], accent="navy"),
            Box("b2", 120, 368, 290, 120, "LongMemEval", ["500 QA over sustained chats", "extraction + reasoning + updates"], accent="teal"),
            Box("b3", 120, 524, 290, 120, "BEAM", ["up to 10M tokens", "memory at ultra-long scale"], accent="amber"),
            Box("b4", 120, 680, 290, 120, "MCP-Atlas / tool benchmarks", ["36 real servers, 220 tools", "realistic tool orchestration"], accent="violet"),
            Box("b5", 500, 212, 420, 588, "What current benchmarks mostly cover", ["1. Recall from long histories", "2. Multi-session temporal reasoning", "3. Knowledge updates and contradictions", "4. Tool-use planning in realistic workflows"], accent="slate"),
            Box("b6", 1010, 212, 440, 588, "What a state-serving benchmark should add", ["1. State carry-over rate after compaction", "2. Retrieval-trigger precision / recall", "3. Memory write amplification and token overhead", "4. Error-recovery half-life after tool failure", "5. Cross-session identity continuity under new evidence", "6. Privacy and policy isolation of portable state"], accent="rose"),
        ],
        arrows=[
            Arrow("a1", "b1", "b5", color="navy", label="memory"),
            Arrow("a2", "b2", "b5", color="teal", label="interactive"),
            Arrow("a3", "b3", "b5", color="amber", label="scale"),
            Arrow("a4", "b4", "b5", color="violet", label="tool use"),
            Arrow("a5", "b5", "b6", color="rose", label="missing metrics", points=[(940, 506), (980, 506), (980, 506), (1010, 506)]),
        ],
        legends=[Legend([("navy", "conversational memory"), ("teal", "interactive memory"), ("amber", "ultra-long history"), ("violet", "tool use"), ("rose", "missing metrics")], 1070, 860)],
        footnotes=[
            "A state-centric system should be judged by what survives the next service window, not only by what fits inside the current one.",
        ],
    )


def build_drawio(figures_list: list[Figure]) -> str:
    mxfile = ET.Element(
        "mxfile",
        {
            "host": "app.diagrams.net",
            "modified": "2026-04-21T00:00:00.000Z",
            "agent": "OpenAI GPT-5.4",
            "version": "24.7.17",
        },
    )
    for fig in figures_list:
        mxfile.append(drawio_for_figure(fig))
    ET.indent(mxfile, space="  ")
    return ET.tostring(mxfile, encoding="unicode")


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    figures_list = list(figures())
    for fig in figures_list:
        svg_path = ASSETS / f"{fig.name}.svg"
        write_text(svg_path, svg_for_figure(fig))
        export_png(svg_path)
    write_text(ROOT / "figures.drawio", build_drawio(figures_list))


if __name__ == "__main__":
    main()
