# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_SUPPORTING`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf`
- Current SHA-256: `ee9cce3ebd57dd84b3bbacd9d4738fc219a334441b80c2bb34e0417c90060ab4`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


                                                             PROJECT mC


                   OPENBRAILLE
              SEMESTER ARCHITECTURE
          AND FUTURE RESEARCH REFERENCE
                     DOSSIER
Frozen Macro Six-Dot Build Plan, Validation Programme and Post-Semester VPD-
                              C7 Research Path

                        Control item                                                                 Value

Course                                                               PBCST504 - Microcontrollers Micro Project

Programme                                                            B.Tech Computer Science and Engineering (Cyber Security)

Group                                                                Group 8

Document status                                                      Complete retained-reference and fallback implementation
                                                                     dossier

Current portfolio status                                             VibeGuard switch requested; OpenBraille remains the fully
                                                                     documented alternative

Frozen architecture                                                  One macro six-dot cell; six SG90-class servos; eccentric cams;
                                                                     guided pins; ESP32 direct PWM

Expected semester budget                                             Approximately ₹2,984; conservative envelope approximately
                                                                     ₹4,909

Future mechanism                                                     VPD-C7 research hypothesis - unbuilt, confidential and
                                                                     evidence-gated


Controlling decision
This dossier does not override the current request to adopt VibeGuard. It provides the complete OpenBraille plan if the
teacher retains the zeroth-review concept, and preserves OpenBraille as a future accessibility/mechatronics research
route.


Patent boundary
The macro six-servo semester prototype is conventional and is not represented as patent-ready. VPD-C7 is a separate post-
semester hypothesis that must be redesigned, built, compared and professionally reviewed before any filing decision.

 Prepared from the controlled Project mC authority set and the Master Evidence, Costing and Decision Basis. This document is an
            engineering reference plan, not a patent opinion, standards-compliance declaration or promise of grant.


   Dept. of CSE (CY)                                PBCST504 - Microcontrollers                                             Page 1

                                Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


Document control and approval use
                             Control item                                                                Value

 Architecture baseline                                                   Frozen OpenBraille Phase 3C macro six-servo/cam architecture

 Return-motion rule                                                      Active servo-driven cam retraction unless a usable passive
                                                                         return is physically proved

 Power baseline                                                          External regulated 5 V servo supply; 5 V/3 A procurement
                                                                         target; measured droop controls acceptance

 USB role                                                                Serial command input and logs; not six-servo power

 Semester boundary                                                       No moving roller, encoder, RAMPS/Mega, continuous paper or
                                                                         electromagnetic substitution

 Future boundary                                                         VPD-C7 only on a separate post-MVP coupon; current never
                                                                         certifies pin height alone


Approval checkpoints required before an OpenBraille procurement freeze
1. Teacher confirmation that OpenBraille, rather than the requested VibeGuard alternative, remains the semester
implementation.
2. Confirmation of the effective build window and dependable institutional FDM-printer access.
3. Approval of the one-dot-first mechanical validation plan before six servos and full-cell materials are committed.
4. Approval of the external 5 V power arrangement, pinch-point controls and tactile-participant protocol.
5. Approval of quantitative repeatability, cycle-life and pattern-test criteria before the locked validation run.


Executive reference decision
 Complete alternative semester plan
 OpenBraille is technically buildable within the ₹5,000 ceiling and offers a strong accessibility demonstration. Its execution
 risk is concentrated in FDM tolerances, cam/follower friction, active retraction, six-servo power behavior and trustworthy
 tactile-state validation. This dossier is therefore retained as the complete fallback/reference plan while VibeGuard
 remains the recommended semester choice.

The correct semester claim is narrow: one macro-scale six-dot cell accepts a character or dot pattern over USB/serial,
commands six independent servo/cam channels, produces repeatable raised/lowered tactile states, and reports
measured limitations. The project must not be presented as a standards-compliant commercial Braille display or as a
patented actuator mechanism.

Success definition at a glance
                     Layer                                Required semester result                                 Evidence

 Mechanical                                     Six independently moving macro dots with         CAD/build IDs, caliper measurements,
                                                active raise/retract and safe rounded pin        photographs, cycle logs
                                                tips

 Electrical                                     Stable ESP32 control and external servo rail     Voltage/current observations, reset log,
                                                without brownouts or unsafe heating              power checklist

 Firmware                                       Correct character-to-six-dot mapping, per-       Unit tests, configuration record, pattern test
                                                dot calibration and USB commands/logs            report

 Validation                                     Repeatability, lifecycle, pattern-transition     Locked test sheet, raw records, failed-run
                                                and approved tactile evidence                    register

 Scope honesty                                  Macro educational prototype; no physical-        Explicit limitations in report and live
                                                state claim from command timing alone            demonstration

 Future separation                              VPD-C7 kept outside the semester                 Separate research folder and disclosure
                                                architecture                                     controls


    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                                 Page 2

                             Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


1. Purpose, audience and scope
1.1 Purpose
This dossier converts the frozen OpenBraille Phase 3C architecture into a procurement-aware and execution-ready
semester plan. It defines the hardware, mechanical build order, electrical integration, firmware, calibration,
validation, team ownership, semester schedule and future-research boundary.

1.2 Audience
• Project coordinator and teacher: concept-retention decision, scope, budget, safety and review gates.
• Five-member student team: CAD, fabrication, firmware, assembly, testing, evidence and demonstration
responsibilities.
• Department laboratories: FDM access, tools, metrology and safety support.
• Accessibility or tactile-test reviewers: honest macro-prototype scope and participant protocol.
• Institutional innovation/IPR reviewers: separation between the public semester cell and confidential VPD-C7 work.

1.3 Scope hierarchy
                Scope tier                                      Included                                        Not included

 Semester OpenBraille                        One macro six-dot cell; six servos/cams/pins;    Standards-compliant product, multi-cell line,
                                             direct PWM; active retraction; USB;              production design, patent claim
                                             measurements

 Semester instrumentation                    Calipers/camera, voltage/current checks and      Permanent endpoint contacts or current-
                                             test scripts used as development evidence        only state inference

 Post-semester VPD-C7                        Separate coupon studying a datum that sets       Assumed performance, filing-ready claims
                                             and directly evidences pin endpoints             or automatic inclusion in the semester cell


2. Engineering identity and problem definition
2.1 Engineering identity
OpenBraille is an assistive embedded-system experiment focused on lowering the cost of refreshable tactile output. Its
semester purpose is not to compete with commercial displays, but to test whether a simple low-cost actuation channel
can create one repeatable six-dot cell suitable for education and engineering study.

