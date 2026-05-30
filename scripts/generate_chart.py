#!/usr/bin/env python3
"""
AAS Radar Chart Generator

Parses all assessment Markdown files in the assessments/ directory,
extracts dimension scores, and generates:
  1. A multi-system radar chart (SVG)
  2. A README.md summary with the embedded chart

Usage:
    python scripts/generate_chart.py
"""

import os
import re
import math
from pathlib import Path

# Configuration
ASSESSMENTS_DIR = Path(__file__).parent.parent / "assessments"
OUTPUT_SVG = ASSESSMENTS_DIR / "chart.svg"
OUTPUT_README = ASSESSMENTS_DIR / "README.md"

# Dimension labels (must match assessment table order)
DIMENSIONS = [
    "Cognitive\nAutonomy",
    "Temporal\nPersistence",
    "Environmental\nAgency",
    "Social\nAgency",
    "Creative\nAgency",
    "Self-\nAwareness",
    "Goal\nFormation",
]

DIMENSION_SHORT = [
    "Cognitive Autonomy",
    "Temporal Persistence",
    "Environmental Agency",
    "Social Agency",
    "Creative Agency",
    "Self-Awareness",
    "Goal Formation",
]

# Color palette for systems (add more as needed)
COLORS = [
    {"fill": "rgba(236, 72, 153, 0.15)", "stroke": "#ec4899", "name": "pink"},      # Airi
    {"fill": "rgba(251, 146, 60, 0.15)", "stroke": "#fb923c", "name": "orange"},     # Claude Code
    {"fill": "rgba(96, 165, 250, 0.15)", "stroke": "#60a5fa", "name": "blue"},       # Future
    {"fill": "rgba(74, 222, 128, 0.15)", "stroke": "#4ade80", "name": "green"},      # Future
    {"fill": "rgba(192, 132, 252, 0.15)", "stroke": "#c084fc", "name": "purple"},    # Future
    {"fill": "rgba(251, 191, 36, 0.15)", "stroke": "#fbbf24", "name": "yellow"},     # Future
    {"fill": "rgba(45, 212, 191, 0.15)", "stroke": "#2dd4bf", "name": "teal"},       # Future
    {"fill": "rgba(248, 113, 113, 0.15)", "stroke": "#f87171", "name": "red"},       # Future
]


def parse_assessment(filepath: Path) -> dict | None:
    """Parse an assessment markdown file and extract system name and scores."""
    content = filepath.read_text(encoding="utf-8")

    # Extract system name from metadata
    name_match = re.search(r"\*\*System:\*\*\s*(.+)", content)
    if not name_match:
        return None
    system_name = name_match.group(1).strip()

    # Extract scores from the table
    # Look for rows like: | 1 | Cognitive Autonomy | 4 | Self-Directed |
    score_pattern = re.compile(
        r"\|\s*(\d)\s*\|[^|]+\|\s*(\d)\s*\|[^|]+\|"
    )
    matches = score_pattern.findall(content)

    if len(matches) < 7:
        return None

    # Sort by dimension number and extract scores
    scores = [0] * 7
    for dim_num, score in matches[:7]:
        scores[int(dim_num) - 1] = int(score)

    # Extract composite score
    composite_match = re.search(r"\*\*Composite Score:\*\*\s*([\d.]+)", content)
    composite = float(composite_match.group(1)) if composite_match else sum(scores) / 7

    return {
        "name": system_name,
        "scores": scores,
        "composite": composite,
        "file": filepath.name,
    }


