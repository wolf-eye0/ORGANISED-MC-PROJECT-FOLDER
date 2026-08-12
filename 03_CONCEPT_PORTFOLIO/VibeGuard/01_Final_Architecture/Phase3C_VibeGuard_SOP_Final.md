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
