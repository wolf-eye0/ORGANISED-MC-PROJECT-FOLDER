# Final Comparison Protocol

## Scope and decision boundary

This protocol applies only to OpenBraille, VibeGuard, and TrueMoist. This extraction pass records evidence without selecting, scoring, ranking, recommending, eliminating, or declaring a winner. Patent-development potential is the primary priority, while buildability, budget, validation, timeline, team fit, and demonstration quality remain mandatory constraints. Patent scoring must wait for the separate current patent-source verification pass.

## Hard gates

Evaluate every concept against:

- **G1 — Budget:** maximum prototype budget of ₹5,000.
- **G2 — Timeline:** credible completion within approximately two months.
- **G3 — Team:** executable by the five-member team.
- **G4 — Demonstrable success:** clear and measurable minimum demonstrable success.
- **G5 — Access:** required components, fabrication, facilities, and validation resources are realistically accessible.
- **G6 — Patent-development path:** a credible path exists that could be supported by prototype experiments.
- **G7 — Fatal dependency:** no unresolved dependency creates a fatal implementation or validation risk.

Allowed statuses only: **Pass**, **Provisional Pass**, **Fail**, or **Insufficient Evidence**.

A gate record must include status, evidence, confidence, unresolved dependency, earliest resolving action, time, cost, and consequence of failure. During evidence extraction, a gate result must not eliminate a concept.

## Weighted rubric (100 points)

| Category / criterion | Weight |
|---|---:|
| **A. Patent-development potential** | **35** |
| A1. Specific claimable technical contribution | 15 |
| A2. Plausible white-space position | 8 |
| A3. Ability to generate experimental patent-supporting evidence | 7 |
| A4. Prior-art/FTO risk | 5 |
| **B. Two-month buildability** | **20** |
| B1. Architecture and integration complexity | 8 |
| B2. Schedule realism | 6 |
| B3. Critical implementation risk | 6 |
| **C. Validation strength** | **15** |
| C1. Availability of credible ground truth | 6 |
| C2. Repeatability and experimental control | 5 |
| C3. Clarity of success metrics | 4 |
| **D. Team fit** | **10** |
| **E. Demonstration quality** | **8** |
| **F. Budget and procurement certainty** | **7** |
| **G. Commercial or social significance** | **5** |
| **Total** | **100** |

## Scoring rules for the later decision pass

Use only:

- 1 = very weak
- 2 = weak
- 3 = credible but uncertain
- 4 = strong
- 5 = exceptional

For A4 — Prior-art/FTO risk:

- 5 means comparatively low or manageable blocking risk.
- 1 means severe, uncertain, or likely blocking risk.
- The patent report must separately record novelty/obviousness risk, patent-eligibility risk, and FTO/infringement risk before assigning the combined A4 score.

Weighted contribution:

```text
(score / 5) × criterion weight
```

Every future score must state:

- score;
- confidence level;
- supporting evidence;
- uncertainty;
- earliest resolving experiment or research action;
- patent-research verification status where patent-related.

Complexity is not inherently valuable. Social value is not patent novelty. Demonstration polish is not proof of novelty. A component list is not proof of system feasibility. Patent potential is not established patentability.

## Required later outputs

After current patent verification and scoring, produce:

- patent-first ranking;
- buildability ranking;
- validation ranking;
- demonstration ranking;
- balanced overall ranking.

The future final report must select exactly:

- one primary project;
- one runner-up;
- one reserve.

No score or ranking is populated in this package.
