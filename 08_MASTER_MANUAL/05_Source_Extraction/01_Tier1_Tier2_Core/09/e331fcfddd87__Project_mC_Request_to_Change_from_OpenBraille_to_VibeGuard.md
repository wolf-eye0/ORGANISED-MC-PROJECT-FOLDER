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
