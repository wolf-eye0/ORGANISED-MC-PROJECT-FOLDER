# Chapter 06 — VibeGuard Frozen Architecture and Semester Scope

## Controlled VibeGuard source packet

This packet contains hash-verified source extracts. Sources have not been reconciled or converted into final manual conclusions.

Mapped sources: **7**


---

## Source 1: `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `ba7d1824fe1ab260be903aead8d9bac00cee83141b6f7728d0e220b65fd8eeb4`

# Source Extraction

- Chapter: `06` — VibeGuard Frozen Architecture and Semester Scope
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Architecture_Report_Final.md`
- Current SHA-256: `ba7d1824fe1ab260be903aead8d9bac00cee83141b6f7728d0e220b65fd8eeb4`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

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


---

## Source 2: `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `e4b96f7ee53bbc94ec960db281a1a56745fc6c8121133b813ca37b76798da5e5`

# Source Extraction

- Chapter: `06` — VibeGuard Frozen Architecture and Semester Scope
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_Memory_Final.md`
- Current SHA-256: `e4b96f7ee53bbc94ec960db281a1a56745fc6c8121133b813ca37b76798da5e5`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

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


---

## Source 3: `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md`

- Authority: `TIER_1`
- Treatment: `CORE_NARRATIVE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `6386bf6d73bbbbb7127c568692ba09abcbdf6dc4cbac40a97690b4edb0dca974`

# Source Extraction

- Chapter: `06` — VibeGuard Frozen Architecture and Semester Scope
- Authority tier: `TIER_1`
- Manual treatment: `CORE_NARRATIVE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/01_Final_Architecture/Phase3C_VibeGuard_SOP_Final.md`
- Current SHA-256: `6386bf6d73bbbbb7127c568692ba09abcbdf6dc4cbac40a97690b4edb0dca974`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

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


---

## Source 4: `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_VibeGuard_Concept_Dossier.docx`

- Authority: `TIER_2`
- Treatment: `CORE_OR_SUPPORTING`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `8a3c40cdc9ec899934ca9a37b05f9c0df22b583cd3ee259ebc81c1da9f0a0ae7`

# Source Extraction

- Chapter: `06` — VibeGuard Frozen Architecture and Semester Scope
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_SUPPORTING`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_VibeGuard_Concept_Dossier.docx`
- Current SHA-256: `8a3c40cdc9ec899934ca9a37b05f9c0df22b583cd3ee259ebc81c1da9f0a0ae7`
- Extraction method: `DOCX_XML`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Document 2 – VibeGuard Concept Dossier

Intelligent Bearing Fault Early-Warning System for Predictive Maintenance

Executive Summary

This concept proposes an intelligent predictive maintenance system that continuously monitors vibration behaviour in rotating machinery to identify early indications of bearing degradation before catastrophic failure occurs. Rather than relying only on scheduled maintenance, the system aims to provide continuous condition awareness, enabling timely maintenance decisions, reducing downtime, and improving equipment reliability.

Background and Motivation

Industrial facilities rely heavily on motors, pumps, fans, compressors and rotating machinery. Bearing failures are among the leading causes of unexpected equipment breakdown. Traditional maintenance strategies are often either reactive, where repairs occur only after failure, or preventive, where components are replaced on fixed schedules regardless of their actual condition. Both approaches increase operational costs. During Phase 1A, predictive maintenance consistently appeared as a high-value opportunity because it combines clear industrial demand, strong embedded systems relevance, affordability, and measurable real-world impact.

Problem Statement

Unexpected bearing failures interrupt production, increase maintenance expenses, reduce equipment lifetime, and may create safety hazards. Smaller industries often cannot afford sophisticated commercial monitoring systems, creating a demand for affordable intelligent monitoring solutions capable of detecting degradation at an early stage.

Current Solutions and Limitations

Commercial predictive maintenance platforms often require expensive industrial sensors, proprietary software, cloud subscriptions, or complex installation. Simpler monitoring approaches typically provide threshold-based alarms that cannot distinguish normal operational changes from developing faults. These limitations create an opportunity for a cost-effective embedded monitoring solution that focuses on early warning rather than full industrial diagnostics.

Why Embedded Systems

Continuous monitoring requires real-time sensor acquisition, deterministic processing, low power consumption, and reliable operation close to the machine. Embedded systems enable local analysis, fast response, and operation without permanent cloud connectivity, making them well suited for industrial environments.

Proposed Concept

We propose an embedded monitoring platform that continuously observes vibration behaviour and analyses changing machine conditions to identify patterns associated with early bearing degradation. The concept focuses on affordable deployment, edge-based decision making, and practical demonstration of predictive maintenance principles within a semester-scale prototype.

Innovation Opportunity

Potential innovation exists in adaptive vibration analysis, lightweight edge intelligence, efficient anomaly detection, cost-optimised monitoring architectures, and simplified deployment strategies for small and medium industries. These areas provide opportunities for future patent and research exploration after prior-art analysis.

Applications

Potential applications include manufacturing plants, workshops, educational laboratories, water treatment facilities, HVAC systems, agricultural processing units, and any environment that depends on rotating machinery.

Commercial Potential

Affordable predictive maintenance has significant commercial relevance because reducing even a single unexpected equipment failure can offset the cost of deployment. The concept has potential value for SMEs that require practical monitoring without enterprise-level infrastructure.

Selection Rationale

Throughout Phases 1A, 1B, 1B.5 and 1C, this opportunity consistently ranked highly because it demonstrates a clear embedded systems advantage, strong demonstration value, realistic semester feasibility, and meaningful commercial potential while remaining achievable within the intended budget.

Risks

Challenges include collecting representative vibration data, distinguishing genuine faults from environmental noise, validating results with limited equipment, and carefully controlling project scope so the prototype remains achievable.

Future Scope

Future development could include multi-machine monitoring, advanced edge AI, cloud dashboards, integration with industrial communication protocols, fleet-level predictive analytics, and validation across multiple machine types.


---

## Source 5: `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf`

- Authority: `TIER_2`
- Treatment: `CORE_OR_SUPPORTING`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `8702d859cdcf816afb2ac31673759a0382348fb69b8e6a4c65120b7c7fe0deff`

# Source Extraction

- Chapter: `06` — VibeGuard Frozen Architecture and Semester Scope
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_SUPPORTING`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/05_Roadmaps_and_Reference_Dossiers/VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf`
- Current SHA-256: `8702d859cdcf816afb2ac31673759a0382348fb69b8e6a4c65120b7c7fe0deff`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                                                      PROJECT mC

                     VIBEGUARD
              SEMESTER IMPLEMENTATION
            AND FUTURE RESEARCH ROADMAP
       Frozen Level-1 Build Plan, Validation Programme and Post-Semester PIRG
                                     Research Path

                           Course                                          PBCST504 - Microcontrollers Micro Project

                                                                 B.Tech Computer Science and Engineering (Cyber
Programme
                                                                 Security)

Group                                                            Group 8

Project Coordinator                                              Ms. Sagna L T, Assistant Professor, CSE (CY)

Prepared for                                                     Semester implementation approval and execution

Date                                                             03 August 2026

Document status                                                  Teacher-facing implementation dossier; controlled draft


  Controlling decision
  This dossier implements only the frozen VibeGuard Level-1 semester architecture: one rigidly mounted
  ADXL345-class accelerometer, one ESP32, local normal-versus-induced-abnormal classification, RGB indication
  and USB evidence. PIRG remains a separate, unbuilt post-semester research hypothesis.


  Patent boundary
  The ordinary semester build is conventional and is not represented as a patent-ready invention. Any future
  filing decision requires new physical evidence, refreshed prior-art work, institutional IPR review and
  professional advice.


 Prepared from the controlled Project mC authority set and the Master Evidence, Costing and Decision Basis. This document is an
             engineering implementation plan, not legal advice, a patent opinion or freedom-to-operate clearance.


   Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                         Page 1
                             Dept. of CSE (CY)          PBCST504 - Microcontrollers         Page 1

                                Topic: VibeGuard - Semester Implementation and Future Research Roadmap


