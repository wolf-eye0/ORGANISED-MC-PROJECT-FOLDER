# Source Extraction

- Chapter: `05` — OpenBraille Patent Evidence and Future Research Path
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_SUPPORTING`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`
- Current SHA-256: `b4ef1d7301d5e0a669185681160cb20c8a85d2464b822c3c569798238f13e27b`
- Extraction method: `DOCX_XML`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

PROJECT mC

OPENBRAILLESEMESTER ARCHITECTUREAND FUTURE RESEARCH REFERENCE DOSSIER

Frozen Macro Six-Dot Build Plan, Validation Programme and Post-Semester VPD-C7 Research Path

Control item

Value

Course

PBCST504 - Microcontrollers Micro Project

Programme

B.Tech Computer Science and Engineering (Cyber Security)

Group

Group 8

Document status

Complete retained-reference and fallback implementation dossier

Current portfolio status

VibeGuard switch requested; OpenBraille remains the fully documented alternative

Frozen architecture

One macro six-dot cell; six SG90-class servos; eccentric cams; guided pins; ESP32 direct PWM

Expected semester budget

Approximately ₹2,984; conservative envelope approximately ₹4,909

Future mechanism

VPD-C7 research hypothesis - unbuilt, confidential and evidence-gated

Controlling decisionThis dossier does not override the current request to adopt VibeGuard. It provides the complete OpenBraille plan if the teacher retains the zeroth-review concept, and preserves OpenBraille as a future accessibility/mechatronics research route.

Patent boundaryThe macro six-servo semester prototype is conventional and is not represented as patent-ready. VPD-C7 is a separate post-semester hypothesis that must be redesigned, built, compared and professionally reviewed before any filing decision.

Prepared from the controlled Project mC authority set and the Master Evidence, Costing and Decision Basis. This document is an engineering reference plan, not a patent opinion, standards-compliance declaration or promise of grant.

Document control and approval use

Control item

Value

Architecture baseline

Frozen OpenBraille Phase 3C macro six-servo/cam architecture

Return-motion rule

Active servo-driven cam retraction unless a usable passive return is physically proved

Power baseline

External regulated 5 V servo supply; 5 V/3 A procurement target; measured droop controls acceptance

USB role

Serial command input and logs; not six-servo power

Semester boundary

No moving roller, encoder, RAMPS/Mega, continuous paper or electromagnetic substitution

Future boundary

VPD-C7 only on a separate post-MVP coupon; current never certifies pin height alone

Approval checkpoints required before an OpenBraille procurement freeze

1. Teacher confirmation that OpenBraille, rather than the requested VibeGuard alternative, remains the semester implementation.

2. Confirmation of the effective build window and dependable institutional FDM-printer access.

3. Approval of the one-dot-first mechanical validation plan before six servos and full-cell materials are committed.

4. Approval of the external 5 V power arrangement, pinch-point controls and tactile-participant protocol.

5. Approval of quantitative repeatability, cycle-life and pattern-test criteria before the locked validation run.

Executive reference decision

Complete alternative semester planOpenBraille is technically buildable within the ₹5,000 ceiling and offers a strong accessibility demonstration. Its execution risk is concentrated in FDM tolerances, cam/follower friction, active retraction, six-servo power behavior and trustworthy tactile-state validation. This dossier is therefore retained as the complete fallback/reference plan while VibeGuard remains the recommended semester choice.

The correct semester claim is narrow: one macro-scale six-dot cell accepts a character or dot pattern over USB/serial, commands six independent servo/cam channels, produces repeatable raised/lowered tactile states, and reports measured limitations. The project must not be presented as a standards-compliant commercial Braille display or as a patented actuator mechanism.

Success definition at a glance

Layer

Required semester result

Evidence

Mechanical

Six independently moving macro dots with active raise/retract and safe rounded pin tips

CAD/build IDs, caliper measurements, photographs, cycle logs

Electrical

Stable ESP32 control and external servo rail without brownouts or unsafe heating

Voltage/current observations, reset log, power checklist

Firmware

Correct character-to-six-dot mapping, per-dot calibration and USB commands/logs

Unit tests, configuration record, pattern test report

Validation

Repeatability, lifecycle, pattern-transition and approved tactile evidence

Locked test sheet, raw records, failed-run register

Scope honesty

Macro educational prototype; no physical-state claim from command timing alone

Explicit limitations in report and live demonstration

Future separation

VPD-C7 kept outside the semester architecture

Separate research folder and disclosure controls

1. Purpose, audience and scope

1.1 Purpose

This dossier converts the frozen OpenBraille Phase 3C architecture into a procurement-aware and execution-ready semester plan. It defines the hardware, mechanical build order, electrical integration, firmware, calibration, validation, team ownership, semester schedule and future-research boundary.

1.2 Audience

• Project coordinator and teacher: concept-retention decision, scope, budget, safety and review gates.

• Five-member student team: CAD, fabrication, firmware, assembly, testing, evidence and demonstration responsibilities.

• Department laboratories: FDM access, tools, metrology and safety support.

• Accessibility or tactile-test reviewers: honest macro-prototype scope and participant protocol.

• Institutional innovation/IPR reviewers: separation between the public semester cell and confidential VPD-C7 work.

