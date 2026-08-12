# Source Extraction

- Chapter: `07` — VibeGuard Patent Evidence and Future Research Path
- Authority tier: `TIER_3`
- Manual treatment: `SUPPORTING_EVIDENCE`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/02_Raw_Research/01_VibeGuard_Patent_Research_ChatGPT_Deep_Research.md`
- SHA-256: `8614a18e8d7764437315a41b61ed46f4fb3e2dcd6eaa8b12e59a0b57ffdd79a7`
- Extraction method: `PLAIN_TEXT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

# VibeGuard Current Patent Verification — Independent Research

**Research cut-off:** 31 July 2026
**Prepared as:** an independent patent-and-technical research pass, not a synthesis of other models
**Scope disclaimer:** This is technical research and project decision support. It is not legal advice, a patentability guarantee, a validity opinion, claim construction, an infringement conclusion, or a freedom-to-operate opinion.

---

## Executive verdict

**Required verdict:** **credible long-term path requiring later-semester extension**
**Track:** **Track C**
**Confidence:** **Medium**
**Most important limitation:** The frozen semester MVP can prove normal-versus-deliberately-imbalanced classification on one isolated rig, but it cannot prove that one sensor attributes an abnormal condition to its mounted target machine when neighbouring machines or structural interference vary independently.
**Should the frozen MVP itself be treated as the invention?** **No.**

The frozen VibeGuard MVP—one rigidly mounted accelerometer, local sampling, DC removal, windowing, common time-domain features, triggered FFT, baseline thresholding, Mahalanobis-distance anomaly scoring, band-limited processing and a simple alert—is a technically coherent and affordable semester prototype. However, the reviewed patent and non-patent landscape shows that these elements, separately and in routine combinations, are longstanding condition-monitoring practice. Baseline acquisition, vibration fingerprints, statistical limits, FFT-derived features, operating-state normalization and automatic vibration diagnosis also appear in older and live patent families.

A credible connected patent-development route remains, but only if later work produces a **specific physical measurement method** that demonstrably improves one-sensor target-machine attribution or installation robustness. The strongest route is not generic “spectral subtraction.” It is a narrowly defined **confidence-gated target-fingerprint method** that: (1) calibrates the target under independently known target and interferer states; (2) models permitted speed/load and mounting variation; (3) refuses or abstains from a target-fault label when interference makes attribution unreliable; and (4) prevents contaminated data from entering the normal baseline. That contribution must outperform ordinary RMS, FFT features, fixed subtraction, and ordinary one-class/Mahalanobis baselines across independently controlled target/interferer states and remounting sessions.

No searched reference was verified as an exact anticipation of that full bounded sequence. That absence does **not** establish novelty or inventive step. Several close references occupy most of its building blocks, so obviousness risk remains high until a non-routine update, confidence, or deployment mechanism and its measurable technical effect are defined and tested.

---

## Input inventory and concept-fidelity confirmation

### Inventory result

The governing instruction file was readable. All ten canonical project inputs were attached and readable, although several uploaded filenames contain numbering prefixes and duplicate-name suffixes such as “(5)”. The content corresponds to the canonical documents specified by the governing file.

| Canonical input | Attached file | Result |
|---|---|---|
| Engineering_Design_Review.md | `01_Engineering_Design_Review(5).md` | Present/readable; filename decorated |
| Project_mC_Decision_Register_v1.2.md | `02_Project_mC_Decision_Register_v1.2(5).md` | **v1.2 present/readable; v1.1 not substituted** |
| Phase3C_Portfolio_Closure_Memo_Approved.md | `03_Phase3C_Portfolio_Closure_Memo_Approved(5).md` | Present/readable; filename decorated |
| Phase3C_VibeGuard_Architecture_Report_Final.md | `04_Phase3C_VibeGuard_Architecture_Report_Final.md` | Present/readable |
| Phase3C_VibeGuard_Memory_Final.md | `05_Phase3C_VibeGuard_Memory_Final.md` | Present/readable |
| Phase3C_VibeGuard_SOP_Final.md | `06_Phase3C_VibeGuard_SOP_Final.md` | Present/readable |
| 03_Concept_Evidence_Matrix.md | `07_Concept_Evidence_Matrix(5).md` | Present/readable; renamed and decorated |
| 05_Uncertainty_and_Test_Register.md | `08_Uncertainty_and_Test_Register(5).md` | Present/readable; renamed and decorated |
| 06_Patent_Research_Input_Pack.md | `09_Patent_Research_Input_Pack(5).md` | Present/readable; renamed and decorated |
| Phase2_Report by CLaude.md | `10_Phase2_Report_by_Claude(5).md` | Present/readable; punctuation/case normalized |

**Missing inputs:** none.
**Duplicate inputs:** no duplicate content was identified among the eleven attachments, which comprise one governing instruction file plus ten canonical inputs.
**Unreadable inputs:** none.
**Ambiguity:** only naming decoration; the contents and authority order resolve the identities.

### Frozen concept confirmation

The research treated VibeGuard as:

- passive detection and alerting;
- one rigidly mounted ADXL345 three-axis accelerometer;
- SPI acquisition into an ESP32-WROOM-32 or ESP32-S3-class MCU;
- local edge processing without cloud dependence;
- DC removal, Hann windowing, continuous low-cost features and triggered FFT;
- calibrated RMS/persistence as the minimum classifier;
- multivariate Mahalanobis anomaly detection as the primary target classifier;
- baseline spectral subtraction, proximity mounting and band-limited features as the baseline noise strategy;
- a motor/fan eccentric-mass bench demonstration for Level 1 evidence;
- possible later single-node target attribution under neighbouring-machine interference for Level 2 evidence.

It was **not** treated as active vibration cancellation, haptics, a wearable device, a multi-sensor array, an audio detector, a cloud predictive-maintenance platform, a remaining-useful-life system, or an industrial high-frequency bearing-fault detector using ADXL345.

