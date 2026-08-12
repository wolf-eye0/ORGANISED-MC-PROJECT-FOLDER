# Phase 3C — TrueMoist Final Engineering Architecture Synthesis Prompt

## ROLE

You are the final multidisciplinary Engineering Architecture Review Board for Project mC.

Act collectively as:
- Chief embedded-systems architect
- Analog and sensor-interface engineer
- Agricultural sensing specialist
- Measurement and calibration engineer
- Experimental-design and statistics reviewer
- Signal-processing and lightweight-ML specialist
- Reliability and validation engineer
- Cost and manufacturability reviewer
- Patent-awareness and innovation reviewer
- Academic prototype feasibility reviewer

Your job is not to summarize the five research reports independently. Your job is to audit them, compare their evidence, identify disagreements, exclude hallucinated or mis-scoped material, resolve the remaining technical questions, and select one coherent, buildable TrueMoist architecture.

## 1. AUTHORITATIVE PROJECT CONTEXT

TrueMoist is a low-cost embedded intelligent sensing system intended to improve the trustworthiness of inexpensive soil-moisture measurements.

Its engineering contribution is not basic moisture sensing. It is local compensation of predictable measurement error caused by temperature, salinity/electrical conductivity, sensor drift, sensor nonlinearity, repeatability limitations, and controlled environmental variation.

TrueMoist must not become a generic irrigation controller, premium laboratory soil sensor, universal calibration-free probe, cloud analytics platform, or full precision-agriculture product.

The minimum demonstrable prototype must show that a compensated moisture estimate performs better than the uncompensated estimate when both are compared with the same gravimetric reference under controlled disturbances.

## 2. FIXED PROJECT CONSTRAINTS

- Preferred budget: ≤ ₹3,000
- Absolute maximum: ₹5,000
- Development period: approximately two months
- Team: five members: three technically strong CS/Cybersecurity students, one learner, one presenter/support member
- No dedicated mechanical engineer
- Local embedded processing
- No required continuous cloud connectivity
- Off-the-shelf or student-accessible components
- One homogeneous soil type preferred for the MVP
- Gravimetric reference required as ground truth
- No unsupported claims of universal, calibration-free, or laboratory-grade accuracy
- Offline training permitted; runtime inference must remain local
- Arduino IDE or similarly accessible tooling preferred
- USB logging/output acceptable and preferred where practical

## 3. INPUT DOCUMENT HIERARCHY

Use the supplied files in this order of authority:

1. Engineering Design Review
2. Phase 3C TrueMoist SOP
3. Phase 3C TrueMoist Deep Research Prompt
4. Phase 3B Engineering Feasibility Report and Memory
5. Phase 3A Engineering Landscape Report and Memory
6. Phase 2 Patent Report and Memory
7. Project mC Decision Register
8. Project Concept Context
9. Master Project Phase Document
10. Five independent Phase 3C research reports

The independent research reports are evidence inputs, not authoritative truth. Later validated project documents take precedence over early summaries.

## 4. MANDATORY CONCEPT-GROUNDING CHECK

Before synthesis, restate:
- what TrueMoist is,
- what engineering problem it solves,
- its engineering hypothesis,
- its minimum demonstrable success,
- what it must not become,
- budget,
- timeline,
- team,
- local-processing requirement,
- and single-soil MVP boundary.

If a research report violates this grounding, mark the affected sections as concept drift and exclude them.

## 5. RESEARCH AUDIT METHOD

For each of the five research reports, evaluate:
- concept fidelity,
- source quality,
- citation reliability,
- technical correctness,
- architecture completeness,
- cost realism,
- experimental realism,
- recognition of uncertainty,
- and consistency with project constraints.

Do not use vote counting. A repeated claim is not automatically correct. A minority report may be preferred when it has stronger evidence.

Classify findings as:
- Strongly supported
- Supported with limitations
- Plausible but unverified
- Empirical prototype question
- Unsupported
- Contradicted
- Concept drift
- Hallucinated or unreliable

Entire mis-scoped sections must be excluded rather than averaged.

## 6. REQUIRED DISAGREEMENT RESOLUTION

Explicitly identify and resolve all important disagreements, especially:

### 6.1 Moisture sensor
Resolve preferred low-cost sensor/probe, raw analog accessibility, suitability for compensation experiments, repeatability, drift, corrosion risk, and whether a commodity capacitive probe is adequate.

### 6.2 Temperature sensing
Resolve soil versus ambient temperature, preferred sensor, placement, resolution, and fallback.

### 6.3 EC / salinity strategy
Select exactly one MVP strategy:
- live direct soil EC,
- pore-water or solution conductivity,
- controlled salinity as a calibration-only variable,
- hybrid calibration plus optional runtime EC,
- or another evidence-backed method.

Clearly distinguish bulk soil EC, pore-water EC, apparent EC, and solution conductivity.

### 6.4 MCU
Resolve ESP32-WROOM-32, ESP32-S3, STM32, or another justified controller. Select one primary MCU and one fallback.

### 6.5 ADC
Resolve internal MCU ADC, ADS1115, another external ADC, or a mandatory Week-1 comparison gate. Use an error-budget argument. Do not assume nominal 16-bit resolution automatically improves the system.

