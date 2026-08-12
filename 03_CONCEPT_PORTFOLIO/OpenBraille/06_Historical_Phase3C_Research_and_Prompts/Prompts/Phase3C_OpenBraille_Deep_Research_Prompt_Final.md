# Phase 3C — System Architecture & Prototype Planning

# Part 1 — Architecture Candidate Exploration

---

## ROLE

You are an elite multidisciplinary Engineering Architecture Review Board composed of:

- Embedded Systems Architect
- Mechanical Design Engineer
- Mechatronics Engineer
- Accessibility Technology Researcher
- Low-Cost Product Design Engineer
- Manufacturing Engineer
- Embedded Firmware Architect
- Electronics Hardware Engineer
- Industrial Design Engineer
- Systems Integration Specialist

Your responsibility is NOT to redesign OpenBraille.

Your responsibility is to identify, analyze, and compare all technically credible architecture candidates capable of implementing the approved OpenBraille engineering concept.

You are beginning the architecture design process—not making the final design decision.

---

# CONTEXT

The following phases have already been completed:

- Phase 1 – Opportunity Discovery
- Phase 2 – Patent Landscape Analysis
- Phase 3A – Engineering Landscape
- Engineering Design Review
- Phase 3B – Engineering Feasibility

These documents are authoritative.

They define:

- engineering identity
- engineering hypothesis
- minimum demonstrable success
- implementation constraints

Do NOT reinterpret the concept from its name.

Use the supplied documents as the official definition.

---

# APPROVED ENGINEERING IDENTITY

The OpenBraille concept exists to demonstrate that a significantly lower-cost actuation principle can replace conventional piezoelectric mechanisms while still producing a refreshable Braille cell with acceptable tactile performance.

The prototype is intended to validate the engineering hypothesis—not compete with commercial refreshable Braille displays.

The approved mission, engineering hypothesis, and minimum demonstrable success defined in the Engineering Design Review shall remain unchanged.

---

# OBJECTIVE

Explore every technically credible implementation architecture.

This phase is exploratory.

Do NOT recommend a final architecture.

Do NOT rank candidates.

Do NOT eliminate candidates unless they are clearly impossible or fundamentally incompatible with the approved engineering hypothesis.

---

# REQUIRED RESEARCH SOURCES

Prioritize evidence from:

- IEEE Xplore
- ACM Digital Library
- Google Scholar
- Engineering conference proceedings
- Mechanical design literature
- Assistive technology research
- Open-source refreshable Braille projects
- Commercial teardown analyses
- Component manufacturer documentation
- Industrial application notes

Use recent literature where available.

---

# TASKS

## 1. Concept Validation

Before beginning,

confirm that your understanding of OpenBraille matches the supplied documentation.

Explicitly restate:

- mission
- engineering hypothesis
- minimum demonstrable success

If uncertainty exists,

identify it before continuing.

---

## 2. Functional Decomposition

Break OpenBraille into its major engineering functions.

Examples include (where applicable):

- user interaction
- dot actuation
- mechanical transmission
- pin guidance
- actuation reset
- controller
- power
- firmware
- diagnostics

Describe the purpose of each function.

---

## 3. Candidate Actuation Principles

Identify every realistic actuation principle capable of satisfying the approved engineering hypothesis.

Examples may include (but are not limited to):

- electromagnetic
- magnetic latching
- miniature solenoid
- rotary-to-linear conversion
- geared mechanisms
- cam mechanisms
- shape-memory alloy
- voice coil
- other evidence-supported alternatives

For each candidate discuss:

- operating principle
- expected force characteristics
- response speed
- repeatability
- durability
- manufacturing considerations
- educational suitability
- known limitations

Do NOT recommend one.

---

## 4. Candidate Mechanical Architectures

Identify realistic mechanical arrangements.

Examples:

- direct-drive
- lever systems
- rocker mechanisms
- cam systems
- linkage systems
- rack-and-pinion
- magnetic coupling
- modular cartridges

Explain:

- motion path
- complexity
- fabrication challenges
- maintenance
- alignment sensitivity
- scalability

---

## 5. Candidate Control Architectures

Identify possible controller organizations.

Discuss:

- centralized control
- distributed control
- modular driver arrangement

Do NOT choose one.

---

## 6. Candidate Driver Strategies

Identify suitable driver approaches.

Examples include:

- H-bridge
- MOSFET switching
- transistor arrays
- dedicated driver ICs

Discuss:

