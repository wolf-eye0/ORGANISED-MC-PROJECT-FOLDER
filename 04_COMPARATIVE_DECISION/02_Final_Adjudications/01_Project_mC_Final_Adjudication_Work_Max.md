# Project mC Final Cross-Concept Patent-Path Adjudication

**Evidence cut-off:** 1 August 2026  
**Adjudication date:** 3 August 2026  
**Decision character:** engineering and patent-strategy support, not legal advice, claim construction, infringement analysis, patentability clearance, or FTO clearance. No project or enhancement is represented as certain to receive a patent.

## 1. Executive decision

| Required decision | Decision | Controlling reason |
|---|---|---|
| Best three-month semester-build candidate | **VibeGuard** | It has the simplest physical build, lowest base BOM, strongest fit to the team's embedded/software skills, clearest live state-change demo, and the least dependence on fabrication or laboratory metrology. |
| Best post-MVP patent-development candidate | **TrueMoist** | Its proposed physical-reference-bound replacement/remount transfer mechanism is the most specific later mechanism whose decisive experiments remain substantially under the team's control. It still has high obviousness and FTO-search risk and is only Track C. |
| Best overall Project mC choice now | **Run one named short feasibility gate before selecting.** | VibeGuard leads the integrated base score at all three weightings, but only by 0.3 points over TrueMoist at 30% build / 70% patent. That lead depends on target-specific information surviving interference and on obtaining independently labelled field access. |
| Runner-up / fallback | **TrueMoist** | If the VibeGuard gate fails, TrueMoist has the strongest remaining combination of a rigorous MVP, high publication value, a specific later mechanism, and experiments not dependent on an external industrial site. |
| Prototype/publication-only or deprioritized concept | **OpenBraille** | Retain as a strong accessibility/mechatronics prototype and publication path. Deprioritize it for patent-first selection unless the D11-type current-ground-truth and practical-scale gates later pass. |

### Named pre-selection gate

**Gate:** *VibeGuard Level-2A Signal-and-Access Gate (VG-SAG)*  
**Deadline:** **13 August 2026, 18:00 IST**.  
**Decision:** pass every criterion below or select TrueMoist instead.

1. Use one target motor and one independently controlled interferer on a shared/coupled base, with the product architecture remaining one rigidly mounted ADXL345-class sensor on the target.
2. Collect target normal/abnormal × interferer off/normal/abnormal data in at least three independently started sessions on three days, with a documented remount before each session. Use at least ten non-overlapping analysis blocks per state cell per session; treat sessions/remounts—not windows—as the independent evidence units. Hold out one complete day/remount from all model and threshold selection.
3. Compare RMS-plus-persistence, ordinary FFT/band features, ordinary Mahalanobis, and static spectral subtraction against a preliminary source-conditioned/ambiguity-gated implementation.
4. On the untouched day/remount, achieve **at least 30% relative reduction in target-attribution error or false target-fault alerts** versus the strongest conventional comparator, with **no more than a five-percentage-point worsening in missed target faults** and **at least 80% decision coverage**. Report all conditions; no post-hoc threshold change or window leakage is allowed.
5. Demonstrate the selected pipeline locally on the ESP32 with no acquisition-block loss in the locked run and no saturation or unreported alias/bandwidth failure.
6. Obtain written, named access in principle to at least one dense-machine or field-like site, within 16 weeks, where target and interferer states can be independently labelled and remounting can be tested safely.

These are project-selection thresholds, not patentability probabilities or field-performance claims. A pass selects **VibeGuard** for Project mC, with the frozen MVP treated as **Track D as a patent target** and the later attribution mechanism as **prospective Track C**. A fail selects **TrueMoist**, subject to its mandatory Week-1 oven/scale and probe-repeatability gates; if those also fail, no concept presently justifies patent-first selection and VibeGuard should continue only as the strongest semester prototype.

## 2. Input inventory and provenance

The stop condition was not triggered. Exactly **12 user attachments** were present and readable. Each attachment's byte count and SHA-256 matched the provenance register. The six synthesis files have six distinct hashes and are complete, concept-faithful records rather than duplicates or partial exports.

| Controlled attachment | Role | Bytes | SHA-256 | Result |
|---|---|---:|---|---|
| `00_READ_FIRST_Project_mC_Final_Adjudication_Instructions.md` | Governing instruction | 16,558 | `1a06d628347b4ec533a6ccea8f44b933de1295b29d9f4b407a028947c8b34ddc` | Read first; complete and governing |
| `01_Project_mC_Decision_Register_v1.2.md` | Authority 1 | 56,071 | `9678c5072d86ef38e48372f940ec91396b7ac7bcbeed0124ac8e2485307f408c` | Readable; v1.2 confirmed |
| `02_Phase3C_Portfolio_Closure_Memo_Approved.md` | Authority 2 | 3,149 | `3c6e6f568c06099251b4b71d4f35cf668ee23a40c8214c95e4a12fe36cf4845a` | Readable and approved |
| `03_Concept_Evidence_Matrix.md` | Authority 3 / common evidence | 19,491 | `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975` | Readable |
| `04_Uncertainty_and_Test_Register.md` | Authority 4 / common evidence | 22,484 | `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b` | Readable |
| `05_OpenBraille_Synthesis_Work_Max.md` | OpenBraille synthesis 1 | 113,903 | `d92dbfbbbdbd4c49e9eaac9fab01e0d2a7db6d986c81d33ee65223710dd42eb1` | Complete; 26 sections; faithful |
| `06_OpenBraille_Synthesis_Valid_Secondary.md` | OpenBraille synthesis 2 | 86,337 | `b9fefadf621f014dc621ef9836ae11b80c05a0227f768c53c11ec1358fc8a09b` | Complete; 26 sections; faithful |
| `07_VibeGuard_Synthesis_Work_Max.md` | VibeGuard synthesis 1 | 111,826 | `f61955b09b976a4c445fcdddbc40aada02cae204302876dbfc7cf1825b8cdf72` | Complete; 26 sections; faithful |
| `08_VibeGuard_Synthesis_Standard_High.md` | VibeGuard synthesis 2 | 70,134 | `b32a41ce9f0a3fe3ab17e55657bd14796cc77b401852b730254f1ac580b2adc4` | Complete; 26 sections; faithful |
| `09_TrueMoist_Synthesis_Max.md` | TrueMoist synthesis 1 | 84,487 | `f43847c672ca9b132a7ef6219a9ce00deb8f0ab657c0bda6a7ed3a930a697900` | Complete; 27 sections; faithful |
| `10_TrueMoist_Synthesis_High_Deep_Research.md` | TrueMoist synthesis 2 | 70,087 | `ddf421678c6f5dbafd7e2d61db82a4b7c1d8c3d817afb4341538ec98f4d91505` | Complete; 27 sections; faithful |
| `99_EXCLUSION_AND_PROVENANCE_REGISTER.md` | File control and reliability context only | 11,518 | `b56ad079dacaf594fc80307d0a1ac4424c2493e11039290fe2a5666dbd4abfef` | Readable; not used as technical evidence |

### Explicit provenance resolutions

- The four common governance/evidence files are all present: Decision Register v1.2, approved closure memo, evidence matrix, and uncertainty/test register.
- Each concept has exactly two selected syntheses.
- The OpenBraille filename crossing is resolved: the concept-faithful secondary/Deep Research record originally carried `OpenBraille_Patent_Synthesis_ChatGPT_Standard_High_no_deeprsearch.md` and is controlled here as file 06.
- The file originally named `OpenBraille_Patent_Synthesis_ChatGPT_Deep_Research.md` was the moving-roller/encoder/RAMPS concept swap and is absent.
- The VibeGuard High + Deep Research software-security/configuration-scanner concept swap is absent.
- The supplementary TrueMoist Work Max web audit is absent and was neither quoted nor inferred.
- Decision Register v1.1 is absent.
- No selected synthesis is missing, unreadable, duplicated, physically partial, or concept-swapped.
- The provenance register was used only to control identity, completeness, exclusions, and the filename crossing. Its reported verdicts were not treated as technical evidence.

## 3. Authority and constraints

The applied authority order was: Decision Register v1.2; approved Phase 3C closure memo; Concept Evidence Matrix; Uncertainty and Test Register; audited syntheses; and one narrow independent claim-text check where the selected VibeGuard syntheses materially disagreed.

| Binding constraint | Adjudication treatment |
|---|---|
| Up to three months | Semester score measures a complete demonstrable MVP within 12 weeks; later patent evidence is scored separately. |
| Preferred spend ≤₹3,000; absolute ceiling ₹5,000 | A concept receives no rescue from patent potential if the semester build exceeds the ceiling. Later work must have a separate budget. |
| Five members: three strong, one learner, one presenter/support | Critical mechanical, metrology, DSP, or statistical work stays with the three strong members; bounded logging, state-machine, test and documentation work goes to the other two. |
| Arduino IDE / embedded-board compatibility | ESP32-WROOM-32/S3 and fixed local inference satisfy the course direction. |
| Low-power components and USB interface/sample | All three frozen systems can provide USB data/control. OpenBraille requires external 5 V servo power rather than USB bus power. |
| Cybersecurity relevance | Helpful only where genuine; it is not a mandatory ranking factor and cannot be manufactured through labels. |
| Strong live demonstration | Scored independently from patent potential. |
| Patent-first but buildability-constrained | Default integration is 40% semester build / 60% patent path, with 50/50 and 30/70 sensitivity. |

The closure memo's earlier language—OpenBraille having the highest physical-invention ceiling, VibeGuard the strongest live DSP demo, and TrueMoist the lowest engineering risk—was treated as project context, not as a conclusion that overrides the completed patent-evidence records.

## 4. Concept-fidelity audit

