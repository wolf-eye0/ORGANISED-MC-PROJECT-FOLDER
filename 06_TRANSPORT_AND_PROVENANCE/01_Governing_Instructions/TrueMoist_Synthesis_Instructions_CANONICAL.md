# Project mC — TrueMoist Patent-Evidence Synthesis Instructions

## 1. Role and scope

Act as an independent patent-evidence review board covering:

- patent searching and claim analysis;
- patent-family and legal-status verification;
- soil-moisture sensing and dielectric measurement;
- embedded analog acquisition and calibration;
- experimental design and metrology;
- novelty, inventive step, patent eligibility, and FTO risk;
- semester-project feasibility and later invention development.

This is a blind synthesis. Do not use prior-chat context, another synthesis,
OpenBraille or VibeGuard reports, or any cross-concept ranking.

Evidence cut-off: **1 August 2026**.

This is technical research and project decision support, not legal advice,
patentability/FTO clearance, claim construction, or an infringement opinion.

## 2. Expected logical input set

Confirm exactly **18 physical attachments**:

1. one governing synthesis instruction;
2. ten canonical project/historical documents;
3. six independent TrueMoist patent-research lanes;
4. one file-control manifest.

Expected controlled names:

00_READ_FIRST_TrueMoist_Synthesis_Instructions.md
01_Engineering_Design_Review.md
02_Project_mC_Decision_Register_v1.2.md
03_Phase3C_Portfolio_Closure_Memo_Approved.md
04_Phase3C_TrueMoist_Architecture_Report_Final.md
05_Phase3C_TrueMoist_Memory_Final.md
06_Phase3C_TrueMoist_SOP_Final.md
07_Concept_Evidence_Matrix.md
08_Uncertainty_and_Test_Register.md
09_Patent_Research_Input_Pack.md
10_Phase2_Report_by_Claude.md
11_TrueMoist_Patent_Research_ChatGPT_DR.md
12_TrueMoist_Patent_Research_Gemini.*
13_TrueMoist_Patent_Research_Perplexity.*
14_TrueMoist_Patent_Research_Qwen_COMPILATION.md
15_TrueMoist_Patent_Research_Mistral*
16_TrueMoist_Patent_Research_Microsoft_Copilot.*
99_INPUT_MANIFEST.md

Use the manifest only for file control. It is not technical evidence.

Stop only if the governing instruction or a required project-authority file is
missing or unreadable. A partial research lane may be downgraded without
halting if the manifest and lane file make the limitation explicit.

## 3. Project authority order

Apply this order strictly:

1. Engineering Design Review.
2. Project mC Decision Register v1.2.
3. Approved Phase 3C Portfolio Closure Memo.
4. Final TrueMoist Architecture Report.
5. Final TrueMoist Memory.
6. Final TrueMoist SOP.
7. Validated current evidence files 07–09.
8. Phase 2 only as historical search leads.
9. Independent research lanes only after source, claim, status, and concept
   fidelity audit.

Decision Register v1.1 and the later 135-run `TrueMoist/by claude/` files are
superseded and must not be used.

Owner constraints override older project text:

- up to three months;
- preferred spend no more than ₹3,000;
- absolute ceiling ₹5,000;
- team of five: three technically strong contributors, one learner, and one
  presenter/support member.

## 4. Frozen TrueMoist architecture

TrueMoist is a **local compensation system for a low-cost analog capacitive
soil-moisture probe**.

### Sensing

- genuine analog capacitive probe, SEN0193-class or characterized equivalent;
- two probe units available for characterization and variation testing;
- waterproof DS18B20 at the same depth, approximately 20–30 mm from the
  moisture probe;
- controlled salinity treatment represented as known salt addition per
  dry-soil mass;
- the salinity-treatment code is experimental metadata, not measured bulk
  soil EC, apparent EC, pore-water EC, or solution conductivity;
- no mandatory live runtime EC sensor.

### Acquisition

- ESP32-WROOM-32 primary; ESP32-S3 fallback;
- ADS1115 primary subject to a mandatory Week-1 paired comparison against
  calibrated ESP32 ADC1;
- retain ADS1115 only if noise, repeatability, pilot RMSE, or reproducibility
  justify it;
- approximately 1 kΩ series resistance, 100 nF input filtering, local 100 nF
  plus 10 µF decoupling, short analog wiring, fixed connectors, deliberate
  grounding, and soldered perfboard after Week-1 characterization;
