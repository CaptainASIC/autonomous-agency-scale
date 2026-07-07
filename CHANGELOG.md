# Changelog

All notable changes to the Autonomous Agency Scale (AAS) framework are documented in this
file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-07-07

### Added

- **Temporal scope of agency**: every dimension is now scored in two bands, Active
  (engaged) and Ambient (across idle periods), with two separate composites
  (README §3.1, §3.4).
- **Idle-Gap Test**: a falsifiable gate for Level 4 in the Ambient band, including the
  substrate-vs-rule distinction for loop-driven architectures (README §3.4).
- **Active-vs-Ambient scatter chart** (`assessments/scatter.svg`), generated alongside the
  existing radar.
- **Evaluation Class** metadata field (`Longitudinal` / `Documentation-Based (Provisional)`)
  disclosing evidence depth per assessment.
- This changelog.

### Changed

- All 6 assessments re-scored in both bands against the revised rubric. Threshold-test
  quotes now match the rubric verbatim.
- `scripts/generate_chart.py` now parses two-band score tables, recomputes both composites
  (warning on mismatch with stated values), and delegates SVG construction to the new
  `scripts/chart_svg.py`.
- README §5 Limitations: the L2-vs-L4 boundary is now partially operationalized (Ambient
  band only). Active-band Level 4 remains judgment-informed.

### Compatibility

- v0.2.0 two-band scores are intentionally not comparable with v0.1.0 single-band scores.

## [0.1.0] - 2026-05-29

### Added

- Initial framework: 7 dimensions of autonomous agency, the 0–5 Level Lexicon, the
  Operational Scoring Rubric, the Longitudinal Turing Test, 6 system assessments, and the
  radar chart generator.
