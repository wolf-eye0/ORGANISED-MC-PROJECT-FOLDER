# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- Current SHA-256: `29d0f85d95f7ef98d1a1a31a395cbbab5511ae25df2eeb15840978d7bfb3590e`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC Final Cross-Concept Patent-Path Adjudication

**Evidence cut-off:** 1 August 2026
**Adjudication basis:** the 12-file blind package only
**Nature of output:** engineering and patent-strategy decision support; not legal advice, patentability clearance, claim construction, infringement analysis, or FTO clearance

## 1. Executive decision

### Required five decisions

1. **Best semester-build candidate: VibeGuard.** Its frozen Level-1 system has the strongest three-month feasibility, lowest cost, clearest live demonstration, and best fit for the team’s embedded/DSP strengths.
2. **Best post-MVP patent-development candidate: OpenBraille D11, conditionally.** The integrated mechanical-datum, per-dot calibration, isolated shared-current verification, physical-ground-truth, bounded-retry/fault-isolation and current-aware sequencing route is the most directly testable and physically anchored of the three later mechanisms. It is not presently established as patentable; the conservative synthesis correctly keeps it at Track D until the named gate passes, while the secondary synthesis supports only a bounded prospective Track B.
3. **Best overall Project mC action now: Run one named short feasibility gate before selecting.** Run the **OpenBraille D11 Physical-State Observability Gate** for **10 calendar days from formal start**. If it passes, select OpenBraille. If it fails, select VibeGuard immediately.
4. **Runner-up and fallback: VibeGuard.** It is the current integrated-score leader under all three weightings and the fallback because its semester success is much less dependent on unresolved mechanical or institutional facilities.
5. **Prototype/publication-only or deprioritized concept: TrueMoist.** Retain it as a rigorous measurement/publication project and later research option, but deprioritize it for the present patent-first selection because decisive transfer/validity proof needs more probes, lots, remounts and metrology than the semester package can support.

### Named gate

**Gate name:** OpenBraille D11 Physical-State Observability Gate
**Deadline:** day 10 after gate start
**Minimum setup:** one single-dot servo/cam/pin module; mechanical datum; three SG90-class servos; two reassemblies; current/voltage sensing; independent optical/mechanical ground truth; fixed-PWM and calibrated comparators.
**Pass threshold:**

- at least **95% sensitivity and 95% specificity** on untouched events for distinguishing completed raise/retract from induced jam/incomplete travel;
- **zero silently accepted wrong physical states in 500 held-out transitions**;
- calibrated datum-plus-verification control must reduce out-of-spec or failed transitions by at least **30% relative to fixed common-PWM control**;
- a current-only decision must not be accepted unless it agrees with physical ground truth; and
- committed spend must remain below ₹5,000 with no unsafe sustained stall.

**Fallback:** any pass element missed means select VibeGuard and retain OpenBraille only as an assistive prototype/publication track. Passing the gate does not prove patentability; it only authorizes selection and a claim-focused search/IPR review.

**Confidence:** medium. The current evidence favors VibeGuard numerically, but a low-cost, short OpenBraille gate can resolve the single uncertainty most capable of reversing a patent-first decision.

## 2. Input inventory and provenance

Exactly **12 physical Markdown attachments** were present. All were readable. Byte counts and SHA-256 hashes for files 00–10 matched the provenance register exactly; parenthetical upload suffixes are transport-name artifacts, not substantive versions.

| Controlled role | Attached file | Result |
|---|---|---|
| Governing instruction | `00_READ_FIRST_Project_mC_Final_Adjudication_Instructions(2).md` | Readable; 16,558 bytes; hash matched |
| Governance 1 | `01_Project_mC_Decision_Register_v1.2(2).md` | Readable; v1.2; hash matched |
| Governance 2 | `02_Phase3C_Portfolio_Closure_Memo_Approved(2).md` | Readable; hash matched |
| Common evidence 1 | `03_Concept_Evidence_Matrix(3).md` | Readable; hash matched |
| Common evidence 2 | `04_Uncertainty_and_Test_Register(2).md` | Readable; hash matched |
| OpenBraille 1 | `05_OpenBraille_Synthesis_Work_Max(2).md` | Complete; concept-faithful; hash matched |
| OpenBraille 2 | `06_OpenBraille_Synthesis_Valid_Secondary(2).md` | Complete; concept-faithful; hash matched |
| VibeGuard 1 | `07_VibeGuard_Synthesis_Work_Max(2).md` | Complete; concept-faithful; hash matched |
| VibeGuard 2 | `08_VibeGuard_Synthesis_Standard_High(2).md` | Complete; concept-faithful; hash matched |
| TrueMoist 1 | `09_TrueMoist_Synthesis_Max(2).md` | Complete; concept-faithful; hash matched |
| TrueMoist 2 | `10_TrueMoist_Synthesis_High_Deep_Research(2).md` | Complete; concept-faithful; hash matched |
| File control | `99_EXCLUSION_AND_PROVENANCE_REGISTER(2).md` | Readable; treated only as provenance/reliability context |

All ten requested control confirmations pass:

1. exactly 12 attachments;
2. governing instruction readable;
3. all four common governance/evidence files present;
4. exactly two valid synthesis reports for each concept;
5. OpenBraille filename crossing explicitly resolved;
6. failed moving-roller OpenBraille synthesis absent;
7. failed software-security VibeGuard synthesis absent;
8. supplementary TrueMoist Work Max web audit absent and not inferred;
9. Decision Register v1.2 present and v1.1 absent;
10. no selected synthesis missing, unreadable, duplicated, physically partial, or concept-swapped.