1.3 Scope hierarchy

Scope tier

Included

Not included

Semester OpenBraille

One macro six-dot cell; six servos/cams/pins; direct PWM; active retraction; USB; measurements

Standards-compliant product, multi-cell line, production design, patent claim

Semester instrumentation

Calipers/camera, voltage/current checks and test scripts used as development evidence

Permanent endpoint contacts or current-only state inference

Post-semester VPD-C7

Separate coupon studying a datum that sets and directly evidences pin endpoints

Assumed performance, filing-ready claims or automatic inclusion in the semester cell

2. Engineering identity and problem definition

2.1 Engineering identity

OpenBraille is an assistive embedded-system experiment focused on lowering the cost of refreshable tactile output. Its semester purpose is not to compete with commercial displays, but to test whether a simple low-cost actuation channel can create one repeatable six-dot cell suitable for education and engineering study.

2.2 Semester engineering hypothesis

Hypothesis to testA macro-scaled servo-and-cam mechanism can produce repeatable raised and lowered tactile states for one six-dot Braille cell within the student budget and schedule, while accepting that the prototype is not commercial-scale or standards-compliant.

2.3 What the hypothesis does not claim

• It does not claim that servo + cam + Braille pin actuation is novel.

• It does not claim commercial Braille pitch, force, refresh speed, noise or lifetime.

• It does not assume a passive servo spring retracts the pin.

• It does not treat a PWM command, elapsed time or servo current as direct proof of tactile-pin height.

• It does not establish a patent or freedom to operate.

3. Frozen system architecture

Figure 1. Frozen macro six-dot architecture and explicit semester scope boundary.

3.1 Subsystem boundaries

Subsystem

Inputs

Outputs

Owner acceptance

USB/serial interface

Character, pattern or test command

Parsed request, acknowledgement and log line

Commands are deterministic, versioned and unit-tested

ESP32 control

Pattern, per-dot calibration and fixed sequencing rules

Six PWM outputs and timestamped command records

No invalid GPIO use, unstable resets or hidden configuration

Six actuator channels

5 V servo power and PWM

Cam rotation and follower displacement

Each channel accepted on a one-dot fixture before full-cell assembly

Mechanical cell

Six channel motions

Six guided raised/lowered tactile pins

No binding, unsafe tips or adjacent-channel interference

Power distribution

External regulated 5 V and common ground

Stable servo rail and logic operation

No USB servo power, brownout or unsafe heating

Development measurement

Pin position, cycle count, rail behavior and operator observations

Evidence package and limitations

External measurement remains the truth source for physical position

3.2 Frozen architecture controls

• One macro-scale six-dot cell only.

• Six SG90-class servos, one eccentric cam and one guided vertical pin per dot.

• ESP32 local direct-PWM control; no intermediate motor driver is required for the servo signal.

• FDM frame/guides/cams and external regulated servo power.

• Active servo-driven retraction unless a procured mechanism proves a reliable passive return under load.

• No moving roller, encoder wheel, RAMPS/Mega embosser, continuous-paper system or electromagnetic substitution.

4. Detailed hardware architecture and BOM

4.1 Required purchased and fabricated items

Item

Qty

Exact semester role

Expected

Conservative

Acceptance/procurement rule

ESP32 development board

1

Six PWM channels, USB/serial commands and logging

₹400

₹899

Verified WROOM-32 DevKit baseline; ESP32-S3 authorized fallback. Record pinout and regulator.

SG90-class servo

6

One independent eccentric-cam actuator per dot

₹120 each / ₹720

₹142 each / ₹852

Buy one consistent batch where possible; inspect every unit; no passive-return assumption.

5 V / 3 A regulated adapter

1

External servo supply with test headroom

₹289

₹408

Connector and regulation verified; adequacy controlled by measured droop and stall tests.

1,000 µF electrolytic capacitor

1-2

Servo-rail transient buffering

₹25

₹50

Install near distribution; voltage rating above 5 V; not a substitute for an adequate supply.

FDM frame, guides, cams and followers

1 cell

Macro mechanical structure

₹450

₹900

Expected case assumes institutional printer access; print a single-dot coupon first.

Stainless pins/rod with rounded tips

6 + spare

Guided tactile dots

₹250

₹400

Local quote; polished/rounded, safe for repeated touch, dimensions recorded.

Fasteners, servo mounts and cable management

1 lot

Alignment, assembly, strain relief and guards

₹300

₹500

Final quantity follows CAD and physical servo dimensions.

Perfboard, wires, headers and connectors

1 lot

Power distribution and stable PWM wiring

₹200

₹350

Servo current never routed through ESP32 3.3 V rail or thin USB wiring.

USB data cable

1

Serial input and logs

₹100

₹150

Reusable cable acceptable after connection reliability check.

Budget layer

Low

Expected

Conservative

Required hardware/material subtotal

₹1,866

₹2,734

₹4,509

Delivery/local variability/replacement allowance

₹100

₹250

₹400

Semester planning total

₹1,966

₹2,984

₹4,909

Budget decisionUse approximately ₹3,000 as the expected teacher-facing budget. The conservative case remains below ₹5,000 only when institutional printing is available and full-cell reprints are limited. One or two spare servos are useful but should be approved separately.