- advantages
- disadvantages
- scalability
- educational suitability

---

## 7. Candidate Mechanical Materials

Discuss realistic material choices for:

- frame
- moving components
- guides
- return mechanisms

Consider:

- 3D printing
- acrylic
- aluminum
- engineering plastics
- spring materials

Discuss manufacturing implications.

---

## 8. Candidate Power Architectures

Explore:

- supply voltage options
- battery operation
- external power
- current requirements
- power stability

Without selecting a final design.

---

## 9. Manufacturing Pathways

Identify realistic manufacturing methods for a student team.

Include:

- 3D printing
- laser cutting
- off-the-shelf assembly
- local fabrication
- simple machining

Clearly distinguish between:

- highly feasible
- conditionally feasible
- unrealistic

---

## 10. Engineering Constraints

Summarize recurring constraints identified across the literature.

Examples:

- force
- stroke
- tolerance
- friction
- wear
- heat
- alignment
- tactile consistency
- assembly complexity

Support conclusions with evidence.

---

# IMPORTANT CONSTRAINTS

Do NOT:

- choose a final actuator
- choose an MCU
- choose exact hardware components
- design circuits
- estimate BOM
- draw system architecture
- produce CAD
- optimize firmware

Those belong to later parts of Phase 3C.

---

# DELIVERABLE

Produce a professional Engineering Architecture Exploration Report.

The report should comprehensively map the design space available for OpenBraille while remaining faithful to the approved Engineering Design Review.

The output of this report shall become the evidence base for architecture selection in Part 2.

Every engineering statement should be supported by evidence wherever reasonably possible.

Where uncertainty exists, acknowledge it explicitly rather than speculating.
 	



# Phase 3C — System Architecture & Prototype Planning

# Part 2 — Architecture Evaluation & Selection

---

# ROLE

You are the OpenBraille Engineering Architecture Selection Board.

You are no longer exploring possible implementations.

The architecture exploration has already been completed.

Your responsibility is to objectively evaluate the candidate architectures identified during Part 1 and determine which implementation pathway best satisfies the approved Engineering Design Review.

Every engineering decision shall be evidence-based.

---

# OBJECTIVE

Select the architecture that best demonstrates the approved engineering hypothesis while remaining achievable within the project's engineering constraints.

The selected architecture shall become the reference architecture for prototype development.

The objective is not to maximize technical sophistication.

The objective is to maximize engineering validation.

---

# PRIMARY DESIGN PRIORITIES

Architecture decisions shall prioritize, in order:

1. Preservation of the Engineering Design Review.
2. Validation of the engineering hypothesis.
3. Prototype manufacturability.
4. Educational feasibility.
5. Reliability.
6. Simplicity.
7. Cost effectiveness.
8. Future scalability.

Commercial optimization is outside the scope of this phase.

---

# REQUIRED EVALUATION

## 1. Candidate Architecture Review

Summarize every architecture candidate from Part 1.

For each candidate discuss:

- operating principle
- engineering maturity
- expected performance
- manufacturing complexity
- educational suitability
- compatibility with the Engineering Design Review

---

## 2. Evaluation Matrix

Construct a comparison matrix including:

- Preservation of engineering hypothesis
- Mechanical complexity
- Electrical complexity
- Firmware complexity
- Manufacturing difficulty
- Component availability
- Educational value
- Reliability
- Maintenance
- Expandability
- Cost confidence
- Prototype suitability
- Overall engineering confidence

Support every assessment with engineering reasoning.

---

## 3. Actuation System Selection

Evaluate every candidate actuation principle.

Discuss:

- expected tactile performance
- repeatability
- response speed
- force capability
- power consumption
- durability
- manufacturability
- implementation risk

Select the preferred actuation principle.

Clearly justify why the selected approach is superior for this project.

Explain why the remaining candidates were not selected.

---

## 4. Mechanical Architecture Selection

Select the preferred mechanical arrangement.

Discuss:

- motion transmission
- pin guidance
- alignment strategy
- reset mechanism
- structural design philosophy

Justify every decision.

---

## 5. Control Architecture Selection

Select:

- controller organization
- driver organization
- subsystem partitioning

Explain why this organization minimizes engineering complexity.

---

## 6. Hardware Platform Selection

Recommend the major hardware building blocks required.

This includes:

- MCU family
- driver approach
- power subsystem
- interface devices
- supporting electronics

For each recommendation:

- explain why it was selected
- explain why alternatives were rejected
- discuss compatibility with budget and educational constraints

