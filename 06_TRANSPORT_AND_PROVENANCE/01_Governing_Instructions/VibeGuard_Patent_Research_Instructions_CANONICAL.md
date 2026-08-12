# Project mC — VibeGuard Current Patent Verification — Independent Deep Research

## Role

Act as an independent multidisciplinary patent-research team consisting of a patent-search specialist, patent-family/legal-status analyst, embedded vibration-monitoring engineer, DSP specialist, industrial condition-monitoring researcher, experimental-design reviewer, and patent-eligibility/FTO risk analyst.

This is an independent current patent-research pass, not a synthesis of other models and not a comparison among Project mC concepts. Findings must be current as of 31 July 2026.

This report is technical research and project decision support, not legal advice, a patentability guarantee, validity opinion, claim construction, infringement conclusion, or freedom-to-operate opinion.

## Input set

You have been given ten canonical project documents:

1. `Engineering_Design_Review.md`
2. `Project_mC_Decision_Register_v1.2.md`
3. `Phase3C_Portfolio_Closure_Memo_Approved.md`
4. `Phase3C_VibeGuard_Architecture_Report_Final.md`
5. `Phase3C_VibeGuard_Memory_Final.md`
6. `Phase3C_VibeGuard_SOP_Final.md`
7. `03_Concept_Evidence_Matrix.md`
8. `05_Uncertainty_and_Test_Register.md`
9. `06_Patent_Research_Input_Pack.md`
10. `Phase2_Report by CLaude.md`

Before substantive research, inventory the attached files and confirm that all ten are present and readable. Do not substitute Decision Register v1.1.

## Project authority order

For project identity, architecture and constraints, use this precedence:

1. Engineering Design Review;
2. Project mC Decision Register v1.2;
3. approved Phase 3C portfolio closure memo;
4. final VibeGuard Phase 3C architecture report;
5. final VibeGuard Phase 3C memory;
6. final VibeGuard Phase 3C SOP;
7. current validated down-selection evidence files;
8. Phase 2 report only as historical patent-search leads.

Phase 2 patent conclusions are not verified current truth. Do not allow historical material or external sources to silently replace the frozen project baseline.

## Current owner overrides

- Current semester implementation window: up to three months.
- Preferred prototype budget: ₹3,000 or less.
- Absolute budget ceiling: ₹5,000.
- Five-member team: three technically strong CS/Cybersecurity members, one beginner/learner, and one presenter/support member.
- A technically coherent later-semester or publication-oriented extension may remain viable even when the strongest patent-bearing development cannot be completed within the current semester.
- Do not reject VibeGuard solely because the strongest patent-development mechanism requires longer than three months.
- Do not allow a speculative long-term patent direction to excuse an unbuildable semester MVP.
- Treat newly identified prospective inventions, implementation details and experiment results as confidential until institutional IPR review.

## Frozen VibeGuard semester MVP

Treat the current baseline as:

- a passive, single-node vibration-monitoring and alerting system;
- one rigidly mounted ADXL345 three-axis accelerometer;
- SPI connection to an ESP32-WROOM-32 or ESP32-S3-class MCU;
- local edge processing without cloud dependence;
- processing order: DC removal/mean subtraction → Hann windowing → continuous time-domain features → triggered FFT;
- time features may include RMS, peak, standard deviation, crest factor and kurtosis;
- minimum classifier: calibrated RMS threshold with persistence;
- primary target classifier: unsupervised multivariate Mahalanobis-distance anomaly detection using calibrated normal data;
- baseline noise mitigation: rigid proximity mounting, band-limited features and baseline spectral subtraction;
- RGB output: green normal, red abnormal, blue calibrating;
- validation rig: small 12 V DC motor or PC fan on a heavy/damped base;
- primary abnormal condition: deliberately attached eccentric mass producing imbalance;
- secondary possible abnormal condition: controlled loosened mounting;
- ADXL345 retained for low-frequency imbalance/misalignment MVP work;
- IIS3DWB only as a documented later upgrade for higher-frequency bearing-fault work.

## Mandatory concept-fidelity rules

VibeGuard is passive detection and alerting, single-node, local/edge computed, and focused first on normal-versus-deliberately-abnormal machine vibration.

VibeGuard is not active vibration cancellation, a haptic/wearable vibration system, a multi-sensor array in the frozen MVP, an audio-event detector, a cloud predictive-maintenance platform, a full remaining-useful-life forecasting system, an industrial-grade bearing-fault detector using ADXL345, or a generic “AI vibration” platform.