The crossing is not that the two attached reports describe two OpenBraille variants. The valid secondary originally carried `OpenBraille_Patent_Synthesis_ChatGPT_Standard_High_no_deeprsearch.md`; the file originally named `OpenBraille_Patent_Synthesis_ChatGPT_Deep_Research.md` was the excluded moving-roller concept swap.

## 3. Authority and constraints

Authority was applied in this order: Decision Register v1.2; approved closure memo; Concept Evidence Matrix; Uncertainty and Test Register; audited syntheses. The register confirms the retained portfolio is OpenBraille, VibeGuard and TrueMoist, and makes patent-development potential the primary selection priority while retaining feasibility, budget, demonstration and team fit as mandatory constraints.

Binding constraints used in scoring:

- up to three months;
- preferred budget ≤₹3,000 and hard ceiling ₹5,000;
- five members: three strong technical contributors, one learner, one presenter/support member;
- Arduino IDE/embedded-board compatibility;
- low-power components and USB interface/sample;
- strong live demonstration;
- no invented scope or unsupported patent certainty.

The closure memo’s descriptive starting point was preserved: OpenBraille has the highest long-term physical-invention ceiling, VibeGuard the strongest live embedded/DSP demonstration and team fit, and TrueMoist the lowest nominal electronics risk with a plausible compensation-method path. Those statements are starting evidence, not the final ranking.

## 4. Concept-fidelity audit

**OpenBraille — pass.** Both selected reports preserve a six-dot macro cell using six SG90-class servos, PWM, eccentric cams/followers and vertically translating pins. The later direction is D11-type verified refresh. No moving roller, encoder wheel, RAMPS/Mega or paper embosser entered the analysis.

**VibeGuard — pass.** Both reports preserve one rigidly mounted ADXL345-class sensor, ESP32 local processing, time features, triggered FFT, RMS-plus-persistence baseline, prospective Mahalanobis, RGB state and isolated-motor Level 1. Level 2 remains target attribution despite independent interference. No software scanner, wearable, active cancellation, array, cloud or RUL substitution was used.

**TrueMoist — pass.** Both reports preserve the validated 72-run, one-soil, analog-probe/DS18B20, controlled-salinity-code, ADC-gate, M0/M1/M2 fixed-offline-model architecture. No live EC, custom multi-frequency probe, irrigation control, cloud, TinyML, online learning or multi-soil MVP was imported.

## 5. Synthesis reliability audit

| Synthesis | Fidelity | Frozen-MVP verdict | Later-route verdict | Reliability | Adjudication treatment |
|---|---|---|---|---|---|
| OpenBraille Work Max | Pass | MVP is an engineering prototype, not a credible invention | D11 remains Track D; reopen B only after search and stringent data | **High** | Most conservative and claim-focused; transparent about unresolved Indian file, state observability and additive-effect risk |
| OpenBraille Valid Secondary | Pass | MVP not an invention | Bounded Track B for integrated tolerance compensation and verified refresh | **Medium** | Strong engineering definition, but its positive Track-B label rests on an unbuilt integration and proposed thresholds; treated as a hypothesis, not a conclusion |
| VibeGuard Work Max | Pass | Frozen stack is conventional | Track C target-attribution mechanism | **High** | Strong separation of Level 1 and Level 2, claim corrections and field-evidence burden; provisional status labels not treated as legal conclusions |
| VibeGuard Standard High | Pass | Frozen stack is research platform | Track C integrated commissioning/abstention/quarantine/remount method | **Medium** | Mechanism is specific and experiments well defined; proposed 30% threshold is a research recommendation, not authority; field transfer remains unproven |
| TrueMoist Max | Pass | Frozen 72-run stack is Track D as a patent direction | Track C composite replacement/remount transfer and validity path | **High** | Conservative treatment of close art and physical-sample burden; strongest on kill criteria and simple-baseline comparison |
| TrueMoist High + Deep Research | Pass | Frozen MVP conventional | Track C physical-reference-bound transfer/acceptance | **Medium** | Good claim-level framing; some legal-status statements remain provisional and the two-probe semester pilot cannot support population transfer |

### Resolution of the OpenBraille disagreement

The reports do not disagree about the frozen MVP: both reject it as the invention. They disagree about when the integrated D11 route deserves Track B. The secondary treats the specificity and three-month accessibility as sufficient for a provisional B; Work Max applies a stricter burden because current signatures may measure internal servo effort rather than tactile state, the individual elements are known, the Indian filing remains unresolved, and no non-additive effect exists yet.

This adjudication adopts **current Track D, prospective Track B only after the named gate and claim-focused review**. That preserves the secondary report’s bounded opportunity without converting an experiment plan into patent evidence.

## 6. Normalization method

Each concept was split into two independent objects:

- the frozen semester MVP actually authorized by project authority;
- the post-MVP invention-development mechanism, with its own hardware, evidence, time, cost and kill conditions.

Scores are 0–5 with low/base/high ranges. Low represents adverse but plausible execution; base represents the most supported current forecast; high represents favorable execution without assuming patent success. Weighted scores are converted to 100. Patent scores assess the later mechanism, not the frozen MVP.

## 7. OpenBraille frozen-MVP fact sheet