| Concept | Required architecture | Selected records | Fidelity finding |
|---|---|---|---|
| OpenBraille | Six SG90-class servos; direct PWM; one eccentric cam/follower/vertically translating pin per dot; macro FDM cell; active cam retraction unless a physical return is proven | Files 05 and 06 | **Pass.** Both preserve the six-servo/cam mechanism, correct the unsupported passive-return assumption, and treat D11 as an enhancement hypothesis. References to rollers, shared setters, or electromagnetic alternatives occur only as excluded/crowded art, not as the project architecture. |
| VibeGuard | One rigid ADXL345-class accelerometer; ESP32; local features; triggered FFT; RMS-plus-persistence minimum; prospective Mahalanobis; RGB; isolated-motor Level 1; separate Level 2 attribution | Files 07 and 08 | **Pass.** Both preserve passive single-node vibration monitoring and explicitly separate Level 1 from target attribution. Neither substitutes software security, active cancellation, a wearable, a sensor array, cloud/RUL, or an audio system. |
| TrueMoist | Genuine analog capacitive probe; DS18B20; controlled salinity-treatment code; ADS1115/ADC gate; fixed M0/M1/M2; one soil; 72 physical runs; gravimetric truth | Files 09 and 10 | **Pass.** Both preserve the validated 72-run architecture and treat transfer/health as Level 2. Neither converts the MVP into live EC, irrigation control, multi-soil, custom multi-frequency hardware, TinyML, or online learning. |

No concept was compared using another concept's speculative redesign. Each frozen MVP is compared with frozen MVPs; each later mechanism is compared with later mechanisms.

## 5. Synthesis reliability audit

Reliability is assigned to the selected synthesis as an evidence record. It is not a ranking of models and is not a vote.

| Synthesis | Current-MVP verdict | Later-route verdict | Audit of fact, inference, contradiction and status | Reliability |
|---|---|---|---|---|
| OpenBraille Work Max | Frozen MVP is not a credible invention; Track D | D11 is experimental Track D now; reopen as Track B only after official-file/search, fast-current, ablation, robustness, 3,000-transition and practical-scale gates | Strongest separation of claims from specifications and database status from official status. Verified art supports servo/cam, guided pins, calibration/stops and generic current diagnostics. The claimed D11 cooperative effect is explicitly inference. Indian `5559/CHE/2014` and live national status remain unresolved. No internal concept contradiction. | **High** |
| OpenBraille valid secondary | Frozen MVP is not the invention | Conditional bounded Track B, 42% confidence | Complete and faithful, with useful physical-control definition. Its Track-B uplift is more optimistic than its own admissions: final claim-language search, non-additive effect and practical-scale support are missing. Its suggestion that INA219/INA226-class sensing may support transient signatures is weaker than the fast-shunt requirement in Work Max. FTO/status remain provisional. | **Medium** |
| VibeGuard Work Max | Frozen feature stack is conventional; no filing on it | Track C label-aware, contamination-protected target attribution | Strong claim-level correction of Tractian and other families; clear Level-1/Level-2 boundary; does not invent acceptance numbers. Verified patents/literature support all component techniques. Novelty of the coordinated loop is inference and field evidence is absent. National status and IN/CN scope remain unresolved. | **High** |
| VibeGuard Standard High | Frozen MVP is a research platform, not invention | Track C integrated target-fingerprint/quarantine/abstention/remount method | Complete and faithful with a strong experiment plan. It underweights KCF US 10,873,791's dependent FFT-baseline/rebaseline claims by treating the family mainly as network compression, and its 30% performance threshold is a proposed rule rather than project authority. Some family/status entries are less fully verified. | **Medium** |
| TrueMoist Max | Frozen MVP is Track D as a patent direction | Track C composite transfer/validity mechanism | Strongest claim-to-experiment and physical-burden analysis; distinguishes grant claims from broader publications, and identifies replacement, health, event-calibration and validity art. Its later mechanism and any unexpected interaction remain inference. Indian, CN and national-stage status gaps are candidly unresolved. | **High** |
| TrueMoist High + Deep Research | Frozen MVP has low patent value | Track C physical-reference-bound transfer/acceptance | Complete, faithful and conservative; correctly rejects generic Mahalanobis/OOD/abstention novelty and requires multi-unit later evidence. Some national statuses and the exact wider sensor-validity search remain incomplete, but no internal contradiction changes the result. | **High** |

### Disagreement adjudication

- **OpenBraille:** the records disagree because they place the Track-B threshold at different stages. The secondary treats a specific, testable integrated mechanism as enough for conditional Track B; Work Max requires non-additive physical evidence, fast sensing, robust hold-out performance, Indian/control-art resolution and practical-scale transfer first. The stricter burden controls. OpenBraille remains current Track D, with only a conditional future B reopening.
- **VibeGuard:** both reach Track C. The KCF conflict was independently checked: claim 1 is a network-compression method, but dependent claim 4 expressly performs FFT magnitude-baseline subtraction and claim 9 expressly nullifies/regenerates a baseline when the spectrum deviates. It is therefore not a literal claim read on local-only VibeGuard without the parent networking/compression limitations, but it is strong disclosure/obviousness evidence against treating spectral subtraction or controlled rebaselining as the invention.
- **TrueMoist:** both reach the same Track-C boundary. Differences are formulation, not outcome: Max emphasizes the full contamination-protected transfer composite; High + Deep Research emphasizes physical-reference-bound transfer and acceptance. They describe the same later physical problem and do not create two votes.

## 6. Normalization method

Two records were created per concept:

- **Frozen MVP:** only the authority-approved semester architecture, deliverable, validation and current patent posture.
- **Post-MVP path:** only the strongest connected later mechanism, its experiments, burden, claim usefulness and kill conditions.

Tracks are normalized as follows: **A** = credible invention already embodied; **B** = bounded near-term invention-development path; **C** = connected but later-semester path; **D** = no credible present patent path. On this normalization, all three frozen MVPs are Track D as patent targets. VibeGuard and TrueMoist have prospective Track C paths; OpenBraille has a Track-D experiment that may reopen to B only after stringent gates.

Scores use 0–5, where 0 is unusable and 5 is unusually strong under the owner constraints. Each cell shows **low / base / high**. These are conditional planning scenarios, not statistical confidence intervals. Weighted score = Σ(score ÷ 5 × factor weight). Low and high totals apply all downside or upside assumptions together and therefore bound the narrative rather than predict frequency.

Patent comparison separates novelty, inventive step, eligibility, FTO, enablement/support and useful claim scope. Exact parts, low price, absence of cloud/live EC, algorithm labels, sample count and aggregation of known steps receive no independent patent reward.

## 7. OpenBraille frozen-MVP fact sheet

| Item | Normalized fact |
|---|---|
| Exact architecture | One macro six-dot cell at about 7 mm pitch and 1.5 mm protrusion; six SG90-class servos; direct ESP32 PWM; individual eccentric cams, followers and guided vertically translating pins; FDM frame/guides/cams; external 5 V/2 A rail and 1,000 µF capacitor; active cam retraction unless a usable physical return is proven. |
| Three-month deliverable | A functioning cell that maps host characters to repeatable tactile patterns, raises/retracts all dots, records faults, survives the approved cycle tests and supports a blinded tactile protocol if participant/approval access exists. |
| Budget | Authority estimate ₹2,060–₹2,850 for the frozen MVP. |
| Validation | Single-dot-first M1–M8 sequence; power/current checks; ≤0.1 mm position variance over 100 cycles; ≥1,000 actuations; full-pattern/end-to-end tests; owner-approved tactile-identification protocol. |
| Primary engineering risk | FDM tolerance/friction and cam/pin return, followed by six-servo power peaks and unconfirmed tactile performance. |
| Current patent verdict | Useful prototype; no credible invention in the frozen combination. |
| Strongest prior art | US8483018B2 rotary raised surface/guided pins/servo disclosure; US20130017516A1 independent tactile pins; micro-servo/cam papers and public motor/cam projects; Freedom/Enhanced Vision stop, capture and modular lineages. |
| Eligibility / FTO | Physical apparatus eligibility is relatively favorable, but it does not cure obviousness. Indian `5559/CHE/2014` is an unresolved close FTO/search issue; recent modular/capture and generic motor-diagnostic claims require design-specific charts. No clearance. |
| Demo value | Very high visually and tactilely if reliable; macro scale is honest educational proof, not standard-Braille product proof. |
| Publication value | Good for accessibility engineering, repeatability, tactile validation, current-state inference limits or negative results. |
| Current Track | **D as a patent target.** |

## 8. OpenBraille post-MVP patent-path fact sheet

| Item | Normalized fact |
|---|---|
| Proposed mechanism | D11-type mechanically referenced per-dot calibration plus isolated shared-current measurement, physical ground-truth correlation, completed/jammed/unknown classification, bounded retry, fault isolation and measured-current sequencing. |
| Relationship to MVP | Direct extension of the same servo/cam/pin channel; no moving roller, shared carriage, electromagnetic cell or other substituted architecture. |
| Closest patent/NPL art | Stops/capture/tolerance art in US12080182/US7410359/Freedom lineages; servo/cam art; generic motor current/position/fault diagnostics; micro-servo calibration; unresolved `5559/CHE/2014`. |
| Claimed physical effect | A common datum creates a repeatable terminal event; calibrated minimum overdrive plus isolated current measurement should reduce silently wrong tactile states, height variance and current peaks with bounded latency. |
| Required experiments | Fast-shunt sensing with independent optical/height truth; global-PWM, datum-only, calibration-only, sensing-only and full-system ablations; servo swaps, rebuilds, voltage, friction, temperature and finger-load perturbations; 3,000 held-out transitions; practical-scale coupon. |
| Units/samples/sites | Six installed plus at least two substitute servos for early work; three rebuilds; ≥600 normal + 600 induced-fault events for development/hold-out in the conservative plan; ≥3 practical-scale coupons and later multiple actuator lots; no external industrial site required. |
| Additional hardware/cost | Fast shunt/current amplifier, optical or height ground truth, load/temperature fixture and practical-scale fabrication. Early overlay roughly ₹450–₹1,100; credible later work roughly ₹5,000–₹20,000. |
| Time beyond semester | Approximately 4–9 additional months for practical scale, multiple builds and 10,000–100,000-cycle evidence. |
| Claim usefulness if successful | Potentially useful but likely narrow: low-cost tactile-channel state verification/recovery tied to a specific datum and sensing sequence. Macro-only or SG90-specific scope would be commercially weak. |
| Patent risks | Novelty unresolved; obviousness high because every component is known; eligibility low-to-medium when physically anchored; FTO unresolved, especially India; enablement requires practical-scale proof. |
| Strongest baseline | Calibrated open loop with fixed one-at-a-time sequencing, plus datum-only and direct-sensor controls—not an intentionally weak global-PWM baseline alone. |
| Kill condition | Shared current cannot verify actual tactile state on untouched data; any silent wrong state occurs in 3,000 transitions; no non-additive benefit; effect is unit/build-specific; or practical-scale transfer fails. |
| Prospective Track | **D now; reopen to B only if every search, interaction, robustness and scale gate passes.** |

