# Project mC — VibeGuard Current Patent Evidence Synthesis and Adversarial Audit

## Role

Act as an independent multidisciplinary Patent Evidence Review Board composed of:

- a senior patent-search specialist;
- a patent-family and legal-status analyst;
- an embedded vibration-monitoring engineer;
- a digital-signal-processing specialist;
- an industrial condition-monitoring researcher;
- an experimental-design reviewer;
- a patent-eligibility analyst;
- a freedom-to-operate risk analyst.

This is a neutral synthesis and adversarial evidence-audit task.

You are not one of the original research models. Do not defend, repeat, average, or vote across their conclusions. Audit them.

This report is technical research and project decision support. It is not legal advice, a patentability opinion, a validity opinion, claim construction, an infringement conclusion, or a freedom-to-operate opinion.

Research and legal-status findings must be current as of 1 August 2026.

## Independence requirement

This synthesis is being performed independently in multiple fresh model configurations.

You have not been given another synthesis and must not assume, predict, imitate, request, or use another synthesis model's output.

## Expected input set

You should receive exactly 18 files.

### Governing instruction

1. `00_READ_FIRST_VibeGuard_Synthesis_Instructions.md`

### Current project and historical documents

2. `01_Engineering_Design_Review.md`
3. `02_Project_mC_Decision_Register_v1.2.md`
4. `03_Phase3C_Portfolio_Closure_Memo_Approved.md`
5. `04_Phase3C_VibeGuard_Architecture_Report_Final.md`
6. `05_Phase3C_VibeGuard_Memory_Final.md`
7. `06_Phase3C_VibeGuard_SOP_Final.md`
8. `07_Concept_Evidence_Matrix.md`
9. `08_Uncertainty_and_Test_Register.md`
10. `09_Patent_Research_Input_Pack.md`
11. `10_Phase2_Report_by_Claude.md`

### Independent current patent-research reports

12. `11_VibeGuard_Patent_Research_ChatGPT_DR.<ext>`
13. `12_VibeGuard_Patent_Research_Gemini.<ext>`
14. `13_VibeGuard_Patent_Research_Perplexity.<ext>`
15. `14_VibeGuard_Patent_Research_Qwen.<ext>`
16. `15_VibeGuard_Patent_Research_Mistral.<ext>`
17. `16_VibeGuard_Patent_Research_Microsoft_Copilot.<ext>`

### File-control manifest

18. `99_INPUT_MANIFEST.md`

The six independent research lanes are:

- ChatGPT Deep Research;
- Gemini Deep Research;
- Perplexity Deep Research;
- Qwen Deep Research;
- Mistral;
- Microsoft Copilot.

Confirm actual filenames, formats, readability, completeness, and source models before substantive analysis.

The manifest is a file-control checklist, not technical evidence.

If an independent report is partial, truncated, citation-broken, or concept-swapped, use only the material actually present and reliable. Downgrade or exclude it. Never reconstruct a missing conclusion.

Stop only if the governing instruction or a required project-authority document is missing or unreadable. A partial independent report may be retained and downgraded rather than causing the synthesis to stop.

## Project authority order

Use this precedence for project identity, requirements, and frozen architecture:

1. Engineering Design Review;
2. Project mC Decision Register v1.2;
3. approved Phase 3C portfolio closure memo;
4. final VibeGuard Phase 3C architecture report;
5. final VibeGuard Phase 3C memory;
6. final VibeGuard Phase 3C SOP;
7. current validated down-selection evidence files;
8. Phase 2 report only as historical patent-search leads;
9. independent current patent-research reports as evidence requiring audit.

An independent research report cannot override the frozen project baseline.

Phase 2 patent conclusions are historical leads, not verified current truth.

Do not use Project mC Decision Register v1.1.

## Current owner overrides

### Timeline and budget

- Current implementation window: up to three months.
- Preferred prototype budget: ₹3,000 or less.
- Absolute prototype budget ceiling: ₹5,000.

Where older documents state approximately two months, treat that timeline as historical for this decision.

Do not change the frozen architecture merely because the owner now allows up to three months.

### Team

The team has five members:

- three technically strong CS/Cybersecurity members;
- one beginner/learner;
- one presenter/support member.

### Longer-term continuation

Do not reject VibeGuard solely because the strongest patent-bearing development requires longer than three months.

A technically coherent later-semester or publication-oriented extension may remain viable.

Classify every surviving direction:

- **Track A** — credible prospective invention already embodied in the frozen MVP;
- **Track B** — credible through a bounded enhancement achievable and testable within three months and ₹5,000;
- **Track C** — semester MVP achievable within three months, but the strongest technically connected patent-oriented mechanism requires a later semester or research extension;
- **Track D** — no credible patent-development path established.

Track C is not automatic rejection. It must define a technically coherent bridge from the semester MVP to the later mechanism.

Long-term potential cannot excuse an unbuildable semester MVP.

## Frozen VibeGuard semester MVP

Treat the current baseline as:

- passive, single-node vibration monitoring and alerting;
- one rigidly mounted ADXL345 three-axis accelerometer;
- SPI connection to an ESP32-WROOM-32 or ESP32-S3-class MCU;
- local edge processing without cloud dependence;
- processing order:
  1. DC removal / mean subtraction;
  2. Hann windowing;
  3. continuous time-domain features;
  4. triggered FFT;
- time-domain features may include RMS, peak, standard deviation, crest factor, and kurtosis;
- minimum classifier: calibrated RMS threshold with persistence;
- primary target classifier: unsupervised multivariate Mahalanobis-distance anomaly detection using calibrated normal data;
- baseline noise mitigation: rigid proximity mounting, band-limited features, and baseline spectral subtraction;
- RGB output:
  - green = normal;
  - red = abnormal;
  - blue = calibrating;
- validation rig: small 12 V DC motor or PC fan on a heavy or damped base;
- primary abnormal condition: deliberately attached eccentric mass producing imbalance;
- secondary possible abnormal condition: controlled loosened mounting;
- ADXL345 retained for lower-frequency imbalance, misalignment, and looseness MVP work;
- IIS3DWB only as a documented later upgrade for higher-frequency bearing-fault work.

Do not silently replace this architecture with another sensor, a cloud platform, a multi-node system, a wearable, haptic feedback, audio-event detection, or active vibration cancellation.

A major-redesign path may be identified only if explicitly labelled.

## Mandatory concept-fidelity rules

VibeGuard is:

- passive detection and alerting;
- single-node;
- locally computed at the edge;
- initially focused on normal-versus-deliberately-abnormal machine vibration.

VibeGuard is not:

- active vibration cancellation;
- a haptic or wearable system;
- an audio-event detector;
- a multi-sensor array in the frozen MVP;
- a cloud predictive-maintenance platform;
- a remaining-useful-life forecasting system;
- an industrial-grade high-frequency bearing-fault detector using ADXL345;
- a generic “AI vibration” platform.

A report that substitutes one of those concepts for the frozen system must be downgraded or excluded.

## Critical evidence distinction

Separate two evidence levels.

### Level 1 — Semester bench demonstration

One isolated target motor or fan is classified as normal or deliberately imbalanced.

This can validate the frozen MVP's engineering hypothesis.

### Level 2 — Patent-oriented single-node attribution

One sensor mounted on a target machine detects the target's abnormal state despite vibration from a neighbouring machine or environmental interferer.

This is a materially harder problem.

Do not treat Level 1 success as proof of Level 2 attribution.

A single-node attribution direction must define:

- target and interferer machines;
- independently known target and interferer states;
- target and interferer speed/load variation;
- mounting and remounting conditions;
- source labels or ground truth;
- baseline comparisons;
- false alarms;
- missed detections;
- attribution errors;
- ambiguous or abstained decisions.

## Central questions

Determine:

1. Whether the frozen MVP itself contains a credible prospective patent contribution.
2. Whether the frozen combination is conventional: accelerometer + edge DSP + thresholding + FFT + spectral features + Mahalanobis anomaly detection + local alert.
3. Whether a bounded three-month enhancement can create a credible patent-development path.
4. Whether the strongest path requires later-semester field validation, practical deployment evidence, or publication-oriented work.
5. Whether a proposed direction is actually a major redesign.
6. Whether single-node target-machine attribution under neighbouring-machine interference is already disclosed, claimed, or conventionally solved.
7. Whether spectral subtraction in machinery vibration monitoring is already conventional.
8. Whether Mahalanobis distance combined with common vibration features contributes anything claim-relevant.
9. Whether mounting-aware calibration, target fingerprint acquisition, baseline contamination protection, confidence gating, abstention, resource scheduling, speed/load normalization, or remounting compensation can form a specific technical contribution.
10. What experiments would support or destroy every surviving direction.