| Field | Finding |
|---|---|
| Exact architecture | One approximately 300%-scale six-dot Braille cell; ESP32-WROOM-32; six SG90-class servos; direct 50 Hz PWM; one eccentric cam/follower/sliding pin per dot; FDM frame/guides/cams; external 5 V/2 A supply and 1,000 µF rail capacitor; active cam retraction unless a real passive return is proven |
| Three-month deliverable | Functional macro cell accepting characters over USB/serial, mapping to six dots, refreshing patterns, measuring travel/repeatability/power and performing tactile evaluation |
| Budget | ₹2,060–₹2,850 frozen estimate; enhancement can bring total to roughly ₹2,910–₹4,700 |
| Validation | Single-dot-first; power and active-retraction tests; six-dot integration; ≤0.1 mm position variance over 100 cycles; ≥1,000 actuations; pre-approved tactile protocol; full character transitions |
| Primary engineering risk | FDM tolerance/friction, active retraction, pin-height consistency, wear and six-servo power transients |
| Current patent verdict | Exact narrow literal differences may exist, but the useful servo/cam/pin combination is predictable and crowded; do not file on the frozen MVP |
| Strongest prior art | Rotary raised surface/guided pins (`US8483018B2`); independently actuated tactile pins (`US20130017516A1`); modular stops/guides (`US8690576B2`, `US7410359B1`, `US12080182B2`); public servo/cam and micro-motor projects; unresolved Indian `5559/CHE/2014` |
| Eligibility/FTO | Physical hardware is generally eligible; novelty/obviousness are the main weakness. FTO unresolved, particularly the Indian filing and active modular/capture families |
| Demo value | Very high social-impact and physical-motion demonstration; tactile success must not be inferred from visual motion |
| Publication value | High for low-cost assistive prototyping, manufacturing reliability, negative current-signature results or calibrated-vs-open-loop benchmarking |
| Current Track | **D as patent direction; strong prototype** |

## 8. OpenBraille post-MVP patent-path fact sheet

| Field | Finding |
|---|---|
| Proposed mechanism | D11 integrated datum + per-dot operating windows + sequential isolated shared-current measurement + independent physical ground truth during development + bounded retry/fault isolation + current-aware sequencing |
| Relationship to MVP | Direct extension of the same servo, cam, pin, power and control errors; no actuator-family switch required |
| Closest patent/NPL art | Braille stops/guides/calibration; generic motor-current state and jam diagnostics; tactile movement sensing; ordinary servo calibration and staggered power control; public servo/cam mechanisms |
| Claimed physical effect | Fewer incomplete raises/retractions, out-of-spec pin heights, silent wrong states, stalls and brownouts than fixed common-PWM control; reliable fault reporting rather than command-assumed success |
| Required decisive experiments | Three servos, two reassemblies, labelled raise/retract/jam events, optical/mechanical ground truth, fixed-PWM/calibration/sensing/full-system baselines, 500-transition short gate then 3,000-transition confirmatory run and ablations |
| Additional hardware/cost | Shunt/current amplifier or sensor, spare servos, printed coupons, ground-truth fixture; roughly ₹500–₹1,400 incremental, total below ₹5,000 if controlled |
| Time | Initial feasibility 10 days; full semester evidence possible; practical-scale and multi-build proof another 4–9 months |
| Claim usefulness if successful | Potentially useful narrow hardware-control claim around verified refresh of heterogeneous low-cost actuator channels; broader “servo Braille” claims are not credible |
| Main risks | High obviousness; current may not reveal pin state; apparent benefit may be ordinary calibration/staggering; unresolved Indian/control claims; practical-scale transfer may fail |
| Strongest baseline | Fixed common PWM; per-dot calibration only; datum only; sensing only; fixed sequential actuation; direct per-dot sensor oracle |
| Kill condition | Failure of physical-state discrimination, any silent wrong state, no cooperative effect beyond components, dependence on hand-selected servo/build, unsafe stall, or closer claim |
| Prospective Track | **B only after gate; otherwise D/publication** |

## 9. VibeGuard frozen-MVP fact sheet

| Field | Finding |
|---|---|
| Exact architecture | One rigid ADXL345-class accelerometer over SPI to ESP32-WROOM-32/S3; local DC removal, Hann, RMS/peak/std/crest/kurtosis, RMS-plus-persistence baseline, triggered 256–1,024 FFT, band features/static subtraction, prospective Mahalanobis, RGB local state; isolated motor/fan eccentric-mass rig |
| Three-month deliverable | Stable acquisition, normal calibration, repeatable induced abnormal condition, local Normal/Abnormal indication, USB logs, resource measurements and quantitative Level-1 trials |
| Budget | ₹1,700–₹2,200; large headroom under ₹3,000 and ₹5,000; IIS3DWB excluded from MVP |
| Validation | Rigid mount and repeated rig sessions; stable eccentric-mass labels; RMS baseline then FFT/Mahalanobis comparators; owner-approved accuracy/false-alarm criteria; no Level-2 claim from target-only bench data |
| Primary engineering risk | Mount/coupling repeatability, sample integrity, threshold tuning and false confidence from overlapping windows rather than independent sessions |
| Current patent verdict | Commodity sensor + standard DSP/statistics + local alert is conventional and predictable; no Track A case |
| Strongest prior art | KCF spectral baseline/rebaselining, Mitsubishi/Valqua Mahalanobis vibration diagnosis, Rolls-Royce speed-frequency normal spaces, Tractian fingerprints/learning, bearing source-provenance and NPL single-sensor separation |
| Eligibility/FTO | Physical diagnostic context helps eligibility but generic scores remain vulnerable; FTO unresolved in US/India/China and across commercial portfolios |
| Demo value | Highest: immediate green/blue/red live response to a visible motor condition |
| Publication value | High for embedded benchmark, mount effects, triggered-vs-continuous DSP, false-alarm analysis and mixed-vibration datasets |
| Current Track | **C for patent path; strong Level-1 prototype** |

## 10. VibeGuard post-MVP patent-path fact sheet