def generate_radar_svg(systems: list[dict]) -> str:
    """Generate a radar chart SVG with multiple systems overlaid."""
    # SVG dimensions
    width = 700
    height = 700
    cx = width / 2
    cy = height / 2
    radius = 250
    max_score = 5
    num_dims = 7

    # Calculate angles (start from top, go clockwise)
    angles = []
    for i in range(num_dims):
        angle = (2 * math.pi * i / num_dims) - (math.pi / 2)
        angles.append(angle)

    def point_at(angle: float, distance: float) -> tuple[float, float]:
        x = cx + distance * math.cos(angle)
        y = cy + distance * math.sin(angle)
        return (x, y)

    svg_parts = []

    # SVG header
    svg_parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}">'
    )

    # Background
    svg_parts.append(f'<rect width="{width}" height="{height}" fill="#0a0a0f"/>')

    # Grid rings (levels 1-5)
    for level in range(1, max_score + 1):
        r = radius * level / max_score
        points = []
        for angle in angles:
            px, py = point_at(angle, r)
            points.append(f"{px:.1f},{py:.1f}")
        polygon_points = " ".join(points)
        opacity = 0.15 if level < max_score else 0.25
        svg_parts.append(
            f'<polygon points="{polygon_points}" fill="none" '
            f'stroke="#374151" stroke-width="1" opacity="{opacity}"/>'
        )

    # Axis lines
    for angle in angles:
        px, py = point_at(angle, radius)
        svg_parts.append(
            f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{px:.1f}" y2="{py:.1f}" '
            f'stroke="#374151" stroke-width="1" opacity="0.3"/>'
        )

    # Level numbers on first axis
    for level in range(1, max_score + 1):
        r = radius * level / max_score
        px, py = point_at(angles[0], r)
        svg_parts.append(
            f'<text x="{px + 8:.1f}" y="{py - 5:.1f}" '
            f'font-family="monospace" font-size="11" fill="#6b7280" '
            f'text-anchor="start">{level}</text>'
        )

    # Dimension labels
    label_offset = 35
    for i, angle in enumerate(angles):
        px, py = point_at(angle, radius + label_offset)
        lines = DIMENSIONS[i].split("\n")
        anchor = "middle"
        if abs(math.cos(angle)) > 0.3:
            anchor = "start" if math.cos(angle) > 0 else "end"

        for j, line in enumerate(lines):
            ly = py + (j * 14) - ((len(lines) - 1) * 7)
            svg_parts.append(
                f'<text x="{px:.1f}" y="{ly:.1f}" '
                f'font-family="system-ui, -apple-system, sans-serif" font-size="12" '
                f'fill="#d1d5db" text-anchor="{anchor}" '
                f'dominant-baseline="middle">{line}</text>'
            )

    # Plot each system
    for idx, system in enumerate(systems):
        color = COLORS[idx % len(COLORS)]
        points = []
        for i, score in enumerate(system["scores"]):
            r = radius * score / max_score
            px, py = point_at(angles[i], r)
            points.append(f"{px:.1f},{py:.1f}")

        polygon_points = " ".join(points)

        # Filled polygon
        svg_parts.append(
            f'<polygon points="{polygon_points}" '
            f'fill="{color["fill"]}" stroke="{color["stroke"]}" '
            f'stroke-width="2.5"/>'
        )

        # Data points
        for i, score in enumerate(system["scores"]):
            r = radius * score / max_score
            px, py = point_at(angles[i], r)
            svg_parts.append(
                f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" '
                f'fill="{color["stroke"]}" stroke="#0a0a0f" stroke-width="1.5"/>'
            )

    # Legend
    legend_x = 20
    legend_y = height - 30 - (len(systems) * 25)
    svg_parts.append(
        f'<rect x="{legend_x - 10}" y="{legend_y - 15}" '
        f'width="220" height="{len(systems) * 25 + 20}" '
        f'rx="6" fill="#111118" stroke="#374151" stroke-width="1"/>'
    )
    for idx, system in enumerate(systems):
        color = COLORS[idx % len(COLORS)]
        ly = legend_y + (idx * 25) + 5
        svg_parts.append(
            f'<rect x="{legend_x}" y="{ly - 5}" width="14" height="14" '
            f'rx="2" fill="{color["stroke"]}"/>'
        )
        svg_parts.append(
            f'<text x="{legend_x + 22}" y="{ly + 5}" '
            f'font-family="system-ui, -apple-system, sans-serif" font-size="13" '
            f'fill="#e5e7eb" dominant-baseline="middle">'
            f'{system["name"]} ({system["composite"]:.2f})</text>'
        )

    # Title
    svg_parts.append(
        f'<text x="{cx:.1f}" y="30" '
        f'font-family="system-ui, -apple-system, sans-serif" font-size="18" '
        f'font-weight="bold" fill="#f9fafb" text-anchor="middle">'
        f'Autonomous Agency Scale — Comparative Assessment</text>'
    )

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def generate_readme(systems: list[dict]) -> str:
    """Generate the assessments/README.md with embedded chart and summary table."""
    lines = []
    lines.append("# AAS Comparative Assessments")
    lines.append("")
    lines.append("This chart is auto-generated from all assessment files in this directory.")
    lines.append("")
    lines.append("![AAS Radar Chart](chart.svg)")
    lines.append("")
    lines.append("## Summary")
    lines.append("")

    # Header
    header = "| System | " + " | ".join(DIMENSION_SHORT) + " | Composite |"
    separator = "|--------|" + "|".join(["-------"] * 7) + "|-----------|"
    lines.append(header)
    lines.append(separator)

    # Sort by composite descending
    sorted_systems = sorted(systems, key=lambda s: s["composite"], reverse=True)

    for system in sorted_systems:
        scores_str = " | ".join(str(s) for s in system["scores"])
        lines.append(
            f"| [{system['name']}]({system['file']}) | "
            f"{scores_str} | **{system['composite']:.2f}** |"
        )

    lines.append("")
    lines.append("## Level Reference")
    lines.append("")
    lines.append("| Score | Level | Meaning |")
    lines.append("|-------|-------|---------|")
    lines.append("| 0 | Dormant | No capability present |")
    lines.append("| 1 | Responsive | Reacts to explicit triggers only |")
    lines.append("| 2 | Conditioned | Follows pre-set rules/schedules |")
    lines.append("| 3 | Contextual | Adapts based on environment/state |")
    lines.append("| 4 | Self-Directed | Initiates from internal state |")
    lines.append("| 5 | Sovereign | Fully autonomous in this dimension |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Auto-generated by `scripts/generate_chart.py`. Do not edit manually.*")
    lines.append("")

    return "\n".join(lines)


def main():
    """Main entry point."""
    # Find all assessment files (exclude README.md)
    assessment_files = sorted(
        f for f in ASSESSMENTS_DIR.glob("*.md")
        if f.name.lower() != "readme.md"
    )

    if not assessment_files:
        print("No assessment files found.")
        return

    # Parse all assessments
    systems = []
    for filepath in assessment_files:
        result = parse_assessment(filepath)
        if result:
            systems.append(result)
            print(f"  Parsed: {result['name']} ({result['composite']:.2f})")
        else:
            print(f"  Skipped: {filepath.name} (could not parse)")

    if not systems:
        print("No valid assessments found.")
        return

    # Generate SVG
    svg_content = generate_radar_svg(systems)
    OUTPUT_SVG.write_text(svg_content, encoding="utf-8")
    print(f"\n  Generated: {OUTPUT_SVG}")

    # Generate README
    readme_content = generate_readme(systems)
    OUTPUT_README.write_text(readme_content, encoding="utf-8")
    print(f"  Generated: {OUTPUT_README}")

    print(f"\n  Total systems: {len(systems)}")


if __name__ == "__main__":
    main()