- USB 5 V and USB serial CSV;
- no cloud/app dependency.

### Modelling

- M0: uncompensated/univariate raw mapping;
- M1: multivariate linear regression;
- M2: ridge-regularized second-order regression;
- inputs: raw probe response, measured soil temperature, controlled
  salinity-treatment code;
- train offline in Python;
- deploy fixed coefficients locally on ESP32;
- no TinyML requirement;
- no online-adaptive training in the frozen MVP.

### Dataset and ground truth

- one homogeneous soil source;
- one documented preparation and packing method;
- 4 moisture × 3 temperature × 2 salinity × 3 independent replicates;
- exactly 72 independent physical runs;
- replicates 1–2 for training/model selection;
- replicate 3 untouched for physical test;
- repeated ADC readings may be averaged but never counted as independent
  physical samples;
- dry-basis gravimetric water content as ground truth;
- drying near 105 ± 5 °C for at least 24 hours and until constant mass;
- 0.01 g scale preferred;
- do not claim volumetric water content unless bulk density is independently
  measured.

### Engineering success on untouched test data

- compensated RMSE at least 20% lower than uncompensated;
- compensated MAE at least 15% lower;
- report absolute errors and disturbance-subset performance.

Passing these thresholds does not prove patentability.

## 5. Concept-fidelity rules

Do not convert TrueMoist into:

- a live-EC meter;
- irrigation controller;
- cloud agriculture platform;
- universal calibration-free probe;
- laboratory reference instrument;
- multi-soil product;
- custom multi-frequency probe;
- TinyML showcase;
- online-adaptive learner;
- generic smart-agriculture platform.

Live EC, multi-frequency sensing, custom probes, multiple soils, cloud
processing, irrigation control, or online learning may appear only as clearly
labelled later extensions or major redesigns.

## 6. Research lanes are evidence, not votes

Do not count model agreement. Audit every lane independently.

### ChatGPT Deep Research

The official lane is the finalized Markdown report only. The earlier
`research on f.patent by chatgpt high deeprserach.pdf` is superseded and must
not appear in this package.

### Qwen warning

File 14 is a lossless compilation of two outputs from **one Qwen research
lane**:

1. initial substantive research;
2. follow-up/final structured response.

It is one evidence source, not two reports or two votes. The second part does
not automatically repair unsupported claims in the first.

Independently verify or downgrade, especially:

- `HIGH / CLEAR` FTO;
- asserted novelty of Mahalanobis validity-envelope abstention;
- Track-B / bounded-three-month confidence;
- eligibility-clearance claims;
- dual-probe health assumptions;
- event-triggered recalibration white-space claims;
- statements that absence of live EC creates patentability.

### Mistral warning

If File 15 is a compilation or partial lane, treat all fragments as one lane.
Do not reconstruct a missing conclusion. Downgrade unsupported patentability,
novelty, status, infringement, FTO, or quantitative claims.

### Supplementary Work Max audit

The separate ChatGPT Work Max web-research audit is deliberately excluded from
the blind synthesis package. Do not infer or use it from prior-chat context.
It may be considered only later during external adjudication of the three
blind syntheses.

## 7. Required audit method

For every research lane:

- confirm concept fidelity;
- identify primary sources versus secondary/aggregator sources;
- verify identifiers, family relationships, priority, applicant, jurisdiction,
  and legal status;
- distinguish independent claims from descriptions and dependent claims;
- distinguish prior-art relevance from FTO relevance;
- identify unsupported quantitative thresholds or experimental claims;
- classify the lane as high, medium, low, partial, or excluded reliability;
- explain every material correction that affects the verdict.

Do not use another lane's repetition as verification.

## 8. Patent and technical verification priorities

Independently investigate, claim-read, and status-check the closest verified
families and any closer art found during synthesis. At minimum address:

- TCS low-cost sensor-health family:
  US12175680B2, WO2021144807A1, EP4090953B1, and the Indian-priority filing;
- CN102914568B replaceable-probe calibration/equivalence;
- US20080199359A1 / WO2007002994 / EP1899716 self-learning soil-moisture
  calibration family;
- WO2020047587A1 event-based auto-calibration and confidence/error logic;
- CN111103333B preset soil-element and temperature correction strategy;
- US7884620B2 and related Campbell/Advanced Sensor Technology
  moisture-and-salinity line;