## 9. VibeGuard frozen-MVP fact sheet

| Item | Normalized fact |
|---|---|
| Exact architecture | One rigidly mounted ADXL345-class accelerometer over SPI to ESP32-WROOM-32/S3; DC removal → Hann → continuous time features → triggered FFT; RMS-plus-persistence minimum; prospective Mahalanobis normal-space score; band-limited/static baseline treatment; RGB local states; isolated 12 V motor/fan with safe eccentric mass. |
| Three-month deliverable | Stable Level-1 acquisition and local Normal/Abnormal classification on controlled normal versus induced-imbalance conditions, with USB logging, RGB output, held-out sessions and measured compute/memory/latency. |
| Budget | ₹1,700–₹2,200 for the ADXL345 MVP; a controlled two-motor scaffold may approach ₹3,000–₹5,000. |
| Validation | Independently repeated normal/abnormal runs; stable eccentric-mass fixture; rigid-mount/remount records; RMS/persistence, FFT/bands, Mahalanobis and static subtraction comparisons; owner-approved quantitative acceptance protocol. |
| Primary engineering risk | Data validity: rigid coupling, sensor authenticity/bandwidth, repeatable fault injection, thresholds and leakage—not basic assembly. |
| Current patent verdict | Conventional monitoring aggregation; frozen system is an experimental platform, not the invention. |
| Strongest prior art | KCF US10873791 dependent FFT-baseline/rebaseline claims; MHI US11334414 vibration Mahalanobis; Rolls-Royce US9874472 state/speed-conditioned spectra; Valqua dual-Mahalanobis bands; single-sensor/multi-motor NPL. |
| Eligibility / FTO | Physical sensing helps, but a generic score/alert has meaningful US/EPO/India software-mathematics risk. Several active industrial families require final code/claim charts; local/no-cloud operation is not FTO clearance. |
| Demo value | Highest: an immediate motor-state change, local LED response and live spectrum/features are easy to understand. |
| Publication value | High for a reproducible low-cost benchmark, mounting/remount study, embedded profiling or negative mixed-source result. |
| Current Track | **D as a patent target.** |

## 10. VibeGuard post-MVP patent-path fact sheet

| Item | Normalized fact |
|---|---|
| Proposed mechanism | Independently labelled target/interferer commissioning; target-conditioned and interference fingerprints; separate target-abnormality and ambiguity evidence; calibrated abstention; contamination-protected update admission/rollback; remount transfer or invalidation; speed/load conditioning where justified. |
| Relationship to MVP | Direct: the permanent product remains one target-mounted accelerometer with local ESP32 processing and local alert. Temporary references establish experimental truth only. |
| Closest patent/NPL art | KCF baseline subtraction/rebaseline; Rolls-Royce state/speed fingerprints; MHI/Ford/Valqua normal-space distance; US7421349 source-related bearing signatures; Nguyen single-sensor BSS; Seitz single-sensor multi-motor state inference; standard reject/drift/remount practice. |
| Claimed physical effect | Fewer wrong-source target alarms and less contaminated learning at useful decision coverage after neighbour changes and remounts. |
| Required experiments | Level 2A factorial target/interferer states, held-out days/remounts, speed/load cells, contamination during update, baseline comparisons and critical ablations; then independently labelled Level 2B field deployment. |
| Units/samples/sites | One permanent product sensor; two motors for bench; at least five independent sessions/remounts across at least three days in the synthesis planning floor; at least one authorised dense-machine site and preferably a replication installation for useful general claims. |
| Additional hardware/cost | Second motor/interferer, repeatable mounts, guards, tachometer/current/reference instrumentation for ground truth. Semester scaffold can remain within ₹5,000; later field/site/reference cost is unresolved and separately funded. |
| Time beyond semester | Roughly 4–6 additional months for initial authorised field work and 6–12 months for multi-installation replication. |
| Claim usefulness if successful | Narrow-to-moderate: a source-validity/update-control loop for a single mounted node. Scope that collapses to generic confidence, Mahalanobis or drift management is weak and easy to design around. |
| Patent risks | No exact complete-loop anticipation established; obviousness very high; eligibility medium-to-high if claimed functionally; FTO medium/uncertain across industrial portfolios; enablement requires labelled field evidence. |
| Strongest baseline | Strongest of RMS/persistence, FFT/bands, ordinary Mahalanobis, static subtraction, naive adaptive baseline, full recalibration and forced binary classification. |
| Kill condition | No held-out wrong-source improvement; benefit comes from excessive abstention or extra labels/capacity; fault enters baseline; remount yields confident errors; no authorised independent field truth; or closer art covers the enabled loop. |
| Prospective Track | **C.** |

## 11. TrueMoist frozen-MVP fact sheet

| Item | Normalized fact |
|---|---|
| Exact architecture | Genuine analog capacitive probe plus nearby DS18B20; controlled NaCl treatment code per dry-soil mass; ESP32-WROOM-32; ADS1115 retained only if paired Week-1 data justify it; hardened soldered analog path; M0 raw, M1 linear and M2 ridge second-order models trained offline and fixed locally; one homogeneous soil; USB CSV. |
| Three-month deliverable | Complete 72-run dataset and local compensated estimate: 4 moisture × 3 temperature × 2 salinity × 3 independent physical replicates; replicates 1–2 train/select and replicate 3 remains untouched. |
| Budget | ₹1,790–₹3,440 with institutional oven/scale access; under ₹5,000 with controlled contingency. Buying an oven is outside scope. |
| Validation | Dry-basis gravimetric truth at 105 ± 5 °C to constant mass; compensated RMSE ≥20% lower and MAE ≥15% lower than M0 on untouched replicate; major-subset MAE not >10% worse; absolute and subset errors reported. |
| Primary engineering risk | Measurement-chain and throughput validity: probe repeatability, packing/reinsertion, oven/scale access, salinity effect and completion of 72 independent runs. |
| Current patent verdict | Scientifically strong but predictable combination; the 72-run design generates evidence and is not itself invention. |
| Strongest prior art | CN108414007 temperature-dependent nonlinear compensation; CN111103333 correction metadata; extensive SEN0193 calibration NPL; Senviro/Bosch self/event calibration; custom moisture/salinity hardware families. |
| Eligibility / FTO | Regression and categorical metadata are vulnerable if claimed as mathematics. Frozen commodity hardware has lower apparent overlap than custom multi-frequency/live-EC systems, but CN/India/EP status and final claim charts remain unresolved. No clearance. |
| Demo value | Good but less immediate: live USB output plus held-out reference/raw/compensated comparison and clear error reduction. |
| Publication value | Highest: rigorous metrology, grouped validation, ADC-value study, temperature/salt effects and negative results remain publishable even if patentability fails. |
| Current Track | **D as a patent target.** |

## 12. TrueMoist post-MVP patent-path fact sheet

| Item | Normalized fact |
|---|---|
| Proposed mechanism | Bind donor calibration/provenance to a probe; apply sparse trusted physical reference challenges after replacement/remount; derive a bounded transfer; evaluate residuals under perturbations; accept only within a transfer-specific validity state; block contaminated updates; abstain/fallback otherwise. |
| Relationship to MVP | Direct: reuses the same probe class, temperature/salt perturbations, gravimetric metrology, fixed local inference and one-soil evidence chain. It does not add live EC, custom multi-frequency hardware or an irrigation controller. |
| Closest patent/NPL art | CN102914568B replacement-probe equivalence; TCS US12175680/EP4090953 health/replacement; Senviro US20080199359 self-calibration; Bosch WO2020047587 event/confidence/exclusion; 63-sensor universal/one-point NPL; generic validity gates. |
| Claimed physical effect | Lower replacement/remount transfer error and fewer silently wrong accepted estimates, with less calibration workload, because physical perturbation residuals determine whether transfer remains valid. |
| Required experiments | Donor/replacement assignment; naive reuse, pooled, one-point, two-point affine and per-probe oracle; remount/packing/temp/salt/electronic-offset/contamination/ageing challenges; always-report, range, distance and composite gates; every critical ablation. |
| Units/samples/sites | Early two-probe pilot only; credible later evidence needs roughly 6–12 probes across at least two lots, at least three independent preparation batches, repeated remounts and later field wet/dry events. No external industrial site is intrinsically required. |
| Additional hardware/cost | More documented probe units, containers/jigs, reference metrology, controlled contamination/ageing fixtures and continued oven/scale access. The credible later programme may exceed ₹5,000; no defensible complete amount is attached. |
| Time beyond semester | At least one additional semester, with longer field/lifecycle replication if the mechanism survives. |
| Claim usefulness if successful | Narrow-to-moderate but practically coherent: commodity-probe replacement/remount calibration acceptance tied to a specific physical challenge and fallback. Generic transfer, provenance or abstention scope would be weak. |
| Patent risks | Exact combined novelty unresolved; obviousness high; eligibility medium if physically anchored; FTO/search risk material in China and TCS/Bosch national families; population support requires multi-unit evidence. |
| Strongest baseline | Two-point affine transfer plus simple range gate, full per-probe calibration oracle, no update and unrestricted event update. |
| Kill condition | No advantage over two-point affine + range gate; benefit comes from one known component; false-valid reduction requires unusable abstention/workload; contamination cannot be separated from real drift; results fail across units/lots/remounts. |
| Prospective Track | **C.** |

## 13. Semester-build scoring matrix

Each factor is scored from 0 (unacceptable) to 5 (excellent). The weighted total is `sum(score / 5 × factor weight)` and is therefore out of 100. Low/base/high values express evidence-bounded uncertainty, not statistical confidence intervals.