Do not declare patentability because an exact duplicate was not found.

## Evidence-review methodology

### Step 1 — Inventory verification

Before synthesis:

- list every attached file;
- classify it as governing instruction, project authority, validated evidence, historical lead, independent research, or manifest;
- confirm exactly 18 files;
- confirm all 10 numbered project/historical files;
- confirm all 6 independent reports;
- identify missing, duplicate, partial, unreadable, concept-swapped, or ambiguously named inputs;
- confirm Decision Register v1.2;
- stop only when the governing instruction or a required project-authority file is missing or unreadable.

### Step 2 — Independent-report audit

Audit each report separately for:

- concept fidelity;
- search breadth;
- primary-source use;
- independent-claim analysis;
- patent-family accuracy;
- legal-status accuracy;
- Indian and Chinese coverage;
- citation traceability;
- reproducible search methodology;
- hallucinated identifiers;
- incorrect family relationships;
- confusion between disclosure and claim scope;
- confusion between expired prior art and FTO;
- unsupported patentability, infringement, or FTO conclusions;
- treatment of US 7,421,349;
- treatment of US 7,346,461;
- treatment of named commercial actors;
- treatment of spectral subtraction;
- treatment of Mahalanobis distance;
- treatment of bench classification versus source attribution;
- three-month feasibility;
- compute, memory, sample-rate, and sensor-bandwidth realism.

Assign each report:

- High reliability;
- Medium reliability;
- Low reliability;
- Excluded in whole or in part.

Do not use model reputation as evidence quality.

### Step 3 — Primary verification of load-bearing findings

Independently verify important findings.

Prefer:

- Indian Patent Office;
- WIPO PATENTSCOPE;
- USPTO Patent Center and Patent Public Search;
- EPO Espacenet and European Patent Register;
- official Chinese, Japanese, and Korean records where relevant;
- primary peer-reviewed technical literature;
- official standards or standards-body material where accessible.

Google Patents may be used for discovery, readable claim text, and family navigation, but not as the sole basis for a load-bearing legal-status conclusion.

For important patent records distinguish:

- published disclosure;
- pending application;
- granted patent;
- abandoned application;
- expired/lapsed patent;
- live claim status where verifiable;
- prior-art relevance;
- FTO relevance.

If an official record cannot be accessed, mark the conclusion unresolved.

### Step 4 — Conflict resolution

Resolve disagreements using:

1. verified independent claims;
2. official family and legal-status records;
3. technical similarity to the frozen VibeGuard architecture;
4. corroborated peer-reviewed or dated non-patent prior art;
5. credible experimental evidence;
6. report reasoning quality.

Do not resolve disagreements by counting models.

A well-supported minority report may override several weak reports.

## Mandatory named-lead review

Audit and resolve, where materially relevant:

- US 7,421,349, the historical US Navy bearing-fault-signature lead;
- US 7,346,461, the NASA vibration/failure-signature lead;
- Tractian US 11,429,900 and its actual family;
- US 9,271,170 B1 and relevant KCF family members;
- US 10,873,791 B1 and relevant KCF family members;
- US 2022/0067020 A1 and any related Mahalanobis/anomaly family;
- actual relevant patent families associated with:
  - Tractian;
  - Infinite Uptime;
  - Augury;
  - KCF Technologies;
  - Senseye;
- relevant major industrial condition-monitoring, bearing, automation, and sensor-company families;
- Indian and Chinese records surfaced by the six reports;
- peer-reviewed single-sensor, edge-anomaly, source-separation, remounting-transfer, and baseline-adaptation literature.

Do not assume identifiers or family relationships supplied by any report are correct.

For every named company:

- identify actual patent families rather than relying on the company name;
- separate patent claim scope from product functionality;
- distinguish cloud, edge, single-sensor, multi-sensor, fingerprinting, source attribution, anomaly detection, mounting calibration, baseline adaptation, and maintenance prediction.

## Frozen-MVP feature comparison

Compare the closest prior art against:

- one rigidly mounted ADXL345;
- SPI acquisition;
- ESP32 local processing;
- DC removal;
- Hann window;
- RMS;
- peak;
- standard deviation;
- crest factor;
- kurtosis;
- threshold plus persistence;
- triggered FFT;
- spectral subtraction;
- band-limited features;
- Mahalanobis anomaly score;
- single-node operation;
- normal-baseline acquisition;
- neighbouring-machine interference handling;
- confidence or abstention;
- adaptive baseline update;
- mounting/remounting calibration;
- target-machine attribution;
- RGB alert;
- low-cost eccentric-mass motor/fan test rig;
- local/no-cloud operation;
- sample-rate and bandwidth limitations;
- RAM, flash, compute-time, and latency limitations.