- US11598743B2 Korean-priority resonance/reference sensor;
- US9804113B2 / US20150330932A1 MCU/RLC capacitive sensing;
- US11415612B2 METER complex-admittance/permittivity line;
- US7944220B2 Delta-T complex-impedance line;
- US7240743B2 Sentek insertion/contact line;
- US9146206B2 / EP2623971 fixture/reference-state calibration line;
- CN102944577A temperature-calibration apparatus;
- CN108414007B nonlinear temperature compensation;
- CN116298198A multi-parameter fusion;
- relevant Vegetronix, Campbell Scientific, METER/Decagon, Toro, Sentek,
  Delta-T, university, Indian, Chinese, and Korean applicants.

Do not assume a listed identifier is correct. Verify it independently.

Search primary technical literature on:

- low-cost capacitive-probe calibration;
- SEN0193 unit-to-unit variation;
- temperature and salinity/conductivity sensitivity;
- gravimetric calibration and dry-mass conventions;
- packing, contact, insertion, and remount effects;
- reference-media calibration;
- replacement-probe transfer;
- drift, ageing, contamination, and sensor health;
- uncertainty, abstention, and calibration validity;
- grouped physical validation and pseudoreplication.

## 9. Required legal separation

Analyze separately:

1. novelty;
2. inventive step/obviousness;
3. patent eligibility in the United States, EPO, and India;
4. FTO by live claim and jurisdiction.

Never conclude FTO from product differences, expired prior art, or failure to
find an exact duplicate.

## 10. Frozen-MVP assessment

Determine whether the complete frozen stack contains a credible independent
technical nucleus or is a predictable combination of:

- commodity capacitive sensing;
- nearby temperature measurement;
- controlled salinity metadata;
- ADC and analog hardening;
- linear/polynomial/ridge calibration;
- local fixed-coefficient MCU inference;
- gravimetric reference measurement;
- one-soil grouped validation.

Explicitly decide whether:

- the controlled salinity code is merely experimental design;
- the 72-run protocol is evidence generation rather than invention;
- the Week-1 ADC gate is engineering hygiene rather than invention;
- the absence of live EC is a cost/scope choice rather than novelty;
- the exact part numbers and budget create no patent distinction.

## 11. Required candidate-direction analysis

Evaluate and reject weak options. At minimum assess:

1. probe-specific characterization;
2. automatic calibration transfer to a replacement probe;
3. dual-probe disagreement used for validity/health rather than averaging;
4. insertion- and packing-aware compensation or invalidation;
5. remount/reinstallation acceptance testing;
6. contamination-protected drift adaptation;
7. confidence-gated or abstaining moisture estimates;
8. reference-event self-validation or bounded recalibration;
9. physics-informed low-order compensation;
10. calibration provenance and physical validity envelope;
11. lifecycle/ageing-state fingerprinting;
12. transfer across soil batches/classes;
13. multi-frequency moisture/salinity separation as a major redesign;
14. live-EC-assisted compensation as a major redesign;
15. any better mechanism supported by verified evidence.

For every direction report:

- physical technical problem;
- proposed contribution;
- closest patent and non-patent art;
- overlap and apparent difference;
- measurable physical effect;
- required baseline and ablations;
- architecture changes;
- cost and compute implications;
- three-month feasibility;
- later work;
- novelty, obviousness, eligibility, and FTO risks;
- confidence;
- kill condition;
- Track A, B, C, or D.

Tracks:

- **Track A:** credible invention already in the frozen MVP.
- **Track B:** credible bounded enhancement within three months and ₹5,000.
- **Track C:** connected later-semester path after a feasible semester MVP.
- **Track D:** no credible patent-development path established.

## 12. Level-1 versus Level-2 evidence

Keep these distinct:

### Level 1 — frozen compensation

Can a fixed local model reduce error for two probes in one homogeneous soil
under controlled moisture, temperature, and salinity-treatment conditions?

### Level 2 — robustness, validity, and transfer

Can a replacement, remounted, aged, contaminated, or physically mismatched
probe be accepted, transferred, recalibrated, rejected, or safely abstained
using a specific validated physical mechanism?

A successful Level-1 72-run result does not prove Level-2 transfer, sensor
health, field robustness, multi-soil generalization, patentability, or FTO.

## 13. Experimental requirements

