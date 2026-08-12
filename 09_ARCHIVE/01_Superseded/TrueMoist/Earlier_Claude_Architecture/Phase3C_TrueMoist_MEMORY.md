# MC_Project_Phase3C_TrueMoist_MEMORY.md

# Project mC
## Phase 3C Memory — TrueMoist
### Final Engineering Architecture Synthesis

Version: 1.0
Status: ✅ COMPLETE
Companion to: `Phase3C_TrueMoist_Architecture_Report_by_Claude.md` (authoritative, dated July 28, 2026)

---

# Purpose

This document records the engineering knowledge, decisions, methodology, and outcomes of Phase 3C for the **TrueMoist** concept. It is the concise continuity record the architecture report itself points to (its own Section 37) but which had not yet been produced — this file closes that gap.

It is **not** intended to replace the full report. The authoritative technical findings, full disagreement-resolution reasoning, subsystem-by-subsystem specification, test matrix, and BOM remain in `Phase3C_TrueMoist_Architecture_Report_by_Claude.md`.

TrueMoist is the third of five concepts to complete Phase 3C, following OpenBraille and VibeGuard.

---

# Phase Objective

Select one final, buildable engineering architecture for TrueMoist by auditing four independently commissioned Deep Research reports (Mistral, Gemini, Perplexity, ChatGPT), resolving their disagreements with evidence rather than vote-counting, and producing a decision-grade blueprint ready for Phase 4 procurement and build.

---

# Inputs

Official Project Documentation
- Engineering Design Review (EDR) — highest authority
- Phase 3C TrueMoist SOP
- Phase 3B Report and Memory
- Phase 3A Report and Memory
- Phase 2 Report and Memory
- Project mC Decision Register
- PROJECT_CONCEPT_CONTEXT.md

Independent Engineering Research (TrueMoist Phase 3C specifically)
- Mistral, Gemini, Perplexity, ChatGPT Deep Research reports

Note: unlike some earlier phases, this evidence set is four reports, not five or six — Qwen and Kimi were not commissioned for this specific gate.

---

# Methodology

Same four-stage discipline as OpenBraille and VibeGuard: (1) concept-grounding check before touching any research report; (2) independent audit of all four reports for concept fidelity and source quality; (3) disagreement resolution by evidence, not vote-counting; (4) single architecture selection with a documented fallback, following the SOP's required report structure.

---

# Major Findings

## 1. Concept fidelity was clean across all four reports — TrueMoist's strongest evidence base yet.

All four performed an explicit concept restatement before researching and correctly restated the EDR's engineering identity, hypothesis, and MDS. No concept-swap or wrong-invention error occurred. This continues TrueMoist's unbroken clean record across Phase 2, 3A, and 3B — the portfolio's most concept-faithful concept, in contrast to TrustLatch's and ColdTrace's Phase 3A fidelity problems.

## 2. Two genuine engineering disagreements existed among the four reports; both were resolved by evidence, not by counting votes.

**EC/salinity strategy:** three of four reports (Gemini, Perplexity, ChatGPT) independently converged on treating salinity as a controlled, calibration-time-only variable; only Mistral proposed live two-electrode galvanic EC sensing. Resolved toward the three-report position — but on engineering grounds specific to this project (the live-EC path requires AC bipolar-pulse excitation circuitry that collides with the team's one documented analog-EE skill gap per Phase 3B; it also risks becoming a second, unreviewed sensor-development effort before the core hypothesis is tested; and it reinforces PDR-045's existing mandate to keep IP off custom hardware), not simply because it was the majority position.

