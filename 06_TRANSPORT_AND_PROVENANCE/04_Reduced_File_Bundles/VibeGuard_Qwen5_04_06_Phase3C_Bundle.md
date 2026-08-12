# VibeGuard Qwen Transport Bundle — Canonical Documents 04–06

## File-control notice

This attachment contains three separate canonical VibeGuard Phase 3C
documents combined solely to satisfy Qwen's five-attachment limit.

Each enclosed document remains a separate logical source.

Nothing has been summarized, corrected, reconciled or omitted.

---

<!-- BEGIN CANONICAL DOCUMENT 04:
04_Phase3C_VibeGuard_Architecture_Report_Final.md -->
# Phase 3C — VibeGuard Architecture Definition & Engineering Selection
## Chief Engineering Review Board Synthesis
### Project mC — Patent-Oriented Embedded Systems Innovation Pipeline

**Status:** ✅ Complete
**Evidence base:** Four independent Phase 3C Deep Research reports (Gemini, Mistral, Perplexity, Qwen), audited against `Phase3C_VibeGuard_SOP_Final.md`, the Engineering Design Review, and the Phase 3B Report/Memory.
**Prepared by:** Claude, acting as CTO / Embedded Systems Architect / IEEE Reviewer / Patent Analyst / VC / Innovation Strategist simultaneously, per this pipeline's established synthesis methodology (Phase 2, 3A, 3B).

---

## How to read this report

This report follows the same two-stage discipline used in Phase 3A and Phase 3B: first a **mandatory fidelity audit** of each independent report against the authoritative documents (not against each other, and not against the shorter `PROJECT_CONCEPT_CONTEXT.md`), then a **synthesis** that treats validated evidence as a single pool, applies exclusion-not-averaging to anything mis-scoped, and makes explicit judgment calls — rather than vote-counting — where reports disagree for substantive reasons.

Unlike Phase 3A and 3B, this phase concerns a single concept (VibeGuard) at architecture-selection depth, so the audit and synthesis are structured around VibeGuard's own decision points rather than a five-concept portfolio.

---

# TASK 1 — Concept-Fidelity Audit

The authoritative grounding for this audit is `Phase3C_VibeGuard_SOP_Final.md` §2–§6 and the Engineering Design Review's VibeGuard section, both of which fix VibeGuard as a **passive, single-node, edge-computed detection-and-alerting system** — not signal cancellation, not a multi-sensor array, not a cloud platform.

| Report | Fidelity result |
|---|---|
| **Gemini** | Correct, high specificity. Notably, its Executive Summary explicitly names and rejects the Phase 3B active-vibration-cancellation error ("a minority of prior theoretical models erroneously framed VibeGuard as a system requiring actuators... to physically cancel out the anomalous vibration... fundamentally misaligns with the EDR"). This is the correct fidelity behavior: rather than silently avoiding the error, it identifies and repudiates it against the authoritative document. |
| **Mistral** | Correct on the core concept. Restates the EDR's Engineering Identity, Mission, Hypothesis, and Fixed Design Principles verbatim before proceeding — the "restatement-and-confirmation" behavior Phase 3B identified as a leading reliability indicator. |
| **Perplexity** | Correct, high specificity, and the most externally-grounded report — the only one citing real industrial standards (ISO 10816/20816, Honeywell and TE Connectivity condition-monitoring white papers) rather than relying primarily on component-vendor pages. |
| **Qwen** | **Correct — a marked fidelity recovery.** This is the significant methodological finding of this round. Qwen produced the sharpest failure in Phase 3B on this exact concept (a full swap into an invented active noise/vibration-*cancellation* system). In Phase 3C, Qwen's entire report is scoped correctly as passive detection: "the architecture will not incorporate advanced features like gyroscopic data fusion or complex multi-modal sensing... developing a reliable physical installation and a simple yet effective signal processing pipeline to interpret the accelerometer's output." No cancellation, no actuator, no invented mechanism anywhere. |

**Concept-fidelity risk this round: Low, across all four reports.** No exclusions are required at the concept level — a first for VibeGuard in this pipeline.

Two lower-severity issues were found during the audit and are treated as data-quality flags rather than fidelity failures (both detailed in Task 2 and §12 below):

1. **Mistral's team-roster arithmetic.** Mistral's task-breakdown table lists six named team members ("Member 1" through "Member 6") against a project that both the SOP and the EDR describe as five-member. Mistral itself flags this in a footnote ("*Note: Original description mentions 5 members total. Adjust as needed to match actual team size.*") without resolving it. This is not a concept-fidelity error — VibeGuard itself is correctly understood — but it is a real internal-consistency defect that should not be carried into Phase 4 planning uncorrected.
2. **Qwen's unattributed "directive."** Qwen states "the user's directive is clear: classical Digital Signal Processing (DSP) must serve as the baseline" — a stronger claim than what the SOP or EDR state on their own (they ask the research to *compare* DSP and ML, not mandate DSP). This may reflect wording in the specific commissioning prompt Qwen received that is not fully visible to this board; it is noted rather than treated as invented, since Qwen's own architecture choice (RMS-threshold-first, ML deferred) is well-reasoned on its own technical merits regardless of the directive's actual source.

---

# TASK 2 — Confidence Level per Report