| Field | Finding |
|---|---|
| Proposed mechanism | Known-state commissioning of target/interferer states; target-conditioned fingerprint; source/mount validity estimate; Normal/Target-abnormal/Unknown decision; candidate-buffer quarantine; guarded baseline promotion; contamination lockout; remount invalidation/transfer; local resource-constrained execution |
| Relationship to MVP | Same one target-mounted sensor and ESP32; adds controlled interference experiments, labels and state-management logic |
| Closest patent/NPL art | Rolls-Royce speed-conditioned fingerprints; Mitsubishi/Valqua normal-space scoring; KCF baseline subtraction/rebaselining; Tractian fingerprints; generic abstention/drift adaptation; mounting standards/studies; single-sensor separation literature |
| Claimed physical effect | Lower wrong-source target alarms and baseline contamination under neighbour changes, without materially increasing missed target faults; reliable invalidation after remount |
| Required experiments | Dual-motor mechanically coupled rig; target normal/abnormal × interferer off/normal/abnormal; ≥2 operating regimes; ≥3 remounts; ≥5 independent sessions; held-out day/remount; mandatory baselines and ablations; later real or field-like site |
| Additional hardware/cost | Second motor/interferer, fixtures and temporary ground-truth tachometer/reference sensor; semester pilot may fit under ₹5,000, but decisive field/site work has no defensible student-budget estimate |
| Time | Preliminary Level 2A in semester; decisive Level 2B approximately one additional semester and dependent on site access |
| Claim usefulness if successful | Narrow but potentially useful source-attribution/update-control claim for a single mounted node; broad vibration-monitoring/statistical claims are unavailable |
| Main risks | High obviousness; generic software/statistics center; field labels unavailable; abstention hides errors; remount/speed confounding; active portfolios need claim charts |
| Strongest baseline | RMS+persistence; ordinary FFT/bands; ordinary Mahalanobis; static subtraction; naive adaptive baseline; full recalibration after remount |
| Kill condition | No held-out attribution gain; excessive abstention; contamination admitted; no cooperative effect; remount failure; field labels unavailable; embedded/resource failure; closer claim |
| Prospective Track | **C** |

## 11. TrueMoist frozen-MVP fact sheet

| Field | Finding |
|---|---|
| Exact architecture | Genuine analog capacitive probe plus nearby DS18B20; ESP32; ADS1115 retained only if paired gate justifies it; controlled NaCl treatment code, not measured EC; hardened analog path; M0/M1/M2 offline training and fixed local inference; one homogeneous soil; 4×3×2×3 = 72 independent physical runs; dry-basis gravimetric truth |
| Three-month deliverable | Complete early gates, collect 72 runs, hold replicate 3 untouched, deploy selected fixed model to ESP32, show raw/reference/compensated values and absolute errors over USB/CSV |
| Budget | ₹1,790–₹3,440 with institutional oven/scale access; below ₹5,000 with optional scale/contingency; oven purchase out of scope |
| Validation | Probe monotonicity/reinsertion; packing jig; ADC comparison; salinity pilot; oven/scale access; 72-run throughput; held-out RMSE ≥20% and MAE ≥15% improvement over M0; no major subset >10% MAE worsening |
| Primary engineering risk | Physical workload and traceable ground truth: packing/insertion, oven capacity, equilibration, dry-mass workflow and schedule |
| Current patent verdict | The exact factorial is rigorous evidence generation, not invention; temperature/salinity metadata plus ordinary regression and fixed MCU inference are predictable |
| Strongest prior art | TCS low-cost sensor health/replacement; CN replacement-probe equivalence; event recalibration/confidence; preset correction identifiers; nonlinear temperature compensation; calibration fixtures; incumbent capacitive/salinity hardware |
| Eligibility/FTO | Generic regression, confidence and metadata are weak eligibility centers; live claims/status unresolved in several jurisdictions; no “clear FTO” conclusion |
| Demo value | Good scientific before/after accuracy display, but less immediately dramatic and dependent on a long experiment completed beforehand |
| Publication value | Highest: controlled compensation, measurement uncertainty, pseudoreplication avoidance, ADC comparison and negative transfer/remount evidence |
| Current Track | **D as frozen patent direction; C only for later robustness/transfer** |

## 12. TrueMoist post-MVP patent-path fact sheet

| Field | Finding |
|---|---|
| Proposed mechanism | Coefficient/provenance binding to probe/setup; defined physical reference challenge after replacement/remount; disturbance-residual validity envelope; accept bounded transfer only when valid; quarantine contaminated recalibration; abstain/fallback when validity fails |
| Relationship to MVP | Uses the same commodity probe, temperature/salinity disturbance model, gravimetric discipline and ESP32; expands from compensation to transfer/validity |
| Closest patent/NPL art | CN replacement-probe reference conditioning; TCS calibration/health/replacement; self-learning wet/dry bounds; event recalibration/confidence/exclusion; preset correction; calibration fixtures; generic OOD/statistical validity |
| Claimed physical effect | Reduce severe accepted errors and calibration workload when replacing/remounting cheap probes, while rejecting contaminated or invalid transfer states |
| Required experiments | Donor/replacement transfer; naive reuse, one-point, two-point affine, pooled and full-oracle baselines; remount/packing/temp/salt/electronic-offset challenges; clean/contaminated events; 6–12 probes, ≥2 lots and ≥3 batches for credible later proof |
| Additional hardware/cost | Existing second probe supports only pilot; later proof needs 6–12 probes, lots, containers, repeated gravimetric work and possibly institutional support beyond ₹5,000 |
| Time | Two-probe pilot in semester; credible proof one additional semester or more |
| Claim usefulness if successful | Narrow transfer/validity claim for commodity probes; broad calibration, replacement, confidence or event-recalibration claims are crowded |
| Main risks | Closest art is directly on replacement equivalence and sensor health; simple two-point affine transfer/range gate may explain result; population support weak; high experimental burden |
| Strongest baseline | Naive coefficient reuse; one-point; two-point affine; pooled model; full per-probe oracle; min/max/range gate; generic Mahalanobis or prediction interval |
| Kill condition | No advantage over two-point affine plus generic gate; false-valid reduction requires unusable abstention; no multi-unit/lot reproducibility; contamination gate fails; Level-1 metrology fails |
| Prospective Track | **C** |

