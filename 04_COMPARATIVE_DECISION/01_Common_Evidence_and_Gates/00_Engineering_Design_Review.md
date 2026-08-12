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