### 6.6 Analog front end
Resolve filtering, grounding, decoupling, sensor excitation, shielding, cable constraints, and breadboard versus soldered/perfboard implementation.

### 6.7 Compensation algorithm
Compare calibration curve, multivariate linear regression, polynomial regression, regularized regression, lookup table, piecewise model, adaptive recalibration, lightweight ML, and TinyML.

Select one baseline, one final MVP method, and at most one future upgrade. Do not select TinyML merely for novelty.

### 6.8 Calibration and dataset
Resolve moisture levels, temperature levels, salinity levels, replicate count, expected total samples, equilibration, grouped validation, leakage prevention, and two-month feasibility.

### 6.9 Gravimetric reference
Resolve preferred drying procedure, drying temperature and duration, scale resolution, formula, uncertainty, and fallback if a laboratory oven is unavailable.

### 6.10 Validation metrics
Select one primary metric, one secondary metric, and realistic success thresholds. The primary metric should focus on improvement of compensated versus uncompensated estimates against the same gravimetric reference. Absolute accuracy must still be reported.

### 6.11 Mechanical test rig
Resolve soil container, sample mass, packing method, probe depth, sensor spacing, repeatable insertion, air-gap control, and labeling.

### 6.12 Interface and logging
Resolve USB serial, CSV schema, display requirement, SD-card requirement, and simplest convincing demonstration method.

### 6.13 Patent and innovation direction
Separate engineering differentiation, semester-project novelty, possible future patent direction, and actual patentability. Do not claim ordinary sensor fusion or polynomial regression alone is patentable.

## 7. ARCHITECTURE SELECTION RULE

Select one primary architecture and at most one fallback.

The primary architecture must specify:
- moisture sensor,
- temperature sensor,
- EC/salinity method,
- MCU,
- ADC,
- analog front end,
- sampling strategy,
- compensation algorithm,
- offline training method,
- embedded inference method,
- calibration procedure,
- gravimetric reference,
- mechanical test arrangement,
- logging/output,
- power architecture,
- expected cost,
- and readiness status.

## 8. REQUIRED EARLY VALIDATION GATES

Define Week-1 and Week-2 tests for:
- raw sensor repeatability,
- soil-packing sensitivity,
- probe insertion sensitivity,
- internal versus external ADC if relevant,
- EC/salinity feasibility,
- gravimetric workflow,
- and pilot dataset feasibility.

For each gate specify exact procedure, pass threshold, fail threshold, and fallback action.

## 9. REQUIRED FINAL REPORT STRUCTURE

1. Executive Architecture Decision
2. Canonical Concept Restatement
3. Engineering Hypothesis
4. Minimum Demonstrable Success
5. Evidence Audit of all five reports
6. Cross-Report Agreement and Disagreement Map
7. Candidate Architecture Families
8. Comparative Decision Matrix
9. Final Selected Architecture
10. System Block Diagram
11. Moisture Sensing Subsystem
12. Temperature Sensing Subsystem
13. EC / Salinity Strategy
14. Analog Front End and ADC Decision
15. MCU and Embedded Architecture
16. Sampling and Preprocessing
17. Compensation Algorithm
18. Calibration Dataset Design
19. Gravimetric Ground-Truth Procedure
20. Mechanical Soil-Test Rig
21. Data Logging and Dataset Schema
22. Validation Metrics and Pass Criteria
23. Prototype Test Matrix
24. Electrical and Power Architecture
25. User Interface and Demonstration
26. Costed BOM
27. Compute, Memory, Storage, and Power Budget
28. Risk Register
29. Rejected Alternatives
30. Patent and Innovation Implications
31. Team Allocation
32. Eight-Week Roadmap
33. Phase 4 Readiness Decision
34. Project Decision Register Updates
35. Phase 3C TrueMoist Memory

## 10. PDR UPDATE REQUIREMENTS

Recommend precise changes to:
- PDR-031
- PDR-032
- PDR-045
- PDR-048
- PDR-049
- PDR-050

Identify any genuinely new PDR decisions. Preserve decision history.

## 11. READINESS CLASSIFICATION

Choose one:
- Architecture Ready
- Architecture Ready with Mandatory Early Validation
- Architecture Conditionally Ready
- Architecture Not Ready

## 12. QUALITY REQUIREMENTS

The synthesis must:
- select one architecture,
- use evidence rather than model voting,
- cite source documents and external evidence where present,
- distinguish fact from inference,
- preserve uncertainty,
- expose unsupported claims,
- identify prototype-only assumptions,
- remain within ₹5,000,
- fit approximately two months,
- avoid cloud dependency,
- avoid patent overclaiming,
- and provide an executable build-and-validation path.

Do not conclude that the system is feasible merely because individual components exist.

Judge the full chain:
soil preparation → sensing → acquisition → calibration → ground truth → model training → embedded inference → controlled validation → demonstration.

## FINAL DECISION QUESTION

What is the simplest technically defensible TrueMoist architecture that can convincingly demonstrate that local environmental compensation improves the trustworthiness of a low-cost soil-moisture sensor?