---

## 7. Manufacturing Strategy

Recommend the preferred manufacturing pathway.

Discuss:

- fabrication method
- assembly strategy
- expected tolerances
- serviceability
- repairability
- prototype reproducibility

---

## 8. Architecture Risk Assessment

Identify:

- remaining technical risks
- mechanical risks
- integration risks
- manufacturing risks

Classify:

- High
- Medium
- Low

For every High or Medium risk,

propose realistic mitigation strategies.

---

## 9. Architecture Decision Records (ADR)

For every major engineering decision provide:

Decision

Context

Alternatives Considered

Selected Option

Reasoning

Trade-offs Accepted

Engineering Consequences

Future Flexibility

---

## 10. Architecture Confidence

Assess confidence in the selected architecture.

Discuss:

- supporting evidence
- remaining uncertainty
- assumptions
- validation requirements

Classify confidence as:

High

Moderate

Low

---

# IMPORTANT CONSTRAINTS

Do NOT:

- produce schematics
- design PCBs
- write firmware
- produce CAD drawings
- optimize manufacturing
- introduce new functionality
- alter the Engineering Design Review

The selected architecture must preserve the approved engineering identity.

---

# DELIVERABLE

Produce a professional Engineering Architecture Selection Report.

The report shall clearly identify one preferred architecture and provide sufficient engineering justification for every major design decision.

This report shall become the authoritative architectural reference for Part 3 of Phase 3C.

Every recommendation shall distinguish between:

- evidence directly supported by literature,
- engineering judgement based on evidence,
- assumptions requiring future validation.

The report should enable an engineering team to understand not only what architecture was selected, but why it was selected over every credible alternative.




# Phase 3C — System Architecture & Prototype Planning

# Part 3 — Final Architecture Definition & Prototype Blueprint

---

# ROLE

You are the Final Engineering Architecture Board for Project mC.

The architecture selection has already been completed.

Your responsibility is to transform the selected architecture into a complete engineering blueprint suitable for prototype implementation.

Do not reconsider alternative architectures unless a critical engineering flaw is discovered.

This document shall become the authoritative technical reference for OpenBraille implementation.

---

# CONTEXT

The following are authoritative:

- Engineering Design Review
- Phase 3A Report
- Phase 3B Report
- Phase 3C Part 1
- Phase 3C Part 2

The architecture selected in Part 2 shall remain the reference architecture.

---

# OBJECTIVE

Produce a complete architecture package that clearly defines how OpenBraille should be implemented while preserving the approved Engineering Design Review.

The architecture shall be sufficiently detailed that an engineering team can begin implementation planning.

---

# REQUIRED TASKS

## 1. Final Architecture Overview

Provide a concise overview of the selected architecture.

Explain:

- overall operating principle
- subsystem interaction
- expected workflow
- how the engineering hypothesis is validated

---

## 2. Complete System Block Diagram

Define the complete high-level system.

Include:

- power subsystem
- controller
- driver electronics
- actuator subsystem
- mechanical transmission
- Braille pin assembly
- user interface
- diagnostics (if applicable)

Describe every subsystem.

Explain its responsibility.

---

## 3. Hardware Architecture

Recommend the complete hardware architecture.

Include:

- MCU
- actuator(s)
- driver IC(s)
- power regulation
- connectors
- interface components
- protection circuitry
- passive components (high level)

For every hardware recommendation provide:

- justification
- expected function
- design considerations
- fallback option

---

## 4. Mechanical Architecture

Define:

- frame structure
- actuator placement
- force transmission
- pin guidance
- return mechanism
- assembly strategy
- maintenance considerations

Identify critical mechanical tolerances.

Discuss expected fabrication methods.

---

## 5. Electrical Architecture

Describe:

- power distribution
- signal flow
- driver arrangement
- electrical isolation (if required)
- wiring philosophy

Do not produce schematics.

---

## 6. Embedded Software Architecture

Describe the firmware organization.

Include:

- initialization
- control loop
- actuator control
- timing
- safety checks
- diagnostics
- configuration
- error handling

Do not write code.

---

## 7. Interface Definitions

Define the interfaces between every subsystem.

Examples:

- MCU ↔ Driver
- Driver ↔ Actuator
- Actuator ↔ Mechanical Assembly
- Firmware ↔ User Input

Clearly explain responsibilities.

---

## 8. Operating Sequence

Describe the complete operational workflow from power-on until one Braille refresh cycle is completed.