---

## Search methodology and reproducible search log

### Method

The pass used keyword, assignee, inventor/family, classification and citation-chain searching. Google Patents was used for discovery, readable claims and family navigation. Important legal-status statements were limited to what could be corroborated from displayed prosecution/family data; Google’s status labels are treated as discovery evidence rather than a legal opinion. Official USPTO, EPO, IP India and ISO materials were used for eligibility and standards context.

The principal classes encountered were:

- **G01H** — measurement of mechanical vibrations or ultrasonic/sonic/infrasonic waves;
- **G01M 13/** — testing of machine parts and mechanical structures;
- **G05B 23/** — monitoring or diagnostic arrangements for control systems and machinery;
- **G06N / G06F** subclasses where statistical or learning-based anomaly analysis is claimed;
- condition-monitoring subclasses involving rotating machinery, operating-speed normalization and spectral analysis.

### Representative reproducible search log

| Source/date | Exact or materially equivalent query | Selection rationale |
|---|---|---|
| Google Patents / web, 31 Jul–1 Aug 2026 | `US 7421349 bearing fault signature detection` | Mandatory historical Navy lead |
| Google Patents / web | `single sensor machine vibration attribution patent` | Target-attribution search |
| Google Patents / web | `machine fault neighboring machine noise patent` | Interference/crosstalk search |
| Google Patents / web | `vibration spectral subtraction condition monitoring patent` | Frozen subtraction feature |
| Google Patents / web | `Mahalanobis vibration anomaly machine patent` | Multivariate baseline search |
| Google Patents / web | `baseline vibration features machine operating speed patent` | Baseline/fingerprint and state-normalization search |
| Google Patents / web | `mounting transfer vibration sensor calibration patent` | Mount/remount direction |
| Google Patents / web | `adaptive baseline contamination anomaly vibration patent` | Drift/update safeguard direction |
| Google Patents / web | `resource constrained triggered FFT vibration condition monitoring patent` | Two-stage compute direction |
| Google Patents / web | `Tractian vibration fault detection patent` | Mandatory named lead |
| Google Patents / web | `Infinite Uptime vibration monitoring patent` | Mandatory named lead |
| Google Patents / web | `Augury mechanical vibration patent` | Mandatory named lead |
| Google Patents / web | `KCF Technologies vibration sensor patent` | Mandatory named lead |
| Google Patents / web | `Senseye condition monitoring patent vibration` | Mandatory named lead; no equally close identifiable family found in this pass |
| Google Patents / web | assignee and citation-chain searches around SKF, GE, Siemens, Hitachi and industrial diagnostic patents | Major industrial landscape expansion |
| ISO official site | `ISO 20816 machine vibration` | Current measurement/evaluation standard context |
| USPTO official site | subject-matter eligibility, MPEP 2106 | US eligibility framework |
| EPO official site | CII technical effect guidelines | European eligibility/technical contribution framework |
| IP India official site | CRI Guidelines 2025 | Indian computer-related-invention framework |

Search limitations are recorded in the unresolved-questions section. In particular, this pass did not obtain counsel-grade INPADOC legal-event verification for every family or full official-file wrappers for every national member.

---

## Technical and patent landscape map

The landscape separates into six crowded layers:

1. **Physical vibration acquisition.** Contact-mounted accelerometers and wireless vibration sensors are mature. KCF’s family claims sensor-packaging and wireless-accelerometer structures, while many industrial families cover acquisition arrangements.
2. **Baseline/fingerprint comparison.** Older families compare current vibration with stored base features, operating-speed-indexed fingerprints or statistical norms.
3. **Spectral decomposition and fault features.** FFT, harmonics, order-related components, envelopes, sidebands, kurtosis and spectral peak selection are extensively disclosed.
4. **Automatic diagnosis and learning.** Augury, Tractian, Hitachi and others claim automated analysis using spectral relationships, learned models or condition classifiers.
5. **Operating-state normalization.** Live patents and older art normalize or select baselines by speed, load or other machine operating conditions.
6. **Source discrimination.** The Navy bearing-signature family distinguishes fault-related peaks from unrelated processes using phase relationships. Other source-separation methods are known in vibration and acoustics, although a verified exact one-sensor, target-mounted, neighbour-varying, abstaining method was not found.

The frozen MVP sits inside layers 1–5. A potential contribution must therefore be more specific than “single sensor,” “edge,” “no cloud,” “low cost,” “FFT,” “Mahalanobis” or “spectral subtraction.”

---

## Verified patent-family ledger

“Verified” below means that the publication, assignee/family relationship and relevant disclosed or claimed subject matter were checked in a patent record during this pass. Status remains a research indication, not a legal opinion.

| Family / record | Indicative status | Relevant independent-claim or disclosure focus | Relevance |
|---|---|---|---|
| **US 7,421,349**, *Bearing fault signature detection* (US Navy) | Granted 2008; old patent, expiration/status must be confirmed from official record | Bearing-fault peaks distinguished from coincident peaks of unrelated processes using phase-coupling relationships | Highly relevant prior art to “unrelated process” discrimination; not the same as the frozen subtraction approach |
| **US 7,133,801 B2**, *System and methodology for vibration analysis and condition monitoring* | Expired/fee-related indicated | Base vibration features, contact transducer, operating-speed estimate and comparison to detect faults | Strong novelty/obviousness art for baseline fingerprints and speed-aware comparison |
| **US 9,176,003 B2**, *Machine vibration monitoring* | Active indicated, expiry 2031 | Composite vibration separated into vectors associated with machine frequency and linked to operating conditions/statistical values | Relevant to vector/band analysis and operating-condition normalization; possible FTO concern only if every live-claim element is practiced |
| **US 8,290,630 B2 / EP 2,169,497**, condition-monitoring parameter normalization | US grant and EP publication | Calculate vibration parameters, normalize them and present alarms, including frequency-band scaling | Relevant to normalized vibration features and band alarms |
| **US 11,429,900 B1**, Tractian, automatic detection of error conditions | Granted 2022; assignment to Tractian Technologies recorded in 2026 | Machine-mounted sensor, transmission/compression/reconstruction and remote ML fault model | Commercially close but materially cloud/remote oriented; less direct to local-only MVP |
| **BR 102022005021 A2**, Tractian counterpart | Published | Same broad family subject | Confirms non-US filing activity |
| **US 9,835,594 B2 / US 10,983,097 B2 / EP 2,909,685 / IN2015DN04150A**, Augury automatic diagnosis family | US grants; EP/IN members identified | Vibration/acoustic data, spectral relationships/patterns and automatic mechanical-system diagnosis | Strong art against generic fingerprint-based automatic diagnosis; Indian member identified |
| **WO 2018/198111 / EP 3,615,899**, Augury monitoring machines | Published/pending or national status varies | Monitoring mechanical/electrical machines with sensor data and diagnostic processing | Broad industrial monitoring adjacency |
| **EP 3,877,819 B1**, Augury non-stationary machine performance | Granted January 2026, active indicated | Analysis of non-stationary machine performance | Relevant to variable operating-state normalization |
| **US 12,607,995 B2 / US 2024/0255942**, Augury continuation | Granted April 2026 | Automated analysis of non-stationary performance | Current live family to review before speed/load-normalized design freeze |
| **WO 2017/151447 / US 2019/0061086**, Infinite Uptime/UC, magnetic add-on system | Publication/application status varies | Magnetic add-on with vibration and acoustic sensing for tool condition monitoring | Relevant to mounting, multi-modal sensing and commercial SME node landscape; not a single-sensor attribution claim |
| **US 9,453,854 B2 / EP 2,913,643**, KCF vibration sensor | US grant with maintenance fees indicated; EP publication | Wireless accelerometer/vibration-sensor construction | Hardware/package FTO adjacency, not generic algorithm ownership |
| **KR 2015-0120160 A**, machine-tool abnormal-vibration determination | Published Korean application | Mahalanobis-Taguchi multivariate vibration factors and abnormal-vibration decision, with control response | Direct evidence that Mahalanobis-based vibration abnormality is not new |
| **US 11,333,580 B2** and **US 11,500,965 B2**, anomaly detection using Mahalanobis/MT | Active grants indicated | Mahalanobis normal-space anomaly detection and contribution/localization analysis | Broad evidence that ordinary Mahalanobis anomaly scoring is mature |
| **US 2021/0231528 A1**, separating periodic peaks from non-periodic peaks | Published | Kurtosis-driven separation of periodic candidate peaks in machine vibration spectra | Relevant to kurtosis and peak-selection approaches |
| **US 12,140,507 B2**, vibration detection/abnormality system | Granted 2024, active indicated | Detecting vibration of a target machine and determining abnormality | Recent broad target-machine vibration art requiring claim-level design review |
| **US 12,276,541 B2 / WO 2021/220162**, non-invasive vibration condition monitoring | US grant 2025 | Non-invasive condition monitoring family | Recent landscape evidence; full independent-claim mapping remains unresolved |

### Ledger conclusions

- No identified family grants exclusive ownership of “an accelerometer plus FFT plus Mahalanobis on an ESP32.”
- Multiple families disclose enough of that combination’s ingredients to create **high obviousness risk**.
- Live-claim FTO risk is more likely to arise from a specific diagnosis workflow, remote architecture, sensor package, operating-state relationship or source-discrimination technique than from using common statistical features themselves.

---

## Closest independent-claim analyses

### 1. US 7,421,349 — bearing fault signature detection

**Claim concept reviewed:** determine whether spectral peaks are generated by a bearing fault by examining phase coupling between peaks, thereby separating fault signatures from coincidental peaks caused by unrelated processes.

**Overlap with VibeGuard:** vibration spectrum; machine-fault monitoring; discrimination from unrelated vibration components.

**Differences:** the frozen MVP proposes baseline spectral subtraction, band limits and anomaly scoring, not phase-coupling/bispectral identification. It also does not initially diagnose a bearing fault.

**Effect:** strong novelty and obviousness art against a broad claim to “one sensor distinguishing a machine fault from neighbouring noise.” It is not a verified literal read on the frozen system. Any future method should avoid casually adopting the claimed phase-coupling sequence without a formal live-claim analysis.

### 2. US 7,133,801 B2 — base vibration features and speed estimation

**Claim 1 elements reviewed:** establish base vibration features; acquire time-domain vibration from a contact transducer; estimate machine speed from vibration; obtain vibration at that speed; detect faults by comparison with the base features.

**Overlap:** contact-mounted sensor, stored baseline, local/current vibration and fault/anomaly comparison.

**Differences:** VibeGuard’s frozen MVP need not estimate speed using the claimed continuous-vibration model and does not necessarily maintain speed-indexed base features.

**Effect:** anticipates or strongly suggests broad baseline-fingerprint ideas. Speed/load-normalized fingerprints can only support a new claim if the specific permitted information, update mechanism, attribution logic and technical improvement differ materially.

### 3. US 9,176,003 B2 — vector components and operating conditions

**Claim 1 elements reviewed:** measure composite vibration; measure multiple operating conditions; filter a vibration vector at a measurement time; select an operating-condition state; store and evaluate associated information.

**Overlap:** composite vibration processing, selected frequency/vector features, operating-state context and statistical comparison.

**Differences:** the frozen MVP presently has no separate operating-condition sensor and does not implement the claim’s full state-selection structure.

**Effect:** a future speed/load-normalized design must be claim-charted. Merely adding speed/load labels to a vibration baseline is unlikely to be inventive.

### 4. Augury automatic mechanical-system diagnosis family

**Independent-claim theme:** obtain vibration-related data from a machine, identify spectral relationships or machine-state patterns and automatically diagnose a mechanical condition, in some claims using reference or expert information.

**Overlap:** machine-attached vibration sensing, spectral features, automatic state decision.

**Differences:** VibeGuard is local-only and initially anomaly-oriented, not a remote expert diagnostic platform. The proposed abstention and contaminated-baseline safeguards were not verified as required elements of the reviewed Augury claims.

**Effect:** broad diagnosis/fingerprint claims are unsafe as an invention narrative. A future filing would need to center on a concrete interference/installation mechanism and measured physical effect.

### 5. Tractian US 11,429,900 B1

**Independent-claim theme:** sensor on a mechanical machine; vibration data may be compressed and transmitted; remote processing reconstructs data; a trained ML model detects error-condition patterns.

**Overlap:** machine sensor and automatic fault decision.

**Differences:** remote processing, data reconstruction and trained model are central; frozen VibeGuard is local and unsupervised/statistical.

**Effect:** limited literal overlap with the MVP, but strong evidence that “low-cost sensor + learned fault detection” is commercially and legally occupied.

### 6. KR 2015-0120160 A and general MT/Mahalanobis art

**Independent-claim theme:** receive multiple machine-tool characteristic factors, compute a Mahalanobis/MT abnormal-vibration measure, compare with a limit and determine abnormal vibration, sometimes calculating a speed to avoid it.

**Overlap:** multivariate features, normal-space model, Mahalanobis distance and abnormal-vibration threshold.

**Difference:** VibeGuard’s exact feature set, local hardware and alert-only action differ, but those are ordinary implementation choices.

**Effect:** Mahalanobis distance plus common vibration features should be treated as conventional and not claim-relevant by itself.

---

## Frozen-MVP feature comparison

Legend: **E** expressly disclosed; **I** necessarily implied or routine implementation; **S** arguably suggested; **A** absent from the reviewed closest set; **U** unresolved.

| Frozen feature | Closest-art position | Assessment |
|---|---|---|
| One ADXL345 | U | Exact part is not important to inventive step; accelerometers are ubiquitous |
| SPI to ESP32 | A/I | Ordinary interface/platform selection; no novelty weight |
| Local/no cloud | E/S | Edge/local systems predate the MVP; cannot carry novelty alone |
| DC removal | I | Routine signal preprocessing |
| Hann window | I | Routine FFT practice |
| RMS/peak/std/crest/kurtosis | E/S | Common vibration features; kurtosis and peak methods patented/published |
| Threshold + persistence | E/S | Conventional alarm logic |
| Triggered FFT | S | Resource scheduling is plausible but routine unless tied to a non-obvious measured result |
| Baseline spectral subtraction | E/S | Difference/background subtraction is old; exact contamination-safe update not verified |
| Band-limited features | E | Frequency-band/vector analysis is old |
| Mahalanobis score | E | Directly old in anomaly and vibration contexts |
| Single-node operation | E/S | Common product architecture; not equivalent to attribution |
| Normal-baseline acquisition | E | Old baseline/fingerprint practice |
| Neighbour interference handling | E/S | Navy and broader source-discrimination art exists; frozen method unproven |
| Confidence/abstention | S/U | Confidence and reject options are known generally; exact target-attribution gating not verified |
| Adaptive baseline update | S/E | Adaptive baselines are known; contamination safeguard could be a narrow development area |
| Remounting compensation | S/U | Transfer-function and installation calibration are known fields; exact one-node method unresolved |
| Target attribution | S/U | Broad problem old; exact bounded sequence not found |
| RGB alert | E/I | Trivial output |
| Eccentric-mass rig | E/I | Standard lab fault simulation; evidence tool, not invention |
| Compute/memory limits | I | Design constraint; claim relevance only if a specific scheduling method preserves measured performance |

**Conclusion:** No frozen-MVP feature, and no presently defined combination, supports Track A.

---

## Mandatory named-lead investigation

### US 7,421,349 / US Navy

The lead is real and correctly titled *Bearing fault signature detection*. It is important prior art for distinguishing fault-related peaks from unrelated processes. Its method is more specific than generic subtraction and appears to rely on phase coupling. It therefore narrows, but does not automatically eliminate, a different confidence-gated fingerprint approach.

### Tractian

A directly identified family is US 11,429,900 B1 with Brazilian member BR 102022005021 A2. It claims a machine-mounted vibration sensor feeding remote processing and a trained model for mechanical error detection. Tractian therefore occupies automatic vibration-fault detection and remote learned diagnosis, but the reviewed claim theme is not the same as a local one-class, abstaining attribution method.

### Infinite Uptime

WO 2017/151447 and US 2019/0061086 identify Infinite Uptime and university co-assignees on a magnetic add-on sensing system using vibration and acoustic capabilities for tool condition monitoring. This confirms actual patent-family activity. It is more relevant to mounting/package and multi-modal monitoring than to the proposed one-sensor attribution rule.

### Augury

Augury has a substantial identifiable family set: automatic mechanical diagnosis (US 9,835,594; US 10,983,097; EP 2,909,685; Indian publication IN2015DN04150A), machine monitoring (WO 2018/198111 / EP 3,615,899) and active 2026 grants concerning non-stationary machine performance (EP 3,877,819 B1 and US 12,607,995 B2). These families are load-bearing evidence that spectral fingerprints, automatic diagnosis and operating-state handling are crowded.

### KCF Technologies

KCF’s US 9,453,854 / EP 2,913,643 family concerns a vibration sensor including a wireless accelerometer. It is relevant to sensor/package design and wireless deployment, not a broad right to vibration monitoring algorithms.

### Senseye

Senseye is an identifiable commercial predictive-maintenance platform, but this pass did not verify an equally close Senseye-assigned vibration-attribution patent family. It should not be represented as holding a specific blocking family without further assignee and ownership-chain searching. Siemens/Senseye-related portfolio transfers and parent ownership may complicate assignee-name searching.

### Other industrial actors

SKF, GE, Siemens, Hitachi and other industrial firms have extensive machine-condition and vibration-monitoring portfolios. The selected ledger includes examples of position-correlated Fourier analysis, operating-condition normalization and robotic vibration anomaly detection. This reinforces crowding but does not replace claim mapping for a final design.

---

## Non-patent prior art and standards

1. **ISO 20816-1:2016** provides general procedures for measuring and evaluating machine vibration and uses vibration magnitude and changes for operational monitoring and acceptance. A second edition was in FDIS processing in 2026. This demonstrates that vibration magnitude, change, measurement position, operating conditions and vibration from other sources are standardized engineering concerns, not VibeGuard-specific discoveries.
2. Lab machinery datasets routinely use normal, imbalance, misalignment and bearing-fault conditions with conventional classifiers. Excellent cross-validation on isolated laboratory datasets does not prove source attribution or field robustness.
3. The vibration-diagnostics literature has long used RMS, crest factor, kurtosis, spectra, envelopes, sidebands, order tracking and one-class/statistical anomaly methods.
4. Spectral subtraction is well established in signal denoising generally. Applying a fixed background spectrum to machine vibration is an expected engineering adaptation unless the acquisition/update/contamination rule yields an unexpected technical result.
5. Transfer functions and sensor-position compensation are established measurement concepts. A remounting method would need a narrowly defined calibration stimulus, invariant representation or compensation protocol and evidence that it preserves diagnosis after reinstallation.

The literature strongly supports the engineering feasibility of Level 1 bench classification. It does not support treating the isolated rig as evidence of Level 2 attribution.

---

## Current frozen-MVP patent assessment

### Novelty

The exact bill of materials and exact sequence may not appear verbatim in one searched document. That is insufficient. Every material element is known, and several references combine baseline comparison, machine-state normalization, spectral vectors and automatic anomaly decisions. The frozen MVP therefore has **low prospective novelty confidence**.

### Inventive step

An examiner could plausibly combine:

- ordinary contact accelerometer monitoring;
- baseline/fingerprint comparison;
- time and spectral features;
- a Mahalanobis normal-space detector;
- fixed background subtraction or band selection;
- a resource-motivated two-stage pipeline;
- a local MCU and an alert.

The combination addresses predictable cost and compute constraints with expected techniques. No unexpected result is currently defined. **Obviousness risk: High.**

### Eligibility

A claim limited to calculating features and a distance score risks being characterized as mathematical analysis. Eligibility improves when the claim is tied to a particular sensor-machine relationship, controlled calibration states, a physical interference condition, and a measurable improvement in machine-state measurement or alert reliability. Even then, eligibility does not establish novelty or inventive step.

### FTO

The frozen MVP is unlikely to infringe every element of the closest reviewed claims merely by using an accelerometer and common DSP. However, no safe FTO conclusion is possible. Particular risk areas are adopting a claimed phase-coupling workflow, a live operating-state vector/normalization claim, a patented sensor package, or a commercial remote-diagnosis architecture. **Indicative FTO risk for the bench MVP: Low-to-Medium; uncertainty Medium.**

---

## Candidate invention-direction matrix

| Direction | Exact proposed contribution | Prior-art/ordinary-practice pressure | Three-month fit | Track / verdict |
|---|---|---|---|---|
| Frozen MVP combination | ADXL345 + tiered features + Mahalanobis + subtraction | Very high; routine aggregation | High | Reject as invention; Track D if standing alone |
| Single-node attribution under neighbour interference | Attribute target fault despite independently varying neighbour | Broad problem and phase-coupling art old; exact method unresolved | Low for credible proof | **Track C candidate** |
| In-situ target fingerprint from known states | Build target baseline using known target on/off/speed states | Baseline and speed-indexed fingerprints old | Medium | Weak alone; combine only |
| Contamination-protected subtraction/update | Update noise/target baseline only under verified safe states and reject contaminated windows | Adaptive baselines known; exact gate may be narrow | Medium | Track B experiment, Track C patent confidence |
| Confidence-gated abstention | Output target fault only when target evidence exceeds interference ambiguity; otherwise “unknown” | Reject options known generally; physical attribution effect could matter | Medium | **Strong component of Track C** |
| Remounting compensation | Calibrate mounting transfer and preserve feature meaning after reinstall | Transfer/installation calibration known; exact protocol unresolved | Medium | Secondary Track B/C candidate |
| Resource-aware triggered FFT | Cheap features select FFT bands/windows while preserving attribution performance | Obvious compute optimization unless unexpected result | High | Reject alone |
| Speed/load-normalized fingerprint | Normalize target signature by permitted state input | Strong older/live prior art | Medium | Reject alone; use as necessary control |
| Drift-aware baseline adaptation | Update normal model with anomaly/interference safeguards | Known general concept; exact contamination logic may be narrow | Medium | Component, not standalone |
| Deployment/source-label protocol | Single-node calibration sequence using independently controlled target/interferer states | Experimental protocols often obvious; technical calibration interaction could matter | Medium | Supporting method, not enough alone |

### Direction decisions

- **Rejected clearly:** generic triggered FFT, generic Mahalanobis, generic spectral subtraction, generic adaptive baseline, low-cost edge node and isolated imbalance rig.
- **Retained only as a combined research hypothesis:** confidence-gated target fingerprint with contamination-protected baseline handling and installation/state controls.

---

## Strongest surviving direction

### Working title

**Confidence-gated, contamination-protected single-node target-machine vibration attribution**

### Exact technical problem

A sensor attached to one target machine receives a structural mixture of target vibration, neighbouring-machine vibration, transient shocks and mounting-transfer effects. A conventional anomaly score may rise even when the target remains healthy. The technical problem is not detecting “more vibration”; it is deciding when the measured evidence is sufficiently attributable to the target to issue a target-fault alert.

### Proposed bounded contribution

1. Collect calibration windows under independently known combinations of target state and interferer state.
2. Construct a target fingerprint containing target-coherent bands/features and an interference-ambiguity model.
3. Estimate whether a live window is inside an approved target operating-state and mounting-validity region.
4. Compute target anomaly evidence and interference ambiguity separately.
5. Issue **Normal**, **Target abnormal**, or **Unknown/abstain**, rather than forcing every anomaly into a target-fault label.
6. Update normal/background statistics only when target state, interference confidence and anomaly score satisfy a contamination-protection gate.
7. After remounting, require a short transfer-validation sequence or invalidate the prior baseline.

### Measurable technical effect

Compared with RMS, ordinary FFT features, ordinary Mahalanobis and fixed spectral subtraction, the method should reduce false target-fault alarms and attribution errors when the neighbour changes state, without unacceptable missed detection of the target’s induced imbalance. It should also prevent a neighbour-abnormal or target-abnormal window from being learned as normal.

### Risks

- Confidence/abstention, adaptive updates and validity regions are well-known general techniques.
- Combining them with vibration attribution may be seen as routine unless the exact physical calibration and update sequence produces a substantial, repeatable improvement.
- A real field test with independent ground truth is likely necessary for patent-first confidence.

### Track

**Track C.** A limited two-motor bench implementation can begin within three months, but the strongest evidence requires later field access, repeated mounting sessions and independently controlled/known machine states.

---

## Bench demonstration versus field-attribution evidence

### Level 1 — semester bench demonstration

A single damped motor/fan, normal versus fixed eccentric mass, can validate:

- acquisition stability;
- low-frequency imbalance sensitivity within ADXL345 bandwidth;
- local feature computation;
- threshold and Mahalanobis operation;
- RGB alert behavior;
- compute, RAM, latency and repeatability.

It cannot validate:

- attribution to the target under variable neighbours;
- industrial fault diagnosis;
- bearing-fault detection;
- remounting invariance;
- adaptive-baseline safety;
- field false-alarm rate.

### Level 2 — patent-oriented attribution

A controlled two-motor rig should randomize at least:

- target normal / target imbalanced;
- interferer off / normal / imbalanced;
- target and interferer speed/load;
- mounting and remounting sessions;
- repeated days;
- startup, shutdown and transient shocks.

Independent state labels are mandatory. “The algorithm said the neighbour was abnormal” is not ground truth. Field evidence should follow only after the rig establishes basic feasibility.

---

## Novelty analysis

### Frozen MVP

No credible novelty conclusion. Exact implementation novelty is possible in a literal sense, but patent novelty must be assessed claim by claim, and the meaningful elements are found across close references.

### Strongest direction

Potentially differentiating elements are:

- separate target-anomaly and interference-ambiguity estimates;
- an explicit abstention state tied to physical source ambiguity;
- calibration with independently known target/interferer combinations;
- contamination-protected normal-model updates;
- baseline invalidation or transfer validation after remounting.

No single reviewed reference was confirmed to require all five in combination. Novelty confidence is nevertheless only **Low-to-Medium**, because the search was not exhaustive and each constituent concept is known.

---

## Inventive-step / obviousness analysis

The strongest rejection case would combine:

1. base vibration features and speed/state comparison from older machine-monitoring patents;
2. unrelated-process discrimination from the Navy phase-coupling art;
3. ordinary one-class/Mahalanobis detection;
4. known confidence/reject-option logic;
5. known adaptive-baseline contamination controls;
6. known installation or transfer calibration.

The applicant would need to show more than the predictable result of that combination. The best rebuttal would be a pre-registered experiment demonstrating that a particular calibration/gating sequence achieves a material reduction in target-attribution errors under neighbour state changes while using a constrained single node, and that simpler combinations do not.

**Risk:** High before experiments; potentially Medium if a strong, unexpected effect is reproduced across remounting and field sessions.

---

## Patent-eligibility analysis

### United States

USPTO guidance applies the statutory-category and judicial-exception framework. A bare feature-vector, Mahalanobis and confidence calculation could be treated as an abstract mathematical analysis. Eligibility is stronger where the claim recites a vibration sensor physically coupled to a target machine, specific calibration under independently controlled machine states, technical processing that changes the reliability of the physical measurement, and an alert/abstention operation based on that improved measurement. The specification should describe the technological improvement and evidence, not merely state “use AI.”

### Europe

EPO computer-implemented-invention practice requires claim features essential to the technical effect. Processing sensor data to improve the measurement or monitoring of a physical machine can contribute technically, but mathematical features count toward inventive step only insofar as they cause a technical effect. A claim should define the sensor-machine coupling, calibration states, interference handling and physical monitoring effect.

### India

India’s 2025 CRI Guidelines and the statutory exclusion of mathematical methods/computer programs per se make a pure algorithm claim risky. The strongest presentation is a technical vibration-measurement and machine-monitoring method producing a demonstrable physical/technical effect, implemented through a defined sensor and embedded system. Eligibility remains separate from novelty and obviousness.

---

## FTO risk analysis

### Bench MVP

- **Sensor and interface:** generally low algorithmic FTO concern, but avoid copying proprietary sensor-package claims.
- **Common features/FFT/Mahalanobis:** use is not automatically free merely because mathematically known, but no reviewed live claim was mapped as covering the complete frozen implementation.
- **Phase coupling:** do not adopt the Navy patent’s exact workflow without current official status and claim analysis.
- **Operating-state vector analysis:** review US 9,176,003 and active Augury non-stationary families before adding sophisticated speed/load state logic.
- **Remote learned diagnosis:** remaining local avoids central Tractian claim themes identified here.

### Strongest future direction

FTO risk rises to **Medium** because the method would enter source discrimination, adaptive baselines, machine-state normalization and installation calibration. A professional search should be run on the final exact sequence before public disclosure or productization.

No infringement conclusion is made.

---

## Claim-to-experiment map

| Prospective element | Nearest art | Baseline | Proposed experiment | Success evidence | Failure evidence |
|---|---|---|---|---|---|
| Independently labelled target/interferer calibration | Baseline/fingerprint and phase-coupling art | Target-only calibration | 2×2 target/interferer state calibration and held-out randomized trials | Lower attribution error than target-only calibration | No gain or unstable fingerprints |
| Separate anomaly and ambiguity scores | Mahalanobis and confidence methods | Single anomaly score | Compare forced binary output vs three-state abstention | Fewer false target-fault alarms at controlled abstention rate | Missed faults rise excessively or no false-alarm reduction |
| Contamination-protected update | Adaptive baseline practice | Ungated rolling update | Inject target/neighbor faults during update periods | Normal model does not absorb abnormal windows; recovery after drift | Abnormal data learned as normal or model freezes under benign drift |
| Remount validation/invalidation | Transfer-function calibration art | Reuse old baseline blindly | Reinstall sensor across sessions with defined torque/bracket | Maintains separation or correctly requests recalibration | Old baseline produces overlapping distributions/false alarms |
| Resource-aware selected analysis | Triggered FFT practice | Continuous FFT and RMS only | Measure compute/RAM/energy and attribution metrics | Similar attribution with materially lower compute/power | Performance loss or negligible resource benefit |

### Proposed pre-registration metrics

These are recommendations, not frozen project facts:

- balanced accuracy;
- sensitivity and specificity;
- target-attribution error;
- false target-fault alarms per hour;
- missed detections;
- abstention/unknown rate;
- confidence calibration error;
- detection delay;
- remounting repeatability;
- compute time, RAM, flash, sample rate and power.

Owner-approved numerical pass thresholds should be frozen before final testing.

---

## Three-month semester plan

### Weeks 1–2 — measurement integrity

- Procure and authenticate ESP32, ADXL345 and two safe motor/fan units.
- Build a rigid, repeatable sensor bracket and eccentric-mass fixture.
- Verify sample timing, axes, bandwidth boundary and SPI integrity.
- Log raw data; do not tune on every collected trial.

### Weeks 3–4 — conventional baselines

- Implement RMS/persistence.
- Implement ordinary FFT-band features.
- Implement Mahalanobis normal-space score.
- Measure compute/RAM/latency.

### Weeks 5–6 — interference rig

- Add independently controlled interferer.
- Run randomized target/interferer state combinations.
- Evaluate fixed spectral subtraction and band selection.

### Weeks 7–8 — bounded enhancement

- Add three-state Normal / Target abnormal / Unknown decision.
- Add gated baseline update and contamination tests.
- Add mounting validity check or forced recalibration after remounting.

### Weeks 9–10 — locked evaluation

- Freeze parameters.
- Run held-out sessions and ablations.
- Report false alarms, misses, attribution errors and abstention.

### Weeks 11–12 — documentation and IPR gate

- Separate public conventional implementation from confidential rules/results.
- Prepare claim-to-experiment evidence and failure analysis.
- Conduct institutional IPR review before posters, repositories or papers.

The semester MVP remains viable even if the patent enhancement fails.

---

## Later-semester or publication extension

The Track C extension requires:

- access to at least one real environment containing a target and independently varying neighbouring machinery;
- independently known target/interferer states;
- repeated days and operating regimes;
- a documented mounting/remounting protocol;
- larger datasets and locked external validation;
- possible machine-speed/load inputs, if permitted without changing the single vibration-node product architecture;
- possibly an IIS3DWB or industrial accelerometer only if the research question expands to higher-frequency phenomena; this is not required for low-frequency attribution;
- approximately one additional semester, depending on field access;
- a larger validation budget for mounts, replacement sensors, tachometer/reference instrumentation and travel/site access.

Publication value remains even if patentability fails: a rigorously labelled dataset and negative/positive results on single-node attribution, remounting and baseline contamination would be useful research.

---

## Budget, compute and team feasibility

### Semester MVP

The canonical ₹1,700–₹2,200 ADXL345 route remains plausible; a second motor, tachometer/reference speed sensor, mounting hardware and replacements may bring a stronger dual-rig experiment closer to ₹3,000–₹5,000. Prices require procurement refresh.

### Compute

ESP32-class hardware can support:

- 3-axis acquisition at the selected ADXL345 rate;
- short time features;
- 256–1,024-point FFTs;
- small covariance matrices and Mahalanobis scoring;
- simple confidence/gating state logic.

Complex blind source separation, large neural networks or continuous high-rate multichannel processing are outside the frozen resource profile.

### Team

The five-member team is suitable if responsibilities are separated:

- acquisition/embedded DSP;
- anomaly and experiment software;
- hardware/rig and mounting;
- logging/state machine and beginner tasks;
- validation, documentation and presentation.

The key dependency is not programming skill but disciplined experiment control and access to independently labelled interference conditions.

---

## Kill criteria

Treat the patent direction as killed or downgraded when any of the following occurs:

1. Ordinary RMS/FFT/Mahalanobis performs as well as the proposed method under all controlled interference states.
2. Neighbour changes cannot be distinguished from target abnormality above mounting/session variability.
3. Abstention reduces false alarms only by refusing most useful decisions.
4. The contamination gate either learns faults as normal or cannot track benign drift.
5. Remounting variability destroys the claimed effect and no bounded calibration restores it.
6. The differentiating result exists only on the isolated one-motor rig.
7. A closer patent is found that expressly claims the same calibration, ambiguity, update and remounting sequence.
8. The method requires a sensor array, cloud processing or a fundamentally different sensor architecture, making it a major redesign.
9. Field ground truth cannot be obtained, preventing credible attribution evidence.

Failure of the patent direction does not kill the semester prototype.

---

## Confidentiality boundary

### Already public or conventional

- ADXL345/ESP32 use;
- rigid mounting in general;
- DC removal, Hann windows and FFT;
- RMS, peak, crest factor, kurtosis and standard deviation;
- Mahalanobis anomaly scoring in general;
- generic fixed spectral subtraction;
- eccentric-mass imbalance demonstration;
- RGB normal/abnormal/calibrating display.

### Potentially confidential until IPR review

- exact independently labelled calibration sequence;
- target/interference fingerprint representation;
- ambiguity/confidence computation;
- abstention thresholds and state logic;
- contaminated-window rejection and update gates;
- remounting validity/transfer method;
- feature/band selection derived from the experiments;
- datasets containing target/interferer ground truth;
- comparative field results and ablations;
- any unexpected relationship that becomes the proposed technical contribution.

Do not publish source code, datasets, posters, videos or detailed methods containing these elements before institutional IPR review.

---

## Final VibeGuard recommendation

**Required recommendation:** **Retain as strong semester prototype but reduce patent priority.**

VibeGuard should continue as an engineering prototype because it is affordable, demonstrable and well matched to the team. It should not presently be represented as a patent-bearing invention. Its patent priority should remain below “patent-first” until the team demonstrates a specific confidence-gated, contamination-protected attribution method on independently labelled target/interferer data and survives a refreshed claim search.

The correct project narrative is:

- **Semester claim:** a low-cost local normal-versus-deliberately-imbalanced vibration detector.
- **Research hypothesis:** one sensor may support reliable target attribution with abstention and safe baseline adaptation under interference.
- **Patent status:** unestablished; Track C only.

---

## Unresolved questions

1. What is the official current legal status and enforceable claim scope of US 7,421,349 in every relevant jurisdiction?
2. Do any continuations or non-US members of the Navy family remain live?
3. What exact independent claims are active in the 2026 Augury non-stationary-machine grants?
4. Are there Tractian continuations beyond US 11,429,900 that move processing onto the sensor node?
5. Is there a Senseye-origin family now assigned to Siemens that specifically covers vibration fingerprints, confidence or adaptive baselines?
6. Which Chinese and Indian national families claim single-sensor interference rejection, mounting calibration or abstaining vibration diagnosis?
7. Can the team obtain independently known neighbour states in a real field environment?
8. What machine-state information is available without violating the frozen single-node architecture?
9. Can a repeatable bracket and remounting protocol be built within budget?
10. What owner-approved numerical success and abstention thresholds will be pre-registered?

---

## Source and verification log

### Project sources

- `00_READ_FIRST_VibeGuard_Patent_Research_Instructions.md`
- `01_Engineering_Design_Review(5).md`
- `02_Project_mC_Decision_Register_v1.2(5).md`
- `03_Phase3C_Portfolio_Closure_Memo_Approved(5).md`
- `04_Phase3C_VibeGuard_Architecture_Report_Final.md`
- `05_Phase3C_VibeGuard_Memory_Final.md`
- `06_Phase3C_VibeGuard_SOP_Final.md`
- `07_Concept_Evidence_Matrix(5).md`
- `08_Uncertainty_and_Test_Register(5).md`
- `09_Patent_Research_Input_Pack(5).md`
- `10_Phase2_Report_by_Claude(5).md` — used only as historical leads, not current truth

### Patent records reviewed

- US 7,421,349 — *Bearing fault signature detection*
- US 7,133,801 B2 and US 2007/0032966 A1 — *System and methodology for vibration analysis and condition monitoring*
- US 9,176,003 B2 — *Machine vibration monitoring*
- US 8,290,630 B2 / EP 2,169,497 — condition-monitoring parameter normalization
- US 11,429,900 B1 / BR 102022005021 A2 — Tractian automatic error-condition detection
- US 9,835,594 B2; US 10,983,097 B2; EP 2,909,685; IN2015DN04150A — Augury automatic mechanical diagnosis
- WO 2018/198111 / EP 3,615,899 — Augury machine monitoring
- EP 3,877,819 B1; US 12,607,995 B2 / US 2024/0255942 — Augury non-stationary performance
- WO 2017/151447 / US 2019/0061086 — Infinite Uptime magnetic add-on sensing
- US 9,453,854 B2 / EP 2,913,643 — KCF vibration sensor
- KR 2015-0120160 A — Mahalanobis-Taguchi abnormal vibration determination
- US 11,333,580 B2; US 11,500,965 B2 — Mahalanobis anomaly detection
- US 2021/0231528 A1 — separating periodic and non-periodic vibration peaks
- US 12,140,507 B2 — vibration detection and abnormality determination
- US 12,276,541 B2 / WO 2021/220162 — non-invasive vibration condition monitoring

### Official legal/technical guidance reviewed

- USPTO subject-matter eligibility page and MPEP §2106 framework, current through 2026.
- EPO Guidelines for Examination 2026, computer-implemented inventions and technical effect.
- IP India, Guidelines for Examination of Computer Related Inventions 2025, published 29 April 2026.
- ISO 20816-1:2016 and the 2026 FDIS revision status.

### Verification cautions

- Patent database status labels are not legal opinions.
- Family relationships and live claims should be rechecked in official registers before filing or commercialization.
- This pass did not establish infringement, validity or complete FTO.
- Search completeness is limited by public indexing, translations, assignee changes and the time available for an independent pass.
