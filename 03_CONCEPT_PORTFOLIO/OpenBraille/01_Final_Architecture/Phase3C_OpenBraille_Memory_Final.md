# MC_Project_Phase3C_OpenBraille_MEMORY.md

# Project mC
## Phase 3C Memory — OpenBraille
### System Architecture & Prototype Planning

Version: 1.0
Status: ✅ COMPLETE
Methodology Version: Phase 3C

---

# Purpose

This document records the engineering knowledge, decisions, and outcomes of Phase 3C for OpenBraille. It is not a replacement for the full `Phase3C_OpenBraille_Architecture_Report.md` — it is a concise memory allowing future AI assistants and project members to rapidly reconstruct Phase 3C context without reprocessing the four independent Deep Research reports. The authoritative technical findings remain in the official report.

---

# 1. Engineering Identity

- **Mission:** Make refreshable Braille technology significantly more affordable and accessible.
- **Engineering Hypothesis:** A lower-cost actuation strategy can replace conventional piezoelectric actuation while maintaining acceptable tactile performance for a refreshable Braille interface.
- **Minimum Demonstrable Success:** Reliably produce refreshable tactile Braille output for at least one Braille cell, meeting basic tactile and repeatability requirements — within ₹3,000–5,000 and ~2 months, by three CS/Cybersecurity students with no mechanical engineer on the team.
- **Fixed Design Principles (unchanged from EDR):** affordability first; maintain refreshable functionality; demonstrate a real prototype; preserve compatibility with standard Braille principles *where appropriate*; avoid piezoelectric dependence if a viable alternative exists.

---

# 2. Final Architecture Summary

**Selected architecture:** Single-cell (6-dot), macro-scaled (~300% of ISO 17049: ≈7 mm pitch, ≈1.5 mm dot height) servo-and-cam-driven refreshable Braille cell, controlled by a centralized ESP32 with direct PWM drive to six SG90-class micro servos. No intermediate driver electronics — SG90's integral driver is used directly. 3D-printed ABS/PETG frame and cams, off-the-shelf stainless-steel pins, servo-integral torsion-spring reset (no external return spring). External 5 V/2 A power supply with decoupling capacitor.

**Implementation philosophy:** Validate the actuation-cost hypothesis with the lowest-risk, highest-team-fit path available, deliberately and permanently accepting non-ISO-compliant dimensions in exchange for retiring the fabrication-tolerance kill factor entirely within this phase's scope, rather than deferring or partially mitigating it.

**Estimated BOM:** ₹2,060–2,850 (well within the ₹3,000 preferred budget), independently order-of-magnitude cross-validated by a second, differently-actuated proposal (₹1,500–2,500).

---

# 3. Final Engineering Decisions

| Decision | Selection | Basis |
|---|---|---|
| Actuation principle | Servo + cam, macro-scaled | Only candidate retiring the fabrication-tolerance kill factor permanently, with no custom driver electronics and no continuous-hold thermal risk |
| Controller/MCU | ESP32-WROOM-32 DevKit | Unanimous across all four Phase 3C reports; team familiarity, ample I/O and timer resources |
| Driver electronics | None — direct PWM | SG90 servos self-drive; adding H-bridges/shift-registers/Darlington arrays (required by the rejected alternatives) would add complexity with no benefit at this scale |
| Mechanical scale | ~300% of ISO 17049 (permanent, not a staging step toward compliance) | Unanimous mitigation strategy across all four reports for Phase 3B's #1 kill factor |
| Manufacturing pathway | In-house FDM 3D printing (ABS frame, PETG/Nylon cams) + off-the-shelf parts | No outsourcing dependency; fully within team-accessible tools and 2-month timeline |
| Validation strategy | Single-dot-first, milestone-based bring-up (M1–M8), culminating in structured tactile user testing | Isolates mechanical, electrical, and firmware variables before integration; matches the EDR's literal MDS text |
| Power architecture | External 5 V/2 A adapter + 1,000 µF decoupling, not USB-bus power | Avoids brown-out risk under multi-servo actuation |

---

# 4. Rejected Alternatives