**External ADC (ADS1115):** three of four reports (Mistral, Gemini, ChatGPT) mandated it on quantitative error-budget grounds (ESP32 internal ADC's documented ENOB degradation — roughly 9 effective bits against a nominal 12, plus RF-noise coupling from the onboard radio); only Perplexity treated it as optional pending a Week-1 comparison. Resolved to mandatory, at a marginal cost (~₹120–150) judged trivial against the budget — Perplexity's Week-1 comparison is retained as an empirical *confirmation* gate, not a decision gate.

## 3. A third, more minor disagreement (regularization) was resolved by adopting what two reports treated as merely an optional upgrade.

ChatGPT alone proposed ridge-regularized second-order regression as its default; Mistral and Gemini proposed unregularized second-order; Perplexity treated regularization as an optional upgrade path. Resolved to ridge-regularized as the default operational model — it costs nothing at runtime (same fixed-coefficient inference either way) and directly addresses the overfitting risk all four reports independently flag, given roughly 10 coefficients fit against a 135-sample dataset.

## 4. Dataset scale (proposals ranged 72–180 samples) was resolved to the convergent mid-point that also preserved full coverage on both named confounders.

Perplexity's reduced 72-sample proposal cut temperature levels from 3 to 2 to save time — but temperature is one of the two physical confounders (alongside salinity) this entire concept exists to correct, making it the wrong place to economize. The architecture report resolved to Mistral's proposal — 5 moisture × 3 temperature × 3 salinity × 3 replicates = 135 samples — as the convergent mid-point across all four proposals that also preserves full 3-level coverage on both confounders.

---

# Final Selected Architecture (Summary)

- **Overall family:** D+B hybrid — offline-trained/embedded-inference (Architecture D) hardened with a mandatory external ADC (Architecture B-style), explicitly excluding B's live-EC subsystem. Architecture C (adaptive on-device recalibration) rejected for the MVP, preserved as the concept's genuine long-term patent direction. Architecture A (temperature-only, internal ADC) is the documented fallback if Week 1–2 validation gates fail.
- **MCU:** ESP32-WROOM-32 (fallback: STM32F103 "Blue Pill")
- **ADC:** ADS1115 16-bit external I²C, mandatory by default; Week-1 comparison against internal ADC is confirmatory, not decisional
- **Moisture sensor:** commodity capacitive probe (v2.0/YL-69/HL-69-class), 2 units (primary + spare for sensor-to-sensor variability characterization)
- **Temperature sensor:** waterproof DS18B20, soil-inserted ~1–2 cm from the moisture probe at matched depth; ambient-air sensing explicitly rejected as a substitute
- **EC/salinity strategy:** controlled, calibration-time-only (3 known NaCl-solution classes: baseline/moderate/high); no live in-soil EC channel
- **Analog front end:** breadboard Week 1 only → soldered perfboard from Week 2 (PDR-050); optional MCP6002/LMV358 buffer stage; RC low-pass filtering; decoupling capacitors
- **Compensation algorithm:** offline-trained, ridge-regularized second-order multivariate polynomial regression (raw capacitance, temperature, coded salinity, cross-terms); fixed-coefficient embedded inference only, <1 ms per sample; baseline comparator = unregularized linear regression
- **Calibration dataset:** 1 homogeneous soil (e.g., sandy loam/loam, documented once); 5 moisture × 3 temperature × 3 salinity × 3 replicates = 135 samples; grouped train/validation split (~100/~35) plus a leave-one-condition-out held-out block
- **Gravimetric reference:** oven-dry at 105°C ± 5°C to constant mass (≥24 h); 0.01 g scale preferred; food-dehydrator/microwave fallback explicitly documented as increasing uncertainty
- **Mechanical rig:** rigid plastic/PVC container (~500 mL–1 L, 8–12 cm diameter); fixed-depth insertion jig; mass-controlled compaction; 20–30 min equilibration
- **Logging/interface:** USB serial CSV, mandatory; 0.96" I²C OLED, optional/demo-only
- **Power:** USB 5V bench power only, no battery
- **Validation:** RMSE primary, MAE/R²/disturbance-sensitivity secondary; target ≥25% RMSE reduction (compensated vs. uncompensated), minimum floor ≥20%
- **Cost:** ≈₹2,080 preferred core / ≈₹3,180–3,380 worst-case (OLED + purchased scale + fallback dehydrator)
- **Readiness:** Architecture Ready with Mandatory Early Validation

---

# Methodological Lessons for the Project Record

1. **A synthesis board resolving toward one report's position on one question, and a different report's position on an adjacent question, is not inconsistent** — as long as each resolution is independently justified on its own technical merits (team skill fit, error-budget quantification, marginal cost) rather than by which position happened to have more reports behind it. The EC-strategy and ADC disagreements both resolved toward their respective 3-report majorities here, but for different, specific, load-bearing reasons documented in the architecture report's Section 7 — not because "3 beats 1."

2. **"Optional upgrade" framing in a source report is not a reason to exclude an idea from the default architecture.** ChatGPT's ridge regularization was the only report to propose it as a default rather than a stretch goal; it was adopted as the default anyway once its cost (zero at runtime) and benefit (directly answers a risk all four reports flag) were evaluated independently of how the source report itself categorized it.

3. **When reports disagree on a quantity (dataset size), check whether cheaper proposals cut on the concept's own defining variables.** Perplexity's smaller, faster-to-collect 72-sample dataset looked attractive on schedule grounds alone, but its reduction came specifically from under-sampling temperature — one of the two physical effects (alongside salinity) TrueMoist's entire engineering hypothesis is built around. A convergent mid-point that preserves full coverage on the concept's own defining confounders is a stronger basis for resolution than dataset size alone.

4. **This concept carries essentially zero embedded-resource risk.** All four reports agree compute, memory, and power are non-binding constraints for this architecture — the entire engineering risk sits in experimental discipline (soil packing, insertion consistency, gravimetric procedure, dataset leakage prevention), not in MCU capability. This matches Phase 3B's own prior finding and is worth carrying forward explicitly into Phase 4 planning.

---

# Deliverables Produced

- `Phase3C_TrueMoist_Architecture_Report_by_Claude.md` — full architecture synthesis (authoritative)
- `Phase3C_TrueMoist_MEMORY.md` — this document
- `Project_mC_Decision_Register_v1_1.md` — PDR-031, 032, 045, 048, 049, 050 updated to Accepted/finalized status; PDR-058 through PDR-068 added (11 new TrueMoist-specific entries covering EC strategy, sensor selection, dataset design, validation thresholds, mechanical rig, interface, power, architecture-selection summary, regularization, and patent-scope refinement)

---

# Decisions Made

✅ Phase 3C TrueMoist is complete.
✅ The D+B-hardened architecture (offline-trained, ridge-regularized second-order regression; mandatory ADS1115; calibration-only salinity; no live EC) is the authoritative engineering reference for Phase 4.
✅ Readiness classification: Architecture Ready with Mandatory Early Validation.
✅ No rerun of Phase 3C for TrueMoist is required.

---

# Known Limitations

Phase 3C TrueMoist intentionally did not determine or attempt:
- Multi-soil or multi-season generalization (remains a held, future validation sprint per PDR-012)
- Live in-soil EC sensing or on-node adaptive/self-calibration — the concept's genuine long-term patent-relevant direction per Phase 2 (Kimi and Gemini's independently-corroborated finding), explicitly deferred to Phase 6+/a post-MVP validation sprint (PDR-068), not abandoned
- Field deployment outside controlled benchtop conditions
- Final claim-charting or formal patentability legal review against the Toro/Meter/Campbell estate and US 11,598,743 (Phase 2/5's responsibility)

---

# Transition to Phase 4

Phase 4 (procurement and physical build) should take as mandatory inputs:
- The final architecture, BOM, and system block diagram in `Phase3C_TrueMoist_Architecture_Report_by_Claude.md` (Sections 11, 12, 28)
- The Week 1–2 mandatory early validation gates (Section 8) — build sequencing should not proceed past Week 2 without these passing or their documented fallback actions being taken; if Gates 1, 3, or 4 fail and cannot be resolved by Week 2, the architecture falls back to Architecture A (temperature-only, no salinity modeling) rather than being abandoned
- The updated Decision Register entries (PDR-031, 032, 045, 048, 049, 050, and new PDR-058–068)

TrueMoist joins OpenBraille and VibeGuard as Phase-3C-complete. TrustLatch and ColdTrace remain pending this same gate.

---

# Phase Status

Phase 3C — TrueMoist
Status: ✅ COMPLETE

Authoritative Output:
`Phase3C_TrueMoist_Architecture_Report_by_Claude.md`

Next Phase:
➡️ Phase 4 — Procurement and Physical Build (TrueMoist), contingent on Week 1–2 validation gates