| Factor | Weight | OpenBraille L/B/H | VibeGuard L/B/H | TrueMoist L/B/H |
|---|---:|---:|---:|---:|
| Build feasibility | 25 | 2.4 / 3.3 / 4.1 | 4.0 / 4.5 / 4.9 | 2.9 / 3.8 / 4.4 |
| Validation clarity | 20 | 2.1 / 3.1 / 3.9 | 3.2 / 4.0 / 4.6 | 3.0 / 4.2 / 4.8 |
| Budget fit | 15 | 3.7 / 4.3 / 4.8 | 4.2 / 4.7 / 5.0 | 3.2 / 4.0 / 4.8 |
| Demonstration value | 15 | 3.8 / 4.7 / 5.0 | 4.3 / 4.8 / 5.0 | 3.0 / 3.8 / 4.5 |
| Schedule fit | 10 | 2.0 / 3.0 / 3.8 | 3.7 / 4.3 / 4.8 | 1.9 / 3.0 / 4.0 |
| Team fit | 10 | 2.5 / 3.2 / 4.0 | 4.2 / 4.7 / 5.0 | 3.5 / 4.1 / 4.6 |
| Publication value | 5 | 3.0 / 3.8 / 4.5 | 3.9 / 4.5 / 4.9 | 4.3 / 4.8 / 5.0 |
| **Weighted total / 100** | **100** | **54.9 / 72.1 / 85.6** | **78.0 / 89.5 / 97.4** | **60.2 / 78.2 / 91.3** |

### Evidence for semester scores

| Concept | Evidence supporting base score | Evidence limiting score / defining range |
|---|---|---|
| OpenBraille | BOM ₹2,060–₹2,850; six-servo prototype is visually and socially compelling; frozen architecture and external supply are specified. | Cam/follower tolerance, friction, dot return, reset state, servo current and tactile validation are coupled. Repeated fabrication can consume the schedule. Team fit trails VibeGuard because the dominant risk is precision mechatronics, not embedded analysis. |
| VibeGuard | BOM ₹1,700–₹2,200; one rigid sensor, ESP32 and simple motor/fan rigs; strong embedded/software fit; immediate state-change demonstration; Level 1 can be completed without an industrial site. | Level 2 attribution is not validated. Remount, speed/load and interferer variation can erase the signal. Independent field labels/access affect the high-value extension, though not the basic build. |
| TrueMoist | Frozen 72-run design, dry-basis gravimetric truth, held-out replicate and quantitative success thresholds support unusually clear validation and publication. | Oven, scale, ADC resolution, drying time, soil preparation and probe repeatability are schedule-critical. BOM can reach ₹3,440 and the dataset is labour intensive. |

Material base-score differences of at least one point are traceable: VibeGuard exceeds OpenBraille build feasibility by 1.2 because its physical rig is simpler; TrueMoist exceeds OpenBraille validation clarity by 1.1 because its gravimetric truth and prespecified error thresholds are stronger; VibeGuard exceeds TrueMoist demonstration value by 1.0 because a live motor-state/RGB change is more immediate than a reference-versus-compensated measurement display; VibeGuard exceeds OpenBraille and TrueMoist schedule fit by 1.3 because it avoids repeated mechanical fabrication and the 72-run drying cycle; VibeGuard exceeds OpenBraille team fit by 1.5 because the available strengths better match embedded/software work; and TrueMoist exceeds OpenBraille publication value by 1.0 because even negative compensation results remain a rigorous metrology dataset. The larger low-side gaps have the same stated causes: OpenBraille mechanical iteration, TrueMoist facility/throughput dependency, and VibeGuard's comparatively simple bench architecture. No high-side gap introduces a different rationale.

**Semester ranking:** VibeGuard first, TrueMoist second, OpenBraille third. The low/base/high ranges do not reverse the base ordering when like-for-like scenarios are compared; cross-extreme comparisons are not decision-useful.

## 14. Patent-path scoring matrix

The same 0–5 method is used. A high score means a more favourable development path; for “obviousness resistance,” “FTO/design-around” and “scope,” higher is better. This is a project-selection model, not a patentability or FTO opinion.

| Factor | Weight | OpenBraille L/B/H | VibeGuard L/B/H | TrueMoist L/B/H |
|---|---:|---:|---:|---:|
| Distance from closest art | 20 | 1.3 / 2.1 / 3.0 | 1.7 / 2.5 / 3.4 | 1.4 / 2.3 / 3.2 |
| Mechanism specificity | 15 | 3.9 / 4.6 / 4.9 | 3.4 / 4.2 / 4.7 | 4.0 / 4.6 / 4.9 |
| Obviousness resistance | 15 | 1.2 / 2.1 / 3.2 | 1.1 / 2.0 / 3.0 | 1.3 / 2.2 / 3.2 |
| Experimental accessibility | 15 | 1.8 / 3.0 / 4.0 | 1.3 / 2.4 / 3.6 | 2.4 / 3.5 / 4.3 |
| Useful claim scope | 10 | 1.2 / 2.7 / 3.8 | 1.5 / 2.7 / 3.8 | 1.9 / 3.1 / 4.0 |
| FTO / design-around position | 10 | 1.1 / 2.3 / 3.4 | 1.7 / 2.7 / 3.7 | 1.3 / 2.4 / 3.4 |
| Connection to frozen MVP | 10 | 4.0 / 4.6 / 4.9 | 4.4 / 4.8 / 5.0 | 4.2 / 4.7 / 5.0 |
| Publication fallback | 5 | 3.6 / 4.4 / 4.8 | 4.3 / 4.8 / 5.0 | 4.5 / 4.9 / 5.0 |
| **Weighted total / 100** | **100** | **42.1 / 61.1 / 77.3** | **43.7 / 61.0 / 77.5** | **48.0 / 65.4 / 79.8** |

### Evidence for patent-path scores

| Concept | Supporting evidence | Principal discount |
|---|---|---|
| OpenBraille | D11 is the most physically specific proposal: mechanical datum, per-dot calibration, isolated shared current sensing, physical ground truth, bounded retry/fault isolation and current-aware sequencing. It is tightly connected to the six-servo MVP. | Servo/cam refreshable Braille is crowded; the Indian application remains unresolved; rail current is not inherently dot-state truth; practical-scale and long-cycle evidence are costly. The likely surviving claim may be a narrow implementation bundle. |
| VibeGuard | The proposed loop is coherent and connected: labelled target/interferer commissioning, target abnormality versus ambiguity, abstention, protected update and remount invalidation with speed/load conditioning. | FFT/baseline subtraction, rebaselining, condition monitoring and novelty detection are crowded. Independently labelled field evidence is externally dependent, and a software-heavy claim risks eligibility and easy design-around. |
| TrueMoist | The later mechanism is specific and testable: donor provenance, sparse physical reference challenges, bounded transfer, perturbation residuals, validity state, contaminated-update blocking and abstention. It can be developed with laboratory samples rather than an industrial site. | Replacement equivalence, sensor health, self-calibration, confidence/event exclusion and one-point transfer are all known components. Multi-unit support is still required, and the useful claim may narrow to a particular challenge/acceptance sequence. |

The only base accessibility gap of at least one point is TrueMoist over VibeGuard (1.1): the former requires more probes and laboratory labour, but the decisive labels are under project control; the latter ultimately needs independently labelled target/interferer field access. Smaller differences remain consequential because all three paths start in crowded art and none exceeds Track C prospectively.

**Patent-path ranking:** TrueMoist first. OpenBraille and VibeGuard are effectively tied on base total (61.1 versus 61.0), but for different reasons: OpenBraille has greater physical specificity, while VibeGuard has better design-around flexibility, MVP connection and publication fallback.

## 15. Integrated-score sensitivity analysis

The integrated score is `semester score × build weight + patent-path score × patent weight`, using base scores only. The default allocation is 40% semester / 60% patent because Project mC is patent-first but requires a credible build.

| Concept | 50% semester / 50% patent | **40% semester / 60% patent** | 30% semester / 70% patent |
|---|---:|---:|---:|
| OpenBraille | 66.6 | **65.5** | 64.4 |
| VibeGuard | **75.3** | **72.4** | **69.5** |
| TrueMoist | 71.8 | **70.5** | 69.2 |
| VibeGuard lead over TrueMoist | 3.5 | **1.9** | 0.3 |

VibeGuard ranks first at all three specified weightings, so the numerical result is not a simple weight-selection artefact. It is not robust enough for unconditional selection: at the most patent-heavy weighting the lead is only 0.3. The **single load-bearing assumption** is that VibeGuard's target-attribution advantage can be demonstrated under independently labelable field access; if that assumption fails, its experimental-access and useful-scope scores fall together and TrueMoist wins. That is why the score supports **VG-SAG**, not immediate patent-first commitment. A VibeGuard gate failure directly removes the assumption responsible for its later-path plausibility; TrueMoist then becomes the selected fallback.

## 16. OpenBraille versus VibeGuard

| Required comparison | Adjudication |
|---|---|
| Better semester build | **VibeGuard.** Simpler mechanics, lower BOM, stronger team fit and faster locked validation outweigh OpenBraille’s excellent visual/tactile demo. |
| More credible later mechanism | OpenBraille’s D11 is more physically specific; VibeGuard’s attribution/ambiguity/update loop is more operationally relevant. On present evidence neither is stronger overall: their patent-path base totals are 61.1 and 61.0. |
| Closer damaging art | OpenBraille faces direct servo/cam Braille and an unresolved Indian family around the physical core. VibeGuard faces extensive condition-monitoring/NPL and explicit spectral-baseline/rebaseline disclosures. Both are crowded; OpenBraille’s core mechanism is more directly occupied, while VibeGuard’s proposed loop is easier to decompose into known software steps. |
| More expensive or longer proof | **VibeGuard** is more externally dependent and may take 6–12 months with field replication. OpenBraille’s practical-scale fixture and 10k–100k transition work can cost more per prototype, but can remain internally controlled. |
| Better chance of a useful narrow claim | Slight edge to **OpenBraille** if—and only if—the full D11 bundle produces non-additive, ground-truthed reliability at practical scale. VibeGuard’s likely narrow claim is software/process-heavy and easier to design around. |
| Clearer kill experiment | **OpenBraille:** fast isolated current capture plus physical dot truth over held-out transitions, followed by 3,000 transitions with zero silent wrong states and ablation. VibeGuard first needs the dual-source gate and later a field site. |
| Better publication fallback | **VibeGuard:** embedded sensing, interference experiments, remount robustness and negative attribution results are easier to publish without a successful patent path. |
| Single reversal fact | If OpenBraille D11 clears the Indian-family review and shows a non-additive effect at practical cell scale with zero silent errors, it could overtake VibeGuard’s later path. Until then, it does not. |