4.2 Reusable or institutional equipment

Equipment

Use

Required status

Laptop with Arduino IDE and Python

Firmware, serial commands, analysis and reporting

Assumed available

FDM printer and slicing software

Frame, guides, cams, followers and coupons

Material dependency; access must be confirmed

Digital calipers

Pin travel, spacing, clearances, repeatability and wear

Required

Multimeter

Power, continuity and servo-rail checks

Required

Bench supply with current limit

One-servo bring-up and fault-safe testing

Strongly recommended / borrowed

Oscilloscope or logic analyzer

PWM and rail-transient checks

Useful but not essential

Camera / fixed measurement jig

External visual ground truth and configuration record

Required for credible evidence

Basic hand tools and soldering station

Assembly, finishing and final wiring

Institutional/reusable

Tactile participant access and approved protocol

Raised/lowered and pattern distinguishability

Not confirmed; teacher/ethics decision

5. Mechanical architecture and one-dot-first build

Figure 2. One-dot channel and the separation between command, physical motion and development ground truth.

5.1 Mechanical design rules

1. Start with one independently testable servo + cam + follower + pin coupon. Do not print the full cell before the coupon moves freely.

2. Use macro spacing and travel as a documented educational design choice. A starting target near 300% of standard sign-Braille geometry may guide CAD, but the prototype must not be labelled standards-compliant.

3. Use rounded, smooth tactile tips and guard all pinch points around cams and servo horns.

4. Set pin-guide clearance through printed tolerance coupons and measured finishing; nominal CAD dimensions do not prove physical clearance.

5. Use active cam-driven raise and retract positions. Do not rely on an unverified servo spring or gravity return.

6. Record each printed part revision, orientation, material, measured dimensions, sanding/finishing and assembly operator.

7. Treat each channel as replaceable for test purposes, but do not present modular replacement as a novel patent feature.

5.2 Provisional geometry and acceptance parameters

Parameter

Starting design basis

Acceptance rule

Cell scale

Macro single cell, approximately 3x commercial sign-Braille pitch as an engineering starting point

Final CAD and measured cell clearly labelled non-standard

Raised travel

Approximately 1.5 mm starting target

Teacher-approved tactile and repeatability test controls final value

Pin material

Approximately 2 mm stainless rod with rounded tip

No sharp edge, binding, corrosion or unsafe surface

Cam throw

Set through one-dot CAD/coupon to create required travel with margin

No stall, follower loss or adjacent interference

Guide clearance

Derived from printed tolerance coupon

Free motion under the selected load with repeatable alignment

Actuation sequence

Fixed sequential or bounded group of changed dots

No brownout, unsafe peak or excessive refresh delay

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

Domain

Source

Loads

Rule

Logic / USB

Laptop USB to ESP32 DevKit

ESP32 and serial interface

Do not back-feed a second 5 V source into an unverified board while USB is connected

Servo rail

External regulated 5 V / 3 A target

Six SG90-class servos

Separate branch and conductors sized for servo current; bulk capacitor near distribution

Signal reference

Common ground

ESP32 PWM and servo signal reference

Use star/controlled grounding; inspect for resets and noise

Measurement

Multimeter / optional scope

Servo rail and logic rail

Measurements must not create unsafe shorts or loose probes near moving cams

6.2 Provisional ESP32-WROOM-32 pin assignment

Function

Provisional GPIO

Notes

Dot 1 PWM

GPIO 16

Output-capable; verify board label

Dot 2 PWM

GPIO 17

Output-capable; verify board label

Dot 3 PWM

GPIO 18

Output-capable; avoid conflict with other planned peripherals

Dot 4 PWM

GPIO 19

Output-capable

Dot 5 PWM

GPIO 21

Output-capable

Dot 6 PWM

GPIO 22

Output-capable

USB serial

Onboard USB-UART

Primary command/log interface

Optional status LED

GPIO 23 or onboard LED where available

Not part of the six-dot mechanism; verify polarity/board mapping

Implementation noteThis is a Phase 4 wiring proposal, not a source-file mandate. Revalidate every pin against the exact purchased DevKit and do not use boot-strapping or input-only pins without understanding their behavior.

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

Module

Responsibility

Required outputs/tests

Configuration manager

Board variant, pin map, cell/build ID, PWM calibration and sequence policy

Startup banner and configuration record

USB command parser

Accept character, six-bit pattern, clear, test and calibration commands

Malformed-command tests and deterministic responses

Braille mapping table

Map supported characters to six-dot patterns

Unit test independent of hardware

PWM/channel manager

Apply per-dot up/down pulse widths and fixed sequencing

Logic-analyzer/servo acceptance and no illegal overlap

Calibration manager

Store per-dot command values established with external measurement

Versioned calibration table and reset procedure

Pattern transition engine

Move only changed dots, apply settle interval and update commanded state

Transition log and pattern suite

Fault/log manager

Record resets, invalid commands, manual faults and channel disable state

Human-readable USB log; no false physical-state claim

Test mode

Cycle one channel or selected patterns under operator control

Repeatability/lifecycle scripts

7.2 Repository and configuration structure

Folder/file

Purpose

firmware/

ESP32 source, board configuration and release tags

firmware/config/

