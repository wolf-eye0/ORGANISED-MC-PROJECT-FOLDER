# Phase 3C — TrueMoist Engineering Architecture Definition SOP

## Document Control

- Project: Project mC
- Concept: TrueMoist
- Phase: 3C — Engineering Architecture Definition
- Status: Active
- Purpose: Select and justify one coherent, buildable TrueMoist prototype architecture
- Team constraint: 5 members, including 3 technically strong CS/Cybersecurity members, 1 learner, and 1 presenter/support member
- Budget constraint: Preferred ≤ ₹3,000; absolute maximum ₹5,000
- Development window: Approximately 2 months
- Processing constraint: Local embedded processing; no continuous cloud dependency
- Current evidence state: Phase 3A and Phase 3B completed; Phase 3C decisions not yet frozen

## 1. Purpose of Phase 3C

Phase 3C converts the TrueMoist engineering hypothesis and Phase 3B feasibility findings into one defensible prototype architecture.

This phase must not merely list sensors, algorithms, or circuit options. It must resolve disagreements, select one implementation pathway, explain why competing pathways were rejected, and produce a blueprint detailed enough to guide implementation planning.

The output shall define the sensing architecture, signal path, controller platform, compensation method, calibration method, dataset procedure, validation procedure, test scenarios, cost assumptions, integration sequence, technical risks, and innovation-preservation strategy.

Phase 3C does not produce the final PCB, production firmware, enclosure, or manufacturing drawings. Those belong to later implementation phases.

## 2. Canonical Engineering Identity

TrueMoist is an affordable embedded intelligent sensing system intended to improve the trustworthiness of low-cost soil-moisture measurements.

It is not a generic irrigation controller, premium laboratory sensor, universal calibration-free probe, or cloud analytics platform.

Its defining contribution is local compensation of measurement error caused by environmental influences such as temperature, salinity/electrical conductivity, sensor drift, and repeatability limitations.

## 3. Mission

Enable more trustworthy irrigation decisions by improving the reliability of inexpensive soil-moisture sensing through local embedded compensation.

## 4. Engineering Hypothesis

A low-cost embedded system can use environmental measurements and calibration data to compensate for predictable error in an inexpensive soil-moisture sensor, producing estimates that are more stable and closer to gravimetric reference values than uncompensated sensor output under controlled test conditions.

## 5. Minimum Demonstrable Success

The architecture must support a prototype that can:

1. Acquire raw output from a low-cost soil-moisture sensor.
2. Measure or represent selected compensation variables, especially temperature and salinity/electrical-conductivity influence.
3. Generate an uncompensated moisture estimate.
4. Generate a compensated estimate locally on the embedded controller.
5. Compare both outputs against a gravimetric reference.
6. Demonstrate improvement in at least one predefined performance metric under controlled disturbances.
7. Produce interpretable results without continuous cloud processing.

The MVP does not need to prove universal performance across all soil types, crops, seasons, or field environments.

## 6. Frozen Project Constraints

- Budget: preferred ≤ ₹3,000; maximum ₹5,000.
- Approximately two months of development.
- Achievable by the existing five-member student team.
- Local embedded processing.
- No required continuous cloud connectivity.
- Off-the-shelf or easily fabricated components.
- One homogeneous soil type for the MVP unless evidence justifies otherwise.
- Physical ground truth must be used rather than another low-cost sensor.
- The prototype must show improved trustworthiness, not merely raw readings.
- Unsupported “calibration-free,” “universal,” or “laboratory-grade” claims are prohibited.
- Architecture must remain explainable and reproducible.

## 7. Authoritative Inputs

Use the following precedence:

1. Engineering Design Review
2. Phase 3B Engineering Feasibility Report and Memory
3. Phase 3A Engineering Landscape Report and Memory
4. Phase 2 Patent Report and Memory
5. Project Concept Context
6. Master Phase Document
7. Independent Phase 3C research reports
8. Project mC Decision Register

Later validated phase outputs take precedence over early summaries unless the later source contains unsupported concept drift.

## 8. Mandatory Concept-Grounding Check

Every research report and synthesis must restate:

- TrueMoist’s engineering identity
- engineering hypothesis
- minimum demonstrable success
- ₹3,000–₹5,000 budget
- two-month schedule
- local-processing requirement
- single-soil MVP boundary

Any report that converts TrueMoist into a generic irrigation controller, premium probe, cloud platform, or universal calibration system must be treated as concept drift and excluded.

## 9. Core Decision Questions

### 9.1 Moisture sensing

Determine the preferred low-cost capacitive sensor or sensing element, whether raw analog output is accessible, expected repeatability and drift, corrosion risks, and suitability for controlled compensation experiments.

### 9.2 Temperature sensing

Determine whether soil temperature, ambient temperature, or both should be measured; choose sensor type, placement, required resolution, and safe simulation method.

### 9.3 Salinity / electrical conductivity

Resolve whether the MVP should directly measure soil EC, use a low-cost EC circuit, use prepared conductivity conditions, infer salinity from controlled salt concentration, or treat salinity only as a controlled calibration variable.

Clearly distinguish variables measured during live operation from variables controlled only during validation.

### 9.4 ADC and analog front end

Resolve whether the MCU internal ADC is sufficient or whether an external ADC such as ADS1115 is necessary.

Assess effective resolution, noise floor, nonlinearity, grounding, filtering, shielding, cable length, power stability, and whether early soldering is mandatory.

An external ADC must be justified using an error budget rather than the claim that more bits are automatically better.

### 9.5 MCU selection

Compare ESP32, a suitable STM32, and any justified alternative using ADC quality, compute, RAM, tools, team familiarity, peripheral support, cost, and reproducibility.

### 9.6 Compensation algorithm

Compare static calibration curves, multivariate linear regression, polynomial regression, piecewise regression, lookup tables, adaptive filtering, recursive calibration, lightweight ML, and hybrid methods.

The selected method must be computationally feasible, interpretable, realistic to train, resistant to overfitting, and demonstrably better than raw output.

TinyML must not be selected only for novelty.

### 9.7 Calibration architecture

Define calibration variables, number of moisture/temperature/salinity levels, replicate count, equilibration time, sample preparation, training-validation split, coefficient storage, recalibration procedure, and model-transfer limitations.

### 9.8 Gravimetric reference

Define wet mass, dry mass, drying method, temperature and duration, container handling, scale resolution, formula, conversion assumptions, and uncertainty sources.

Where laboratory oven access is uncertain, provide a fallback and state its limitations.

### 9.9 Dataset requirements

Determine minimum viable dataset size, repeated readings, randomization, data-leakage controls, train/validation strategy, outlier policy, metrics, and how to avoid apparent accuracy caused by repeated readings from the same soil state.

### 9.10 Validation metrics

Select at least one primary and one secondary metric from MAE, RMSE, maximum error, repeatability, drift, hysteresis, coefficient of variation, temperature sensitivity, salinity sensitivity, and improvement over uncompensated readings.

### 9.11 Test scenarios

The architecture must support controlled comparisons such as:

- same moisture, different temperature
- same moisture, different salinity
- repeated wetting/drying
- raw versus compensated output
- calibration conditions versus held-out conditions
- short-term drift or warm-up behaviour

### 9.12 Output interface

Choose the simplest useful interface: serial plotter, USB logging, small display, RGB status, or local storage.

Evidence collection and interpretability take priority over visual complexity.

### 9.13 Power architecture

Determine USB versus external supply, sensor excitation, reference stability, regulator and decoupling needs, grounding, and whether battery operation is necessary.

### 9.14 Mechanical/sample arrangement

Define soil container, probe placement, depth, spacing, insertion method, packing method, sample mixing, and reduction of air gaps and density variation.

### 9.15 Patent and innovation preservation

Assess whether the architecture preserves a credible direction in compensation logic, adaptive calibration, error modeling, embedded decision logic, or low-cost validation workflow.

Ordinary sensor fusion or polynomial regression alone must not be treated as patentable.

Separate semester-project differentiation from actual patentability.

## 10. Candidate Architecture Families

### Architecture A — Minimal compensation demonstrator

- Capacitive moisture probe
- Temperature sensor
- Controlled salinity conditions
- MCU internal ADC
- Static or multivariate regression
- USB serial output

