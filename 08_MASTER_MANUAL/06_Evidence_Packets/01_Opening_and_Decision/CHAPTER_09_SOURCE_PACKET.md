# Chapter 09 — Comparative Decision and Proposed Concept Shift

## Controlled source packet

This packet contains hash-verified source extracts. The sources have not been reconciled, corrected or converted into final manual conclusions.

Mapped sources in packet: **18**


---

## Source 1: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/00_Engineering_Design_Review.md`
- Current SHA-256: `46f017501ac3ff9ebd6c1fb1e5ee8c068c22ddb08ae204c5609f2b759090295e`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Engineering Design Review

Engineering Design Review Overview

Purpose

The Engineering Design Review (EDR) serves as the transition between Phase 3A – Engineering Landscape Analysis and Phase 3B – Engineering Feasibility Analysis.

Its purpose is not to redesign concepts or determine implementation details. Instead, it validates that each shortlisted concept possesses:

a clearly defined engineering problem,
a measurable engineering hypothesis,
an appropriate prototype scope,
fixed design principles,
and sufficient technical maturity to justify feasibility analysis.

Throughout this review, every concept was challenged to reduce unnecessary complexity, eliminate ambiguous objectives, and define the smallest prototype capable of validating its core engineering hypothesis.

No concept was eliminated during this review.

Any future down-selection will occur only after objective engineering evidence is collected during subsequent feasibility and architecture phases.

Review Methodology

Each concept was reviewed using the following framework:

Original Vision
Engineering Identity
Mission
Engineering Hypothesis
Engineering Foundation
Phase 3A Validation
Invalidated Assumptions
Major Engineering Risks
Open Questions
Fixed Design Principles
Minimum Demonstrable Success
Phase 3B Evaluation Objectives
Review Board Decision
Review Notes

This methodology ensures that every concept enters Phase 3B with a stable engineering objective while avoiding premature implementation decisions.


Project: Project mC

Status:
🔄 Ongoing

---

# Concept 1 — OpenBraille

Review Status

✅ Approved for Phase 3B Evaluation

---

## Original Vision

Develop a significantly lower-cost refreshable Braille system by replacing the expensive actuation mechanism used in conventional refreshable Braille displays while maintaining the core functionality of tactile refreshability.

---

## Engineering Identity

OpenBraille is an assistive embedded system focused on making refreshable Braille technology more affordable through the exploration of alternative low-cost actuation strategies.

Rather than competing with commercial high-end Braille displays, the project aims to validate whether refreshable tactile output can be achieved using substantially lower-cost engineering approaches suitable for educational and resource-constrained environments.

---

## Mission

Make refreshable Braille technology significantly more affordable and accessible.

---

## Engineering Hypothesis

A lower-cost actuation strategy can replace conventional piezoelectric actuation while maintaining acceptable tactile performance for a refreshable Braille interface.

---

## Engineering Foundation

The concept builds upon mature accessibility engineering, embedded systems, tactile interface design, and refreshable Braille technologies while investigating improvements within the actuation subsystem.

---

## Phase 3A Validation

Phase 3A confirmed that:

- Refreshable Braille is a mature engineering domain.
- Commercial systems are dominated by expensive piezoelectric mechanisms.
- The major engineering opportunity lies in reducing actuation cost rather than reinventing the overall system.
- Existing research provides sufficient engineering knowledge to support feasibility analysis.

---

## Invalidated Assumptions

None identified.

Phase 3A refined the understanding of the engineering problem but did not invalidate the original concept.

---

## Major Engineering Risks

- Achieving sufficient tactile force.
- Mechanical durability.
- Repeatable refresh cycles.
- Manufacturing simplicity.
- Cost-performance trade-offs.

---

## Open Questions

Phase 3B must determine:

- Which actuation strategy is technically realistic?
- Can acceptable tactile performance be achieved?
- Can the solution remain within the project budget?
- Can the prototype be completed within the semester timeline?

---

## Fixed Design Principles

- Focus on affordability.
- Maintain refreshable functionality.
- Demonstrate a real engineering prototype.
- Preserve compatibility with standard Braille principles where appropriate.
- Avoid dependence on expensive piezoelectric mechanisms if a viable alternative exists.

---

## Minimum Demonstrable Success

Demonstrate that a significantly lower-cost actuation strategy can reliably produce refreshable tactile Braille output for at least one Braille cell while meeting basic tactile and repeatability requirements.

---

## Phase 3B Evaluation Objectives

Evaluate whether the engineering hypothesis can be implemented by:

- Three technically capable CSE/Cybersecurity students.
- A prototype budget of ₹3000–₹5000.
- Approximately two months of development.

---

## Review Board Decision

✅ Approved to proceed to Phase 3B Engineering Feasibility Analysis.

The concept remains technically relevant, possesses a clearly defined engineering objective, and has a measurable prototype scope suitable for feasibility evaluation.

---

## Review Notes

The review concluded that the identity of OpenBraille should be defined by its mission of affordable refreshable Braille rather than by any specific actuator technology.

Future phases must evaluate engineering approaches without prematurely committing to a particular implementation.

# Concept 2 — VibeGuard

## Review Status

✅ Approved for Phase 3B Evaluation

---

## Original Vision

Develop a low-cost embedded predictive maintenance system capable of monitoring machine vibrations and providing early warning of abnormal operating conditions before failures occur. The concept targets small and medium-sized industries that often lack access to expensive industrial condition monitoring solutions.

---

## Engineering Identity

VibeGuard is an embedded edge-intelligence condition monitoring system designed to improve machine reliability by analyzing vibration data locally on resource-constrained hardware.

Rather than functioning as a conventional vibration sensor, the system seeks to interpret vibration patterns and identify early indicators of abnormal machine behaviour. Its objective is to provide affordable predictive maintenance capabilities through intelligent embedded analysis rather than expensive industrial monitoring infrastructure.

---

## Mission

Enable affordable predictive condition monitoring through the early detection of abnormal machine behaviour, reducing unplanned downtime and supporting proactive maintenance decisions.

---

## Engineering Hypothesis

A low-cost embedded edge-intelligence system can locally analyze machine vibration signals and reliably distinguish normal operating conditions from early abnormal behaviour using computational methods suitable for resource-constrained hardware.

---

## Engineering Foundation

The concept builds upon mature engineering domains including:

- Predictive maintenance
- Condition monitoring
- Embedded systems
- MEMS vibration sensing
- Edge computing
- Embedded signal processing
- TinyML and lightweight machine intelligence

Phase 3A established that while industrial vibration monitoring is a mature field, opportunities remain in developing affordable, locally intelligent solutions suitable for small-scale industrial environments.

---

## Phase 3A Validation

Phase 3A confirmed that:

- Machine vibration is one of the most established indicators of equipment health.
- Predictive maintenance is a well-developed engineering discipline with extensive industrial adoption.
- Edge computing offers practical advantages by reducing latency, bandwidth requirements, and dependence on cloud infrastructure.
- Affordable embedded predictive maintenance remains an active area of engineering interest, particularly for SMEs that cannot justify the cost of enterprise monitoring systems.
- The concept aligns well with current research trends involving embedded intelligence, lightweight analytics, and low-cost industrial monitoring.

---

## Invalidated Assumptions

No major assumptions from Phase 1C were invalidated.

However, Phase 3A refined the concept by demonstrating that the innovation does not lie in vibration sensing itself, but in performing meaningful condition analysis locally using inexpensive embedded hardware.

This distinction significantly clarified the engineering direction of the project.

---

## Major Engineering Risks

The primary engineering risks identified include:

- Distinguishing meaningful abnormal vibration from environmental noise.
- Achieving reliable classification using limited computational resources.
- Preventing false positives and false negatives.
- Designing algorithms suitable for constrained embedded platforms.
- Maintaining repeatable performance across varying operating conditions.

---

## Open Questions

Phase 3B should determine:

- Which sensing approach provides sufficient fidelity for the intended prototype.
- Which embedded analysis technique offers the best balance between performance and computational cost.
- Whether lightweight machine learning, statistical analysis, rule-based methods, or hybrid approaches are most appropriate.
- Whether the complete prototype can be achieved within the available budget and semester timeline.
- How prototype validation should be performed using representative machinery or controlled experimental setups.

---

## Fixed Design Principles

The following principles were approved during the Engineering Design Review and shall remain unchanged in later phases:

- Maintain affordability as a primary design objective.
- Perform condition analysis locally on embedded hardware.
- Focus on early detection of abnormal operating behaviour rather than comprehensive industrial fault diagnosis.
- Produce interpretable and repeatable maintenance alerts.
- Avoid dependence on continuous cloud connectivity.
- Ensure the solution remains suitable for educational prototypes and SME-oriented applications.

---

## Minimum Demonstrable Success

Demonstrate that a low-cost embedded prototype can acquire vibration data from a representative machine or controlled test rig, consistently distinguish between normal and deliberately introduced abnormal operating conditions, and generate an interpretable early maintenance alert without relying on cloud processing.

---

## Phase 3B Evaluation Objectives

Phase 3B shall evaluate whether the engineering hypothesis can realistically be implemented by:

- Three technically capable Computer Science / Cybersecurity students.
- A prototype budget of ₹3000–₹5000.
- Approximately two months of development.

The feasibility study shall focus on identifying an engineering approach that satisfies the project's technical objectives while remaining within practical educational constraints.

---

## Review Board Decision

✅ Approved to proceed to Phase 3B Engineering Feasibility Analysis.

The review concluded that VibeGuard possesses a clearly defined engineering objective, a focused and testable hypothesis, an achievable prototype scope, and strong alignment with both current industrial engineering trends and the team's technical capabilities.

---

## Review Notes

The Engineering Design Review determined that the defining characteristic of VibeGuard is not vibration measurement itself, but the ability to perform meaningful condition analysis locally through embedded edge intelligence.

Future phases should therefore concentrate on evaluating computational strategies and embedded implementation approaches rather than treating the project as a conventional vibration sensing system.


# Concept 3 — TrueMoist

## Review Status

✅ Approved for Phase 3B Evaluation

---

## Original Vision

Develop an affordable intelligent soil moisture monitoring system capable of improving the reliability of low-cost soil moisture sensors by compensating for environmental influences and sensor drift. The objective is to support better irrigation decisions without relying on expensive agricultural sensing solutions.

---

## Engineering Identity

TrueMoist is an embedded intelligent sensing system designed to improve the long-term trustworthiness of low-cost soil moisture measurements.

Rather than attempting to compete directly with premium soil moisture sensors, the concept focuses on enhancing the reliability of inexpensive sensing hardware through adaptive embedded intelligence, allowing practical irrigation support while maintaining affordability for smallholder farmers and educational deployments.

---

## Mission

Enable affordable and trustworthy irrigation decision-making by improving the reliability of low-cost soil moisture sensing.

---

## Engineering Hypothesis

A low-cost embedded system can intelligently compensate for sensor drift and environmental influences, allowing inexpensive soil moisture sensors to produce consistently reliable measurements suitable for practical irrigation support.

---

## Engineering Foundation

The concept builds upon mature engineering domains including:

- Precision agriculture
- Soil moisture sensing
- Embedded systems
- Environmental sensing
- Adaptive signal processing
- Sensor calibration techniques
- Edge intelligence

Phase 3A established that while soil moisture sensing is a mature engineering field, significant opportunities remain in improving the trustworthiness of inexpensive sensors operating under varying environmental conditions.

---

## Phase 3A Validation

Phase 3A confirmed that:

- Soil moisture sensing technologies are well established.
- Low-cost sensors commonly suffer from sensor drift, salinity sensitivity, temperature variation, aging effects, and calibration degradation.
- Premium sensing systems achieve higher reliability primarily through improved sensing technologies and sophisticated calibration.
- Adaptive embedded compensation represents a promising engineering direction for improving low-cost sensor performance.
- Reliable measurement is more valuable than simply increasing measurement frequency.

---

## Invalidated Assumptions

No major assumptions from Phase 1C were invalidated.

However, Phase 3A significantly refined the concept by demonstrating that the innovation is not the soil moisture sensor itself, but the intelligent compensation of measurement errors and environmental influences affecting inexpensive sensors.

This clarified the engineering focus of the project.

---

## Major Engineering Risks

The primary engineering risks identified include:

- Correctly identifying sensor drift.
- Distinguishing environmental influences from genuine moisture changes.
- Developing adaptive compensation suitable for constrained embedded hardware.
- Maintaining stable long-term calibration performance.
- Preventing overcompensation or inaccurate correction under changing environmental conditions.

---

## Open Questions

Phase 3B should determine:

- Which low-cost sensing technology provides the best foundation for adaptive compensation.
- Which compensation strategy offers the best balance between computational complexity and measurement improvement.
- Whether statistical, rule-based, adaptive filtering, lightweight machine learning, or hybrid approaches are most appropriate.
- How environmental variation should be represented during prototype validation.
- Whether the complete prototype can be achieved within the available budget and semester timeline.

---

## Fixed Design Principles

The following principles were approved during the Engineering Design Review and shall remain unchanged in later phases:

- Maintain affordability as the primary objective.
- Improve measurement reliability rather than replacing premium sensing technologies.
- Perform compensation locally on embedded hardware.
- Focus on practical irrigation support rather than laboratory-grade precision.
- Produce stable, repeatable and interpretable moisture estimates.
- Ensure suitability for resource-constrained agricultural environments.

---

## Minimum Demonstrable Success

Demonstrate that a low-cost embedded prototype can detect and compensate for controlled sensor drift or environmental influences, producing more stable and repeatable soil moisture estimates than an uncompensated low-cost sensor under equivalent test conditions.

---

## Phase 3B Evaluation Objectives

Phase 3B shall evaluate whether the engineering hypothesis can realistically be implemented by:

- Three technically capable Computer Science / Cybersecurity students.
- A prototype budget of ₹3000–₹5000.
- Approximately two months of development.

The feasibility study shall focus on identifying an embedded compensation approach that significantly improves the reliability of inexpensive soil moisture sensing while remaining practical for educational implementation.

---

## Review Board Decision

✅ Approved to proceed to Phase 3B Engineering Feasibility Analysis.

The review concluded that TrueMoist possesses a clearly defined engineering objective, a focused and measurable engineering hypothesis, and an achievable prototype scope suitable for academic development. The concept is distinguished by its emphasis on improving the trustworthiness of inexpensive sensing technologies rather than attempting to replace premium agricultural instrumentation.

---

## Review Notes

The Engineering Design Review concluded that the defining characteristic of TrueMoist is not soil moisture measurement itself, but the intelligent enhancement of low-cost sensor reliability through adaptive embedded compensation.

Future phases should therefore prioritize engineering approaches that improve measurement trustworthiness while preserving affordability, rather than pursuing maximum sensing accuracy or competing directly with commercial high-end agricultural systems.

# Concept 4 — TrustLatch

## Review Status

✅ Approved for Phase 3B Evaluation

---

## Original Vision

Develop an affordable embedded hardware trust establishment system capable of verifying firmware integrity before system execution, improving the security of low-cost embedded and IoT devices that lack built-in hardware trust mechanisms.

---

## Engineering Identity

TrustLatch is an embedded hardware trust establishment system designed to provide affordable firmware integrity verification for resource-constrained embedded devices.

Rather than attempting to implement enterprise-grade embedded security platforms, the concept focuses on establishing a trustworthy execution environment before application firmware begins running. The project aims to demonstrate that meaningful hardware-based trust can be achieved using inexpensive embedded hardware suitable for educational, research, and low-cost IoT deployments.

---

## Mission

Provide affordable trust establishment for resource-constrained embedded systems by verifying firmware integrity before normal system operation begins.

---

## Engineering Hypothesis

A low-cost embedded trust anchor can verify firmware integrity and establish device trust before firmware execution, providing meaningful hardware-based trust without requiring expensive dedicated security hardware.

---

## Engineering Foundation

The concept builds upon mature engineering domains including:

- Hardware Root-of-Trust
- Secure Boot
- Firmware Integrity Verification
- Embedded Systems Security
- Cryptographic Hashing
- Embedded Authentication
- Trusted Computing Principles

Phase 3A established that while hardware root-of-trust technologies are well developed, affordable implementations for low-cost embedded systems remain an active engineering opportunity.

---

## Phase 3A Validation

Phase 3A confirmed that:

- Many low-cost embedded and IoT devices lack secure boot mechanisms.
- Firmware authenticity is often assumed rather than verified.
- Hardware-based trust establishment significantly improves embedded system security.
- Existing commercial solutions frequently depend on dedicated secure hardware that increases system cost.
- Affordable embedded trust mechanisms remain relevant for educational, industrial, and IoT applications.

---

## Invalidated Assumptions

No major assumptions from Phase 1C were invalidated.

However, Phase 3A refined the concept by demonstrating that the primary innovation is not secure boot itself, but establishing an affordable hardware root-of-trust suitable for resource-constrained systems.

This clarified the engineering scope and strengthened the concept's identity.

---

## Major Engineering Risks

The primary engineering risks identified include:

- Establishing a trustworthy verification chain.
- Secure storage of integrity reference values.
- Preventing bypass of the verification mechanism.
- Selecting cryptographic methods suitable for constrained hardware.
- Balancing security strength with implementation complexity.

---

## Open Questions

Phase 3B should determine:

- Which trust establishment architecture is most appropriate for the intended prototype.
- Which firmware integrity verification technique offers the best balance between security and computational cost.
- How cryptographic material should be securely managed.
- Whether the complete prototype can be implemented within the project budget and semester timeline.
- Which attack scenarios should be demonstrated during validation.

---

## Fixed Design Principles

The following principles were approved during the Engineering Design Review and shall remain unchanged in later phases:

- Maintain affordability as the primary objective.
- Establish trust before firmware execution.
- Verify firmware integrity locally on embedded hardware.
- Focus on trust establishment rather than comprehensive embedded security.
- Demonstrate practical protection against firmware tampering.
- Remain suitable for resource-constrained embedded devices.

---

## Minimum Demonstrable Success

Demonstrate that a low-cost embedded prototype can verify the integrity of authentic firmware prior to execution, successfully permit trusted firmware to boot, detect intentionally modified firmware, and prevent normal execution or generate an appropriate security alert.

---

## Phase 3B Evaluation Objectives

Phase 3B shall evaluate whether the engineering hypothesis can realistically be implemented by:

- Three technically capable Computer Science / Cybersecurity students.
- A prototype budget of ₹3000–₹5000.
- Approximately two months of development.

The feasibility study shall identify an embedded trust establishment approach that provides meaningful firmware integrity verification while remaining practical for educational implementation.

---

## Review Board Decision

✅ Approved to proceed to Phase 3B Engineering Feasibility Analysis.

The review concluded that TrustLatch possesses a clearly defined engineering objective, a focused and measurable engineering hypothesis, and a prototype scope well suited for academic development. The concept distinguishes itself through its emphasis on affordable hardware trust establishment rather than attempting to replicate enterprise-grade embedded security platforms.

---

## Review Notes

The Engineering Design Review determined that the defining characteristic of TrustLatch is the establishment of trust before firmware execution rather than the implementation of comprehensive embedded security features.

Future phases should therefore prioritize engineering approaches that reliably establish firmware trust while maintaining affordability, implementation simplicity, and suitability for resource-constrained embedded systems.


# Concept 5 — ColdTrace

## Review Status

✅ Approved for Phase 3B Evaluation

---

## Original Vision

Develop an affordable embedded cold-chain monitoring system capable of improving the assessment of pharmaceutical and temperature-sensitive product integrity by combining multiple environmental indicators rather than relying solely on temperature threshold monitoring.

The objective is to reduce false alarms while providing more meaningful assessments of transport conditions for resource-constrained logistics environments.

---

## Engineering Identity

ColdTrace is an embedded context-aware cold-chain integrity assessment system designed to improve the reliability of transport condition evaluation through intelligent interpretation of multiple environmental indicators.

Rather than functioning as a conventional temperature logger, the system seeks to combine temperature measurements with additional transport context to distinguish harmless environmental events from conditions that present meaningful product integrity risks.

---

## Mission

Improve confidence in cold-chain integrity by intelligently distinguishing meaningful product risk from benign transport events through affordable embedded multi-sensor analysis.

---

## Engineering Hypothesis

A low-cost embedded multi-sensor system can combine temperature measurements with transport-related context to distinguish genuine cold-chain integrity risks from transient environmental events, producing more meaningful integrity assessments than conventional temperature-only monitoring.

---

## Engineering Foundation

The concept builds upon mature engineering domains including:

- Cold-chain monitoring
- Embedded environmental sensing
- Pharmaceutical logistics
- Multi-sensor data fusion
- Edge intelligence
- Transport condition monitoring
- Embedded decision support systems

Phase 3A established that while temperature logging technologies are mature, opportunities remain in improving interpretation of transport events through contextual embedded analysis.

---

## Phase 3A Validation

Phase 3A confirmed that:

- Conventional temperature loggers frequently rely on simple threshold-based alarms.
- Short-term environmental disturbances can generate false alarms despite products remaining within acceptable transport conditions.
- Temperature alone often provides insufficient context for assessing transport integrity.
- Combining multiple environmental indicators offers potential improvements in decision quality.
- Affordable embedded intelligence represents a promising direction for improving cold-chain monitoring without requiring expensive commercial logistics platforms.

---

## Invalidated Assumptions

No major assumptions from Phase 1C were invalidated.

However, Phase 3A refined the concept by demonstrating that the innovation is not temperature monitoring itself, but intelligent interpretation of multiple transport conditions to improve cold-chain integrity assessment.

This significantly clarified the engineering direction of the project.

---

## Major Engineering Risks

The primary engineering risks identified include:

- Correctly distinguishing genuine cold-chain failures from transient environmental events.
- Developing reliable decision logic from multiple sensor inputs.
- Selecting appropriate sensing modalities while maintaining affordability.
- Preventing excessive false positives or false negatives.
- Maintaining repeatable decision-making under varying transport conditions.

---

## Open Questions

Phase 3B should determine:

- Which combination of environmental indicators provides the greatest improvement in integrity assessment.
- Which embedded decision-making approach best balances accuracy, computational complexity and affordability.
- Whether rule-based reasoning, statistical methods, lightweight machine learning or hybrid approaches are most appropriate.
- How representative transport scenarios should be simulated during prototype validation.
- Whether the complete prototype can be implemented within the available budget and semester timeline.

---

## Fixed Design Principles

The following principles were approved during the Engineering Design Review and shall remain unchanged in later phases:

- Maintain affordability as the primary design objective.
- Evaluate product integrity using multiple sources of environmental evidence rather than temperature alone.
- Perform assessment locally on embedded hardware.
- Focus on reducing unnecessary alarms while maintaining reliable detection of genuine transport risks.
- Generate interpretable integrity assessments suitable for practical logistics environments.
- Ensure the solution remains appropriate for educational prototypes and resource-constrained deployments.

---

## Minimum Demonstrable Success

Demonstrate that a low-cost embedded prototype can correctly distinguish between a controlled transient transport event (such as a brief door opening resulting in a temporary temperature increase) and a simulated harmful cold-chain excursion by combining multiple environmental indicators, generating appropriate integrity assessments for each scenario.

---

## Phase 3B Evaluation Objectives

Phase 3B shall evaluate whether the engineering hypothesis can realistically be implemented by:

- Three technically capable Computer Science / Cybersecurity students.
- A prototype budget of ₹3000–₹5000.
- Approximately two months of development.

The feasibility study shall identify an embedded multi-sensor integrity assessment approach that provides meaningful improvements over conventional temperature-only monitoring while remaining practical for educational implementation.

---

## Review Board Decision

✅ Approved to proceed to Phase 3B Engineering Feasibility Analysis.

The review concluded that ColdTrace possesses a clearly defined engineering objective, a focused and measurable engineering hypothesis, and a practical prototype scope suitable for academic development. The concept distinguishes itself through its emphasis on intelligent contextual integrity assessment rather than conventional environmental data logging.

---

## Review Notes

The Engineering Design Review determined that the defining characteristic of ColdTrace is the intelligent interpretation of multiple environmental indicators to improve cold-chain integrity assessment rather than the collection of temperature data alone.

Future phases should therefore prioritize engineering approaches that improve decision quality through contextual embedded analysis while maintaining affordability, implementation simplicity and suitability for resource-constrained logistics environments.


Engineering Design Review Conclusion

Following completion of the Engineering Design Review, all five shortlisted concepts were determined to possess:

clearly defined engineering identities,
measurable engineering hypotheses,
realistic prototype objectives,
fixed design principles,
and sufficient technical maturity to proceed to Phase 3B.

No concepts were eliminated during this review.

The Engineering Review Board concluded that eliminating concepts at this stage would be premature because feasibility, implementation complexity, hardware availability, development effort, and prototype cost have not yet been objectively evaluated.

The next phase (Phase 3B) will therefore focus exclusively on determining whether each engineering hypothesis can realistically be implemented within the project's resource constraints.

A formal portfolio down-selection will occur only after sufficient engineering evidence has been gathered during Phase 3B and Phase 3C.


---

## Source 2: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/01_Comparison_Protocol.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `9711020de0cc5108fb7e4a779e06fdba8e640a2100c098791d1a6b7ead410d7d`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/01_Comparison_Protocol.md`
- Current SHA-256: `9711020de0cc5108fb7e4a779e06fdba8e640a2100c098791d1a6b7ead410d7d`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Final Comparison Protocol

## Scope and decision boundary

This protocol applies only to OpenBraille, VibeGuard, and TrueMoist. This extraction pass records evidence without selecting, scoring, ranking, recommending, eliminating, or declaring a winner. Patent-development potential is the primary priority, while buildability, budget, validation, timeline, team fit, and demonstration quality remain mandatory constraints. Patent scoring must wait for the separate current patent-source verification pass.

## Hard gates

Evaluate every concept against:

- **G1 — Budget:** maximum prototype budget of ₹5,000.
- **G2 — Timeline:** credible completion within approximately two months.
- **G3 — Team:** executable by the five-member team.
- **G4 — Demonstrable success:** clear and measurable minimum demonstrable success.
- **G5 — Access:** required components, fabrication, facilities, and validation resources are realistically accessible.
- **G6 — Patent-development path:** a credible path exists that could be supported by prototype experiments.
- **G7 — Fatal dependency:** no unresolved dependency creates a fatal implementation or validation risk.

Allowed statuses only: **Pass**, **Provisional Pass**, **Fail**, or **Insufficient Evidence**.

A gate record must include status, evidence, confidence, unresolved dependency, earliest resolving action, time, cost, and consequence of failure. During evidence extraction, a gate result must not eliminate a concept.

## Weighted rubric (100 points)

| Category / criterion | Weight |
|---|---:|
| **A. Patent-development potential** | **35** |
| A1. Specific claimable technical contribution | 15 |
| A2. Plausible white-space position | 8 |
| A3. Ability to generate experimental patent-supporting evidence | 7 |
| A4. Prior-art/FTO risk | 5 |
| **B. Two-month buildability** | **20** |
| B1. Architecture and integration complexity | 8 |
| B2. Schedule realism | 6 |
| B3. Critical implementation risk | 6 |
| **C. Validation strength** | **15** |
| C1. Availability of credible ground truth | 6 |
| C2. Repeatability and experimental control | 5 |
| C3. Clarity of success metrics | 4 |
| **D. Team fit** | **10** |
| **E. Demonstration quality** | **8** |
| **F. Budget and procurement certainty** | **7** |
| **G. Commercial or social significance** | **5** |
| **Total** | **100** |

## Scoring rules for the later decision pass

Use only:

- 1 = very weak
- 2 = weak
- 3 = credible but uncertain
- 4 = strong
- 5 = exceptional

For A4 — Prior-art/FTO risk:

- 5 means comparatively low or manageable blocking risk.
- 1 means severe, uncertain, or likely blocking risk.
- The patent report must separately record novelty/obviousness risk, patent-eligibility risk, and FTO/infringement risk before assigning the combined A4 score.

Weighted contribution:

```text
(score / 5) × criterion weight
```

Every future score must state:

- score;
- confidence level;
- supporting evidence;
- uncertainty;
- earliest resolving experiment or research action;
- patent-research verification status where patent-related.

Complexity is not inherently valuable. Social value is not patent novelty. Demonstration polish is not proof of novelty. A component list is not proof of system feasibility. Patent potential is not established patentability.

## Required later outputs

After current patent verification and scoring, produce:

- patent-first ranking;
- buildability ranking;
- validation ranking;
- demonstration ranking;
- balanced overall ranking.

The future final report must select exactly:

- one primary project;
- one runner-up;
- one reserve.

No score or ranking is populated in this package.


---

## Source 3: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `f2d6f77836230780b63ae10353d9bf65f61d43ef2500e0872b5e9a65e57835c6`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/02_Authoritative_Source_Manifest.md`
- Current SHA-256: `f2d6f77836230780b63ae10353d9bf65f61d43ef2500e0872b5e9a65e57835c6`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Authoritative Source Manifest

## Authority levels

Levels follow the owner-specified precedence. “Used” means used for governance, technical extraction, conflict identification, or a lower-level patent-history gap. Final Phase 3C reports supersede earlier implementation assumptions, but the EDR remains authoritative for identity and hypothesis and Decision Register v1.2 remains authoritative for accepted decisions.

| Exact path | Level | Concept | Role | Status | Criteria supported | Limitations / supersession |
|---|---:|---|---|---|---|---|
| `README.md` | Governance context | Portfolio | Repository status and canonical links | Current | Candidate scope, phase status | Not a technical evidence source; substantive matters governed by listed authorities. |
| `AGENTS.md` | Governance context | Portfolio | Repository policy, authority order, special cases | Current | Source handling and exclusions | Not concept evidence. |
| `PHASE 3/Engineering_Design_Review.md` | 1 | All three | Canonical identity, hypothesis, fixed principles, MDS, project constraints | Current | G2–G4; team fit; significance; validation objective | Predates Phase 3C component selection; does not freeze architecture. |
| `Project_mC_Decision_Register_v1.2.md` | 2 | All three / portfolio | Accepted requirements and PDR decisions | Current, authoritative register | Budget, team, architecture, validation, IP pivots, readiness | Some “verified” component decisions remain physically unvalidated; PDR-021 explicitly corrects the SG90 reset claim. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md` | 3 | Portfolio | Retained shortlist, priorities, next action | Current, approved | Candidate scope, patent-first priority, constraints | High-level only; no detailed architecture evidence. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md` | 4 | OpenBraille | Frozen Phase 3C architecture, BOM, validation, risk, readiness | Current final | G1–G7; build, validation, demo, team, patent experiment surface | Superseded by PDR-021 where it states an SG90 integrated torsion spring provides passive reset; some exact mechanical/current claims remain untested. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md` | 4 | VibeGuard | Frozen Phase 3C architecture, cost, DSP, validation, risk, innovation discussion | Current final | G1–G7; build, validation, demo, team, patent experiment surface | Dense-machine attribution and spectral-subtraction adequacy remain empirical; report surfaced a 5-vs-6 roster inconsistency later resolved by PDR-038. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md` | 4 | TrueMoist | Frozen architecture, BOM, factorial validation, gates, patent implications | Current final | G1–G7; build, validation, demo, team, patent experiment surface | Procurement estimates need refresh; institutional oven/scale access and physical gates are pending. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md` | 5 | OpenBraille | Concise decision and risk memory | Current final memory | Architecture, BOM, risks, team tasks | Architecture report prevails; repeats passive-reset claim superseded/qualified by PDR-021. It also describes a team allocation that can be read as six roles. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md` | 5 | VibeGuard | Concise architecture and unresolved-question memory | Current final memory | Sensor, pipeline, costs, team, risks | Architecture report and PDR decisions prevail; its ADXL345 bandwidth wording must be read as MVP-limited. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md` | 5 | TrueMoist | Concise frozen architecture, gates, fallback hierarchy | Current final memory | Architecture, dataset, thresholds, facilities, readiness | Architecture report prevails. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_SOP_Final.md` | 6 | OpenBraille | Phase procedure and architecture criteria | Current Phase 3C SOP | Process, constraints, success framing | Pre-selection process document; final report/register supersede implementation choices. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_SOP_Final.md` | 6 | VibeGuard | Canonical Phase 3C mission/MDS and investigation requirements | Current Phase 3C SOP | MDS, budget, validation, innovation preservation | Team categories sum to six despite “five-member”; PDR-038 resolves roster as five. |
| `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP_Final.md` | 6 | TrueMoist | Canonical Phase 3C identity/MDS, frozen constraints, evidence rules | Current Phase 3C SOP | MDS, validation, patent boundary, team | Header predates frozen decisions; final report/register supersede architecture options. Its internal source order placing the register last is superseded by repository governance. |
| `PHASE 2/Phase2_Report by CLaude.md` | 9 | All three | Historical consolidated patent landscape | Historical evidence, used only for patent-history gap | Named prior art, saturation, IP pivots, search questions | Not current patent verification, not legal advice/FTO; Phase 3C and register supersede old concept scope and recommendations. Its historical ranking is excluded from present comparison. |

## Explicitly excluded or non-authoritative

The following were not treated as current technical authority:

- `COPY PASTE FOLDER/`, `every sop and memory/`, `contexts.zip`, all phase ZIPs, and ZIP members — convenience/context packages.
- `Project_mC_Decision_Register_v1.0_HISTORICAL.md` and other historical registers — traceability only; v1.2 controls.
- Raw independent Gemini, Mistral, Perplexity, Qwen, Kimi, and ChatGPT research — evidence already synthesized where appropriate; it cannot override authoritative documents.
- The failed, mis-scoped ChatGPT OpenBraille Phase 3C research output — failed research preserved for methodology traceability, not OpenBraille evidence.
- Raw VibeGuard research under `VibeGuard/research/` — non-authoritative relative to the final architecture report.
- Repository audit, reorganization, validation, and cleanup files — repository history, not current technical evidence.
- Phase 2’s historical composite ranking and old recommendations — excluded because the task prohibits present ranking and later Phase 3C decisions supersede scope.

## Lower-phase consultation

Phase 3B, Phase 3A, and Phase 1C were not needed for unresolved architecture facts because the final Phase 3C packages and Decision Register covered them. Phase 2 was consulted only to prepare the later patent-search input pack; its claims remain historical and require current primary-source verification.


---

## Source 4: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/03_Concept_Evidence_Matrix.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/03_Concept_Evidence_Matrix.md`
- Current SHA-256: `8f999b878cfc7f863227682f141a278a4dfa4ee7705e49e1d55ef147c27a1975`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Concept Evidence Matrix

## Reading rules and source keys

This is a neutral extraction, not an evaluation. Each cell gives the evidence, then `[source; location; confidence; conflict]`. “None noted” means no disagreement was found in the authoritative set; it does not prove the claim experimentally.

- **EDR:** `PHASE 3/Engineering_Design_Review.md`
- **PDR:** `Project_mC_Decision_Register_v1.2.md`
- **OB-R:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`
- **OB-M:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md`
- **VG-R:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`
- **VG-M:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md`
- **TM-R:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md`
- **TM-M:** `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md`
- **P2:** `PHASE 2/Phase2_Report by CLaude.md`

| Evidence row | OpenBraille | VibeGuard | TrueMoist |
|---|---|---|---|
| Engineering identity | Affordable refreshable-Braille assistive embedded system exploring low-cost actuation, not a high-end-display competitor. `[EDR; Concept 1 / Engineering Identity; High; none noted]` | Passive, single-node edge condition-monitoring system interpreting vibration locally, not merely sensing it. `[EDR; Concept 2 / Engineering Identity; High; Phase 3B mis-scoped cancellation research is excluded]` | Embedded intelligent sensing that improves trustworthiness of inexpensive soil-moisture measurement through local compensation. `[EDR; Concept 3 / Engineering Identity; High; Phase 3C narrows universal/adaptive language to controlled MVP]` |
| Engineering hypothesis | A lower-cost actuation strategy can replace piezoelectric actuation while retaining acceptable tactile performance. `[EDR; Concept 1 / Engineering Hypothesis; High; none noted]` | Low-cost local analysis can reliably distinguish normal from early abnormal machine behaviour on constrained hardware. `[EDR; Concept 2 / Engineering Hypothesis; High; MVP narrows “early” to deliberately introduced abnormal vibration]` | Environmental information and calibration data can compensate predictable error and improve closeness/stability versus uncompensated output under controlled conditions. `[TM-R; §2.2; High; refines EDR’s broader drift/adaptive formulation]` |
| Minimum demonstrable success | One refreshable cell with tactilely distinguishable, repeatable low-cost output. `[EDR; Concept 1 / Minimum Demonstrable Success; High; Phase 3C adds quantitative tests]` | Sense a rig, establish normal, detect deliberate abnormal condition, classify Normal/Abnormal locally, and show clear output. `[VG-R; Task 1 and VG SOP §2 MDS as incorporated; High; dense-floor attribution is beyond bench MDS]` | Acquire raw moisture and temperature, represent salinity treatment, compute raw and compensated estimates locally, compare both to gravimetric truth, and improve on held-out samples. `[TM-R; §2.3; High; more specific than EDR]` |
| Frozen Phase 3C architecture | One 6-dot, ~300%-scale servo/cam cell; direct PWM; FDM frame. `[OB-R; Final Architecture / Architecture Overview; High; reset mechanism is qualified by PDR-021]` | Rigid ADXL345→SPI→ESP32; tiered DSP; threshold then Mahalanobis target; RGB LED; eccentric-mass rig. `[VG-R; §13; High; noise isolation remains unvalidated]` | D-dominant/B-hardened: capacitive probe + DS18B20 + ADS1115 + ESP32, controlled salinity, offline regression, local inference, CSV, gravimetric validation. `[PDR; PDR-058; High; mandatory early gates remain]` |
| MCU | ESP32-WROOM-32 DevKit. `[PDR; PDR-017; High; none noted]` | ESP32 WROOM-32 or S3-class. `[PDR; PDR-025; High; none noted]` | ESP32-WROOM-32 DevKit; ESP32-S3 fallback. `[TM-R; §§12.1–12.2; High; none noted]` |
| Primary sensor or actuator | Six SG90-class micro servos driving eccentric cams and pins. `[OB-R; Hardware Architecture; High; SG90 passive-return detail unvalidated]` | ADXL345, 3-axis digital MEMS, SPI, 3,200 Hz max ODR / 1,600 Hz stated Nyquist bandwidth. `[VG-M; Selected Architecture / Sensor; High; IIS3DWB is future upgrade, not MVP]` | Two genuine analog capacitive probes (one final, one spare/characterization) plus waterproof DS18B20. `[TM-R; §§8–9; High; exact procured variant remains Phase 4]` |
| Power architecture | External 5 V/2 A adapter and 1,000 µF servo-rail capacitor; avoid USB bus power. `[PDR; PDR-020; High; adequacy for six-servo peaks is not empirically proven]` | Shared 3.3 V sensor/logic rail; 0.1 µF sensor decoupling; low-voltage motor rig separately supplied as needed. `[VG-M; Selected Architecture / Electrical interface and Test rig; Medium; report gives less explicit whole-system power budget]` | USB 5 V to dev board; design for 5 V/1 A; 3.3 V ADS1115/DS18B20; no battery. `[TM-R; §20; High; exact probe supply depends on selected probe]` |
| Fabrication requirements | In-house FDM: ABS frame, PETG/Nylon cams, stainless pins; optional laser-cut acrylic guide fallback. `[PDR; PDR-019 and OB-R ADR-005; High; actual tolerances untested]` | Heavy damped motor/fan base, rigid bonded/bolted sensor bracket, final soldered perfboard. `[VG-R; §§8,10,13; High; mount repeatability untested]` | 500–1000 mL containers, repeatability/packing jig, soldered perfboard, sample-preparation apparatus. `[TM-R; §§17,11.4; High; physical workflow not yet exercised]` |
| Software complexity | Event-driven serial commands, six PWM channels, lookup table, calibration storage, self-test. `[OB-R; Embedded Software Architecture; High; some timeout/settle assumptions unverified]` | Interrupt/DMA SPI acquisition, feature extraction, 256–1,024 FFT, calibration, threshold/Mahalanobis, spectral subtraction, logging/LED. `[VG-R; §§6–7,13; High; exact thresholds empirical]` | Sensor drivers, filtering, CSV, offline Python modeling, coefficient export, fixed polynomial inference, quality flags. `[TM-R; §§12–14; High; dataset operations dominate compute]` |
| Algorithm or control approach | Unicode/Braille lookup → target angles → direct 50 Hz PWM; actuate changed dots. `[OB-R; Embedded Software Architecture; High; active cam retraction may be the real reset behavior]` | DC removal → Hann → RMS/peak/other features → triggered FFT; RMS persistence baseline, Mahalanobis primary target; spectral subtraction. `[PDR; PDR-026, PDR-027, PDR-054; High; isolation adequacy pending]` | Raw univariate baseline, multivariate linear baseline, ridge second-order candidate; offline training/fixed MCU coefficients. `[PDR; PDR-031; High; final model depends on held-out result]` |
| Expected BOM range | ₹2,060–₹2,850. `[OB-R; Hardware Architecture / Total estimated BOM; High; procurement estimate, not invoices]` | ₹1,700–₹2,200 ADXL345 MVP; ~₹4,000 IIS3DWB upgrade. `[VG-R; §13; High; upgrade is not MVP]` | ₹1,790–₹3,440 with institutional oven/scale conditions; below ₹5,000 with purchased scale/contingency. `[TM-R; §22; High; institutional equipment assumption is material]` |
| Critical procurement concerns | Six consistent SG90-class servos, suitable FDM materials/printer, 5 V supply; exact variants deferred. `[OB-R; Hardware Architecture and Implementation Readiness; Medium; no current supplier verification]` | ADXL345 authenticity/availability, ESP32, motor/fan and rigid mount; order sensor/MCU early. `[VG-R; §§4,10; Medium; no current procurement pass]` | Genuine analog probes (two), ADS1115 authenticity/stability, scale access/purchase, containers/consumables. `[TM-R; §§8,22,26; High; prices must be refreshed]` |
| Facilities / institutional resources | In-house FDM printer, calipers, multimeter; optional oscilloscope; ideally visually impaired tactile participant and optional faculty/lab mechanical advice. `[OB-R; Implementation Readiness and M6; High; participant/consultation access not confirmed]` | Basic electronics tools, soldering, mechanical base/bracket tools; later real dense-machine floor required for spatial-attribution validation. `[VG-R; §§8,13 and PDR PDR-013; Medium; field access not confirmed]` | Institutional 105 ± 5 °C oven, preferably 0.01 g scale, soil prep/storage space and controlled temperature handling. `[TM-R; §§16,22,26 Gate C; High; access not confirmed]` |
| Critical mechanical risk | Pin/cam friction, tolerance stack-up, cam wear, torque, tactile height; macro scale reduces but does not prove performance. `[OB-R; Remaining Engineering Risks and M3–M6; High; report’s “resolved” wording is stronger than unbuilt evidence]` | Rigid coupling and repeatable eccentric-mass rig; loose mounts filter signals. `[PDR; PDR-028, PDR-030; High; physical repeatability pending]` | Reinsertion, packing density, probe placement, temperature gradients and sample consistency. `[TM-R; §§17,24,26; High; mandatory gates pending]` |
| Critical electrical risk | Brownout/current peaks with six servos; 5 V/2 A + capacitor proposed. `[OB-R; Electrical Architecture / Remaining Risks; High; simultaneous-current adequacy untested]` | SPI integrity above ~2 MHz on jumpers; sensor decoupling and perfboard required. `[VG-M; Major Engineering Risks; High; actual bus margin untested]` | ADC-path noise/nonlinearity, grounding, counterfeit/unstable ADS1115, wet connectors. `[TM-R; §§11,24; High; Week-1 comparison pending]` |
| Critical software risk | Mapping/calibration errors and command/state faults; software is not dominant risk. `[OB-R; Remaining Engineering Risks; Medium; no code exists]` | Sampling jitter, compute/memory, false alarms, threshold tuning, spectral subtraction. `[VG-R; §§6–7,10; High; classifier performance untested]` | Leakage/overfit, model-subset degradation, Python/MCU mismatch, invalid-range handling. `[TM-R; §§14–15,18,25; High; data not collected]` |
| Integration risk | Six mechanical modules plus power and PWM; single-dot-first sequence isolates failures. `[PDR; PDR-022; High; full-cell interference untested]` | Coupling + acquisition + DSP + fault rig + background noise interact; controlled rig precedes field attribution. `[VG-R; §§3c,8,13; High; dense environment remains unresolved]` | Measurement chain depends on probe, jig, reference, treatment, ADC, model and 72-run schedule. `[PDR; PDR-061; High; component list alone is insufficient]` |
| Proposed validation method | M1–M8 bottom-up: single dot, six dots, 100 cycles, tactile test, character set, end-to-end. `[OB-R; Prototype Validation Strategy; High; participant protocol details unavailable]` | Normal baseline versus eccentric-mass abnormal condition on damped motor/fan rig; repeat trials, secondary loose-mount condition, then dense-machine field validation for attribution. `[PDR; PDR-030 and PDR-013; High; exact quantitative acceptance protocol unavailable]` | 72 independent factorial runs, held-out physical replicate, gravimetric GWC, raw-vs-compensated RMSE/MAE and subset analysis. `[PDR; PDR-048, PDR-059, PDR-060; High; timing pilot pending]` |
| Ground-truth quality | Human tactile distinction plus caliper/cycle measurements; “ideally” visually impaired reader. `[OB-R; M5–M8; Medium; tactile ground-truth protocol/sample size not specified]` | Injected eccentric mass gives known condition label, but not actual incipient industrial fault or source attribution truth. `[VG-R; §2 Consensus and §13; Medium; bench labels are credible only for MVP condition classification]` | Dry-basis gravimetric GWC at 105 ± 5 °C until constant mass; 0.01 g preferred. `[PDR; PDR-048; High if access/procedure confirmed; access pending]` |
| Quantitative success threshold | ≤0.1 mm position variance over 100 cycles; ≥1,000 actuations without failure; tactile distinction; BOM ≤₹5,000. `[OB-R; Prototype Validation Strategy / Acceptance criteria; High; user-test success rate not quantified]` | Normal/Abnormal local classification and clear output are specified, but no authoritative minimum accuracy/false-alarm/repeatability number was found. `[VG SOP as quoted in VG-R Task 1 and VG-R §13; High for absence; conflict: “reliably” lacks threshold]` | Held-out RMSE ≥20% lower and MAE ≥15% lower than raw; no major subset MAE worsened >10%. `[PDR; PDR-060 and TM-R §18; High; pending validation]` |
| Expected demonstration | Host character produces refreshable tactile macro-scale one-cell Braille patterns. `[OB-R; M7–M8; High; tactile legibility pending]` | Live motor/fan changes from green Normal to red Abnormal under eccentric mass, using local processing; calibration blue. `[PDR; PDR-029, PDR-030; High; reliability threshold absent]` | Held-out sequence shows reference, raw and compensated estimates, temperature, salinity code, and absolute errors. `[TM-R; §18.4; High; depends on gravimetric results]` |
| Team-skill fit | Firmware/electrical fit strong; mechanical CAD/fabrication is growth area and dominant effort. `[OB-R; Student Team Guidance; High; report’s role count wording conflicts with authoritative five-person roster]` | Strong fit for CS/embedded/DSP; no professional vibration/mechanical expertise assumed; hardware member handles rig. `[VG-R; §11 and PDR PDR-038; High; SOP role arithmetic conflict resolved by PDR]` | Members 1–3 own embedded, model, hardware/validation; learner and presenter support noncritical work. `[TM-R; §29; High; matches PDR-038]` |
| Beginner-member task | Unicode-to-Braille lookup and self-test/diagnostic unit tests. `[OB-R; Student Team Guidance; High; none noted]` | LED/output mapping, calibration state machine, serial logging. `[VG-R; §11; High; none noted]` | Batch labels, CSV checks, temperature logging, test scripts, LEDs, supervised sample prep. `[TM-R; §29 Member 4; High; none noted]` |
| Known patent target | Phase 2 pivot: manufacturing/fabrication method and firmware control rather than actuator mechanism. `[PDR; PDR-009; High as project direction; not patentability]` | Narrow possible target: adaptive single-node noise isolation / in-situ baseline + band-limited spectral subtraction + multivariate statistics. `[VG-R; §12 and P2 §2.2; Medium; current MVP is largely conventional and target unverified]` | Validated compensation workflow, drift/confidence logic, constrained deployment, calibration methodology; not custom probe hardware. `[PDR; PDR-045 and TM-R §28; High as direction; not patentability]` |
| Known prior-art saturation | Actuation mechanism Moderate–High historically; Dot Incorporation named dominant fence. `[P2; §2.1 Patent Saturation / Major Patent Holders; Medium; historical AI synthesis needs current primary-source verification]` | Broad PdM/single-node concept historically High; narrower adaptive niche described as Moderate/unproven; US 7,421,349, Tractian, Infinite Uptime named. `[P2; §2.2; Medium; contested historical synthesis, no current verification]` | Hardware compensation High historically; Campbell, METER, Toro and US 11,598,743 named. `[P2; §2.3; Medium; current status/claims unverified]` |
| Known IP pivot | Away from physical actuation novelty toward manufacturing and firmware. `[PDR; PDR-009; High; current servo/cam’s connection to pivot is unresolved]` | Away from generic monitor/SME economics toward a specific experimentally superior adaptive attribution method, if one exists. `[P2; §2.2; Medium; Phase 3C MVP uses threshold/statistics, not demonstrated adaptive novelty]` | Commodity hardware MVP; future specific recalibration, drift detection, confidence gating, transfer calibration, or controlled error-separation workflow. `[PDR; PDR-045 and TM-R §28.3; High as research directions]` |
| Prototype-generated patent evidence | Force/travel, tactile outcome, repeatability, wear, power, geometry/process and control data could support a later specific technical contribution. `[OB-R; M3–M8 and ADRs; Medium; report does not connect servo/cam tests to a defined claim]` | Noise rejection, attribution, false-alarm, repeatability and comparison against conventional thresholds could support a specific method only if differentiated. `[VG-R; §§3c,12–13; Medium; no comparison protocol against named prior art]` | Controlled raw-vs-compensated errors, packing/temp/salinity separation, confidence/range flags and transfer/drift experiments could support later method development. `[TM-R; §§18,28; High for evidence generation; claimability unverified]` |
| Known unresolved technical assumptions | Passive return versus active retraction; 5 V/2 A peak adequacy; friction/tolerance; tactile height; torque/wear. `[PDR; PDR-021 and OB-R Remaining Engineering Risks; High; direct conflict on reset]` | ADXL345 scope, rigid-mount repeatability, spectral subtraction, eccentric-mass repeatability, thresholds, dense-machine attribution. `[VG-R; §§3,10,13; High; bench/field scope distinction material]` | ADC value, probe/reinsertion/packing, oven/scale, salinity effect, 72-run timing, pilot model. `[PDR; PDR-061; High; all pending]` |
| Known unresolved patent assumptions | Whether macro servo/cam can support a meaningful claim; whether manufacturing/firmware white space remains; current Dot claims/status. `[PDR; PDR-009 and P2 §2.1; High as unresolved; current sources absent]` | Whether differentiation exceeds conventional vibration monitoring and named prior art; whether dense attribution is achieved and claim-relevant. `[P2; §2.2 and VG-R §12; High as unresolved]` | Whether static calibration/compensation workflow is more than ordinary regression/fusion; whether future adaptive variants have current white space. `[TM-R; §28.2–28.3 and P2 §2.3; High as unresolved]` |
| Phase 4 readiness status | “Ready with Minor Refinements” in architecture report. `[OB-R; Architecture Readiness Assessment; High; register reset correction creates a mandatory early check not reflected in label]` | “Ready with Minor Refinements.” `[VG-R; §13 Decision Gate; High; PDR-067 says Phase 4 has not started and final down-selection comes first]` | “Architecture Ready with Mandatory Early Validation.” `[PDR; PDR-063; High; gates explicitly pending]` |

## Cross-cutting conflict notes

1. **Phase 4 status:** concept reports sometimes say “proceed to Phase 4,” but PDR-067 and the closure memo make final comparative down-selection the next action. Therefore, architecture readiness is not authorization or evidence that Phase 4 has started.
2. **Team count:** the authoritative roster is five (PDR-038). VibeGuard’s SOP role arithmetic and parts of OpenBraille team wording can sum to six; those lower-authority inconsistencies are not used to change the roster.
3. **OpenBraille reset:** OB-R describes an “integrated servo torsion spring” as passive reset. PDR-021 explicitly marks this technically unvalidated and requires inspection; active servo-driven cam retraction is the documented correction if no usable passive return exists.
4. **TrueMoist scope:** Phase 2 discussed adaptive, multi-soil/calibration-free validation. Phase 3C freezes a one-soil, fixed-coefficient controlled MVP, so the broader scope is not carried into the MVP. PDR-012 nevertheless remains a future two-season, multi-soil validation task outside the semester MVP.


---

## Source 5: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `6ee8fb1e9570342b58cc1f4facfdce2c61cc1c71d3959dcbdf0951615c0cc02c`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/04_Hard_Gate_Precheck.md`
- Current SHA-256: `6ee8fb1e9570342b58cc1f4facfdce2c61cc1c71d3959dcbdf0951615c0cc02c`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Repository-Only Hard-Gate Precheck

## Interpretation

This is a precheck, not elimination. Statuses use only Pass, Provisional Pass, Fail, or Insufficient Evidence. Cost/time values are planning estimates for the resolving action, not invented BOM or performance claims; “₹0 if available” means use of already-owned/institutional resources. Evidence paths and sections are given in each row.

## OpenBraille