- **Electromagnetic latching micro-coils, two-stage (300% FDM → 100% SLA-outsourced)** — proposed by one of four Phase 3C reports (Gemini), with genuinely strong real-world precedent (named open-hardware projects MOLBED and MagnePins) and a true zero-power bistable latch advantage. **Not selected** because its second stage re-introduces the exact fabrication-tolerance risk this architecture exists to retire (the report's own risk table rates the SLA stage "High" severity), exceeds the EDR's actual MDS (which does not require ISO compliance), adds an outsourced-service dependency and an unquantified cost, and demands the highest analog/EE skill level (custom coil winding, H-bridge design, SPI-multiplexed shift registers, crosstalk-avoidance firmware) of any candidate — directly against the team's stated composition. **Explicitly preserved as the recommended starting point for a future phase** that pursues true ISO 17049 compliance under different team-capability or mentorship conditions.
- **Non-latching push-pull solenoid, macro-scaled, direct-drive** — proposed by one of four Phase 3C reports (Qwen). Simpler electrically than EM latching (single ULN2003 driver IC), but carries an unresolved engineering gap: holding a pin raised requires continuous coil energization against spring return, which is a real thermal/reliability risk the proposing report itself does not mechanically resolve ("momentary activation strategy" is asserted but not specified for a design with no latch). **Not selected** on this basis. Could be revisited if a genuine latching mechanism (magnetic or mechanical detent) were added.
- **Shape Memory Alloy, voice coil, EAP, pneumatic/microfluidic** — considered and rejected by multiple reports across Phase 3A/3B/3C consistently, on grounds of slow response, thermal/fatigue limitations, fabrication complexity, or immaturity; not seriously re-litigated in Phase 3C given the consistent prior rejection.

---

# 5. Architecture Constraints for Future Phases

The following shall not change without new evidence:

- The prototype targets **one 6-dot Braille cell**, not a multi-cell line, per the EDR's MDS.
- The mechanical scale is **permanently macro** (~300%) for this prototype phase; ISO 17049 compliance is an explicitly deferred, not abandoned, future goal.
- **No driver ICs** (H-bridge, shift register, Darlington array) are part of this architecture; if a future phase changes the actuation principle, this constraint should be revisited alongside that change, not independently.
- The **budget baseline is ₹2,060–2,850**; any future BOM revision should be measured against this baseline, not against the ₹5,000 ceiling in isolation.
- The team-capability allocation (three technical members on firmware/electrical, two on fabrication/CAD/sourcing, one beginner on a scoped software module) is a **Phase 3C recommendation**, not an EDR-fixed constraint, and may be revised by the project team as actual capacity becomes clear.

---

# 6. Remaining Risks and Open Assumptions

- **Open, unvalidated by any report:** whether a 1.5 mm pin height is comfortably tactilely distinguishable by touch. This is the single most important unresolved empirical question carried into Phase 4 — it bears directly on the EDR's "acceptable tactile performance" language and should be an early (Week 1–3) validation priority, not deferred to final testing.
- **Open, low-severity:** SG90 torque sufficiency at the chosen cam mechanical advantage (fallback: MG996R); cam/follower wear over extended cycling (mitigated by PETG/Nylon material choice, to be confirmed during the 1,000-cycle reliability test).
- **Resolved by this architecture, not merely mitigated:** fabrication-tolerance failure at true dot pitch, actuator force/speed shortfall, and the team's mechanical-CAD skill gap compounding fabrication risk — all three were Phase 3B's High-severity findings for OpenBraille, and all three are structurally addressed (not just budgeted-around) by the macro-scaling and driver-free-actuator decisions.

---

# 7. Future Phase Guidance

**What Phase 4 (Prototype Engineering) must preserve:**
- The selected actuation principle (servo + cam, macro-scaled) and the reasoning against the two rejected alternatives — do not re-litigate this choice without new evidence (e.g., an actual failed cam-fabrication attempt, or a change in team composition/mentorship availability).
- The permanent (not staged) macro-scaling decision, unless and until the project explicitly decides to pursue ISO 17049 compliance as a distinct, later goal.
- The single-dot-first bring-up sequence, which is both a risk-mitigation strategy and a natural task-division scaffold for the five-member team.

**What requires empirical validation, not further research:** tactile-height adequacy (Section 6 above) and cam/servo durability under the specific macro-scale geometry — both are hands-on prototyping questions, not open research questions, and should not trigger another Deep Research commissioning round.

**Recommended engineering priority for Phase 4:** front-load the tactile-validation question (build and touch-test a single dot as early as possible, even before all six are integrated) rather than treating it as a final-week check, since it is the one open assumption that could, in principle, require a design revision (pin height, spacing, or profile) if it fails — and revisions are cheapest to make before all six modules are built.

**If ISO 17049 compliance becomes a future goal** (e.g., after gaining mechanical-engineering mentorship, per Phase 3B's still-open question): begin from Gemini's Phase 3C electromagnetic-latching research, not from a compliance-driven revision of the servo+cam design — the two architectures solve the tolerance problem in fundamentally different ways, and the EM-latching approach's real-world precedents (MOLBED, MagnePins) are the more directly applicable evidence base for that specific goal.

---

# Methodological Lessons for the Project Record

- **A report can reverse its own prior-phase position without acknowledging it.** Gemini's Phase 3C recommendation (EM latching) directly contradicts Gemini's own Phase 3B recommendation (macro-scaled servo+cam) with no explicit acknowledgment of the change or reasoning for it. This is a new failure mode, distinct from concept-fidelity drift or incompleteness, and worth watching for in future phases: a report's *internal* consistency across phases is a signal worth auditing, not just its fidelity to the grounding documents in the current phase.
- **Strong evidentiary citation (real, named, working precedents) does not automatically mean the recommended path is correct for this team.** Gemini's MOLBED/MagnePins citations are genuinely the strongest piece of evidence produced across all four Phase 3C reports, yet the architecture they support was still correctly rejected on team-fit and scope grounds. Evidence quality and architectural fitness are separate axes; a synthesis should weigh both, not conflate them.
- **An incomplete submission is a distinct failure mode from a concept-fidelity failure**, and should be flagged and weighted accordingly rather than silently treated as equivalent to a complete-but-lower-confidence report. Qwen's Phase 3C submission was correct wherever it went, but stopped less than halfway through the required Part 3 content — this is recorded explicitly rather than absorbed into a generic confidence discount.
- **Where Phase 3C differs structurally from Phase 3A/3B:** those phases' mandate was to preserve genuine, well-evidenced disagreement for a later phase to resolve. Phase 3C's mandate is the opposite — it must select one architecture, because its output is the actual build blueprint. The same "evidence over vote-counting" discipline applies, but the required output shape is different, and future synthesis work in this pipeline should expect that shift at the architecture-selection phase specifically.

---

# Phase Status

**Phase 3C (OpenBraille): ✅ COMPLETE**

**Authoritative Output:** `Phase3C_OpenBraille_Architecture_Report.md`

**Next Phase:** ➡️ Phase 4 — Prototype Engineering (OpenBraille), using this architecture as the fixed engineering baseline.