Pin map, per-dot calibration and build identifiers

firmware/tests/

Character mapping and command-parser unit tests

cad/

Versioned frame, guide, cam, follower and coupon designs

fabrication/

Slicer settings, material, orientation and post-processing record

protocols/

Electrical, mechanical, cycle, tactile and demo procedures

data/

Measurements, cycle logs, power observations and fault records

evidence/

Photographs, videos, signed checklists and final locked results

7.3 Command and state semantics

The firmware should distinguish commanded state from verified physical state. Without a permanent pin sensor, the runtime may record that a PWM command and settle interval completed, but it must not label that event UPPER_CONFIRMED or LOWER_CONFIRMED. Physical confirmation belongs to external development measurement and the approved tactile protocol.

State

Meaning

Allowed evidence

Exit/exception

STARTUP

Board and configuration initialization

Firmware and board checks

FAULT on invalid configuration

READY

No active transition; accepts command

Commanded pattern record

RAISING / LOWERING / TEST

RAISING

One or more selected channels commanded toward up position

PWM command and timestamp

SETTLE_WAIT after command interval

LOWERING

Selected channels commanded toward down position

PWM command and timestamp

SETTLE_WAIT after command interval

SETTLE_WAIT

Fixed mechanical settling delay

Timer only

COMMAND_FINISHED; not physical confirmation

COMMAND_FINISHED

Requested command sequence ended

Command log

External tests decide physical correctness

FAULT/ISOLATED

Manual/operator or electrical/mechanical fault recorded

Fault input, reset, test observation

Operator-cleared after inspection

8. Calibration, sequencing and control logic

8.1 Per-dot calibration process

1. Assign a permanent channel and servo identity.

2. Use external calipers/camera or a fixed displacement jig to measure the lowered and raised pin positions.

3. Sweep the up command in small controlled increments to find the minimum repeatable raised position without stall or excessive load.

4. Repeat for active retraction and verify the pin returns to the approved lowered band.

5. Repeat across multiple cycles and store the selected command values with hardware/build IDs.

6. Invalidate or recheck calibration after servo replacement, cam/guide reprint or major reassembly.

8.2 Fixed sequencing policy

The semester system should use a simple fixed sequence: identify changed dots, lower dots that must clear, then raise dots that must set, with a bounded number of simultaneously moving channels chosen only after measured power testing. Dynamic current-aware sequencing belongs to future research and must not be backfilled into the frozen MVP.

8.3 Pattern transition rules

Rule

Purpose

Move only changed dots

Reduces unnecessary cycles, noise and power

Active retract before conflicting raise

Prevents ambiguous intermediate patterns

Fixed settle time per tested channel group

Makes behavior reproducible and loggable

Reject malformed/unsupported command

Protects mapping and state integrity

Manual stop on stall, heating or binding

No automatic recovery without evidence

Calibration version stored with every test

Prevents results from being separated from command values

8.4 Physical-truth boundary

Do not overclaim stateA servo angle, PWM pulse, elapsed time, current rise or visible cam movement does not automatically prove acceptable tactile-pin height. Semester physical truth comes from external measurement and an approved tactile evaluation. Current sensing may be used for power/safety observation, not endpoint certification.

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

Evidence type

What it supports

What it does not support

USB command log

Requested patterns, timestamps and firmware behavior

Actual tactile height

Calipers/camera/displacement jig

Development measurement of pin positions

Long-term tactile usability by itself

Power measurements

Supply adequacy, peaks, droop and resets

Endpoint correctness

Cycle log

Repeatability and mechanical failure history

Commercial lifetime

Tactile protocol

Participant distinguishability under the approved setup

Universal user performance or standards compliance

Photographs/video

Configuration and visible operation

Precise dimensions without measurement

9.3 Final evidence package

Evidence file

Minimum content

Configuration record

Board, pins, six servo IDs, CAD/slicer versions, power source and calibration table

Mechanical acceptance

One-dot and six-dot dimensions, travel, free-motion and safety checklist

Electrical acceptance

Supply voltage, resets, wiring, capacitor and combined-pattern observations

Pattern test

Supported character/pattern suite and exact pass/fail outputs

Repeatability/lifecycle

Per-channel measurements, cycle counts and failures

Tactile protocol report

Approved method, participants/ethics status, randomization, results and limitations

Failure register

Binding, wear, servo replacement, reprints, rejected runs and corrective action

Final demo package

Frozen firmware/CAD, demo script, backup evidence and limitations

10. Validation and acceptance programme

10.1 Validation stages

Stage

Question

Minimum evidence

Stop/fallback

OB-V0 Component acceptance

Are the ESP32, first servo, supply and tools usable?

Board/USB check, servo sweep, adapter polarity/voltage

Replace failed component before CAD freeze

OB-V1 One-dot mechanics

Can one printed channel raise and actively retract without binding?

Measured motion, photographs and repeated cycles

Redesign guide/cam before ordering full batch

OB-V2 Calibration

Can per-dot command windows produce repeatable positions?

External measurement across cycles

Change geometry or actuator; do not tune blindly

OB-V3 Six-dot integration

Do six channels coexist without interference and brownout?

Pattern commands, power observation and mechanical inspection