## 13. Semester-build scoring matrix

| Factor | Weight | OpenBraille low/base/high | VibeGuard low/base/high | TrueMoist low/base/high |
|---|---:|---:|---:|---:|
| Build feasibility within three months | 25% | 2.4/3.3/4.0 | 3.9/4.5/4.9 | 3.0/3.8/4.4 |
| Measurement/validation feasibility | 20% | 1.8/2.6/3.3 | 3.5/4.2/4.7 | 2.0/3.1/4.0 |
| Budget compliance | 15% | 4.0/4.5/4.8 | 4.4/4.8/5.0 | 3.3/4.1/4.7 |
| Live demonstration clarity | 15% | 4.1/4.6/5.0 | 4.4/4.8/5.0 | 3.0/3.6/4.2 |
| Schedule and dependency risk | 10% | 2.0/2.8/3.5 | 3.4/4.1/4.6 | 1.8/2.8/3.8 |
| Team fit and task divisibility | 10% | 3.0/3.6/4.2 | 4.2/4.7/5.0 | 3.5/4.0/4.5 |
| Publication/educational fallback | 5% | 3.8/4.3/4.8 | 4.0/4.5/4.9 | 4.5/4.9/5.0 |

### Weighted semester-build totals

| Concept | Low | Base | High |
|---|---:|---:|---:|
| OpenBraille | 57.3 | **71.3** | 82.8 |
| VibeGuard | 79.1 | **90.2** | 97.4 |
| TrueMoist | 57.0 | **73.0** | 86.3 |

**Why material differences exist:** VibeGuard exceeds OpenBraille by more than one point on build feasibility, validation and team fit because its Level-1 rig has fewer coupled mechanical parts, no human tactile dependency and matches the team’s embedded/DSP strengths. VibeGuard exceeds TrueMoist by more than one point on validation, demonstration and schedule because TrueMoist’s authoritative output depends on 72 independent physical runs and institutional gravimetric facilities. TrueMoist exceeds OpenBraille on team/process divisibility and scientific fallback, while OpenBraille exceeds TrueMoist on live demonstration clarity.

## 14. Patent-path scoring matrix

| Factor | Weight | OpenBraille low/base/high | VibeGuard low/base/high | TrueMoist low/base/high |
|---|---:|---:|---:|---:|
| Distance from closest prior art | 20% | 1.5/2.5/3.4 | 1.8/2.7/3.5 | 1.3/2.1/3.0 |
| Specificity of proposed mechanism | 15% | 4.0/4.6/4.9 | 4.2/4.7/5.0 | 4.0/4.5/4.9 |
| Inventive-step resistance | 15% | 1.2/2.3/3.3 | 1.5/2.5/3.4 | 1.2/2.1/3.0 |
| Accessibility of decisive experiments | 15% | 3.5/4.4/4.8 | 1.7/2.6/3.6 | 1.5/2.5/3.5 |
| Usefulness/breadth of plausible claim | 10% | 2.0/3.2/4.0 | 2.3/3.3/4.0 | 1.8/2.8/3.6 |
| FTO/design-around posture | 10% | 1.6/2.6/3.5 | 1.8/2.7/3.5 | 1.5/2.3/3.2 |
| Direct connectedness to semester MVP | 10% | 4.6/4.9/5.0 | 4.4/4.7/5.0 | 4.2/4.5/4.9 |
| Publication value if patentability fails | 5% | 4.0/4.5/4.9 | 4.5/4.9/5.0 | 4.7/5.0/5.0 |

### Weighted patent-path totals

| Concept | Low | Base | High |
|---|---:|---:|---:|
| OpenBraille | 52.5 | **69.8** | 82.5 |
| VibeGuard | 50.9 | **66.5** | 80.0 |
| TrueMoist | 45.0 | **59.9** | 74.6 |

OpenBraille leads the base patent-path score because its mechanism is physically specific, almost perfectly connected to the MVP and can be falsified cheaply. This is not a finding that its prior-art position is better; its obviousness and FTO scores remain weak. VibeGuard’s mechanism is equally specific but decisive evidence requires independent interference labels and field-like validation. TrueMoist’s mechanism is specific, but the closest art is more directly aimed at replacement transfer, calibration and sensor health, and its proof requires a larger physical population.

## 15. Integrated-score sensitivity analysis

| Weighting | OpenBraille | VibeGuard | TrueMoist | Winner |
|---|---:|---:|---:|---|
| 40% build / 60% patent | 70.4 | **76.0** | 65.1 | VibeGuard |
| 50% build / 50% patent | 70.5 | **78.3** | 66.5 | VibeGuard |
| 30% build / 70% patent | 70.2 | **73.6** | 63.8 | VibeGuard |

The current score winner is **VibeGuard under every weighting**, so the numerical result is stable. The single assumption most capable of reversing the decision is whether OpenBraille can obtain reliable physical-state observability and a cooperative effect from D11 rather than ordinary calibration plus staggering. Because that assumption is inexpensive to test, a 10-day gate is more rational than either ignoring OpenBraille’s physical-invention upside or immediately committing the semester to its higher mechanical risk.

## 16. OpenBraille versus VibeGuard

