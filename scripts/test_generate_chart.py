"""Tests for the AAS chart generator (two-band parsing and scatter math)."""

from chart_svg import generate_scatter_svg
from generate_chart import parse_assessment, short_name

FIXTURE = """# AAS Assessment: Testbot

## Metadata

- **System:** Testbot 1.0 (Example System)
- **Evaluation Class:** Documentation-Based (Provisional)
- **AAS Framework Version:** v0.2.0

## Scores

| # | Dimension | Active | Ambient | Designation (Active) |
|---|-----------|:------:|:-------:|----------------------|
| 1 | Cognitive Autonomy | 3 | 2 | Contextual |
| 2 | Temporal Persistence | 2 | 0 | Conditioned |
| 3 | Environmental Agency | 4 | 0 | Self-Directed |
| 4 | Social Agency | 1 | 0 | Responsive |
| 5 | Creative Agency | 2 | 2 | Conditioned |
| 6 | Self-Awareness | 2 | 0 | Conditioned |
| 7 | Goal Formation | 3 | 0 | Contextual |

**Active Composite:** {active_composite} / 5.0
**Ambient Composite:** {ambient_composite} / 5.0
"""


def _write_fixture(tmp_path, active_composite="2.43", ambient_composite="0.57"):
    path = tmp_path / "testbot.md"
    path.write_text(
        FIXTURE.format(active_composite=active_composite, ambient_composite=ambient_composite),
        encoding="utf-8",
    )
    return path


def _system(name, active_composite, ambient_composite):
    return {
        "name": name,
        "short_name": name,
        "active": [0] * 7,
        "ambient": [0] * 7,
        "active_composite": active_composite,
        "ambient_composite": ambient_composite,
        "evaluation_class": "Documentation-Based (Provisional)",
        "file": f"{name}.md",
    }


def test_parse_two_band_table_returns_both_bands(tmp_path):
    """Expected: a well-formed two-band assessment parses fully."""
    result = parse_assessment(_write_fixture(tmp_path))
    assert result is not None
    assert result["active"] == [3, 2, 4, 1, 2, 2, 3]
    assert result["ambient"] == [2, 0, 0, 0, 2, 0, 0]
    assert abs(result["active_composite"] - 17 / 7) < 1e-9
    assert abs(result["ambient_composite"] - 4 / 7) < 1e-9
    assert result["short_name"] == "Testbot 1.0"
    assert result["evaluation_class"] == "Documentation-Based (Provisional)"


def test_parse_recomputes_composite_and_warns_on_mismatch(tmp_path, capsys):
    """Edge: a stated composite that disagrees is overridden with a warning."""
    result = parse_assessment(_write_fixture(tmp_path, active_composite="9.99"))
    assert result is not None
    assert abs(result["active_composite"] - 17 / 7) < 1e-9
    captured = capsys.readouterr()
    assert "WARNING" in captured.out
    assert "testbot.md" in captured.out


def test_parse_returns_none_when_rows_missing(tmp_path):
    """Failure: fewer than 7 score rows rejects the file."""
    content = _write_fixture(tmp_path).read_text(encoding="utf-8")
    lines = [line for line in content.splitlines() if "| 6 |" not in line and "| 7 |" not in line]
    path = _write_fixture(tmp_path)
    path.write_text("\n".join(lines), encoding="utf-8")
    assert parse_assessment(path) is None


def test_short_name_strips_parenthetical():
    """Edge: parenthetical qualifiers are dropped, plain names pass through."""
    assert short_name("Apple Siri (iOS 18/26 Apple Intelligence architecture)") == "Apple Siri"
    assert short_name("Manus 1.6 Max") == "Manus 1.6 Max"


def test_scatter_svg_plots_composites():
    """Expected: points land at the composite-derived coordinates with labels."""
    systems = [_system("Alpha", 3.0, 1.0), _system("Beta", 1.0, 4.0)]
    svg = generate_scatter_svg(systems)

    width = 700
    margin = 90
    plot = width - 2 * margin
    max_score = 5

    def sx(value):
        return margin + plot * value / max_score

    def sy(value):
        return width - margin - plot * value / max_score

    assert f'cx="{sx(3.0):.1f}" cy="{sy(1.0):.1f}"' in svg
    assert f'cx="{sx(1.0):.1f}" cy="{sy(4.0):.1f}"' in svg
    assert ">Alpha</text>" in svg
    assert ">Beta</text>" in svg


def test_scatter_svg_dodges_identical_points():
    """Edge: identical composites must not render overlapping labels."""
    systems = [_system("Alpha", 1.71, 0.5), _system("Beta", 1.71, 0.5)]
    svg = generate_scatter_svg(systems)

    import re

    label_ys = {
        match.group(2): float(match.group(1))
        for match in re.finditer(r'<text x="[\d.]+" y="([\d.]+)" [^>]*>(Alpha|Beta)</text>', svg)
    }
    assert set(label_ys) == {"Alpha", "Beta"}
    assert label_ys["Alpha"] != label_ys["Beta"]