Document control and approval use
                            Control item                                                        Value

                                                                    Frozen VibeGuard Level-1, single-node ADXL345-class
Architecture baseline
                                                                    sensor + ESP32

Expected semester budget                                            Approximately ₹2,200

Protected conservative envelope                                     Approximately ₹3,900; below the ₹5,000 ceiling

                                                                    Reach minimum demonstrable system by Week 8; Weeks 9-
Core implementation window
                                                                    12 reserved for validation, recovery and presentation

                                                                    PIRG only after semester foundation; separate folder,
Future research
                                                                    budget, evidence and confidentiality

                                                                    This dossier becomes the controlling build plan after teacher
Primary project record
                                                                    approval


Approval checkpoints required before procurement freeze
 1. Teacher approval of the change from OpenBraille to VibeGuard and the exact Level-1 semester scope.
 2. Confirmation whether the effective build window is approximately eight weeks or the full twelve-week plan.
 3. Approval of the selected ESP32 board variant and procurement source.
 4. Faculty/laboratory safety review of the powered motor, shaft guard and retained eccentric-mass fixture.
 5. Approval of a quantitative Level-1 held-out validation protocol before the locked test.


Executive implementation decision
   Recommended semester build
   Build VibeGuard as a low-cost, single-node embedded vibration-monitoring prototype that distinguishes a
   controlled normal rig state from a repeatable induced-abnormal state. Use RMS plus persistence as the
   minimum classifier; add triggered FFT/bands and ordinary Mahalanobis only as comparisons after the baseline
   works.


VibeGuard is selected because its main risks - sensor authenticity, rigid coupling, stable acquisition, repeatable fault
injection, threshold selection and data leakage - can be isolated through scripted experiments and logs. Its expected
budget leaves more recovery headroom than OpenBraille, and the team’s strongest capabilities align with ESP32
firmware, signal processing, USB evidence and quantitative validation.
The project should not be described as a complete industrial predictive-maintenance product. The correct semester
claim is a controlled proof that a low-cost embedded node can acquire vibration, establish a normal condition, detect
a deliberately introduced abnormal condition and report the result locally without cloud processing.

Success definition at a glance
                    Layer                             Required semester result                           Evidence

                                                                                         Acceptance checklist, axis verification,
                                               Stable ESP32 + ADXL345 SPI acquisition
Hardware                                                                                 ODR record, dropped-block and saturation
                                               on a rigid target mount
                                                                                         counters

                                                                                         Rig configuration IDs, photos, RPM/load
                                               Safe, repeatable normal and induced-
Rig                                                                                      notes, retained eccentric mass and guard
                                               abnormal operating states
                                                                                         inspection

                                                                                         Frozen calibration, state logs,
                                               RMS threshold with persistence works
Minimum decision                                                                         classification latency and held-out
                                               locally
                                                                                         confusion matrix

                                               FFT/bands and ordinary Mahalanobis are    Feature plots/tables, resource use and
Secondary analysis
                                               compared without delaying the baseline    comparator results

      Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                          Page 2
                                Dept. of CSE (CY)          PBCST504 - Microcontrollers         Page 2

                             Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                   Layer                            Required semester result                            Evidence

                                                                                        Live demonstration and exportable
Output                                      Clear RGB state and USB evidence
                                                                                        CSV/log file

                                                                                        Negative-results log, remount records and
Honesty                                     Limitations and failed runs are preserved
                                                                                        scope statement


1. Purpose, audience and scope
1.1 Purpose
This document converts the approved Phase 3C VibeGuard architecture into a procurement-ready and execution-
ready semester plan. It defines the exact hardware, interfaces, mechanical test rig, firmware modules, validation
controls, team responsibilities, budget, schedule, risks, outputs and future-research boundary.

1.2 Audience
 • Project coordinator and teacher: approval, scope control, safety and review gates.
 • Five-member student team: subsystem ownership, integration sequence and evidence requirements.
 • Department laboratories: equipment booking, safety assistance and optional measurement support.
 • Institutional innovation/IPR reviewers: separation of the public semester prototype from confidential future
   research.

1.3 Scope hierarchy
                Scope tier                                  Included                                  Not included

                                            One target-mounted sensor; normal           Mixed-source attribution, field
Semester Level 1                            versus induced abnormal; local              deployment, cloud platform, RUL or
                                            processing; RGB and USB evidence            patent claim

                                            PIRG target/interferer research after a
Post-semester Level 2                                                                   Assumed success or automatic filing
                                            stable Level-1 platform exists

                                            Only after later validation and
Commercial/industrial                                                                   Any promise in the current project
                                            professional review


2. Engineering identity and problem definition
2.1 Engineering identity
VibeGuard is a passive edge condition-monitoring system. Its defining feature is not the accelerometer itself, but the
local interpretation of vibration on constrained embedded hardware. It targets educational and small-enterprise
contexts where expensive industrial monitoring infrastructure may be unavailable.

2.2 Semester engineering hypothesis

   Hypothesis to test
   A low-cost target-mounted accelerometer and ESP32 can consistently distinguish a controlled normal operating
   condition from a deliberately introduced abnormal-vibration condition using lightweight local analysis,
   without cloud processing.


2.3 What the hypothesis does not claim
 • It does not identify a real bearing defect or predict remaining useful life.
 • It does not prove that one sensor can attribute vibration to the correct machine in a dense factory.
 • It does not establish universal thresholds across motors, mounts or environments.
 • It does not claim that FFT, Mahalanobis distance or edge execution is novel.

    Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                         Page 3
                             Dept. of CSE (CY)           PBCST504 - Microcontrollers         Page 3

                             Topic: VibeGuard - Semester Implementation and Future Research Roadmap


3. Frozen system architecture


                           Figure 1. Frozen Level-1 architecture and explicit semester scope boundary.

3.1 Subsystem boundaries
           Subsystem                              Inputs                          Outputs                       Owner acceptance

                                12 V power, normal/abnormal          Repeatable vibration transmitted    Guarded, stable, labelled and
Mechanical target rig
                                fixture state                        to target housing/base              reproducible

                                Mechanical vibration, 3.3 V                                              Correct axes, no saturation,
Sensor/mount                                                         Timestamped X/Y/Z samples
                                power, SPI clock/control                                                 documented mount ID

                                SPI samples and interrupt/FIFO                                           Stable ODR, zero block loss in
Embedded acquisition                                                 Raw windows, integrity counters
                                state                                                                    locked run

                                                                     Time features, triggered            Versioned, deterministic and
Feature pipeline                Raw windows
                                                                     spectra/bands                       reproducible

                                Calibrated baseline and current      Calibrating/Normal/Abnormal         Frozen thresholds and
Decision/state
                                features                             state                               persistence

                                                                                                         Teacher-readable demonstration
Human/evidence interface        State and records                    RGB indication, USB CSV/logs
                                                                                                         and audit trail


    Dept. of CSE (CY)                                  PBCST504 - Microcontrollers                                               Page 4
                              Dept. of CSE (CY)             PBCST504 - Microcontrollers             Page 4

                                Topic: VibeGuard - Semester Implementation and Future Research Roadmap


4. Detailed hardware architecture and BOM
4.1 Required purchased and fabricated items
        Item                    Qty            Exact semester role             Expected          Conservative       Acceptance/
                                                                                                                 procurement rule

                                                                                                                Verified WROOM-32
                                               Main controller: SPI                                             DevKit baseline;
ESP32 development                              acquisition, local                                               ESP32-S3 is
                        1                                               ₹400               ₹899
board                                          processing, RGB and                                              authorized fallback.
                                               USB                                                              Confirm pinout, USB-
                                                                                                                UART and regulator.

                                                                                                                Buy from a reputable
                                                                                                                source; verify board
                                               Rigidly mounted tri-