Explain each stage.

---

## 9. Prototype Validation Plan

Define:

- subsystem testing order
- integration sequence
- validation milestones
- acceptance criteria
- measurable success indicators

Ensure alignment with the approved Minimum Demonstrable Success.

---


## 10. High-Level Component Summary

Summarize all selected components.

For each include:

- purpose
- reason for selection
- fallback option

Do not provide purchasing links.

---

## 11. Remaining Engineering Risks

Identify:

- unresolved risks
- assumptions
- dependencies
- recommended future investigations

Classify each risk:

- High
- Medium
- Low

Provide mitigation strategies.

---
## 12. Prototype Assembly & Bring-Up Strategy

Define a practical engineering roadmap for assembling, integrating, and validating the prototype.

The objective is to minimize integration risk by recommending an evidence-based build sequence rather than assembling the complete system at once.

The strategy shall include:

### A. Assembly Sequence

Recommend the preferred order for assembling the major subsystems.

Examples include:

- Mechanical frame
- Actuator installation
- Mechanical transmission
- Braille pin assembly
- Electronics mounting
- Driver electronics
- MCU integration
- Power subsystem
- Firmware loading
- Final system integration

Justify why this sequence minimizes engineering risk.

---

### B. Bring-Up Strategy

Recommend the order in which the engineering team should power and validate the system.

Examples:

Stage 1
Mechanical verification only

Stage 2
Actuator movement verification

Stage 3
Driver electronics verification

Stage 4
MCU communication

Stage 5
Single actuation test

Stage 6
Complete Braille refresh cycle

Explain the objective of each stage.

---

### C. Subsystem Verification

For every subsystem identify:

- expected behaviour
- pass criteria
- common failure modes
- recommended troubleshooting approach

---

### D. Integration Checkpoints

Identify major integration milestones.

Examples include:

- Mechanical subsystem complete
- Electronics operational
- Actuator successfully driven
- Mechanical motion verified
- Single Braille pin validated
- Complete Braille cell validated

Define measurable success criteria for each checkpoint.

---

### E. Critical Failure Points

Identify the most likely causes of prototype failure.

Examples may include:

- Mechanical misalignment
- Insufficient actuator force
- Driver instability
- Excessive friction
- Timing errors
- Power instability
- Mechanical wear

For every failure point provide practical mitigation recommendations.

---

### F. Required Tools and Fabrication Resources

Recommend the minimum engineering resources required to complete the prototype.

Examples may include:

- 3D printer
- Laser cutter
- Basic machining services
- Soldering station
- Bench power supply
- Digital multimeter
- Oscilloscope (optional or recommended)
- Calipers
- Hand tools

Clearly distinguish between:

- Essential
- Recommended
- Optional

---

### G. Prototype Readiness Checklist

Provide a final engineering checklist confirming that the architecture is ready to enter implementation.

The checklist should verify:

- Mechanical architecture finalized
- Hardware architecture finalized
- Component selections completed
- Assembly pathway defined
- Validation plan completed
- Engineering risks documented
- Bring-up strategy completed

The objective of this section is to provide a structured transition from architecture planning to prototype implementation while minimizing integration uncertainty and reducing development risk.

## 13. Architecture Readiness Assessment

Assess whether the architecture is ready to enter prototype implementation.

Discuss:

- completeness
- confidence
- expected implementation challenges
- overall engineering readiness

Classify readiness as:

- Ready
- Ready with Minor Refinements
- Requires Additional Investigation

Support the decision with engineering evidence.

---

# IMPORTANT CONSTRAINTS

Do NOT:

- redesign the concept
- introduce new functionality
- produce PCB layouts
- produce CAD drawings
- write firmware
- optimize for commercial production

Maintain complete consistency with the Engineering Design Review and the selected architecture.

---

# FINAL DELIVERABLE

Produce a professional OpenBraille Architecture Package suitable for handoff to the implementation phase.

The package shall include:

- Final Architecture Overview
- Hardware Architecture
- Mechanical Architecture
- Electrical Architecture
- Embedded Software Architecture
- System Block Diagram (textual if diagrams cannot be rendered)
- Interface Definitions
- Component Summary
- Prototype Validation Plan
- Remaining Risks
- Architecture Readiness Assessment

Every engineering recommendation shall distinguish between:

- literature-supported evidence,
- engineering judgement,
- assumptions requiring prototype validation.

This document shall become the authoritative engineering reference for OpenBraille implementation.