| Gate | Status | Evidence and confidence | Unresolved dependency | Earliest resolving action | Time / approximate cost | Consequence if gate fails |
|---|---|---|---|---|---|---|
| G1 Budget | **Provisional Pass** | BOM ₹2,060–₹2,850. `[OpenBraille architecture report, Hardware Architecture; High]` | Replacement servos/prints and supply suitability not procured. | Refresh quotes and buy one-servo/single-dot materials first. | 1–2 days / within listed BOM; exact current cost unavailable | Redesign BOM or concept cannot meet ceiling. |
| G2 Two months | **Provisional Pass** | M1–M8 reaches MDS by Week 4; report says ready with minor refinements. `[OpenBraille report, Prototype Validation Strategy and Readiness; Medium]` | Mechanical iteration time is unmeasured. | Fabricate and cycle one dot before six-dot build. | 2–5 days / cost included in prototype materials | Excess iteration could consume schedule. |
| G3 Team | **Provisional Pass** | Firmware/electrical align with strong members; scoped beginner task; mechanical work is growth area. `[OpenBraille report, Student Team Guidance; Medium]` | FDM/CAD capacity and mechanical mentorship/access not confirmed. | Assign five-person responsibilities and complete single-dot fabrication exercise. | 1–3 days / ₹0–material cost | Mechanical critical path may exceed team capability. |
| G4 Measurable MDS | **Provisional Pass** | The mechanical criteria are explicit: one-cell tactile output, ≤0.1 mm variance/100 cycles, and ≥1,000 cycles without failure. `[EDR OpenBraille MDS; OpenBraille report, Validation; High]` | A blinded tactile-identification protocol, participant plan, and quantitative acceptance rate must still be frozen. | Freeze the blinded tactile-identification protocol, participant plan, and quantitative acceptance rate before testing. | <1 day / ₹0 | Results may be ambiguous even if the mechanism meets its mechanical criteria. |
| G5 Access | **Provisional Pass** | Required tools: FDM printer, calipers, multimeter, 5 V supply; tactile participant ideally visually impaired. `[OpenBraille report, Implementation Readiness; Medium]` | Actual printer, material, participant, and optional lab support access unconfirmed. | Inventory/booking and participant-access check. | 1–3 days / ₹0 if available; unavailable otherwise | Fabrication or credible tactile validation may be blocked. |
| G6 Patent path | **Insufficient Evidence** | PDR-009 redirects target to manufacturing and firmware; prototype can generate geometry/control/reliability data. `[Decision Register, PDR-009; OpenBraille report M3–M8; Medium]` | No current claim chart; unclear whether macro servo/cam supports a specific nonconventional contribution. | Current primary patent search and provisional claim-element map, then define discriminating experiment. | Patent pass: duration/cost not established in repository | Patent-first priority cannot be scored defensibly. |
| G7 Fatal dependency | **Provisional Pass** | Macro-scale/single-dot-first strategy mitigates tolerance risk. `[Decision Register, PDR-016/PDR-022; Medium]` | PDR-021 reset conflict, current demand, friction, torque, tactile adequacy remain physical. | Inspect SG90, log one-dot force/travel/current, then staged six-servo power test and tactile check. | 2–5 days / one servo + measurement/fabrication materials | Failed tactile actuation or unfixable power/mechanics could invalidate MVP architecture. |

## VibeGuard

| Gate | Status | Evidence and confidence | Unresolved dependency | Earliest resolving action | Time / approximate cost | Consequence if gate fails |
|---|---|---|---|---|---|---|
| G1 Budget | **Provisional Pass** | ADXL345 MVP ₹1,700–₹2,200; IIS3DWB path ~₹4,000. `[VibeGuard architecture report, §13; High]` | Current parts/authenticity and complete rig cost not verified. | Refresh quotes for complete ADXL345 rig and contingency. | 1–2 days / within listed range; exact current cost unavailable | Substitute parts or architecture could breach ceiling. |
| G2 Two months | **Provisional Pass** | Architecture classified ready with minor refinements and uses staged threshold/DSP. `[VibeGuard report, §13; Medium]` | No authoritative detailed two-month experimental schedule or measured integration time. | Build acquisition-to-RMS vertical slice and time the workflow. | 3–5 days / prototype subset cost | DSP/mount/debug work may consume the schedule. |
| G3 Team | **Provisional Pass** | Strong CS/embedded fit; beginner can own LED/state/logging; five-person roster fixed by PDR-038. `[VibeGuard report, §11; PDR-038; High]` | No professional vibration expertise; hardware role capacity and field support unconfirmed. | Role assignment plus advisor/department access check. | <2 days / ₹0 | Mechanical/experimental errors may undermine data. |
| G4 Measurable MDS | **Provisional Pass** | Normal/Abnormal local classification and RGB output are clear. `[VibeGuard SOP §2; PDR-029/PDR-030; High]` | No minimum accuracy, false-alarm, missed-detection, or repeatability threshold is frozen. | Pre-register trial count and quantitative confusion/false-alarm acceptance criteria. | <1 day / ₹0 | “Reliable” success could be judged subjectively. |
| G5 Access | **Provisional Pass** | Low-voltage motor/fan rig and ordinary electronics/fabrication tools suffice for bench MDS. `[VibeGuard report, §13; High]` | Real dense-machine floor access is needed for the claimed spatial-attribution validation, not bench MDS. | Confirm bench resources and identify/secure later field site. | 1–7 days / ₹0 if accessible; unavailable otherwise | Bench MVP may work but patent-relevant attribution remains unverified. |
| G6 Patent path | **Insufficient Evidence** | Phase 3C names in-situ baseline + spectral subtraction + multivariate statistics as an innovation surface; Phase 2 names directly adjacent art. `[VibeGuard report §12; Phase 2 report §2.2; Medium]` | No current patent verification or evidence the proposed method exceeds conventional monitoring. | Current primary patent search/claim chart; define comparator and dense-noise experiment. | Duration/cost not established in repository | Generic monitor may not support patent-first objective. |
| G7 Fatal dependency | **Provisional Pass** | Bench classification is feasible with ADXL345 and eccentric-mass rig. `[PDR-023–030; High]` | Rigid-mount/fault repeatability and spectral subtraction; dense attribution remains a major unresolved dependency for advanced claim. | Repeat randomized normal/fault rig trials, then controlled interferer and field test. | Bench 3–7 days / within rig BOM; field time/cost unavailable | Failure may leave only conventional vibration sensing with weak attribution evidence. |

## TrueMoist

| Gate | Status | Evidence and confidence | Unresolved dependency | Earliest resolving action | Time / approximate cost | Consequence if gate fails |
|---|---|---|---|---|---|---|
| G1 Budget | **Provisional Pass** | ₹1,790–₹3,440 depending on institutional equipment; below ₹5,000 with purchased scale/contingency; oven assumed institutional. `[TrueMoist report, §22; High]` | Oven cannot be purchased within budget; current quotes/access absent. | Confirm institutional equipment and refresh full BOM. | 1–3 days / ₹0 if institutional; scale ₹400–₹700 as listed | No ground-truth facility or excessive replacement costs can breach gate. |
| G2 Two months | **Provisional Pass** | Eight-week roadmap and 72-run target; 54-run fallback. `[TrueMoist report, §§25,30; Medium]` | Pilot timing and equilibration/drying throughput unmeasured. | Time a small end-to-end factorial pilot including drying workflow. | 3–7 elapsed days / consumables within BOM | Dataset/validation may not finish; scope reduction may weaken evidence. |
| G3 Team | **Provisional Pass** | Clear five-member allocation; compute is light and roles isolate critical work. `[TrueMoist report, §29; High]` | Physical sample workload/oven logistics may exceed available labor. | Run pilot with actual role allocation and log person-hours. | 2–5 days / consumables | Experimental workload could overwhelm team despite easy firmware. |
| G4 Measurable MDS | **Pass** | Held-out RMSE ≥20% and MAE ≥15% improvement, subset guardrail, gravimetric reference. `[PDR-060; TrueMoist report §18; High]` | No issue in definition; achievement remains untested. | Preserve metrics and pre-register split before data collection. | <1 day / ₹0 | Failure means compensation hypothesis not demonstrated. |
| G5 Access | **Provisional Pass** | Required oven 105 ± 5 °C, scale, containers, jig, soil workspace are specified. `[PDR-048; TrueMoist report §§16–17; High]` | Institutional oven and precision-scale access explicitly pending. | Gate C: written/booking confirmation and trial dry-to-constant-mass run. | 1–3 days confirmation; ≥24 h trial / ₹0 if available | Without credible gravimetric truth, final accuracy claims cannot proceed. |
| G6 Patent path | **Insufficient Evidence** | Current direction is workflow/drift/confidence/calibration methodology; ordinary fusion/regression is not automatically patentable. `[PDR-045; TrueMoist report §28; High]` | MVP fixed regression may be conventional; future adaptive angles and current prior art unverified. | Current primary-source patent search, then choose a specific mechanism and corresponding experiment. | Duration/cost not established in repository | Successful MVP may still provide only engineering validation, not a patent-development path. |
| G7 Fatal dependency | **Provisional Pass** | Architecture explicitly classified ready with mandatory early validation and has fallbacks. `[PDR-061/PDR-063; High]` | Probe repeatability, packing, salinity effect, ADC value, gravimetric access and pilot improvement all pending. | Execute Week-1/Week-2 Gates A–F before main dataset. | 1–2 weeks / prototype/consumables within BOM | No repeatable probe/reference chain is an architecture kill; other failures force narrower scope. |

## Precheck summary without elimination

No concept is eliminated. Repository evidence supports several provisional implementation paths, but G6 is **Insufficient Evidence for all three** until current patent verification is performed. Other provisional gates are tied to early physical experiments or resource confirmation, not to further document synthesis.


---

## Source 6: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md`
- Current SHA-256: `125c057229524532b115391fbba948023684ad61d0153fb28ac29e6031e8ee3b`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Uncertainty and Test Register

## Use

Costs and durations are approximate planning values bounded by repository evidence. Where the repository provides no defensible amount, the entry says “unavailable” rather than inventing one. Patent effects describe evidence implications, not patentability.

## Threshold-status rule

Unless explicitly identified as an accepted PDR or final-architecture threshold, numerical pass/fail values in this register are proposed pre-registration thresholds for owner approval. They are not frozen project requirements.

Accepted PDR/report thresholds must remain distinguished from newly proposed working thresholds.

### U-OB-01 — SG90 passive-return / torsion-spring claim

- **Concept / category:** OpenBraille / mechanical architecture
- **Question:** Does the selected SG90 variant provide a usable passive return that retracts the pin when commanded/unpowered, or must the servo actively rotate the cam back?
- **Why it matters:** The final report says passive integral-spring reset; PDR-021 marks it technically unvalidated and requires correction if absent.
- **Current evidence:** `Project_mC_Decision_Register_v1.2.md`, PDR-021; `OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`, Hardware and Mechanical Architecture.
- **Earliest action / equipment:** Physically inspect one procured servo; bench it powered and unpowered with cam load; video/angle/force record. Servo, supply, simple load/cam.
- **Cost / duration:** One servo within BOM; <1 day.
- **Pass / fail:** Pass = repeatable passive return sufficient for required pin travel/load. Fail = no passive return or insufficient/unreliable return.
- **Effect:** Patent case—clarifies actual claim elements; buildability—requires truthful active-retraction control or mechanical spring fallback.
- **Urgency:** Immediate, before CAD freeze.

### U-OB-02 — Active cam-retraction interpretation

- **Concept / category:** OpenBraille / control-mechanics interface
- **Question:** If passive return is absent, does commanded 90°→0° cam motion retract all pins reliably without an added spring?
- **Why it matters:** This is PDR-021’s required correction and changes failure modes and control description.
- **Current evidence:** PDR-021; OpenBraille report, operating principle and Mechanical Architecture.
- **Action / equipment:** Single-dot cam prototype; repeated up/down commands under representative friction; calipers and current logging.
- **Cost / duration:** Single-dot materials within BOM; 1–2 days.
- **Pass / fail:** Pass = repeatable full retraction with no sticking across planned cycles. Fail = incomplete return requiring geometry or spring redesign.
- **Effect:** Patent—defines the real control/mechanical interaction; buildability—may add hardware/iteration.
- **Urgency:** Immediate.

### U-OB-03 — Six-servo current demand and 5 V/2 A adequacy

- **Concept / category:** OpenBraille / electrical
- **Question:** Does the specified supply/capacitor prevent voltage sag and resets under worst credible six-servo transitions, stalls, and rapid sequences?
- **Why it matters:** Each servo is reported up to ~500 mA peak; “never all six active” is an operating assumption, not measured proof.
- **Current evidence:** OpenBraille report, Hardware/Electrical Architecture; PDR-020.
- **Action / equipment:** Current/voltage logging for one, three, then six servos; worst-pattern transition and controlled stall test; multimeter/oscilloscope if available.
- **Cost / duration:** Within prototype BOM; 1 day after six servos arrive.
- **Pass / fail:** Pass = no unsafe sag, brownout, overheating, or reset with margin. Fail = any repeatable power fault.
- **Effect:** Patent—usually peripheral unless power sequencing becomes specific contribution; buildability—may require larger supply/sequencing and BOM revision.
- **Urgency:** Week 1, before full integration.

### U-OB-04 — Mechanical friction and tolerance

- **Concept / category:** OpenBraille / fabrication
- **Question:** Can FDM guides, pins, cams and followers achieve free motion, ≤0.1 mm variance over 100 cycles, and ≥1,000 cycles without failure?
- **Why it matters:** Macro-scaling mitigates but does not validate the dominant mechanical risk.
- **Current evidence:** OpenBraille report, Mechanical Architecture, Validation, Remaining Risks.
- **Action / equipment:** Print a single-dot tolerance coupon/module, measure clearances, run automated cycling, inspect wear.
- **Cost / duration:** Single-dot fraction of ₹2,060–₹2,850 BOM; 2–4 days including printing/cycling.
- **Pass / fail:** Pass = report thresholds met; fail = binding, excessive variance, or failure before 1,000 cycles.
- **Effect:** Patent—produces manufacturing/geometry evidence; buildability—direct critical-path risk.
- **Urgency:** Immediate.

### U-OB-05 — Macro MVP versus long-term invention path

- **Concept / category:** OpenBraille / scope and patent development
- **Question:** What exact technical bridge, if any, connects the deliberately non-ISO macro servo/cam MVP to the manufacturing/firmware invention direction or future true-scale mechanism?
- **Why it matters:** Semester success and long-term invention are distinct; the macro MVP must not be assumed to prove commercial-scale feasibility.
- **Current evidence:** PDR-009/PDR-016; OpenBraille report ADR-002; Phase 2 report §2.1.
- **Action / equipment/data:** After current patent search, make a claim-to-experiment map separating macro evidence, scale-dependent elements, and deferred true-scale elements.
- **Cost / duration:** Patent pass cost/duration unavailable; mapping 1–2 days after results.
- **Pass / fail:** Pass = at least one specific prospective contribution is testable at macro scale and relevant beyond mere substitution. Fail = all meaningful claim elements depend on unbuilt true-scale architecture.
- **Effect:** Patent—central; buildability—prevents inappropriate scope expansion.
- **Urgency:** Before patent scoring.

### U-OB-06 — Meaningful servo-cam patent support

- **Concept / category:** OpenBraille / patent evidence
- **Question:** Can the servo-cam prototype support a specific manufacturing or firmware/control claim rather than only demonstrating a conventional actuator substitution?
- **Why it matters:** PDR-009 explicitly moves the target away from the physical mechanism.
- **Current evidence:** PDR-009; Phase 2 §2.1; OpenBraille report ADRs and validation.
- **Action:** Current primary patent search/claim chart; identify nearest relevant manufacturing/control art; design a comparative experiment.
- **Cost / duration:** Unavailable in repository.
- **Pass / fail:** Pass = specific differentiated claim elements plus measurable advantage. Fail = only known component aggregation or known actuation.
- **Effect:** Patent—decisive; buildability—may define extra experiments but must not redesign prematurely.
- **Urgency:** Before any patent-potential score.

### U-OB-07 — Tactile-identification protocol and acceptance

- **Concept / category:** OpenBraille / demonstrable success
- **Question:** What blinded tactile-identification protocol, participant plan, and quantitative acceptance rate will establish that raised and lowered dots and complete patterns are reliably distinguishable by touch?
- **Why it matters:** The EDR requires acceptable tactile performance, while the final architecture report calls for structured human testing but does not freeze a participant plan or quantitative reader-success threshold.
- **Current evidence:** `PHASE 3/Engineering_Design_Review.md`, OpenBraille / Minimum Demonstrable Success; `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`, Prototype Validation Strategy M6 and Acceptance Criteria.
- **Action / equipment/data:** Obtain owner approval for a blinded protocol, participant plan, trial count, pattern set, randomization, and quantitative acceptance rate before tactile testing.
- **Cost / duration:** Participant-access cost and duration are unavailable in the repository.
- **Pass / fail:** Pass = the owner-approved pre-registered tactile-identification criterion is met. Fail = it is not met or the test lacks the approved controls.
- **Effect:** Patent—determines whether tactile-performance evidence is credible; buildability—may require changes to pin height, spacing, profile, or mechanism.
- **Urgency:** Before tactile validation and final G4 confirmation.

### U-VG-01 — ADXL345 bandwidth boundary

- **Concept / category:** VibeGuard / sensing scope
- **Question:** Is ADXL345 adequate for every claimed MVP phenomenon, and are bearing-fault/high-frequency claims explicitly excluded?
- **Why it matters:** 1,600 Hz stated bandwidth is adequate for low-frequency imbalance but IIS3DWB is the documented 6,000 Hz upgrade for bearing work.
- **Current evidence:** PDR-023/PDR-055; VibeGuard report §§3b–4.
- **Action / equipment:** Measure rig spectral content and anti-aliasing/ODR behavior; freeze claim boundary. Optional side-by-side higher-bandwidth sensor only if bearing scope is proposed.
- **Cost / duration:** ADXL rig within BOM; comparison sensor ₹800–₹1,200 if chosen; 2–3 days.
- **Pass / fail:** Pass = relevant fault energy and repeatable features lie within verified band. Fail = required discriminating signature lies outside.
- **Effect:** Patent—limits claim language; buildability—may trigger documented sensor upgrade.
- **Urgency:** Before test protocol freeze.

### U-VG-02 — Rigid-mount repeatability

- **Concept / category:** VibeGuard / mechanical validation
- **Question:** Can the sensor be remounted or reproduced with sufficiently consistent coupling that classification does not depend on an accidental installation?
- **Why it matters:** Mounting changes the transfer function and may dominate the signal.
- **Current evidence:** PDR-028; VibeGuard report §§2,8,10.
- **Action / equipment:** Repeated remove/reinstall trials using a defined bracket/torque/adhesive process; compare feature distributions.
- **Cost / duration:** Bracket/fasteners within rig BOM; 1–2 days.
- **Pass / fail:** Pass = between-mount variation remains below pre-registered normal/fault separation. Fail = mount variance overlaps the fault effect.
- **Effect:** Patent—supports deployment/repeatability evidence if relevant; buildability—may require a better fixture.
- **Urgency:** Early bench phase.

### U-VG-03 — Spectral-subtraction adequacy

- **Concept / category:** VibeGuard / DSP
- **Question:** Does baseline spectral subtraction plus band-limited features improve discrimination under controlled interfering vibration without unacceptable false alarms or lost fault energy?
- **Why it matters:** It is the frozen mitigation for single-node noise but explicitly unproven.
- **Current evidence:** PDR-027; VibeGuard report §3c and §12.
- **Action / equipment:** Target motor plus separately controlled interferer; randomized baseline/fault/noise trials; compare raw features, band limits, subtraction, and threshold baseline.
- **Cost / duration:** Second motor/access cost unavailable; 3–7 days after rig build.
- **Pass / fail:** Pass = pre-registered improvement in attribution/classification without material degradation; numeric threshold must be frozen before test. Fail = no benefit or unstable false alarms.
- **Effect:** Patent—central to any specific isolation-method case; buildability—could reduce MVP to conventional controlled bench monitor.
- **Urgency:** High, after acquisition is stable.

### U-VG-04 — Dense-machine attribution claim

- **Concept / category:** VibeGuard / validation and patent
- **Question:** Can one node attribute a fault to its mounted machine on a real dense-machine floor rather than merely detect increased vibration?
- **Why it matters:** Phase 2’s narrow potential and PDR-013 depend on real field evidence.
- **Current evidence:** PDR-013; Phase 2 report §2.2; VibeGuard report §3c.
- **Action / equipment/data:** Secure a site; independently label machine states; compare target fault/no-fault while neighbors vary; pre-register attribution metrics.
- **Cost / duration:** Site/access cost and duration unavailable; likely after bench validation.
- **Pass / fail:** Pass = meets pre-registered attribution/false-alarm thresholds across neighbor states. Fail = response cannot be assigned to target machine.
- **Effect:** Patent—decisive for narrow niche; buildability—field dependence may exceed semester constraints even if bench MDS passes.
- **Urgency:** Before patent scoring or any dense-floor claim.

### U-VG-05 — Eccentric-mass fault-simulation repeatability

- **Concept / category:** VibeGuard / ground truth
- **Question:** Does the chosen eccentric mass and placement generate repeatable abnormal conditions without varying speed/mounting unpredictably?
- **Why it matters:** Bench labels are only credible if the induced condition is controlled.
- **Current evidence:** PDR-030; VibeGuard report Consensus and §13.
- **Action / equipment:** Fixed mass, radius and attachment fixture; tachometer if available; repeated randomized install/run trials.
- **Cost / duration:** Within test-rig BOM; 1–2 days.
- **Pass / fail:** Pass = feature distribution is stable and separated from normal across replicates. Fail = induced effect varies enough to confound classifier.
- **Effect:** Patent—quality of experimental support; buildability—may require a precision fixture.
- **Urgency:** Before classifier tuning.

### U-VG-06 — More than a conventional vibration monitor

- **Concept / category:** VibeGuard / patent differentiation
- **Question:** What experimentally demonstrated feature is nonconventional beyond ADXL345 + FFT/features + threshold/anomaly alert?
- **Why it matters:** Phase 3C itself warns that a bare sensor relay is not the differentiator; Phase 2 names crowded art.
- **Current evidence:** VibeGuard report §12; Phase 2 §2.2; PDR-046.
- **Action:** Current patent search and claim chart; benchmark proposed isolation/statistical method against simple RMS/FFT baseline and nearest identified methods.
- **Cost / duration:** Patent pass unavailable; experimental comparison 3–7 days after rig.
- **Pass / fail:** Pass = specific method and measurable improvement tied to claim elements. Fail = only conventional monitoring remains.
- **Effect:** Patent—decisive; buildability—advanced experiment may add burden.
- **Urgency:** Before patent score.

### U-VG-07 — Quantitative bench-classification success threshold

- **Concept / category:** VibeGuard / demonstrable success
- **Question:** What trial count and quantitative accuracy, false-alarm, missed-detection, persistence, and repeatability criteria will define reliable Normal/Abnormal classification on the controlled bench rig?
- **Why it matters:** The EDR requires consistent distinction and the final architecture leaves statistical threshold tuning empirical, but no authoritative system-level numerical acceptance threshold is frozen.
- **Current evidence:** `PHASE 3/Engineering_Design_Review.md`, VibeGuard / Minimum Demonstrable Success; `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`, §13 Remaining Engineering Uncertainties.
- **Action / equipment/data:** Obtain owner approval for a pre-registered randomized trial protocol and quantitative acceptance criteria before classifier evaluation.
- **Cost / duration:** Protocol-definition cost and duration are unavailable in the repository.
- **Pass / fail:** Pass = the owner-approved pre-registered bench-classification criteria are met. Fail = they are not met or the evaluation lacks the approved controls.
- **Effect:** Patent—provides interpretable baseline and differentiator evidence; buildability—prevents a visually convincing but quantitatively undefined demonstration from being treated as success.
- **Urgency:** Before classifier tuning and final G4 confirmation.

### U-TM-01 — ADS1115 value versus calibrated ESP32 ADC1

- **Concept / category:** TrueMoist / instrumentation
- **Question:** Does ADS1115 materially improve noise, drift, reproducibility, or held-out pilot RMSE?
- **Why it matters:** PDR-032 forbids justification from bit count alone.
- **Current evidence:** PDR-032; TrueMoist report §11.3.
- **Action / equipment:** Same-node paired reads for dry/medium/wet samples; compare SD, 10-minute drift, reinsertion and pilot RMSE.
- **Cost / duration:** ADS1115 ₹120–₹220 listed; 1–2 days.
- **Pass / fail:** ≥15% improvement strongly justifies; 5–15% supports retention; <5% permits fallback; instability/unavailability fails module.
- **Effect:** Patent—normally conventional; buildability—determines simpler acquisition path.
- **Urgency:** Week 1.

### U-TM-02 — Probe repeatability

- **Concept / category:** TrueMoist / sensing
- **Question:** Does a genuine capacitive probe give stable, monotonic, repeatable output?
- **Why it matters:** No model can rescue an unstable measurement chain.
- **Current evidence:** TrueMoist report §§8.2–8.3 and Gate A.
- **Action / equipment:** Dry-air/warm-up tests, fixed moist sample, ten jig insertions, two-probe comparison.
- **Cost / duration:** Two probes ₹300–₹600 listed; 1–2 days.
- **Pass / fail:** Gate A pass <5% usable-span reinsertion SD and monotonic pilot; fail >10%, saturation, or non-monotonicity.
- **Effect:** Patent—determines whether compensation evidence is credible; buildability—architecture kill if no usable probe.
- **Urgency:** Week 1.

### U-TM-03 — Insertion and packing sensitivity

- **Concept / category:** TrueMoist / mechanical experimental control
- **Question:** Can a jig and fixed preparation reduce packing/insertion variation below intended environmental effects?
- **Why it matters:** Packing may masquerade as or overwhelm temperature/salinity effects.
- **Current evidence:** PDR-061; TrueMoist report §§17,24, Gate D.
- **Action / equipment:** Independently repack controlled samples using fixed mass, compaction and fill height; compare variance.
- **Cost / duration:** Jig/container materials ₹200–₹450 listed; 2–4 days.
- **Pass / fail:** Pass = packing variance below intended disturbance effect. Fail = equal or greater.
- **Effect:** Patent—essential to claimed error-separation workflow; buildability—may force rig redesign or scope reduction.
- **Urgency:** Week 1–2.

### U-TM-04 — Institutional oven and precision-scale access

- **Concept / category:** TrueMoist / facilities and ground truth
- **Question:** Is credible 105 ± 5 °C drying-to-constant-mass and suitable weighing actually available for the full schedule?
- **Why it matters:** PDR-048 makes gravimetric GWC authoritative; buying an oven is outside budget.
- **Current evidence:** PDR-048; TrueMoist report §§16,22, Gate C.
- **Action / equipment:** Written booking/access confirmation; one full dry/reweigh trial; confirm 0.01 g preferred or justify 0.1 g with 300–500 g samples.
- **Cost / duration:** ₹0 if institutional; optional scale ₹400–₹700; ≥24 h trial.
- **Pass / fail:** Pass = repeatable access/process/resolution. Fail = no traceable ground truth.
- **Effect:** Patent—invalidates performance evidence if absent; buildability—architecture becomes conditional and final accuracy claims stop.
- **Urgency:** Week 1, before main procurement/dataset.

### U-TM-05 — Controlled-salinity treatment effect

- **Concept / category:** TrueMoist / experimental factor
- **Question:** Can one NaCl treatment produce a repeatable, non-saturating shift distinct from noise at fixed moisture/temperature?
- **Why it matters:** Salinity is represented as a controlled treatment, not measured EC; if no separable effect, the compensation scope narrows.
- **Current evidence:** PDR-062; TrueMoist report §§10,26 Gate E.
- **Action / equipment:** Pilot S0/S1 dose by dry-soil mass; adjust dose once if necessary.
- **Cost / duration:** Consumables within ₹100–₹300 line; 1–3 days plus equilibration.
- **Pass / fail:** Pass = shift >3× within-condition electronic noise, repeatable and nonsaturating. Fail = no separable effect/unstable direction after one adjustment.
- **Effect:** Patent—affects controlled error-separation evidence; buildability—fallback is temperature-only MVP.
- **Urgency:** Week 2.

### U-TM-06 — Feasibility of 72 independent physical runs

