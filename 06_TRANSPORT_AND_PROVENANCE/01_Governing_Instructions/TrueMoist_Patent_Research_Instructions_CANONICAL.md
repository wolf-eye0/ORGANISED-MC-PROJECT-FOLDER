# Project mC — TrueMoist Current Patent Verification — Independent Research

## Role

Act as an independent patent-research and engineering-review board covering
patent searching, patent families/legal status, embedded sensing, analog
measurement, soil-moisture calibration, experimental design, patent
eligibility, and FTO risk.

This is one blind independent research lane. Do not use another model's
TrueMoist report, OpenBraille/VibeGuard research, prior-chat context, or
cross-concept ranking.

Evidence cut-off: 1 August 2026.

This is technical research and project decision support, not legal advice,
patentability/FTO clearance, claim construction, or an infringement opinion.

## Expected files

Confirm exactly 11 readable attachments:

00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md
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

Stop only if the governing instruction or a required project-authority file is
missing/unreadable. Do not substitute Decision Register v1.1.

## Authority order

1. Engineering Design Review
2. Decision Register v1.2
3. approved Phase 3C closure memo
4. final TrueMoist architecture report
5. final TrueMoist memory
6. final TrueMoist SOP
7. validated evidence files
8. Phase 2 only as historical patent-search leads

## Current constraints

- Up to three months.
- Preferred budget ≤ ₹3,000; absolute ceiling ₹5,000.
- Five members: three technically strong, one learner, one presenter/support.
- Patent potential matters, but buildability remains mandatory.
- New mechanisms, calibration rules, datasets and results remain confidential
  until institutional IPR review.

## Frozen TrueMoist MVP

TrueMoist is a local compensation system for a low-cost analog capacitive
soil-moisture probe.

Sensing:
- genuine analog capacitive probe, SEN0193-class or characterized equivalent;
- two probe units available for characterization/variation testing;
- waterproof DS18B20 at the same depth, about 20–30 mm from the moisture probe;
- controlled salinity treatment expressed as known salt addition per dry-soil
  mass;
- no mandatory live runtime EC sensor;
- salinity-treatment code is not measured bulk-soil EC, apparent EC,
  pore-water EC or solution conductivity.

Acquisition:
- ESP32-WROOM-32 primary; ESP32-S3 fallback;
- ADS1115 primary, with mandatory Week-1 comparison against calibrated ESP32
  ADC1;
- retain ADS1115 only when noise, repeatability, pilot RMSE or reproducibility
  justify it;
- approximately 1 kΩ series resistance, 100 nF input filtering, local 100 nF
  and 10 µF decoupling, short analog wiring, fixed connectors, deliberate
  grounding and soldered perfboard after Week-1 characterization;
- USB 5 V and USB serial CSV;
- no cloud/app dependency.

Modelling:
- uncompensated baseline: univariate mapping from raw probe response;
- modelling baseline: multivariate linear regression;
- final MVP candidate: ridge-regularized second-order regression;
- inputs: raw probe response, measured soil temperature, controlled
  salinity-treatment code;
- train offline in Python;
- deploy fixed coefficients locally on ESP32;
- no TinyML requirement and no on-device adaptive training in the frozen MVP.

Dataset:
- one homogeneous soil source and one documented preparation/packing method;
- 4 moisture × 3 temperature × 2 salinity × 3 independent replicates;
- 72 independent physical runs;
- replicates 1–2 for training/model selection and replicate 3 as untouched
  physical test data;
- rapid ADC readings may be averaged but never counted as independent
  physical samples;
- dry-basis gravimetric water content as ground truth;
- drying near 105 ± 5 °C for at least 24 h and until constant mass;
- 0.01 g scale preferred;
- do not claim volumetric water content unless bulk density is independently
  measured.

Engineering success on untouched test replicates:
- compensated RMSE at least 20% lower than uncompensated;
- compensated MAE at least 15% lower;
- report absolute errors and disturbance-subset performance.

Passing these thresholds does not prove patentability.

## Concept fidelity

TrueMoist is not an irrigation controller, cloud agriculture platform,
universal calibration-free probe, laboratory reference instrument, live EC
meter, custom multi-frequency probe, TinyML showcase, online-adaptive learner,
or multi-soil system.

A live-EC, multi-frequency, custom-probe, multi-soil or cloud architecture may
appear only as an explicitly labelled later extension/major redesign.

## Core patent questions

Determine:

1. whether the frozen MVP itself has a credible patent contribution;
2. whether it is a conventional combination of capacitive sensing,
   temperature/salinity compensation, regression, ADC conditioning, local MCU
   inference and gravimetric calibration;
3. whether controlled salinity without live EC has patent relevance or is only
   experimental design;
4. whether the factorial dataset/grouped validation contributes anything
   patent-relevant;
5. whether a bounded three-month enhancement can create a credible path;
6. whether the strongest path requires later-semester transfer/field work;
7. whether probe replacement transfer, drift/ageing detection,
   insertion/packing compensation, uncertainty gating, self-validation or
   calibration validity can form a specific technical contribution;
8. whether any surviving direction requires a major hardware redesign;
9. what evidence would support or kill each direction;
10. what live claims create FTO concerns in relevant jurisdictions.

Do not infer patentability from failure to find an exact duplicate.

## Search method

Provide a reproducible search log: database, date, exact query, CPC/IPC
classes, assignee/inventor searches, citation chains, selected/rejected
results.

Prefer InPASS, WIPO, USPTO, EPO and relevant official Asian registers.
Google Patents may support discovery/claim reading but not a load-bearing
status conclusion.

Read independent claims, not only titles/abstracts. Separate publication,
grant, pending/abandoned/expired status, prior-art relevance and FTO relevance.