## 17. OpenBraille versus TrueMoist

| Required comparison | Adjudication |
|---|---|
| Better semester build | **TrueMoist** on the weighted base score (78.2 versus 72.1), principally because the frozen experiment has stronger quantitative truth and publication value. OpenBraille remains the stronger live exhibit. |
| More credible later mechanism | OpenBraille is more electromechanically integrated; **TrueMoist** is more credible overall because its transfer/validity mechanism and decisive experiments are accessible without precision multi-cell fabrication. |
| Closer damaging art | OpenBraille has direct servo/cam Braille and unresolved Indian-family risk. TrueMoist has close replacement-equivalence, health, self-calibration and event/confidence art. Both require combination/claim charts; OpenBraille has the more direct physical-core collision. |
| More expensive or longer proof | OpenBraille likely needs the more specialized practical-scale fixture and ₹5,000–₹20,000 later programme. TrueMoist is labour- and sample-heavy and needs another semester, but its equipment is more ordinary if oven/scale access exists. |
| Better chance of a useful narrow claim | **TrueMoist** at base: a physical-reference-bound replacement/remount acceptance sequence has an identifiable operational user and can be tested across commodity probes. |
| Clearer kill experiment | OpenBraille has the sharper single sensor-truth gate. TrueMoist has the clearer comparative transfer gate: it must beat two-point affine transfer plus a simple range gate across units/lots/remounts at usable coverage. |
| Better publication fallback | **TrueMoist.** The frozen 72-run metrology dataset and later population-transfer study remain publishable under negative outcomes. |
| Single reversal fact | A strong, non-additive D11 result at practical scale could move OpenBraille ahead; conversely, loss of reliable oven/scale access would remove TrueMoist’s present advantage. The current evidence supports TrueMoist. |

## 18. VibeGuard versus TrueMoist

| Required comparison | Adjudication |
|---|---|
| Better semester build | **VibeGuard.** Its base semester score is 89.5 versus 78.2, with the advantage concentrated in build simplicity, budget, schedule, team fit and demonstration. |
| More credible later mechanism | **TrueMoist** at present because its physical-reference transfer/acceptance mechanism is more specific and the labels are internally obtainable. VibeGuard may have greater industrial value only if source-conditioned attribution survives and field access materializes. |
| Closer damaging art | VibeGuard’s spectral subtraction, rebaseline, novelty detection and condition monitoring are heavily disclosed; TrueMoist’s replacement transfer, health and calibration components are also close. VibeGuard has the greater software-combination/eligibility pressure; TrueMoist has more exact transfer analogues. |
| More expensive or longer proof | **VibeGuard** is more likely to become longer and externally costly because credible evidence needs independently labelled industrial operation and remount/load variation. TrueMoist needs more units and laboratory labour but can progress under project control. |
| Better chance of a useful narrow claim | **TrueMoist**, modestly: its base useful-scope score is 3.1 versus 2.7, provided the physical challenge and acceptance logic outperform simple transfer/range gates. |
| Clearer kill experiment | **TrueMoist** has the cleaner later kill comparison. VibeGuard’s VG-SAG is an excellent early kill gate but passing it still leaves the field-validity problem. |
| Better publication fallback | Both are strong; **TrueMoist** is slightly higher because the prespecified gravimetric dataset is publishable even before the patent extension. |
| Single reversal fact | If VG-SAG passes and written access to independently labelled target/interferer field data is secured, VibeGuard’s superior semester execution and higher-value field mechanism would justify selection over TrueMoist. This is the exact fact the gate tests. |

## 19. Novelty comparison

Novelty is assessed here as a risk-screening question—whether every required element may be found in one enabling reference—not as a legal conclusion. No synthesis established a clean claim chart for a final claim set.