- **Concept / category:** TrueMoist / schedule and validation
- **Question:** Can the team prepare, equilibrate, measure, dry, log and quality-check 72 independent runs within eight weeks?
- **Why it matters:** Rapid ADC reads cannot be counted as independent; physical workload is the limiting resource.
- **Current evidence:** PDR-059; TrueMoist report §§15,23,30.
- **Action / equipment/data:** Time an end-to-end pilot batch and calculate throughput using actual oven capacity and person-hours.
- **Cost / duration:** Pilot consumables within BOM; 3–7 elapsed days.
- **Pass / fail:** Pass = measured throughput supports 72 with contingency. Fail = does not; documented 54-run fallback may be considered.
- **Effect:** Patent—smaller dataset may weaken evidentiary breadth; buildability—direct schedule risk.
- **Urgency:** Week 2–3 before main dataset.

### U-TM-07 — Claimability of calibration/compensation workflow

- **Concept / category:** TrueMoist / patent differentiation
- **Question:** Is the actual MVP workflow sufficiently specific and nonconventional, or only generic calibration plus ordinary regression?
- **Why it matters:** TM-R §28.2 explicitly says ordinary fusion, polynomial regression and generic calibration are not automatically patentable.
- **Current evidence:** PDR-045; TrueMoist report §28; Phase 2 §2.3.
- **Action:** Current primary patent search and claim chart for controlled error separation, confidence/range fallback, drift/event recalibration and transfer calibration; map experiments to one specific mechanism.
- **Cost / duration:** Unavailable in repository.
- **Pass / fail:** Pass = verified prospective claim elements linked to measurable advantage. Fail = only conventional workflow remains.
- **Effect:** Patent—decisive; buildability—may distinguish semester MVP from a later invention experiment.
- **Urgency:** Before patent score.


---

## Source 7: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/06_Patent_Research_Input_Pack.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `969d6bd97f0a726186d0f9bae405248ed82ef6314e3d5618166a0a1185411428`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/06_Patent_Research_Input_Pack.md`
- Current SHA-256: `969d6bd97f0a726186d0f9bae405248ed82ef6314e3d5618166a0a1185411428`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Patent Research Input Pack

## Scope and warning

This pack prepares—not performs—a later current patent search. Historical repository conclusions below are search leads, not verified current patent status, patentability, validity, claim construction, or freedom-to-operate. No concept is stated to be patentable. Search primary patent records, current family/legal status, claims, citations, assignments, continuations/divisionals, non-US equivalents (including relevant Indian and Chinese records), and relevant non-patent literature before scoring.

## OpenBraille

### Current technical definition

- **Engineering hypothesis:** A lower-cost actuation strategy can replace conventional piezoelectric actuation while retaining acceptable tactile performance for a refreshable Braille interface. Source: `PHASE 3/Engineering_Design_Review.md`, OpenBraille / Engineering Hypothesis.
- **MVP architecture:** One macro-scale (~300% ISO 17049), 6-dot refreshable cell; ESP32 direct PWM; six SG90-class servos; eccentric cams/followers/pins; FDM frame; external 5 V/2 A supply. Source: `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`, Final Architecture.
- **Phase 2 historical conclusion:** Mechanism space was assessed Moderate–High saturation, with Dot Incorporation a dominant named fence; naive known-actuator substitution had high obviousness risk. Historical pivot: manufacturing/fabrication method and firmware/control. Source: `PHASE 2/Phase2_Report by CLaude.md`, §2.1; accepted direction in PDR-009.

### Proposed patent-development angle

Repository-supported directions to verify:

- a specific manufacturing/fabrication method for low-cost tactile cells/arrays;
- a specific control/firmware method that enables cheap commodity actuators;
- geometry/process/control interactions supported by force, travel, repeatability, wear, power, tolerance and tactile evidence.

These are directions only. The current macro servo/cam implementation has not been shown to embody a claimable contribution.

### Apparently conventional features

Servo motor, eccentric cam, follower and pin; ESP32 PWM; serial character mapping; 3D-printed frame; macro scaling as a prototyping tactic; ordinary calibration/self-test; external low-voltage supply. Verify rather than assume.

### Suggested differentiators to test

- specific manufacturable cell geometry or modular assembly that produces repeatable tactile travel at low tolerance/cost;
- fabrication sequence/material/clearance combination with measured yield or durability advantage;
- actuator-control/sequencing/calibration method that improves peak current, travel consistency, wear, or cost;
- any bridge from macro proof to practical multi-cell or smaller-scale architecture.

### Required experimental proof

Actual reset mode; actuator force/torque and current; pin travel and tactile outcome; tolerance/yield; 100-cycle variance and ≥1,000-cycle durability; multi-servo power behavior; comparison against a conventional servo/cam or nearest identified approach; scale-dependence of asserted advantages.

### Named repository leads

Historical/unverified: Dot Incorporation/Dot Inc. estate; Orbit Research/Orbit Reader; Innovision/Braille Me; Canute; Monarch; MOLBED; MagnePins; US 5,685,721; US 6,881,063; US 11,410,574; US 6,743,021 B2; US 8,770,981 B2; WO 2015189863 A2; CA 3,120,784 A1; US 11,854,423 B1; EP 4,049,116 A1; US 10,254,499 B1. Source lead: Phase 2 §2.1 and OpenBraille final report’s rejected-alternative discussion. Every identifier, family, claim, status and relevance requires primary-source verification.

### Search terms and variants

`refreshable braille cell`, `refreshable tactile display`, `tactile pin array`, `braille dot actuator`, `servo cam braille`, `cam follower tactile pin`, `low cost braille actuator`, `macro scale braille prototype`, `3D printed refreshable braille`, `additive manufactured tactile display`, `monolithic tactile cell`, `modular braille actuator`, `PWM tactile actuator control`, `adaptive overdrive braille actuator`, `shared driver tactile pins`, `low force latching tactile pixel`, `piezoelectric braille replacement`.

Variants: refreshable/rewritable/dynamic; Braille/tactile/haptic; dot/pin/taxel/tactile pixel; cell/module/array/display; actuator/raiser/lifter; cam/eccentric/linkage; fabrication/manufacture/additive/printed/molded.

### Likely claim elements to test

Do not draft claims yet. Test combinations involving: cell frame/guide geometry; identical replaceable actuator modules; cam/follower travel relationship; manufacturing process and tolerances; actuator calibration; selective/sequenced actuation; peak-current management; closed/verified tactile state; low-cost multi-cell scaling; control tied to a measurable physical benefit.

### Verification assumptions and questions

- What Dot families are alive, where, and what do their independent claims actually cover?
- Does any family cover servo/cam, printed guides, modular tactile pins, manufacturing methods, or control/sequencing?
- Are MOLBED/MagnePins prior art, open-hardware publications, patents, or combinations?
- Is the Phase 2 manufacturing/firmware “white space” still plausible after current searching?
- Is macro-scale evidence technically relevant to any claim with practical value?
- Does the prototype show more than substitution of a known actuator into a known Braille cell?
- Which experiments distinguish a prospective contribution from the closest current primary art?

## VibeGuard

### Current technical definition

- **Engineering hypothesis:** Low-cost embedded local vibration analysis can distinguish normal from deliberately introduced early abnormal behaviour on constrained hardware without cloud processing. Sources: EDR VibeGuard / Engineering Hypothesis; VibeGuard SOP §2.
- **MVP architecture:** Rigid ADXL345 over SPI to ESP32; DC removal, Hann, continuous time features, triggered FFT; calibrated RMS/persistence baseline and Mahalanobis target; baseline spectral subtraction; RGB alert; eccentric-mass motor/fan rig. Source: `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`, §§4–13.
- **Phase 2 historical conclusion:** Broad predictive-maintenance/SME monitoring assessed crowded; narrow adaptive single-node attribution niche assessed contested/unproven. A real dense-machine test was required. Source: Phase 2 §2.2; PDR-013 and PDR-046.

### Proposed patent-development angle

A specific, experimentally superior single-node attribution/noise-discrimination method using in-situ baseline calibration, band-limited spectral subtraction and multivariate statistical detection on constrained hardware. Zero-subscription/SME economics is a commercial position, not technical novelty.

### Apparently conventional features

MEMS accelerometer on a motor; rigid mount; ESP32; SPI acquisition; DC removal/Hann/FFT; RMS, peak, crest factor, kurtosis; threshold/persistence; RGB alarm; eccentric-mass imbalance rig; generic Mahalanobis anomaly detection. Their combination must not be presumed novel.

### Suggested differentiators to test

- target-machine attribution under neighboring-machine interference using one sensor;
- a specific calibration/subtraction/feature-selection/control sequence;
- resource-constrained implementation that preserves measurable attribution performance;
- adaptive or confidence-gated behavior beyond fixed thresholds;
- mounting/calibration interaction only if technically specific and nonconventional.

### Required experimental proof

Rigid-mount repeatability; fault-injection repeatability; classifier accuracy, false alarms and missed detections; ablations (RMS only, FFT features, Mahalanobis, subtraction); controlled interferer; real dense-machine field data with independent source labels; compute/memory/timing; comparison to nearest patent methods.

### Named repository leads

Historical/unverified: US 7,421,349 (US Navy phase-coupling lead); Tractian and a reported fault-detection patent; Infinite Uptime; Augury; KCF/Senseye. Source: Phase 2 §2.2. IIS3DWB is a technical upgrade, not a patent lead. All identifiers, families, current status and claim scope require primary verification.

### Search terms and variants

`single sensor machine vibration attribution`, `single node vibration source isolation`, `machine fault neighboring machine noise`, `vibration spectral subtraction condition monitoring`, `in situ vibration baseline calibration`, `edge vibration anomaly Mahalanobis`, `band limited vibration fault features`, `spatial attribution accelerometer machine`, `phase coupling unrelated spectral peaks fault`, `low cost predictive maintenance edge node`, `target machine vibration discrimination`, `dense factory vibration cross talk`, `mechanical cross-talk condition monitoring`, `unsupervised vibration anomaly embedded`.

Variants: predictive maintenance/condition monitoring/machine health/fault detection; vibration/acceleration/acoustic emission; source isolation/source separation/attribution/discrimination/crosstalk rejection; edge/local/on-device/single-node; baseline/subtraction/fingerprint/envelope/sideband/phase coupling; anomaly/novelty/one-class/Mahalanobis.

### Likely claim elements to test

Sensor-to-machine mounting; baseline acquisition conditions; spectral envelope representation; target bands; subtraction/update rule; feature vector; multivariate distance/confidence; persistence; attribution decision; constrained compute scheduling/triggered FFT; handling neighbor-state changes; output tied to maintenance condition.

### Verification assumptions and questions

- What does US 7,421,349 actually claim, what families/status exist, and how close is it to the proposed method?
- Which Tractian/Infinite Uptime or other families cover fingerprinting, local diagnosis, SME nodes, or source attribution?
- Is spectral subtraction in vibration monitoring already conventional?
- Does Mahalanobis plus common features add anything claim-relevant?
- Can single-node dense-machine attribution be demonstrated, and against which closest-art baseline?
- Is the patent angle an algorithm/method claim with jurisdiction-specific eligibility/obviousness risk?
- What primary sources exist in Indian and Chinese databases that earlier passes missed?

## TrueMoist

### Current technical definition

- **Engineering hypothesis:** Environmental measurements and controlled calibration data can compensate predictable commodity-probe error, improving stability and closeness to gravimetric reference versus uncompensated output under controlled tests. Source: TrueMoist final report §2.2.
- **MVP architecture:** Genuine analog capacitive probe; DS18B20; ADS1115 with Week-1 value gate; ESP32; controlled salinity treatment, not live EC; one soil; offline linear/ridge second-order models and fixed MCU coefficients; USB CSV; 72 physical runs; gravimetric GWC. Source: PDR-058–063 and TrueMoist final report.
- **Phase 2 historical conclusion:** Hardware compensation assessed crowded; software-only event-driven/self-updating correction was the proposed pivot. Phase 3C intentionally narrows MVP to fixed coefficients and controlled single-soil proof. Source: Phase 2 §2.3; PDR-045.

### Proposed patent-development angle

Repository-supported future mechanisms to verify:

- event-triggered recalibration using sparse trusted reference events;
- sensor-drift detection with confidence gating;
- calibration transfer across commodity probe units;
- calibration compression on constrained MCUs;
- a controlled sequence separating packing, temperature and conductivity effects;
- validity-region detection and safe fallback.

The current polynomial model, ESP32, ADS1115, generic sensor fusion and generic calibration are explicitly not automatically patentable.

### Apparently conventional features

Capacitive moisture probe; temperature sensor; external ADC; ESP32; RC filter; gravimetric calibration; linear/polynomial/ridge regression; offline training/fixed coefficients; CSV; controlled salt dosing; jigs and ordinary sample preparation.

### Suggested differentiators to test

- a specific experimental/control workflow that distinguishes error sources and controls confidence;
- drift/event detection and gated recalibration mechanism;
- cross-unit transfer with bounded confidence/fallback;
- validity-region detection that prevents unsafe extrapolation;
- materially compressed calibration without losing compensation performance.

### Required experimental proof

Probe/reinsertion/packing repeatability; gravimetric traceability; salinity effect; raw versus compensated held-out RMSE/MAE; subset guardrails; grouped validation; model/MCU equivalence; drift sequences; multiple probe units for transfer; ablation of each variable/mechanism; comparison to conventional calibration.

### Named repository leads

Historical/unverified: Campbell Scientific; METER Group/TEROS; Toro; CropX; US 7,884,620; US 11,598,743; US 7,170,302 B2; US 20150330932A1. Source: Phase 2 §2.3. All assignees, families, status, expiry estimates, independent claims and relevance require current primary-source verification.

### Search terms and variants

`soil moisture temperature salinity compensation`, `capacitive soil moisture drift correction`, `soil moisture sensor self calibration`, `event triggered recalibration soil sensor`, `soil probe confidence gating`, `commodity soil probe transfer calibration`, `embedded soil moisture regression compensation`, `soil sensor validity region fallback`, `packing effect compensation soil moisture`, `conductivity temperature dielectric moisture correction`, `sparse reference recalibration irrigation`, `multi probe calibration transfer`, `edge calibration compression sensor`, `gravimetric calibrated embedded moisture`.

Variants: moisture/water content/dielectric/permittivity; soil/substrate/growing media; salinity/conductivity/EC/fertilizer; drift/aging/hysteresis/bias; compensation/correction/calibration/recalibration; confidence/quality/validity/out-of-range; transfer/interchangeability/unit-to-unit; event/irrigation/dry-down/reference.

### Likely claim elements to test

Commodity sensor inputs; environmental/treatment inputs; trusted reference event; drift detector; confidence score; model-validity region; update gate; safe fallback; cross-unit transfer; calibration dataset/control sequence; compressed coefficients; local inference; physical measurement improvement.

### Verification assumptions and questions

- What do the named Campbell/METER/Toro/Korean-assignee families actually claim and where are they alive?
- How crowded are calibration, environmental compensation, drift detection, event recalibration and probe-transfer subfields today?
- Is controlled error-source separation a technical method or merely ordinary experimental practice?
- Does the fixed-coefficient MVP generate evidence relevant to a later adaptive claim, or are additional drift/reference-event experiments mandatory?
- Can any prospective element show a measurable advantage over generic multivariate calibration?
- Which claim form has technical-effect/eligibility risk in relevant jurisdictions?
- What Indian/Chinese and non-patent sources were missed historically?

## Required output of the later patent pass

For each concept, the later pass should provide:

1. primary-source search log, databases, dates, jurisdictions and query strings;
2. verified family table and current legal status;
3. independent-claim summaries with direct source links;
4. closest-art feature chart against the actual frozen MVP and any future invention variant;
5. explicit separation of novelty, obviousness/inventive step, patent eligibility, and FTO;
6. unresolved claim-construction/legal questions;
7. experiments needed to support or falsify each prospective technical contribution;
8. confidence and limitations;
9. no legal conclusion beyond the evidence and reviewer competence.


---

## Source 8: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/07_Scoring_Worksheet.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `e0a1aeea2e7ba0de3e571531bcca2f51f441bca9e860dbb10fa8d6d22a4f744b`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/07_Scoring_Worksheet.md`
- Current SHA-256: `e0a1aeea2e7ba0de3e571531bcca2f51f441bca9e860dbb10fa8d6d22a4f744b`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Blank Final Scoring Worksheet

## Instructions

Do not complete this worksheet until the current patent-source verification pass is complete. Use scores 1–5 and calculate `(score / 5) × weight`. Every score requires confidence, evidence, uncertainty, resolving action, and patent-verification status. All score, total, gate-summary, and ranking fields are intentionally blank.

## OpenBraille

| Criterion | Weight | Score | Weighted contribution | Confidence | Evidence reference | Uncertainty | Resolving action | Patent research verified? |
|---|---:|---|---|---|---|---|---|---|
| A1 Specific claimable technical contribution | 15 |  |  |  |  |  |  |  |
| A2 Plausible white-space position | 8 |  |  |  |  |  |  |  |
| A3 Experimental patent-supporting evidence | 7 |  |  |  |  |  |  |  |
| A4 Prior-art/FTO risk | 5 |  |  |  |  |  |  |  |
| B1 Architecture and integration complexity | 8 |  |  |  |  |  |  | N/A |
| B2 Schedule realism | 6 |  |  |  |  |  |  | N/A |
| B3 Critical implementation risk | 6 |  |  |  |  |  |  | N/A |
| C1 Credible ground truth | 6 |  |  |  |  |  |  | N/A |
| C2 Repeatability and experimental control | 5 |  |  |  |  |  |  | N/A |
| C3 Clarity of success metrics | 4 |  |  |  |  |  |  | N/A |
| D Team fit | 10 |  |  |  |  |  |  | N/A |
| E Demonstration quality | 8 |  |  |  |  |  |  | N/A |
| F Budget and procurement certainty | 7 |  |  |  |  |  |  | N/A |
| G Commercial or social significance | 5 |  |  |  |  |  |  | As relevant |
| **Total** | **100** |  |  |  |  |  |  |  |

- **Hard-gate status:**
- **Patent-first rank:**
- **Buildability rank:**
- **Validation rank:**
- **Demonstration rank:**
- **Balanced overall rank:**
- **Final role (primary / runner-up / reserve):**

## VibeGuard

| Criterion | Weight | Score | Weighted contribution | Confidence | Evidence reference | Uncertainty | Resolving action | Patent research verified? |
|---|---:|---|---|---|---|---|---|---|
| A1 Specific claimable technical contribution | 15 |  |  |  |  |  |  |  |
| A2 Plausible white-space position | 8 |  |  |  |  |  |  |  |
| A3 Experimental patent-supporting evidence | 7 |  |  |  |  |  |  |  |
| A4 Prior-art/FTO risk | 5 |  |  |  |  |  |  |  |
| B1 Architecture and integration complexity | 8 |  |  |  |  |  |  | N/A |
| B2 Schedule realism | 6 |  |  |  |  |  |  | N/A |
| B3 Critical implementation risk | 6 |  |  |  |  |  |  | N/A |
| C1 Credible ground truth | 6 |  |  |  |  |  |  | N/A |
| C2 Repeatability and experimental control | 5 |  |  |  |  |  |  | N/A |
| C3 Clarity of success metrics | 4 |  |  |  |  |  |  | N/A |
| D Team fit | 10 |  |  |  |  |  |  | N/A |
| E Demonstration quality | 8 |  |  |  |  |  |  | N/A |
| F Budget and procurement certainty | 7 |  |  |  |  |  |  | N/A |
| G Commercial or social significance | 5 |  |  |  |  |  |  | As relevant |
| **Total** | **100** |  |  |  |  |  |  |  |

- **Hard-gate status:**
- **Patent-first rank:**
- **Buildability rank:**
- **Validation rank:**
- **Demonstration rank:**
- **Balanced overall rank:**
- **Final role (primary / runner-up / reserve):**

## TrueMoist

| Criterion | Weight | Score | Weighted contribution | Confidence | Evidence reference | Uncertainty | Resolving action | Patent research verified? |
|---|---:|---|---|---|---|---|---|---|
| A1 Specific claimable technical contribution | 15 |  |  |  |  |  |  |  |
| A2 Plausible white-space position | 8 |  |  |  |  |  |  |  |
| A3 Experimental patent-supporting evidence | 7 |  |  |  |  |  |  |  |
| A4 Prior-art/FTO risk | 5 |  |  |  |  |  |  |  |
| B1 Architecture and integration complexity | 8 |  |  |  |  |  |  | N/A |
| B2 Schedule realism | 6 |  |  |  |  |  |  | N/A |
| B3 Critical implementation risk | 6 |  |  |  |  |  |  | N/A |
| C1 Credible ground truth | 6 |  |  |  |  |  |  | N/A |
| C2 Repeatability and experimental control | 5 |  |  |  |  |  |  | N/A |
| C3 Clarity of success metrics | 4 |  |  |  |  |  |  | N/A |
| D Team fit | 10 |  |  |  |  |  |  | N/A |
| E Demonstration quality | 8 |  |  |  |  |  |  | N/A |
| F Budget and procurement certainty | 7 |  |  |  |  |  |  | N/A |
| G Commercial or social significance | 5 |  |  |  |  |  |  | As relevant |
| **Total** | **100** |  |  |  |  |  |  |  |

- **Hard-gate status:**
- **Patent-first rank:**
- **Buildability rank:**
- **Validation rank:**
- **Demonstration rank:**
- **Balanced overall rank:**
- **Final role (primary / runner-up / reserve):**

## Required final allocation check

- **Primary project:**
- **Runner-up:**
- **Reserve:**

Validation rule for the later pass: exactly one concept must occupy each role, but no field is filled during this extraction task.


---

## Source 9: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/08_High_Reasoning_Audit.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `4243ca6643361946805fcb4f5b3b7feb319ec352149b54664471b2d9cbd9e324`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/08_High_Reasoning_Audit.md`
- Current SHA-256: `4243ca6643361946805fcb4f5b3b7feb319ec352149b54664471b2d9cbd9e324`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# High-Reasoning Audit

## Audit scope

This audit independently reviewed the existing final down-selection evidence package for factual accuracy, authority handling, threshold status, neutrality, internal consistency, patent terminology, MVP boundaries, hard-gate logic, and repository safety. It did not regenerate the package, perform online research, or evaluate the candidates.

The audit was restricted to the package files for review and correction. Authoritative repository sources were read only to verify package claims. `ZEROTH PRESENTATION/` was not inspected or modified.

## Files and authoritative sources inspected

Package files:

- `README.md`
- `01_Comparison_Protocol.md`
- `02_Authoritative_Source_Manifest.md`
- `03_Concept_Evidence_Matrix.md`
- `04_Hard_Gate_Precheck.md`
- `05_Uncertainty_and_Test_Register.md`
- `06_Patent_Research_Input_Pack.md`
- `07_Scoring_Worksheet.md`
- `CODEX_EXTRACTION_VALIDATION.md`

Authoritative and gap-only sources:

- `PHASE 3/Engineering_Design_Review.md`
- `Project_mC_Decision_Register_v1.2.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/Phase3C_Portfolio_Closure_Memo_Approved.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Architecture_Report_Final.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_Memory_Final.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/OpenBraille/Phase3C_OpenBraille_SOP_Final.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Architecture_Report_Final.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_Memory_Final.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/VibeGuard/Phase3C_VibeGuard_SOP_Final.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Architecture_Report_Final.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_Memory_Final.md`
- `PHASE 3/PHASE 3C-Comparative Technical Evaluation/TrueMoist/Phase3C_TrueMoist_SOP_Final.md`
- `PHASE 2/Phase2_Report by CLaude.md` — checked only for the historical patent leads already carried into the input pack.

No raw independent-research file was used to override these sources.

## Previously approved corrections confirmed

The four approved corrections are present once in their operative locations and were not duplicated:

1. `01_Comparison_Protocol.md` contains one A4 direction rule: 5 means comparatively low/manageable blocking risk and 1 means severe, uncertain, or likely blocking risk; novelty/obviousness, patent eligibility, and FTO/infringement must be recorded separately.
2. `04_Hard_Gate_Precheck.md` contains one OpenBraille G4 row marked **Provisional Pass**. VibeGuard G4 remains **Provisional Pass** and TrueMoist G4 remains **Pass**.
3. `05_Uncertainty_and_Test_Register.md` contains one `Threshold-status rule` distinguishing accepted PDR/final-report thresholds from proposed owner-approval thresholds.
4. `CODEX_EXTRACTION_VALIDATION.md` contains one `Post-review corrections` section.

The validation record’s summary of those corrections is a historical record, not a duplicate operative rule.

## Additional factual or methodological corrections

### 1. OpenBraille tactile-identification uncertainty

- **Package file and section:** `05_Uncertainty_and_Test_Register.md`, added U-OB-07.
- **Original issue:** The matrix and hard-gate precheck correctly marked tactile validation as unresolved, but the uncertainty register lacked the blinded protocol, participant plan, and quantitative acceptance-rate question needed to resolve OpenBraille G4.
- **Authoritative source and location:** `PHASE 3/Engineering_Design_Review.md`, OpenBraille / Minimum Demonstrable Success; `Phase3C_OpenBraille_Architecture_Report_Final.md`, Prototype Validation Strategy M6 and Acceptance Criteria.
- **Minimal correction made:** Added one uncertainty entry requiring owner-approved pre-registration. No numerical threshold was invented.

### 2. VibeGuard quantitative bench-classification uncertainty

- **Package file and section:** `05_Uncertainty_and_Test_Register.md`, added U-VG-07.
- **Original issue:** The matrix and hard-gate precheck correctly stated that no numeric MDS acceptance threshold exists, but the uncertainty register lacked a dedicated question covering accuracy, false alarms, missed detections, persistence, repeatability, and trial count.
- **Authoritative source and location:** `PHASE 3/Engineering_Design_Review.md`, VibeGuard / Minimum Demonstrable Success; `Phase3C_VibeGuard_Architecture_Report_Final.md`, §13 Remaining Engineering Uncertainties.
- **Minimal correction made:** Added one uncertainty entry requiring owner-approved pre-registration. No numerical threshold was invented.

### 3. TrueMoist future multi-soil validation status

- **Package files and sections:** `03_Concept_Evidence_Matrix.md`, Cross-cutting conflict note 4; `CODEX_EXTRACTION_VALIDATION.md`, Contradictions and scope tensions item 7.
- **Original issue:** The package correctly excluded adaptive, calibration-free, multi-soil scope from the semester MVP, but its wording could be read as cancelling the earlier scope entirely.
- **Authoritative source and location:** `Project_mC_Decision_Register_v1.2.md`, PDR-012 (future two-season, multi-soil validation task) and PDR-049 (single-soil MVP limit).
- **Minimal correction made:** Clarified that the broader scope is not part of the semester MVP but PDR-012 remains a future validation task.

All three corrections were also recorded in `CODEX_EXTRACTION_VALIDATION.md`.

## Issues reviewed but not changed

- **Planning durations and resolving-action costs:** Many are approximate estimates rather than accepted source values. The precheck and register explicitly label them as planning estimates, use “unavailable” where no defensible amount exists, and do not present them as accepted requirements. No authoritative source directly demonstrated a replacement value, so no edit was justified.
- **OpenBraille architecture-report technical assertions:** Exact tolerances, servo current, mechanical behavior, and power mitigation originate in the final architecture report. The package does not independently validate them and appropriately marks reset, friction, torque, tactile adequacy, and 5 V/2 A sufficiency as pending.
- **VibeGuard 1,600 Hz wording:** The package preserves the repository’s stated ADXL345 3,200 Hz ODR / 1,600 Hz bandwidth boundary and confines it to low-frequency MVP tests. No external datasheet check was performed.
- **Historical patent identifiers and saturation statements:** They remain explicitly historical, unverified search leads. Current legal status, claims, patent eligibility, novelty/obviousness, and FTO are deferred to the upcoming primary-source pass.
- **Phase 4 readiness labels:** The package quotes concept-level readiness classifications but explicitly states that PDR-067 makes comparative down-selection the next action and that Phase 4 has not started.
- **Five-member role wording:** Lower-authority six-role arithmetic remains documented as a contradiction; PDR-038 controls with five members.
- **Audit-file indexing:** The package README indexes the original nine evidence-package files. This audit is a verification artifact created by the present task, not a replacement evidence file; no stylistic index expansion was made.