| Report | Confidence | Reasoning |
|---|---|---|
| **Gemini** | **High** | The most technically granular of the four — the only report operating at register-level detail (specific ADXL345 offset registers 0x1E/0x1F/0x20, BW_RATE/DATA_FORMAT configuration, SPI clock-speed degradation thresholds on breadboard wiring, exact GPIO pin mapping). Explicitly identifies and resolves the SPI-vs-I²C bandwidth bottleneck — a genuinely new technical finding this pipeline had not previously surfaced. Correctly and explicitly repudiates the Phase 3B Qwen error. Minor flag: understates the hardware/fabrication sub-team as one person against the SOP's "two members" wording (§12). |
| **Mistral** | **High** | The most exhaustive sensor and MCU comparison (five accelerometer candidates including IIS3DWB, LIS3DH, and MMA8452Q — a richer field than any other report considered), and the only report to give a fully itemized, contingency-inclusive BOM (₹4,070 with 10% margin). Report structure leans heavily on restating the commissioning prompt's own tables rather than original prose synthesis in several sections, which inflates length without proportionally inflating insight — but its final recommendation (§3.13) is concrete and well-justified. Team-roster defect noted above is a real, if contained, quality issue. |
| **Perplexity** | **High** | The best externally-cited report (real ISO standards and industrial white papers, not just vendor/hobbyist pages), and the most complete on validation methodology, reliability, and procurement. Notably more conservative/generic on hardware commitment — it never names a specific sensor part number, staying at "a digital MEMS accelerometer, ~2–3 kHz usable bandwidth" throughout, which makes it less directly actionable for procurement than Gemini or Mistral, though its underlying reasoning is sound. |
| **Qwen** | **Medium-High** *(upgraded from Low in Phase 3B)* | The clear fidelity recovery is the headline finding — see Task 1. The report is also the shortest and thinnest of the four (94 lines vs. Perplexity's 462 and Mistral's 1,319), and its cost estimate (§10 below) omits the test-rig/motor cost that both Gemini and Mistral itemize, making its "~₹1,170" headline figure not directly comparable to the others' totals. Its citations are real and specific (datasheet links, ResearchGate, MDPI), which is consistent with — and probably causally related to — its improved fidelity this round. |

**Consequence for synthesis:** All four reports are retained at full weight for VibeGuard. This is the first phase in this pipeline where no report required exclusion on this concept.

---

# SYNTHESIS

## 1. Engineering Feasibility Summary

All four reports converge, independently, on the same architecture family: **a single MEMS accelerometer, rigidly mounted to a small motor/fan test rig, feeding an ESP32-class MCU that performs time-domain and frequency-domain feature extraction locally, with a decision layer ranging from simple thresholding to lightweight statistical anomaly detection.** This is the tightest four-way architectural convergence VibeGuard has shown across Phase 3A, 3B, and now 3C. The three disagreements Phase 3B carried into this phase (DSP-vs-ML, sensor bandwidth, ML necessity) have all narrowed substantially — none has been erased, but none remains a fork requiring further research either. Both new fidelity risk (concept-swap) and the review board's own supplementary judgment calls are addressed below.

## 2. Consensus Findings

- **Architecture class:** Single-node MEMS accelerometer + MCU, edge-computed. Multi-sensor arrays, industrial piezoelectric transducers, and cloud-tethered designs are unanimously eliminated on cost/complexity grounds, consistent with Phase 3B.
- **MCU:** ESP32 (WROOM-32 or S3-class) is the primary recommendation in all four reports, on the same grounds each time — hardware FPU for FFT, sufficient SRAM for windowed buffers, DMA-capable peripheral bus, mature Arduino-ecosystem tooling matching the team's CS/Cybersecurity background. STM32 (F4-class, with FPU) is the consistent fallback if ESP32 is unavailable.
- **Mounting:** Rigid coupling (epoxy/superglue to a 3D-printed bracket, or bolt-mount) directly to the machine housing is unanimous. Magnetic mounts and foam adhesives are explicitly and independently rejected by three of four reports (Gemini, Qwen, Perplexity) as mechanical low-pass filters that would destroy the fault signatures the algorithm depends on.
- **Signal pipeline shape:** All four independently arrive at the same two-tier structure — cheap, always-on time-domain features (RMS, peak, variance/standard deviation, crest factor, kurtosis) running continuously, with a more expensive FFT/spectral stage triggered only when the cheap stage crosses a threshold. This tiered design was not explicit in Phase 3B and represents genuine architectural progress.
- **Edge intelligence, negative consensus:** All four reports independently reject supervised deep-learning TinyML (CNNs, trained autoencoders) as inappropriate for the MVP, and for the same reason — a normally-operating machine produces overwhelmingly "Normal" data, so labeled-failure datasets are not realistically obtainable by a student team in one semester. This is a stronger and more specific convergence than Phase 3B had; in Phase 3B, Gemini's position was read as "ML is required." In Phase 3C, Gemini itself has moved off that position (see §3(a)).
- **Test scenario:** An unbalanced rotor (small DC motor or fan with an attachable eccentric mass — a binder clip, tape, or epoxy putty) is the unanimous primary validation scenario. Loosened mounting bolts is the consistent secondary/backup scenario (Mistral, Perplexity).
- **Budget:** All four estimates land comfortably inside ₹5,000, with a wider spread than Phase 3B's ₹1,000–4,700 range would suggest at first glance once cost-comparability is corrected (see §10).

## 3. Resolution of the Three Phase 3B Disagreements

### (a) Classical DSP vs. Edge AI/ML

Phase 3B recorded this as a genuine three-way split: Mistral/Perplexity favored DSP-first, Gemini argued pure time-domain was inadequate and recommended edge-AI spectral analysis outright. **That split has narrowed, not resolved to unanimity, but narrowed in an important way: no report now proposes supervised deep-learning ML for the MVP.** What remains is a genuine but smaller disagreement about how much statistical sophistication belongs in the *decision rule* itself:

