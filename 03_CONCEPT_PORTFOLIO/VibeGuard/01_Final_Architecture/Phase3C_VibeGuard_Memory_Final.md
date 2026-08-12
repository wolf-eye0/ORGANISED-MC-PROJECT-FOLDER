# Phase3C_VibeGuard_MEMORY.md

# Project mC
## Phase 3C Memory — VibeGuard
### Architecture Definition & Engineering Selection

Version: 1.0
Status: ✅ COMPLETE
Methodology Version: Phase 3C

---

# Purpose

This document records the engineering knowledge, decisions, and outcomes of Phase 3C for **VibeGuard only**. It is not a replacement for `Phase3C_VibeGuard_Architecture_Report.md`; it exists so future phases (and future AI assistants) can reconstruct VibeGuard's architecture context without reprocessing the full report or the four independent research passes.

---

# Phase Objective

Convert VibeGuard's Phase 3B-validated feasibility into a concrete, evidence-based architecture: sensor, MCU, signal-processing pipeline, edge-intelligence strategy, mechanical/electrical design, cost, and a Phase 4 readiness classification — while resolving the three specific disagreements Phase 3B left open (DSP-vs-ML, sensor bandwidth, ML necessity).

---

# Inputs

- `Phase3C_VibeGuard_SOP_Final.md` — governing SOP for this phase
- `Phase3C_VibeGuard_DeepResearch_Prompt` (Parts 1–4) — commissioning document
- `Engineering_Design_Review.md` — VibeGuard section (authoritative Engineering Identity/Hypothesis/Fixed Design Principles)
- `Phase3B_Report_by_Claude.md` and `Phase3B_MEMORY.md` — VibeGuard's Phase 3B feasibility findings
- `PROJECT_CONCEPT_CONTEXT.md`
- Four independent Phase 3C Deep Research reports: Gemini, Mistral, Perplexity, Qwen

---

# Selected Architecture

**Sensor:** ADXL345 (3-axis digital MEMS accelerometer, SPI interface, ±2–16g selectable range, 13-bit resolution, 3,200 Hz max ODR / 1,600 Hz Nyquist bandwidth). Cost: ₹130–350.

- **Upgrade path (documented, not required for MVP):** IIS3DWB (6,000 Hz bandwidth, ~₹800–1,200) if the team later wants bearing-fault-range coverage beyond the MDS's low-frequency imbalance/misalignment demonstration scenarios.
- **Rejected:** MPU6050 (gyroscope adds unused EMI-susceptible data), ADXL1002 (₹5,500+, breaches budget alone), SW-420 (binary threshold switch only, cannot support FFT/classification).

**MCU:** ESP32 (WROOM-32 or S3-class). Dual-core, 240 MHz, hardware FPU, 520 KB SRAM, DMA-capable SPI. Cost: ₹300–500. STM32F4-class is the confirmed fallback. Arduino Uno-class and RP2040 are disqualified (no hardware FPU / insufficient RAM for real-time FFT).

**Electrical interface:** SPI, not I²C — I²C's ~400 kHz ceiling cannot sustain the ADXL345's full 3,200 Hz three-axis output rate without buffer overflow. Shared 3.3V logic rail (both devices native 3.3V, no level shifter needed). 0.1 µF decoupling at sensor supply pins.

**Signal processing pipeline:**
1. DC removal / mean subtraction
2. Hann windowing (controls FFT spectral leakage)
3. Continuous time-domain features: RMS, peak, crest factor, kurtosis, standard deviation
4. Triggered FFT (256–1,024 points) only when time-domain features cross a first threshold

**Edge intelligence strategy:** Staged.
- **MVP (lowest risk):** Calibrated single-feature threshold on RMS, with a persistence/duration requirement to reject transient shocks.
- **Primary target (recommended, not a stretch goal):** Mahalanobis-distance multivariate anomaly detector over the calibrated feature vector (RMS, crest factor, kurtosis, top spectral peaks) — unsupervised, no labeled-failure-data requirement, fully explainable.
- **Explicitly out of scope for this semester:** Supervised deep-learning TinyML (CNN, trained autoencoder) — rejected by all four independent reports on the same grounds (machines run "Normal" ~99% of the time; labeled failure data is not realistically obtainable).

**Noise-isolation strategy:** Baseline spectral subtraction (capture ambient/background spectral envelope during calibration; subtract from live FFT bins) plus band-limited features and proximity-based mounting. **This is documented as a prototype-testing item, not a solved research question** — the mitigation techniques are established engineering practice, but their adequacy against real ambient interference can only be confirmed empirically.

**Mechanical integration:** Rigid mounting only — epoxy/cyanoacrylate-bonded 3D-printed bracket, or bolt-mount, directly to the machine housing. Magnetic and foam-adhesive mounts explicitly rejected (act as unintended low-pass filters).