## Confirmed contradictions and evidence gaps

### OpenBraille

- PDR-021 overrides any assumption that an SG90 passive return is already proven; active servo-driven cam retraction is the required documented interpretation if physical inspection finds no usable passive return.
- The 5 V/2 A supply and 1,000 µF capacitor are accepted architecture selections, but six-servo worst-case adequacy remains unvalidated.
- Macro scaling addresses the semester build path but does not establish practical-scale or multi-cell invention feasibility.
- Mechanical friction, tolerance, torque, wear, 1.5 mm tactile adequacy, participant access, and the blinded tactile protocol remain pending.
- The patent direction is manufacturing/firmware, not a presumption that the servo-cam mechanism is novel or patentable.

### VibeGuard

- ADXL345 is the low-frequency MVP sensor; IIS3DWB remains the later bearing-fault bandwidth path.
- Bench eccentric-mass Normal/Abnormal detection is not evidence of dense-machine source attribution; PDR-013 retains the real field test.
- No authoritative numeric system-level success threshold exists for accuracy, false alarms, missed detections, or repeatability.
- Spectral subtraction and Mahalanobis detection are frozen architecture elements or targets whose adequacy/differentiation remains experimentally unvalidated.
- Conventional vibration-monitor and adjacent single-node prior art remain a material historical risk requiring current verification.

### TrueMoist

- ADS1115 is included in the primary architecture but remains evidence-gated against calibrated ESP32 ADC1.
- Dry-basis gravimetric GWC is authoritative; oven and scale access are pending.
- The target is 72 independent physical runs; repeated ADC readings are averaged and are not independent samples.
- Salinity is a controlled treatment code/known salt addition, not live or measured field EC.
- The semester MVP deploys offline-trained fixed coefficients; adaptive recalibration and related patent directions are later work.
- Accepted thresholds are held-out RMSE improvement of at least 20%, MAE improvement of at least 15%, and no more than 10% MAE worsening in a major tested subset. The first two are accepted in PDR-060; the subset guardrail is accepted in the final architecture report §18.3.
- PDR-012’s future two-season, multi-soil task remains outside the single-soil semester MVP.

### Cross-cutting

- Current primary patent-family status, independent-claim scope, continuations/divisionals, non-US records, patent eligibility, novelty/obviousness, and FTO remain unavailable.
- Current procurement quotes, supplier authenticity, facility bookings, physical builds, code, and experimental data remain unavailable.
- These are expected inputs to the patent-verification and later prototype phases, not evidence that a candidate has already passed them.

## Scoring and neutrality check

- Every score cell and weighted-contribution cell in `07_Scoring_Worksheet.md` remains blank.
- Total, hard-gate summary, ranking, final-role, primary-project, runner-up, and reserve fields remain blank.
- No score, total, ranking, recommendation, elimination, or selection was introduced by this audit.
- No candidate is explicitly or implicitly presented as the winner.
- Comparative adjectives retained from source descriptions are attributed and do not form a package-level ranking.

## Repository safety confirmation

- No authoritative project file was modified.
- No raw research was modified.
- `ZEROTH PRESENTATION/` was not inspected or modified and remains an unrelated untracked directory.
- No online research was performed.
- Nothing was staged, committed, merged, tagged, or pushed.
- The only existing package files edited by this audit were `03_Concept_Evidence_Matrix.md`, `05_Uncertainty_and_Test_Register.md`, and `CODEX_EXTRACTION_VALIDATION.md`.
- `HIGH_REASONING_AUDIT.md` is the only new audit file.

## Readiness verdict

**Ready for current patent verification**

The package now preserves the authority chain, special-concept boundaries, accepted-versus-proposed threshold distinction, hard-gate uncertainty, MVP-versus-long-term scope, and patent terminology needed for a current primary-source patent pass. Remaining patent and experimental gaps are explicitly identified rather than resolved by unsupported inference.

## Final validation

The final commands produced:

### `git diff --check`

```text
(no output; passed)
```

### `git status --short`

```text
?? "PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/"
?? "ZEROTH PRESENTATION/"
```

### `git diff --name-status`

```text
(no output; no tracked file changed)
```

### `git diff --stat`

```text
(no output; no tracked file changed)
```

Direct untracked-package verification:

- The original nine package files exist and are non-empty.
- `HIGH_REASONING_AUDIT.md` is the only newly added audit file relative to the initial nine-file inventory captured at audit start.
- All ten files are directly inside `PHASE 3/PHASE 3C-Comparative Technical Evaluation/FINAL_DOWNSELECTION/`.
- No tracked project file changed.
- `ZEROTH PRESENTATION/` remains unrelated and untouched.


---

## Source 10: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/09_Final_Downselection_README.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `e213c44f71348a07dfa2b0982d5944fa8d4458f4a118531fd8ade6f2bf6e09e2`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/09_Final_Downselection_README.md`
- Current SHA-256: `e213c44f71348a07dfa2b0982d5944fa8d4458f4a118531fd8ade6f2bf6e09e2`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC Final Down-Selection Evidence Package

## Purpose

This directory prepares repository-grounded evidence for the later final comparison of:

1. OpenBraille
2. VibeGuard
3. TrueMoist

It is an extraction and comparison-preparation package. It does not score, rank, recommend, eliminate, or select any concept. No winner has been selected. TrustLatch and ColdTrace are deferred and are not candidates.

## Workflow

1. Apply the authority policy below.
2. Read the neutral concept matrix and hard-gate precheck.
3. Resolve the uncertainty and test register where decision-critical.
4. Run a separate, current external patent-source verification pass using the patent research input pack.
5. Only then complete the blank scoring worksheet and the required rankings.
6. The future final report must name exactly one primary project, one runner-up, and one reserve.

## Authority policy

Conflicts are governed in this order: Engineering Design Review; Decision Register v1.2; approved portfolio closure memo; final Phase 3C architecture reports; final Phase 3C memories; Phase 3C SOPs; Phase 3B; Phase 3A; Phase 2; Phase 1C; raw independent research. Raw research, convenience copies, ZIP members, historical registers, failed research, and audit files cannot override current authoritative documents. Contradictions are recorded rather than silently reconciled.

## Files

- `README.md` — scope, workflow, authority policy, and directory index.
- `01_Comparison_Protocol.md` — hard gates, 100-point future rubric, scoring rules, and required later outputs.
- `02_Authoritative_Source_Manifest.md` — sources used, authority, status, scope, limitations, supersession, and exclusions.
- `03_Concept_Evidence_Matrix.md` — neutral side-by-side extraction with source locations, confidence, and conflicts.
- `04_Hard_Gate_Precheck.md` — repository-only G1–G7 precheck; it does not eliminate concepts.
- `05_Uncertainty_and_Test_Register.md` — unresolved technical and comparison questions with earliest resolving actions.
- `06_Patent_Research_Input_Pack.md` — neutral query and claim-element preparation for a later current patent search.
- `07_Scoring_Worksheet.md` — blank rubric worksheet; all score and ranking fields remain unfilled.
- `CODEX_EXTRACTION_VALIDATION.md` — inspection trail, safeguards, contradictions, unavailable evidence, and terminal checks.
- `HIGH_REASONING_AUDIT.md` — independent verification, minimal audit corrections, neutrality check, and patent-verification readiness verdict.
- `CODEX_SESSION_HANDOFF.md` — non-authoritative operational continuity file for resuming the work in a future Codex conversation.

## Patent warning

Repository patent findings are historical evidence, not current patent status, patentability, validity, claim scope, or freedom-to-operate conclusions. Any patent-dependent score or decision requires a current external pass against primary patent sources and, where appropriate, qualified legal review.


---

## Source 11: `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `02baa83e691bf88e5221e20ac92e5be94eb3c71280b48c8338a02401bb173c9f`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- Current SHA-256: `02baa83e691bf88e5221e20ac92e5be94eb3c71280b48c8338a02401bb173c9f`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

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


---

## Source 12: `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `29d0f85d95f7ef98d1a1a31a395cbbab5511ae25df2eeb15840978d7bfb3590e`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- Current SHA-256: `29d0f85d95f7ef98d1a1a31a395cbbab5511ae25df2eeb15840978d7bfb3590e`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC Final Cross-Concept Patent-Path Adjudication

**Evidence cut-off:** 1 August 2026
**Adjudication basis:** the 12-file blind package only
**Nature of output:** engineering and patent-strategy decision support; not legal advice, patentability clearance, claim construction, infringement analysis, or FTO clearance

## 1. Executive decision

### Required five decisions

1. **Best semester-build candidate: VibeGuard.** Its frozen Level-1 system has the strongest three-month feasibility, lowest cost, clearest live demonstration, and best fit for the team’s embedded/DSP strengths.
2. **Best post-MVP patent-development candidate: OpenBraille D11, conditionally.** The integrated mechanical-datum, per-dot calibration, isolated shared-current verification, physical-ground-truth, bounded-retry/fault-isolation and current-aware sequencing route is the most directly testable and physically anchored of the three later mechanisms. It is not presently established as patentable; the conservative synthesis correctly keeps it at Track D until the named gate passes, while the secondary synthesis supports only a bounded prospective Track B.
3. **Best overall Project mC action now: Run one named short feasibility gate before selecting.** Run the **OpenBraille D11 Physical-State Observability Gate** for **10 calendar days from formal start**. If it passes, select OpenBraille. If it fails, select VibeGuard immediately.
4. **Runner-up and fallback: VibeGuard.** It is the current integrated-score leader under all three weightings and the fallback because its semester success is much less dependent on unresolved mechanical or institutional facilities.
5. **Prototype/publication-only or deprioritized concept: TrueMoist.** Retain it as a rigorous measurement/publication project and later research option, but deprioritize it for the present patent-first selection because decisive transfer/validity proof needs more probes, lots, remounts and metrology than the semester package can support.

### Named gate

**Gate name:** OpenBraille D11 Physical-State Observability Gate
**Deadline:** day 10 after gate start
**Minimum setup:** one single-dot servo/cam/pin module; mechanical datum; three SG90-class servos; two reassemblies; current/voltage sensing; independent optical/mechanical ground truth; fixed-PWM and calibrated comparators.
**Pass threshold:**

- at least **95% sensitivity and 95% specificity** on untouched events for distinguishing completed raise/retract from induced jam/incomplete travel;
- **zero silently accepted wrong physical states in 500 held-out transitions**;
- calibrated datum-plus-verification control must reduce out-of-spec or failed transitions by at least **30% relative to fixed common-PWM control**;
- a current-only decision must not be accepted unless it agrees with physical ground truth; and
- committed spend must remain below ₹5,000 with no unsafe sustained stall.

**Fallback:** any pass element missed means select VibeGuard and retain OpenBraille only as an assistive prototype/publication track. Passing the gate does not prove patentability; it only authorizes selection and a claim-focused search/IPR review.

**Confidence:** medium. The current evidence favors VibeGuard numerically, but a low-cost, short OpenBraille gate can resolve the single uncertainty most capable of reversing a patent-first decision.

## 2. Input inventory and provenance

Exactly **12 physical Markdown attachments** were present. All were readable. Byte counts and SHA-256 hashes for files 00–10 matched the provenance register exactly; parenthetical upload suffixes are transport-name artifacts, not substantive versions.

| Controlled role | Attached file | Result |
|---|---|---|
| Governing instruction | `00_READ_FIRST_Project_mC_Final_Adjudication_Instructions(2).md` | Readable; 16,558 bytes; hash matched |
| Governance 1 | `01_Project_mC_Decision_Register_v1.2(2).md` | Readable; v1.2; hash matched |
| Governance 2 | `02_Phase3C_Portfolio_Closure_Memo_Approved(2).md` | Readable; hash matched |
| Common evidence 1 | `03_Concept_Evidence_Matrix(3).md` | Readable; hash matched |
| Common evidence 2 | `04_Uncertainty_and_Test_Register(2).md` | Readable; hash matched |
| OpenBraille 1 | `05_OpenBraille_Synthesis_Work_Max(2).md` | Complete; concept-faithful; hash matched |
| OpenBraille 2 | `06_OpenBraille_Synthesis_Valid_Secondary(2).md` | Complete; concept-faithful; hash matched |
| VibeGuard 1 | `07_VibeGuard_Synthesis_Work_Max(2).md` | Complete; concept-faithful; hash matched |
| VibeGuard 2 | `08_VibeGuard_Synthesis_Standard_High(2).md` | Complete; concept-faithful; hash matched |
| TrueMoist 1 | `09_TrueMoist_Synthesis_Max(2).md` | Complete; concept-faithful; hash matched |
| TrueMoist 2 | `10_TrueMoist_Synthesis_High_Deep_Research(2).md` | Complete; concept-faithful; hash matched |
| File control | `99_EXCLUSION_AND_PROVENANCE_REGISTER(2).md` | Readable; treated only as provenance/reliability context |

All ten requested control confirmations pass:

1. exactly 12 attachments;
2. governing instruction readable;
3. all four common governance/evidence files present;
4. exactly two valid synthesis reports for each concept;
5. OpenBraille filename crossing explicitly resolved;
6. failed moving-roller OpenBraille synthesis absent;
7. failed software-security VibeGuard synthesis absent;
8. supplementary TrueMoist Work Max web audit absent and not inferred;
9. Decision Register v1.2 present and v1.1 absent;
10. no selected synthesis missing, unreadable, duplicated, physically partial, or concept-swapped.

The crossing is not that the two attached reports describe two OpenBraille variants. The valid secondary originally carried `OpenBraille_Patent_Synthesis_ChatGPT_Standard_High_no_deeprsearch.md`; the file originally named `OpenBraille_Patent_Synthesis_ChatGPT_Deep_Research.md` was the excluded moving-roller concept swap.

## 3. Authority and constraints

Authority was applied in this order: Decision Register v1.2; approved closure memo; Concept Evidence Matrix; Uncertainty and Test Register; audited syntheses. The register confirms the retained portfolio is OpenBraille, VibeGuard and TrueMoist, and makes patent-development potential the primary selection priority while retaining feasibility, budget, demonstration and team fit as mandatory constraints.

Binding constraints used in scoring:

- up to three months;
- preferred budget ≤₹3,000 and hard ceiling ₹5,000;
- five members: three strong technical contributors, one learner, one presenter/support member;
- Arduino IDE/embedded-board compatibility;
- low-power components and USB interface/sample;
- strong live demonstration;
- no invented scope or unsupported patent certainty.

The closure memo’s descriptive starting point was preserved: OpenBraille has the highest long-term physical-invention ceiling, VibeGuard the strongest live embedded/DSP demonstration and team fit, and TrueMoist the lowest nominal electronics risk with a plausible compensation-method path. Those statements are starting evidence, not the final ranking.

## 4. Concept-fidelity audit

**OpenBraille — pass.** Both selected reports preserve a six-dot macro cell using six SG90-class servos, PWM, eccentric cams/followers and vertically translating pins. The later direction is D11-type verified refresh. No moving roller, encoder wheel, RAMPS/Mega or paper embosser entered the analysis.

**VibeGuard — pass.** Both reports preserve one rigidly mounted ADXL345-class sensor, ESP32 local processing, time features, triggered FFT, RMS-plus-persistence baseline, prospective Mahalanobis, RGB state and isolated-motor Level 1. Level 2 remains target attribution despite independent interference. No software scanner, wearable, active cancellation, array, cloud or RUL substitution was used.

**TrueMoist — pass.** Both reports preserve the validated 72-run, one-soil, analog-probe/DS18B20, controlled-salinity-code, ADC-gate, M0/M1/M2 fixed-offline-model architecture. No live EC, custom multi-frequency probe, irrigation control, cloud, TinyML, online learning or multi-soil MVP was imported.

## 5. Synthesis reliability audit

| Synthesis | Fidelity | Frozen-MVP verdict | Later-route verdict | Reliability | Adjudication treatment |
|---|---|---|---|---|---|
| OpenBraille Work Max | Pass | MVP is an engineering prototype, not a credible invention | D11 remains Track D; reopen B only after search and stringent data | **High** | Most conservative and claim-focused; transparent about unresolved Indian file, state observability and additive-effect risk |
| OpenBraille Valid Secondary | Pass | MVP not an invention | Bounded Track B for integrated tolerance compensation and verified refresh | **Medium** | Strong engineering definition, but its positive Track-B label rests on an unbuilt integration and proposed thresholds; treated as a hypothesis, not a conclusion |
| VibeGuard Work Max | Pass | Frozen stack is conventional | Track C target-attribution mechanism | **High** | Strong separation of Level 1 and Level 2, claim corrections and field-evidence burden; provisional status labels not treated as legal conclusions |
| VibeGuard Standard High | Pass | Frozen stack is research platform | Track C integrated commissioning/abstention/quarantine/remount method | **Medium** | Mechanism is specific and experiments well defined; proposed 30% threshold is a research recommendation, not authority; field transfer remains unproven |
| TrueMoist Max | Pass | Frozen 72-run stack is Track D as a patent direction | Track C composite replacement/remount transfer and validity path | **High** | Conservative treatment of close art and physical-sample burden; strongest on kill criteria and simple-baseline comparison |
| TrueMoist High + Deep Research | Pass | Frozen MVP conventional | Track C physical-reference-bound transfer/acceptance | **Medium** | Good claim-level framing; some legal-status statements remain provisional and the two-probe semester pilot cannot support population transfer |

### Resolution of the OpenBraille disagreement

The reports do not disagree about the frozen MVP: both reject it as the invention. They disagree about when the integrated D11 route deserves Track B. The secondary treats the specificity and three-month accessibility as sufficient for a provisional B; Work Max applies a stricter burden because current signatures may measure internal servo effort rather than tactile state, the individual elements are known, the Indian filing remains unresolved, and no non-additive effect exists yet.

This adjudication adopts **current Track D, prospective Track B only after the named gate and claim-focused review**. That preserves the secondary report’s bounded opportunity without converting an experiment plan into patent evidence.

## 6. Normalization method

Each concept was split into two independent objects:

- the frozen semester MVP actually authorized by project authority;
- the post-MVP invention-development mechanism, with its own hardware, evidence, time, cost and kill conditions.

Scores are 0–5 with low/base/high ranges. Low represents adverse but plausible execution; base represents the most supported current forecast; high represents favorable execution without assuming patent success. Weighted scores are converted to 100. Patent scores assess the later mechanism, not the frozen MVP.

## 7. OpenBraille frozen-MVP fact sheet

| Field | Finding |
|---|---|
| Exact architecture | One approximately 300%-scale six-dot Braille cell; ESP32-WROOM-32; six SG90-class servos; direct 50 Hz PWM; one eccentric cam/follower/sliding pin per dot; FDM frame/guides/cams; external 5 V/2 A supply and 1,000 µF rail capacitor; active cam retraction unless a real passive return is proven |
| Three-month deliverable | Functional macro cell accepting characters over USB/serial, mapping to six dots, refreshing patterns, measuring travel/repeatability/power and performing tactile evaluation |
| Budget | ₹2,060–₹2,850 frozen estimate; enhancement can bring total to roughly ₹2,910–₹4,700 |
| Validation | Single-dot-first; power and active-retraction tests; six-dot integration; ≤0.1 mm position variance over 100 cycles; ≥1,000 actuations; pre-approved tactile protocol; full character transitions |
| Primary engineering risk | FDM tolerance/friction, active retraction, pin-height consistency, wear and six-servo power transients |
| Current patent verdict | Exact narrow literal differences may exist, but the useful servo/cam/pin combination is predictable and crowded; do not file on the frozen MVP |
| Strongest prior art | Rotary raised surface/guided pins (`US8483018B2`); independently actuated tactile pins (`US20130017516A1`); modular stops/guides (`US8690576B2`, `US7410359B1`, `US12080182B2`); public servo/cam and micro-motor projects; unresolved Indian `5559/CHE/2014` |
| Eligibility/FTO | Physical hardware is generally eligible; novelty/obviousness are the main weakness. FTO unresolved, particularly the Indian filing and active modular/capture families |
| Demo value | Very high social-impact and physical-motion demonstration; tactile success must not be inferred from visual motion |
| Publication value | High for low-cost assistive prototyping, manufacturing reliability, negative current-signature results or calibrated-vs-open-loop benchmarking |
| Current Track | **D as patent direction; strong prototype** |

## 8. OpenBraille post-MVP patent-path fact sheet

| Field | Finding |
|---|---|
| Proposed mechanism | D11 integrated datum + per-dot operating windows + sequential isolated shared-current measurement + independent physical ground truth during development + bounded retry/fault isolation + current-aware sequencing |
| Relationship to MVP | Direct extension of the same servo, cam, pin, power and control errors; no actuator-family switch required |
| Closest patent/NPL art | Braille stops/guides/calibration; generic motor-current state and jam diagnostics; tactile movement sensing; ordinary servo calibration and staggered power control; public servo/cam mechanisms |
| Claimed physical effect | Fewer incomplete raises/retractions, out-of-spec pin heights, silent wrong states, stalls and brownouts than fixed common-PWM control; reliable fault reporting rather than command-assumed success |
| Required decisive experiments | Three servos, two reassemblies, labelled raise/retract/jam events, optical/mechanical ground truth, fixed-PWM/calibration/sensing/full-system baselines, 500-transition short gate then 3,000-transition confirmatory run and ablations |
| Additional hardware/cost | Shunt/current amplifier or sensor, spare servos, printed coupons, ground-truth fixture; roughly ₹500–₹1,400 incremental, total below ₹5,000 if controlled |
| Time | Initial feasibility 10 days; full semester evidence possible; practical-scale and multi-build proof another 4–9 months |
| Claim usefulness if successful | Potentially useful narrow hardware-control claim around verified refresh of heterogeneous low-cost actuator channels; broader “servo Braille” claims are not credible |
| Main risks | High obviousness; current may not reveal pin state; apparent benefit may be ordinary calibration/staggering; unresolved Indian/control claims; practical-scale transfer may fail |
| Strongest baseline | Fixed common PWM; per-dot calibration only; datum only; sensing only; fixed sequential actuation; direct per-dot sensor oracle |
| Kill condition | Failure of physical-state discrimination, any silent wrong state, no cooperative effect beyond components, dependence on hand-selected servo/build, unsafe stall, or closer claim |
| Prospective Track | **B only after gate; otherwise D/publication** |

## 9. VibeGuard frozen-MVP fact sheet

| Field | Finding |
|---|---|
| Exact architecture | One rigid ADXL345-class accelerometer over SPI to ESP32-WROOM-32/S3; local DC removal, Hann, RMS/peak/std/crest/kurtosis, RMS-plus-persistence baseline, triggered 256–1,024 FFT, band features/static subtraction, prospective Mahalanobis, RGB local state; isolated motor/fan eccentric-mass rig |
| Three-month deliverable | Stable acquisition, normal calibration, repeatable induced abnormal condition, local Normal/Abnormal indication, USB logs, resource measurements and quantitative Level-1 trials |
| Budget | ₹1,700–₹2,200; large headroom under ₹3,000 and ₹5,000; IIS3DWB excluded from MVP |
| Validation | Rigid mount and repeated rig sessions; stable eccentric-mass labels; RMS baseline then FFT/Mahalanobis comparators; owner-approved accuracy/false-alarm criteria; no Level-2 claim from target-only bench data |
| Primary engineering risk | Mount/coupling repeatability, sample integrity, threshold tuning and false confidence from overlapping windows rather than independent sessions |
| Current patent verdict | Commodity sensor + standard DSP/statistics + local alert is conventional and predictable; no Track A case |
| Strongest prior art | KCF spectral baseline/rebaselining, Mitsubishi/Valqua Mahalanobis vibration diagnosis, Rolls-Royce speed-frequency normal spaces, Tractian fingerprints/learning, bearing source-provenance and NPL single-sensor separation |
| Eligibility/FTO | Physical diagnostic context helps eligibility but generic scores remain vulnerable; FTO unresolved in US/India/China and across commercial portfolios |
| Demo value | Highest: immediate green/blue/red live response to a visible motor condition |
| Publication value | High for embedded benchmark, mount effects, triggered-vs-continuous DSP, false-alarm analysis and mixed-vibration datasets |
| Current Track | **C for patent path; strong Level-1 prototype** |

## 10. VibeGuard post-MVP patent-path fact sheet

| Field | Finding |
|---|---|
| Proposed mechanism | Known-state commissioning of target/interferer states; target-conditioned fingerprint; source/mount validity estimate; Normal/Target-abnormal/Unknown decision; candidate-buffer quarantine; guarded baseline promotion; contamination lockout; remount invalidation/transfer; local resource-constrained execution |
| Relationship to MVP | Same one target-mounted sensor and ESP32; adds controlled interference experiments, labels and state-management logic |
| Closest patent/NPL art | Rolls-Royce speed-conditioned fingerprints; Mitsubishi/Valqua normal-space scoring; KCF baseline subtraction/rebaselining; Tractian fingerprints; generic abstention/drift adaptation; mounting standards/studies; single-sensor separation literature |
| Claimed physical effect | Lower wrong-source target alarms and baseline contamination under neighbour changes, without materially increasing missed target faults; reliable invalidation after remount |
| Required experiments | Dual-motor mechanically coupled rig; target normal/abnormal × interferer off/normal/abnormal; ≥2 operating regimes; ≥3 remounts; ≥5 independent sessions; held-out day/remount; mandatory baselines and ablations; later real or field-like site |
| Additional hardware/cost | Second motor/interferer, fixtures and temporary ground-truth tachometer/reference sensor; semester pilot may fit under ₹5,000, but decisive field/site work has no defensible student-budget estimate |
| Time | Preliminary Level 2A in semester; decisive Level 2B approximately one additional semester and dependent on site access |
| Claim usefulness if successful | Narrow but potentially useful source-attribution/update-control claim for a single mounted node; broad vibration-monitoring/statistical claims are unavailable |
| Main risks | High obviousness; generic software/statistics center; field labels unavailable; abstention hides errors; remount/speed confounding; active portfolios need claim charts |
| Strongest baseline | RMS+persistence; ordinary FFT/bands; ordinary Mahalanobis; static subtraction; naive adaptive baseline; full recalibration after remount |
| Kill condition | No held-out attribution gain; excessive abstention; contamination admitted; no cooperative effect; remount failure; field labels unavailable; embedded/resource failure; closer claim |
| Prospective Track | **C** |

## 11. TrueMoist frozen-MVP fact sheet