ADXL345 breakout        1                                               ₹229               ₹350                 layout, axes, ODR,
                                               axis vibration sensor
                                                                                                                noise and saturation
                                                                                                                before integration.

                                                                                                                Choose a stable
                                                                                                                mounting face and
12 V geared motor or                           Controlled target test
                        1                                               ₹215               ₹300                 guarded shaft. RPM is
suitable fan                                   article
                                                                                                                metadata, not the
                                                                                                                differentiator.

                                                                                                                Confirm polarity,
12 V, 1 A regulated                            Separate motor-rig
                        1                                               ₹140               ₹330                 connector and
adapter                                        supply
                                                                                                                current margin.

                                               Green Normal, Blue                                               Three separate LEDs
Common-cathode
                        1 set                  Calibrating, Red         ₹25                ₹65                  are acceptable if
RGB LED + resistors
                                               Abnormal                                                         clearer.

                                                                                                                Breadboard only for
                                               Stable final                                                     bring-up; final SPI
Perfboard               1                      sensor/controller        ₹58                ₹85                  wiring should be
                                               interface                                                        short and strain-
                                                                                                                relieved.

                                               SPI, low-voltage                                                 Separate motor-
Wires, headers and
                        1 lot                  power and USB-           ₹180               ₹250                 current paths from
connectors
                                               support connections                                              sensor/logic paths.

                                                                                                                Local allowance;
                                               Repeatable
Heavy base and rigid                                                                                            preserve
                        1 set                  mechanical coupling      ₹300               ₹500
sensor mount                                                                                                    CAD/measurements,
                                               and safe support
                                                                                                                photos and mount ID.

                                                                                                                Mass must be
                                               Safe, repeatable                                                 mechanically
Eccentric mass,
                        1 set                  induced abnormal         ₹200               ₹350                 retained and
guard and fasteners
                                               condition                                                        operated behind a
                                                                                                                guard.

                                               Decoupling, switch,
Passives and                                                                                                    Finalize ratings after
                        1 lot                  DC jack,                 ₹150               ₹280
protection                                                                                                      motor procurement.
                                               fuse/protection

                                               Logistics and one
Delivery/replacement                                                                                            Not a hidden feature
                     1                         controlled rework        ₹300               ₹500
allowance                                                                                                       budget.
                                               margin


  Budget decision
  Expected semester planning total: approximately ₹2,200. Protected conservative envelope: approximately
  ₹3,900. The future PIRG rig, second motor, temporary reference instruments, patent search and professional
  fees are not included.


    Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                          Page 5
                                Dept. of CSE (CY)            PBCST504 - Microcontrollers          Page 5

                                 Topic: VibeGuard - Semester Implementation and Future Research Roadmap


4.2 Reusable or institutional equipment
               Equipment                                           Use                                    Required status

                                                Firmware, serial logs, data analysis and
Laptop with Arduino IDE and Python                                                          Assumed available
                                                reports

Soldering station and hand tools                Final perfboard and connectors              Book before Week 3

                                                Supply, continuity and basic current
Digital multimeter                                                                          Required
                                                checks

                                                SPI timing, rail noise and dropped-sample
Oscilloscope or logic analyzer                                                              Strongly useful; borrowed
                                                debugging

Bench supply with current limit                 Safe motor and controller bring-up          Strongly recommended

Tachometer/RPM reference                        Rig metadata and repeatability              Useful but optional

Calipers and fabrication tools                  Bracket, guard and base measurements        Required for mount repeatability

                                                Mount/remount evidence and demo
Camera                                                                                      Required evidence tool
                                                recording


5. Mechanical test rig and safety


            Figure 2. Proposed controlled rig. The final dimensions and motor variant remain procurement-dependent.

5.1 Rig design rules
1. Mount the motor/fan to a heavy base using bolts or a rigid bracket. Do not rely on hand pressure, foam tape or a
   loose table surface.
2. Mount the ADXL345 rigidly to the target housing or a documented target bracket. Magnetic, foam or soft adhesive
   mounts are prohibited for the final evidence run.
3. Create the abnormal state with a small, retained eccentric mass or another repeatable safe method. Record mass,
   radius, position, speed/load and configuration ID.
4. Install a physical shaft guard and an emergency power disconnect before abnormal operation.
5. Run first at low voltage/speed or under current-limited supply. Inspect fasteners and the eccentric fixture before
   every session.
6. Keep the ESP32 and sensor wiring outside the rotating hazard area and strain-relieve the short SPI connection.

5.2 Safety stop conditions
 • Visible movement of the motor base or guard.
 • Loosening, cracking or movement of the eccentric mass or shaft fixture.
   Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                          Page 6
                                 Dept. of CSE (CY)           PBCST504 - Microcontrollers         Page 6

                           Topic: VibeGuard - Semester Implementation and Future Research Roadmap


 • Abnormal heating, smell, sparking, adapter instability or repeated resets.
 • Sensor/bracket detachment or wiring entering the rotating zone.
 • A faculty/lab reviewer requests suspension or redesign.


6. Electrical integration and provisional pin map
6.1 Power domains
             Domain                         Source                           Loads                              Rule

                                                                                                  Low-voltage only; local
                              ESP32 USB input and 3.3 V                                           decoupling at sensor; do not
Logic/sensor                                                   ESP32, ADXL345, RGB LED
                              regulator                                                           power the motor from USB or
                                                                                                  ESP32 regulator

                                                                                                  Keep motor-current wiring
                                                                                                  separate. A common ground is
                              Separate 12 V adapter with
Motor rig                                                      Motor/fan only                     not required unless a later
                              switch/protection
                                                                                                  controlled interface explicitly
                                                                                                  needs it.

                                                                                                  Data/control only; do not use
Laptop/USB                    Laptop USB                       ESP32 programming and logs
                                                                                                  as the motor power path


6.2 Provisional ESP32-WROOM-32 DevKit pin assignment

  Implementation note
  This is a Phase 4 wiring proposal, not a source-file mandate. Revalidate every pin against the exact purchased
  board. ESP32-S3 uses a different approved pin map.


               Signal                 ADXL345 / output               Provisional ESP32 pin                      Notes

                                                                                                  Use local 0.1 µF decoupling at the
3.3 V                         VCC                              3V3
                                                                                                  breakout

                                                                                                  Short return path; avoid motor-
Ground                        GND                              GND
                                                                                                  current routing

                                                                                                  Start at a conservative clock;
SPI clock                     SCL/SCLK                         GPIO 18                            increase only after integrity
                                                                                                  testing

SPI MOSI                      SDA/SDI                          GPIO 23                            ESP32 to sensor

SPI MISO                      SDO                              GPIO 19                            Sensor to ESP32

SPI chip select               CS                               GPIO 5                             Dedicated output

                                                                                                  Optional but recommended for
Data-ready interrupt          INT1                             GPIO 4
                                                                                                  stable timing

                                                                                                  Common-cathode LED or
RGB green                     LED + resistor                   GPIO 25
                                                                                                  separate indicator

RGB blue                      LED + resistor                   GPIO 26                            Calibrating

RGB red                       LED + resistor                   GPIO 27                            Abnormal/fault indication

                                                                                                  Logging, commands and
USB serial                    On-board USB-UART                Laptop USB
                                                                                                  firmware upload


6.3 Wiring acceptance checklist
 • Board powers without motor connected; 3.3 V rail measured and stable.
 • ADXL345 device ID and axis response verified before high-rate acquisition.
 • SPI wiring kept short; final evidence build soldered or locked in a rigid connector.
    Dept. of CSE (CY)                            PBCST504 - Microcontrollers                                             Page 7
                            Dept. of CSE (CY)         PBCST504 - Microcontrollers            Page 7

                                 Topic: VibeGuard - Semester Implementation and Future Research Roadmap


 • No sensor saturation during normal or induced-abnormal pilot runs.
 • USB logs remain stable while the motor is switched and while the abnormal state is active.