2.2 Semester engineering hypothesis

 Hypothesis to test
 A macro-scaled servo-and-cam mechanism can produce repeatable raised and lowered tactile states for one six-dot
 Braille cell within the student budget and schedule, while accepting that the prototype is not commercial-scale or
 standards-compliant.


2.3 What the hypothesis does not claim
• It does not claim that servo + cam + Braille pin actuation is novel.
• It does not claim commercial Braille pitch, force, refresh speed, noise or lifetime.
• It does not assume a passive servo spring retracts the pin.
• It does not treat a PWM command, elapsed time or servo current as direct proof of tactile-pin height.
• It does not establish a patent or freedom to operate.


    Dept. of CSE (CY)                                PBCST504 - Microcontrollers                                                Page 3

                             Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


3. Frozen system architecture


                         Figure 1. Frozen macro six-dot architecture and explicit semester scope boundary.

3.1 Subsystem boundaries
           Subsystem                           Inputs                              Outputs                       Owner acceptance

 USB/serial interface            Character, pattern or test           Parsed request,                      Commands are deterministic,
                                 command                              acknowledgement and log line         versioned and unit-tested

 ESP32 control                   Pattern, per-dot calibration and     Six PWM outputs and                  No invalid GPIO use, unstable
                                 fixed sequencing rules               timestamped command records          resets or hidden configuration

 Six actuator channels           5 V servo power and PWM              Cam rotation and follower            Each channel accepted on a one-
                                                                      displacement                         dot fixture before full-cell
                                                                                                           assembly

 Mechanical cell                 Six channel motions                  Six guided raised/lowered tactile    No binding, unsafe tips or
                                                                      pins                                 adjacent-channel interference

 Power distribution              External regulated 5 V and           Stable servo rail and logic          No USB servo power, brownout
                                 common ground                        operation                            or unsafe heating

 Development measurement         Pin position, cycle count, rail      Evidence package and                 External measurement remains
                                 behavior and operator                limitations                          the truth source for physical
                                 observations                                                              position


3.2 Frozen architecture controls
• One macro-scale six-dot cell only.
• Six SG90-class servos, one eccentric cam and one guided vertical pin per dot.
• ESP32 local direct-PWM control; no intermediate motor driver is required for the servo signal.
• FDM frame/guides/cams and external regulated servo power.
• Active servo-driven retraction unless a procured mechanism proves a reliable passive return under load.
• No moving roller, encoder wheel, RAMPS/Mega embosser, continuous-paper system or electromagnetic substitution.


    Dept. of CSE (CY)                                PBCST504 - Microcontrollers                                                 Page 4

                                 Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


4. Detailed hardware architecture and BOM
4.1 Required purchased and fabricated items
                                                                                                                              Acceptance/
        Item                        Qty           Exact semester role            Expected               Conservative
                                                                                                                           procurement rule


ESP32 development       1                        Six PWM channels,        ₹400                    ₹899                    Verified WROOM-32
board                                            USB/serial commands                                                      DevKit baseline;
                                                 and logging                                                              ESP32-S3 authorized
                                                                                                                          fallback. Record
                                                                                                                          pinout and regulator.

SG90-class servo        6                        One independent          ₹120 each / ₹720        ₹142 each / ₹852        Buy one consistent
                                                 eccentric-cam                                                            batch where possible;
                                                 actuator per dot                                                         inspect every unit; no
                                                                                                                          passive-return
                                                                                                                          assumption.

5 V / 3 A regulated     1                        External servo supply    ₹289                    ₹408                    Connector and
adapter                                          with test headroom                                                       regulation verified;
                                                                                                                          adequacy controlled
                                                                                                                          by measured droop
                                                                                                                          and stall tests.

1,000 µF electrolytic   1-2                      Servo-rail transient     ₹25                     ₹50                     Install near
capacitor                                        buffering                                                                distribution; voltage
                                                                                                                          rating above 5 V; not a
                                                                                                                          substitute for an
                                                                                                                          adequate supply.

FDM frame, guides,      1 cell                   Macro mechanical         ₹450                    ₹900                    Expected case
cams and followers                               structure                                                                assumes institutional
                                                                                                                          printer access; print a
                                                                                                                          single-dot coupon
                                                                                                                          first.

Stainless pins/rod      6 + spare                Guided tactile dots      ₹250                    ₹400                    Local quote;
with rounded tips                                                                                                         polished/rounded,
                                                                                                                          safe for repeated
                                                                                                                          touch, dimensions
                                                                                                                          recorded.

Fasteners, servo        1 lot                    Alignment, assembly,     ₹300                    ₹500                    Final quantity follows
mounts and cable                                 strain relief and                                                        CAD and physical
management                                       guards                                                                   servo dimensions.

Perfboard, wires,       1 lot                    Power distribution       ₹200                    ₹350                    Servo current never
headers and                                      and stable PWM                                                           routed through ESP32
connectors                                       wiring                                                                   3.3 V rail or thin USB
                                                                                                                          wiring.

USB data cable          1                        Serial input and logs    ₹100                    ₹150                    Reusable cable
                                                                                                                          acceptable after
                                                                                                                          connection reliability
                                                                                                                          check.

         Budget layer                               Low                               Expected                          Conservative

Required hardware/material            ₹1,866                              ₹2,734                               ₹4,509
subtotal

Delivery/local                        ₹100                                ₹250                                 ₹400
variability/replacement
allowance

Semester planning total               ₹1,966                              ₹2,984                               ₹4,909


 Budget decision
 Use approximately ₹3,000 as the expected teacher-facing budget. The conservative case remains below ₹5,000 only when
 institutional printing is available and full-cell reprints are limited. One or two spare servos are useful but should be
 approved separately.


    Dept. of CSE (CY)                                     PBCST504 - Microcontrollers                                                Page 5

                                  Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


4.2 Reusable or institutional equipment
                    Equipment                                           Use                                          Required status

 Laptop with Arduino IDE and Python               Firmware, serial commands, analysis and          Assumed available
                                                  reporting

 FDM printer and slicing software                 Frame, guides, cams, followers and coupons       Material dependency; access must be
                                                                                                   confirmed

 Digital calipers                                 Pin travel, spacing, clearances, repeatability   Required
                                                  and wear

 Multimeter                                       Power, continuity and servo-rail checks          Required

 Bench supply with current limit                  One-servo bring-up and fault-safe testing        Strongly recommended / borrowed

 Oscilloscope or logic analyzer                   PWM and rail-transient checks                    Useful but not essential

 Camera / fixed measurement jig                   External visual ground truth and                 Required for credible evidence
                                                  configuration record

 Basic hand tools and soldering station           Assembly, finishing and final wiring             Institutional/reusable

 Tactile participant access and approved          Raised/lowered and pattern                       Not confirmed; teacher/ethics decision
 protocol                                         distinguishability