| Field | Finding |
|---|---|
| Exact architecture | Genuine analog capacitive probe plus nearby DS18B20; ESP32; ADS1115 retained only if paired gate justifies it; controlled NaCl treatment code, not measured EC; hardened analog path; M0/M1/M2 offline training and fixed local inference; one homogeneous soil; 4×3×2×3 = 72 independent physical runs; dry-basis gravimetric truth |
| Three-month deliverable | Complete early gates, collect 72 runs, hold replicate 3 untouched, deploy selected fixed model to ESP32, show raw/reference/compensated values and absolute errors over USB/CSV |
| Budget | ₹1,790–₹3,440 with institutional oven/scale access; below ₹5,000 with optional scale/contingency; oven purchase out of scope |
| Validation | Probe monotonicity/reinsertion; packing jig; ADC comparison; salinity pilot; oven/scale access; 72-run throughput; held-out RMSE ≥20% and MAE ≥15% improvement over M0; no major subset >10% MAE worsening |
| Primary engineering risk | Physical workload and traceable ground truth: packing/insertion, oven capacity, equilibration, dry-mass workflow and schedule |
| Current patent verdict | The exact factorial is rigorous evidence generation, not invention; temperature/salinity metadata plus ordinary regression and fixed MCU inference are predictable |
| Strongest prior art | TCS low-cost sensor health/replacement; CN replacement-probe equivalence; event recalibration/confidence; preset correction identifiers; nonlinear temperature compensation; calibration fixtures; incumbent capacitive/salinity hardware |
| Eligibility/FTO | Generic regression, confidence and metadata are weak eligibility centers; live claims/status unresolved in several jurisdictions; no “clear FTO” conclusion |
| Demo value | Good scientific before/after accuracy display, but less immediately dramatic and dependent on a long experiment completed beforehand |
| Publication value | Highest: controlled compensation, measurement uncertainty, pseudoreplication avoidance, ADC comparison and negative transfer/remount evidence |
| Current Track | **D as frozen patent direction; C only for later robustness/transfer** |

## 12. TrueMoist post-MVP patent-path fact sheet

| Field | Finding |
|---|---|
| Proposed mechanism | Coefficient/provenance binding to probe/setup; defined physical reference challenge after replacement/remount; disturbance-residual validity envelope; accept bounded transfer only when valid; quarantine contaminated recalibration; abstain/fallback when validity fails |
| Relationship to MVP | Uses the same commodity probe, temperature/salinity disturbance model, gravimetric discipline and ESP32; expands from compensation to transfer/validity |
| Closest patent/NPL art | CN replacement-probe reference conditioning; TCS calibration/health/replacement; self-learning wet/dry bounds; event recalibration/confidence/exclusion; preset correction; calibration fixtures; generic OOD/statistical validity |
| Claimed physical effect | Reduce severe accepted errors and calibration workload when replacing/remounting cheap probes, while rejecting contaminated or invalid transfer states |
| Required experiments | Donor/replacement transfer; naive reuse, one-point, two-point affine, pooled and full-oracle baselines; remount/packing/temp/salt/electronic-offset challenges; clean/contaminated events; 6–12 probes, ≥2 lots and ≥3 batches for credible later proof |
| Additional hardware/cost | Existing second probe supports only pilot; later proof needs 6–12 probes, lots, containers, repeated gravimetric work and possibly institutional support beyond ₹5,000 |
| Time | Two-probe pilot in semester; credible proof one additional semester or more |
| Claim usefulness if successful | Narrow transfer/validity claim for commodity probes; broad calibration, replacement, confidence or event-recalibration claims are crowded |
| Main risks | Closest art is directly on replacement equivalence and sensor health; simple two-point affine transfer/range gate may explain result; population support weak; high experimental burden |
| Strongest baseline | Naive coefficient reuse; one-point; two-point affine; pooled model; full per-probe oracle; min/max/range gate; generic Mahalanobis or prediction interval |
| Kill condition | No advantage over two-point affine plus generic gate; false-valid reduction requires unusable abstention; no multi-unit/lot reproducibility; contamination gate fails; Level-1 metrology fails |
| Prospective Track | **C** |

## 13. Semester-build scoring matrix

| Factor | Weight | OpenBraille low/base/high | VibeGuard low/base/high | TrueMoist low/base/high |
|---|---:|---:|---:|---:|
| Build feasibility within three months | 25% | 2.4/3.3/4.0 | 3.9/4.5/4.9 | 3.0/3.8/4.4 |
| Measurement/validation feasibility | 20% | 1.8/2.6/3.3 | 3.5/4.2/4.7 | 2.0/3.1/4.0 |
| Budget compliance | 15% | 4.0/4.5/4.8 | 4.4/4.8/5.0 | 3.3/4.1/4.7 |
| Live demonstration clarity | 15% | 4.1/4.6/5.0 | 4.4/4.8/5.0 | 3.0/3.6/4.2 |
| Schedule and dependency risk | 10% | 2.0/2.8/3.5 | 3.4/4.1/4.6 | 1.8/2.8/3.8 |
| Team fit and task divisibility | 10% | 3.0/3.6/4.2 | 4.2/4.7/5.0 | 3.5/4.0/4.5 |
| Publication/educational fallback | 5% | 3.8/4.3/4.8 | 4.0/4.5/4.9 | 4.5/4.9/5.0 |

### Weighted semester-build totals

| Concept | Low | Base | High |
|---|---:|---:|---:|
| OpenBraille | 57.3 | **71.3** | 82.8 |
| VibeGuard | 79.1 | **90.2** | 97.4 |
| TrueMoist | 57.0 | **73.0** | 86.3 |

**Why material differences exist:** VibeGuard exceeds OpenBraille by more than one point on build feasibility, validation and team fit because its Level-1 rig has fewer coupled mechanical parts, no human tactile dependency and matches the team’s embedded/DSP strengths. VibeGuard exceeds TrueMoist by more than one point on validation, demonstration and schedule because TrueMoist’s authoritative output depends on 72 independent physical runs and institutional gravimetric facilities. TrueMoist exceeds OpenBraille on team/process divisibility and scientific fallback, while OpenBraille exceeds TrueMoist on live demonstration clarity.

## 14. Patent-path scoring matrix

| Factor | Weight | OpenBraille low/base/high | VibeGuard low/base/high | TrueMoist low/base/high |
|---|---:|---:|---:|---:|
| Distance from closest prior art | 20% | 1.5/2.5/3.4 | 1.8/2.7/3.5 | 1.3/2.1/3.0 |
| Specificity of proposed mechanism | 15% | 4.0/4.6/4.9 | 4.2/4.7/5.0 | 4.0/4.5/4.9 |
| Inventive-step resistance | 15% | 1.2/2.3/3.3 | 1.5/2.5/3.4 | 1.2/2.1/3.0 |
| Accessibility of decisive experiments | 15% | 3.5/4.4/4.8 | 1.7/2.6/3.6 | 1.5/2.5/3.5 |
| Usefulness/breadth of plausible claim | 10% | 2.0/3.2/4.0 | 2.3/3.3/4.0 | 1.8/2.8/3.6 |
| FTO/design-around posture | 10% | 1.6/2.6/3.5 | 1.8/2.7/3.5 | 1.5/2.3/3.2 |
| Direct connectedness to semester MVP | 10% | 4.6/4.9/5.0 | 4.4/4.7/5.0 | 4.2/4.5/4.9 |
| Publication value if patentability fails | 5% | 4.0/4.5/4.9 | 4.5/4.9/5.0 | 4.7/5.0/5.0 |

### Weighted patent-path totals

| Concept | Low | Base | High |
|---|---:|---:|---:|
| OpenBraille | 52.5 | **69.8** | 82.5 |
| VibeGuard | 50.9 | **66.5** | 80.0 |
| TrueMoist | 45.0 | **59.9** | 74.6 |

OpenBraille leads the base patent-path score because its mechanism is physically specific, almost perfectly connected to the MVP and can be falsified cheaply. This is not a finding that its prior-art position is better; its obviousness and FTO scores remain weak. VibeGuard’s mechanism is equally specific but decisive evidence requires independent interference labels and field-like validation. TrueMoist’s mechanism is specific, but the closest art is more directly aimed at replacement transfer, calibration and sensor health, and its proof requires a larger physical population.

## 15. Integrated-score sensitivity analysis

| Weighting | OpenBraille | VibeGuard | TrueMoist | Winner |
|---|---:|---:|---:|---|
| 40% build / 60% patent | 70.4 | **76.0** | 65.1 | VibeGuard |
| 50% build / 50% patent | 70.5 | **78.3** | 66.5 | VibeGuard |
| 30% build / 70% patent | 70.2 | **73.6** | 63.8 | VibeGuard |

The current score winner is **VibeGuard under every weighting**, so the numerical result is stable. The single assumption most capable of reversing the decision is whether OpenBraille can obtain reliable physical-state observability and a cooperative effect from D11 rather than ordinary calibration plus staggering. Because that assumption is inexpensive to test, a 10-day gate is more rational than either ignoring OpenBraille’s physical-invention upside or immediately committing the semester to its higher mechanical risk.

## 16. OpenBraille versus VibeGuard

- **Stronger semester build:** VibeGuard, by a large margin.
- **Stronger later technical mechanism:** OpenBraille if D11 passes; otherwise VibeGuard.
- **Closer/more damaging prior art:** OpenBraille’s physical elements are heavily crowded and the Indian filing is unresolved; VibeGuard’s statistical sub-elements are also crowded. OpenBraille has the more direct mechanism overlap, while VibeGuard has the more generic-software obviousness problem.
- **More expensive/longer evidence:** VibeGuard for decisive field attribution; OpenBraille’s first decisive experiment is cheaper.
- **Higher chance of a narrow useful claim:** OpenBraille conditional on verified state and synergy; VibeGuard if field attribution is real and reproducible.
- **Clearer kill experiment:** OpenBraille D11 physical-state gate.
- **Better publication fallback:** VibeGuard slightly, because a mixed-vibration benchmark and embedded results have broad technical value; OpenBraille has stronger social-impact value.
- **Reversal fact:** reliable D11 state verification and non-additive error reduction would move OpenBraille ahead; failure makes VibeGuard decisively preferable.

## 17. OpenBraille versus TrueMoist

- **Stronger semester build:** TrueMoist has lower mechanical complexity, but OpenBraille has the clearer live demo; base semester totals are close, with TrueMoist slightly higher.
- **Stronger later technical mechanism:** OpenBraille D11 because the decisive interaction can be tested with existing hardware and is more physically coupled.
- **Closer/more damaging prior art:** TrueMoist has especially close replacement-equivalence, event-calibration and sensor-health art; OpenBraille has dense actuator/guide/calibration art.
- **More expensive/longer evidence:** TrueMoist, due to 6–12 probes, lots and gravimetric physical challenges.
- **Higher chance of narrow useful claim:** OpenBraille, conditional on gate.
- **Clearer kill experiment:** OpenBraille.
- **Better publication fallback:** TrueMoist.
- **Reversal fact:** if OpenBraille current sensing cannot correlate with physical state, TrueMoist becomes the more defensible research programme, though not the preferred patent-first choice.

## 18. VibeGuard versus TrueMoist

- **Stronger semester build:** VibeGuard.
- **Stronger later technical mechanism:** VibeGuard, because source attribution plus guarded learning addresses a distinct diagnostic failure; TrueMoist is closer to known transfer/calibration practice.
- **Closer/more damaging prior art:** TrueMoist.
- **More expensive/longer evidence:** Both need later work; VibeGuard depends on a site, TrueMoist on many probes/lots and repeated metrology. Site access makes VibeGuard less controllable, while TrueMoist is more labor intensive.
- **Higher chance of narrow useful claim:** VibeGuard.
- **Clearer kill experiment:** TrueMoist’s two-point-affine-plus-range-gate comparator is clearer; VibeGuard’s field truth is harder.
- **Better publication fallback:** TrueMoist slightly for rigorous measurement science; VibeGuard for embedded/DSP relevance.
- **Reversal fact:** inability to obtain independent target/interferer labels would collapse VibeGuard’s Track C route and make TrueMoist the better later research option.

## 19. Novelty comparison

None of the frozen MVPs has a credible broad novelty nucleus. OpenBraille may avoid single-reference anticipation only through arbitrary exact details; VibeGuard’s feature stack is conventional; TrueMoist’s exact 72-run design is methodologically specific but not an invention.

For later paths, no reviewed source was shown to recite every element of D11, the VibeGuard integrated attribution/update sequence, or the TrueMoist composite transfer/validity sequence. That absence is not proof of novelty. Relative novelty risk is lowest for the exact VibeGuard and OpenBraille integrations, and highest for TrueMoist because replacement-reference and confidence/event-calibration art is particularly close.

## 20. Inventive-step/obviousness comparison

**OpenBraille:** high risk because stops, calibration, current diagnostics, retries and sequencing are individually familiar. The only defensible answer is a measured cooperative effect—physical state verification and fewer silent tactile errors that cannot be explained by ordinary tuning.

**VibeGuard:** high risk because known-state calibration, abstention, guarded updates, drift management and remount checks are familiar. Inventive step requires a source-specific coupling between ambiguity, decision, baseline promotion and mount validity that materially reduces wrong-source alarms.

**TrueMoist:** highest risk because one-/two-point calibration, reference challenges, replacement equivalence, confidence/exclusion and event recalibration are close art. A useful claim requires more than relabelling generic transfer and gating.

## 21. Patent-eligibility comparison

OpenBraille has the best eligibility posture because the center is an electromechanical tactile mechanism with measured physical states. VibeGuard and TrueMoist can also be framed as sensor-measurement improvements, but claims centered on Mahalanobis, confidence, abstention, regression, metadata or generic updates face greater US abstract-idea, EPO technical-contribution and Indian section 3(k) risk. Eligibility is not the primary weakness for any concept; novelty, inventive step and support dominate.

## 22. FTO and design-around comparison

No concept is FTO-cleared.

- **OpenBraille:** design away from active electromagnetic/capture-layer structures and generic modular claims; retrieve and chart `5559/CHE/2014`; avoid assuming expired art is a block while retaining it as prior art.
- **VibeGuard:** avoid exact Mitsubishi amplitude/phase Mahalanobis, Valqua dual-distance prognosis, Rolls-Royce speed-frequency noise-floor and Tractian remote reconstruction/retraining sequences; commercial portfolio coverage remains incomplete.
- **TrueMoist:** avoid CN replacement-output-equivalence conditioning, TCS image/rugged-reference health pipeline, claimed event recalibration and custom multi-frequency/live-salinity structures; official IN/CN/EP status requires counsel-grade review.

OpenBraille and VibeGuard have comparable unresolved posture; TrueMoist has the most directly relevant active-family risk for its proposed later center.

## 23. Evidence accessibility and experimental burden

1. **OpenBraille:** easiest decisive patent experiment. One-dot hardware, spare servos and ground truth can falsify the route quickly. Practical-scale proof remains later.
2. **VibeGuard:** easiest semester MVP but harder decisive patent evidence. A dual rig is manageable, yet real attribution requires independent labels, remounts and a field-like site.
3. **TrueMoist:** evidence is controllable but labor intensive. The semester can produce Level-1 data and a two-probe pilot; credible transfer needs a probe population and lots.

## 24. Claim usefulness and narrowness risk

- **OpenBraille:** a surviving claim could be narrow but commercially meaningful if it covers reliable refresh of heterogeneous low-cost actuator channels without per-dot position sensors. Narrowness risk: medium-high.
- **VibeGuard:** a claim coupling ambiguity, quarantine, remount validity and source attribution could be useful for one-node deployments. It may become a narrow protocol tied to labelled commissioning. Narrowness risk: high.
- **TrueMoist:** a claim may narrow to a specific reference challenge, transfer mapping and contamination gate for a probe class. Close art may force highly specific physical conditions. Narrowness risk: very high.

## 25. Optimistic/base/pessimistic simulation

These are conditional decision-support bands, not legal probabilities.

| Concept | Optimistic case | Base case | Pessimistic case |
|---|---|---|---|
| OpenBraille | **25–40%** chance the D11 evidence becomes counsel-worthy: state inference is reliable, full integration beats ablations, practical-scale relationship survives and search leaves useful scope | **10–25%**: engineering reliability improves, but claim scope is narrow or obviousness remains difficult | **<10%**: current measures servo effort rather than pin state, simple calibration explains benefit, or closer claims defeat route |
| VibeGuard | **20–35%**: controlled and field-like data show materially lower wrong-source alarms at useful coverage, with remount-safe update control | **10–20%**: strong publication result and prototype, but field evidence or obviousness prevents filing-quality claim | **<10%**: neighbour and mount variation swamp target information, abstention hides errors, or independent labels/site access fail |
| TrueMoist | **15–30%**: multi-unit/lots show transfer and validity benefit beyond two-point affine plus generic gate | **5–15%**: Level-1 paper succeeds, but transfer path remains conventional or too narrow | **<5%**: metrology/packing fails, simple baselines match, or close art leaves no useful scope |

## 26. Kill-probability and decision-reversal analysis

| Concept | Estimated patent-path kill probability | Risk surviving claim is commercially too narrow | Primary reversal variable |
|---|---:|---:|---|
| OpenBraille | **60–75%** | **55–75%** | Whether current-plus-datum can verify actual pin state and produce a cooperative effect |
| VibeGuard | **65–80%** | **60–80%** | Whether target-specific information survives independently varying interference and remounts |
| TrueMoist | **75–90%** | **70–85%** | Whether the full mechanism beats two-point affine transfer plus generic validity gating across units/lots |

The overall decision reverses to immediate VibeGuard if OpenBraille misses any gate threshold. It reverses toward OpenBraille if the gate passes strongly and a rapid claim-focused search finds no close integrated claim. TrueMoist becomes fallback research only if VibeGuard cannot obtain labels/site access and OpenBraille fails mechanically.

## 27. Best semester-build candidate

**VibeGuard.** Base Semester Build Score: **90.2/100**. It is inexpensive, visually clear, technically divisible and can meet its legitimate Level-1 scope without a large mechanical tolerance stack, human tactile access or an oven-based 72-run campaign. The team must pre-register quantitative success criteria and not present Level 1 as target attribution.

## 28. Best post-MVP patent-development candidate

**OpenBraille D11, conditionally.** Base Patent-Path Score: **69.8/100**, versus VibeGuard 66.5 and TrueMoist 59.9. Its advantage is not prior-art distance; it is specificity, direct MVP connection and accessibility of decisive experiments. Current classification remains Track D until the gate passes, then prospective Track B subject to search/IPR review.

## 29. Best overall Project mC choice

**Run one named short feasibility gate before selecting.** The current integrated-score leader is VibeGuard, but the gate can resolve OpenBraille’s strategically decisive uncertainty in 10 days for modest cost. This is preferable to selecting OpenBraille on speculation or selecting VibeGuard without testing the only near-term physical invention route.

## 30. Runner-up and deprioritized concept

**Runner-up/fallback:** VibeGuard. Select it immediately if the OpenBraille gate fails.
**Deprioritized for patent-first selection:** TrueMoist. Preserve all Level-1 plans and consider it for a rigorous publication or later institutional research study.

## 31. First 12-week execution plan

### Days 1–10: selection gate

- Freeze public baseline descriptions and open confidential invention logs.
- Build the OpenBraille one-dot gate setup; use three servos and two reassemblies.
- Lock thresholds before held-out data.
- Day 10 decision: pass → OpenBraille; fail → VibeGuard.

### Weeks 3–4: procurement and architecture freeze

**If OpenBraille selected:** procure six servos, power rail, FDM materials and instrumentation; freeze active retraction, datum geometry and safety limits.
**If VibeGuard selected:** procure authentic ADXL345/ESP32, motor/rig materials, rigid bracket and wiring; freeze ODR/bandwidth after measured signal review.

Team allocation for either path:

- technical lead: architecture, safety and integration;
- firmware/data lead: acquisition/control, immutable logs and analysis;
- mechanical/rig lead: fixtures, repeatability and ground truth;
- learner: scripted tests, labels, inventory and repeat runs;
- presenter/support: public-safe demo, source ledger and version control.

### Weeks 5–6: minimum demonstrable system

- OpenBraille: full six-dot macro cell, fixed-PWM baseline, power and travel measurements.
- VibeGuard: stable Level-1 acquisition, repeatable normal/abnormal rig and RMS+persistence baseline.

### Weeks 7–8: quantitative validation

- Lock evaluation protocol and held-out runs.
- OpenBraille: calibration/datum/current verification plus fixed and partial baselines.
- VibeGuard: time/FFT/Mahalanobis baselines, mount repeats and resource profiling.

### Weeks 9–10: robustness and ablation

- OpenBraille: induced jams, replacements, reassembly, all pattern transitions, 1,000-cycle screening.
- VibeGuard: add controlled interferer only if Level 1 is stable; quantify neighbour confusion and test preliminary Unknown/quarantine logic.

### Weeks 11–12: demo, decision and documentation

- Freeze firmware, BOM, schematics/CAD, SOP, raw data and negative results.
- Prepare a public demo containing only frozen architecture and generic known techniques.
- Hold institutional IPR review before disclosing exact later mechanism, thresholds or results.
- Decide filing-search continuation versus publication-only route.

## 32. Later invention-development plan

**OpenBraille after a pass:** 3,000–10,000 transition confirmatory dataset; full ablations; practical-scale single-dot coupons; three independent builds; multiple actuator lots; contamination/load/temperature testing; claim-focused search including Indian file; later six-dot practical geometry and approved Braille-reader evaluation.

**VibeGuard fallback/later path:** dual-rig randomized states; at least three remounts and five sessions; held-out day/remount; strongest baselines and ablations; real or field-like site with independent labels; counsel-grade search on exact update/abstention/remount sequence.

**TrueMoist retained research:** complete Level 1 first; then 6–12 probes, ≥2 lots, ≥3 preparation batches, repeated remounts, contamination and ageing proxies, full transfer baselines and later soil classes. Do not add live EC or multi-frequency hardware merely to rescue patent scoring.

For any selected path: refresh prior art only after the mechanism is frozen; prepare a human-authored invention disclosure; identify target jurisdictions; obtain institutional ownership/inventorship review; then commission professional novelty/FTO work and make a filing/no-filing decision. If filing is not justified, preserve a publication-quality dataset and negative results.

## 33. Confidentiality and institutional IPR plan

Publicly discuss only the frozen architecture, generic known algorithms, course requirements and high-level test goals. Keep confidential:

- exact OpenBraille datum geometry, signatures, retry/fault logic, thresholds and ablations;
- VibeGuard attribution, source-confidence, quarantine/promotion, remount and abstention logic;
- TrueMoist physical reference challenges, transfer mappings, contamination gates and validity states;
- unpublished data, negative results, parameter values and contributor chronology.

Maintain dated lab notebooks, Git commit history, CAD revisions, raw-data hashes, decision logs and contributor statements. AI suggestions are not inventorship. Human contributors must identify who conceived each claim-relevant element and who reduced it to practice. Obtain institutional approval before poster, repository, paper, video or competition disclosure.

## 34. Final recommendation

**Run the OpenBraille D11 Physical-State Observability Gate before selecting.**
**Current OpenBraille MVP Track:** D as a patent direction; strong semester prototype.
**Prospective later Track:** B only if the 10-day gate passes and claim-focused/IPR review preserves a meaningful distinction.
**Confidence:** medium.
**Primary kill condition:** inability to verify actual pin state with ≥95% sensitivity/specificity and zero silent wrong states in 500 held-out transitions, or failure to outperform fixed-PWM control by ≥30%.
**Fallback:** select VibeGuard, current Track C, and execute a disciplined Level-1 build while retaining source-attribution work as later research.
**Deprioritized concept:** TrueMoist for patent-first selection; retain for Level-1 engineering/publication.

No project or enhancement is represented as certain to receive a patent.

## 35. Unresolved questions

1. Can the OpenBraille current measurement distinguish actual tactile pin contact/state from internal servo effort across units, reassembly, voltage and wear?
2. What official file, claim scope and current legal status apply to Indian application `5559/CHE/2014`?
3. What owner-approved quantitative tactile-identification threshold and participant protocol will govern OpenBraille?
4. What owner-approved Level-1 accuracy/false-alarm criteria will govern VibeGuard?
5. Can VibeGuard obtain safe independent target/interferer labels and a field-like site within the later programme?
6. Is oven/scale access guaranteed for the full TrueMoist schedule, and can measured throughput support 72 independent runs?
7. Which jurisdictions and commercialization acts define the eventual FTO search?
8. Which exact human contributions, if any, survive the experiments as claim-relevant inventive concepts?

## 36. Source and verification log

### Governing and common authority

- `00_READ_FIRST_Project_mC_Final_Adjudication_Instructions(2).md`
- `01_Project_mC_Decision_Register_v1.2(2).md`
- `02_Phase3C_Portfolio_Closure_Memo_Approved(2).md`
- `03_Concept_Evidence_Matrix(3).md`
- `04_Uncertainty_and_Test_Register(2).md`

### Selected analytical evidence

- `05_OpenBraille_Synthesis_Work_Max(2).md`
- `06_OpenBraille_Synthesis_Valid_Secondary(2).md`
- `07_VibeGuard_Synthesis_Work_Max(2).md`
- `08_VibeGuard_Synthesis_Standard_High(2).md`
- `09_TrueMoist_Synthesis_Max(2).md`
- `10_TrueMoist_Synthesis_High_Deep_Research(2).md`

### File-control-only context

- `99_EXCLUSION_AND_PROVENANCE_REGISTER(2).md`

### Verification performed

- physical attachment count and readability;
- byte and SHA-256 verification against the provenance register for controlled files 00–10;
- heading/completeness audit of all six selected syntheses;
- explicit concept-fidelity review;
- reconciliation of the OpenBraille Track D/B disagreement without voting;
- weighted score calculation and sensitivity analysis;
- no excluded synthesis, supplementary TrueMoist audit, prior-chat context or prior adjudication output used.

No independent web result was needed to convert an unresolved status into a factual conclusion. Where the attached syntheses could not establish official legal status or claim scope, the issue remains expressly unresolved rather than guessed.


---

## Source 13: `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `aebf3926dda0cb7dca568e8e0c54dbf4679550c3c3e50c1fd05c94ac5b0810f9`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.docx`
- Current SHA-256: `aebf3926dda0cb7dca568e8e0c54dbf4679550c3c3e50c1fd05c94ac5b0810f9`
- Extraction method: `DOCX_XML`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

PROJECT mC

REQUEST FOR APPROVAL TO CHANGE THE SEMESTER PROJECT

From OpenBraille to VibeGuard

Course

PBCST504 - Microcontrollers Micro Project

Programme

B.Tech Computer Science and Engineering (Cyber Security)

Group

Group 8

Project Coordinator

Ms. Sagna L T, Assistant Professor, CSE (CY)

Date

03 August 2026

Decision requested

Approve the team's change from the frozen OpenBraille semester architecture to the frozen VibeGuard Level-1 architecture, while retaining OpenBraille as documented accessibility/mechatronics work and a possible future research project.

1. Formal request

To: Ms. Sagna L T, Project Coordinator

Subject: Request to approve VibeGuard as the Group 8 semester implementation

The team respectfully requests permission to change the semester implementation from OpenBraille, which was presented during the zeroth review, to VibeGuard. OpenBraille was selected for the zeroth review while the planned comparative engineering, budget, validation and future-research assessment was still incomplete. That assessment has now been completed. It retains OpenBraille as a valuable accessibility project, but identifies VibeGuard as the lower-risk and better-aligned semester build.

2. Executive decision summary

VibeGuard provides the strongest probability of completing a stable, measurable and demonstrable system within the semester.

Its expected hardware budget is approximately ₹2,200, with a protected conservative envelope of approximately ₹3,900.

Its main work aligns with ESP32 programming, embedded acquisition, signal processing, USB logging and quantitative testing - areas that match the team better than repeated precision mechanical fabrication.

The requested switch is not based on a promise of patent grant. The ordinary VibeGuard semester MVP is treated as conventional.