7. Firmware and software architecture


                         Figure 3. Staged pipeline. The minimum RMS/persistence path controls schedule risk.

7.1 Firmware module breakdown
                     Module                                     Responsibility                             Required outputs/tests

                                                 Board variant, pin map, ODR, range, window     Human-readable configuration block printed
Configuration manager
                                                 size, threshold version and build ID           at startup and stored with logs

                                                 Initialization, device ID, range/ODR,          Axis test, known orientation check and read-
ADXL345 driver
                                                 burst/FIFO reads and interrupt status          error counter

                                                 Timestamp samples/windows and maintain         Measured achieved sample rate; zero locked-
Acquisition engine
                                                 loss/overrun counters                          run block loss

                                                 Mean/DC removal; optional Hann window          Deterministic output verified against offline
Preprocessor
                                                 for FFT; scaling and validation                script

                                                 RMS, peak, standard deviation, crest factor
Time-feature engine                                                                             Unit tests on stored windows
                                                 and optional kurtosis

                                                 Normal baseline, threshold and consecutive-    Calibrating/Normal/Abnormal transitions
Persistence classifier
                                                 window logic                                   and threshold log

                                                 Compute spectrum only when scheduled or
Triggered FFT/bands                                                                             Frequency-resolution and latency record
                                                 triggered

                                                 Regularized normal-space score; optional       Offline/embedded agreement and
Mahalanobis comparator
                                                 comparison only                                RAM/timing record

State/output manager                             RGB state and fault behavior                   Visible deterministic indication

                                                 CSV logs, metadata, start/stop/calibrate
USB logger/command interface                                                                    Recoverable files with schema/version
                                                 commands

                                                 Saturation, read errors, timing overruns and
Health monitor                                                                                  No silent acquisition failure
                                                 configuration faults


7.2 Repository and configuration structure
                              Folder/file                                                             Purpose

firmware/                                                                ESP32 source, libraries, board configuration and release tags


    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                                Page 8
                                  Dept. of CSE (CY)            PBCST504 - Microcontrollers            Page 8

                                  Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                               Folder/file                                                               Purpose

                                                                          Wiring record, BOM, datasheets, board photos and mount
hardware/
                                                                          CAD/dimensions

rig/                                                                      Motor, base, guard and abnormality configuration IDs

data/raw/                                                                 Immutable raw or minimally transformed session files

data/processed/                                                           Versioned feature exports generated by scripts

analysis/                                                                 Python notebooks/scripts, metrics and plots

tests/                                                                    Unit tests, acceptance checklists and locked-run protocol

docs/                                                                     Teacher reports, weekly reviews, risk and decision logs

                                                                          Access-restricted future-research material; not used in semester
future_pirg_private/
                                                                          grading


8. Signal-processing and decision logic
8.1 Acquisition parameters to resolve in pilot testing
                   Parameter                                    Starting proposal                                  Decision rule

                                                                                                   Increase only if saturation is observed;
Range                                             Start at ±4 g full-resolution mode
                                                                                                   record every change

                                                  Start at 800 Hz; evaluate 1,600 Hz if spectral   Use the lowest rate that captures
Output data rate
                                                  evidence requires it                             discriminating energy with stable SPI timing

                                                                                                   Freeze before locked validation; overlap
Window                                            256 samples at 800 Hz or equivalent duration
                                                                                                   must be reported

                                                                                                   Triggered/periodic comparison; not always-
FFT                                               256 or 512 points with Hann window
                                                                                                   on if it threatens acquisition

                                                  Multiple complete normal sessions, not one       Separate calibration/training sessions from
Normal calibration
                                                  short run                                        held-out sessions

                                                  Derived from normal distribution with
Threshold                                                                                          Do not change after viewing held-out results
                                                  owner-approved rule

                                                  Require abnormal evidence for consecutive        Select on calibration data; report
Persistence
                                                  windows/time                                     classification latency

                                                  Select from pilot evidence and physical
Bands/features                                                                                     Freeze the list before held-out testing
                                                  plausibility


8.2 Minimum classifier
The minimum classifier is a calibrated RMS threshold with persistence. The firmware calculates the vibration
magnitude or a predeclared axis combination, estimates a normal baseline from approved calibration sessions, and
raises the Abnormal state only when the threshold is exceeded for the approved persistence period. A single transient
shock should not automatically become a persistent machine fault.

8.3 Triggered FFT and band features
FFT analysis is used to explain and compare the state change, identify repeatable spectral components and support
later research. It is triggered when the low-cost stage crosses a pre-trigger or at scheduled diagnostic intervals. The
report must disclose sample rate, window length, frequency resolution, overlap and selected bands.

8.4 Ordinary Mahalanobis comparator
Mahalanobis distance may be implemented as an optional normal-space comparator over a small feature vector. It
must use regularized covariance and must be benchmarked against the simpler RMS/persistence baseline. The
semester project succeeds without it if the minimum classifier and evidence programme are complete.


       Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                                    Page 9
                                   Dept. of CSE (CY)            PBCST504 - Microcontrollers              Page 9

                            Topic: VibeGuard - Semester Implementation and Future Research Roadmap


8.5 State-machine behavior
             State                       Entry condition                      Output                        Exit/exception

                                Power-on, configuration and                                        Fault if sensor or configuration
STARTUP/SELF-CHECK                                               Blue pulse / USB status
                                sensor identity checks                                             is invalid

                                                                                                   Restart if saturation,
                                Approved normal session and
CALIBRATING                                                      Blue                              movement or timing fault
                                stable acquisition
                                                                                                   occurs

                                Features inside calibrated                                         Abnormal evidence enters
NORMAL                                                           Green
                                bounds                                                             persistence counter

                                Threshold/persistence rule                                         Return only after approved
ABNORMAL                                                         Red
                                satisfied                                                          recovery/hysteresis rule

                                Sensor read error, saturation,
                                                                 Logged fault; distinct visible    Requires operator action or
FAULT/INVALID                   timing loss or mount-invalid
                                                                 pattern if implemented            controlled restart
                                condition


9. Data and evidence management
9.1 Required session metadata
 • Project, firmware and configuration version.
 • Sensor board identity, axis orientation, range, ODR and SPI clock.
 • Mount ID, photographs, fasteners/adhesive method and whether the sensor was remounted.
 • Motor/fan identity, supply voltage, speed/load proxy and abnormality-fixture configuration.
 • Session date/time, operator, target state and any transient events.
 • Sample count, lost blocks, read errors, saturation count and timing statistics.
 • Threshold/feature version and whether the session was calibration, development or locked hold-out.

9.2 Data split rule

  Leakage prevention
  Never randomly split windows from the same continuous run into training and test sets. Hold out complete
  sessions, days and remounts so the result tests repeatability rather than memorizing one recording.


9.3 Evidence package for final review
                       Evidence file                                                       Minimum content

                                                                 Exact board, sensor, pin map, sample rate, range, window,
Configuration record
                                                                 feature and threshold version

BOM and procurement record                                       Seller, date, unit cost, delivery and acceptance result

                                                                 Annotated photos, dimensions, safety inspection and state
Rig record
                                                                 definitions

Session register                                                 Every run, including failures and exclusions with reasons

Raw/processed data                                               Immutable original files and reproducible processing scripts

                                                                 Confusion matrix, false alerts, missed detections, latency,
Validation report
                                                                 resource use and limitations

                                                                 Power-up, calibration, normal run, abnormal run, RGB/USB
Demo checklist
                                                                 evidence and shutdown

                                                                 Dated member responsibilities, code commits, hardware
Contribution record
                                                                 changes and experiment ownership


   Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                              Page 10
                             Dept. of CSE (CY)         PBCST504 - Microcontrollers            Page 10

                    Topic: VibeGuard - Semester Implementation and Future Research Roadmap