Do not concept-swap into those areas. A multi-sensor, cloud, high-bandwidth or different-sensor architecture may be discussed only as an explicitly labelled later redesign or comparison, not as the current MVP.

## Critical evidence distinction

Separate two evidence levels:

### Level 1 — Semester bench demonstration

One isolated target motor/fan is classified as normal or deliberately imbalanced. This can validate the frozen MVP's engineering hypothesis.

### Level 2 — Patent-oriented single-node attribution

One sensor mounted on a target machine detects the target's abnormal state despite vibration from a neighbouring machine or environmental interferer.

This is materially harder and is not proven by the isolated bench demo. Any claimed single-node attribution direction must define target/interferer machines, independently known states, speed/load variation, mounting/remounting conditions, source labels or ground truth, baseline comparisons, false alarms, misses and attribution errors.

## Central research questions

Determine:

1. Whether the frozen MVP itself contains any credible prospective patent contribution.
2. Whether its features are merely a conventional combination of an accelerometer, edge DSP, thresholding, FFT and anomaly detection.
3. Whether a bounded three-month enhancement can create a credible patent-development path.
4. Whether the strongest path requires a later-semester field-validation or publication programme.
5. Whether any proposed direction would actually be a major redesign.
6. Whether single-node target-machine attribution under neighbouring-machine interference is already disclosed, claimed or conventionally solved.
7. Whether spectral subtraction in machine vibration monitoring is conventional.
8. Whether Mahalanobis distance plus common vibration features contributes anything claim-relevant.
9. Whether mounting-aware calibration, baseline acquisition, adaptive updating, confidence gating, resource scheduling or abstention can form a specific technical contribution.
10. What experiments would support or destroy each surviving direction.

Do not declare patentability because an exact duplicate was not found.

## Research methodology

### Reproducible search log

Record database/source, date searched, exact query, CPC/IPC classes explored, assignee/inventor searches, citation-chain searches, selected result, and reason selected or rejected.

Search patent classifications related to mechanical vibration measurement, machine/bearing condition monitoring, diagnostic machine monitoring, signal processing/anomaly detection, and embedded/on-device diagnosis. Identify and expand the correct CPC/IPC classes during the search rather than relying only on keywords.

### Primary patent sources

Prefer Indian Patent Office, WIPO PATENTSCOPE, USPTO Patent Center/Patent Public Search, EPO Espacenet/European Patent Register, and official Chinese/Japanese/Korean records where relevant.

Google Patents may be used for discovery, readable claim text and family navigation, but not as the sole source for a load-bearing legal-status conclusion.

For each important record distinguish publication/disclosure, pending application, granted patent, abandoned application, expired/lapsed patent, live independent claim where verifiable, prior-art relevance and FTO relevance.

### Technical primary literature

Search peer-reviewed journal/conference papers, official standards/technical guidance where accessible, university/research-institute publications, and official company patent/product technical documents where needed. Separate peer-reviewed evidence from marketing statements, blogs and secondary summaries.

### Claim-level review

Analyze independent claims, not only titles or abstracts. For the closest families identify relevant independent claims, map claim elements to the frozen MVP and proposed enhancement, distinguish specification disclosure from claim requirements, identify continuations/divisionals and material non-US family members, and flag unresolved status or scope.

### Separate legal analyses

Analyze novelty, inventive step/obviousness, patent eligibility and FTO separately.

For obviousness, assess whether the proposed difference is merely a routine combination of accelerometer monitoring, baseline calibration, FFT/spectral features, spectral subtraction, threshold/persistence, Mahalanobis or one-class anomaly detection, adaptive baseline updating, mounting compensation, compute-triggered analysis, confidence gating or source attribution.

For eligibility, identify the required physical technical effect and machine-measurement relationship for the United States, Europe and India.

Do not state infringement without a live-claim comparison.

## Mandatory historical and commercial leads

Investigate rather than assume:

- US 7,421,349, historically described in the repository as a US Navy phase-coupling lead;
- Tractian and any identifiable reported vibration/fault-detection patent families;
- Infinite Uptime;
- Augury;
- KCF Technologies;
- Senseye;
- relevant families from major industrial condition-monitoring, bearing, automation and sensor companies;
- Indian and Chinese records missed by previous passes.

