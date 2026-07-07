#!/usr/bin/env python3
"""
AAS Chart Generator

Parses all assessment Markdown files in the assessments/ directory,
extracts two-band (Active/Ambient) dimension scores, and generates:
  1. A multi-system radar chart of Active scores (SVG)
  2. An Active-vs-Ambient composite scatter chart (SVG)
  3. A README.md summary with both charts embedded

Usage:
    python scripts/generate_chart.py
"""

import re
from pathlib import Path

from chart_svg import DIMENSION_SHORT, generate_radar_svg, generate_scatter_svg

# Configuration
ASSESSMENTS_DIR = Path(__file__).parent.parent / "assessments"
OUTPUT_SVG = ASSESSMENTS_DIR / "chart.svg"
OUTPUT_SCATTER = ASSESSMENTS_DIR / "scatter.svg"
OUTPUT_README = ASSESSMENTS_DIR / "README.md"

# Matches a two-band score row: | 1 | Cognitive Autonomy | 4 | 4 | Self-Directed |
SCORE_ROW = re.compile(r"\|\s*(\d)\s*\|[^|]+\|\s*(\d)\s*\|\s*(\d)\s*\|[^|]+\|")


def short_name(full_name: str) -> str:
    """Return the display name truncated before the first parenthetical qualifier."""
    return full_name.split(" (")[0].strip()


def _warn_on_composite_mismatch(content: str, filename: str, band: str, computed: float) -> None:
    """Warn when a stated composite disagrees with the recomputed value."""
    stated = re.search(rf"\*\*{band} Composite:\*\*\s*([\d.]+)", content)
    if stated and abs(float(stated.group(1)) - computed) > 0.005:
        print(
            f"  WARNING: {filename} states {band} Composite {stated.group(1)} "
            f"but scores compute to {computed:.2f} — using computed value"
        )


def parse_assessment(filepath: Path) -> dict | None:
    """Parse an assessment file into name, two-band scores, and composites."""
    content = filepath.read_text(encoding="utf-8")

    name_match = re.search(r"\*\*System:\*\*\s*(.+)", content)
    if not name_match:
        return None
    system_name = name_match.group(1).strip()

    matches = SCORE_ROW.findall(content)
    if len(matches) < 7:
        return None

    active = [0] * 7
    ambient = [0] * 7
    for dim_num, active_score, ambient_score in matches[:7]:
        active[int(dim_num) - 1] = int(active_score)
        ambient[int(dim_num) - 1] = int(ambient_score)

    active_composite = sum(active) / 7
    ambient_composite = sum(ambient) / 7
    _warn_on_composite_mismatch(content, filepath.name, "Active", active_composite)
    _warn_on_composite_mismatch(content, filepath.name, "Ambient", ambient_composite)

    class_match = re.search(r"\*\*Evaluation Class:\*\*\s*(.+)", content)
    if not class_match:
        print(f"  WARNING: {filepath.name} declares no Evaluation Class")
    evaluation_class = class_match.group(1).strip() if class_match else "Unspecified"

    return {
        "name": system_name,
        "short_name": short_name(system_name),
        "active": active,
        "ambient": ambient,
        "active_composite": active_composite,
        "ambient_composite": ambient_composite,
        "evaluation_class": evaluation_class,
        "file": filepath.name,
    }


def generate_readme(systems: list[dict]) -> str:
    """Generate the assessments/README.md with embedded charts and summary table."""
    lines = []
    lines.append("# AAS Comparative Assessments")
    lines.append("")
    lines.append("These charts are auto-generated from all assessment files in this directory.")
    lines.append("")
    lines.append("![AAS Radar Chart — Active band](chart.svg)")
    lines.append("")
    lines.append("![Active vs Ambient scatter](scatter.svg)")
    lines.append("")
    lines.append("## Summary")
    lines.append("")

    # Header
    header = "| System | Evidence | " + " | ".join(DIMENSION_SHORT) + " | Active | Ambient |"
    separator = "|--------|----------|" + "|".join(["-------"] * 7) + "|--------|---------|"
    lines.append(header)
    lines.append(separator)

    # Sort by Active composite descending
    sorted_systems = sorted(systems, key=lambda s: s["active_composite"], reverse=True)

    for system in sorted_systems:
        evidence = (
            "Longitudinal"
            if system["evaluation_class"].startswith("Longitudinal")
            else "Docs (provisional)"
        )
        cells = " | ".join(f"{a} / {b}" for a, b in zip(system["active"], system["ambient"]))
        lines.append(
            f"| [{system['name']}]({system['file']}) | {evidence} | {cells} | "
            f"**{system['active_composite']:.2f}** | **{system['ambient_composite']:.2f}** |"
        )

    lines.append("")
    lines.append(
        "Each dimension cell is **Active / Ambient**, the engaged vs idle-period band "
        "scores (README §3.4)."
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
        f for f in ASSESSMENTS_DIR.glob("*.md") if f.name.lower() != "readme.md"
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
            print(
                f"  Parsed: {result['name']} (A {result['active_composite']:.2f} / "
                f"a {result['ambient_composite']:.2f})"
            )
        else:
            print(f"  Skipped: {filepath.name} (could not parse)")

    if not systems:
        print("No valid assessments found.")
        return

    # Generate radar SVG (Active band)
    svg_content = generate_radar_svg(systems)
    OUTPUT_SVG.write_text(svg_content, encoding="utf-8")
    print(f"\n  Generated: {OUTPUT_SVG}")

    # Generate Active-vs-Ambient scatter SVG
    scatter_content = generate_scatter_svg(systems)
    OUTPUT_SCATTER.write_text(scatter_content, encoding="utf-8")
    print(f"  Generated: {OUTPUT_SCATTER}")

    # Generate README
    readme_content = generate_readme(systems)
    OUTPUT_README.write_text(readme_content, encoding="utf-8")
    print(f"  Generated: {OUTPUT_README}")

    print(f"\n  Total systems: {len(systems)}")


if __name__ == "__main__":
    main()