| Concept | Frozen MVP | Later proposed mechanism | Novelty posture |
|---|---|---|---|
| OpenBraille | Six hobby servos, PWM control and eccentric cam/follower dot motion are not a credible inventive core. | The D11 bundle adds a datum, per-dot calibration, isolated shared-current evidence, physical dot truth, bounded retry/fault isolation and current-aware sequencing. | No reviewed source was shown to disclose that exact whole bundle in one system, but direct refreshable-Braille actuation art and the unresolved Indian application make the gap fragile. **Track D now; only conditional re-entry.** |
| VibeGuard | One accelerometer, FFT/features, thresholding/Mahalanobis and a local indicator are conventional condition monitoring. | Source-labelled commissioning separates target abnormality from interference ambiguity, abstains, protects updates and invalidates/transfers state on remount under speed/load variation. | Exact combined disclosure was not established, but each major function has close analogues. Independent verification shows KCF claim 1 is a networking/compression parent while dependent claims 4 and 9 expressly cover FFT baseline subtraction and baseline regeneration after spectral deviation; this does not literally read on the local-only frozen design, but materially narrows any novelty story based on subtraction/rebaselining alone. [US10873791B1](https://patents.google.com/patent/US10873791B1/en) **Track C prospectively.** |
| TrueMoist | Temperature/salt coding, fixed regression and held-out validation on a capacitive probe are evidence generation, not a credible inventive core. | Provenance-bound replacement/remount transfer is accepted only after sparse physical reference challenges and perturbation residuals establish a validity state; contaminated updates are blocked and the device abstains/falls back. | No exact single-reference anticipation was established for the whole sequence, but replacement equivalence, sensor health, self-calibration, event/confidence exclusion and one-point transfer are separately close. **Track C prospectively.** |

Relative result: TrueMoist and VibeGuard retain unresolved exact-combination gaps suitable for experiments and professional searching; OpenBraille retains a possible exact gap but has the most direct collision at its physical core. None has a demonstrated novel claim ready for filing.

## 20. Inventive-step/obviousness comparison

| Concept | Why a skilled-person combination is plausible | Evidence needed to resist that inference |
|---|---|---|
| OpenBraille | Servo/cam actuation, homing/calibration, current monitoring, retries and fault isolation are familiar reliability measures. Adding them to a refreshable cell may be characterized as routine engineering. | A practical-scale, held-out and ablated result showing that the specific datum/current/ground-truth/sequence interaction prevents silent wrong dots beyond the sum of its parts, across rebuilds, servo swaps and environmental variation. |
| VibeGuard | Source conditioning, spectral features, anomaly distance, abstention, protected baselines and remount reset are known signal-processing/ML operations. Their ordering may look like predictable deployment hygiene. | Locked prospective evidence that the defined source-conditioned ambiguity state and update rule deliver a non-obvious physical-monitoring effect versus the strongest subtraction, band-feature and ordinary Mahalanobis comparators, across remounts and a labelled field setting. |
| TrueMoist | Calibration transfer, one/two-point affine correction, range/distance gates, provenance, sensor-health checks and abstention are familiar metrology patterns. | Multi-unit, multi-lot evidence that the particular sparse physical challenge plus perturbation-residual validity state reduces false-valid estimates and calibration work versus two-point affine plus range gating, with ablations proving the interaction rather than one known component. |

All three have **high obviousness risk**. TrueMoist receives the slight base advantage because the proposed physical challenge/validity mechanism has a clear comparative test under project control. That is a research advantage, not a conclusion that an inventive step exists.

## 21. Patent-eligibility comparison

| Concept | Principal eligibility exposure | Safer technical anchoring | Relative risk |
|---|---|---|---|
| OpenBraille | Low algorithmic exposure; risk instead lies in novelty/obviousness and functional claiming. | Claim only a supported physical cell/control arrangement and measured interaction, not the abstract aim of reliable Braille. | **Lowest of the three**, but physicality does not cure prior-art weakness. |
| VibeGuard | Highest exposure to characterization as mathematical methods, algorithms or software per se if drafted around FFT, distances, classification or “AI.” | Specific sensor placement/acquisition, physical commissioning states, actuator/source conditions, on-device control of baseline validity, abstention output and measured machinery-monitoring effect. | **Highest.** A locally executed algorithm is not automatically eligible. |
| TrueMoist | Regression, categorical metadata, transfer maps and confidence gates can be characterized as mathematical processing. | Tie each step to a replaced/remounted physical probe, specified reference challenges, measured perturbation residuals, a bounded validity state and a concrete accept/abstain output. | **Medium.** Stronger than a generic calibration formula, still counsel-dependent. |

Final eligibility depends on jurisdiction, claim form and current law. Indian Section 3(k) and any other relevant exclusions require professional review before drafting; this adjudication does not resolve them.

## 22. FTO and design-around comparison

Patentability and freedom to operate are separate. Even a patentable improvement can infringe a broader live claim; conversely, an expired, lapsed or foreign-only document can remain powerful prior art without blocking local use. No concept has FTO clearance.

| Concept | FTO/search focus | Design-around pressure | Adjudicated position |
|---|---|---|---|
| OpenBraille | Resolve `5559/CHE/2014` and family/status/claims; chart direct refreshable-Braille servo/cam and diagnostic-control families in intended manufacture/use jurisdictions. | Competitors could change actuator, sensing topology, datum or retry logic. A claim broad enough to stop those changes is unlikely on present evidence. | Weakest FTO posture because the physical product category and the unresolved Indian record are directly relevant. |
| VibeGuard | Chart KCF, Mitsubishi, Rolls-Royce and other cited families against acquisition, baseline, remount, source separation, update and output steps; verify legal status by jurisdiction. | Source separation, adaptive filters, multiple sensors or server-side learning can bypass a narrow local ambiguity/update sequence. | Slightly better design-around flexibility for the project, but also easier for others to avoid; field use can encounter vendor analytics claims. |
| TrueMoist | Chart CN replacement/calibration families, TCS health/replacement, Senviro, Bosch and custom moisture/salinity families; check India and intended markets. | Alternative reference challenges, per-probe calibration, population models or different validity statistics can bypass the sequence. | Material unresolved risk, but the commodity frozen hardware offers more implementation room than a new multi-frequency/live-EC probe. |

Before any filing or deployment decision, counsel should run fresh family/status searches, claim charts and an intended-jurisdiction FTO review. Search absence in the supplied syntheses is not evidence of non-infringement.

## 23. Evidence accessibility and experimental burden

| Concept | First decisive evidence | Control of inputs/labels | Later credible burden | Access risk |
|---|---|---|---|---|
| OpenBraille | Fast isolated current capture synchronized to direct physical dot-state truth; held-out classifier/threshold and ablation. | Mostly internal, but needs reliable tactile/physical truth and fabrication. | Practical-scale cell/coupon, rebuilds, servo swaps, voltage/friction/temp/load variation, 3,000 silent-error run and later 10k–100k cycles; roughly 4–9 months and ₹5,000–₹20,000 indicated. | Medium: internally controllable but specialist mechanical iteration and measurement bandwidth are demanding. |
| VibeGuard | VG-SAG dual-source, remounted, held-out attribution test. | Early labels are internal; credible later labels and operating variability depend on a cooperating field site. | At least five independent sessions/remounts across three or more days, one independently labelled field site, load/speed regimes, locked ablations and later replication; approximately 6–12 months is plausible. | **Highest:** external access, labels and operational permissions are the controlling uncertainty. |
| TrueMoist | Week-1 oven/scale/ADC/probe gate, then frozen 72-run study; later two-probe transfer pilot. | Laboratory labels are substantially internal if facilities are available. | Roughly 6–12 probes from at least two lots, three or more preparation batches, remounts, packing/temp/salt/electronic-offset/contamination/ageing and field wet/dry events; at least another semester. | Medium: facility and labour intensive, but less dependent on an external industrial partner. |

For the semester, VibeGuard has the lowest experimental burden. For a defensible later patent path, TrueMoist has the best balance of mechanism specificity and controllable evidence; VibeGuard has the largest access discontinuity; OpenBraille has the largest precision/reliability discontinuity.

## 24. Claim usefulness and narrowness risk

| Concept | Smallest presently coherent later claim centre | Potential user value | Easy design-around / over-narrowing risk | Forecast risk that any surviving claim is too narrow to justify the programme |
|---|---|---|---|---:|
| OpenBraille | A defined datum/current/physical-truth control sequence for a specific multi-dot cam/servo cell. | Fewer silent wrong dots and bounded recovery in a low-cost refreshable cell. | Changing actuator, local sensing, datum arrangement or fault policy may escape; the full bundle may be required merely to clear art. | **60–80%** |
| VibeGuard | A specified source-conditioned commissioning and ambiguity/update-validity loop for a local single-sensor machinery monitor. | Fewer false target alarms in the presence of a coupled interferer without corrupting the baseline. | Add a sensor, use adaptive filtering/source separation, change update/abstention logic or move computation. Eligibility constraints may force more physical detail. | **65–85%** |
| TrueMoist | A specific sparse physical-reference challenge and residual-validity sequence for replacement/remount transfer of commodity probes. | Less recalibration work with fewer silently accepted bad estimates after probe change/remount. | Use per-probe calibration, different challenge points/statistics, a population model or a different fallback. Exact transfer/health art may force a tight sequence. | **55–75%** |

These are broad programme-risk bands, not legal probabilities. A narrow claim is not inherently poor: it is useful only if it covers a product-relevant mechanism, is detectable/enforceable, and is not trivially avoided. TrueMoist has the best base balance; VibeGuard has the greatest risk of an elegant experiment yielding an algorithmically narrow claim; OpenBraille has the best physical detectability but the weakest present distance from its core art.

Enablement/support is a separate weakness in all three: OpenBraille needs practical-scale and lifecycle data for a multi-dot reliability claim; VibeGuard needs independently labelled remount/field data for source-conditioned operation; TrueMoist needs multi-unit, multi-lot and perturbation data for population transfer. A broad claim should not be pursued beyond the mechanism and operating range actually supported.

## 25. Optimistic/base/pessimistic simulation

The simulation applies the same default 40% semester / 60% patent weighting to the matched low, base and high scores. It is a stress test of the selection model, not a forecast of patent-office outcomes.

| Scenario | OpenBraille integrated score | VibeGuard integrated score | TrueMoist integrated score | Operational interpretation |
|---|---:|---:|---:|---|
| Optimistic (matched high inputs) | 80.6 | **85.5** | 84.4 | All builds work well; later effects survive initial ablations; key access/search issues are favourable. VibeGuard retains a small execution lead, while TrueMoist is close. |
| Base | 65.5 | **72.4** | 70.5 | VibeGuard leads but its 1.9-point margin is conditional on attribution evidence and field access; run VG-SAG. |
| Pessimistic (matched low inputs) | 47.2 | **57.4** | 52.9 | Patent paths are killed or become impractically narrow. VibeGuard remains the best semester-only build, not a patent-first commitment. |

| Concept | Optimistic case | Base case | Pessimistic case |
|---|---|---|---|
| OpenBraille | Targeted art/status review leaves a usable gap; fast current plus physical truth discriminates dot state; the full D11 bundle shows a non-additive effect, zero silent errors in 3,000 transitions and practical-scale robustness. The route may reopen toward Track B review. | Bench discrimination is possible, but scale, rebuild and ablation results are mixed or the surviving claim is very narrow. Complete the prototype/publication path; retain Track D. | Rail current mostly measures servo effort, silent dot errors remain, or direct art/status closes the claim centre. Kill the patent programme. |
| VibeGuard | VG-SAG passes cleanly; the named site delivers independent labels; the locked source-conditioned ambiguity/update loop beats every conventional comparator across remounts and field variation. Continue prospective Track C review. | Semester MVP succeeds, while attribution improvement or access is marginal and later scope remains uncertain. Use the gate decision; publish Level 1/bench results if the later path does not survive. | Target information is not separable from the interferer at useful coverage, updates contaminate, or field access fails. Kill patent-first work and retain only the semester build. |
| TrueMoist | Frozen compensation thresholds pass; the composite transfer-validity mechanism beats two-point affine plus range gating across units/lots/remounts with lower false-valid error and acceptable coverage/workload. Continue prospective Track C review. | The 72-run study is publishable and the two-probe pilot is promising, but population effect or claim breadth remains modest. Extend only under a locked multi-unit plan. | Facilities/probe repeatability fail, or simple transfer/range baselines explain the benefit across units. Kill the later patent path; publish the metrology result if valid. |

| Concept | Plausible mass on optimistic regime | Plausible mass on base regime | Plausible mass on pessimistic regime | Principal driver |
|---|---:|---:|---:|---|
| OpenBraille | 10–20% | 50–65% | 20–35% | Whether current plus physical truth produces a reproducible non-additive reliability effect and the direct art clears. |
| VibeGuard | 15–25% | 45–60% | 20–35% | Whether target-specific information survives a coupled interferer/remount and a labelled field site is secured. |
| TrueMoist | 15–25% | 50–65% | 15–30% | Whether the composite validity state beats simple two-point/range baselines across units and lots at usable coverage. |

The broad bounds are elicited management ranges and are not intended to sum at their endpoints. They represent the chance that the *development regime* will resemble the stated scenario, not the chance of patent grant, validity, non-infringement or commercial success.

## 26. Kill-probability and decision-reversal analysis

| Concept | Forecast chance that later patent path is killed before filing review | Earliest decisive experiment | Later decisive experiment | What would reverse the current decision |
|---|---:|---|---|---|
| OpenBraille | **65–80%** | Show whether fast isolated rail-current features predict direct physical dot state on held-out transitions; then test the full D11 bundle over 3,000 transitions with zero silent wrong states and component ablations. | Repeat the locked, ablated mechanism at practical cell/coupon scale across rebuilds, servo swaps, voltage/friction/temp/load variation and lifecycle runs approaching the proposed 10k–100k range. | Re-enter patent-first comparison only if the targeted Indian/current-art review clears, the full bundle beats components non-additively, and the effect survives practical scale, rebuilds and servo/environment changes. |
| VibeGuard | **60–75%** | **VG-SAG by 13 August 2026, 18:00 IST.** | Independently labelled field validation and replication across remounts, machines, speeds/loads and contamination/update challenges, with locked baselines and ablations. | Pass every signal, runtime and written-access threshold: select VibeGuard. Fail any threshold: reverse to TrueMoist, subject to its Week-1 facility/probe gate. |
| TrueMoist | **55–70%** | Two-probe/remount pilot comparing the composite validity logic with two-point affine transfer plus range gating, after oven/scale/ADC access is confirmed. | Locked evaluation across roughly 6–12 probes, at least two lots, at least three preparation batches, remounts and perturbations, followed by field wet/dry events. | It becomes the immediate selection if VG-SAG fails. If selected, abandon its patent extension if it cannot reduce false-valid estimates at usable coverage or if multi-unit/lot access cannot be funded. |

The bands are intentionally high because each proposal is a post-MVP enhancement assembled in crowded art and still lacks the decisive multi-condition result. Model agreement did not enter the estimates. The overall decision tree is therefore simple: **VG-SAG pass → VibeGuard; VG-SAG fail → TrueMoist; TrueMoist access/early-transfer fail → no patent-first selection, retain VibeGuard only as the semester build.** OpenBraille does not displace either branch without the separate, stricter re-entry evidence above.

## 27. Best semester-build candidate

**VibeGuard is the best semester-build candidate.** Its frozen MVP—not the unproven Level-2 invention path—fits the three-month, ₹3,000-preferred envelope most comfortably. The one-sensor ESP32 architecture, isolated motor/fan rig, local RMS/persistence plus triggered FFT and RGB output make a clear demonstration. The team can implement and test it with its strongest embedded/software members while giving bounded logging, rig-state and presentation tasks to the learner and support member.

Selection for the semester does not imply patent selection. Level 1 condition indication and Level 2 target/interferer attribution must remain separately labelled in data, code, claims and demonstrations. A successful Level 1 result must not be narrated as proof of Level 2.

## 28. Best post-MVP patent-development candidate

**TrueMoist is the best presently evidenced post-MVP patent-development candidate.** It does not have the highest semester score, and its frozen compensation experiment remains Track D as a patent target. Its advantage lies in the later mechanism: replacement/remount transfer accepted only through a defined physical challenge, residual-validity state, protected update and abstain/fallback sequence. That proposal is specific, directly connected to the MVP, quantitatively falsifiable and less dependent on external field labels than VibeGuard.

This is only **prospective Track C**. It earns another controlled invention-development stage, not a filing presumption. The path should be killed if it cannot beat two-point affine transfer plus a simple range gate across units/lots/remounts at usable coverage.

## 29. Best overall Project mC choice

**Run the VibeGuard Level-2A Signal-and-Access Gate (VG-SAG) before selecting the overall Project mC concept.**

- **Deadline:** 13 August 2026, 18:00 IST.
- **Success threshold:** all six Section 1 criteria, including the locked held-out day/remount result (≥30% relative reduction in attribution error or false target alerts; missed target faults no more than 5 percentage points worse; ≥80% coverage), local ESP32 runtime integrity, and written named field access in principle within 16 weeks.
- **If it passes:** select VibeGuard. Treat the frozen MVP as Track D for patents and the later source-conditioned ambiguity/update mechanism as prospective Track C.
- **If it fails:** select TrueMoist, subject to its Week-1 oven/scale/ADC/probe-repeatability gate. Treat the frozen study as Track D and the later transfer-validity mechanism as prospective Track C.
- **If the fallback gate also fails:** make no patent-first selection; complete VibeGuard only as the best semester prototype/publication project.

This is the only overall selection rule. It prevents VibeGuard’s large build advantage from masking its field-access discontinuity while preserving a fast, high-information decision.

## 30. Runner-up and deprioritized concept

**Runner-up and controlled fallback: TrueMoist.** It becomes the overall selection immediately upon VG-SAG failure if its mandatory resources and early probe gate pass. Its semester scope must remain the frozen one-soil, offline/fixed-model 72-run design; the later multi-unit transfer programme is separately funded and scheduled.

**Deprioritized for patent-first selection: OpenBraille.** It should not consume the Project mC patent budget now. It remains suitable for a prototype, accessibility/usability study or publication, and its D11 proposal may be retained in confidential lab records. Re-entry requires all of the following: targeted resolution of the Indian/current-art issue, fast-current-to-physical-state discrimination, zero silent wrong states in the defined 3,000-transition run, non-additive ablation evidence and practical-scale robustness. No credit is given merely because two syntheses discussed a similar route.

## 31. First 12-week execution plan

### Common decision and control period

| Week / dates | Work | Locked output / decision | Lead roles |
|---|---|---|---|
| 1: 3–9 Aug 2026 | Place only reversible/common procurement; build coupled target/interferer fixture; define six state cells, block length, remount log, held-out day, comparator code and saturation/alias checks. In parallel, obtain written oven/scale availability and price/lot availability for TrueMoist probes without starting its full study. | Versioned protocol, BOM, risk log, team assignments, raw-data schema and confidentiality notice. No public disclosure. | Strong member A: hardware; B: DSP/data; C: protocol/statistics; learner: logger/state controls; presenter: access letters and documentation. |
| 2: 10–16 Aug 2026 | Complete three independently started VG-SAG sessions on three days with a remount each day; keep one entire day untouched; run locked comparators and ESP32 integrity test; obtain named field-access letter. | **Gate decision at 13 Aug, 18:00 IST.** Signed one-page pass/fail record with every criterion, deviations and raw-data hashes. Freeze the selected branch by 14 Aug. | Same owners; no one who tunes on training days may inspect the held-out labels/results until freeze. |

### Branch A — VG-SAG passes: VibeGuard semester MVP

| Week | Work | Exit criterion |
|---|---|---|
| 3 | Freeze Level-1 requirements and frozen architecture: one rigid ADXL345, SPI, ESP32, isolated motor/fan + eccentric mass, RMS/persistence, triggered FFT and RGB state. | Schematics, pin map, safe rig, fixed sample-rate/bandwidth and acceptance plan. |
| 4 | Implement acquisition, timestamping, block-loss counter, RMS/persistence and deterministic RGB states. | Repeatable normal/abnormal response with raw capture; no hidden dropped blocks. |
| 5 | Add triggered FFT/band features and ordinary Mahalanobis as prospective, clearly separated modules. | Feature tests and versioned fixed parameters; Level 1 remains independently functional. |
| 6 | Run speed/load/orientation/remount characterization on the bench; freeze thresholds before the held-out run. | Documented failure envelope and threshold freeze. |
| 7 | Build the live demonstration and fail-safe/unknown indication; complete electrical and mechanical safety review. | Continuous local demo; interferer does not get misrepresented as a proven field fault. |
| 8 | Execute locked Level-1 validation over independent sessions and remounts; retain all failures. | Confusion/event metrics by session, coverage, latency and resource use. |
| 9 | Repeat the Level-2A gate implementation as a research extension with ablations, not as an MVP claim. | Source-conditioned effect, if any, separated from comparator and leakage effects. |
| 10 | Independent replication/rebuild and code review; freeze demo firmware. | Reproducible run by a second team member and archived raw data/code/BOM. |
| 11 | Prepare report, poster and live demonstration; distinguish frozen result, later hypothesis and limitations. | Internal technical review completed; no unsupported field or patent claim. |
| 12 | Submit invention disclosure only if the later mechanism still meets its gate; obtain institutional publication/filing decision. | Demonstrable semester MVP, final evidence pack and authorized disclosure/publication sequence. |

### Branch B — VG-SAG fails: TrueMoist fallback

| Week | Work | Exit criterion |
|---|---|---|
| 3 | Confirm oven and scale access; check analog probe stability/remount repeatability and ESP32-versus-ADS1115 resolution; procure within the frozen BOM. | Facilities documented; ADC path chosen prospectively; no unacceptable short-term drift/repeatability. Failure means no patent-first selection. |
| 4 | Freeze one soil, moisture preparation, controlled salt code, DS18B20 method, M0/M1/M2 models, 4×3×2×3 assignment, dry-basis reference, held-out replicate and analysis script. | Protocol and thresholds locked before outcome inspection. |
| 5 | Prepare and randomize samples; calibrate weighing/drying workflow; pilot only process timing and QC. | Mass balance and sample-ID audit pass. |
| 6 | Acquire the first balanced block with logged temperature, salt condition, raw ADC and environmental/QC data. | No missing cells; repeatability within the prespecified QC rule. |
| 7 | Complete remaining acquisition and oven-dry references without changing models. | All 72 assigned runs accounted for; exclusions documented before analysis. |
| 8 | Fit M0/M1/M2 using training groups only; lock coefficients and categorical encodings. | Reproducible fixed model artefacts. |
| 9 | Evaluate the untouched replicate and prespecified subsets. | Primary pass requires RMSE ≥20% lower and MAE ≥15% lower, with no subset MAE worsening >10%. |
| 10 | Implement fixed inference and live USB display; conduct repeatability and power/runtime checks. | Demo reports reference/raw/compensated values without online adaptation. |
| 11 | Run only a bounded two-probe/remount feasibility pilot for the later path; compare naive reuse, two-point affine and simple range gate. | Evidence-based continue/kill memo; no claim of population transfer. |
| 12 | Finalize dataset, report, poster and invention disclosure decision before any public release. | Auditable semester study and authorized filing/publication sequence. |

The branch choice is irreversible for the semester unless a safety or resource stop condition occurs. OpenBraille is not mixed into either branch, and the frozen architectures are not expanded to rescue a weak result.

## 32. Later invention-development plan

### If VibeGuard is selected after VG-SAG

1. **Month 1:** execute a professional current-art/family/status search and preliminary claim chart focused on source attribution, spectral baseline/subtraction, update invalidation, remount and abstention; settle a measurable technical-effect hypothesis before expanding hardware.
2. **Months 1–2:** convert the gate rig into a locked Level-2A protocol with at least five independent sessions/remounts across at least three days, multiple speeds/loads and physically logged target/interferer states. Preserve RMS/persistence, band/FFT, static subtraction and ordinary Mahalanobis comparators.
3. **Months 2–4:** use the named site under a written safety/data/IP agreement. Obtain independently labelled target and interferer events; separate commissioning, target abnormality, ambiguity/unknown, update eligibility and remount invalidation. Do not use weak machine logs as ground truth without qualification.
4. **Months 3–5:** run ablations of source conditioning, ambiguity gate, protected update, remount rule and speed/load normalization. Report coverage, false target alerts, missed target faults, latency, block loss and calibration workload by session/site.
5. **Months 5–6:** replicate on a second machine or independent fixture if possible. Freeze the mechanism and repeat the search against the actual supported elements.
6. **Filing gate:** proceed to counsel only if the locked combined mechanism beats the strongest comparator with no unacceptable miss/coverage trade-off, survives remount/field variation, shows an interaction not explained by one known component, and a claim chart identifies useful scope. Otherwise publish the benchmark/negative result after clearance.

### If TrueMoist is selected as fallback

1. **Month 1:** run a professional search/claim chart around replacement equivalence, transfer calibration, sensor health, provenance, reference challenges, validity gating, contamination blocking and abstention. Freeze the proposed physical sequence.
2. **Months 1–2:** complete a two-probe/remount pilot with naive reuse, pooled calibration, one-point, two-point affine, per-probe oracle and simple range/distance gates. Select metrics and coverage/workload limits prospectively.
3. **Months 2–5:** expand to roughly 6–12 documented probes from at least two lots and at least three independently prepared batches. Randomize donor/replacement assignments and repeated remounts.
4. **Months 3–6:** challenge packing, temperature, salt, electronic offset, contamination and ageing; include field wet/dry events later. Keep trusted reference events separate from normal operation and prevent contaminated updates.
5. **Months 5–7:** ablate provenance, each reference challenge, residual features, validity state, update block and abstain/fallback. Compare false-valid rate, accepted-error distribution, coverage and calibration workload—not RMSE alone.
6. **Filing gate:** proceed only if the composite mechanism outperforms two-point affine plus range gating across units/lots/remounts at usable coverage, the effect is not due to one known element, and the refreshed claim chart retains product-relevant scope. Otherwise publish the transfer benchmark/negative result after clearance.

OpenBraille’s D11 work remains a separately budgeted confidential re-entry study and is not combined with either selected mechanism. Cross-concept hybridization would destroy concept fidelity and is not authorized by this adjudication.

## 33. Confidentiality and institutional IPR plan

1. **Before disclosure:** notify the institution’s IPR/innovation office now; identify the governing student, sponsor, laboratory and university policies; impose a written publication hold until the office records a filing-or-release decision. Posters, repositories, demonstrations to outsiders, competitions, abstracts and social posts all count as potential disclosure channels.
2. **Records:** keep dated, versioned protocols, schematics, source commits, raw-data hashes, calibration records, failed runs, gate decisions and meeting notes. Preserve who conceived each claimed element and who reduced it to practice. Do not rewrite history after a positive result.
3. **Inventorship:** determine inventorship claim by claim from documented contribution to conception under applicable law. Team membership, authorship, supervision, funding, coding volume and model-generated suggestions do not automatically make someone an inventor. Use qualified patent counsel for the final determination.
4. **Ownership and agreements:** document student/institution ownership, assignments, sponsor terms and contributor expectations before later work. For VibeGuard, the field-site agreement must address background IP, new IP, data rights, safety, access, confidentiality and publication review. For TrueMoist, record probe vendors/lots and laboratory-resource terms.
5. **Third-party material:** maintain a bill of software, libraries, datasets and hardware documentation with licences. Do not place confidential site data or patent-sensitive notebooks in public AI prompts or public repositories. Review export, privacy and safety constraints where relevant.
6. **Filing sequence:** invention disclosure → counsel-led inventor interviews/search/claim review → institutional decision → filing if approved → only then authorized publication. A provisional or other filing is not presumed; counsel chooses jurisdiction and instrument.
7. **If no filing:** obtain written release from the responsible office, then publish a carefully scoped engineering result with negative outcomes and limitations. Keep FTO separate from permission to publish or from ownership.

Treat this report and the following project records as confidential pending that review: exact D11 implementation details; VibeGuard source-attribution, contamination, remount and abstention logic; TrueMoist reference challenges, transfer mappings, contamination gates and validity states; all unpublished positive and negative results, ablations and parameter values; and contributor chronology/invention records. Public discussion should remain limited to frozen architectures and generic known techniques until written release.

## 34. Final recommendation

**Run the VibeGuard Level-2A Signal-and-Access Gate (VG-SAG) now; do not make an unconditional patent-first selection.** Complete it by **13 August 2026, 18:00 IST** under the locked six-cell, three-day/remount, whole-day-held-out protocol. A pass requires the specified ≥30% relative attribution/false-alert improvement, ≤5-percentage-point miss penalty, ≥80% coverage, clean local ESP32 operation and written named field access within 16 weeks.

The **primary kill condition** is failure of any locked VG-SAG criterion—most importantly, failure to preserve target-attribution improvement at the miss-rate/coverage limits on the untouched day/remount, or failure to secure the named field-access letter by the deadline.

- **Pass:** select **VibeGuard** as Project mC because it is the best semester build and has earned a prospective Track C later experiment. Its frozen MVP remains Track D for patents.
- **Fail:** select **TrueMoist** as runner-up/fallback, subject to the Week-1 facility/ADC/probe gate. It is the best current post-MVP patent-development candidate; its frozen study remains Track D and later mechanism prospective Track C.
- **Fallback also fails:** make **no patent-first selection** and finish VibeGuard only as the strongest semester prototype/publication project.
- **OpenBraille:** deprioritize for patent-first work; retain only prototype/publication value and a separately gated confidential D11 re-entry route.

Confidence in this *decision procedure* is **medium-high** because the build ranking is stable and the decisive uncertainty is explicit. Confidence that any later enhancement will support a useful patent is **low-to-medium** and contingent on experiments, refreshed searching and counsel. No project or enhancement is predicted or promised to receive a patent.

## 35. Unresolved questions

| Open question | Owner / deadline | Decision effect |
|---|---|---|
| Can VG-SAG meet the held-out attribution, miss-rate and coverage thresholds without leakage? | VibeGuard technical lead; 13 Aug 2026 | Pass/fail overall selection. |
| Is a named site willing to provide independently labelled target/interferer access, safe remounts and acceptable data/IP terms within 16 weeks? | Access/IP lead; 13 Aug 2026 for letter, agreement before field work | Mandatory VibeGuard gate element; determines later evidence accessibility. |
| What exact current legal status and claim scope apply to KCF and other VibeGuard families in India/intended markets? | Patent professional before later protocol expansion | May narrow or kill useful scope; not resolved by claim-text screening. |
| Are oven, calibrated scale and stable drying capacity available for the entire TrueMoist 72-run study? | TrueMoist fallback lead; Week 1 and reconfirm on branch selection | Mandatory fallback feasibility condition. |
| Does ESP32 ADC performance satisfy the frozen QC rule, or is ADS1115 required within budget? | TrueMoist hardware lead; first fallback week | Controls measurement validity and BOM. |
| Can 6–12 traceable probes from at least two lots and three preparation batches be funded for later TrueMoist work? | Project lead/IP office; before later phase | Controls population support for the proposed mechanism. |
| Does TrueMoist’s composite validity logic beat two-point affine plus range gating at usable coverage across remounts/lots? | Metrology lead; two-probe pilot, then later phase | Primary later kill condition. |
| What is the status/claim scope of Indian application `5559/CHE/2014` and its family? | Patent professional before any OpenBraille re-entry | Mandatory OpenBraille re-entry condition. |
| Can isolated high-bandwidth current features predict direct physical Braille-dot truth rather than servo effort? | OpenBraille re-entry lead before practical-scale spend | Earliest OpenBraille technical kill condition. |
| Which university/student/sponsor policy controls ownership, and who conceived each eventual claim element? | Institutional IPR office immediately | Controls disclosure, ownership, inventorship record and filing authority. |

## 36. Source and verification log

The adjudication used only the controlled attachments below plus one narrow primary-source claim-text check. The provenance register controlled files and exclusions; it supplied no technical premise. Synthesis agreement was never counted as a vote.

| Source key | Controlled source | Use in adjudication | Reliability / verification treatment |
|---|---|---|---|
| G0 | `00_READ_FIRST_Project_mC_Final_Adjudication_Instructions.md` | Governing workflow, required decisions, scoring weights, sensitivity cases, gate/output form and 36-section report structure. | Read first and applied as governing. |
| A1 | `01_Project_mC_Decision_Register_v1.2.md` | Binding concept definitions, frozen MVPs, budget, schedule, team, patent-first priority and current decisions. | Highest substantive authority; v1.2 confirmed, v1.1 absent. |
| A2 | `02_Phase3C_Portfolio_Closure_Memo_Approved.md` | Approved portfolio closure and separation of frozen MVP from later patent work. | Common authority; checked against A1. |
| A3 | `03_Concept_Evidence_Matrix.md` | Cross-concept evidence state, budgets, architecture and known-risk normalization. | Common evidence; conflicts resolved by A1 and uncertainty register. |
| A4 | `04_Uncertainty_and_Test_Register.md` | Unknowns, decisive experiments, stop conditions and test burden. | Common evidence; used to prevent false certainty. |
| OB-WM | `05_OpenBraille_Synthesis_Work_Max.md` | Primary OpenBraille prior-art synthesis, D11 route, thresholds, costs, timelines and risks. | High synthesis reliability; concept-faithful and complete. Legal conclusions treated as hypotheses pending claim/status review. |
| OB-2 | `06_OpenBraille_Synthesis_Valid_Secondary.md` | Independent OpenBraille challenge/secondary synthesis. | Medium reliability; complete and faithful. More optimistic Track B treatment was discounted where evidence and sensing bandwidth were weaker than OB-WM. |
| VG-WM | `07_VibeGuard_Synthesis_Work_Max.md` | Primary VibeGuard art map, Level separation, source-conditioned mechanism, field protocol and burden. | High synthesis reliability; concept-faithful and complete. |
| VG-2 | `08_VibeGuard_Synthesis_Standard_High.md` | Independent VibeGuard challenge, comparators, proposed quantitative thresholds and KCF interpretation. | Medium reliability; complete and faithful. Proposed thresholds were adopted only as project gates, not authority facts. KCF conflict checked directly. |
| TM-M | `09_TrueMoist_Synthesis_Max.md` | Primary TrueMoist art map, composite transfer/validity mechanism, population design and burden. | High synthesis reliability; concept-faithful and complete. |
| TM-2 | `10_TrueMoist_Synthesis_High_Deep_Research.md` | Independent TrueMoist challenge, physical-reference transfer route and conservative Track C assessment. | High synthesis reliability; concept-faithful and complete. |
| P0 | `99_EXCLUSION_AND_PROVENANCE_REGISTER.md` | Attachment identity, hashes, completeness, filename crossing and exclusions only. | File-control/reliability context only; not technical evidence. |
| V1 | [US10873791B1, Google Patents claim text](https://patents.google.com/patent/US10873791B1/en) | Narrow resolution of a material synthesis conflict: claim 1’s networking/compression context versus dependent claims 4 (FFT magnitude-baseline subtraction) and 9 (baseline regeneration after spectral deviation). | Primary patent publication checked on 3 Aug 2026. Used only for the stated claim-text point; legal status, family scope, construction, validity and FTO remain unverified. |

### Exclusion compliance

No other adjudication output was used. No prior-chat fact, score, recommendation or missing-file inference was used. The absent OpenBraille moving-roller synthesis, absent VibeGuard software-security synthesis and absent supplementary TrueMoist Work Max web audit supplied no technical content. The six selected syntheses were normalized as evidence-bearing reports, not as six votes. All forecasts and scores in this report are the adjudicator’s transparent decision model tied to the controlled evidence above.