OpenBraille work will be preserved as a complete documented concept and may continue later as an accessibility/mechatronics research direction.

3. Why the zeroth-review choice is changing

The zeroth-review presentation correctly described OpenBraille as an affordable, macro-scale, single-cell Braille prototype using six low-cost servos and eccentric cams. The later review did not show that this was a poor idea. It showed that the two projects carry different kinds of semester risk.

Concept

Main semester risk

OpenBraille

Mechanical iteration risk: guide friction, cam alignment, pin travel, active retraction, six-servo current demand, wear and tactile-state confirmation.

VibeGuard

Data-validity risk: sensor authenticity, rigid mounting, repeatable fault injection, stable sampling, threshold selection and held-out validation.

For this five-member CSE (Cyber Security) team, VibeGuard's risks are easier to isolate through scripted experiments and logs. OpenBraille can succeed, but a mechanical redesign can restart CAD, printing, assembly and power testing. VibeGuard allows faster recovery because the sensor, controller, rig, firmware and analysis can be tested as separate subsystems.

4. Frozen semester architectures

4.1 Proposed VibeGuard build

One rigidly mounted ADXL345-class tri-axis accelerometer connected to an ESP32 over SPI.

Continuous time-domain features, with RMS plus persistence as the minimum classifier.

Triggered FFT and selected frequency-band features for explanation and comparison.

Optional ordinary Mahalanobis anomaly score only as a comparative method.

Local RGB indication and USB data logging.

A guarded low-voltage motor/fan rig with controlled normal and induced-abnormal vibration states.

No cloud dependence, permanent second sensor, source-separation array, active cancellation or remaining-useful-life claim.

4.2 Retained OpenBraille definition

One macro-scale six-dot cell with six SG90-class servos, six eccentric cams, followers and guided vertical pins.

ESP32 direct PWM control, external regulated servo power and USB/serial character input.

Active servo-driven retraction unless a real passive return is experimentally proved.

No moving roller, encoder wheel, RAMPS/Mega embosser, continuous-paper system or electromagnetic substitution.

Architecture-control statement

The requested change selects one semester implementation. It does not merge the two concepts, rewrite either frozen architecture or claim that later research features have already been built.

5. Comparative semester decision

Criterion

VibeGuard

OpenBraille

Finding

Build complexity

Low-to-moderate electronics, firmware and test-rig work

High mechanical integration across six channels

VibeGuard

Expected cost

About ₹2,200

About ₹3,000

VibeGuard

Conservative envelope

About ₹3,900

About ₹4,900

VibeGuard

Team alignment

Strong: ESP32, firmware, DSP, data and testing

Requires sustained CAD/FDM/mechanical tuning

VibeGuard

Validation

Repeated labelled sessions and held-out tests

Metrology, cycling, tactile distinction and power tests

VibeGuard

Live demonstration

Motor-state change, RGB and live logs/features

High social impact if mechanics remain reliable

Both strong; VibeGuard safer

Schedule recovery

Subsystems can be replaced independently

Mechanical revision can restart multiple stages

VibeGuard

Semester patent position

Conventional MVP; no filing claim

Conventional MVP; no filing claim

Equal

6. Proposed VibeGuard semester scope

6.1 Minimum demonstrable success

Acquire stable vibration data from the controlled rig using the target-mounted sensor.

Establish a repeatable normal operating condition.

Create a safe and repeatable induced-abnormal condition.

Classify the two states locally with RMS plus persistence as the minimum baseline.

Provide an interpretable RGB indication and USB evidence.

Report repeatability, false alerts, missed detections, resource use and limitations on held-out sessions.

6.2 Budget summary

Layer

Planning value

ESP32 development board

₹400 expected; ESP32-S3 only as an authorized fallback

ADXL345 breakout

₹229 expected; provenance and bench acceptance required

Low-voltage motor and adapter

Approximately ₹355 expected

Rigid base, sensor bracket, shaft guard and abnormality fixture

Approximately ₹500 expected planning allowance

Perfboard, indicators, connectors and passives

Approximately ₹400 expected

Delivery/replacement allowance

Approximately ₹300

Expected planning total

Approximately ₹2,200

Protected conservative envelope

Approximately ₹3,900; below the ₹5,000 ceiling

6.3 Twelve-week roadmap

Week

Primary milestone

1

Approval, scope freeze, safety review, procurement

2

ESP32 and ADXL345 acceptance; motor and mount inspection

3

Stable SPI acquisition, timestamps and dropped-block counters

4

Rigid mounting and repeated normal sessions

5

Safe induced-abnormal fixture and repeated abnormal sessions

6

RMS plus persistence, RGB output and USB logging

7

Triggered FFT/bands and ordinary comparator

8

Independent sessions, remount records and held-out-test design

9

Startup, shock, mount and saturation edge cases

10

Locked Level-1 validation and demo freeze

11

Documentation, BOM, wiring, limitations and rehearsal

12

Contingency repair and final delivery; no late scope expansion

Schedule rule

The minimum demonstrable system should work by the end of Week 8. Weeks 9-12 are reserved for validation, recovery and presentation rather than adding the future patent-research mechanism.

7. Team structure and accountability

The five members listed in the zeroth-review presentation remain the project team. Final technical ownership should be confirmed after approval using the following balanced structure:

Role

Responsibility

Technical integration lead

Architecture control, schedule, interfaces, safety and final integration

Firmware/data lead

SPI acquisition, feature pipeline, USB logs, analysis and held-out protocol

Hardware/rig lead

Procurement, wiring, motor base, rigid sensor mounting, guard and power

Learner/test assistant

Inventory, scripted sessions, labels, mount photographs and repeatable test records

Documentation/communication lead

Teacher communication, reports, demo script, slide updates and source log

Existing presentation responsibilities remain useful: Sreehari handles slide construction, Amith audits hardware/factual accuracy, Sreeprada coordinates speaker allocation after the deck is frozen, and Archa supports communication coaching/lead presenting.

The technical role-to-name map should be signed by all members after teacher approval; no critical subsystem will have only one knowledgeable owner.

8. Transition plan and preservation of OpenBraille work

Archive the final zeroth-review PPTX, OpenBraille architecture, memory, SOP, CAD concepts, BOM and research record under their existing configuration names.

Do not present OpenBraille as failed or wasted. Record it as a retained accessibility/mechatronics project and possible future research path.

Do not purchase the full six-servo OpenBraille BOM after switch approval unless the teacher separately authorizes a parallel or future build.

Freeze a new VibeGuard implementation folder, BOM, wiring record, firmware repository and validation log so evidence from the two projects cannot be mixed.

Update the next presentation transparently: explain the comparative assessment, approved change and exact new scope.

9. Patent and future-research boundary

Neither frozen semester project is being presented as a patent-ready invention. The later simulations identified research hypotheses only. These are not part of the approval request and must not be described as working results.

Future research hypothesis

Teacher-safe description

VibeGuard - PIRG

A later study may compare controlled target-machine changes with independently controlled interference changes to test whether one target-mounted sensor can distinguish target faults from neighbouring vibration. It is unbuilt and may fail.

OpenBraille - VPD-C7

A later mechanical study may examine whether the same registered endpoint that sets tactile-pin position can also provide direct pin-side endpoint evidence. It is unbuilt; current alone must never certify pin position.

Future research details, raw data, exact thresholds, unpublished CAD and claim-oriented structures should remain confidential until institutional IPR review.

A later filing/no-filing decision requires physical experiments, refreshed prior-art analysis and professional review. No patent grant is promised.

10. Risks and mitigations after the switch

Risk

Mitigation

Counterfeit or poor-quality sensor module

Buy from a reputable source, inspect the board and run a formal acceptance test before integration.

Unstable or unsafe motor rig

Use a heavy base, retained eccentric mass, shaft guard, current-limited bring-up and faculty/lab safety review.

Mount-dependent results

Use a rigid, documented bracket and preserve mount/remount photographs and configuration IDs.

Data leakage or over-optimistic accuracy

Split by complete sessions/remounts, not random windows; freeze thresholds before the locked test.

Late algorithm expansion

RMS plus persistence remains the minimum. FFT and Mahalanobis are comparisons, not excuses to delay the core build.

Patent expectation influencing the semester

Keep the semester MVP and future research in separate scopes, folders, budgets and claims.

11. Formal approval requested

Requested decision

Approve VibeGuard as Group 8's semester microcontroller project, using the frozen single-sensor Level-1 architecture and the approximately ₹2,200 expected budget. Retain OpenBraille as completed zeroth-review research and a possible future accessibility project.

The team believes this change increases the probability of delivering a complete, measurable and technically honest project without discarding the work already completed. Upon approval, procurement and role assignment will be frozen, and the detailed VibeGuard implementation dossier will become the controlling build plan.

Teacher decision

Approved / Approved with conditions / Not approved

Conditions or comments

Signature

Date

12. Evidence basis

This request was prepared from the controlled Project mC master evidence package, including:

Evidence layer

Controlled basis

Project authority

Engineering Design Review; Decision Register v1.2; approved Phase 3C Closure Memo; Concept Evidence Matrix; Uncertainty and Test Register

Technical authority

Final VibeGuard and OpenBraille Architecture Reports, Memories and SOPs

Comparative context

Two final cross-concept adjudications, treated as context rather than votes

Future-research boundary

VibeGuard and OpenBraille pre-build simulations, treated as unbuilt hypotheses

Current costing

Master Evidence, Costing and Decision Basis, price-checked 03 August 2026 using official specifications and reputable Indian retailer listings

Prepared for academic project approval. This document is not a patent opinion or freedom-to-operate clearance.


---

## Source 14: `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.pdf`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `e331fcfddd8782336049de278dd58880c408c67a7448ceb02e171ef9792b0aba`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/03_Change_Request/Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.pdf`
- Current SHA-256: `e331fcfddd8782336049de278dd58880c408c67a7448ceb02e171ef9792b0aba`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Topic: Project mC - Request to Change from OpenBraille to VibeGuard


                                                  PROJECT mC

             REQUEST FOR APPROVAL TO CHANGE THE
                      SEMESTER PROJECT
                                From OpenBraille to VibeGuard
    Course                                                   PBCST504 - Microcontrollers Micro Project

    Programme                                                B.Tech Computer Science and Engineering (Cyber
                                                             Security)

    Group                                                    Group 8

    Project Coordinator                                      Ms. Sagna L T, Assistant Professor, CSE (CY)

    Date                                                     03 August 2026


    Decision requested
    Approve the team's change from the frozen OpenBraille semester architecture to the frozen VibeGuard
    Level-1 architecture, while retaining OpenBraille as documented accessibility/mechatronics work and a
    possible future research project.


    1. Formal request
    To: Ms. Sagna L T, Project Coordinator
    Subject: Request to approve VibeGuard as the Group 8 semester implementation
    The team respectfully requests permission to change the semester implementation from OpenBraille, which
    was presented during the zeroth review, to VibeGuard. OpenBraille was selected for the zeroth review while
    the planned comparative engineering, budget, validation and future-research assessment was still
    incomplete. That assessment has now been completed. It retains OpenBraille as a valuable accessibility
    project, but identifies VibeGuard as the lower-risk and better-aligned semester build.

    2. Executive decision summary
    VibeGuard provides the strongest probability of completing a stable, measurable and demonstrable system
     within the semester.
    Its expected hardware budget is approximately ₹2,200, with a protected conservative envelope of
     approximately ₹3,900.
    Its main work aligns with ESP32 programming, embedded acquisition, signal processing, USB logging and
     quantitative testing - areas that match the team better than repeated precision mechanical fabrication.
    The requested switch is not based on a promise of patent grant. The ordinary VibeGuard semester MVP is
     treated as conventional.
    OpenBraille work will be preserved as a complete documented concept and may continue later as an
     accessibility/mechatronics research direction.


      Dept. of CSE (CY)                        PBCST504 - Microcontrollers                                  Page 1

                          Topic: Project mC - Request to Change from OpenBraille to VibeGuard


    3. Why the zeroth-review choice is changing
    The zeroth-review presentation correctly described OpenBraille as an affordable, macro-scale, single-cell
    Braille prototype using six low-cost servos and eccentric cams. The later review did not show that this was a
    poor idea. It showed that the two projects carry different kinds of semester risk.

                           Concept                                             Main semester risk

                                                             Mechanical iteration risk: guide friction, cam
    OpenBraille                                              alignment, pin travel, active retraction, six-servo
                                                             current demand, wear and tactile-state confirmation.

                                                             Data-validity risk: sensor authenticity, rigid mounting,
    VibeGuard                                                repeatable fault injection, stable sampling, threshold
                                                             selection and held-out validation.
    For this five-member CSE (Cyber Security) team, VibeGuard's risks are easier to isolate through scripted
    experiments and logs. OpenBraille can succeed, but a mechanical redesign can restart CAD, printing,
    assembly and power testing. VibeGuard allows faster recovery because the sensor, controller, rig, firmware
    and analysis can be tested as separate subsystems.

    4. Frozen semester architectures
    4.1 Proposed VibeGuard build
    One rigidly mounted ADXL345-class tri-axis accelerometer connected to an ESP32 over SPI.
    Continuous time-domain features, with RMS plus persistence as the minimum classifier.
    Triggered FFT and selected frequency-band features for explanation and comparison.
    Optional ordinary Mahalanobis anomaly score only as a comparative method.
    Local RGB indication and USB data logging.
    A guarded low-voltage motor/fan rig with controlled normal and induced-abnormal vibration states.
    No cloud dependence, permanent second sensor, source-separation array, active cancellation or remaining-
     useful-life claim.

    4.2 Retained OpenBraille definition
    One macro-scale six-dot cell with six SG90-class servos, six eccentric cams, followers and guided vertical
     pins.
    ESP32 direct PWM control, external regulated servo power and USB/serial character input.
    Active servo-driven retraction unless a real passive return is experimentally proved.
    No moving roller, encoder wheel, RAMPS/Mega embosser, continuous-paper system or electromagnetic
     substitution.

    Architecture-control statement
    The requested change selects one semester implementation. It does not merge the two concepts, rewrite
    either frozen architecture or claim that later research features have already been built.


      Dept. of CSE (CY)                        PBCST504 - Microcontrollers                                    Page 2

                         Topic: Project mC - Request to Change from OpenBraille to VibeGuard


5. Comparative semester decision
             Criterion                 VibeGuard                       OpenBraille                       Finding

                               Low-to-moderate electronics,    High mechanical integration
 Build complexity                                                                            VibeGuard
                               firmware and test-rig work      across six channels

 Expected cost                 About ₹2,200                    About ₹3,000                  VibeGuard

 Conservative envelope         About ₹3,900                    About ₹4,900                  VibeGuard

                               Strong: ESP32, firmware, DSP,   Requires sustained
 Team alignment                                                                              VibeGuard
                               data and testing                CAD/FDM/mechanical tuning

                               Repeated labelled sessions      Metrology, cycling, tactile
 Validation                                                                                  VibeGuard
                               and held-out tests              distinction and power tests

                               Motor-state change, RGB and     High social impact if
 Live demonstration                                                                          Both strong; VibeGuard safer
                               live logs/features              mechanics remain reliable

                               Subsystems can be replaced      Mechanical revision can
 Schedule recovery                                                                           VibeGuard
                               independently                   restart multiple stages

                               Conventional MVP; no filing     Conventional MVP; no filing
 Semester patent position                                                                    Equal
                               claim                           claim


6. Proposed VibeGuard semester scope
6.1 Minimum demonstrable success
1.    Acquire stable vibration data from the controlled rig using the target-mounted sensor.
2.    Establish a repeatable normal operating condition.
3.    Create a safe and repeatable induced-abnormal condition.
4.    Classify the two states locally with RMS plus persistence as the minimum baseline.
5.    Provide an interpretable RGB indication and USB evidence.
6.    Report repeatability, false alerts, missed detections, resource use and limitations on held-out sessions.

6.2 Budget summary
                            Layer                                                    Planning value

 ESP32 development board                                       ₹400 expected; ESP32-S3 only as an authorized fallback

                                                               ₹229 expected; provenance and bench acceptance
 ADXL345 breakout
                                                               required

 Low-voltage motor and adapter                                 Approximately ₹355 expected

 Rigid base, sensor bracket, shaft guard and
                                                               Approximately ₹500 expected planning allowance
 abnormality fixture

 Perfboard, indicators, connectors and passives                Approximately ₹400 expected

 Delivery/replacement allowance                                Approximately ₹300

 Expected planning total                                       Approximately ₹2,200

 Protected conservative envelope                               Approximately ₹3,900; below the ₹5,000 ceiling

6.3 Twelve-week roadmap
                            Week                                                   Primary milestone

 1                                                             Approval, scope freeze, safety review, procurement


     Dept. of CSE (CY)                         PBCST504 - Microcontrollers                                         Page 3

                            Topic: Project mC - Request to Change from OpenBraille to VibeGuard


                               Week                                                Primary milestone

                                                               ESP32 and ADXL345 acceptance; motor and mount
    2
                                                               inspection

                                                               Stable SPI acquisition, timestamps and dropped-block
    3
                                                               counters

    4                                                          Rigid mounting and repeated normal sessions

                                                               Safe induced-abnormal fixture and repeated abnormal
    5
                                                               sessions

    6                                                          RMS plus persistence, RGB output and USB logging

    7                                                          Triggered FFT/bands and ordinary comparator

                                                               Independent sessions, remount records and held-out-test
    8
                                                               design

    9                                                          Startup, shock, mount and saturation edge cases

    10                                                         Locked Level-1 validation and demo freeze

    11                                                         Documentation, BOM, wiring, limitations and rehearsal

                                                               Contingency repair and final delivery; no late scope
    12
                                                               expansion

    Schedule rule
    The minimum demonstrable system should work by the end of Week 8. Weeks 9-12 are reserved for
    validation, recovery and presentation rather than adding the future patent-research mechanism.


    7. Team structure and accountability
    The five members listed in the zeroth-review presentation remain the project team. Final technical
    ownership should be confirmed after approval using the following balanced structure:

                               Role                                                  Responsibility

                                                               Architecture control, schedule, interfaces, safety and final
    Technical integration lead
                                                               integration

                                                               SPI acquisition, feature pipeline, USB logs, analysis and
    Firmware/data lead
                                                               held-out protocol

                                                               Procurement, wiring, motor base, rigid sensor mounting,
    Hardware/rig lead
                                                               guard and power

                                                               Inventory, scripted sessions, labels, mount photographs
    Learner/test assistant
                                                               and repeatable test records

                                                               Teacher communication, reports, demo script, slide
    Documentation/communication lead
                                                               updates and source log

    Existing presentation responsibilities remain useful: Sreehari handles slide construction, Amith audits
     hardware/factual accuracy, Sreeprada coordinates speaker allocation after the deck is frozen, and Archa
     supports communication coaching/lead presenting.
    The technical role-to-name map should be signed by all members after teacher approval; no critical
     subsystem will have only one knowledgeable owner.


        Dept. of CSE (CY)                        PBCST504 - Microcontrollers                                        Page 4

                              Topic: Project mC - Request to Change from OpenBraille to VibeGuard


    8. Transition plan and preservation of OpenBraille work
    7.  Archive the final zeroth-review PPTX, OpenBraille architecture, memory, SOP, CAD concepts, BOM and
        research record under their existing configuration names.
    8. Do not present OpenBraille as failed or wasted. Record it as a retained accessibility/mechatronics project
        and possible future research path.
    9. Do not purchase the full six-servo OpenBraille BOM after switch approval unless the teacher separately
        authorizes a parallel or future build.
    10. Freeze a new VibeGuard implementation folder, BOM, wiring record, firmware repository and
        validation log so evidence from the two projects cannot be mixed.
    11. Update the next presentation transparently: explain the comparative assessment, approved change and
        exact new scope.

    9. Patent and future-research boundary
    Neither frozen semester project is being presented as a patent-ready invention. The later simulations
    identified research hypotheses only. These are not part of the approval request and must not be described as
    working results.

                       Future research hypothesis                                 Teacher-safe description

                                                                  A later study may compare controlled target-machine
                                                                  changes with independently controlled interference
     VibeGuard - PIRG                                             changes to test whether one target-mounted sensor can
                                                                  distinguish target faults from neighbouring vibration. It is
                                                                  unbuilt and may fail.

                                                                  A later mechanical study may examine whether the same
                                                                  registered endpoint that sets tactile-pin position can also
     OpenBraille - VPD-C7
                                                                  provide direct pin-side endpoint evidence. It is unbuilt;
                                                                  current alone must never certify pin position.

    Future research details, raw data, exact thresholds, unpublished CAD and claim-oriented structures should
     remain confidential until institutional IPR review.
    A later filing/no-filing decision requires physical experiments, refreshed prior-art analysis and professional
     review. No patent grant is promised.

    10. Risks and mitigations after the switch
                                 Risk                                                     Mitigation

                                                                  Buy from a reputable source, inspect the board and run a
     Counterfeit or poor-quality sensor module
                                                                  formal acceptance test before integration.

                                                                  Use a heavy base, retained eccentric mass, shaft guard,
     Unstable or unsafe motor rig
                                                                  current-limited bring-up and faculty/lab safety review.

                                                                  Use a rigid, documented bracket and preserve
     Mount-dependent results
                                                                  mount/remount photographs and configuration IDs.

                                                                  Split by complete sessions/remounts, not random
     Data leakage or over-optimistic accuracy
                                                                  windows; freeze thresholds before the locked test.

                                                                  RMS plus persistence remains the minimum. FFT and
     Late algorithm expansion                                     Mahalanobis are comparisons, not excuses to delay the
                                                                  core build.

                                                                  Keep the semester MVP and future research in separate
     Patent expectation influencing the semester
                                                                  scopes, folders, budgets and claims.


         Dept. of CSE (CY)                          PBCST504 - Microcontrollers                                        Page 5

                        Topic: Project mC - Request to Change from OpenBraille to VibeGuard


11. Formal approval requested
Requested decision
Approve VibeGuard as Group 8's semester microcontroller project, using the frozen single-sensor Level-1
architecture and the approximately ₹2,200 expected budget. Retain OpenBraille as completed zeroth-
review research and a possible future accessibility project.


The team believes this change increases the probability of delivering a complete, measurable and technically
honest project without discarding the work already completed. Upon approval, procurement and role
assignment will be frozen, and the detailed VibeGuard implementation dossier will become the controlling
build plan.

Teacher decision                                               Approved / Approved with conditions / Not approved

Conditions or comments


Signature


Date


12. Evidence basis
This request was prepared from the controlled Project mC master evidence package, including:

                       Evidence layer                                                Controlled basis

                                                               Engineering Design Review; Decision Register v1.2; approved
Project authority                                              Phase 3C Closure Memo; Concept Evidence Matrix;
                                                               Uncertainty and Test Register

                                                               Final VibeGuard and OpenBraille Architecture Reports,
Technical authority
                                                               Memories and SOPs

                                                               Two final cross-concept adjudications, treated as context
Comparative context
                                                               rather than votes

                                                               VibeGuard and OpenBraille pre-build simulations, treated as
Future-research boundary
                                                               unbuilt hypotheses

                                                               Master Evidence, Costing and Decision Basis, price-checked 03
Current costing                                                August 2026 using official specifications and reputable Indian
                                                               retailer listings


       Prepared for academic project approval. This document is not a patent opinion or freedom-to-operate clearance.


  Dept. of CSE (CY)                             PBCST504 - Microcontrollers                                          Page 6


---

## Source 15: `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/01_Team_Submission_6222246419165853974.pdf`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `80c2ddec1fb68dba305bcbce98a78221170644eb5338c99c4e6dd43242799bc6`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/01_Team_Submission_6222246419165853974.pdf`
- Current SHA-256: `80c2ddec1fb68dba305bcbce98a78221170644eb5338c99c4e6dd43242799bc6`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Gimme feasibility and shit
Short version: your docs say the one‑cell OpenBraille servocam MVP is technically buildable
this semester if you follow the test register, but the patent story is deliberately conservative and
treated as “future hypothesis,” while VibeGuard and TrueMoist carry more schedule/facility
risk. [1] [2] [3]

What “feasibility” means in these files
The Concept Evidence Matrix separates three layers: (1) engineering identity and MVP, (2)
minimum demonstrable success, and (3) whether Phase‑4/“next phase” is actually authorized.
[1] It explicitly warns that “Ready with Minor Refinements” in an architecture report is not the
same as “Phase 4 has started,” and that macro prototypes don’t automatically prove
commercial‑scale designs or patentability. [1] [3]

OpenBraille engineering feasibility
OpenBraille’s frozen MVP is a single six‑dot cell at macro scale with six SG90‑class servos, one
eccentric cam per servo, follower‑guided vertical pins, an ESP32 using direct PWM, an FDM
frame, and an external 5 V ≈2 A supply plus bulk capacitance. [1] [3] The matrix estimates a BOM
in the 2,060–2,850 range and calls out critical mechanical risks (pin/cam friction, tolerance
stack‑up, tactile height, wear) and electrical risk (six‑servo peaks vs 5 V/2 A rail), but all of these
are explicitly targeted by short, pre‑registered tests in the Uncertainty and Test Register. [1] [2]
The OpenBraille uncertainties U‑OB‑01…07 cover: verifying whether SG90 actually has a usable
passive torsion‑spring return, proving active cam retraction is reliable if passive return fails,
checking six‑servo current demands vs the 5 V/2 A supply and capacitors, 3D‑printed
mechanical tolerances over 1,000 cycles, and designing a blinded tactile‑identification protocol
with quantitative acceptance criteria. [2] Each test has concrete equipment, 1–4 day durations,
and “Immediate” or early‑semester urgency, which is exactly the profile of “feasible but only if
you front‑load the bench tests before CAD freeze and assembly.” [2] [3]

OpenBraille patent feasibility
The pre‑build patent‑case simulation states that the frozen semester MVP is a “strong semester
prototype and a Track D no‑current‑filing patent position,” because low‑cost servo‑cam Braille
cells and motor‑driven cam pin actuation with position sensing are already present in recent
US and EP patents and academic work. [3] It concludes that the current D11 bundle (calibration,
current sensing, retry logic, replacement acceptance, etc.) is still just an aggregation of familiar
elements until comparative experiments show a cooperative physical effect that actually lowers
silent wrong tactile states beyond strong baselines. [3]

The simulation identifies a more promising but speculative future direction—Verified
Pin‑Datum Cell VPD‑C7—where the same mechanically registered datum both sets pin
endpoints and produces a pin‑side endpoint electrical event, with current used only as
independent effort evidence; but it is explicit that this redesign is not disclosed in the frozen
architecture and needs new mechanical/electrical design, displacement ground truth,
wear/contamination tests, and a refreshed patent search before anyone calls it an invention. [3]
In other words, engineered OpenBraille MVP: yes; near‑term patent: intentionally “not yet,”
with feasibility framed as “research hypothesis that only survives if later data beat obvious
combinations of HumanWare/Enhanced Vision/current‑sensing prior art.” [3]