5. Mechanical architecture and one-dot-first build


          Figure 2. One-dot channel and the separation between command, physical motion and development ground truth.

5.1 Mechanical design rules
1. Start with one independently testable servo + cam + follower + pin coupon. Do not print the full cell before the
coupon moves freely.
2. Use macro spacing and travel as a documented educational design choice. A starting target near 300% of standard
sign-Braille geometry may guide CAD, but the prototype must not be labelled standards-compliant.
3. Use rounded, smooth tactile tips and guard all pinch points around cams and servo horns.
4. Set pin-guide clearance through printed tolerance coupons and measured finishing; nominal CAD dimensions do
not prove physical clearance.
5. Use active cam-driven raise and retract positions. Do not rely on an unverified servo spring or gravity return.
6. Record each printed part revision, orientation, material, measured dimensions, sanding/finishing and assembly
operator.
7. Treat each channel as replaceable for test purposes, but do not present modular replacement as a novel patent
feature.


     Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                                  Page 6

                               Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


5.2 Provisional geometry and acceptance parameters
                   Parameter                               Starting design basis                                  Acceptance rule

 Cell scale                                    Macro single cell, approximately 3x              Final CAD and measured cell clearly labelled
                                               commercial sign-Braille pitch as an              non-standard
                                               engineering starting point

 Raised travel                                 Approximately 1.5 mm starting target             Teacher-approved tactile and repeatability
                                                                                                test controls final value

 Pin material                                  Approximately 2 mm stainless rod with            No sharp edge, binding, corrosion or unsafe
                                               rounded tip                                      surface

 Cam throw                                     Set through one-dot CAD/coupon to create         No stall, follower loss or adjacent
                                               required travel with margin                      interference

 Guide clearance                               Derived from printed tolerance coupon            Free motion under the selected load with
                                                                                                repeatable alignment

 Actuation sequence                            Fixed sequential or bounded group of             No brownout, unsafe peak or excessive
                                               changed dots                                     refresh delay


5.3 Mechanical stop conditions
• Pin binds, tilts, scrapes or fails to retract fully.
• Cam/follower loses contact, jumps, cracks or creates an exposed pinch hazard.
• Servo stalls or heats during the normal pattern sequence.
• Pin height varies beyond the approved repeatability band.
• A rounded tactile tip becomes loose or unsafe.
• Full-cell assembly changes the motion that passed on the single-dot coupon.


6. Electrical integration and provisional pin map


    Figure 3. Recommended power and control boundary. Final wiring must be verified against the purchased board and supply.

6.1 Power domains
               Domain                           Source                                Loads                                 Rule

 Logic / USB                       Laptop USB to ESP32 DevKit           ESP32 and serial interface           Do not back-feed a second 5 V
                                                                                                             source into an unverified board
                                                                                                             while USB is connected

 Servo rail                        External regulated 5 V / 3 A         Six SG90-class servos                Separate branch and conductors
                                   target                                                                    sized for servo current; bulk
                                                                                                             capacitor near distribution


     Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                                    Page 7

                               Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


              Domain                            Source                                Loads                                    Rule

 Signal reference                  Common ground                        ESP32 PWM and servo signal             Use star/controlled grounding;
                                                                        reference                              inspect for resets and noise

 Measurement                       Multimeter / optional scope          Servo rail and logic rail              Measurements must not create
                                                                                                               unsafe shorts or loose probes
                                                                                                               near moving cams


6.2 Provisional ESP32-WROOM-32 pin assignment
                    Function                                 Provisional GPIO                                          Notes

 Dot 1 PWM                                     GPIO 16                                              Output-capable; verify board label

 Dot 2 PWM                                     GPIO 17                                              Output-capable; verify board label

 Dot 3 PWM                                     GPIO 18                                              Output-capable; avoid conflict with other
                                                                                                    planned peripherals

 Dot 4 PWM                                     GPIO 19                                              Output-capable

 Dot 5 PWM                                     GPIO 21                                              Output-capable

 Dot 6 PWM                                     GPIO 22                                              Output-capable

 USB serial                                    Onboard USB-UART                                     Primary command/log interface

 Optional status LED                           GPIO 23 or onboard LED where available               Not part of the six-dot mechanism; verify
                                                                                                    polarity/board mapping


 Implementation note
 This is a Phase 4 wiring proposal, not a source-file mandate. Revalidate every pin against the exact purchased DevKit and
 do not use boot-strapping or input-only pins without understanding their behavior.


6.3 Wiring acceptance checklist
• ESP32 boots and USB serial works with servo rail disconnected.
• External adapter polarity and no-load/loaded voltage are verified.
• Servo rail and logic share only the intended reference ground.
• Each servo is tested alone before joining the distribution rail.
• Bulk capacitor polarity and placement are correct.
• No servo current passes through the ESP32 3.3 V regulator or laptop USB cable.
• Combined pattern transitions produce no reset, cable heating or connector instability.


7. Firmware and software architecture
7.1 Firmware module breakdown
                    Module                                     Responsibility                                 Required outputs/tests

 Configuration manager                         Board variant, pin map, cell/build ID, PWM           Startup banner and configuration record
                                               calibration and sequence policy

 USB command parser                            Accept character, six-bit pattern, clear, test       Malformed-command tests and
                                               and calibration commands                             deterministic responses

 Braille mapping table                         Map supported characters to six-dot                  Unit test independent of hardware
                                               patterns

 PWM/channel manager                           Apply per-dot up/down pulse widths and               Logic-analyzer/servo acceptance and no
                                               fixed sequencing                                     illegal overlap

 Calibration manager                           Store per-dot command values established             Versioned calibration table and reset
                                               with external measurement                            procedure


    Dept. of CSE (CY)                                  PBCST504 - Microcontrollers                                                    Page 8

                               Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


                    Module                                         Responsibility                                 Required outputs/tests

 Pattern transition engine                      Move only changed dots, apply settle                 Transition log and pattern suite
                                                interval and update commanded state

 Fault/log manager                              Record resets, invalid commands, manual              Human-readable USB log; no false physical-
                                                faults and channel disable state                     state claim

 Test mode                                      Cycle one channel or selected patterns               Repeatability/lifecycle scripts
                                                under operator control


7.2 Repository and configuration structure
                             Folder/file                                                                    Purpose

 firmware/                                                                 ESP32 source, board configuration and release tags

 firmware/config/                                                          Pin map, per-dot calibration and build identifiers

 firmware/tests/                                                           Character mapping and command-parser unit tests

 cad/                                                                      Versioned frame, guide, cam, follower and coupon designs

 fabrication/                                                              Slicer settings, material, orientation and post-processing record

 protocols/                                                                Electrical, mechanical, cycle, tactile and demo procedures

 data/                                                                     Measurements, cycle logs, power observations and fault records

 evidence/                                                                 Photographs, videos, signed checklists and final locked results


