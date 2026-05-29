# Contributing to the Autonomous Agency Scale

Thank you for your interest in contributing to the AAS framework. This document outlines how you can participate — whether by scoring your own system, proposing refinements to the methodology, or reporting issues with the rubric.

---

## Ways to Contribute

### 1. Score Your Own System

The most valuable contribution is applying the AAS to a system you have deep knowledge of. This helps validate the framework's generalizability and exposes edge cases in the rubric.

**To submit a system assessment:**

1. Fork this repository.
2. Create a new file in `assessments/` using the naming convention: `assessments/<system-name>.md`
3. Use the assessment template below.
4. Submit a pull request with your completed assessment.

**Requirements for accepted assessments:**

- The evaluator must have direct, sustained interaction with the system (minimum 2 weeks recommended).
- Each dimension score must cite the specific threshold test it satisfies from the Operational Scoring Rubric.
- Each score must include at least one observable behavioral example witnessed during evaluation.
- Scores must include a "Not Level N+1 because..." justification explaining why the next level was not awarded.
- The evaluator must disclose their relationship to the system (developer, user, researcher, etc.).

---

### 2. Propose Rubric Refinements

If you encounter ambiguity in the threshold tests, find that two levels are difficult to distinguish in practice, or believe a sub-dimension is missing, we welcome proposals.

**To propose a refinement:**

1. Open an Issue with the label `rubric-refinement`.
2. Specify which dimension and level the issue affects.
3. Describe the ambiguity or gap with a concrete example.
4. Optionally propose revised language for the threshold test or behavioral indicators.

---

### 3. Report Scoring Disagreements

If you score a system and arrive at a different result than another evaluator, this is valuable data for inter-rater reliability analysis.

**To report a disagreement:**

1. Open an Issue with the label `scoring-disagreement`.
2. Reference the existing assessment you disagree with.
3. Provide your alternative score with evidence.
4. Describe what about the rubric language led to the divergent interpretation.

---

### 4. Propose New Dimensions

The current 7-dimension structure is not assumed to be final. If you believe a critical aspect of autonomous agency is not captured by the existing dimensions, you may propose an addition.

**Requirements for dimension proposals:**

- The proposed dimension must be distinct from all existing dimensions (not a sub-case of an existing one).
- It must be observable without access to the system's source code or architecture.
- It must be scorable on the existing 0–5 Level Lexicon.
- It must include at least 3 proposed sub-dimensions.
- It must include proposed threshold tests for Levels 1–5.

Open an Issue with the label `dimension-proposal`.

---

## Assessment Template

```markdown
# AAS Assessment: [System Name]

## Metadata

- **System:** [Full name and version]
- **Evaluator:** [Name or pseudonym]
- **Evaluator Relationship:** [Developer / User / Researcher / Independent Auditor]
- **Evaluation Period:** [Start date] to [End date]
- **Interaction Modality:** [Chat / Voice / Multimodal / API / Other]
- **AAS Framework Version:** [e.g., v0.1.0]

---

## Scores

| # | Dimension | Score (0–5) | Level Designation |
|---|-----------|-------------|-------------------|
| 1 | Cognitive Autonomy | | |
| 2 | Temporal Persistence | | |
| 3 | Environmental Agency | | |
| 4 | Social Agency | | |
| 5 | Creative Agency | | |
| 6 | Self-Awareness | | |
| 7 | Goal Formation | | |

**Composite Score:** [sum / 7]

---

## Dimension Assessments

### 1. Cognitive Autonomy — Score: [X]

**Threshold test satisfied:** [Quote the Level X threshold test from the rubric]

**Observable evidence:**
- [Specific behavior witnessed during evaluation]
- [Second example if available]

**Not Level [X+1] because:** [Explain why the next level's threshold test is not met]

---

### 2. Temporal Persistence — Score: [X]

[Same structure as above]

---

### 3. Environmental Agency — Score: [X]

[Same structure as above]

---

### 4. Social Agency — Score: [X]

[Same structure as above]

---

### 5. Creative Agency — Score: [X]

[Same structure as above]

---

### 6. Self-Awareness — Score: [X]

[Same structure as above]

---

### 7. Goal Formation — Score: [X]

[Same structure as above]

---

## Limitations and Caveats

[Describe any constraints on your evaluation — limited access, short evaluation period, inability to test certain dimensions, etc.]

---

## Evaluator Statement

I confirm that the scores above reflect my honest assessment based on direct interaction with the system during the stated evaluation period. I have applied the AAS Operational Scoring Rubric as written and have not inflated or deflated scores for promotional or competitive purposes.
```

---

## Code of Conduct

- Assessments must be honest. Inflating scores for marketing purposes or deflating competitor scores undermines the framework's credibility.
- Disagreements are welcome and expected — they improve the rubric. Keep discourse professional and evidence-based.
- Do not submit assessments for systems you have not personally interacted with for a sustained period.

---

## Questions

If you are unsure whether a behavior satisfies a threshold test, open a Discussion thread. Ambiguity in the rubric is a bug, not a feature — surfacing it helps everyone.