| Position | Reports | Mechanism |
|---|---|---|
| Simple calibrated threshold on RMS/peak | Qwen, Perplexity | Deterministic, zero training, matches MDS literally |
| Classical DSP (FFT + envelope/spectral features) feeding a threshold | Mistral | Same determinism, richer feature set, TinyML deferred as "future enhancement" |
| Unsupervised one-class statistical anomaly detection (Mahalanobis distance over a multivariate feature vector — RMS, crest factor, kurtosis, top spectral peaks) | Gemini | Still zero labeled-failure-data requirement, still fully explainable, but a genuine step beyond single-variable thresholding |

This board's judgment: **Gemini's position is the more defensible one for genuinely satisfying the EDR's "reliably distinguish" language, and it is not actually in tension with the other three** — a Mahalanobis-distance classifier is not "ML" in the sense the SOP warns against ("do not use machine learning merely for appearance"); it requires no training data beyond the same normal-baseline calibration every report already proposes, and it is exactly as explainable as a threshold, just multivariate rather than univariate. **Recommendation: implement the single-feature threshold first (satisfies the literal MDS at lowest risk, and is what three of four reports treat as sufficient), and treat the multivariate statistical layer as the immediate next increment within Phase 3C's own architecture — not a stretch goal requiring new tooling, since it uses the same calibration data already being collected.** True supervised TinyML (CNN, trained autoencoder) should be treated as genuinely out of scope for this semester, consistent with all four reports.

### (b) Sensor bandwidth: is ADXL345 (1,600 Hz) adequate, or is IIS3DWB (6,000 Hz) required?

Mistral is the only report to select IIS3DWB; Gemini and Qwen both explicitly select ADXL345 and consider its bandwidth adequate; Perplexity stays generic ("~2–3 kHz usable bandwidth," implicitly ADXL345-class). This disagreement is real but resolvable by attending to what the MDS actually requires demonstrating: the EDR and SOP's minimum demonstrable success calls for a **deliberately introduced abnormal vibration condition** — every report's own proposed test scenario is an unbalanced rotor or a loosened mount, both of which are low-frequency phenomena (1×–3× shaft rotational frequency, typically well under 200 Hz for any lab-safe motor). ADXL345's 1,600 Hz bandwidth (Nyquist limit from its 3,200 Hz ODR) has enormous margin over that. IIS3DWB's extra bandwidth matters specifically for **high-frequency bearing-race spalling signatures** — a real and important predictive-maintenance phenomenon, but not what any of the four proposed MVP test scenarios actually exercises.

**Recommendation: ADXL345 as the default MVP sensor** — it satisfies the literal MDS, it is the cheapest option by a wide margin (₹130–350 vs. ₹800–1,200), and three of four independent reports converge on it once Mistral's own reasoning is examined against its own test-scenario choice rather than in the abstract. **IIS3DWB should be documented as the upgrade path** if the team wants margin for later bearing-fault work beyond the MVP (Mistral's BOM shows this costs only ~₹650–1,050 more, which is still comfortably inside budget) — this is exactly the kind of "what was simplified, and what future version restores the advanced capability" documentation the SOP's Innovation Preservation Requirement (§5) calls for.

### (c) Is single-node noise isolation demonstrable at all?

This was flagged in Phase 3A and Phase 3B as VibeGuard's one genuinely hard, unsolved problem, and it remains exactly that — but Phase 3C has produced real candidate mitigation techniques for the first time, rather than just re-flagging the difficulty:

- **Gemini:** Baseline spectral subtraction — capture the ambient/background spectral envelope during calibration, subtract it from live FFT bins during monitoring, explicitly rejecting computationally prohibitive blind-source-separation methods (FastICA, SSA, EEMD) as exceeding the ESP32's real-time budget.
- **Qwen:** In-situ baseline establishment plus proximity/band-limited features — mount as close to the source as possible and rely on the fact that a target machine's fault harmonics often occupy different bands than broadband ambient/HVAC noise.
- **Perplexity:** Approximates isolation via controlled experimental design (only the target machine's condition changes; background is held fixed) rather than claiming the algorithm itself solves blind isolation.
- **Mistral:** Declines to claim the problem is solved — lists it as a "Known Unknown" resolvable only through prototype testing, with a documented contingency (multi-sensor array) if single-node isolation proves inadequate.

**This board's judgment, consistent with the SOP's own instruction to differentiate research questions from prototype-testing questions:** the mitigation techniques above (spectral subtraction, proximity + band-limited features, controlled-experiment design) are real, cite-able engineering practice and should be implemented — but their *adequacy* is not something further research can establish; it is empirically testable only once a physical rig exists. This is not a gap in the research; it is the correct place for research to stop and prototyping to begin, and all four reports (to varying degrees of explicitness) reach the same place.

## 4. Sensor Evaluation

| Sensor | Bandwidth | Cost (INR) | Recommended by | Verdict |
|---|---|---|---|---|
| **ADXL345** | 1,600 Hz (from 3,200 Hz ODR) | ₹130–350 | Gemini, Qwen (primary); implicit in Perplexity | **Selected for MVP** — adequate for the literal test scenarios, cheapest, best-documented in academic/hobbyist literature (lowest implementation risk) |
| IIS3DWB | 6,000 Hz | ₹800–1,200 | Mistral (primary) | Recommended upgrade path for future bearing-fault work; not required for MVP |
| MPU6050 | ~1,000 Hz (gyro-inclusive) | ₹80–400 | Considered, rejected by all four | Gyroscope adds EMI susceptibility (Gemini flags this specifically — relevant since the sensor operates near AC induction motors) and unused angular-rate data; no report recommends it |
| ADXL1002 | 21,000 Hz | ₹5,500–7,900+ | Considered, rejected by all four | Industrial-grade; instantly breaches the entire project budget on the sensor alone |
| SW-420 (piezo switch) | N/A (binary) | ₹37–63 | Considered, rejected by Gemini | Threshold switch only — cannot output continuous data for FFT; fails the MDS's "classify" requirement outright |

## 5. Embedded Platform Evaluation

ESP32 (WROOM-32 class) is the unanimous primary recommendation: 240 MHz dual-core Xtensa LX6, 520 KB SRAM, hardware FPU, DMA-capable SPI, ₹300–500. This is consistent with — and reinforces — Phase 3B's own cross-portfolio finding that ESP32/STM32 is a shared platform investment across the whole five-concept portfolio, not a VibeGuard-specific decision. STM32F4-class (Cortex-M4, hardware FPU) is the universal fallback if ESP32 sourcing fails. Arduino Uno-class (ATmega328P, no FPU, 2 KB RAM) and RP2040 (no hardware FPU) are both explicitly disqualified by multiple reports for real-time FFT — RP2040's absence of hardware floating point is specifically flagged by Gemini as disqualifying despite its otherwise-attractive PIO peripheral.

**One new, genuinely useful technical finding from this round, not previously surfaced in Phase 3A or 3B:** Gemini identifies that achieving the ADXL345's full 3,200 Hz output data rate requires **SPI, not I²C** — I²C's ~400 kHz Fast-Mode ceiling cannot sustain three-axis 16-bit samples at that rate without buffer overflow. This is a concrete, checkable engineering constraint that should be treated as settled rather than re-litigated in Phase 4: **the electrical architecture must use SPI.**

## 6. Signal Acquisition & Processing Pipeline

**Sampling:** 1–5 kHz (Perplexity, matched to lab-motor fault frequencies) up to the sensor's full 3,200 Hz ODR (Gemini) is the practical range; Mistral's 25–50 kHz recommendation is scoped to the higher-bandwidth IIS3DWB sensor and is not applicable if ADXL345 is selected per §3(b). Hardware-timer or interrupt/DMA-driven acquisition (triggered off the sensor's FIFO watermark via its INT1 pin, per Gemini) is preferred over software polling to avoid the sampling jitter that would corrupt FFT phase accuracy.

**Pipeline (unanimous shape):**
1. DC removal / mean subtraction
2. Windowing (Hann, per Gemini — specifically to control spectral leakage from finite-block FFT)
3. Time-domain features: RMS, peak, crest factor, kurtosis, standard deviation — computed continuously, cheaply
4. Triggered FFT (256–1,024 points) only when time-domain features cross a first-tier threshold — controls compute load on a constrained MCU while preserving diagnostic depth when it matters

## 7. Edge Intelligence Strategy — Recommended Direction

Per §3(a): implement a calibrated single-feature threshold (RMS, with a persistence/duration requirement to reduce false alarms from transient shocks — flagged by Perplexity) as the MVP decision rule, immediately extended to a Mahalanobis-distance multivariate anomaly detector over the calibrated feature vector (RMS, crest factor, kurtosis, top spectral peaks) as the primary target architecture, since it requires no additional data collection burden and is the strongest of the four positions for actually satisfying "reliably distinguish" rather than merely "detect a gross change." Supervised deep TinyML remains out of scope for this semester across all four reports and this board's own judgment.

## 8. Mechanical & Electrical Architecture

- **Mounting:** Rigid — 3D-printed bracket bolted or bonded (epoxy/cyanoacrylate) directly to the motor/fan housing. No magnetic or foam-adhesive mounting for the final demonstration.
- **Interface:** SPI (not I²C — see §5), 3.3V shared logic rail between ESP32 and ADXL345 (both operate natively at 3.3V, eliminating level-shifter complexity), 0.1 µF decoupling capacitor at the sensor's supply pins.
- **Indication:** A common-cathode RGB LED (Green/Red/Blue for Normal/Abnormal/Calibrating) satisfies the MDS's "clear output" requirement without added display complexity; an optional small OLED can be added later for numeric feature readout if time permits (Perplexity), but is not required.
- **Test rig:** A small 12V DC motor or PC cooling fan on a heavy, vibration-damped base (plywood or acrylic), with an attachable eccentric mass for the primary fault-injection scenario.

## 9. Cost Assessment

| Report | Total (INR) | Notes |
|---|---|---|
| Gemini | ₹1,919–2,207 | ADXL345 route; includes 20% contingency and full test-rig cost |
| Mistral | ₹4,070 | IIS3DWB route; includes dedicated test rig and 10% contingency |
| Perplexity | Not itemized | States "comfortably within ₹3,000–5,000" |
| Qwen | ~₹1,170 *(incomplete)* | **Flag: omits any motor/test-rig line item.** Adding a comparable rig cost (~₹300–500, per Gemini's and Mistral's own itemization) brings Qwen's realistic total to roughly ₹1,500–1,700 |

All four estimates — Qwen's once corrected — land well inside the ₹5,000 ceiling, with the ADXL345 route (Gemini/Qwen) landing near ₹1,700–2,200 and the IIS3DWB route (Mistral) near ₹4,000. **Budget confidence: High**, with ample headroom for the ADXL345-to-IIS3DWB upgrade path if the team chooses it later.

## 10. Engineering Risk Assessment & Kill Factors

| Risk | Cross-report support | Mitigation |
|---|---|---|
| Poor/loose mechanical coupling acting as an unintended low-pass filter | Unanimous (all four) | Rigid epoxy/bolt mounting only; no breadboard-dangling sensor for the final demo |
| SPI signal integrity over prototype wiring (capacitive loading above ~2 MHz on breadboard jumpers) | Gemini (new, specific, checkable) | Step SPI clock down from 5 MHz to 1–2 MHz; move to soldered perfboard for the final build rather than breadboard |
| Single-node spatial/spectral noise isolation inadequate in practice | Unanimous, carried from Phase 3A/3B | Baseline spectral subtraction + controlled-experiment validation; explicitly flagged as a prototype-testing item, not a research gap (§3c) |
| MCU compute/memory exhaustion running FFT | Gemini, carried from Phase 3B | Resolved at the platform-selection level by mandating an FPU-equipped MCU (ESP32/STM32); use KISS_FFT or CMSIS-DSP, constrain FFT size to 256–1,024 points |
| Lack of genuine failure data | Gemini, Mistral | Drives the universal rejection of supervised ML (§3a) — not a risk to mitigate so much as a constraint that has already shaped the recommended architecture |
| Component/schedule delays | Mistral, Perplexity | Order ESP32 and sensor early; multiple Indian suppliers confirmed available for both candidate sensors and both candidate MCUs |

## 11. Team Feasibility

Three of four reports (Qwen, Perplexity, and Mistral's underlying task list before its own roster error) describe the team as **3 CS/Cybersecurity-strong + 1 beginner programmer + 2 hardware/fabrication members = 6 people**; Gemini describes it as **3 + 1 + 1 = 5**. This is not, on inspection, a fault introduced by any individual report — **the underlying project documents themselves are internally inconsistent on this point.** `Phase3C_VibeGuard_SOP_Final.md` §6 and the Phase 3C deep research prompt's Team Context both state "five-member student team" and then list three role categories (3 CS/Cybersecurity, 1 beginner, 2 hardware/fabrication) that sum to six. `PROJECT_CONCEPT_CONTEXT.md` states only "five members... three technically strong CS/Cybersecurity students" without resolving the remaining two roles at all.

**This is flagged to Yozo as an open documentation item, not resolved unilaterally by this synthesis** (following the same pattern used for OpenBraille's team-fit strategic fork in Phase 3B): either the "one beginner programmer" is one of "the two hardware-oriented members" (making the real headcount 3 + 2 = 5, with one of the two hardware members also picking up light programming tasks), or the team is genuinely six people and every document undercounts by one. Both readings support the architecture unchanged — the task allocation below assumes 5 and can absorb a 6th member into the hardware/fabrication track without restructuring:

- **2 members — Firmware & signal processing:** MCU bring-up, SPI/DMA acquisition, FFT/feature-extraction pipeline
- **1 member — Edge intelligence:** Calibration logic, threshold/Mahalanobis-distance classifier, noise-mitigation (spectral subtraction)
- **1 member (beginner) — Systems logic:** LED/output mapping, calibration-sequence state machine, serial logging — a genuinely manageable, well-scoped on-ramp per all four reports
- **1 (or 2) members — Hardware/mechanical:** Component sourcing, test-rig fabrication, rigid sensor mounting, assembly, documentation

## 12. Innovation Discussion

Per the SOP's Innovation Preservation Requirement, the architecture above preserves VibeGuard's core differentiator — edge-computed intelligence rather than a bare sensor relay — while simplifying the hardest part (true single-node blind source separation, which all four reports agree is computationally out of reach on this hardware) down to baseline-calibrated spectral subtraction and band-limited features. What is preserved, what is simplified, and why:

- **Preserved:** Local, edge-computed classification; single-node (no sensor array); interpretable, explainable decision logic; affordability.
- **Simplified:** True blind-source separation (FastICA/SSA/EEMD) is replaced with baseline spectral subtraction and controlled-experiment validation. This is a genuine capability reduction, honestly documented rather than hidden, consistent with the SOP's explicit requirement.
- **Future path:** IIS3DWB sensor swap for bearing-fault-range bandwidth; ESP32's dormant Wi-Fi stack could later support a low-bandwidth MQTT alert mesh across multiple VibeGuard nodes (Gemini) — genuine scalability headroom that does not require redesigning the core architecture.
- **Genuine innovation surface for later phases:** the specific combination of in-situ baseline calibration + band-limited spectral subtraction + multivariate statistical (not neural) anomaly detection, executed entirely on a sub-₹2,000 single-node platform, is the most concrete, demonstrable technical claim this pipeline has produced for VibeGuard to date. This board makes no patentability claim at this stage, per the SOP's explicit prohibition (§18), but notes it as the strongest candidate innovation surface identified so far.

## 13. Final Engineering Recommendation

**Recommended architecture:** ADXL345 (SPI interface, rigid epoxy/bolt-mounted) → ESP32 (hardware FPU, DMA/interrupt-driven acquisition) → tiered signal pipeline (continuous RMS/peak/crest-factor/kurtosis, triggered 256–1,024-point Hann-windowed FFT) → calibrated single-feature threshold as the MVP decision rule, immediately extended to a Mahalanobis-distance multivariate anomaly detector as the primary target, with baseline spectral subtraction for noise mitigation → RGB LED output → unbalanced-rotor test rig as the primary validation scenario, loosened-mount as secondary.

**Estimated cost:** ₹1,700–2,200 for the ADXL345 route (recommended for MVP); documented upgrade path to ~₹4,000 with IIS3DWB if the team later wants bearing-fault-range bandwidth. Both comfortably inside the ₹5,000 ceiling.

**Remaining engineering uncertainties (properly scoped as prototype-testing items, not research gaps):**
1. Whether the proposed noise-mitigation techniques (spectral subtraction, band-limited features) achieve adequate single-node isolation in practice — testable only once a rig exists.
2. The exact statistical threshold (number of standard deviations, persistence duration) needed to balance false alarms against missed detections — inherently an empirical calibration exercise.
3. Whether the team is five or six people — an open documentation item for the project owner, not an engineering blocker either way.

**Phase 3C Decision Gate:**

### ✅ READY WITH MINOR REFINEMENTS

This matches the independent conclusions of three of the four source reports (Mistral and Gemini use this label explicitly; Qwen calls it "READY," slightly more optimistic but directionally identical; Perplexity does not use a formal label but concludes the architecture is "ready to proceed into Phase 4"). The architecture is fundamentally sound, satisfies every element of the Minimum Demonstrable Success, comfortably clears the budget gate, and matches the team's stated skill profile — the "minor refinements" are the three empirically-scoped items above, exactly the kind of remaining work the SOP's decision-gate definition (§16) describes as consistent with this classification rather than with "requires additional investigation."

---

# Methodological Notes Carried Forward

1. **Qwen's fidelity recovery is this round's headline process finding.** After failing this exact concept in Phase 3B (active-cancellation swap) and a different concept in Phase 3A (TrustLatch/SiliconFingerprint swap), Qwen produced a fully correct VibeGuard section this round. This is the first clean pass Qwen has had on VibeGuard specifically, and worth tracking in future phases as a (cautiously) positive signal rather than assuming the prior failure pattern will recur by default.
2. **A new document-inconsistency was surfaced, not introduced, by this audit:** the 5-vs-6 team-headcount arithmetic in the project's own SOP and deep research prompt (§11). This should be corrected at the source before Phase 4 commissions any further research, the same way Phase 3A's short-form-document finding led to using the EDR as the primary grounding document in Phase 3B.
3. **Cost figures across independently-commissioned reports are not automatically comparable** — Qwen's lower headline total reflects an incomplete BOM (missing test-rig cost), not a genuinely cheaper architecture. Future cost synthesis should normalize for BOM completeness before comparing totals across reports.
4. **The DSP-vs-ML disagreement did not resolve to unanimity, but resolved to a narrower and more tractable disagreement** (threshold vs. multivariate-statistical, rather than DSP vs. neural-network ML). This is the kind of narrowing Phase 3B predicted would happen "as an ordinary architecture-selection decision within Phase 3C itself rather than requiring a further research pass" — which is exactly what occurred.

---

**Phase 3C Status (VibeGuard): ✅ Complete.**
**This document is the official Phase 3C Architecture Report for VibeGuard and the mandatory input to Phase 4.**
<!-- END CANONICAL DOCUMENT 04:
04_Phase3C_VibeGuard_Architecture_Report_Final.md -->

---

<!-- BEGIN CANONICAL DOCUMENT 05:
05_Phase3C_VibeGuard_Memory_Final.md -->
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
<!-- END CANONICAL DOCUMENT 05:
05_Phase3C_VibeGuard_Memory_Final.md -->

---

<!-- BEGIN CANONICAL DOCUMENT 06:
06_Phase3C_VibeGuard_SOP_Final.md -->
# Phase 3C — VibeGuard Architecture Definition & Engineering Selection

## Standard Operating Procedure (SOP)

**Project:** Project mC
**Concept:** VibeGuard
**Phase:** 3C — Architecture Definition & Engineering Selection
**Status:** Pre-Research / Architecture Investigation

---

# 1. Purpose

Phase 3C converts the validated VibeGuard engineering concept into a concrete, evidence-based prototype architecture.

Phase 3B established that VibeGuard is potentially feasible for the student team and that its core engineering direction is a low-cost embedded edge-intelligent system capable of distinguishing normal machine vibration from deliberately introduced abnormal vibration.

Phase 3C determines:

* what sensing architecture should be used,
* what processing architecture should be used,
* what embedded hardware is appropriate,
* how vibration data should be acquired and processed,
* how abnormal vibration should be classified,
* how the system should isolate relevant machine vibration from environmental or neighboring-machine noise,
* what minimum prototype architecture can demonstrate the hypothesis,
* and whether the architecture is realistically buildable within the project's budget, timeline, and team capabilities.

This phase is an **architecture-selection phase**, not a prototype-building phase.

---

# 2. VibeGuard Engineering Identity

## Mission

Develop an affordable embedded system capable of detecting early abnormal machine vibration so that developing machine faults can be identified before they contribute to production disruption or degraded machine performance.

## Engineering Hypothesis

A low-cost embedded edge-intelligent system can distinguish normal machine vibration from deliberately introduced abnormal vibration using local vibration sensing and lightweight on-device analysis, without requiring cloud processing or expensive industrial condition-monitoring equipment.

## Minimum Demonstrable Success

The minimum prototype shall:

1. Sense vibration from a selected machine or mechanical test setup.
2. Establish or recognize a normal operating vibration condition.
3. Detect a deliberately introduced abnormal vibration condition.
4. Classify the observed condition as at least:

   * Normal
   * Abnormal
5. Perform the core classification locally on the embedded system.
6. Produce a clear output indicating the detected condition.

The prototype does not need to perform complete industrial predictive-maintenance forecasting.

It must first demonstrate that the fundamental engineering hypothesis works.

---

# 3. Phase 3C Primary Question

The central question of Phase 3C is:

> What is the simplest, lowest-cost, technically defensible embedded architecture that can reliably demonstrate edge-based normal-versus-abnormal vibration classification while preserving VibeGuard's intended innovation direction?

---

# 4. Scope

Phase 3C shall investigate and select:

### Sensing

* vibration sensor technology
* sensor placement
* sensor mounting
* sampling requirements
* signal quality
* environmental-noise considerations

### Embedded Processing

* MCU / embedded processing platform
* sampling architecture
* signal preprocessing
* feature extraction
* classification approach
* memory and computational requirements

### Edge Intelligence

Investigate practical low-cost approaches such as:

* threshold-based features
* statistical features
* frequency-domain features
* lightweight machine-learning models
* anomaly detection
* embedded classification

The final architecture must explain why the selected approach is appropriate for a student-built prototype.

### Electrical Architecture

Determine:

* sensor interface
* ADC requirements
* signal conditioning
* power requirements
* MCU interfaces
* output / alert mechanisms

### Mechanical Integration

Determine:

* sensor mounting
* attachment method
* enclosure requirements
* vibration coupling
* repeatability of sensor placement

### Prototype Validation

Determine how the system will demonstrate:

* normal vibration
* deliberately introduced abnormal vibration
* classification accuracy
* repeatability
* false-alarm behavior

---

# 5. Innovation Preservation Requirement

The architecture shall preserve VibeGuard's intended differentiator:

> Low-cost embedded edge intelligence applied to machine-vibration monitoring rather than functioning merely as a conventional vibration sensor.

The architecture should also investigate the feasibility of the previously identified **single-node noise-isolation / vibration-discrimination concept**, where applicable.

However, the architecture shall not artificially preserve a technical feature if credible engineering evidence shows that it cannot be demonstrated reliably within the project constraints.

If a simplified implementation is required, clearly document:

* what was preserved,
* what was simplified,
* why it was simplified,
* and what future version could restore the advanced capability.

---

# 6. Project Constraints

All candidate architectures shall be evaluated against:

### Budget

Target project budget:

**₹3000–₹5000 INR**

The architecture should preferably remain comfortably below the upper limit to provide contingency for failed components, fabrication, and replacement parts.

### Team

Five-member student team.

Three members have stronger Computer Science / Cybersecurity / programming backgrounds.

One member is a programming beginner who will learn embedded programming through manageable project tasks.

Two members can contribute substantially to:

* hardware support,
* mechanical work,
* fabrication,
* component sourcing,
* prototype assembly,
* documentation,
* and coordination with relevant engineering departments.

The architecture must not assume the team possesses professional industrial vibration-analysis or mechanical-engineering expertise.

External departmental consultation may be used where available, but the final prototype must remain realistically achievable by the student team.

### Platform

The project remains focused on:

* low-cost embedded hardware,
* standalone operation,
* Arduino IDE-compatible development where practical,
* low-power implementation,
* local / edge processing.

### Connectivity

Cloud processing shall not be required for the minimum demonstrable prototype.

If wireless communication is proposed, it must be treated as an optional supporting feature rather than a dependency for core classification.

---

# 7. Candidate Architecture Investigation

Deep research shall investigate multiple implementation approaches rather than assuming one sensor, MCU, or algorithm from the beginning.

Candidate approaches should be compared across:

* sensor technology,
* sensing quality,
* sampling capability,
* signal conditioning,
* MCU capability,
* computational requirements,
* classification method,
* mechanical integration,
* cost,
* availability,
* complexity,
* reliability,
* student feasibility,
* and innovation potential.

The research must identify both:

1. the most technically capable approach, and
2. the most practical student-prototype approach.

These do not automatically have to be the same.

---

# 8. Hardware Decision Requirements

Phase 3C should move significantly closer to real hardware than Phase 3A or Phase 3B.

Research shall investigate concrete candidate hardware where evidence permits, including:

* vibration sensors / accelerometers,
* MCU boards,
* signal-conditioning components,
* power components,
* mounting solutions,
* required passive components,
* optional display / indicators,
* required fabrication materials.

Exact component selection should be based on engineering suitability rather than popularity.

Do not recommend hardware merely because it is inexpensive.

---

# 9. Edge-Intelligence Decision Requirements

The research shall determine what level of intelligence is realistically necessary.

Compare approaches such as:

* simple signal thresholds,
* RMS / peak / variance,
* frequency-domain analysis,
* FFT-based features,
* lightweight ML,
* anomaly detection,
* classification models suitable for embedded execution.

The selected approach must be justified according to:

* computational cost,
* memory,
* training requirements,
* explainability,
* robustness,
* data requirements,
* false-alarm behavior,
* and student implementation difficulty.

The project must not use machine learning merely for appearance.

---

# 10. Experimental Scenario Definition

The architecture must support a controlled demonstration.

The research shall define a practical test scenario in which:

### Normal Condition

The machine or mechanical system operates in its intended normal state.

### Abnormal Condition

A deliberately introduced and repeatable abnormal vibration condition is created.

The abnormal condition must be:

* safe,
* reproducible,
* measurable,
* distinguishable from normal vibration,
* and appropriate for a student laboratory environment.

The final architecture should not depend on an actual industrial machine failure for demonstration.

---

# 11. Noise and False-Alarm Consideration

Because VibeGuard's value is not simply measuring vibration magnitude, Phase 3C shall investigate environmental interference.

Consider:

* neighboring machines,
* structural vibration,
* sensor mounting variation,
* human interaction,
* transient shocks,
* startup / shutdown events,
* changing machine load,
* and other non-fault disturbances.

The architecture should determine how these conditions can be distinguished from genuine abnormal vibration.

Any proposed noise-isolation strategy must be supported by engineering evidence.

---

# 12. Research Evidence Rules

Deep research must distinguish:

* established engineering practice,
* published research,
* commercially demonstrated approaches,
* experimental approaches,
* theoretical proposals,
* and unsupported claims.

Do not assume that an approach is practical simply because it appears in a paper.

Where research evidence conflicts:

* identify the disagreement,
* identify the assumptions,
* compare the evidence,
* and preserve the uncertainty for Phase 3C synthesis.

---

# 13. Required Phase 3C Outputs

The research package must provide enough information for final architecture synthesis.

Required outputs include:

### A. Architecture Candidates

At least several viable architecture options.

### B. Hardware Comparison

Concrete candidate:

* sensors,
* MCU,
* supporting electronics,
* mounting / mechanical approach.

### C. Processing Comparison

Compare signal-processing and edge-intelligence approaches.

### D. Cost Feasibility

Estimate the prototype-level cost of each serious candidate architecture.

### E. Manufacturing / Assembly Feasibility

Determine whether the architecture can realistically be assembled using:

* off-the-shelf components,
* basic fabrication,
* 3D printing,
* simple mechanical mounting,
* or available college facilities.

### F. Team Feasibility

Assess whether the five-member team can build the system within the semester.

### G. Innovation Potential

Identify which subsystem or combination of subsystems could contain genuine technical innovation.

Do not claim patentability at this stage.

### H. Prototype Validation Plan

Define how the minimum demonstrable success can be experimentally demonstrated.

---

# 14. Required Decision Questions

Phase 3C must ultimately answer:

1. Which vibration-sensing principle is best for the prototype?
2. Which specific sensor class or candidate component is most appropriate?
3. Which MCU / embedded platform is appropriate?
4. What sampling rate and signal-processing capability are actually required?
5. What edge-processing method should be used?
6. What classification strategy is practical?
7. How should the sensor be mounted?
8. How can environmental vibration and false alarms be reduced?
9. What is the simplest architecture capable of demonstrating the engineering hypothesis?
10. What architecture provides the best balance between feasibility and innovation?
11. What hardware can realistically be obtained within ₹3000–₹5000?
12. What skills must the five-member team acquire?
13. What can the beginner programmer safely contribute?
14. Which tasks should be delegated to the mechanically oriented members?
15. What are the major engineering failure points?
16. What uncertainties must be tested through prototyping rather than further research?
17. Is the architecture ready for detailed engineering, or is additional investigation required?

---

# 15. Architecture Selection Criteria

Candidate architectures shall ultimately be evaluated using:

| Criterion                               | Priority |
| --------------------------------------- | -------- |
| Minimum demonstrable success            | Critical |
| Reliable normal/abnormal classification | Critical |
| Edge processing                         | Critical |
| Budget                                  | Critical |
| Student buildability                    | Critical |
| Sensor quality                          | High     |
| False-alarm resistance                  | High     |
| Mechanical simplicity                   | High     |
| Availability                            | High     |
| Power consumption                       | Medium   |
| Scalability                             | Medium   |
| Patent / innovation potential           | Medium   |
| Commercial sophistication               | Low      |

Patent potential must not override a serious engineering feasibility problem.

Likewise, low cost must not justify an architecture that cannot reliably demonstrate the engineering hypothesis.

---

# 16. Phase 3C Decision Gate

At the end of Phase 3C, the concept shall be classified as one of:

### READY

A sufficiently supported architecture exists and can proceed toward implementation planning.

### READY WITH MINOR REFINEMENTS

The architecture is fundamentally sound but requires limited engineering refinement.

### REQUIRES ADDITIONAL INVESTIGATION

Important engineering uncertainty remains that prevents responsible architecture selection.

### NOT RECOMMENDED

The engineering hypothesis cannot reasonably be demonstrated within the project's constraints.

---

# 17. Required Phase 3C Deliverables

The completed phase should produce:

1. `Phase3C_VibeGuard_SOP.md`
2. `Phase3C_VibeGuard_Deep_Research_Prompt_Final.md`
3. Independent Deep Research reports
4. `Phase3C_VibeGuard_Claude_Synthesis_Prompt.md`
5. `Phase3C_VibeGuard_Architecture_Report.pdf`
6. `Phase3C_VibeGuard_Memory_Final.md`
7. Engineering Architecture Review
8. Final Phase 3C decision

---

# 18. Phase Boundary

Phase 3C shall NOT:

* build the final prototype,
* finalize a complete PCB,
* produce production-ready CAD,
* write the complete firmware,
* conduct full-scale machine-failure prediction,
* claim industrial-grade predictive-maintenance capability,
* claim patentability,
* or declare freedom-to-operate.

Those activities belong to later phases.

Phase 3C defines the architecture required to make those activities possible.

---

# 19. Final Principle

VibeGuard Phase 3C shall optimize for:

> **A low-cost, student-buildable edge-intelligent vibration-monitoring architecture that can reliably demonstrate normal-versus-abnormal machine vibration classification, while preserving a credible path toward more advanced predictive maintenance and future innovation.**

The objective is not to build the most sophisticated industrial monitoring system.

The objective is to establish the **simplest technically defensible architecture that proves the core hypothesis and gives the team a strong foundation for later innovation.**

---

# END OF SOP
<!-- END CANONICAL DOCUMENT 06:
06_Phase3C_VibeGuard_SOP_Final.md -->