7.3 Command and state semantics
The firmware should distinguish commanded state from verified physical state. Without a permanent pin sensor, the
runtime may record that a PWM command and settle interval completed, but it must not label that event
UPPER_CONFIRMED or LOWER_CONFIRMED. Physical confirmation belongs to external development measurement
and the approved tactile protocol.

                State                           Meaning                             Allowed evidence                         Exit/exception


 STARTUP                           Board and configuration                 Firmware and board checks               FAULT on invalid configuration
                                   initialization

 READY                             No active transition; accepts           Commanded pattern record                RAISING / LOWERING / TEST
                                   command

 RAISING                           One or more selected channels           PWM command and timestamp               SETTLE_WAIT after command
                                   commanded toward up position                                                    interval

 LOWERING                          Selected channels commanded             PWM command and timestamp               SETTLE_WAIT after command
                                   toward down position                                                            interval

 SETTLE_WAIT                       Fixed mechanical settling delay         Timer only                              COMMAND_FINISHED; not
                                                                                                                   physical confirmation

 COMMAND_FINISHED                  Requested command sequence              Command log                             External tests decide physical
                                   ended                                                                           correctness

 FAULT/ISOLATED                    Manual/operator or                      Fault input, reset, test observation    Operator-cleared after inspection
                                   electrical/mechanical fault
                                   recorded


8. Calibration, sequencing and control logic
8.1 Per-dot calibration process
1. Assign a permanent channel and servo identity.
2. Use external calipers/camera or a fixed displacement jig to measure the lowered and raised pin positions.
3. Sweep the up command in small controlled increments to find the minimum repeatable raised position without
stall or excessive load.
4. Repeat for active retraction and verify the pin returns to the approved lowered band.
    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                                        Page 9

                                 Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


5. Repeat across multiple cycles and store the selected command values with hardware/build IDs.
6. Invalidate or recheck calibration after servo replacement, cam/guide reprint or major reassembly.

8.2 Fixed sequencing policy
The semester system should use a simple fixed sequence: identify changed dots, lower dots that must clear, then raise
dots that must set, with a bounded number of simultaneously moving channels chosen only after measured power
testing. Dynamic current-aware sequencing belongs to future research and must not be backfilled into the frozen
MVP.

8.3 Pattern transition rules
                                  Rule                                                                   Purpose

 Move only changed dots                                                   Reduces unnecessary cycles, noise and power

 Active retract before conflicting raise                                  Prevents ambiguous intermediate patterns

 Fixed settle time per tested channel group                               Makes behavior reproducible and loggable

 Reject malformed/unsupported command                                     Protects mapping and state integrity

 Manual stop on stall, heating or binding                                 No automatic recovery without evidence

 Calibration version stored with every test                               Prevents results from being separated from command values


8.4 Physical-truth boundary

 Do not overclaim state
 A servo angle, PWM pulse, elapsed time, current rise or visible cam movement does not automatically prove acceptable
 tactile-pin height. Semester physical truth comes from external measurement and an approved tactile evaluation. Current
 sensing may be used for power/safety observation, not endpoint certification.


9. Data and evidence management
9.1 Required build and session metadata
• Project, firmware, CAD, slicer and protocol version.
• Servo identity, seller/batch, channel assignment and replacement history.
• Cam, follower, guide and pin revision; material, print orientation and finishing.
• Per-dot up/down command values and calibration date.
• Supply identity, measured voltage, actuation grouping and reset/brownout observations.
• Pattern sequence, cycle count, operator, temperature/contamination/load note where relevant.
• Measured raised/lowered positions, failed transitions, binding, wear and manual interventions.
• Photographs/videos tied to the exact configuration ID.

9.2 Evidence hierarchy
                Evidence type                                  What it supports                             What it does not support

 USB command log                                 Requested patterns, timestamps and               Actual tactile height
                                                 firmware behavior

 Calipers/camera/displacement jig                Development measurement of pin positions         Long-term tactile usability by itself

 Power measurements                              Supply adequacy, peaks, droop and resets         Endpoint correctness

 Cycle log                                       Repeatability and mechanical failure history     Commercial lifetime

 Tactile protocol                                Participant distinguishability under the         Universal user performance or standards
                                                 approved setup                                   compliance

 Photographs/video                               Configuration and visible operation              Precise dimensions without measurement


    Dept. of CSE (CY)                                    PBCST504 - Microcontrollers                                                Page 10

                                   Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


9.3 Final evidence package
                                Evidence file                                                             Minimum content


Configuration record                                                          Board, pins, six servo IDs, CAD/slicer versions, power source and
                                                                              calibration table

Mechanical acceptance                                                         One-dot and six-dot dimensions, travel, free-motion and safety checklist

Electrical acceptance                                                         Supply voltage, resets, wiring, capacitor and combined-pattern
                                                                              observations

Pattern test                                                                  Supported character/pattern suite and exact pass/fail outputs

Repeatability/lifecycle                                                       Per-channel measurements, cycle counts and failures

Tactile protocol report                                                       Approved method, participants/ethics status, randomization, results and
                                                                              limitations

Failure register                                                              Binding, wear, servo replacement, reprints, rejected runs and corrective
                                                                              action

Final demo package                                                            Frozen firmware/CAD, demo script, backup evidence and limitations


10. Validation and acceptance programme
10.1 Validation stages
                Stage                               Question                          Minimum evidence                          Stop/fallback


OB-V0 Component acceptance             Are the ESP32, first servo, supply     Board/USB check, servo sweep,          Replace failed component before
                                       and tools usable?                      adapter polarity/voltage               CAD freeze

OB-V1 One-dot mechanics                Can one printed channel raise and      Measured motion, photographs           Redesign guide/cam before
                                       actively retract without binding?      and repeated cycles                    ordering full batch

OB-V2 Calibration                      Can per-dot command windows            External measurement across            Change geometry or actuator; do
                                       produce repeatable positions?          cycles                                 not tune blindly

OB-V3 Six-dot integration              Do six channels coexist without        Pattern commands, power                Use fixed sequencing, stronger
                                       interference and brownout?             observation and mechanical             supply or rebuild distribution
                                                                              inspection

OB-V4 Pattern correctness              Does character mapping produce         Unit tests and physical pattern        Fix mapping/configuration before
                                       intended six-dot states?               checks                                 user testing

OB-V5 Repeatability/lifecycle          Does the mechanism retain              100-cycle precision set and at least   Record failure; redesign or limit
                                       position and motion over               1,000 total actuations                 claim
                                       approved cycles?