Search primary technical literature on low-cost capacitive probes,
temperature/salinity effects, dielectric sensing, gravimetric calibration,
probe variability, insertion/packing effects, drift, ageing, uncertainty and
calibration transfer.

Search and expand at least:

- capacitive soil moisture temperature compensation patent
- soil moisture salinity compensation capacitance patent
- dielectric soil moisture conductivity correction
- commodity probe calibration transfer
- probe-to-probe soil-moisture calibration
- soil-moisture sensor drift/ageing compensation
- insertion and packing-density compensation
- remount/reinstallation calibration validity
- gravimetric calibration capacitive soil moisture
- polynomial/ridge regression sensor calibration
- edge soil-moisture compensation microcontroller
- uncertainty-gated or abstaining moisture estimate
- dual-probe disagreement sensor health
- reference-event self-calibration
- multi-soil calibration transfer
- multi-frequency moisture/salinity separation
- sensor replacement automatic recalibration

Identify actual relevant families associated with METER/Decagon, Campbell
Scientific, Sentek, Delta-T, Vegetronix, low-cost probe manufacturers, major
irrigation/agriculture firms, universities, and Indian/Chinese applicants.
Do not infer claim scope from company products.

## Required legal separation

Analyze separately:

- novelty;
- inventive step/obviousness;
- patent eligibility in the US/EPO/India;
- FTO by live claim and jurisdiction.

## Frozen-feature chart

Compare prior art against the complete frozen architecture, including probe,
DS18B20 placement, controlled salinity, no live EC, ADS1115/ADC comparison,
analog hardening, ESP32 local inference, all three regression levels,
one-soil/72-run grouped validation, gravimetric truth, transfer/drift/
insertion/packing/validity features.

Use only:
- expressly disclosed;
- necessarily implied;
- arguably suggested;
- absent;
- unresolved.

## Candidate directions

Evaluate and reject weak options. At minimum assess:

1. probe-specific characterization and automatic calibration transfer;
2. dual-probe disagreement used for validity/health, not simple averaging;
3. insertion- and packing-aware compensation;
4. contamination-protected drift adaptation;
5. confidence-gated/abstaining moisture estimates outside the validated
   physical domain;
6. reference-event self-validation or bounded recalibration;
7. physics-informed low-order compensation beyond generic polynomial fitting;
8. calibration provenance and validity envelope;
9. later transfer across soil batches/classes;
10. multi-frequency moisture/salinity separation as a later redesign;
11. live-EC-assisted compensation as a later extension/redesign;
12. any better direction supported by verified evidence.

For each state: problem, contribution, closest patent/NPL, overlap,
difference, physical effect, baseline, experiment, changes, cost, three-month
feasibility, later work, novelty/obviousness/eligibility/FTO risks, confidence,
kill condition, and Track A/B/C/D.

Tracks:
- A: credible invention already in frozen MVP.
- B: credible bounded enhancement within three months and ₹5,000.
- C: connected later-semester path after a feasible semester MVP.
- D: no credible patent-development path established.

## Experimental evidence

Preserve the existing engineering thresholds. Additional patent-oriented
thresholds must be labelled proposed and owner-approved before testing.

Compare:
- univariate raw baseline;
- multivariate linear baseline;
- ridge second-order candidate;
- every proposed enhancement;
- ablations removing each allegedly inventive element.

Where relevant vary moisture, temperature, salinity treatment, replicate,
probe unit, insertion, packing, remounting, drift/ageing, preparation batch
and later soil class.

Report RMSE, MAE, bias, repeatability, probe-transfer error,
insertion/remount error, subset error, rejection/validity rate, confidence,
drift-detection delay, false invalidation, ADC repeatability, compute and
memory.

Never count repeated ADC samples as independent physical samples.

## Required report

# TrueMoist Current Patent Verification — Independent Research

1. Executive verdict
2. Input inventory and concept fidelity
3. Search methodology and reproducible log
4. Technical and patent landscape
5. Verified patent-family ledger
6. Closest independent-claim analyses
7. Frozen-MVP feature comparison
8. Commercial/institutional/India/China landscape
9. Non-patent prior art and measurement practice
10. Frozen-MVP patent assessment
11. Candidate invention-direction matrix
12. Strongest surviving direction
13. Level-1 compensation versus Level-2 robustness/transfer
14. Novelty
15. Inventive step/obviousness
16. Patent eligibility
17. FTO
18. Claim-to-experiment map
19. Three-month semester plan
20. Later-semester/publication extension
21. Budget, measurement, compute and team feasibility
22. Kill criteria
23. Confidentiality boundary
24. Final recommendation
25. Unresolved questions
26. Source and verification log

Executive verdict must choose exactly one:
- credible patent path in current MVP;
- credible path through bounded three-month enhancement;
- credible long-term path requiring later-semester extension;
- credible path only through major redesign;
- no credible patent path established.

Final recommendation must choose exactly one:
- Advance as patent-first candidate;
- Advance conditionally pending named evidence;
- Retain as strong semester prototype but reduce patent priority;
- Deprioritize under the patent-first selection criterion.

Do not compare with other Project mC concepts or select the winner.

## Quality rules

Do not invent patents, families, status, standards or results.
Do not treat expired patents as irrelevant prior art.
Do not treat expired/abandoned records as automatically blocking FTO.
Do not equate low cost, ESP32, ADS1115, DS18B20, a capacitive probe,
controlled salinity, regression or gravimetric validation with novelty.
Do not claim universal accuracy from one soil.
Do not describe the salinity code as measured EC.
Do not silently add live EC, multi-frequency hardware, irrigation, cloud or
multi-soil scope.
Clearly separate verified fact, source assertion, inference, recommendation
and unresolved uncertainty.
Cite every load-bearing patent/status/technical conclusion.