Dept. of CSE (CY)                        PBCST504 - Microcontrollers                         Page 11
                    Dept. of CSE (CY)         PBCST504 - Microcontrollers         Page 11

                                  Topic: VibeGuard - Semester Implementation and Future Research Roadmap


10. Validation and acceptance programme
10.1 Validation stages
              Stage                               Question                      Minimum evidence                       Stop/fallback

                                     Are the purchased ESP32, sensor,    Device ID, axis response, stable   Replace or redesign the failing
V0 - Component acceptance
                                     motor and supply usable?            rails, motor/guard inspection      component before integration

                                                                         Achieved ODR, error/loss
                                     Can the system collect stable                                          Reduce SPI clock/ODR, shorten
V1 - Acquisition integrity                                               counters, no unexplained
                                     timestamped data?                                                      wiring or move to perfboard
                                                                         saturation

                                     Is the controlled normal state      Multiple sessions and remount      Fix rig/mount before classifier
V2 - Normal repeatability
                                     stable across sessions?             record; feature distributions      tuning

                                     Is the induced state safe and       Repeated labelled abnormal         Redesign the fixture; do not tune
V3 - Abnormal repeatability
                                     distinct?                           sessions and physical metadata     around an unstable fault

                                     Does RMS + persistence work         Frozen threshold, latency and      Simplify features or improve rig
V4 - Minimum classifier
                                     locally?                            development results                labels

                                     Do FFT/bands or Mahalanobis         Same held-out protocol; resource   Drop optional method if it adds
V5 - Comparator evaluation
                                     add useful evidence?                comparison                         no value

                                     Does the frozen system
                                                                         Pre-registered metrics; no         Report failure honestly; retain
V6 - Locked held-out run             generalize to untouched
                                                                         threshold changes                  project as measurement study
                                     sessions/remount?

                                     Can another person operate and      Checklist, rehearsal and source-
V7 - Demo and documentation                                                                                 Freeze features and repair only
                                     explain the project?                backed report


10.2 Proposed Level-1 acceptance targets for teacher approval

  Status of numbers
  The project authority did not freeze quantitative Level-1 accuracy thresholds. The following are proposed pre-
  registration targets and become binding only after teacher/owner approval.


                    Metric                                      Proposed target                                 Why it matters

                                                  At least three days with independently
                                                                                                 Prevents a single-run demonstration from
Independent evidence                              started normal and abnormal sessions; at
                                                                                                 being called reliable
                                                  least one complete day/remount held out

Sensitivity to induced abnormal                   ≥90% on the untouched Level-1 test             Limits missed abnormal states

Specificity for normal                            ≥90% on the untouched Level-1 test             Limits false alarms

                                                  No more than one alert during a 10-minute
Stable-normal false alerts                                                                       Makes the live demonstration credible
                                                  locked stable-normal run

Decision latency                                  ≤2 seconds for the minimum classifier          Maintains interpretable local alerting

                                                  100% for Level-1 unless an explicit            Avoids hiding errors through abstention in
Decision coverage
                                                  sensor/invalid fault is logged                 the semester binary task

                                                  Zero lost analysis blocks during the locked
                                                                                                 Ensures apparent accuracy is not built on
Acquisition integrity                             run; saturation and alias/bandwidth limits
                                                                                                 missing data
                                                  reported

                                                  A second operator can execute the demo         Shows project readiness rather than owner-
Reproducibility
                                                  from the checklist                             only operation


10.3 Required performance reporting
 • Confusion matrix and class counts, not only a single accuracy percentage.
 • Sensitivity, specificity, precision where meaningful, false-alert count and missed-detection count.
 • Decision latency and persistence delay.

    Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                              Page 12
                                  Dept. of CSE (CY)            PBCST504 - Microcontrollers            Page 12

                                  Topic: VibeGuard - Semester Implementation and Future Research Roadmap


• ESP32 RAM/flash use, feature/FFT timing and dropped-block counters.
• Normal and abnormal plots from untouched sessions with the same axis/range.
• Failure cases, remount sensitivity and known limits of the ADXL345 frequency band.


11. Twelve-week semester roadmap
         Week                 Primary work                Owner(s)               Measurable output              Exit criterion                Fallback


                                                                                                                                      Use available verified
                                                                               Approved scope; final       No purchase until
                         Approval, scope freeze,   Nihad + team; Amith                                                                ESP32/motor variants
1                                                                              order list; lab/tool        change and rig-safety
                         safety and procurement    hardware audit                                                                     without changing
                                                                               inventory; risk register    direction are approved
                                                                                                                                      architecture

                         ESP32/ADXL345             Sreehari firmware;          Device ID/axis test;                                   Return/replace failed
                                                                                                           Sensor and motor pass
2                        acceptance and motor      Amith hardware;             motor/supply inspection;                               module before
                                                                                                           acceptance
                         inspection                Sreeprada checklist         provisional mount plan                                 integration

                                                                               Timestamped X/Y/Z           Continuous stable          Reduce ODR/SPI clock;
                         Stable SPI acquisition
3                                                  Sreehari + Nihad            stream; achieved ODR;       acquisition and USB        shorten wires; move to
                         vertical slice
                                                                               loss/saturation counters    logging                    perfboard

                                                                               Final mount ID; normal      Feature distributions
                         Rigid mount and           Amith rig; Sreeprada                                                               Rebuild mount/base
4                                                                              sessions on separate        repeatable enough to
                         normal-state sessions     records; Nihad review                                                              before classifier tuning
                                                                               starts                      define baseline

                                                                               Guarded eccentric           Safe, reproducible state   Change
                         Safe induced-abnormal     Amith + faculty safety;
5                                                                              fixture; repeated           separation visible in      mass/radius/speed
                         fixture and sessions      team operators
                                                                               abnormal labels             raw/features               within safe limits

                                                                                                           End-to-end                 Simplify to one
                         RMS + persistence and     Sreehari firmware;          Working local minimum
6                                                                                                          Normal/Abnormal            magnitude feature;
                         RGB/USB state             Nihad integration           classifier and logs
                                                                                                           demonstration              improve calibration

                                                                               FFT timing,                 Baseline remains stable;   Drop comparator if
                         Triggered FFT/bands       Sreehari data; Nihad
7                                                                              spectra/bands; optional     comparator does not        timing/data burden is
                         and comparator            review
                                                                               Mahalanobis prototype       break acquisition          excessive

                         Independent sessions      Nihad protocol;             Locked test plan,           Minimum demonstrable       Use Weeks 9-10 to
8                        and held-out protocol     Sreeprada registry;         thresholds, session split   system complete by end     stabilize baseline; no
                         freeze                    Archa documentation         and demo draft              of week                    future-scope expansion

                                                                               Startup/shutdown,
                                                                                                           Known edge cases           Document limitation if
                         Edge cases and fault                                  shock, loose-mount,
9                                                  Team                                                    produce honest             reliable handling is not
                         handling                                              saturation and sensor-
                                                                                                           state/fault evidence       feasible
                                                                               fault logs

                                                                                                           Approved acceptance
                         Locked Level-1                                        Untouched results,                                     No post-hoc threshold
                                                   Nihad + Sreehari;                                       target met or failure
10                       validation and demo                                   metrics, resource profile                              change; repeat only after
                                                   independent operator                                    documented without
                         freeze                                                and frozen release                                     formal redesign
                                                                                                           patching

                                                                               Final dossier updates,
                                                                                                           Teacher-ready package;     Cut nonessential
                         Documentation and         Archa lead; all technical   wiring/BOM, results,
11                                                                                                         second operator can run    content; retain core
                         rehearsal                 review                      demo script and
                                                                                                           demo                       evidence
                                                                               limitations

                                                                               Stable submitted                                       Repair from spares;
                         Contingency repair and                                                            No new feature;