OB-V6 Tactile evaluation               Are raised/lowered dots and            Teacher-approved blinded               Adjust geometry or report MDS not
                                       selected patterns distinguishable?     protocol                               achieved

OB-V7 Locked demonstration             Can the frozen build reproduce the     Signed checklist, frozen               Use approved backup evidence; no
                                       result safely?                         configuration and final evidence       late redesign


10.2 Proposed semester acceptance targets for teacher approval

 Status of numbers
 The project authority contains some architecture-level repeatability and lifecycle targets, but the tactile participant
 threshold is not frozen. The following set should be preregistered and approved before the locked run.

                     Metric                                         Proposed target                                     Why it matters


Channel function                                    All six channels independently raise and            Minimum six-dot cell functionality
                                                    actively retract throughout the final pattern
                                                    sequence

Repeatability                                       ≤0.1 mm position variation over 100 measured        Source-derived architecture target; measures
                                                    cycles under the approved setup                     mechanical consistency

Lifecycle screen                                    At least 1,000 actuations without mechanical        Early engineering screen, not product lifetime
                                                    failure that invalidates the demo


    Dept. of CSE (CY)                                       PBCST504 - Microcontrollers                                                      Page 11

                                       Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


 Pattern mapping                                            100% correct output for the frozen supported            Separates firmware mapping from mechanical
                                                            character/test set                                      failure

 Power integrity                                            No brownout/reset, connector heating or unsafe          Electrical safety and reliability
                                                            voltage collapse in the locked sequence

 Tactile distinguishability                                 Teacher-approved blinded threshold and trial            Avoids inventing or post-hoc selecting a success
                                                            count fixed before testing                              rate

 Failure honesty                                            Every incomplete/bound transition is logged; no         Evidence integrity
                                                            command-complete event relabelled as
                                                            physically verified

 Budget                                                     Final semester spend ≤₹5,000, with preferred            Course requirement
                                                            target near ₹3,000


10.3 Required performance reporting
• Per-dot raised and lowered position distributions, not only average travel.
• Pattern-level pass/fail counts and the exact supported character set.
• Power/reset observations for one, multiple and worst planned transitions.
• Cycle count, wear inspection and parts replaced.
• Tactile results with protocol, participant context and limitations.
• Negative evidence, binding, failed prints and calibration changes.
• Explicit statement that the macro prototype does not establish commercial-scale feasibility.


11. Twelve-week semester roadmap
          Week                      Primary work                    Owner(s)              Measurable output               Exit criterion                   Fallback


 1                            Teacher decision, scope       Nihad + team; Amith        Approved concept status;     No full-cell purchase until   Use available verified
                              freeze, FDM/tool audit        fabrication audit          one-servo order;             one-dot gate and teacher      ESP32/servo variants
                              and first procurement                                    printer/tool booking; risk   direction are confirmed       without changing
                                                                                       register                                                   architecture

 2                            ESP32/USB bring-up, one       Sreehari + Amith           Commanded servo sweep;       Stable board/serial and       Replace failed
                              bare servo and power                                     adapter/polarity record;     safe one-servo motion         board/servo/supply before
                              acceptance                                               provisional pin map                                        CAD integration

 3                            Print tolerance coupons       Amith + Nihad              Measured coupon set;         Pin moves freely and cam      Adjust guide/cam
                              and one-dot                                              one-dot assembly;            produces controllable         dimensions; laser-cut
                              frame/cam/follower                                       CAD/build ID                 travel                        guide fallback only if
                                                                                                                                                  approved

 4                            Active raise/retract          Amith + Sreehari;          Per-dot calibration          Stable raised/lowered         Change geometry/servo
                              calibration and single-dot    Sreeprada tests            procedure; 100-cycle         bands without binding or      before multiplying
                              repeatability                                            single-dot dataset           unsafe stall                  channels

 5                            Procure/accept remaining      Amith + Sreeprada          Six accepted servo IDs;      Each channel passes           Use spares or pause
                              servos and fabricate six-     inventory                  completed printed parts;     independent bench test        channels; do not hide
                              dot parts                                                assembly checklist                                         batch variation

 6                            Six-dot mechanical and        Nihad + Amith + Sreehari   Assembled cell; external     All six move                  Fixed sequential
                              electrical integration                                   rail; six PWM channels;      independently; no             actuation,
                                                                                       command logs                 brownout/interference         supply/distribution
                                                                                                                                                  revision or rebuild

 7                            Braille mapping, pattern      Sreehari + Sreeprada       Supported character set;     Frozen test patterns          Reduce demo set while
                              transitions and per-dot                                  mapping unit tests;          produce correct               keeping mapping
                              calibration                                              calibration table            commanded states              evidence honest

 8                            Power, safety,                Amith + Nihad; Sreeprada   Worst planned transition     No unsafe heating, reset,     Limit actuation group,
                              repeatability and failure-    runs                       record; fault/reprint log;   pinch or uncontrolled         strengthen guard/supply
                              mode testing                                             safety review                motion                        or redesign

 9                            Lifecycle screen and          Nihad + Archa;             Cycle progress; approved     Mechanism survives and        Report tactile validation
                              tactile-protocol approval     teacher/participant        blinded protocol or          protocol is approved          unavailable rather than
                                                            coordination               documented access limit      before use                    improvising

 10                           Locked                        Full team; test led by     Frozen configuration and     Approved targets met          Record failure; use honest
                              pattern/repeatability/tacti   Sreeprada                  signed result sheets         without post-result           partial-MDS conclusion
                              le validation                                                                         calibration changes

 11                           Final report, source          Archa + Nihad; technical   Final BOM, CAD/firmware      Every technical claim         Remove unsupported
                              records and live-demo         review by Sreehari/Amith   versions, results,           traces to evidence            claims and use backup
                              rehearsal                                                limitations and demo                                       video only if approved
                                                                                       script


      Dept. of CSE (CY)                                              PBCST504 - Microcontrollers                                                             Page 12

                                    Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


          Week                  Primary work                 Owner(s)              Measurable output            Exit criterion              Fallback


 12                        Contingency, repair-only   Full team                 Stable final build and    No late VPD-C7 or         Submit the strongest
                           window and final                                     archived evidence         architecture expansion    verified semester result
                           delivery                                             package


 Schedule rule
 The minimum demonstrable cell should work by the end of Week 8. Weeks 9-12 are for lifecycle, tactile evidence,
 recovery and presentation. VPD-C7 hardware must not enter the semester critical path.