For each named company, identify actual patent families rather than relying on company name alone. Separate patented claim scope from product functionality and classify whether the relevant feature concerns cloud, edge, single-sensor, multi-sensor, fingerprinting, source attribution, anomaly detection, mounting calibration, baseline adaptation or maintenance prediction.

Do not assume a commercial platform's existence proves every feature is patented.

## Mandatory search terms and variants

Use and expand:

`single sensor machine vibration attribution`
`single node vibration source isolation`
`machine fault neighboring machine noise`
`vibration spectral subtraction condition monitoring`
`in situ vibration baseline calibration`
`edge vibration anomaly Mahalanobis`
`band limited vibration fault features`
`spatial attribution accelerometer machine`
`phase coupling unrelated spectral peaks fault`
`low cost predictive maintenance edge node`
`target machine vibration discrimination`
`dense factory vibration cross talk`
`mechanical cross-talk condition monitoring`
`unsupervised vibration anomaly embedded`
`mounting transfer vibration sensor calibration`
`remounting invariant machine vibration monitoring`
`adaptive baseline contamination vibration anomaly`
`confidence gated machine anomaly detection`
`abstention unknown state vibration monitoring`
`resource constrained triggered FFT condition monitoring`
`machine startup shutdown fingerprint calibration`

Expand across predictive maintenance/condition monitoring/machine health/fault detection; vibration/acceleration/acoustic emission; source isolation/source separation/attribution/discrimination/crosstalk rejection; edge/local/on-device/embedded/single-node; baseline/subtraction/fingerprint/envelope/sideband/phase coupling; anomaly/novelty/one-class/Mahalanobis/confidence/abstention; mounting/remounting/transfer function/installation calibration; adaptive update/drift/contamination protection/operating-state normalization.

## Frozen-MVP feature chart

Compare closest prior art against:

- one rigidly mounted ADXL345;
- SPI acquisition;
- ESP32 local processing;
- DC removal;
- Hann window;
- RMS/peak/standard deviation/crest factor/kurtosis;
- threshold and persistence;
- triggered FFT;
- spectral subtraction;
- band-limited features;
- Mahalanobis anomaly score;
- single-node operation;
- normal-baseline acquisition;
- neighbouring-machine interference handling;
- confidence/abstention;
- adaptive baseline update;
- mounting/remounting calibration;
- target-machine attribution;
- RGB alert;
- low-cost isolated eccentric-mass test rig;
- local/no-cloud operation;
- compute, memory and latency constraints.

Use only expressly disclosed, necessarily implied, arguably suggested, absent or unresolved. Do not equate an absent single-reference feature with inventive step.

## Candidate invention directions

Evaluate at least:

1. Single-node target-machine attribution under neighbouring-machine interference.
2. In-situ target fingerprint/baseline acquisition using known machine operating states.
3. A specific spectral-subtraction and band-selection update rule protected against contamination by target faults or neighbour-state changes.
4. Confidence-gated or abstaining anomaly decisions that refuse to label ambiguous interference as a target fault.
5. Mounting-transfer or remounting compensation preserving diagnostic meaning after sensor reinstallation.
6. Resource-aware two-stage processing where cheap features trigger selected FFT/band analysis while preserving measurable attribution performance.
7. Speed/load-normalized target fingerprints or order-related features using only the permitted single node and available machine-state information.
8. Drift-aware baseline adaptation with safeguards preventing abnormal data from being learned as normal.
9. A deployment/calibration protocol creating independently testable source labels/fingerprints without a multi-sensor product architecture.
10. Any additional direction supported by verified evidence.

For each state the exact problem, proposed contribution, closest patent/NPL, overlapping elements, differentiating elements, whether it is ordinary DSP/statistics/calibration/deployment practice, required physical technical effect, baseline comparator, experiments, hardware/software changes, compute/memory/latency impact, cost, three-month feasibility, later work, novelty risk, obviousness risk, eligibility risk, FTO risk, confidence, kill condition and Track A/B/C/D.

Reject weak directions clearly. Do not retain a direction merely to give VibeGuard a patent story.

## Track classifications

- Track A: credible prospective invention already embodied in frozen MVP.
- Track B: credible path through a bounded enhancement achievable/testable within three months and ₹5,000.
- Track C: semester MVP achievable within three months, but strongest connected patent-development mechanism needs a later semester/publication programme.
- Track D: no credible patent-development path established.

## Experimental evidence

The authority documents do not freeze a numerical classification-accuracy threshold. Do not invent one as a current project fact. Numerical thresholds may be recommended only as clearly labelled pre-registration proposals requiring owner approval.