- **Stronger semester build:** VibeGuard, by a large margin.
- **Stronger later technical mechanism:** OpenBraille if D11 passes; otherwise VibeGuard.
- **Closer/more damaging prior art:** OpenBraille’s physical elements are heavily crowded and the Indian filing is unresolved; VibeGuard’s statistical sub-elements are also crowded. OpenBraille has the more direct mechanism overlap, while VibeGuard has the more generic-software obviousness problem.
- **More expensive/longer evidence:** VibeGuard for decisive field attribution; OpenBraille’s first decisive experiment is cheaper.
- **Higher chance of a narrow useful claim:** OpenBraille conditional on verified state and synergy; VibeGuard if field attribution is real and reproducible.
- **Clearer kill experiment:** OpenBraille D11 physical-state gate.
- **Better publication fallback:** VibeGuard slightly, because a mixed-vibration benchmark and embedded results have broad technical value; OpenBraille has stronger social-impact value.
- **Reversal fact:** reliable D11 state verification and non-additive error reduction would move OpenBraille ahead; failure makes VibeGuard decisively preferable.

## 17. OpenBraille versus TrueMoist

- **Stronger semester build:** TrueMoist has lower mechanical complexity, but OpenBraille has the clearer live demo; base semester totals are close, with TrueMoist slightly higher.
- **Stronger later technical mechanism:** OpenBraille D11 because the decisive interaction can be tested with existing hardware and is more physically coupled.
- **Closer/more damaging prior art:** TrueMoist has especially close replacement-equivalence, event-calibration and sensor-health art; OpenBraille has dense actuator/guide/calibration art.
- **More expensive/longer evidence:** TrueMoist, due to 6–12 probes, lots and gravimetric physical challenges.
- **Higher chance of narrow useful claim:** OpenBraille, conditional on gate.
- **Clearer kill experiment:** OpenBraille.
- **Better publication fallback:** TrueMoist.
- **Reversal fact:** if OpenBraille current sensing cannot correlate with physical state, TrueMoist becomes the more defensible research programme, though not the preferred patent-first choice.

## 18. VibeGuard versus TrueMoist

- **Stronger semester build:** VibeGuard.
- **Stronger later technical mechanism:** VibeGuard, because source attribution plus guarded learning addresses a distinct diagnostic failure; TrueMoist is closer to known transfer/calibration practice.
- **Closer/more damaging prior art:** TrueMoist.
- **More expensive/longer evidence:** Both need later work; VibeGuard depends on a site, TrueMoist on many probes/lots and repeated metrology. Site access makes VibeGuard less controllable, while TrueMoist is more labor intensive.
- **Higher chance of narrow useful claim:** VibeGuard.
- **Clearer kill experiment:** TrueMoist’s two-point-affine-plus-range-gate comparator is clearer; VibeGuard’s field truth is harder.
- **Better publication fallback:** TrueMoist slightly for rigorous measurement science; VibeGuard for embedded/DSP relevance.
- **Reversal fact:** inability to obtain independent target/interferer labels would collapse VibeGuard’s Track C route and make TrueMoist the better later research option.

## 19. Novelty comparison

None of the frozen MVPs has a credible broad novelty nucleus. OpenBraille may avoid single-reference anticipation only through arbitrary exact details; VibeGuard’s feature stack is conventional; TrueMoist’s exact 72-run design is methodologically specific but not an invention.

For later paths, no reviewed source was shown to recite every element of D11, the VibeGuard integrated attribution/update sequence, or the TrueMoist composite transfer/validity sequence. That absence is not proof of novelty. Relative novelty risk is lowest for the exact VibeGuard and OpenBraille integrations, and highest for TrueMoist because replacement-reference and confidence/event-calibration art is particularly close.

## 20. Inventive-step/obviousness comparison

**OpenBraille:** high risk because stops, calibration, current diagnostics, retries and sequencing are individually familiar. The only defensible answer is a measured cooperative effect—physical state verification and fewer silent tactile errors that cannot be explained by ordinary tuning.

**VibeGuard:** high risk because known-state calibration, abstention, guarded updates, drift management and remount checks are familiar. Inventive step requires a source-specific coupling between ambiguity, decision, baseline promotion and mount validity that materially reduces wrong-source alarms.

**TrueMoist:** highest risk because one-/two-point calibration, reference challenges, replacement equivalence, confidence/exclusion and event recalibration are close art. A useful claim requires more than relabelling generic transfer and gating.

## 21. Patent-eligibility comparison

OpenBraille has the best eligibility posture because the center is an electromechanical tactile mechanism with measured physical states. VibeGuard and TrueMoist can also be framed as sensor-measurement improvements, but claims centered on Mahalanobis, confidence, abstention, regression, metadata or generic updates face greater US abstract-idea, EPO technical-contribution and Indian section 3(k) risk. Eligibility is not the primary weakness for any concept; novelty, inventive step and support dominate.

## 22. FTO and design-around comparison

No concept is FTO-cleared.

- **OpenBraille:** design away from active electromagnetic/capture-layer structures and generic modular claims; retrieve and chart `5559/CHE/2014`; avoid assuming expired art is a block while retaining it as prior art.
- **VibeGuard:** avoid exact Mitsubishi amplitude/phase Mahalanobis, Valqua dual-distance prognosis, Rolls-Royce speed-frequency noise-floor and Tractian remote reconstruction/retraining sequences; commercial portfolio coverage remains incomplete.
- **TrueMoist:** avoid CN replacement-output-equivalence conditioning, TCS image/rugged-reference health pipeline, claimed event recalibration and custom multi-frequency/live-salinity structures; official IN/CN/EP status requires counsel-grade review.

OpenBraille and VibeGuard have comparable unresolved posture; TrueMoist has the most directly relevant active-family risk for its proposed later center.

## 23. Evidence accessibility and experimental burden

1. **OpenBraille:** easiest decisive patent experiment. One-dot hardware, spare servos and ground truth can falsify the route quickly. Practical-scale proof remains later.
2. **VibeGuard:** easiest semester MVP but harder decisive patent evidence. A dual rig is manageable, yet real attribution requires independent labels, remounts and a field-like site.
3. **TrueMoist:** evidence is controllable but labor intensive. The semester can produce Level-1 data and a two-probe pilot; credible transfer needs a probe population and lots.