12. Team roles, actual members and accountability
 Role status
 The following map mirrors the established five-member structure. It is a proposed assignment for team approval; it
 deliberately gives mechanical work substantial ownership because that is OpenBraille’s critical risk.

              Member                           Proposed primary role             Specific OpenBraille ownership              Review/backup obligation


 Nihad P C - JEC24CC044                  Technical integration lead / project   Architecture control, schedule,         Backs up firmware and hardware;
                                         manager                                interface decisions, validation         approves configuration freezes
                                                                                protocol, final integration and
                                                                                evidence integrity

 Sreehari K - JEC24CC055                 Firmware and embedded-control          USB command parser, Braille             Nihad reviews releases; Sreeprada
                                         lead                                   mapping, PWM/channel manager,           executes scripted tests
                                                                                calibration storage, test scripts and
                                                                                logs

 Amith Krishna Das - JEC24CC016          Mechanical, hardware and power         CAD/FDM, cam/follower/guide             Nihad reviews interfaces/safety;
                                         lead                                   design, servo acceptance, power         Sreehari checks control
                                                                                rail, assembly and safety               requirements
                                                                                inspection

 Sreeprada K S - JEC24CC056              Learner, test and inventory            Inventory, servo/build labels, cycle    Works from signed procedures;
                                         assistant                              scripts, measurements, photos, test     learns USB operation and
                                                                                registry and repeated independent       calibration workflow
                                                                                trials

 Archa Pramod - JEC24CC022               Documentation, teacher                 Weekly records, teacher-safe            Technical statements reviewed by
                                         communication and                      explanations, tactile-test              Nihad, Sreehari and Amith
                                         demonstration lead                     coordination, live-demo script,
                                                                                final presentation and source
                                                                                register


12.1 Responsibility rules
• Every critical subsystem has one primary owner, one technical reviewer and one written checklist.
• No one changes CAD, PWM calibration, power wiring or test labels without a dated configuration update.
• The learner/test role is evidence-critical and must run independent repetitions, not only observe.
• The documentation lead does not publish VPD-C7 details without technical and IPR review.
• Nihad acts as integration failsafe, but CAD, firmware and validation must remain independently owned and
reviewable.


13. Procurement, acceptance and configuration control
13.1 Procurement sequence
1. Confirm teacher decision and institutional FDM access.
2. Buy one verified ESP32 board, one SG90-class servo, the external supply and basic mechanical material first.
3. Pass the one-dot mechanical/active-retraction gate before buying or committing the remaining servo batch and full-
cell prints.
4. Buy the remaining servos from one consistent seller/batch where practical and record every identity.
5. Fabricate the full frame only after the physical servo and pin dimensions are measured.
6. Purchase spares only when acceptance or delivery risk justifies them within the conservative envelope.

      Dept. of CSE (CY)                                       PBCST504 - Microcontrollers                                                      Page 13

                                     Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


13.2 Component acceptance record
                      Component                                    Acceptance checks                                            Reject if


 ESP32                                               Reliable boot/USB, exact board identity and           Unknown pinout, repeated disconnect,
                                                     usable output GPIOs                                   overheating or unstable regulator

 SG90 servo                                          Smooth sweep, no damaged gears, stable                Dead zone, severe jitter, gear damage,
                                                     horn/shaft and repeatable response                    overheating or inconsistent return command

 5 V adapter                                         Correct polarity, stable loaded output, adequate      Unsafe voltage, instability, excessive droop or
                                                     connector and no overheating                          poor connector

 FDM coupon                                          Measured clearance, free pin motion, no cracks        Binding, unsafe roughness, large warp or non-
                                                     or warped datum surfaces                              repeatable fit

 Cam/follower                                        Smooth engagement and required travel                 Stiction, follower jump, crack or unsafe pinch
                                                     without losing contact                                exposure

 Pin/tip                                             Straight, smooth, rounded and securely                Sharp edge, looseness, corrosion or unsafe
                                                     retained                                              touch surface


13.3 Configuration ID format
Recommended format: OB-[cell/build]-[dot/servo]-[CAD]-[firmware]-[protocol]-[session]. Example: OB-C01-D3-SV05-
CAD0.4-FW0.6-P03-R012. The exact format may change, but every measurement, image and result must identify the
physical and software configuration.


14. Risk register and mitigation
               Risk                   Likelihood / impact             Early indicator                    Mitigation                Decision consequence


 FDM guide/cam tolerance          High / High                  Pin does not slide freely;       One-dot coupons, measured       Do not proceed to six-dot
 and friction                                                  variable travel; follower drag   clearance, material/print       assembly until passed
                                                                                                iteration, limited finishing

 No usable passive return         High / Medium                Pin remains raised or servo      Use active commanded            Architecture remains valid
                                                               does not return under load       retraction; remove passive-     with corrected control
                                                                                                return language                 description

 Servo batch                      Medium / High                Different travel for common      Consistent batch, per-dot       May increase calibration and
 variation/backlash                                            PWM; jitter or gear play         calibration, spare/replace      evidence burden
                                                                                                failed unit

 Six-servo brownout or rail       Medium / High                ESP32 reset, adapter sag,        Separate 5 V rail, bulk         Upgrade supply/distribution
 droop                                                         connector heating                capacitor, fixed sequencing,    or reduce simultaneous
                                                                                                measured load                   motion

 Pin tip unsafe or tactility      Medium / High                Sharp/loose tip or participant   Rounded tips, geometry          MDS may fail even when
 poor                                                          cannot distinguish states        iteration, approved tactile     motion is visible
                                                                                                protocol

 Cam/follower wear                Medium / Medium              Position drift, dust,            Material choice, inspection,    Limit claims and redesign if
                                                               roughness or increased noise     lifecycle screen, replaceable   systematic
                                                                                                coupon

 CAD/print schedule slippage      High / Medium                Multiple full reprints or        Single-dot gate, modular        May force reduced demo or
                                                               printer unavailable              prints, early lab booking,      switch to VibeGuard
                                                                                                controlled fallback

 Firmware                         Low / Medium                 Wrong pattern despite            Independent unit tests and      Fix before tactile validation
 mapping/calibration error                                     correct mechanics                configuration versioning

 Tactile participant/protocol     Medium / Medium              No approved access or trial      Secure approval early;          Do not claim tactile success
 unavailable                                                   design                           document visual/mechanical      without the test
                                                                                                evidence separately

 Macro prototype overstated       Medium / High                Slides imply standard            Teacher-safe wording,           Remove unsupported claim
 as product                                                    compliance or commercial         explicit dimensions/limits      before presentation
                                                               readiness                        and review

 Future patent concept leaks      Medium / Medium              VPD-C7 contact/current           Separate folders, approval      Exclude from semester build
 into MVP                                                      details added late               gate and confidentiality rule   and results


     Dept. of CSE (CY)                                       PBCST504 - Microcontrollers                                                        Page 14

                                Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