### Architecture B — Measurement-focused compensated sensor

- Capacitive moisture probe
- Temperature sensor
- Direct EC measurement
- External ADC
- Multivariate compensation
- Local display or serial logging

### Architecture C — Adaptive embedded calibration system

- Capacitive probe
- Temperature and EC inputs
- External ADC where justified
- Adaptive or recursive model
- On-device recalibration
- Local output and logging

### Architecture D — Offline training / embedded inference

- Controlled dataset collection
- Model trained offline
- Coefficients or lightweight model deployed to MCU
- Fully local runtime inference
- No cloud dependency

Additional architectures may be proposed but must be compared with these baselines.

## 11. Architecture Selection Criteria

Score candidates against:

1. Ability to prove the hypothesis
2. Measurement reliability
3. Calibration realism
4. Signal integrity
5. Computational feasibility
6. Cost
7. Two-month buildability
8. Team skill fit
9. Component availability
10. Validation clarity
11. Reproducibility
12. Risk of overclaiming
13. Innovation preservation
14. Patent/FTO compatibility
15. Upgrade potential

Select one primary architecture and at most one fallback.

## 12. Evidence Quality Rules

Primary evidence includes peer-reviewed papers, standards, manufacturer datasheets, and official technical documentation.

Secondary evidence includes credible engineering and institutional references.

Tertiary evidence includes tutorials, hobby projects, and marketplace listings.

Critical decisions about ADC adequacy, EC sensing, sensor performance, and gravimetric validation must rely mainly on primary sources.

Marketplace pages may support Indian price estimates only.

## 13. Hallucination and Concept-Drift Protocol

Exclude or quarantine sections that:

- analyze a different product or trademark
- assume premium sensors outside budget
- claim universal calibration without evidence
- substitute irrigation automation for sensing reliability
- require cloud processing
- make inaccessible lab equipment mandatory
- confuse soil EC with water EC without explanation
- fabricate citations, patents, standards, or specifications

Unsupported evidence must be excluded rather than averaged.

## 14. Mandatory Engineering Analyses

Every report must include:

- signal-chain diagram
- error budget
- data-flow diagram
- compute/RAM/flash budget
- power budget
- costed BOM
- risk register
- rejected-alternatives table

The error budget must include sensor repeatability, ADC error, temperature, salinity, packing, probe placement, gravimetric reference uncertainty, and model error.

## 15. Kill Factors

Explicitly evaluate:

- sensor output too unstable to model
- moisture and salinity effects inseparable
- external ADC provides no measurable advantage
- EC measurement unreliable in the selected arrangement
- gravimetric reference cannot be performed adequately
- dataset too small or correlated
- model overfits calibration conditions
- compensation worsens important edge cases
- soil packing dominates response
- unavailable equipment
- calibration workload exceeds timeline
- cost exceeds budget
- claimed innovation reduces to ordinary regression on commodity sensors

A kill factor is a condition that invalidates the architecture or forces the fallback.

## 16. Staged Validation Plan

### Stage 1 — Sensor characterization

Test repeatability, warm-up, insertion sensitivity, raw noise, drift, and internal versus external ADC if unresolved.

### Stage 2 — Controlled-variable testing

Hold moisture approximately constant while varying temperature and salinity. Repeat enough times to estimate variance.

### Stage 3 — Dataset generation

Prepare controlled moisture levels and record sensor output, temperature, EC/salinity condition, and gravimetric reference.

### Stage 4 — Model development

Fit baseline and candidate models, test on held-out conditions, and compare complexity, accuracy, and stability.

### Stage 5 — Embedded deployment

Port coefficients or model to the MCU, verify equivalence with offline results, and measure resource use.

### Stage 6 — Comparative demonstration

Display raw and compensated estimates against the reference and demonstrate at least one disturbance where compensation improves performance.

## 17. Required Deliverables