Use only:

- expressly disclosed;
- necessarily implied;
- arguably suggested;
- absent;
- unresolved.

Do not equate an absent feature in one reference with inventive step.

## Candidate invention directions

Evaluate at least:

1. single-node target-machine attribution under neighbouring-machine interference;
2. in-situ target fingerprint acquisition using known machine operating states;
3. guarded spectral subtraction or band-selection update protected against contamination by target faults or neighbour-state changes;
4. confidence-gated or abstaining anomaly decisions that refuse to label ambiguous interference as a target fault;
5. mounting-transfer or remounting compensation preserving diagnostic meaning after sensor reinstallation;
6. resource-aware two-stage processing in which cheap features trigger selected FFT/band analysis while preserving measurable attribution performance;
7. speed/load-normalized target fingerprints or order-related features using only the permitted single node and available machine-state information;
8. drift-aware baseline adaptation with safeguards preventing abnormal data from being learned as normal;
9. a deployment/calibration protocol creating independently testable source labels or target fingerprints without a multi-sensor product architecture;
10. any additional direction supported by audited evidence.

For each direction state:

- exact physical/technical problem;
- prospective technical contribution;
- closest verified patent and non-patent art;
- overlapping and apparently differentiating elements;
- whether it is ordinary DSP, statistics, calibration, deployment practice, hardware structure, or an integrated technical mechanism;
- measurable physical or diagnostic technical effect;
- baseline comparator;
- required experiment;
- hardware/software changes;
- sample-rate and bandwidth impact;
- RAM/flash/compute impact;
- latency and energy impact where material;
- likely cost;
- three-month feasibility;
- later work;
- novelty risk;
- inventive-step/obviousness risk;
- eligibility risk;
- FTO risk;
- Track A, B, C, or D;
- confidence;
- kill condition.

Reject weak directions clearly.

Do not retain a direction merely to ensure VibeGuard has a patent story.

## Separate patent-risk analyses

### Novelty

Could one verified item disclose every required element?

### Inventive step / obviousness

Would the differences be a routine combination of accelerometer monitoring, baseline calibration, FFT, spectral features, spectral subtraction, thresholding, Mahalanobis or one-class anomaly detection, adaptive updating, mounting compensation, triggered analysis, confidence gating, or source discrimination?

### Patent eligibility

Could a software/DSP direction face abstract-algorithm, mathematical-method, or computer-program-per-se issues?

Identify the physical technical effect and machine-measurement relationship needed for the United States, Europe, and India.

### Freedom to operate

Could building, using, or commercializing the frozen MVP or a proposed enhancement fall within active claims?

Do not merge these analyses.

Do not state infringement without a live-claim comparison.

## Experimental-evidence requirements

The project authority documents do not freeze a numerical accuracy threshold.

Do not invent one as a current project fact.

You may recommend pre-registration thresholds, but label them as research recommendations requiring owner approval before testing.

At minimum compare:

- RMS/persistence baseline;
- ordinary FFT-feature baseline;
- Mahalanobis baseline;
- baseline spectral subtraction;
- each proposed direction;
- ablations removing each allegedly inventive element.

Test conditions should distinguish:

- target normal / target abnormal;
- interferer off / normal / abnormal;
- target speed/load changes;
- interferer speed/load changes;
- sensor remounting;
- repeated sessions and days;
- controlled mounting changes where safe;
- controlled dual-motor rig;
- real dense-machine field data as a separate higher evidence level.

Metrics should include, where relevant:

- sensitivity;
- specificity;
- balanced accuracy;
- false alarms per hour;
- missed detections;
- target-attribution error;
- confidence calibration;
- abstention or unknown rate;
- detection delay;
- remounting repeatability;
- compute time;
- RAM and flash use;
- sample rate and usable bandwidth;
- energy or power where material.

Any patent-oriented attribution direction must use independent ground truth for both target and interferer states.

An isolated eccentric-mass bench test cannot establish source attribution.

## Claim-to-experiment mapping

For every surviving direction provide:

- prospective technical element;
- nearest verified prior art;
- measurable technical effect;
- baseline system;
- proposed system;
- independent variable;
- controlled variables;
- required equipment;
- sample/session count;
- proposed pre-registration threshold;
- success evidence;
- failure evidence;
- bench-rig relevance;
- field-data requirement;
- three-month deliverability;
- later work;
- confidentiality sensitivity.

## Three-month and longer-term development plan

Separate:

### Semester MVP

Define the isolated motor/fan normal-versus-imbalance demonstration achievable within three months and ₹5,000.

### Bounded enhancement

Define any patent-oriented improvement that can be integrated and tested without replacing the frozen architecture.

### Later extension

For Track C directions state:

- additional mechanism or method;
- additional duration;
- additional cost;
- field-access requirement;
- source-label/ground-truth requirement;
- higher-bandwidth sensor requirement, if any;
- validation burden;
- publication opportunity;
- why it remains VibeGuard rather than an unrelated predictive-maintenance project.

## Confidentiality

Mark newly identified prospective inventions as confidential project material.

Separate:

- already public or conventional MVP features;
- potentially confidential calibration sequences;
- potentially confidential target-fingerprint methods;
- potentially confidential baseline-update and contamination-protection rules;
- potentially confidential confidence/abstention logic;
- potentially confidential mounting-transfer methods;
- potentially confidential datasets and field results.

Do not recommend public disclosure before institutional IPR review.

## Required output

Produce one self-contained Markdown report:

# VibeGuard Current Patent Evidence Synthesis

## 1. Executive verdict

State exactly one:

- credible patent path in current MVP;
- credible path through bounded three-month enhancement;
- credible long-term path requiring later-semester extension;
- credible path only through major redesign;
- no credible patent path established.

Also state:

- Track A, B, C, or D;
- confidence;
- most important limitation;
- whether the frozen MVP should be treated as the invention.

## 2. Input inventory

## 3. Research-report reliability audit

## 4. Search coverage and evidence gaps

## 5. Verified patent-family ledger

For each family include:

- identifiers;
- priority date;
- applicant/assignee;
- jurisdictions;
- official status where available;
- independent-claim subject;
- relevance;
- novelty significance;
- FTO significance;
- confidence;
- primary source.

## 6. Closest independent-claim analyses

## 7. Frozen-MVP closest-art feature chart

## 8. Mandatory named-lead investigation

Include US 7,421,349, US 7,346,461, and actual relevant families associated with the named commercial actors.

## 9. Non-patent prior art and standards

## 10. Current frozen-MVP patent assessment

## 11. Candidate invention-direction matrix

## 12. Strongest surviving direction

Define it precisely enough to distinguish it from generic FFT, thresholding, Mahalanobis scoring, spectral subtraction, routine calibration, or ordinary deployment practice. Do not draft final legal claims.

## 13. Bench demonstration versus field-attribution evidence

## 14. Novelty analysis

## 15. Inventive-step / obviousness analysis

## 16. Patent-eligibility analysis

## 17. FTO risk analysis

## 18. Claim-to-experiment map

## 19. Three-month semester plan

## 20. Later-semester or publication extension

## 21. Budget, compute, and team feasibility

## 22. Kill criteria

## 23. Confidentiality boundary

## 24. Final VibeGuard recommendation

Use exactly one:

- Advance as patent-first candidate;
- Advance conditionally pending named evidence;
- Retain as strong semester prototype but reduce patent priority;
- Deprioritize under the patent-first selection criterion.

Do not compare against OpenBraille or TrueMoist.

Do not select the final Project mC winner.

Do not fill the final cross-concept scoring worksheet.

## 25. Unresolved questions

## 26. Source and verification log

## Final quality rules

- Do not vote across reports.
- Do not use another synthesis output.
- Do not invent patent families, legal status, search results, standards, or experimental evidence.
- Do not treat abstracts as claims.
- Do not treat expired patents as irrelevant prior art.
- Do not treat expired or abandoned records as automatically blocking FTO.
- Do not equate edge processing, low cost, no cloud, ESP32, FFT, spectral subtraction, Mahalanobis distance, anomaly detection, or a single sensor with novelty.
- Do not treat the eccentric-mass bench rig as proof of dense-machine source attribution.
- Do not describe the ADXL345 MVP as validating high-frequency industrial bearing-fault diagnosis.
- Clearly separate verified fact, report assertion, inference, recommendation, and unresolved uncertainty.
- Cite every load-bearing patent, legal-status, and technical-literature conclusion.
- State when evidence is insufficient.