15. Required semester deliverables and live demonstration
15.1 Deliverables
• Working macro one-cell, six-dot servo/cam OpenBraille prototype if the concept is retained.
• Final BOM, procurement record, power diagram and provisional pin map.
• Versioned CAD, slicer settings, firmware and Braille mapping tests.
• One-dot and six-dot mechanical acceptance records.
• Per-dot calibration table and pattern-transition test suite.
• Repeatability, lifecycle, power and tactile-protocol results with limitations.
• Failure/reprint/replacement register and contributor chronology.
• Teacher-ready presentation and live-demo procedure.
• Separate confidential VPD-C7 research folder with no semester performance backfill.

15.2 Recommended five-minute live demonstration
1. Show the powered-off macro cell, six servos, rounded pins, guard/covering and separate servo power rail.
2. Connect USB, display the configuration banner and run a commanded one-dot test while explaining that command
timing is not physical confirmation.
3. Display a small frozen sequence of characters or six-bit patterns and clear/refresh them.
4. Show per-dot calibration and one repeatability result table or measurement image.
5. Run the approved safe pattern transition while showing no reset/brownout and the USB log.
6. State the limitations: macro scale, educational prototype, active retraction, no standard-compliance or patent claim.

15.3 Demo failure fallback
If classroom operation is unsafe, unreliable or too noisy, use an approved guarded video of the locked physical setup
plus a live USB/firmware demonstration and the signed measurement evidence. The fallback must not substitute a
different actuator or conceal that the physical build failed the planned gate.


16. Post-semester VPD-C7 research hypothesis


                        Figure 4. VPD-C7 research concept. It is not implemented or validated in the semester cell.

16.1 Technical question
Can a pin-side mechanical datum that sets the tactile endpoint also provide direct endpoint evidence with less
registration error and fewer silent wrong states than a passive stop plus a separately mounted sensor, while keeping
actuator current limited to independent effort/supply information?

16.2 Candidate mechanism in non-claim language
1. Redesign one post-MVP guide/pin coupon with mechanically registered upper and lower endpoint features.

    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                   Page 15

                                 Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


2. Arrange the endpoint feature so reaching it can produce a low-energy pin-side event without carrying servo power
through the contact.
3. Use external displacement and force measurement as the development oracle; do not let the candidate sensor label
itself as truth.
4. Use a separate current/voltage channel only to characterize effort, obstruction-like behavior or supply disturbance.
5. Declare an endpoint state only from qualified pin-side evidence; absent or conflicting evidence becomes
incomplete, jammed or Unknown.
6. Permit recovery/isolation only after the physical and safety behavior is experimentally qualified.

16.3 Why this is only a hypothesis
• A mechanical stop that also acts as a switch/contact is familiar engineering and may be obvious.
• The added contact may increase friction, force, bounce, contamination sensitivity or wear.
• Practical Braille pitch may not accommodate the contact and wiring.
• A separately mounted optical/magnetic sensor may perform just as well or better.
• Current may add no independent diagnostic value beyond command, time and voltage.
• The official Indian close-prior-art file and worldwide claims remain unresolved.
• No experiment currently shows a cooperative or non-additive physical effect.


17. Six-to-twelve-month future research roadmap
             Month                      Stage                          Work                         Pass evidence                    Failure action


 0-2                        Semester foundation and        Complete frozen macro MVP;        Stable one-dot baseline and a   Continue
                            search boundary                preserve mechanical/power         defined professional search     semester/publication only if
                                                           records; obtain official close-   problem                         close art anticipates the
                                                           prior-art documents; build                                        structural core
                                                           direct displacement oracle

 2-4                        Current observability and      Compare calibrated open           Held-out evidence showing       Remove current from the
                            direct sensor baseline         loop, current-only                what current can and cannot     putative invention if it adds
                                                           observation and a separate        reveal                          no independent value
                                                           direct pin sensor on one-dot
                                                           fixtures

 4-6                        Dual-purpose datum coupon      Build passive-stop, separate-     Distinct physical advantage     End VPD-C7 thesis if separate
                                                           sensor and same-datum-            fixed before confirmatory       sensor performs equivalently
                                                           contact coupons; measure          data
                                                           force, bounce, registration
                                                           and false endpoints

 6-8                        Practical-scale and            Develop smaller coupons; test     Feasible packing and stable     Hold Track D if only macro
                            contamination tests            wiring, force, dust/fiber,        endpoint evidence               geometry works
                                                           cleaning and assembly yield

 8-10                       Replacement, reassembly and    Blind servo/cam/pin/datum         Transfer across builds with     Redesign and restart after
                            lifecycle                      swaps; multiple operators;        bounded drift and no            systematic wear/failure
                                                           extended cycling and              systematic false endpoint
                                                           inspection

 10-11                      Locked held-out evidence       Run the preregistered 3,000-      Zero silently accepted wrong    Kill the route after a silent
                                                           transition silent-error test on   states plus practical           wrong state unless a
                                                           unseen                            Unknown/false isolation rates   genuinely new mechanism
                                                           units/builds/conditions                                           restarts the gate

 11-12                      Professional decision gate     Refresh worldwide search;         Useful narrow scope             Choose confidential know-
                                                           claim/FTO chart;                  supported by reproducible       how, defensive/academic
                                                           inventorship/disclosure           physical evidence               publication or stop
                                                           review; management file/no-
                                                           file decision


17.1 Research baselines and ablations
                                 Type                                                                 Required comparison

 Strong conventional baselines                                              Fixed common PWM; calibrated per-dot open loop; passive datum
                                                                            only; direct separate sensor; fixed sequential refresh


        Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                                         Page 16

                              Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


                                  Type                                                         Required comparison

 Current tests                                                         Current without endpoint contact; endpoint contact without
                                                                       current; current removed from full candidate

 State logic                                                           Unknown retained versus coerced binary decision; retry removed;
                                                                       isolation removed

 Service robustness                                                    Servo/pin/cam/datum replacement and independent reassembly

 Scale and environment                                                 Macro versus practical-scale coupons; clean versus
                                                                       contamination/wear conditions


17.2 Patent-development kill conditions
• A closer enabling reference or official Indian file discloses the defining combination.
• The same-datum contact has no measurable advantage over a passive stop plus separate sensor.
• The contact adds unacceptable force, friction, bounce, wear or debris sensitivity.
• Practical-scale packaging fails.
• Performance collapses after servo replacement, reprint, remount or reassembly.
• Current adds no independent diagnostic value or is required to certify endpoint completion.
• The locked 3,000-transition test contains a silently accepted wrong state.
• Useful scope collapses to exact hobby parts, macro dimensions or a trivial retry count.
• Institutional/professional review does not justify filing cost or disclosure risk.