12                                                 Full team                   prototype and archived                                 present validated subset
                         final delivery                                                                    deliver/rehearse
                                                                               evidence                                               honestly


     Schedule rule
     The minimum demonstrable system should work by the end of Week 8. Weeks 9-12 are for validation, recovery,
     documentation and presentation. PIRG is prohibited from becoming a late semester feature.


     Dept. of CSE (CY)                                      PBCST504 - Microcontrollers                                                          Page 13
                                   Dept. of CSE (CY)              PBCST504 - Microcontrollers                    Page 13

                             Topic: VibeGuard - Semester Implementation and Future Research Roadmap


12. Team roles, actual members and accountability
  Role status
  The following name-to-role map is a proposed implementation assignment based on the established five-
  member team and earlier presentation responsibilities. The team and teacher should sign or amend it before
  Week 1 closes.


           Member                        Proposed primary role           Specific VibeGuard ownership           Review/backup obligation

                                                                         Architecture control, schedule,
                                                                         interfaces, safety coordination,    Backs up firmware and
                                    Technical integration lead /
Nihad P C - JEC24CC044                                                   validation protocol, final          hardware; approves
                                    project manager
                                                                         integration and evidence            configuration freezes
                                                                         integrity

                                                                         ADXL345 driver, SPI acquisition,
                                                                         feature pipeline,
                                    Firmware, signal-processing and                                          Nihad reviews releases;
Sreehari K - JEC24CC055                                                  RMS/persistence,
                                    data lead                                                                Sreeprada executes scripted tests
                                                                         FFT/comparators, USB schema
                                                                         and analysis scripts

                                                                         Procurement audit,
                                                                                                             Nihad reviews interfaces/safety;
                                    Hardware, power and physical-        motor/base/guard, rigid sensor
Amith Krishna Das - JEC24CC016                                                                               Sreehari checks signal-integrity
                                    rig lead                             mount, supply wiring, perfboard
                                                                                                             needs
                                                                         and safety inspections

                                                                         Inventory, configuration labels,
                                                                                                             Works from signed procedures;
                                    Learner, test and inventory          scripted sessions, mount photos,
Sreeprada K S - JEC24CC056                                                                                   learns USB logging and basic
                                    assistant                            operator checklists, run registry
                                                                                                             firmware operation
                                                                         and repeated tests

                                                                         Weekly review notes, teacher-
                                    Documentation, teacher               facing explanations, source
                                                                                                             Technical statements reviewed
Archa Pramod - JEC24CC022           communication and                    register, live-demo script,
                                                                                                             by Nihad, Sreehari and Amith
                                    demonstration lead                   presentation coordination and
                                                                         lead communication


12.1 Responsibility rules
 • Every critical subsystem has one primary owner, one technical reviewer and one written checklist.
 • No one may change hardware wiring, firmware thresholds or test labels without a dated configuration update.
 • The learner/test role is substantive: repeated independent runs, inventory control and evidence integrity are
   project-critical.
 • The documentation lead does not publish future-research details without technical and IPR review.
 • Nihad acts as final integration failsafe, but work must remain distributed so the project does not depend on one
   member.


13. Procurement, acceptance and configuration control
13.1 Procurement sequence
1. Obtain teacher approval and freeze the semester architecture.
2. Order the ESP32, one ADXL345 module, motor/fan and power adapter first.
3. Accept or reject the sensor and motor before ordering duplicate or final fabrication items.
4. Fabricate the base, guard and rigid bracket after physical dimensions are known.
5. Buy a spare sensor or motor only when acceptance/delivery risk justifies it within the conservative envelope.

13.2 Component acceptance record
               Component                                     Acceptance checks                                     Reject if

                                                 Boots reliably, USB serial works, board         Unknown board mapping, repeated
ESP32
                                                 identity/pinout recorded, regulator stable      disconnects, overheating or unstable supply
   Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                               Page 14
                                 Dept. of CSE (CY)            PBCST504 - Microcontrollers             Page 14

                                 Topic: VibeGuard - Semester Implementation and Future Research Roadmap


13.3 Configuration ID format
Recommended format: VG-[rig]-[mount]-[sensor]-[firmware]-[protocol]-[session]. Example: VG-R01-M02-S01-FW0.6-
P03-D2N04. The exact format may change, but every data file and photograph must resolve to one reproducible
physical and software configuration.


14. Risk register and mitigation
            Risk                 Likelihood / impact          Early indicator                Mitigation               Decision consequence

                                                                                     Reputable source, formal
                                                        Wrong device ID, unstable
Counterfeit or poor-quality                                                          acceptance test, preserve      Do not tune algorithms
                              Medium / High             noise, limited ODR or
ADXL345 module                                                                       seller/board photos, replace   around a failed sensor
                                                        clipping
                                                                                     before integration

                                                                                     Retained mass, shaft guard,
Unsafe or unstable                                      Fastener movement, guard     heavy base,                    Stop powered testing until
                              Medium / Critical
abnormality fixture                                     vibration or base walking    low-speed/current-limited      redesigned
                                                                                     bring-up and faculty review

                                                                                     Rigid documented bracket,
                                                        Feature shift after minor                                   Report mount dependence;
Mount-dependent result        High / High                                            mount ID, remount trials
                                                        handling                                                    do not claim generality
                                                                                     and photos

                                                                                     Short wiring, conservative
                                                        Timing overrun, sample                                      No locked result accepted
SPI/acquisition loss          Medium / High                                          clock/ODR, interrupt/FIFO
                                                        gaps, corrupted frames                                      with silent loss
                                                                                     use, perfboard and counters

                                                                                     Adjust range; verify signal
Sensor saturation or                                    Clipped samples or missing   band; limit claims; consider   Do not claim phenomena
                              Medium / High
bandwidth mismatch                                      discriminating frequency     documented future sensor       outside measured band
                                                                                     upgrade

                                                                                     Stabilize base, speed/load
Unrepeatable                                            Overlapping sessions or                                     Redesign rig, not the
                              Medium / High                                          and eccentric fixture before
normal/abnormal labels                                  changing motor behavior                                     classifier
                                                                                     thresholding

                                                                                     Split complete
Data leakage / inflated                                 Random-window split gives    sessions/days/remounts;
                              Medium / High                                                                         Reject leaked metric
accuracy                                                much higher result           freeze thresholds before
                                                                                     hold-out

                                                                                     RMS+persistence first;
                                                        Core demo delayed by                                        Drop comparator, preserve
Late algorithm expansion      High / Medium                                          optional methods after
                                                        ML/feature work                                             minimum system
                                                                                     Week 6

                                                                                     Primary/reviewer/checklist
                                                        One person owns code, rig                                   Reassign before critical
Team bottleneck               Medium / High                                          structure; weekly cross-
                                                        and report knowledge                                        week
                                                                                     training

                                                        PIRG features enter          Separate folders, budgets
Patent expectation distorts                                                                                         Remove future mechanism
                              Medium / High             BOM/schedule or public       and claims; teacher-safe
semester                                                                                                            from semester build
                                                        claims                       wording; IPR review


15. Required semester deliverables and live demonstration
15.1 Deliverables
 • Working guarded VibeGuard Level-1 prototype.
 • Final BOM, source record, wiring/pin map and power-domain diagram.
 • Motor-rig configuration and safety checklist.
 • Versioned ESP32 firmware and reproducible analysis scripts.
 • Raw-session register, configuration metadata and held-out validation results.
 • Final report containing results, limitations, negative evidence and resource use.
 • Teacher-ready presentation and live-demo procedure.
 • Archived OpenBraille zeroth-review package kept separate from VibeGuard implementation evidence.


    Dept. of CSE (CY)                                  PBCST504 - Microcontrollers                                                 Page 15
                                  Dept. of CSE (CY)         PBCST504 - Microcontrollers             Page 15

                              Topic: VibeGuard - Semester Implementation and Future Research Roadmap


