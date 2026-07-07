"""SVG chart builders for the AAS assessment suite (radar + scatter)."""

import math

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
    {"fill": "rgba(236, 72, 153, 0.15)", "stroke": "#ec4899", "name": "pink"},  # Airi
    {"fill": "rgba(251, 146, 60, 0.15)", "stroke": "#fb923c", "name": "orange"},  # Claude Code
    {"fill": "rgba(96, 165, 250, 0.15)", "stroke": "#60a5fa", "name": "blue"},  # Future
    {"fill": "rgba(74, 222, 128, 0.15)", "stroke": "#4ade80", "name": "green"},  # Future
    {"fill": "rgba(192, 132, 252, 0.15)", "stroke": "#c084fc", "name": "purple"},  # Future
    {"fill": "rgba(251, 191, 36, 0.15)", "stroke": "#fbbf24", "name": "yellow"},  # Future
    {"fill": "rgba(45, 212, 191, 0.15)", "stroke": "#2dd4bf", "name": "teal"},  # Future
    {"fill": "rgba(248, 113, 113, 0.15)", "stroke": "#f87171", "name": "red"},  # Future
]


def generate_radar_svg(systems: list[dict]) -> str:
    """Generate a radar chart SVG with multiple systems overlaid (Active band)."""
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
        for i, score in enumerate(system["active"]):
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
        for i, score in enumerate(system["active"]):
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
            f"{system['name']} ({system['active_composite']:.2f})</text>"
        )

    # Title
    svg_parts.append(
        f'<text x="{cx:.1f}" y="30" '
        f'font-family="system-ui, -apple-system, sans-serif" font-size="18" '
        f'font-weight="bold" fill="#f9fafb" text-anchor="middle">'
        f"Autonomous Agency Scale — Active Band</text>"
    )

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def generate_scatter_svg(systems: list[dict]) -> str:
    """Generate the Active-vs-Ambient composite quadrant scatter (SVG).

    Args:
        systems: Parsed assessment dicts (see generate_chart.parse_assessment).

    Returns:
        Complete SVG document as a string.
    """
    width = 700
    height = 700
    margin = 90
    plot = width - 2 * margin
    max_score = 5

    def sx(value: float) -> float:
        return margin + plot * value / max_score

    def sy(value: float) -> float:
        return height - margin - plot * value / max_score

    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}">'
    )
    parts.append(f'<rect width="{width}" height="{height}" fill="#0a0a0f"/>')

    # Gridlines and tick labels, 0-5 on both axes
    for level in range(0, max_score + 1):
        gx, gy = sx(level), sy(level)
        parts.append(
            f'<line x1="{gx:.1f}" y1="{sy(0):.1f}" x2="{gx:.1f}" y2="{sy(max_score):.1f}" '
            f'stroke="#374151" stroke-width="1" opacity="0.2"/>'
        )
        parts.append(
            f'<line x1="{sx(0):.1f}" y1="{gy:.1f}" x2="{sx(max_score):.1f}" y2="{gy:.1f}" '
            f'stroke="#374151" stroke-width="1" opacity="0.2"/>'
        )
        parts.append(
            f'<text x="{gx:.1f}" y="{sy(0) + 24:.1f}" font-family="monospace" '
            f'font-size="11" fill="#6b7280" text-anchor="middle">{level}</text>'
        )
        parts.append(
            f'<text x="{sx(0) - 12:.1f}" y="{gy + 4:.1f}" font-family="monospace" '
            f'font-size="11" fill="#6b7280" text-anchor="end">{level}</text>'
        )

    # Quadrant midlines at 2.0. Reason: the current composites straddle 2.0 on the
    # Active axis (task agents above it, reactive assistants below); a naive
    # max_score / 2 = 2.5 midline would plot every system except Airi in the left half.
    mid = 2.0
    parts.append(
        f'<line x1="{sx(mid):.1f}" y1="{sy(0):.1f}" x2="{sx(mid):.1f}" '
        f'y2="{sy(max_score):.1f}" stroke="#6b7280" stroke-width="1" '
        f'stroke-dasharray="6 4" opacity="0.5"/>'
    )
    parts.append(
        f'<line x1="{sx(0):.1f}" y1="{sy(mid):.1f}" x2="{sx(max_score):.1f}" '
        f'y2="{sy(mid):.1f}" stroke="#6b7280" stroke-width="1" '
        f'stroke-dasharray="6 4" opacity="0.5"/>'
    )

    # Quadrant captions, centered per quadrant. "Scheduled / Background" (top-left)
    # is expected to be empty with the current roster; the caption stays regardless.
    lo = mid / 2
    hi = mid + (max_score - mid) / 2
    captions = [
        (lo, lo, "Reactive"),
        (hi, lo, "Task Agents"),
        (lo, hi, "Scheduled / Background"),
        (hi, hi, "Ambient Agents"),
    ]
    for qx, qy, label in captions:
        parts.append(
            f'<text x="{sx(qx):.1f}" y="{sy(qy):.1f}" '
            f'font-family="system-ui, -apple-system, sans-serif" font-size="13" '
            f'fill="#4b5563" text-anchor="middle" font-style="italic">{label}</text>'
        )

    # Axis titles
    parts.append(
        f'<text x="{width / 2:.1f}" y="{height - 28:.1f}" '
        f'font-family="system-ui, -apple-system, sans-serif" font-size="14" '
        f'fill="#d1d5db" text-anchor="middle">Active Composite (engaged) →</text>'
    )
    parts.append(
        f'<text x="28" y="{height / 2:.1f}" '
        f'font-family="system-ui, -apple-system, sans-serif" font-size="14" '
        f'fill="#d1d5db" text-anchor="middle" '
        f'transform="rotate(-90 28 {height / 2:.1f})">Ambient Composite (idle period) →</text>'
    )

    # Data points with label dodging
    placed: list[tuple[float, float]] = []
    for idx, system in enumerate(systems):
        color = COLORS[idx % len(COLORS)]
        px = sx(system["active_composite"])
        py = sy(system["ambient_composite"])
        parts.append(
            f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7" fill="{color["stroke"]}" '
            f'stroke="#0a0a0f" stroke-width="1.5"/>'
        )
        lx, ly = px + 12, py + 4
        # Reason: systems can share or nearly share composites, stacking their points;
        # dodge labels that would overlap an already-placed one.
        while any(abs(lx - ox) < 140 and abs(ly - oy) < 16 for ox, oy in placed):
            ly += 18
        placed.append((lx, ly))
        parts.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" '
            f'font-family="system-ui, -apple-system, sans-serif" font-size="13" '
            f'fill="#e5e7eb">{system["short_name"]}</text>'
        )

    # Title
    parts.append(
        f'<text x="{width / 2:.1f}" y="34" '
        f'font-family="system-ui, -apple-system, sans-serif" font-size="18" '
        f'font-weight="bold" fill="#f9fafb" text-anchor="middle">'
        f"Autonomous Agency Scale — Active vs Ambient</text>"
    )

    parts.append("</svg>")
    return "\n".join(parts)