Use fixed sequencing, stronger supply or rebuild distribution

OB-V4 Pattern correctness

Does character mapping produce intended six-dot states?

Unit tests and physical pattern checks

Fix mapping/configuration before user testing

OB-V5 Repeatability/lifecycle

Does the mechanism retain position and motion over approved cycles?

100-cycle precision set and at least 1,000 total actuations

Record failure; redesign or limit claim

OB-V6 Tactile evaluation

Are raised/lowered dots and selected patterns distinguishable?

Teacher-approved blinded protocol

Adjust geometry or report MDS not achieved

OB-V7 Locked demonstration

Can the frozen build reproduce the result safely?

Signed checklist, frozen configuration and final evidence

Use approved backup evidence; no late redesign

10.2 Proposed semester acceptance targets for teacher approval

Status of numbersThe project authority contains some architecture-level repeatability and lifecycle targets, but the tactile participant threshold is not frozen. The following set should be preregistered and approved before the locked run.

Metric

Proposed target

Why it matters

Channel function

All six channels independently raise and actively retract throughout the final pattern sequence

Minimum six-dot cell functionality

Repeatability

≤0.1 mm position variation over 100 measured cycles under the approved setup

Source-derived architecture target; measures mechanical consistency

Lifecycle screen

At least 1,000 actuations without mechanical failure that invalidates the demo

Early engineering screen, not product lifetime

Pattern mapping

100% correct output for the frozen supported character/test set

Separates firmware mapping from mechanical failure

Power integrity

No brownout/reset, connector heating or unsafe voltage collapse in the locked sequence

Electrical safety and reliability

Tactile distinguishability

Teacher-approved blinded threshold and trial count fixed before testing

Avoids inventing or post-hoc selecting a success rate

Failure honesty

Every incomplete/bound transition is logged; no command-complete event relabelled as physically verified

Evidence integrity

Budget

Final semester spend ≤₹5,000, with preferred target near ₹3,000

Course requirement

10.3 Required performance reporting

• Per-dot raised and lowered position distributions, not only average travel.

• Pattern-level pass/fail counts and the exact supported character set.

• Power/reset observations for one, multiple and worst planned transitions.

• Cycle count, wear inspection and parts replaced.

• Tactile results with protocol, participant context and limitations.

• Negative evidence, binding, failed prints and calibration changes.

• Explicit statement that the macro prototype does not establish commercial-scale feasibility.

11. Twelve-week semester roadmap

Week

Primary work

Owner(s)

Measurable output

Exit criterion

Fallback

1

Teacher decision, scope freeze, FDM/tool audit and first procurement

Nihad + team; Amith fabrication audit

Approved concept status; one-servo order; printer/tool booking; risk register

No full-cell purchase until one-dot gate and teacher direction are confirmed

Use available verified ESP32/servo variants without changing architecture

2

ESP32/USB bring-up, one bare servo and power acceptance

Sreehari + Amith

Commanded servo sweep; adapter/polarity record; provisional pin map

Stable board/serial and safe one-servo motion

Replace failed board/servo/supply before CAD integration

3

Print tolerance coupons and one-dot frame/cam/follower

Amith + Nihad

Measured coupon set; one-dot assembly; CAD/build ID

Pin moves freely and cam produces controllable travel

Adjust guide/cam dimensions; laser-cut guide fallback only if approved

4

Active raise/retract calibration and single-dot repeatability

Amith + Sreehari; Sreeprada tests

Per-dot calibration procedure; 100-cycle single-dot dataset

Stable raised/lowered bands without binding or unsafe stall

Change geometry/servo before multiplying channels

5

Procure/accept remaining servos and fabricate six-dot parts

Amith + Sreeprada inventory

Six accepted servo IDs; completed printed parts; assembly checklist

Each channel passes independent bench test

Use spares or pause channels; do not hide batch variation

6

Six-dot mechanical and electrical integration

Nihad + Amith + Sreehari

Assembled cell; external rail; six PWM channels; command logs

All six move independently; no brownout/interference

Fixed sequential actuation, supply/distribution revision or rebuild

7

Braille mapping, pattern transitions and per-dot calibration

Sreehari + Sreeprada

Supported character set; mapping unit tests; calibration table

Frozen test patterns produce correct commanded states

Reduce demo set while keeping mapping evidence honest

8

Power, safety, repeatability and failure-mode testing

Amith + Nihad; Sreeprada runs

Worst planned transition record; fault/reprint log; safety review

No unsafe heating, reset, pinch or uncontrolled motion

Limit actuation group, strengthen guard/supply or redesign

9

Lifecycle screen and tactile-protocol approval

Nihad + Archa; teacher/participant coordination

Cycle progress; approved blinded protocol or documented access limit

Mechanism survives and protocol is approved before use

Report tactile validation unavailable rather than improvising

10

Locked pattern/repeatability/tactile validation

Full team; test led by Sreeprada

Frozen configuration and signed result sheets

Approved targets met without post-result calibration changes

Record failure; use honest partial-MDS conclusion

11

Final report, source records and live-demo rehearsal

Archa + Nihad; technical review by Sreehari/Amith

Final BOM, CAD/firmware versions, results, limitations and demo script

Every technical claim traces to evidence

Remove unsupported claims and use backup video only if approved