15.2 Recommended five-minute live demonstration
1. Show the guarded rig, rigid sensor mount, ESP32 and separate power domains while power is off.
2. Connect USB, show the configuration banner and complete a short calibration/self-check.
3. Run the normal state: green LED and live USB features/logs.
4. Apply the pre-inspected induced-abnormal configuration: red LED after persistence and visible logged
   feature/spectral change.
5. Return to the approved normal configuration and show recovery according to the frozen state rule.
6. Show one held-out result table, resource measurements and the explicit limitations: controlled rig, Level 1 only, no
   patent claim.

15.3 Demo failure fallback
If the powered abnormality demonstration cannot be run safely in the classroom, use an approved guarded video of
the locked setup plus a live sensor/firmware playback only if the teacher accepts that fallback. Do not improvise an
unguarded rotating mass for presentation impact.


16. Post-semester PIRG research hypothesis


                   Figure 4. PIRG research concept. This is not implemented or validated in the semester system.

16.1 Technical question
Can one target-mounted vibration sensor preserve enough information to distinguish a change caused by the target
machine from a change caused by an independently operating neighbouring source, when the system is
commissioned using controlled paired physical interventions?

16.2 Candidate mechanism in non-claim language
1. During commissioning, change the target state while keeping the interferer at the same labelled condition. Form a
   target-change representation from paired differences.
2. Separately change the interferer while the target is independently confirmed normal. Form an interference-
   change representation.
3. At runtime, compare a new deviation against both representations using one permanent target-mounted sensor.
4. Declare Target-Abnormal only when the event is anomalous and fits the target-change structure materially better
   than the interference-change structure.
5. Return Unknown for ambiguous, unsupported or mount-invalid observations rather than forcing a target-fault
   claim.


    Dept. of CSE (CY)                              PBCST504 - Microcontrollers                                     Page 16
                              Dept. of CSE (CY)         PBCST504 - Microcontrollers          Page 16

                                Topic: VibeGuard - Semester Implementation and Future Research Roadmap


6. Defer quarantined baseline updates until the attribution core has independently passed; do not make every
   familiar feature part of one speculative bundle.

16.3 Why this is only a hypothesis
 • One sensor observes a mixture; the two physical sources may be non-identifiable or nearly collinear.
 • Mounting, speed, load and structural coupling may change the contrast structures.
 • Known subspace comparison, open-set rejection, Mahalanobis models and single-sensor classification create high
   obviousness risk.
 • No current experiment shows that PIRG beats strong conventional baselines.
 • A model simulation cannot replace enablement, field labels or professional patent review.


17. Six-to-twelve-month future research roadmap
            Month                       Stage                            Work                        Pass evidence                      Failure action


                                                             Freeze Level-1 platform;
                                                                                                                                Continue
                                                             preserve raw                    Stable Level-1 data; safety-
                           Semester foundation and                                                                              semester/publication only if a
0-2                                                          data/timing/mount records;      approved target/interferer
                           research design                                                                                      reliable scaffold cannot be
                                                             design two-motor coupled rig    scaffold
                                                                                                                                built
                                                             and temporary ground truth

                                                                                             Untouched day/remount
                                                             Collect target
                                                                                             shows ≥30% relative
                                                             normal/abnormal × interferer
                                                                                             reduction in wrong                 Kill PIRG if target/interference
                                                             off/normal/abnormal across
2-4                        Early paired-intervention gate                                    attribution/false target alerts,   directions are inseparable or
                                                             ≥3 days/remounts; compare
                                                                                             ≤5 percentage-point miss-rate      gain is leakage/abstention
                                                             RMS, FFT/bands, Mahalanobis
                                                                                             worsening and ≥80%
                                                             and conventional classifier
                                                                                             coverage

                                                             Freeze PIRG representation;
                                                                                             Complete mechanism
                                                             remove each asserted                                               Remove non-contributing
                           Mechanism and ablation                                            outperforms strongest
4-6                                                          component; test held-out                                           features; kill patent route if
                           phase                                                             baseline and critical ablations
                                                             interferer level, speed/load                                       result is additive/generic
                                                                                             on locked data
                                                             and mount validity

                                                             Test more than one
                                                             motor/arrangement; obtain
                                                                                             Effect survives another
                                                             independently labelled                                             Retain only as bench
6-9                        Field-like replication                                            arrangement without
                                                             target/interferer states; run                                      publication if transfer fails
                                                                                             permanent reference sensors
                                                             local ESP32 timing/resource
                                                             tests

                                                             Lock architecture, datasets,
                                                                                             Reproducible evidence pack
                                                             negative results, contributor                                      Do not file from an outcome-
9-10                       Confidential evidence freeze                                      and clear claim-to-experiment
                                                             chronology and public/private                                      only idea
                                                                                             map
                                                             disclosure log

                                                             Refresh worldwide
                                                             patent/NPL search;
                                                                                             Named useful scope remains
                           Fresh claim-level search and      institutional invention                                            Trade secret/publication/kill if
10-11                                                                                        after closest art and design-
                           IPR review                        disclosure; counsel-led                                            scope is trivial or blocked
                                                                                             around analysis
                                                             novelty, inventive-step,
                                                             eligibility and FTO screen

                                                             Select narrow supported
                                                             filing, confidential            One reasoned written               Archive and publish only
11-12                      File/no-file management gate
                                                             continuation, publication or    decision; no grant promise         after IPR/FTO review
                                                             termination


17.1 Research baselines and ablations
                               Type                                                                   Required comparison

                                                                              RMS+persistence; FFT/bands; ordinary Mahalanobis; static
Strong conventional baselines
                                                                              spectral subtraction; a competent single-sensor classifier

                                                                              Target contrast removed; interference contrast removed;
PIRG component ablations                                                      Unknown forced into binary; mount-validity gate removed;
                                                                              operating-state conditioning removed

                                                                              Hold out complete day/remount and at least one interference
Evidence split
                                                                              condition; never random-window leakage


       Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                                          Page 17
                                Dept. of CSE (CY)                PBCST504 - Microcontrollers                  Page 17

                            Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                            Type                                                         Required comparison

                                                                   ESP32 acquisition and inference with no locked-run block loss
Local deployment
                                                                   or hidden saturation

                                                                   Temporary reference sensors or independent controls may label
Physical truth
                                                                   experiments but are not permanent product sensors


17.2 Patent-development kill conditions
 • Target and interference changes occupy essentially the same observable signal direction.
 • PIRG does not beat the strongest conventional comparator on held-out sessions.
 • Performance works only by classifying an impractically large fraction as Unknown.
 • A permanent second/reference sensor is required for operation.
 • The ADXL345 misses the discriminating band and a broader sensor change destroys the connected architecture
   case.
 • Remounting, speed/load or another motor arrangement destroys the result.
 • Fresh prior art shows the claim-defining combination or useful scope becomes trivial/easily avoided.
 • Institutional/professional review does not justify filing cost or disclosure risk.


18. Confidentiality, inventorship and disclosure control
18.1 Public-safe semester material
 • ADXL345 + ESP32 architecture, SPI acquisition, time features, triggered FFT, RMS/persistence, ordinary
   Mahalanobis comparison, RGB and guarded eccentric-mass rig.
 • Level-1 normal-versus-induced-abnormal results, provided limitations and configuration are disclosed.
 • Budget, schedule, team roles and educational objectives.

18.2 Keep private until IPR review
 • Exact PIRG paired-intervention representation, residual/fit calculation and thresholds.
 • Any baseline quarantine, update, rollback or mount-validity mechanism that later survives ablation.
 • Labelled interference/remount datasets, field-like results and claim-to-experiment maps.
 • Unpublished negative/positive ablation results and any combination showing an unexpected technical effect.

18.3 Inventorship/contribution record
Maintain a dated record of who conceived each later mechanism, who designed each experiment, who implemented
code/hardware, and when the result was first reduced to practice. Model-generated wording is not a substitute for
human conception. The institutional IPR cell should determine inventorship and disclosure strategy before any filing.

