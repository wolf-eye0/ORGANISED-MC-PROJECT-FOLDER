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