Preserve the frozen engineering thresholds.

Any new patent-oriented threshold must be labelled **proposed** and must be
owner-approved before confirmatory testing.

Required baselines where relevant:

- raw/univariate mapping;
- multivariate linear model;
- ridge second-order model;
- full per-probe calibration oracle;
- naive coefficient reuse;
- one-point calibration;
- two-point affine transfer;
- pooled model;
- always-report model;
- simple min/max or distance gate;
- unrestricted event recalibration;
- no-adaptation model;
- every critical ablation of the proposed mechanism.

Required experimental factors where relevant:

- moisture;
- temperature;
- salinity treatment;
- physical replicate;
- probe unit and manufacturing lot;
- preparation batch;
- insertion/packing;
- remounting;
- ADC/wiring path;
- contamination;
- wet/dry cycling;
- drift/ageing proxy;
- later soil class.

Report:

- RMSE;
- MAE;
- bias;
- repeatability;
- probe-transfer error;
- remount/insertion error;
- subset error;
- valid/reject/abstention rate;
- false-valid rate;
- false invalidation;
- drift-detection delay;
- calibration workload;
- compute, RAM, flash, and timing.

Never treat rapid ADC readings or overlapping windows as independent physical
samples.

## 14. Confidentiality boundary

The following may be discussed generically:

- low-cost capacitive probes;
- temperature/salinity effects;
- ordinary regression;
- gravimetric calibration;
- the frozen 72-run engineering design.

Keep confidential pending institutional IPR review:

- exact physical-reference challenge sequences;
- probe fingerprints;
- transfer mappings;
- validity-envelope definitions;
- contamination gates;
- remount acceptance logic;
- lifecycle-state features;
- coefficient/provenance binding;
- parameter values;
- raw labelled transfer/remount/ageing datasets;
- code, negative results, and ablations;
- invention chronology and contributor records.

Do not recommend public disclosure before institutional IPR review.

## 15. Required output structure

Produce one Markdown report titled:

# TrueMoist Patent-Evidence Synthesis

Use exactly these sections:

1. Executive verdict
2. Input inventory
3. Project authority and frozen concept
4. Research-lane reliability audit
5. Search coverage and unresolved gaps
6. Verified patent-family ledger
7. Closest independent-claim analyses
8. Frozen-MVP feature chart
9. Named-lead and commercial-actor investigation
10. Non-patent prior art and measurement practice
11. Frozen-MVP patent assessment
12. Candidate invention-direction matrix
13. Strongest surviving direction
14. Level-1 compensation versus Level-2 robustness/transfer
15. Novelty
16. Inventive step/obviousness
17. Patent eligibility
18. FTO
19. Claim-to-experiment map
20. Three-month semester plan
21. Later-semester or publication extension
22. Budget, measurement, compute, and team feasibility
23. Kill criteria
24. Confidentiality boundary
25. Final TrueMoist recommendation
26. Unresolved questions
27. Source and verification log

The Executive verdict must choose exactly one:

- credible patent path in current MVP;
- credible path through bounded three-month enhancement;
- credible long-term path requiring later-semester extension;
- credible path only through major redesign;
- no credible patent path established.

The Final recommendation must choose exactly one:

- Advance as patent-first candidate;
- Advance conditionally pending named evidence;
- Retain as strong semester prototype but reduce patent priority;
- Deprioritize under the patent-first selection criterion.

State the Track and confidence explicitly.

## 16. Quality rules

- Do not invent patents, claims, families, legal status, standards, or results.
- Do not treat an abstract or description passage as an independent claim.
- Do not treat expired/abandoned records as irrelevant prior art.
- Do not treat expired/abandoned records as automatically blocking FTO.
- Do not call salinity-treatment code measured EC.
- Do not claim universal accuracy from one soil.
- Do not infer independent sample size from repeated ADC readings.
- Do not treat ridge regression, Mahalanobis distance, confidence scoring,
  abstention, event recalibration, probe transfer, or provenance as novel
  without claim-focused searching and technical evidence.
- Do not claim `HIGH/CLEAR` FTO without jurisdiction-specific claim charts and
  current official status.
- Do not compare TrueMoist with OpenBraille or VibeGuard.
- Do not select the final Project mC winner.
- Clearly distinguish verified fact, report assertion, inference,
  recommendation, and unresolved uncertainty.