**Output indication:** Common-cathode RGB LED (Green = Normal, Red = Abnormal, Blue = Calibrating). Satisfies the MDS's "clear output" requirement without added display complexity.

**Test rig / validation scenario:** Small 12V DC motor or PC fan on a heavy, vibration-damped base. Primary scenario: attach an eccentric mass (binder clip, tape, epoxy putty) to simulate rotor imbalance. Secondary scenario: progressively loosen mounting bolts.

**Estimated cost:** ₹1,700–2,200 (ADXL345 route, recommended for MVP); ~₹4,000 (IIS3DWB route, optional upgrade). Both comfortably inside the ₹5,000 ceiling.

---

# Major Engineering Risks

1. **Single-node spatial/spectral noise isolation** — VibeGuard's defining hard problem since Phase 3A, carried forward unresolved-in-principle but now with concrete, cite-able mitigation techniques (spectral subtraction, band-limited features) ready for prototype testing.
2. **SPI signal integrity over breadboard prototype wiring** — newly identified this round (Gemini): capacitive loading degrades signal above ~2 MHz on jumper wires. Mitigation: start at 100 kHz–1 MHz clock, step up; move to soldered perfboard for the final build.
3. **Mechanical coupling quality** — unanimous concern; resolved at the architecture-selection level by mandating rigid mounting only.
4. **MCU compute/memory exhaustion running FFT** — resolved at the platform-selection level (FPU-equipped MCU mandated; FFT size capped at 256–1,024 points; KISS_FFT or CMSIS-DSP libraries recommended).

---

# Unresolved Questions for Phase 4

1. **Team headcount ambiguity (5 vs. 6).** `Phase3C_VibeGuard_SOP_Final.md` and the Phase 3C deep research prompt both state "five-member team" but then list role categories (3 CS/Cybersecurity + 1 beginner + 2 hardware/fabrication) that sum to six. This is a documentation inconsistency in the project's own source material, not a research-report error, and should be clarified by the project owner before Phase 4 task allocation is finalized. The recommended architecture and task breakdown work unchanged under either reading.
2. **Final sensor choice (ADXL345 vs. IIS3DWB).** ADXL345 is recommended for the MVP as it comfortably covers the low-frequency fault types (imbalance, misalignment) the MDS's own test scenarios exercise. IIS3DWB remains a documented, affordable (~+₹650–1,050) upgrade path if the team wants bearing-fault-range bandwidth. This is a preference decision, not an open technical question.
3. **Exact statistical threshold tuning** (number of standard deviations for the Mahalanobis distance cutoff, persistence duration for the RMS threshold) — inherently empirical; to be determined during prototype bring-up (Stage 7 of the bring-up sequence), not before.

---

# Methodological Findings Carried Forward

1. **Qwen achieved a full fidelity recovery on VibeGuard this round**, after producing this pipeline's sharpest concept-swap failure on this exact concept in Phase 3B (invented active noise/vibration-cancellation actuator). No exclusion was required for any report in this phase — a first for VibeGuard.
2. **A team-headcount inconsistency in the project's own source documents (`Phase3C_VibeGuard_SOP_Final.md`, deep research prompt) was surfaced during this audit** — three role categories described in the SOP sum to six people against a stated five-member team. Recommend correcting at the source before further research commissioning, following the same logic that led Phase 3A's findings to elevate the EDR as the primary grounding document for Phase 3B.
3. **Cost figures across independently-commissioned reports require BOM-completeness normalization before comparison** — Qwen's ~₹1,170 headline figure omits any test-rig/motor cost that both Gemini and Mistral itemize explicitly; the corrected, comparable figure is closer to ₹1,500–1,700.
4. **The Phase 3B "DSP-vs-ML" disagreement narrowed to a smaller, more tractable disagreement** (single-feature threshold vs. multivariate statistical anomaly detection) rather than resolving to unanimity or requiring further research — consistent with Phase 3B's own prediction that this would be "resolved as an ordinary architecture-selection decision within Phase 3C itself."

---

# Decisions Made

✅ Phase 3C (VibeGuard) is complete.
✅ ADXL345 + ESP32 + tiered DSP pipeline + staged threshold-then-Mahalanobis edge intelligence is the recommended architecture for Phase 4.
✅ IIS3DWB is documented as an optional upgrade path, not a requirement.
✅ Single-node noise isolation adequacy is explicitly deferred to prototype testing, not treated as a blocking research gap.
✅ Team headcount ambiguity (5 vs. 6) is flagged to the project owner for explicit resolution, not resolved unilaterally by this synthesis.

---

# Phase Status

Phase 3C (VibeGuard)
Status: ✅ COMPLETE

Authoritative Output: `Phase3C_VibeGuard_Architecture_Report.md`

Next Phase: ➡️ Phase 4 — Detailed Design & Prototype Implementation (VibeGuard), pending the project owner's parallel Phase 3C passes on TrueMoist, TrustLatch, ColdTrace, and OpenBraille's resolution of its own strategic fork.