At minimum compare:

- RMS/persistence baseline;
- ordinary FFT-feature baseline;
- Mahalanobis baseline;
- baseline spectral subtraction;
- each proposed direction;
- ablations removing each allegedly inventive element.

Test target normal/abnormal; interferer off/normal/abnormal; target and interferer speed/load changes; sensor remounting; repeated sessions/days; controlled dual-motor rig; and real dense-machine field data as a separate higher evidence level.

Metrics should include sensitivity, specificity, balanced accuracy, false alarms per hour, missed detections, target-attribution error, confidence calibration, abstention/unknown rate, detection delay, remounting repeatability, compute time, RAM/flash use, sample rate/bandwidth and power where material.

For patent-oriented single-node attribution require independent ground truth for target and interferer states. An isolated eccentric-mass bench test alone cannot establish source attribution.

## Claim-to-experiment mapping

For every surviving direction provide prospective technical element, nearest verified prior art, measurable technical effect, baseline system, proposed system, independent variable, controlled variables, equipment, sample/session count, proposed pre-registration threshold, success evidence, failure evidence, bench relevance, field-data requirement, three-month deliverability, later work and confidentiality sensitivity.

## Three-month and later-development analysis

Separate:

### Semester MVP

Define the isolated motor/fan normal-versus-imbalance demonstration achievable within three months and ₹5,000.

### Bounded enhancement

Define any patent-oriented improvement that can be integrated and tested without replacing the frozen architecture.

### Later extension

For Track C directions state extra mechanism/method, duration, cost, field access, ground-truth requirement, higher-bandwidth sensor requirement if any, validation burden, publication opportunity and why it remains VibeGuard.

## Confidentiality

Separate already public/conventional MVP features from potentially confidential calibration sequences, baseline-update/contamination-protection rules, confidence/abstention logic, mounting-transfer methods, datasets and field results. Do not recommend public disclosure before institutional IPR review.

## Required output

Produce one self-contained Markdown report titled:

# VibeGuard Current Patent Verification — Independent Research

Use these sections:

1. Executive verdict
2. Input inventory and concept-fidelity confirmation
3. Search methodology and reproducible search log
4. Technical and patent landscape map
5. Verified patent-family ledger
6. Closest independent-claim analyses
7. Frozen-MVP feature comparison
8. Mandatory named-lead investigation
9. Non-patent prior art and standards
10. Current frozen-MVP patent assessment
11. Candidate invention-direction matrix
12. Strongest surviving direction
13. Bench demonstration versus field-attribution evidence
14. Novelty analysis
15. Inventive-step / obviousness analysis
16. Patent-eligibility analysis
17. FTO risk analysis
18. Claim-to-experiment map
19. Three-month semester plan
20. Later-semester or publication extension
21. Budget, compute and team feasibility
22. Kill criteria
23. Confidentiality boundary
24. Final VibeGuard recommendation
25. Unresolved questions
26. Source and verification log

In the executive verdict choose exactly one:

- credible patent path in current MVP;
- credible path through bounded three-month enhancement;
- credible long-term path requiring later-semester extension;
- credible path only through major redesign;
- no credible patent path established.

Also state Track A/B/C/D, confidence, most important limitation and whether the frozen MVP itself should be treated as the invention.

For final recommendation choose exactly one:

- Advance as patent-first candidate;
- Advance conditionally pending named evidence;
- Retain as strong semester prototype but reduce patent priority;
- Deprioritize under the patent-first selection criterion.

Do not compare against OpenBraille or TrueMoist. Do not select the final Project mC winner.

## Final quality rules

- Do not use another model's current VibeGuard research.
- Do not synthesize or vote across models.
- Do not rely on prior-chat context.
- Do not invent patent identifiers, family relationships or legal status.
- Do not treat abstracts as claims.
- Do not treat expired patents as irrelevant prior art.
- Do not treat expired/abandoned records as automatically blocking FTO.
- Do not equate edge processing, low cost, no cloud, ESP32, FFT, spectral subtraction, Mahalanobis distance or a single sensor with novelty.
- Do not treat the eccentric-mass bench rig as proof of dense-machine source attribution.
- Do not describe the ADXL345 MVP as validating high-frequency bearing-fault diagnosis.
- Separate verified fact, report assertion, inference, recommendation and unresolved uncertainty.
- Cite every load-bearing patent, legal-status and technical-literature conclusion.
- State when evidence is insufficient.