18. Confidentiality, inventorship and disclosure control
18.1 Public-safe semester material
• Macro six-dot architecture, six SG90-class servos, eccentric cams, guided pins, ESP32 direct PWM and external servo
power.
• Semester budget, team roles, CAD/fabrication learning, repeatability/lifecycle and approved tactile results.
• Honest limitations: macro educational prototype, active retraction, no current-only state verification and no patent
claim.

18.2 Keep private until IPR review
• Exact VPD-C7 contact/datum geometry, materials, dimensions, circuits and thresholds.
• Unpublished comparative results against passive stops, separate sensors and current-only inference.
• Replacement/reassembly, wear, contamination and held-out silent-error datasets.
• Claim-to-experiment maps, filing strategies and contributor/inventorship analysis.

18.3 Inventorship/contribution record
Maintain dated records of who conceived each later mechanical/electrical interaction, who designed each experiment,
who created CAD/firmware, and when the mechanism was first built and tested. AI/model assistance is not
inventorship and must not replace human conception records.

18.4 Disclosure rule

 Do not rely on an assumed grace period
 Before publishing code, CAD, datasets, posters, videos, papers, competition entries or VPD-C7 details, obtain institutional
 IPR review. A patent filing or defensive publication does not create freedom to operate.


19. Decision gates and escalation rules
                 Gate                           When                                   Pass                           Fail response


 OB-G0 Teacher concept decision     Before procurement                 OpenBraille retained with            Proceed with VibeGuard or revise
                                                                       scope/budget approved                the project request


     Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                             Page 17

                              Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


               Gate                               When                                   Pass                               Fail response


OB-G1 Facility/procurement        Week 1                                 Printer/tools and first components      Do not commit full-cell schedule;
                                                                         available                               use VibeGuard fallback if needed

OB-G2 One-dot mechanics           Weeks 3-4                              Active raise/retract and                Redesign coupon; stop six-dot
                                                                         repeatability pass                      expansion

OB-G3 Six-servo power             Weeks 6-8                              No unsafe droop, reset, heating or      Upgrade supply/distribution or
                                                                         stall in planned sequence               reduce groups

OB-G4 Six-dot MDS                 Week 8                                 Correct pattern transitions and         Report partial prototype or switch
                                                                         safe operation                          according to teacher direction

OB-G5 Locked validation           Week 10                                Approved                                No patent or performance
                                                                         repeatability/lifecycle/tactile gates   overclaim; document failure
                                                                         pass

OB-G6 VPD-C7 research entry       Post-semester                          Separate design, confidentiality        Keep OpenBraille as
                                                                         and search approval                     semester/publication record only

OB-G7 Counsel-led filing          Months 11-12                           Unexpected physical effect,             Do not file; choose
evaluation                                                               enabling evidence and useful            publication/know-how/stop
                                                                         scope survive review


20. Open questions and teacher decisions
                ID                         Question / decision                          Owner                                Required by


Q1                                Should OpenBraille remain the          Project coordinator                     Before procurement
                                  semester project or should the
                                  requested VibeGuard switch be
                                  approved?

Q2                                Is the working build window            Teacher/project coordinator             Week 1
                                  approximately eight weeks or the
                                  full twelve-week plan?

Q3                                Is institutional FDM access            Amith + lab                             Week 1
                                  dependable, and what
                                  material/print limits apply?

Q4                                Which exact ESP32 and SG90             Nihad/Sreehari/Amith                    Before order
                                  seller/batch are approved?

Q5                                What quantitative tactile-             Teacher + Archa/Nihad                   Before tactile test
                                  identification protocol and
                                  participant access are approved?

Q6                                What is the approved                   Technical team + teacher                Before locked validation
                                  raised/lowered position band for
                                  the macro cell?

Q7                                Is the 5 V / 3 A target supply         Amith + Nihad                           Before full integration
                                  adequate under the actual six-
                                  servo sequence?

Q8                                What content may be disclosed          IPR cell / project owner                Before publication or competition
                                  publicly before institutional IPR
                                  review?

Q9                                Should VPD-C7 remain only a            Team + institution                      After MVP evidence
                                  confidential future option after the
                                  semester?


21. Teacher approval and conditions
                           Decision item                                                             Teacher response

Semester project                                                         Retain OpenBraille / Approve VibeGuard switch / Revise and
                                                                         resubmit

Frozen OpenBraille scope                                                 Approved / Approved with conditions / Not approved


     Dept. of CSE (CY)                                 PBCST504 - Microcontrollers                                                         Page 18

                                Topic: OpenBraille - Semester Architecture and Future Research Reference Dossier


                           Decision item                                                           Teacher response

 Expected budget near ₹3,000                                             Approved / Revise

 External 5 V servo supply and safety controls                           Approved / Lab review required

 One-dot-first procurement gate                                          Approved / Revise

 Tactile participant protocol                                            Approved / Separate ethics/access review required

 Future VPD-C7 treatment                                                 Confidential post-semester only / Not approved / Further review

 Teacher conditions

 Signature and date


22. Source basis
This dossier was prepared from the controlled Project mC master package. The main evidence layers are:

                          Evidence layer                                                           Controlled source

 Project authority                                                       Engineering Design Review; Project mC Decision Register v1.2;
                                                                         approved Phase 3C Portfolio Closure Memo

 Common evidence                                                         Concept Evidence Matrix; Uncertainty and Test Register

 OpenBraille technical authority                                         Final OpenBraille Architecture Report; Memory; SOP

 Comparative decision context                                            Two final cross-concept adjudications - treated as context, not votes

 Future research boundary                                                OpenBraille Pre-Build Future Patent-Case Simulation

 Costing and teacher context                                             Project mC Teacher Documents - Master Evidence, Costing and
                                                                         Decision Basis

 Previous presentation                                                   Final OpenBraille zeroth-review presentation dated 30-07-2026


22.1 Current official specification and price references
• Espressif, ESP32-WROOM-32 data sheet: https://www.espressif.com/sites/default/files/documentation/esp32-
wroom-32_datasheet_en.pdf
• Espressif, ESP32-S3 product page and DevKitC-1 guide: https://www.espressif.com/en/products/socs/esp32-s3
• TowerPro, SG90 analog servo specifications: https://towerpro.com.tw/product/sg90-analog/
• Indian price snapshots and procurement cautions are recorded in the Master Evidence, Costing and Decision Basis
and must be refreshed on purchase day.
Prepared for academic project planning. The future research section is a management and experimental roadmap, not legal advice,
           patentability clearance, freedom-to-operate clearance, a filing recommendation or a promise of patent grant.


    Dept. of CSE (CY)                                   PBCST504 - Microcontrollers                                               Page 19