## 24. Claim usefulness and narrowness risk

- **OpenBraille:** a surviving claim could be narrow but commercially meaningful if it covers reliable refresh of heterogeneous low-cost actuator channels without per-dot position sensors. Narrowness risk: medium-high.
- **VibeGuard:** a claim coupling ambiguity, quarantine, remount validity and source attribution could be useful for one-node deployments. It may become a narrow protocol tied to labelled commissioning. Narrowness risk: high.
- **TrueMoist:** a claim may narrow to a specific reference challenge, transfer mapping and contamination gate for a probe class. Close art may force highly specific physical conditions. Narrowness risk: very high.

## 25. Optimistic/base/pessimistic simulation

These are conditional decision-support bands, not legal probabilities.

| Concept | Optimistic case | Base case | Pessimistic case |
|---|---|---|---|
| OpenBraille | **25–40%** chance the D11 evidence becomes counsel-worthy: state inference is reliable, full integration beats ablations, practical-scale relationship survives and search leaves useful scope | **10–25%**: engineering reliability improves, but claim scope is narrow or obviousness remains difficult | **<10%**: current measures servo effort rather than pin state, simple calibration explains benefit, or closer claims defeat route |
| VibeGuard | **20–35%**: controlled and field-like data show materially lower wrong-source alarms at useful coverage, with remount-safe update control | **10–20%**: strong publication result and prototype, but field evidence or obviousness prevents filing-quality claim | **<10%**: neighbour and mount variation swamp target information, abstention hides errors, or independent labels/site access fail |
| TrueMoist | **15–30%**: multi-unit/lots show transfer and validity benefit beyond two-point affine plus generic gate | **5–15%**: Level-1 paper succeeds, but transfer path remains conventional or too narrow | **<5%**: metrology/packing fails, simple baselines match, or close art leaves no useful scope |

## 26. Kill-probability and decision-reversal analysis

| Concept | Estimated patent-path kill probability | Risk surviving claim is commercially too narrow | Primary reversal variable |
|---|---:|---:|---|
| OpenBraille | **60–75%** | **55–75%** | Whether current-plus-datum can verify actual pin state and produce a cooperative effect |
| VibeGuard | **65–80%** | **60–80%** | Whether target-specific information survives independently varying interference and remounts |
| TrueMoist | **75–90%** | **70–85%** | Whether the full mechanism beats two-point affine transfer plus generic validity gating across units/lots |

The overall decision reverses to immediate VibeGuard if OpenBraille misses any gate threshold. It reverses toward OpenBraille if the gate passes strongly and a rapid claim-focused search finds no close integrated claim. TrueMoist becomes fallback research only if VibeGuard cannot obtain labels/site access and OpenBraille fails mechanically.

## 27. Best semester-build candidate

**VibeGuard.** Base Semester Build Score: **90.2/100**. It is inexpensive, visually clear, technically divisible and can meet its legitimate Level-1 scope without a large mechanical tolerance stack, human tactile access or an oven-based 72-run campaign. The team must pre-register quantitative success criteria and not present Level 1 as target attribution.

## 28. Best post-MVP patent-development candidate

**OpenBraille D11, conditionally.** Base Patent-Path Score: **69.8/100**, versus VibeGuard 66.5 and TrueMoist 59.9. Its advantage is not prior-art distance; it is specificity, direct MVP connection and accessibility of decisive experiments. Current classification remains Track D until the gate passes, then prospective Track B subject to search/IPR review.

## 29. Best overall Project mC choice

**Run one named short feasibility gate before selecting.** The current integrated-score leader is VibeGuard, but the gate can resolve OpenBraille’s strategically decisive uncertainty in 10 days for modest cost. This is preferable to selecting OpenBraille on speculation or selecting VibeGuard without testing the only near-term physical invention route.

## 30. Runner-up and deprioritized concept

**Runner-up/fallback:** VibeGuard. Select it immediately if the OpenBraille gate fails.
**Deprioritized for patent-first selection:** TrueMoist. Preserve all Level-1 plans and consider it for a rigorous publication or later institutional research study.

## 31. First 12-week execution plan

### Days 1–10: selection gate

- Freeze public baseline descriptions and open confidential invention logs.
- Build the OpenBraille one-dot gate setup; use three servos and two reassemblies.
- Lock thresholds before held-out data.
- Day 10 decision: pass → OpenBraille; fail → VibeGuard.

### Weeks 3–4: procurement and architecture freeze

**If OpenBraille selected:** procure six servos, power rail, FDM materials and instrumentation; freeze active retraction, datum geometry and safety limits.
**If VibeGuard selected:** procure authentic ADXL345/ESP32, motor/rig materials, rigid bracket and wiring; freeze ODR/bandwidth after measured signal review.

Team allocation for either path:

- technical lead: architecture, safety and integration;
- firmware/data lead: acquisition/control, immutable logs and analysis;
- mechanical/rig lead: fixtures, repeatability and ground truth;
- learner: scripted tests, labels, inventory and repeat runs;
- presenter/support: public-safe demo, source ledger and version control.

### Weeks 5–6: minimum demonstrable system

- OpenBraille: full six-dot macro cell, fixed-PWM baseline, power and travel measurements.
- VibeGuard: stable Level-1 acquisition, repeatable normal/abnormal rig and RMS+persistence baseline.

### Weeks 7–8: quantitative validation

- Lock evaluation protocol and held-out runs.
- OpenBraille: calibration/datum/current verification plus fixed and partial baselines.
- VibeGuard: time/FFT/Mahalanobis baselines, mount repeats and resource profiling.