18.4 Disclosure rule

   Do not rely on an assumed grace period
   Before publishing code, datasets, posters, videos, papers, competition entries or detailed teacher material about
   the future mechanism, obtain institutional IPR review. The public semester MVP and confidential future
   research must remain in separate folders and explanations.


19. Decision gates and escalation rules
             Gate                                When                             Pass                        Fail response

                                                                   VibeGuard Level-1 approved        Continue approved concept or
G0 - Teacher approval           Before procurement
                                                                   with scope/budget                 revise request

                                                                   ESP32, ADXL345, motor and
G1 - Component acceptance       Week 2                                                               Replace before integration
                                                                   supply pass checks


    Dept. of CSE (CY)                               PBCST504 - Microcontrollers                                          Page 18
                             Dept. of CSE (CY)           PBCST504 - Microcontrollers            Page 18

                                  Topic: VibeGuard - Semester Implementation and Future Research Roadmap


                Gate                                  When                               Pass                          Fail response

                                                                           Stable ODR/timestamps; visible    Reduce rate/clock, fix wiring or
G2 - Acquisition integrity           Week 3
                                                                           counters; no silent loss          replace sensor

                                                                           Normal and abnormal states are    Redesign mechanical fixture
G3 - Rig repeatability               Weeks 4-5
                                                                           safe and repeatable               before algorithm work

G4 - Minimum demonstrable                                                  Local RMS+persistence, RGB and    Use Weeks 9-10 for stabilization
                                     End Week 8
system                                                                     USB path works                    only; cut optional features

                                                                                                             Submit as controlled
                                                                           Teacher-approved Level-1
G5 - Locked semester validation      Week 10                                                                 measurement study with
                                                                           metrics reported honestly
                                                                                                             documented limitations if missed

                                                                           Attribution improvement
                                                                                                             Stop patent spending; retain
G6 - PIRG early research             Months 2-4 post-semester              survives untouched
                                                                                                             publication/engineering value
                                                                           session/remount

                                                                           Evidence, useful scope, search
G7 - IPR/file-no-file                Months 10-12                          and professional review support   Trade secret, publication or kill
                                                                           action


20. Open questions and teacher decisions
                 ID                          Question / decision                        Owner                          Required by

                                     Approve VibeGuard as the
                                     semester implementation and
Q1                                                                         Project coordinator               Before procurement
                                     this dossier as the controlling
                                     build plan?

                                     Confirm whether the
                                     implementation window is
Q2                                                                         Project coordinator               Week 1
                                     effectively 8 weeks or the full 12-
                                     week roadmap?

                                     Approve verified ESP32-
Q3                                   WROOM-32 DevKit or authorize          Teacher + Nihad/Sreehari          Before order
                                     ESP32-S3 based on availability?

                                     Approve the proposed
                                     quantitative Level-1 validation
Q4                                                                         Teacher + technical leads         Before Week 8
                                     targets or replace them with
                                     another pre-registered protocol?

                                     Which lab tools and safety
Q5                                   reviewer are available for the        Amith + department                Week 1
                                     motor rig?

                                     Approve the proposed name-to-
Q6                                                                         Full team + teacher               Week 1
                                     role map or require changes?

                                     What project information may
Q7                                   be made public before                 Project owner/IPR cell            Before public disclosure
                                     institutional IPR review?

                                     Does the department have a later
                                     field-like site or industry contact
Q8                                                                         Coordinator/department            Post-semester planning
                                     for independently labelled
                                     target/interferer research?


21. Teacher approval and conditions
                             Decision item                                                          Teacher response

Semester project                                                           Approved / Approved with conditions / Not approved

                                                                           ESP32-WROOM-32 DevKit / ESP32-S3 / Other authorized
Approved board
                                                                           board: __________

     Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                               Page 19
                                  Dept. of CSE (CY)            PBCST504 - Microcontrollers             Page 19

                               Topic: VibeGuard - Semester Implementation and Future Research Roadmap


Approved budget ceiling                                            ₹ __________

Approved implementation window                                     __________ weeks

                                                                   As proposed / Modified as attached / To be submitted by
Approved Level-1 acceptance protocol
                                                                   __________

Safety/facility conditions

Other conditions/comments

Signature and date


22. Source basis
This dossier was prepared from the controlled Project mC master package. The following files are the main evidence
layers:

                          Evidence layer                                                  Controlled source

                                                                   Engineering Design Review; Project mC Decision Register v1.2;
Project authority
                                                                   approved Phase 3C Portfolio Closure Memo

Comparative evidence                                               Concept Evidence Matrix; Uncertainty and Test Register

VibeGuard technical authority                                      Final VibeGuard Architecture Report, Memory and SOP

                                                                   Two final cross-concept adjudications, treated as context rather
Comparative decision context
                                                                   than votes

                                                                   VibeGuard Pre-Build Future Patent-Case Simulation, treated as
Future-research boundary
                                                                   an unbuilt hypothesis

                                                                   Project mC Teacher Documents Master Evidence, Costing and
Current cost/spec basis
                                                                   Decision Basis, price-checked 03 August 2026

                                                                   Final OpenBraille zeroth-review presentation and approved
Previous academic context
                                                                   change request


22.1 Current official specification and price references
 • Analog Devices, ADXL345 product page and data sheet: https://www.analog.com/en/products/adxl345.html
 • Espressif, ESP32-WROOM-32 data sheet: https://www.espressif.com/sites/default/files/documentation/esp32-
   wroom-32_datasheet_en.pdf
 • Espressif, ESP32-S3 product page and DevKitC-1 guide: https://www.espressif.com/en/products/socs/esp32-s3
 • Indian price snapshots and procurement notes are listed in the Master Evidence, Costing and Decision Basis and
   must be refreshed on purchase day.
  Prepared for academic project implementation. The future research section is a management and experimental roadmap, not a
                    patent opinion, filing recommendation, freedom-to-operate clearance or promise of grant.


    Dept. of CSE (CY)                               PBCST504 - Microcontrollers                                         Page 20
                                Dept. of CSE (CY)        PBCST504 - Microcontrollers          Page 20


---

## Source 6: `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md`

- Authority: `TIER_2`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `cb80b048a9238c232ed2b9a37da9f0997ba65cd5eb5f0f303764c42b51c99e4b`

# Source Extraction

- Chapter: `06` — VibeGuard Frozen Architecture and Semester Scope
- Authority tier: `TIER_2`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/PATENT_EVIDENCE_INDEX.md`
- Current SHA-256: `cb80b048a9238c232ed2b9a37da9f0997ba65cd5eb5f0f303764c42b51c99e4b`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# VibeGuard — Patent Evidence Index

## Controlled research lanes

1. ChatGPT Deep Research
2. Gemini
3. Perplexity
4. Qwen
5. Mistral — one partial compilation of incomplete fragments
6. Microsoft Copilot

## Valid synthesis set

1. Work Max
2. Standard High

## Exclusion

The separate Deep Research High synthesis preserved in the archive contains a
software-security concept swap. It is not valid evidence and is not a vote.

## Interpretation

The frozen Level-1 MVP is not treated as patent-ready. PIRG and dense-machine
attribution remain post-semester hypotheses requiring controlled evidence.


---

## Source 7: `03_CONCEPT_PORTFOLIO/VibeGuard/README.md`

- Authority: `TIER_2`
- Treatment: `SUPPORTING_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `1c2d6a321bb7c2673eefed788241e515bae213a5e654c3f524f8a6b3dad89b9f`

# Source Extraction

- Chapter: `06` — VibeGuard Frozen Architecture and Semester Scope
- Authority tier: `TIER_2`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/README.md`
- Current SHA-256: `1c2d6a321bb7c2673eefed788241e515bae213a5e654c3f524f8a6b3dad89b9f`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# VibeGuard — Concept Status

The files under `01_Final_Architecture` define the frozen Level-1 semester architecture. Dense-floor attribution and PIRG remain separate post-semester research hypotheses.