12

Contingency, repair-only window and final delivery

Full team

Stable final build and archived evidence package

No late VPD-C7 or architecture expansion

Submit the strongest verified semester result

Schedule ruleThe minimum demonstrable cell should work by the end of Week 8. Weeks 9-12 are for lifecycle, tactile evidence, recovery and presentation. VPD-C7 hardware must not enter the semester critical path.

12. Team roles, actual members and accountability

Role statusThe following map mirrors the established five-member structure. It is a proposed assignment for team approval; it deliberately gives mechanical work substantial ownership because that is OpenBraille’s critical risk.

Member

Proposed primary role

Specific OpenBraille ownership

Review/backup obligation

Nihad P C - JEC24CC044

Technical integration lead / project manager

Architecture control, schedule, interface decisions, validation protocol, final integration and evidence integrity

Backs up firmware and hardware; approves configuration freezes

Sreehari K - JEC24CC055

Firmware and embedded-control lead

USB command parser, Braille mapping, PWM/channel manager, calibration storage, test scripts and logs

Nihad reviews releases; Sreeprada executes scripted tests

Amith Krishna Das - JEC24CC016

Mechanical, hardware and power lead

CAD/FDM, cam/follower/guide design, servo acceptance, power rail, assembly and safety inspection

Nihad reviews interfaces/safety; Sreehari checks control requirements

Sreeprada K S - JEC24CC056

Learner, test and inventory assistant

Inventory, servo/build labels, cycle scripts, measurements, photos, test registry and repeated independent trials

Works from signed procedures; learns USB operation and calibration workflow

Archa Pramod - JEC24CC022

Documentation, teacher communication and demonstration lead

Weekly records, teacher-safe explanations, tactile-test coordination, live-demo script, final presentation and source register

Technical statements reviewed by Nihad, Sreehari and Amith

12.1 Responsibility rules

• Every critical subsystem has one primary owner, one technical reviewer and one written checklist.

• No one changes CAD, PWM calibration, power wiring or test labels without a dated configuration update.

• The learner/test role is evidence-critical and must run independent repetitions, not only observe.

• The documentation lead does not publish VPD-C7 details without technical and IPR review.

• Nihad acts as integration failsafe, but CAD, firmware and validation must remain independently owned and reviewable.

13. Procurement, acceptance and configuration control

13.1 Procurement sequence

1. Confirm teacher decision and institutional FDM access.

2. Buy one verified ESP32 board, one SG90-class servo, the external supply and basic mechanical material first.

3. Pass the one-dot mechanical/active-retraction gate before buying or committing the remaining servo batch and full-cell prints.

4. Buy the remaining servos from one consistent seller/batch where practical and record every identity.

5. Fabricate the full frame only after the physical servo and pin dimensions are measured.

6. Purchase spares only when acceptance or delivery risk justifies them within the conservative envelope.

13.2 Component acceptance record

Component

Acceptance checks

Reject if

ESP32

Reliable boot/USB, exact board identity and usable output GPIOs

Unknown pinout, repeated disconnect, overheating or unstable regulator

SG90 servo

Smooth sweep, no damaged gears, stable horn/shaft and repeatable response

Dead zone, severe jitter, gear damage, overheating or inconsistent return command

5 V adapter

Correct polarity, stable loaded output, adequate connector and no overheating

Unsafe voltage, instability, excessive droop or poor connector

FDM coupon

Measured clearance, free pin motion, no cracks or warped datum surfaces

Binding, unsafe roughness, large warp or non-repeatable fit

Cam/follower

Smooth engagement and required travel without losing contact

Stiction, follower jump, crack or unsafe pinch exposure

Pin/tip

Straight, smooth, rounded and securely retained

Sharp edge, looseness, corrosion or unsafe touch surface

13.3 Configuration ID format

Recommended format: OB-[cell/build]-[dot/servo]-[CAD]-[firmware]-[protocol]-[session]. Example: OB-C01-D3-SV05-CAD0.4-FW0.6-P03-R012. The exact format may change, but every measurement, image and result must identify the physical and software configuration.

14. Risk register and mitigation

Risk

Likelihood / impact

Early indicator

Mitigation

Decision consequence

FDM guide/cam tolerance and friction

High / High

Pin does not slide freely; variable travel; follower drag

One-dot coupons, measured clearance, material/print iteration, limited finishing

Do not proceed to six-dot assembly until passed

No usable passive return

High / Medium

Pin remains raised or servo does not return under load

Use active commanded retraction; remove passive-return language

Architecture remains valid with corrected control description

Servo batch variation/backlash

Medium / High

Different travel for common PWM; jitter or gear play

Consistent batch, per-dot calibration, spare/replace failed unit

May increase calibration and evidence burden

Six-servo brownout or rail droop

Medium / High

ESP32 reset, adapter sag, connector heating

Separate 5 V rail, bulk capacitor, fixed sequencing, measured load

Upgrade supply/distribution or reduce simultaneous motion

Pin tip unsafe or tactility poor

Medium / High

Sharp/loose tip or participant cannot distinguish states

Rounded tips, geometry iteration, approved tactile protocol

MDS may fail even when motion is visible

Cam/follower wear

Medium / Medium