1. Phase 3C TrueMoist Architecture Report
2. Phase 3C TrueMoist Memory
3. Final system block diagram
4. Signal-chain diagram
5. Data-flow diagram
6. Selected sensing architecture
7. MCU and ADC decision
8. Compensation algorithm
9. Calibration procedure
10. Gravimetric procedure
11. Dataset plan
12. Validation matrix
13. Costed BOM
14. Power budget
15. Compute and memory budget
16. Mechanical/sample arrangement
17. Risk register
18. Kill-factor assessment
19. Rejected alternatives
20. Eight-week roadmap
21. Team allocation
22. Innovation and patent assessment
23. Phase 4 readiness decision
24. PDR update recommendations

## 18. Final Report Structure

1. Executive decision
2. Canonical concept restatement
3. Engineering hypothesis
4. Minimum demonstrable success
5. Evidence audit
6. Architecture candidates
7. Decision matrix
8. Selected architecture
9. Sensing subsystem
10. Analog front end and ADC
11. MCU and processing
12. Compensation algorithm
13. Calibration and dataset strategy
14. Gravimetric reference
15. Mechanical/sample design
16. Electrical and power design
17. Interface and logging
18. Validation plan
19. BOM
20. Resource budget
21. Risks and kill factors
22. Rejected alternatives
23. Patent and innovation implications
24. Team allocation
25. Eight-week roadmap
26. Unresolved questions
27. Readiness classification
28. PDR updates

## 19. Readiness Classification

### Architecture Ready
One coherent architecture is selected, fits budget and schedule, and has no blocking unresolved issue.

### Architecture Ready with Mandatory Early Validation
Architecture is selected, but one or more assumptions must be tested in Weeks 1–2.

### Architecture Conditionally Ready
A plausible design exists, but equipment, availability, or sensing uncertainty threatens feasibility.

### Architecture Not Ready
Evidence does not support a viable two-month prototype within budget.

## 20. Working Decision Boundaries

Unless strong evidence overturns Phase 3B:

- one homogeneous soil type
- gravimetric ground truth
- local embedded compensation
- temperature as a measured variable
- salinity/EC as either measured or rigorously controlled
- offline training permitted
- embedded inference required
- no universal calibration-free claim
- no dependence on custom patented probe hardware
- external ADC only when justified
- statistical regression preferred over TinyML unless TinyML clearly wins

These are starting boundaries, not automatic final decisions.

## 21. Team Allocation Guidance

### Member 1 — Embedded integration
MCU firmware, interfaces, model deployment, integration.

### Member 2 — Data and compensation
Dataset design, model fitting, metrics, offline-to-embedded equivalence.

### Member 3 — Hardware and validation
AFE, ADC testing, soil rig, electrical-noise control.

### Member 4 — Learner
Logging interface, data formatting, simple UI states, test scripts.

### Member 5 — Documentation and experimental support
Sample labels, experiment records, BOM, photographs, presentation.

Critical-path work must not depend exclusively on the learner or presenter/support member.

## 22. Eight-Week Boundary

- Week 1: component verification and sensor characterization
- Week 2: ADC/AFE decision and test-rig preparation
- Week 3: pilot measurements and procedure refinement
- Week 4: calibration dataset collection
- Week 5: model selection and offline validation
- Week 6: embedded deployment and integration
- Week 7: comparative validation and debugging
- Week 8: repeatability testing, documentation, and demonstration

Architectures requiring substantially more time must be rejected or reduced.

## 23. Exit Gate

TrueMoist may exit Phase 3C only when:

- one primary architecture is selected
- one fallback is documented
- ADC question is resolved
- EC/salinity approach is resolved
- compensation baseline is selected
- ground-truth method is operationally defined
- success metrics are fixed
- dataset plan is feasible
- cost is within limits
- kill factors have mitigations
- architecture is detailed enough for implementation planning

## 24. PDR Update Rules

After Phase 3C:

- PDR-031 becomes Accepted, Rejected, or Superseded.
- PDR-032 is resolved.
- PDR-045 is retained or revised.
- PDR-048 is confirmed or modified.
- PDR-049 is confirmed, rejected, or superseded.
- PDR-050 is confirmed or revised.
- New decisions receive new sequential PDR IDs.
- Historical provisional decisions are not deleted.

## 25. Final Principle

The goal is not to create the most sophisticated soil sensor.

The goal is to select the simplest architecture that convincingly proves low-cost soil-moisture sensing becomes more trustworthy when predictable environmental error is measured, modeled, and compensated locally.