### Weeks 9–10: robustness and ablation

- OpenBraille: induced jams, replacements, reassembly, all pattern transitions, 1,000-cycle screening.
- VibeGuard: add controlled interferer only if Level 1 is stable; quantify neighbour confusion and test preliminary Unknown/quarantine logic.

### Weeks 11–12: demo, decision and documentation

- Freeze firmware, BOM, schematics/CAD, SOP, raw data and negative results.
- Prepare a public demo containing only frozen architecture and generic known techniques.
- Hold institutional IPR review before disclosing exact later mechanism, thresholds or results.
- Decide filing-search continuation versus publication-only route.

## 32. Later invention-development plan

**OpenBraille after a pass:** 3,000–10,000 transition confirmatory dataset; full ablations; practical-scale single-dot coupons; three independent builds; multiple actuator lots; contamination/load/temperature testing; claim-focused search including Indian file; later six-dot practical geometry and approved Braille-reader evaluation.

**VibeGuard fallback/later path:** dual-rig randomized states; at least three remounts and five sessions; held-out day/remount; strongest baselines and ablations; real or field-like site with independent labels; counsel-grade search on exact update/abstention/remount sequence.

**TrueMoist retained research:** complete Level 1 first; then 6–12 probes, ≥2 lots, ≥3 preparation batches, repeated remounts, contamination and ageing proxies, full transfer baselines and later soil classes. Do not add live EC or multi-frequency hardware merely to rescue patent scoring.

For any selected path: refresh prior art only after the mechanism is frozen; prepare a human-authored invention disclosure; identify target jurisdictions; obtain institutional ownership/inventorship review; then commission professional novelty/FTO work and make a filing/no-filing decision. If filing is not justified, preserve a publication-quality dataset and negative results.

## 33. Confidentiality and institutional IPR plan

Publicly discuss only the frozen architecture, generic known algorithms, course requirements and high-level test goals. Keep confidential:

- exact OpenBraille datum geometry, signatures, retry/fault logic, thresholds and ablations;
- VibeGuard attribution, source-confidence, quarantine/promotion, remount and abstention logic;
- TrueMoist physical reference challenges, transfer mappings, contamination gates and validity states;
- unpublished data, negative results, parameter values and contributor chronology.

Maintain dated lab notebooks, Git commit history, CAD revisions, raw-data hashes, decision logs and contributor statements. AI suggestions are not inventorship. Human contributors must identify who conceived each claim-relevant element and who reduced it to practice. Obtain institutional approval before poster, repository, paper, video or competition disclosure.

## 34. Final recommendation

**Run the OpenBraille D11 Physical-State Observability Gate before selecting.**
**Current OpenBraille MVP Track:** D as a patent direction; strong semester prototype.
**Prospective later Track:** B only if the 10-day gate passes and claim-focused/IPR review preserves a meaningful distinction.
**Confidence:** medium.
**Primary kill condition:** inability to verify actual pin state with ≥95% sensitivity/specificity and zero silent wrong states in 500 held-out transitions, or failure to outperform fixed-PWM control by ≥30%.
**Fallback:** select VibeGuard, current Track C, and execute a disciplined Level-1 build while retaining source-attribution work as later research.
**Deprioritized concept:** TrueMoist for patent-first selection; retain for Level-1 engineering/publication.

No project or enhancement is represented as certain to receive a patent.

## 35. Unresolved questions

1. Can the OpenBraille current measurement distinguish actual tactile pin contact/state from internal servo effort across units, reassembly, voltage and wear?
2. What official file, claim scope and current legal status apply to Indian application `5559/CHE/2014`?
3. What owner-approved quantitative tactile-identification threshold and participant protocol will govern OpenBraille?
4. What owner-approved Level-1 accuracy/false-alarm criteria will govern VibeGuard?
5. Can VibeGuard obtain safe independent target/interferer labels and a field-like site within the later programme?
6. Is oven/scale access guaranteed for the full TrueMoist schedule, and can measured throughput support 72 independent runs?
7. Which jurisdictions and commercialization acts define the eventual FTO search?
8. Which exact human contributions, if any, survive the experiments as claim-relevant inventive concepts?

## 36. Source and verification log

### Governing and common authority

- `00_READ_FIRST_Project_mC_Final_Adjudication_Instructions(2).md`
- `01_Project_mC_Decision_Register_v1.2(2).md`
- `02_Phase3C_Portfolio_Closure_Memo_Approved(2).md`
- `03_Concept_Evidence_Matrix(3).md`
- `04_Uncertainty_and_Test_Register(2).md`

### Selected analytical evidence

- `05_OpenBraille_Synthesis_Work_Max(2).md`
- `06_OpenBraille_Synthesis_Valid_Secondary(2).md`
- `07_VibeGuard_Synthesis_Work_Max(2).md`
- `08_VibeGuard_Synthesis_Standard_High(2).md`
- `09_TrueMoist_Synthesis_Max(2).md`
- `10_TrueMoist_Synthesis_High_Deep_Research(2).md`

### File-control-only context

- `99_EXCLUSION_AND_PROVENANCE_REGISTER(2).md`

### Verification performed

- physical attachment count and readability;
- byte and SHA-256 verification against the provenance register for controlled files 00–10;
- heading/completeness audit of all six selected syntheses;
- explicit concept-fidelity review;
- reconciliation of the OpenBraille Track D/B disagreement without voting;
- weighted score calculation and sensitivity analysis;
- no excluded synthesis, supplementary TrueMoist audit, prior-chat context or prior adjudication output used.

No independent web result was needed to convert an unresolved status into a factual conclusion. Where the attached syntheses could not establish official legal status or claim scope, the issue remains expressly unresolved rather than guessed.