Position drift, dust, roughness or increased noise

Material choice, inspection, lifecycle screen, replaceable coupon

Limit claims and redesign if systematic

CAD/print schedule slippage

High / Medium

Multiple full reprints or printer unavailable

Single-dot gate, modular prints, early lab booking, controlled fallback

May force reduced demo or switch to VibeGuard

Firmware mapping/calibration error

Low / Medium

Wrong pattern despite correct mechanics

Independent unit tests and configuration versioning

Fix before tactile validation

Tactile participant/protocol unavailable

Medium / Medium

No approved access or trial design

Secure approval early; document visual/mechanical evidence separately

Do not claim tactile success without the test

Macro prototype overstated as product

Medium / High

Slides imply standard compliance or commercial readiness

Teacher-safe wording, explicit dimensions/limits and review

Remove unsupported claim before presentation

Future patent concept leaks into MVP

Medium / Medium

VPD-C7 contact/current details added late

Separate folders, approval gate and confidentiality rule

Exclude from semester build and results

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

2. Connect USB, display the configuration banner and run a commanded one-dot test while explaining that command timing is not physical confirmation.

3. Display a small frozen sequence of characters or six-bit patterns and clear/refresh them.

4. Show per-dot calibration and one repeatability result table or measurement image.

5. Run the approved safe pattern transition while showing no reset/brownout and the USB log.

6. State the limitations: macro scale, educational prototype, active retraction, no standard-compliance or patent claim.

15.3 Demo failure fallback

If classroom operation is unsafe, unreliable or too noisy, use an approved guarded video of the locked physical setup plus a live USB/firmware demonstration and the signed measurement evidence. The fallback must not substitute a different actuator or conceal that the physical build failed the planned gate.

16. Post-semester VPD-C7 research hypothesis

Figure 4. VPD-C7 research concept. It is not implemented or validated in the semester cell.

16.1 Technical question

Can a pin-side mechanical datum that sets the tactile endpoint also provide direct endpoint evidence with less registration error and fewer silent wrong states than a passive stop plus a separately mounted sensor, while keeping actuator current limited to independent effort/supply information?

16.2 Candidate mechanism in non-claim language

1. Redesign one post-MVP guide/pin coupon with mechanically registered upper and lower endpoint features.

2. Arrange the endpoint feature so reaching it can produce a low-energy pin-side event without carrying servo power through the contact.

3. Use external displacement and force measurement as the development oracle; do not let the candidate sensor label itself as truth.

4. Use a separate current/voltage channel only to characterize effort, obstruction-like behavior or supply disturbance.

5. Declare an endpoint state only from qualified pin-side evidence; absent or conflicting evidence becomes incomplete, jammed or Unknown.

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

Month

Stage

Work

Pass evidence

Failure action

0-2

Semester foundation and search boundary

Complete frozen macro MVP; preserve mechanical/power records; obtain official close-prior-art documents; build direct displacement oracle

Stable one-dot baseline and a defined professional search problem

Continue semester/publication only if close art anticipates the structural core

2-4

Current observability and direct sensor baseline

Compare calibrated open loop, current-only observation and a separate direct pin sensor on one-dot fixtures

Held-out evidence showing what current can and cannot reveal

Remove current from the putative invention if it adds no independent value

4-6

Dual-purpose datum coupon

Build passive-stop, separate-sensor and same-datum-contact coupons; measure force, bounce, registration and false endpoints

Distinct physical advantage fixed before confirmatory data

End VPD-C7 thesis if separate sensor performs equivalently

6-8

Practical-scale and contamination tests

Develop smaller coupons; test wiring, force, dust/fiber, cleaning and assembly yield

Feasible packing and stable endpoint evidence

Hold Track D if only macro geometry works

8-10

Replacement, reassembly and lifecycle

Blind servo/cam/pin/datum swaps; multiple operators; extended cycling and inspection

Transfer across builds with bounded drift and no systematic false endpoint

Redesign and restart after systematic wear/failure

10-11

Locked held-out evidence

Run the preregistered 3,000-transition silent-error test on unseen units/builds/conditions

Zero silently accepted wrong states plus practical Unknown/false isolation rates

Kill the route after a silent wrong state unless a genuinely new mechanism restarts the gate

11-12

Professional decision gate

Refresh worldwide search; claim/FTO chart; inventorship/disclosure review; management file/no-file decision

Useful narrow scope supported by reproducible physical evidence

Choose confidential know-how, defensive/academic publication or stop

17.1 Research baselines and ablations

Type

Required comparison

Strong conventional baselines

Fixed common PWM; calibrated per-dot open loop; passive datum only; direct separate sensor; fixed sequential refresh

Current tests

Current without endpoint contact; endpoint contact without current; current removed from full candidate

State logic

Unknown retained versus coerced binary decision; retry removed; isolation removed

Service robustness

Servo/pin/cam/datum replacement and independent reassembly

Scale and environment

Macro versus practical-scale coupons; clean versus contamination/wear conditions

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

• Macro six-dot architecture, six SG90-class servos, eccentric cams, guided pins, ESP32 direct PWM and external servo power.

• Semester budget, team roles, CAD/fabrication learning, repeatability/lifecycle and approved tactile results.