VibeGuard feasibility
VibeGuard’s MVP identity is a passive, single‑node edge condition‑monitoring system: ADXL345
accelerometer on a rigid mount, ESP32, FFT‑based features plus Mahalanobis statistics and
spectral subtraction, and a damped motor/fan rig with an eccentric‑mass fault. [1] The Evidence
Matrix and Uncertainty Register both stress that bench‑rig normal vs deliberate abnormal
classification is on‑scope, while dense‑floor attribution (one node correctly attributing a fault
to its own machine in a crowded environment) is explicitly beyond the minimum
demonstrable success and has unresolved site‑access and protocol issues. [1] [2]
Uncertainties U‑VG‑01…07 require you to (a) prove ADXL345’s bandwidth is enough for all
claimed MVP phenomena, (b) show rigid remounts don’t dominate classification, (c) test
whether spectral subtraction actually improves discrimination vs simpler thresholds, (d) get
real dense‑floor ground truth, and (e) demonstrate repeatable eccentric‑mass fault simulation
and bench classifier accuracy with pre‑registered statistical thresholds. [2] Many of these have
2–7 day durations but depend on rig build and external site access, which makes VibeGuard
more logistically fragile than OpenBraille for a single semester, even though the core bench
classification problem is well‑scoped. [1] [2]

TrueMoist feasibility
TrueMoist’s MVP is an embedded soil‑moisture instrument that combines genuine capacitive
probes, temperature sensing, ADS1115 ADC, local regression‑based compensation, and
gravimetric ground‑truth at 105 ± 5 °C to show that compensated estimates beat raw sensor
output on held‑out samples under controlled conditions. [1] The architecture is labelled as
“Ready with Mandatory Early Validation,” with many explicit gates around probe stability, ADC
value vs ESP32’s internal ADC, packing/jig effects, oven and precision scale access, controlled
salinity treatment, and the throughput needed for roughly 72 independent runs in eight weeks.
[1] [2]

Uncertainties U‑TM‑01…07 ask whether ADS1115 materially improves noise/drift/RMSE,
whether the chosen capacitive probe is monotonic and repeatable, whether a jig can keep
packing variance below intended environmental effects, whether institutional oven/scale
access is real, and whether a single NaCl treatment produces a stable, non‑saturating shift
distinct from noise. [2] The Concept Evidence Matrix highlights that institutional oven and
scale access and the 72‑run workflow are direct schedule risks and that a documented 54‑run
fallback may be needed if throughput is lower, so TrueMoist is feasible only if you lock facilities
early and treat schedule planning as a first‑week task, not an afterthought. [1] [2]

What this means for you in practice
Given the way these files are written, OpenBraille is deliberately positioned as the “least risky
to build this semester” concept: single‑cell macro scale, clear BOM, short bench tests for core
mechanical/electrical uncertainties, and a validation plan that you can run with an ESP32 and
straightforward firmware, provided you design and pre‑register a tactile protocol with the
project owner. [1] [2] [3] VibeGuard and TrueMoist are more dependent on access (dense machine
floor vs institutional oven/scale) and on bigger statistical datasets, so they’re better treated as
“bench‑rig and methods prototypes” unless those external conditions are locked in writing. [1]
[2]

If your immediate goal is “get something solid and defensible built and reported,” the feasible
path is roughly:
      Front‑load the U‑OB tests: servo passive/active return, six‑servo current adequacy,
      single‑dot mechanical coupon, then design/approve the tactile protocol before committing
      to full CAD and assembly. [2]
      Treat the D11/VPD‑C7 patent content strictly as a research roadmap: log all execution data
      (force, travel, current, failures), but don’t promise patentability until you have comparative
      evidence against direct sensors and strong prior art. [3]
      Only scale VibeGuard beyond a motor‑fan bench demo if you can secure a dense‑floor site
      and pre‑registered attribution metrics early; otherwise, keep claims to “bench‑rig normal
      vs abnormal classification” with explicit limits. [1] [2]
      For TrueMoist, do a hard Week‑1 facilities check (oven, scale, storage, probes, ADS1115) and
      be ready to formally adopt the documented 54‑run fallback if throughput or access falls
      short of the ideal 72‑run plan. [1] [2]
If you tell me which of the three you’re actually trying to push right now (OpenBraille vs
VibeGuard vs TrueMoist), I can turn this into a very concrete “do this first, then this” checklist
keyed directly to the uncertainty IDs and evidence rows in your files. [1] [2] [3]
                                                 ⁂


Check with data from these sources aswell
Updated verdict: once you include the change‑request and VibeGuard roadmap PDFs, the
controlled evidence explicitly recommends VibeGuard as the lower‑risk, better‑aligned
semester build for your five‑member CSE(CY) team, with OpenBraille kept as archived
accessibility/mechatronics work and a future research direction. [4] [5]

What the change‑request actually says
The “Request to Change from OpenBraille to VibeGuard” memo asks your coordinator to
approve switching the semester implementation from OpenBraille to the frozen VibeGuard
Level‑1 architecture. [4] It argues:
      VibeGuard “provides the strongest probability of completing a stable, measurable and
      demonstrable system within the semester.” [4]

    Expected hardware budget is ≈₹2,200 with a conservative envelope ≈₹3,900, staying under
    your ₹5k ceiling and leaving more recovery headroom than OpenBraille’s ≈₹3,000 / ≈₹4,900
    planning values. [4]
    VibeGuard’s main work is ESP32 programming, embedded acquisition, signal processing,
    USB logging, and quantitative testing—deliberately matched to a CS/Cyber student skill
    profile, unlike OpenBraille’s sustained CAD/FDM and mechanical tuning. [4]
The comparative table in that PDF flat‑out states VibeGuard wins on build complexity, expected
cost, conservative envelope, team alignment, validation tractability, and schedule recovery,
while both concepts are treated as “conventional MVP; no filing claim” for patents this
semester. [4]

VibeGuard architecture and MVP from the roadmap
The VibeGuard roadmap locks the Level‑1 semester scope to one rigidly mounted
ADXL345‑class accelerometer on an ESP32 over SPI, a guarded low‑voltage motor/fan rig,
RMS+persistence classification as the minimum baseline, optional FFT/band features and
Mahalanobis only as comparisons, RGB indication, and USB logging. [5] It defines minimum
demonstrable success as:
 1. Stable sensor acquisition on a rigid mount.
 2. A repeatable normal operating condition.
 3. A safe, repeatable induced‑abnormal condition.
 4. Local Normal/Abnormal classification with RMS+persistence.
 5. Interpretable RGB + USB evidence.
 6. Repeatability/false‑alert/missed‑detection reporting on held‑out sessions. [5]
The doc also sets a Week‑8 target for reaching “minimum demonstrable system,” with Weeks 9–
12 reserved for validation, recovery, and presentation, and lists clear approval gates (change
from OpenBraille, build‑window confirmation, ESP32 variant choice, rig safety review, and
pre‑registered held‑out protocol) before procurement freeze. [5]

Risk profile: VibeGuard vs OpenBraille with the new docs
The change‑request reframes the main semester risks:
    OpenBraille: mechanical iteration—guide friction, cam alignment, pin travel, active
    retraction, six‑servo current demand, wear, and tactile‑state confirmation. [4]
    VibeGuard: data validity—sensor authenticity, rigid mounting, repeatable fault injection,
    stable sampling, threshold selection, and held‑out validation. [4]
For a five‑member CS/Cyber team, the document argues VibeGuard’s risks are easier to isolate
and recover from (scripted experiments and logs, independently testable subsystems), whereas
a mechanical mistake in OpenBraille can force you to restart CAD, printing, assembly and
power testing. [4] That’s consistent with the VibeGuard roadmap’s risk register (counterfeit
ADXL345, unsafe rig, mount‑dependent results, SPI loss, saturation/bandwidth mismatch, data
leakage, late algorithm expansion, team bottleneck, and patent expectations), each with

specific mitigation steps like formal sensor acceptance tests, rigid bracket IDs, conservative
ODR/clock settings, session‑level splits, and keeping RMS+persistence as the core demo. [5]

Patent and future‑research boundary
Both PDFs are very explicit that the semester VibeGuard build is “conventional and is not
represented as a patent‑ready invention,” and that PIRG (the post‑semester target vs interferer
dense‑floor attribution hypothesis) is a separate, unbuilt research path with its own folder,
budget, and confidentiality. [4] [5] Likewise, they retain OpenBraille as a documented
macro‑scale Braille concept plus a possible future VPD‑C7 pin‑datum research line, but forbid
treating any of that as working patent results this semester. [4]

What you should actually do now
Given all five controlled docs together (matrix, uncertainty register, OpenBraille simulation,
change‑request, VibeGuard roadmap), the “honest and finishable” path for you this semester is:
    Formally seek/record approval to switch to VibeGuard Level‑1 using the exact scope and
    budget in the change‑request. [4]
    Treat the VibeGuard roadmap as your controlling build plan: one ADXL345‑class sensor +
    ESP32, guarded motor rig, RMS+persistence baseline by ≈Week 8, then validation and
    demo. [5]
    Use the risk and mitigation table from the roadmap as your task list for Week 1–4 (sensor
    acceptance test, rig safety checklist, mount/remount trials, SPI health counters, held‑out
    protocol freezing). [5]
    Archive all OpenBraille PPTX/architecture/SOP/CAD/BOM/research under their existing
    names, do not bin it as “failed,” and don’t buy the six‑servo BOM unless your teacher
    explicitly authorizes parallel/future work. [4]
If you want, I can turn the VibeGuard roadmap plus the Uncertainty Register into a concrete
week‑by‑week checklist (what exactly to code, wire, and test each week) so you can hit that
Week‑8 minimum system with maximum safety margin. [6] [4] [5]
                                                ⁂

  1. 03_Concept_Evidence_Matrix.md
  2. 07_Uncertainty_and_Test_Register.md
  3. 17_OpenBraille_PreBuild_Future_Patent_Case_Simulation.md
  4. Project_mC_Request_to_Change_from_OpenBraille_to_VibeGuard.pdf
  5. VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf
  6. 07_Uncertainty_and_Test_Register.md


---

## Source 16: `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/02_Team_Submission_6282084529079524834.pdf`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `fcf17069f5cd3e9ca6bd388792b3c4987b26618876c66991e1076764fc2e3539`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/02_Team_Submission_6282084529079524834.pdf`
- Current SHA-256: `fcf17069f5cd3e9ca6bd388792b3c4987b26618876c66991e1076764fc2e3539`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Gimme feasibility and shit
Short version: your docs say the one‑cell OpenBraille servocam MVP is technically buildable
this semester if you follow the test register, but the patent story is deliberately conservative and
treated as “future hypothesis,” while VibeGuard and TrueMoist carry more schedule/facility
risk. [1] [2] [3]

What “feasibility” means in these files
The Concept Evidence Matrix separates three layers: (1) engineering identity and MVP, (2)
minimum demonstrable success, and (3) whether Phase‑4/“next phase” is actually authorized.
[1] It explicitly warns that “Ready with Minor Refinements” in an architecture report is not the
same as “Phase 4 has started,” and that macro prototypes don’t automatically prove
commercial‑scale designs or patentability. [1] [3]

OpenBraille engineering feasibility
OpenBraille’s frozen MVP is a single six‑dot cell at macro scale with six SG90‑class servos, one
eccentric cam per servo, follower‑guided vertical pins, an ESP32 using direct PWM, an FDM
frame, and an external 5 V ≈2 A supply plus bulk capacitance. [1] [3] The matrix estimates a BOM
in the 2,060–2,850 range and calls out critical mechanical risks (pin/cam friction, tolerance
stack‑up, tactile height, wear) and electrical risk (six‑servo peaks vs 5 V/2 A rail), but all of these
are explicitly targeted by short, pre‑registered tests in the Uncertainty and Test Register. [1] [2]
The OpenBraille uncertainties U‑OB‑01…07 cover: verifying whether SG90 actually has a usable
passive torsion‑spring return, proving active cam retraction is reliable if passive return fails,
checking six‑servo current demands vs the 5 V/2 A supply and capacitors, 3D‑printed
mechanical tolerances over 1,000 cycles, and designing a blinded tactile‑identification protocol
with quantitative acceptance criteria. [2] Each test has concrete equipment, 1–4 day durations,
and “Immediate” or early‑semester urgency, which is exactly the profile of “feasible but only if
you front‑load the bench tests before CAD freeze and assembly.” [2] [3]

OpenBraille patent feasibility
The pre‑build patent‑case simulation states that the frozen semester MVP is a “strong semester
prototype and a Track D no‑current‑filing patent position,” because low‑cost servo‑cam Braille
cells and motor‑driven cam pin actuation with position sensing are already present in recent
US and EP patents and academic work. [3] It concludes that the current D11 bundle (calibration,
current sensing, retry logic, replacement acceptance, etc.) is still just an aggregation of familiar
elements until comparative experiments show a cooperative physical effect that actually lowers
silent wrong tactile states beyond strong baselines. [3]

The simulation identifies a more promising but speculative future direction—Verified
Pin‑Datum Cell VPD‑C7—where the same mechanically registered datum both sets pin
endpoints and produces a pin‑side endpoint electrical event, with current used only as
independent effort evidence; but it is explicit that this redesign is not disclosed in the frozen
architecture and needs new mechanical/electrical design, displacement ground truth,
wear/contamination tests, and a refreshed patent search before anyone calls it an invention. [3]
In other words, engineered OpenBraille MVP: yes; near‑term patent: intentionally “not yet,”
with feasibility framed as “research hypothesis that only survives if later data beat obvious
combinations of HumanWare/Enhanced Vision/current‑sensing prior art.” [3]

VibeGuard feasibility
VibeGuard’s MVP identity is a passive, single‑node edge condition‑monitoring system: ADXL345
accelerometer on a rigid mount, ESP32, FFT‑based features plus Mahalanobis statistics and
spectral subtraction, and a damped motor/fan rig with an eccentric‑mass fault. [1] The Evidence
Matrix and Uncertainty Register both stress that bench‑rig normal vs deliberate abnormal
classification is on‑scope, while dense‑floor attribution (one node correctly attributing a fault
to its own machine in a crowded environment) is explicitly beyond the minimum
demonstrable success and has unresolved site‑access and protocol issues. [1] [2]
Uncertainties U‑VG‑01…07 require you to (a) prove ADXL345’s bandwidth is enough for all
claimed MVP phenomena, (b) show rigid remounts don’t dominate classification, (c) test
whether spectral subtraction actually improves discrimination vs simpler thresholds, (d) get
real dense‑floor ground truth, and (e) demonstrate repeatable eccentric‑mass fault simulation
and bench classifier accuracy with pre‑registered statistical thresholds. [2] Many of these have
2–7 day durations but depend on rig build and external site access, which makes VibeGuard
more logistically fragile than OpenBraille for a single semester, even though the core bench
classification problem is well‑scoped. [1] [2]

TrueMoist feasibility
TrueMoist’s MVP is an embedded soil‑moisture instrument that combines genuine capacitive
probes, temperature sensing, ADS1115 ADC, local regression‑based compensation, and
gravimetric ground‑truth at 105 ± 5 °C to show that compensated estimates beat raw sensor
output on held‑out samples under controlled conditions. [1] The architecture is labelled as
“Ready with Mandatory Early Validation,” with many explicit gates around probe stability, ADC
value vs ESP32’s internal ADC, packing/jig effects, oven and precision scale access, controlled
salinity treatment, and the throughput needed for roughly 72 independent runs in eight weeks.
[1] [2]

Uncertainties U‑TM‑01…07 ask whether ADS1115 materially improves noise/drift/RMSE,
whether the chosen capacitive probe is monotonic and repeatable, whether a jig can keep
packing variance below intended environmental effects, whether institutional oven/scale
access is real, and whether a single NaCl treatment produces a stable, non‑saturating shift
distinct from noise. [2] The Concept Evidence Matrix highlights that institutional oven and
scale access and the 72‑run workflow are direct schedule risks and that a documented 54‑run
fallback may be needed if throughput is lower, so TrueMoist is feasible only if you lock facilities
early and treat schedule planning as a first‑week task, not an afterthought. [1] [2]

What this means for you in practice
Given the way these files are written, OpenBraille is deliberately positioned as the “least risky
to build this semester” concept: single‑cell macro scale, clear BOM, short bench tests for core
mechanical/electrical uncertainties, and a validation plan that you can run with an ESP32 and
straightforward firmware, provided you design and pre‑register a tactile protocol with the
project owner. [1] [2] [3] VibeGuard and TrueMoist are more dependent on access (dense machine
floor vs institutional oven/scale) and on bigger statistical datasets, so they’re better treated as
“bench‑rig and methods prototypes” unless those external conditions are locked in writing. [1]
[2]

If your immediate goal is “get something solid and defensible built and reported,” the feasible
path is roughly:
        Front‑load the U‑OB tests: servo passive/active return, six‑servo current adequacy,
        single‑dot mechanical coupon, then design/approve the tactile protocol before committing
        to full CAD and assembly. [2]
        Treat the D11/VPD‑C7 patent content strictly as a research roadmap: log all execution data
        (force, travel, current, failures), but don’t promise patentability until you have comparative
        evidence against direct sensors and strong prior art. [3]
        Only scale VibeGuard beyond a motor‑fan bench demo if you can secure a dense‑floor site
        and pre‑registered attribution metrics early; otherwise, keep claims to “bench‑rig normal
        vs abnormal classification” with explicit limits. [1] [2]
        For TrueMoist, do a hard Week‑1 facilities check (oven, scale, storage, probes, ADS1115) and
        be ready to formally adopt the documented 54‑run fallback if throughput or access falls
        short of the ideal 72‑run plan. [1] [2]
If you tell me which of the three you’re actually trying to push right now (OpenBraille vs
VibeGuard vs TrueMoist), I can turn this into a very concrete “do this first, then this” checklist
keyed directly to the uncertainty IDs and evidence rows in your files. [1] [2] [3]
                                                    ⁂

      1. 03_Concept_Evidence_Matrix.md
      2. 07_Uncertainty_and_Test_Register.md
      3. 17_OpenBraille_PreBuild_Future_Patent_Case_Simulation.md


---

## Source 17: `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/03_Team_Submission_IDK.pdf`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `59a07438163718094c4cd4704016cee80bacce689939eafa52eb9cb91e56f126`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/03_Team_Submission_IDK.pdf`
- Current SHA-256: `59a07438163718094c4cd4704016cee80bacce689939eafa52eb9cb91e56f126`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

The application of Braille on equipment and appliances is strictly governed by the ISO
17049:2013 standard. To ensure tactile readability, this standard dictates precise dimen-
sional parameters: a dot base diameter of 1.0 to 1.7 mm (specifically 1.5 mm to 1.6 mm
in many regional adoptions), a horizontal dot spacing of 2.0 to 2.8 mm, and a dot height
of 0.3 to 0.7 mm. The biomechanics of tactile reading depend entirely on these precise di-
mensions, as the human fingertip must cover multiple dots simultaneously to recognize a cell
pattern instantly. Fused Deposition Modeling (FDM) 3D printers using standard 0.4 mm
nozzles struggle immensely to resolve a 1.5 mm domed dot reliably without severe stringing
or layer-line artifacts that degrade tactile readability.
While ”macro-scaling” the physical cell mathematically solves the mechanical FDM tolerance
risk, it introduces a severe factual and logical error: a macro-scaled Braille cell violates the
strict ISO 17049 dimensional parameters and actively destroys tactile readability, rendering
the device useless for an actual Braille reader. If the distance between corresponding dots
in adjacent cells exceeds the standard 6.1 mm to 7.6 mm, the user cannot read the display
fluidly. Claiming to build a Braille display while intentionally violating the foundational
standard that defines Braille geometry is a critical technical flaw that must be addressed.a
catastrophic academic and architectural misalignment exists. The presentation is explicitly
designated for the course ”PBCST504,” which is the KTU Microcontrollers course (Semester
5, 2024 Scheme). The official university syllabus for this course explicitly focuses on the
ARM Cortex-M architecture—specifically the Cortex-M23 and Cortex-M33 processors—and
mandates the use of STM32 microcontrollers (such as the STM32U575) for peripheral pro-
gramming, TrustZone implementation, and FreeRTOS deployment.
However, Slide 11 states that the project utilizes an ”ESP32-WROOM-32” development
board. The ESP32 is based on the Tensilica Xtensa Dual-Core 32-bit LX6 microprocessor
architecture, not the ARM Cortex-M architecture. Using an Espressif Xtensa-based micro-
controller for a project assigned under a curriculum strictly dedicated to ARM Cortex-M
and STM32 microcontrollers represents a fundamental failure to meet the core academic
requirements of the course.
Second, the slide demonstrates a technical terminology error regarding the hardware itself.
The text specifies the use of an ”ESP32-WROOM-32 development board”. The ESP32-
WROOM-32 is a surface-mount module consisting of the SoC, flash memory, and an antenna.
It is not a development board. The development board that houses this module, providing
the USB-to-UART bridge, voltage regulation, and pin headers, is officially designated as
the ESP32-DevKitC. Conflating a bare module with a populated development board is an
elementary hardware engineering mistake.
Third, the electrical power architecture described in the slide requires immediate verification.
The text states: ”Six positional SG90-class micro servos drive eccentric cams,” and ”A 1,000
µF capacitor is proposed across the servo power rail to help reduce transient voltage dips.” The
SG90 micro servo is a standard 9-gram actuator that operates via Pulse Width Modulation
(PWM) at a 50Hz frequency, requiring 1ms to 2ms duty cycles. While the ESP32’s LEDC
peripheral features 16 independent hardware PWM channels capable of driving these signal
lines simultaneously, the power draw is a major concern. An SG90 servo typically draws
between 100mA and 250mA during standard movement, but stall currents can spike up to


                                               1

700mA per servo. If all six servos move simultaneously or encounter mechanical resistance
(e.g., binding against the FDM printed cams), the total current draw on the 5V rail could
surge to between 1.5A and 4.2A. While a 1,000 µF bulk decoupling capacitor will smooth
short, high-frequency voltage transients and prevent the ESP32 from resetting (brownout)
due to common ground loops, it is mathematically incapable of sustaining continuous high-
current stall loads. The text critically omits any specification regarding the amperage rating
of the external 5V power supply required to drive this load.”Basic Block Diagram.” A review
of the slide reveals a critical omission: there is no diagram present. The slide contains only
the title text and is otherwise completely blank. In a technical hardware presentation, the
block diagram is essential for illustrating the interfacing between the microcontroller, the
power distribution network, the PWM signal routing, and the electromechanical actuators.
Submitting or presenting a slide deck with a missing primary visual graphic demonstrates a
severe lack of quality assurance. . Ranked Top 5 Most Serious Errors
Syllabus/Architecture Mismatch (Slide 11): The presentation proposes using an ESP32 (Ten-
silica Xtensa architecture) for a project in a KTU course (PBCST504) that strictly mandates
ARM Cortex-M and STM32 microcontrollers. This is a fatal academic failure that will result
in immediate penalization during an engineering review.
Missing Block Diagram (Slide 12): Submitting an entirely blank slide designated for the core
system architecture demonstrates a severe lack of quality control and will cause a critical
stoppage during a live presentation.
ISO 17049 Dimension Violation (Slide 9): ”Macro-scaling” the Braille cell mathematically
solves FDM printing tolerances but destroys the physiological capability of the fingertip to
read the tactile data. The text must acknowledge this as a non-standard mechanical proof-
of-concept rather than a functional Braille interface.
Hardware Terminology Conflation (Slide 11): Referring to the ”ESP32-WROOM-32” as a
development board instead of a bare surface-mount module is a rudimentary hardware en-
gineering error that undermines technical credibility.I have fact-checked the statements you
provided against official technical documentation, standards, and university curriculum guide-
lines. Here is the verification for each point:
1. ISO 17049:2013 and Braille Dimensions
The statements regarding the Braille dimensions are accurate. The ISO 17049:2013 standard
mandates strict dimensional parameters to ensure tactile readability, explicitly dictating a dot
base diameter between 1.0 and 1.7 mm and a dot height between 0.3 and 0.7 mm. Regional
accessibility guidelines that adopt these principles specify standard base diameters of 1.5 to
1.6 mm, dot spacing of 2.3 to 2.5 mm, and adjacent cell corresponding dot spacing of 6.1 to 7.6
mm. Therefore, intentionally ”macro-scaling” a Braille cell to bypass 3D printing tolerances
would fundamentally violate these standardized metrics, rendering the display functionally
useless for a tactile reader.
2. Academic Misalignment (KTU PBCST504 vs. ESP32)
The claim regarding the academic mismatch is factually correct. The APJ Abdul Kalam Tech-
nological University (KTU) 2024 Scheme defines course ”PBCST504” as ”Microcontrollers”


                                               2

for Semester 5. The official syllabus is strictly dedicated to ARM Cortex-M architecture
(specifically Cortex-M23 and M33 processors) and mandates the use of STM32 microcon-
trollers, such as the STM32U575. Conversely, the ESP32 operates on a Tensilica Xtensa
dual-core architecture. Using an ESP32 for this specific project is a direct violation of the
course’s core architectural requirements.
3. Hardware Terminology (WROOM-32 vs. DevKitC)
The hardware terminology correction is highly accurate. The ESP32-WROOM-32 is a bare
surface-mount module that contains the system-on-chip, memory, and a PCB antenna. It
requires a carrier board to provide the USB-to-UART bridge, voltage regulation, and pinout
headers for prototyping. The official Espressif development board that houses this module is
the ESP32-DevKitC. Conflating the two is a technical terminology error.
4. Power Architecture and SG90 Servos
The technical assessment of the power architecture and current draw is accurate. The ESP32
features 16 independent hardware PWM channels (via its LEDC peripheral) capable of pre-
cisely driving multiple servos. However, while an SG90 servo draws 100mA to 250mA during
standard movement, its stall current can spike from 360mA up to approximately 700mA. If
six servos move simultaneously or stall, the combined current draw on the 5V rail can easily
surge between 2.1A and 4.2A. A 1,000 µF capacitor is meant to smooth transient dips; it
cannot supply sustained high current. A dedicated external 5V power supply rated for the
total stall current is mandatory to prevent system failure.
5. Missing Block Diagram
The critique regarding the missing visual element is logically and professionally sound. In
hardware engineering presentations, a block diagram is a mandatory requirement to illustrate
power distribution, signal routing, and component interfacing. Presenting a slide with only
a title and no corresponding graphic is a critical quality assurance failure.


                                             3


---

## Source 18: `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

- Authority: `TIER_2`
- Treatment: `CORE_DECISION_EVIDENCE`
- Hash status: `HASH_VERIFIED`
- Extraction status: `EXTRACTED`
- Source mode: `REUSED_STAGE10B_EXTRACTION`
- SHA-256: `ac94cb30df641c577af516da7047e1f2ebbdf1252620755aede08f9f0ed68568`

# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`
- Current SHA-256: `ac94cb30df641c577af516da7047e1f2ebbdf1252620755aede08f9f0ed68568`
- Extraction method: `PLAIN_TEXT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

# Project mC — Comparative Decision Index

## Common evidence and gates

This section contains the shared engineering baseline, comparison protocol,
evidence matrix, hard-gate precheck, uncertainty register, patent input pack,
scoring worksheet and reasoning audit.

These documents establish decision context. A score or model conclusion must
not be treated as a vote merely because it appears in a separate file.

## Final adjudications

Two final cross-concept adjudications are preserved:

1. Work Max adjudication.
2. Deep Research High adjudication.

They are independent decision-support outputs. Neither automatically overrides
the project authority files, teacher constraints or experimental evidence.

## Change request

The editable and rendered change-request documents preserve the formal proposal
to move the semester implementation from OpenBraille to VibeGuard.

Their presence does not itself prove that the change was approved.

## Team audits and objections

Team-submitted challenge documents are preserved without assigning them
automatic authority. Claims in those documents must be checked against the
frozen architectures, valid syntheses, experiments and current governance.

## Current boundary

The repository organization preserves both the original OpenBraille direction
and the proposed VibeGuard shift. Folder placement alone does not finalize the
team or teacher decision.