• Honest limitations: macro educational prototype, active retraction, no current-only state verification and no patent claim.

18.2 Keep private until IPR review

• Exact VPD-C7 contact/datum geometry, materials, dimensions, circuits and thresholds.

• Unpublished comparative results against passive stops, separate sensors and current-only inference.

• Replacement/reassembly, wear, contamination and held-out silent-error datasets.

• Claim-to-experiment maps, filing strategies and contributor/inventorship analysis.

18.3 Inventorship/contribution record

Maintain dated records of who conceived each later mechanical/electrical interaction, who designed each experiment, who created CAD/firmware, and when the mechanism was first built and tested. AI/model assistance is not inventorship and must not replace human conception records.

18.4 Disclosure rule

Do not rely on an assumed grace periodBefore publishing code, CAD, datasets, posters, videos, papers, competition entries or VPD-C7 details, obtain institutional IPR review. A patent filing or defensive publication does not create freedom to operate.

19. Decision gates and escalation rules

Gate

When

Pass

Fail response

OB-G0 Teacher concept decision

Before procurement

OpenBraille retained with scope/budget approved

Proceed with VibeGuard or revise the project request

OB-G1 Facility/procurement

Week 1

Printer/tools and first components available

Do not commit full-cell schedule; use VibeGuard fallback if needed

OB-G2 One-dot mechanics

Weeks 3-4

Active raise/retract and repeatability pass

Redesign coupon; stop six-dot expansion

OB-G3 Six-servo power

Weeks 6-8

No unsafe droop, reset, heating or stall in planned sequence

Upgrade supply/distribution or reduce groups

OB-G4 Six-dot MDS

Week 8

Correct pattern transitions and safe operation

Report partial prototype or switch according to teacher direction

OB-G5 Locked validation

Week 10

Approved repeatability/lifecycle/tactile gates pass

No patent or performance overclaim; document failure

OB-G6 VPD-C7 research entry

Post-semester

Separate design, confidentiality and search approval

Keep OpenBraille as semester/publication record only

OB-G7 Counsel-led filing evaluation

Months 11-12

Unexpected physical effect, enabling evidence and useful scope survive review

Do not file; choose publication/know-how/stop

20. Open questions and teacher decisions

ID

Question / decision

Owner

Required by

Q1

Should OpenBraille remain the semester project or should the requested VibeGuard switch be approved?

Project coordinator

Before procurement

Q2

Is the working build window approximately eight weeks or the full twelve-week plan?

Teacher/project coordinator

Week 1

Q3

Is institutional FDM access dependable, and what material/print limits apply?

Amith + lab

Week 1

Q4

Which exact ESP32 and SG90 seller/batch are approved?

Nihad/Sreehari/Amith

Before order

Q5

What quantitative tactile-identification protocol and participant access are approved?

Teacher + Archa/Nihad

Before tactile test

Q6

What is the approved raised/lowered position band for the macro cell?

Technical team + teacher

Before locked validation

Q7

Is the 5 V / 3 A target supply adequate under the actual six-servo sequence?

Amith + Nihad

Before full integration

Q8

What content may be disclosed publicly before institutional IPR review?

IPR cell / project owner

Before publication or competition

Q9

Should VPD-C7 remain only a confidential future option after the semester?

Team + institution

After MVP evidence

21. Teacher approval and conditions

Decision item

Teacher response

Semester project

Retain OpenBraille / Approve VibeGuard switch / Revise and resubmit

Frozen OpenBraille scope

Approved / Approved with conditions / Not approved

Expected budget near ₹3,000

Approved / Revise

External 5 V servo supply and safety controls

Approved / Lab review required

One-dot-first procurement gate

Approved / Revise

Tactile participant protocol

Approved / Separate ethics/access review required

Future VPD-C7 treatment

Confidential post-semester only / Not approved / Further review

Teacher conditions

Signature and date

22. Source basis

This dossier was prepared from the controlled Project mC master package. The main evidence layers are:

Evidence layer

Controlled source

Project authority

Engineering Design Review; Project mC Decision Register v1.2; approved Phase 3C Portfolio Closure Memo

Common evidence

Concept Evidence Matrix; Uncertainty and Test Register

OpenBraille technical authority

Final OpenBraille Architecture Report; Memory; SOP

Comparative decision context

Two final cross-concept adjudications - treated as context, not votes

Future research boundary

OpenBraille Pre-Build Future Patent-Case Simulation

Costing and teacher context

Project mC Teacher Documents - Master Evidence, Costing and Decision Basis

Previous presentation

Final OpenBraille zeroth-review presentation dated 30-07-2026

22.1 Current official specification and price references

• Espressif, ESP32-WROOM-32 data sheet: https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf

• Espressif, ESP32-S3 product page and DevKitC-1 guide: https://www.espressif.com/en/products/socs/esp32-s3

• TowerPro, SG90 analog servo specifications: https://towerpro.com.tw/product/sg90-analog/

• Indian price snapshots and procurement cautions are recorded in the Master Evidence, Costing and Decision Basis and must be refreshed on purchase day.

Prepared for academic project planning. The future research section is a management and experimental roadmap, not legal advice, patentability clearance, freedom-to-operate clearance, a filing recommendation or a promise of patent grant.
