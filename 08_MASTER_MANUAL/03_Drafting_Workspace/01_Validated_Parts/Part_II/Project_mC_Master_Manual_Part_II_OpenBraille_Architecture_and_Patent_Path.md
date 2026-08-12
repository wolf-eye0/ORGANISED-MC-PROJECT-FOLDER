# Project mC Master Manual

## Part II — OpenBraille Architecture and Patent Research Path

## Document control

| Field | Value |
|---|---|
| Document | Project mC Master Manual — Part II |
| Controlled filename | `Project_mC_Master_Manual_Part_II_OpenBraille_Architecture_and_Patent_Path.md` |
| Status | Controlled draft |
| Scope | Chapter 04 — OpenBraille Frozen Architecture and Semester Scope; Chapter 05 — OpenBraille Patent Evidence and Future Research Path; Part II open-decision, contradiction and source-ledger sections |
| Source boundary | Only the nine attachments in the controlled Part II drafting package |
| Input inventory | Exactly nine physical attachments were present and readable. The eight hash-controlled files matched the manifest byte counts and SHA-256 values. The self-referential manifest was used only for file control. Upload transport suffixes did not create additional logical sources. |
| Current implementation status | This document is not an implementation, procurement or Phase 4 authorization |
| Approval status | This document is not a teacher-approval record and does not establish the authorized semester concept or platform |
| Patent status | No patentability, filing, infringement or freedom-to-operate conclusion |
| External verification | No fresh web, market, manufacturer, standards, legal-status or patent research was performed in this drafting stage |
| Relationship to Part I | Part I remains controlling for the current comparative decision: VibeGuard is the strongest semester-build recommendation; OpenBraille remains retained and legitimate; the proposed shift is not proved teacher-approved; Phase 4 and procurement are not proved started; no frozen MVP is established as patentable; and the two adjudications disagree on the preferred later patent-development route |

The Part II drafting package was complete. The governing instruction, authority and contradiction protocol, Master Manual blueprint, validated Part I, validated OpenBraille reconciliation, Chapter 04 and Chapter 05 source packets, required output template and manifest were readable. No prior-chat context, memory, web research or unstated technical assumption was used. The reconciliation controls resolved wording and contradictions; the source packets provide the underlying evidence; validated Part I controls the current project state.

## How to read Part II

Part II preserves four boundaries.

**Frozen architecture versus refinements.** OpenBraille means one non-standard macro six-dot cell with six SG90-class servos, six cam/follower channels, six guided pins, ESP32 direct PWM, FDM structure, external servo power, USB command/logging, active retraction and single-dot-first validation. Calibration, tolerance, guarding, sequencing, logging and power-distribution changes may refine this architecture; replacing it requires formal change control.

**Semester MVP versus future research.** The semester MVP is an educational embedded/mechatronics prototype. D11 and VPD-C7 are separate post-MVP hypotheses and must not be backfilled into the semester result.

**Targets versus results.** Dimensions, supply ratings, costs, repeatability thresholds, lifecycle screens and tactile criteria are planning values until configuration-controlled tests establish results.

**Patent evidence versus filing.** Research identifies prior art, uncertainties and experiments. It does not prove novelty, authorize filing or provide FTO. The current decision is no filing commitment.

# Chapter 04 — OpenBraille Frozen Architecture and Semester Scope

## 04.1 Chapter purpose

This chapter defines the controlled OpenBraille semester architecture, the boundary of permissible engineering work and the evidence required before implementation claims may be made. It is an implementation reference, not permission to purchase parts or enter Phase 4.

OpenBraille asks a bounded question: can a five-member student team use commodity actuation, embedded control and accessible FDM fabrication to produce one repeatable refreshable macro six-dot cell and document its limits? The project does not claim to solve the commercial refreshable-Braille problem. A successful result would demonstrate controlled electromechanical integration at educational geometry; a partial or negative result remains valuable when recorded honestly.

## 04.2 Current architecture identity

> **OPENBRAILLE ARCHITECTURE LOCK**
>
> For the frozen semester architecture, **OpenBraille means only**:
>
> - one permanent, non-standard macro-scale six-dot tactile cell;
> - six SG90-class micro servos, one actuator per dot;
> - six eccentric cam/follower channels;
> - six guided vertical tactile pins with safe rounded tips;
> - one ESP32-WROOM-32-class controller using six direct PWM signal channels;
> - FDM-manufactured frame, guides, cams/followers and related structure;
> - an external regulated servo-power branch with measured current headroom;
> - a shared electrical reference ground between the ESP32 signal domain and servo-power domain;
> - USB/serial command input and evidence logging;
> - active servo-driven raise and retract positions; and
> - mandatory single-dot-first commissioning before six-dot integration.
>
> This is an educational tactile/mechanical proof-of-concept. It is **not** an ISO-compliant cell, commercial refreshable Braille display, fluent-reading device, validated assistive product, patent-ready mechanism or approved semester implementation.

The architecture lock exists because earlier OpenBraille work contained several alternative mechanisms and because later patent work introduced separate experimental hypotheses. Those records remain useful as history or research context, but they do not change the frozen semester identity.

The most important correction concerns return motion. Earlier Phase 3C wording assumed that an internal servo spring or passive mechanical effect would reliably reset the pin. The controlling rule is now active retraction. Firmware and cam geometry must deliberately command and produce both raise and lower motion. A passive contribution may be observed and documented, but it may control the architecture only after the procured, fully coupled servo/cam/follower/pin channel proves repeatable return under the intended load. Until then, passive return is an unproved possibility, not a design fact.

Macro scale is equally important. The enlarged cell is not a temporary presentation mock-up within the semester architecture; it is the selected fabrication strategy for that architecture. Post-semester research may explore smaller practical geometry, but such work is a separate configuration and cannot be reported as the frozen semester cell.

## 04.3 Bounded semester objective

The semester objective is to build and evaluate one macro six-dot cell that accepts a supported character or six-bit pattern through USB/serial, independently commands six channels, actively raises and retracts the intended pins, and records enough physical and digital evidence to distinguish commanded behavior from actual behavior.

The interface may remain small and versioned: raw six-bit pattern, clear/all-down, one-dot diagnostic, calibration/test commands and a frozen character subset. A complete language interface, screen reader, multi-cell line or fluent-reading benchmark is outside scope.

Evidence must cover mechanics, electrical power, firmware mapping, repeatability and—only through an approved protocol—tactile distinguishability. Macro scaling reduces fabrication risk but cannot establish practical Braille pitch, product thickness, speed, noise, durability, array density or user readiness.

## 04.4 System architecture overview

| Subsystem | Frozen role | Principal interfaces | Evidence boundary |
|---|---|---|---|
| Host computer | Sends characters, six-bit patterns and controlled test commands; receives logs | USB data connection to ESP32 | Host acknowledgement proves data exchange only, not physical pin state |
| ESP32 controller | Parses commands, applies mapping, generates six PWM signals, sequences transitions and logs state | USB serial; six servo signal lines; shared reference ground | GPIO map and board behavior require validation on the exact purchased board |
| Servo channels | Six SG90-class servos provide rotary actuation, one per dot | Direct PWM signal; external regulated servo rail; mechanical coupling | Commanded angle does not prove output torque, cam position or pin endpoint |
| Cam/follower conversion | Six eccentric cams/followers convert servo rotation into vertical motion | Servo horn/coupling; follower; guided pin | Geometry and friction require coupon measurement; no passive reset assumption |
| Guided pin assembly | Produces the raised or lowered tactile state | Follower, guide, rounded tip and frame datum | Raised/lowered bands require external displacement evidence |
| FDM structure | Maintains pitch, alignment, guides, actuator mounting, guarding and cable management | All mechanical channels and fasteners | Printed dimensions and finishing must be measured and versioned |
| Servo-power branch | Supplies actuator energy independently of laptop USB | External regulated 5 V-class supply, distribution, conductors and bulk capacitance | A 2 A or 3 A label is not proof of adequacy; measured headroom controls |
| Development ground truth | Measures physical travel, force where available, current/voltage and visible failure | Calipers, camera/fixed jig, multimeter and approved test fixtures | External measurement supports development; it is not a permanent semester endpoint sensor |
| Evidence and configuration system | Associates commands and measurements with firmware, CAD, calibration and BOM revisions | USB logs, photographs, test sheets and repository records | Unversioned results cannot support final acceptance statements |

The subsystem boundaries deliberately prevent one type of evidence from substituting for another. For example, servo current may reveal effort, a stall-like condition or supply disturbance, but it does not by itself show that a tactile pin reached the correct height. A camera may show motion but cannot automatically establish user distinguishability. A successful character mapping test proves software logic, not mechanical correctness. The final demonstration must bring these evidence streams together without confusing them.

## 04.5 Functional and control flow

The controlled functional sequence is as follows:

1. The host transmits a supported character, explicit six-dot pattern or controlled service command over USB serial.
2. The ESP32 validates syntax, command length and permitted range. Invalid commands are rejected and logged without moving the mechanism.
3. A versioned mapping table converts a supported character into a six-bit target pattern. Raw dot-pattern commands bypass the character mapping but remain range checked.
4. The controller compares the target pattern with its last commanded pattern and identifies only the channels that require a state change.
5. The transition engine applies the frozen sequencing policy. It may actuate changed channels sequentially or in a bounded group if that policy has passed power and timing tests.
6. For every selected channel, the PWM manager issues the versioned raise or retract command value derived from external calibration.
7. The servo rotates its eccentric cam. The cam/follower interface converts rotary movement into constrained vertical pin travel.
8. A raise command drives the pin toward its measured upper band. A lower command actively drives the pin toward its measured retracted band.
9. Firmware records the command, target pattern, channel sequence, timing, configuration ID, reset events and declared faults.
10. Development measurements determine whether the physical state matched the command. Where direct physical evidence is absent, the correct runtime statement is `COMMAND_FINISHED`, `INCOMPLETE`, `FAULT` or `UNKNOWN`, not `UPPER_CONFIRMED` or `LOWER_CONFIRMED`.

The distinction between commanded and measured state is a core design rule. The controller may maintain a **command-state model** for sequencing, but that model is not a physical-state oracle. Servo pulse width, elapsed time, visible rotation and a current transient can all occur while a pin binds, a follower disengages, a horn slips or the mechanism stops short. Acceptance therefore depends on an independently measured physical band during calibration and locked validation.

The ordinary semester design does not include a permanent six-pin endpoint-sensing system. External calipers, a fixed camera/displacement fixture or other approved measurement method may provide ground truth during development. Those fixtures remain test equipment unless a later authorized architecture change states otherwise. Permanent D11 or VPD-C7 hardware must not be added late to the semester cell.

## 04.6 Mechanical architecture

The cell contains six independently testable channels. Each channel uses an SG90-class servo, horn/coupling, eccentric cam, follower, guided vertical pin and local support geometry. A shared FDM frame maintains the macro six-dot arrangement, provides alignment and mounting, and carries guarding and cable-management features.

Historical architecture work used approximately three times a cited sign-Braille geometry, with roughly 7 mm pitch and 1.5 mm raised travel as starting targets. These values are provisional CAD/test references, not standards claims or achieved measurements. Final dimensions must come from printed tolerance coupons, procured-part measurements and controlled travel tests.

A raised state is a measured protrusion band accepted by the approved macro tactile protocol. A lowered state is a measured retracted band that avoids an unintended dot. Neither may be inferred from PWM, servo angle, elapsed time or visible cam motion alone.

**Active retraction controls.** The lower command and cam geometry must return the pin to the measured lower band. Gravity, elastic effects or servo construction may assist only after the complete coupled mechanism proves reliable loaded return.

**Single-dot-first construction is mandatory.** Before a six-dot frame is committed, one coupon must reveal guide binding, pin tilt, follower loss, cam-profile error, coupling slip, unsafe stall, raised/lowered overlap, return failure, pinch hazards and repeatability. Six-dot fabrication follows only after measured motion, safe operation and a versioned calibration are established.

Allowed mechanical development includes tolerance coupons, controlled finishing, print-orientation/material changes within the FDM route, cam-profile iteration, rounded tips, guards and replaceable channel fixtures. A new actuation principle requires formal change control. Smaller practical-scale work is separate post-semester research.

## 04.7 Electronics and power architecture

The baseline controller is an ESP32-WROOM-32-class development board. It supplies six independent PWM control signals directly to the integrated electronics of the six SG90-class servos. The architecture does not require an H-bridge, Darlington array or external motor driver for these servo signal inputs. A different board or actuator may be considered only through explicit change control and complete revalidation.

The exact GPIO allocation remains provisional until checked against the exact purchased board and its manufacturer documentation. The final mapping must avoid input-only pins, boot-strapping conflicts and clashes with any required serial or peripheral function. The configuration record should identify board variant, GPIO map, firmware build and wiring revision.

USB serves two controlled roles:

- host-to-controller command input; and
- controller-to-host logs and evidence metadata.

USB is not the servo-power source. Servo current must not pass through the laptop cable or the ESP32 3.3 V regulator. The six servos require an external regulated 5 V-class supply connected through suitable distribution, conductor sizing and protection. The ESP32 signal ground and servo-power ground must share the intended reference point so that PWM levels are meaningful, while the high-current branch remains physically separate from the USB and logic-power path. The wiring must be inspected for accidental back-feed before a laptop is connected.

Historical records mention both 5 V/2 A and 5 V/3 A planning values. Neither is accepted solely because it appears on an adapter label. The controlling requirement is an external regulated supply with measured headroom under the frozen worst planned transition. Acceptance should consider:

- minimum rail voltage during transitions;
- aggregate and channel current;
- ESP32 reset or serial-disconnect events;
- servo chatter and incomplete motion;
- connector, conductor and regulator heating;
- supply protection behavior;
- repeated transition stability; and
- behavior during a jam or bounded fault test.

Bulk capacitance near the servo distribution is an allowed transient-control refinement. It cannot compensate for an undersized or unsafe supply. Similarly, sequential actuation may reduce peak demand and make faults easier to attribute, but it must still meet the approved refresh-time requirement and cannot be presented as proof of a novel power architecture.

## 04.8 Firmware architecture and operating sequence

The firmware should be deterministic and inspectable. Its required modules are:

| Module | Required function | Controlled output |
|---|---|---|
| Configuration manager | Board/GPIO, channel, build, CAD, calibration and sequencing identity | Configuration ID at boot and in logs |
| USB/serial parser | Validates character, raw-pattern, clear, test and calibration commands | Accepted command or explicit rejection |
| Mapping table | Converts the frozen character set to six-dot patterns | Unit-tested pattern and table version |
| PWM/channel manager | Applies bounded per-dot raise/retract values | Commanded state and timing record |
| Calibration manager | Stores externally measured operating windows | Versioned values; no runtime physical-state claim |
| Transition engine | Changes required dots using the locked sequence | Ordered transition record |
| Fault/log manager | Records invalid input, reset, timeout, isolation and bounded retry | Machine-readable event log |
| Test mode | Runs one-dot, repeatability and lifecycle procedures | Test ID, cycle count and stop reason |

Normal operation is: verify wiring; boot and emit identifiers; initialize a safe commanded state; validate the host command; calculate the target pattern; actuate changed channels using the frozen sequence; log completion and faults; and use external measurement for physical confirmation during tests. Absent or conflicting evidence remains `UNKNOWN`.

A boot sweep or timeout may prove that software issued commands; it cannot verify pin travel, height, retraction or tactile correctness. Mapping tests must cover the complete frozen set before physical validation. Automatic retries must remain within a physically qualified bounded policy.

## 04.9 Build materials and manufacturing control

FDM printing is the frozen manufacturing route. ABS-class frame material, PETG/Nylon-class cam/follower material and stainless-steel pins are candidate recommendations, not validated specifications. Final choices must follow actual print behavior, friction, wear and availability.

Configuration control must retain CAD/print-file versions, printer and material identity, print settings, measured dimensions, post-processing, assembly operator, photographs, replacement history and failed coupons. A tolerance matrix should establish guide fits and cam/follower clearances before full fabrication.

Dependable FDM access is an entry gate because cost and schedule assume institutional printing. Changing manufacturing route requires authorization. Rounded tips, guarded pinch points, restrained wiring and immediate power isolation are required safety controls; sharp pins, ejected parts, overheating or uncontrolled force are stop conditions.

## 04.10 BOM and budget evidence

The attached record contains several historical planning layers. They show that the frozen architecture may fit the project ceiling under stated assumptions, but none is a current supplier quotation.

| Evidence layer | Included basis | Historical amount | Correct treatment in Part II |
|---|---|---:|---|
| Phase 3C architecture estimate | ESP32, six SG90-class servos, 5 V/2 A planning supply, capacitor, FDM structure, pins, wiring and assembly materials | ₹2,060–₹2,850 | Order-of-magnitude architecture estimate only |
| Patent-synthesis MVP plus optional experiment envelope | Frozen MVP plus datum/guide variants, current-sense parts, substitute test servos, ground-truth fixture and contingency | ₹2,910–₹4,700 | Conditional research planning; must not consume the semester MVP budget without authorization |
| Reference-dossier expected semester plan | Detailed required purchased/fabricated items with institutional printing | approximately ₹2,984 | Preferred internal planning figure in the attached record; not a current quotation |
| Reference-dossier conservative envelope | Higher component/material allowances, delivery/replacement margin and controlled reprints | approximately ₹4,909 | Conservative planning envelope below the ₹5,000 maximum only under stated printing assumptions |
| Controlling project constraint | Preferred budget and absolute hardware ceiling | ≤₹3,000 preferred; ≤₹5,000 maximum | Actual procurement must be controlled by current verification, authorization and invoices |

### Reconciled planning BOM

The frozen architecture requires, at planning level:

- one ESP32-WROOM-32-class development board;
- six SG90-class micro servos, with any spare purchase separately justified;
- one external regulated 5 V-class supply with measured current headroom;
- bulk capacitor or capacitors appropriate to measured transient behavior;
- FDM-printed frame, guides, cams/followers and guards;
- six rounded tactile pins plus controlled spares;
- fasteners, servo horns/couplings and mounting hardware;
- perfboard or equivalent distribution, wiring, headers and connectors;
- one reliable USB data cable; and
- labels or other means to preserve channel and configuration identity.

Required capabilities such as digital calipers, multimeter, laptop, printer, fixed camera/displacement jig, hand tools and approved tactile-test resources may be institutional or reusable. They should not be hidden from the feasibility assessment simply because they are not purchased as project hardware.

Final procurement requires a later external-verification stage covering exact manufacturer specifications, current Indian prices, availability, supplier authenticity, delivery time and institutional printing cost. Purchased, borrowed, donated and institutional items must be recorded separately. The final cost statement should use actual invoices and document exclusions rather than repeating a historical estimate as a current total.

## 04.11 Minimum demonstrable success

The controlled minimum demonstrable success is:

> One non-standard macro six-dot cell, built within the approved budget and schedule, accepts a controlled character or dot pattern through USB/serial; independently commands all six servo/cam/pin channels; actively raises and retracts the intended dots; reproduces the frozen supported patterns without unsafe power behavior; and provides measured mechanical, electrical, firmware and tactile evidence under a preregistered protocol while reporting all limitations and failures.

The attached architecture work proposes the following acceptance targets. Their status must remain explicit.

| Proposed target | Purpose | Present status |
|---|---|---|
| All six channels independently raise and actively retract | Basic six-dot function | Proposed; no physical result attached |
| No brownout, unsafe rail collapse, connector heating or servo stall in the frozen sequence | Electrical and power acceptance | Proposed; supply adequacy unmeasured |
| 100% correct mapping for the frozen supported pattern set | Firmware correctness | Proposed; supported set not finally frozen |
| Position variation at or below 0.1 mm over a 100-cycle measured set | Early repeatability screen | Proposed; method and threshold require preregistration/approval |
| At least 1,000 actuations | Early wear/lifecycle screen | Proposed; cycle definition and failure rules not executed |
| Teacher/institution-approved blinded tactile threshold and trial count | Bounded tactile distinguishability | Unresolved; participant, consent and stop rules not attached |

These targets are not achieved results and are not automatically the final acceptance criteria. They should be preregistered before locked validation, including measurement method, exclusion rules, uncertainty, stop conditions and how negative data will be reported.

A visually correct pattern is not sufficient for tactile success. If an approved tactile route is unavailable, the team may report mechanical travel and visual pattern formation but must state that tactile validation was not conducted. Team-member visual judgement or informal touching cannot be represented as user validation.

## 04.12 Validation and entry-gate sequence

| Gate | Question | Required evidence | Pass consequence | Fail consequence |
|---|---|---|---|---|
| OB-G0 | Is OpenBraille and its platform authorized? | Explicit teacher/project decision | Permit procurement planning | Do not assume approval |
| OB-V0 | Are the exact board, first servo, supply, FDM access and tools usable? | Board/USB check, controlled sweep, supply and facility confirmation | Freeze coupon inputs | Resolve before CAD commitment |
| OB-V1 | Can one channel raise and actively retract freely and safely? | Versioned coupon, measured travel, repeated cycles and inspection | Authorize remaining channels | Redesign; stop six-dot expansion |
| OB-V2 | Do measured command windows create repeatable upper/lower bands? | External displacement evidence | Store versioned values | Change geometry/actuator; do not tune blindly |
| OB-V3 | Do six channels coexist without interference or power failure? | Pattern tests, rail/reset log and inspection | Freeze integrated configuration | Improve distribution/sequence or rebuild |
| OB-V4 | Does firmware produce the intended states? | Unit tests and physical checks | Permit locked pattern evaluation | Correct mapping/configuration |
| OB-V5 | Does travel remain acceptable through cycle screening? | 100-cycle dataset, ≥1,000-actuation record and wear log | Permit final validation | Redesign, narrow or report failure |
| OB-V6 | Are states/patterns distinguishable under an approved tactile protocol? | Preregistered blinded method and raw results | Support bounded macro tactile conclusion | Adjust or report tactile MDS not achieved |
| OB-V7 | Can the frozen build reproduce verified behavior safely? | Frozen CAD, firmware, calibration, BOM and signed checklist | Demonstrate verified capabilities | Use approved fallback evidence and disclose failure |

Single-dot-first validation prevents six copies of the same defect and keeps mechanical, power and firmware failures separable. The final demonstration must use the same controlled configuration that produced the acceptance evidence; late changes require revalidation.

## 04.13 Mechanical, electrical and tactile risks

| Risk | Current evidence state | Required control |
|---|---|---|
| Printed guide/cam tolerance | Macro scaling helps; no coupon result attached | Tolerance matrix, measurement, finishing record and one-dot gate |
| Pin tilt/follower loss | Identified, untested | Stop and redesign before expansion |
| Active retraction | Passive return unproved | Loaded raise/retract measurement; retain active command |
| Servo torque/stall | Plausible actuator, untested geometry | One-dot travel/current/force tests; no automatic upgrade |
| Cam/follower wear | Materials proposed only | ≥1,000-actuation screen and inspection log |
| Six-servo power demand | 2 A/3 A are planning values | External supply, measured droop/current, resets and heat |
| USB/grounding error | Wiring boundary unverified | Shared reference, separated current path and back-feed inspection |
| Command-state confusion | Conceptually resolved, implementation risk remains | External evidence and `UNKNOWN` state |
| Tactile distinguishability | No approved validation | Blinded approved protocol and limitations |
| Repeatability drift | Proposed threshold only | Preregister method and report distribution |
| Pin/pinch safety | Foreseeable hazards | Rounded tips, guards, isolation and supervision |
| Facility/schedule dependency | FDM access assumed | Confirm printer, material and queue |
| Scope overclaim | Strong visible demo can mislead | Use controlled current-state language |

A failed gate must trigger documented iteration within scope, formal change control, a narrowed result or route closure—not a hidden architecture substitution.

## 04.14 Allowed refinements

The following work may be performed without changing the frozen architecture, provided every change is versioned, remains inside the approved budget/schedule and is revalidated where necessary:

- per-dot PWM calibration derived from external displacement evidence;
- measured active raise and retract command windows;
- FDM tolerance coupons and controlled guide-clearance changes;
- cam-profile iteration within the eccentric cam/follower principle;
- documented post-processing and print-orientation changes;
- suitable FDM material substitutions that retain the same architecture;
- rounded pin-tip refinement and pinch-point guards;
- fixed sequential or bounded-group actuation of changed dots;
- improved external power distribution, conductor sizing and bulk capacitance based on measurement;
- deterministic USB commands, mapping tests, configuration IDs and fault logs;
- external camera, caliper, displacement or force fixtures used as development ground truth;
- one-dot and replaceable channel test fixtures within the same servo/cam/pin structure; and
- mounting, cable-management and serviceability changes that do not create a new actuator or cell architecture.

These are ordinary engineering refinements unless later physical evidence shows a distinct non-additive effect and Chapter 05’s patent-development gates are satisfied. Their presence does not make the semester MVP patentable.

## 04.15 Prohibited substitutions

The following must not be introduced or described as the frozen OpenBraille semester design:

- moving-roller or rotating encoder-wheel actuation;
- continuous-paper Braille printing or embossing;
- RAMPS/Mega motion-control architecture;
- electromagnetic latching, non-latching solenoid, SMA, pneumatic or other replacement actuation;
- a commercial-scale standard Braille cell or multi-cell reading line;
- PCA9685 or multi-cell expansion represented as part of the current one-cell scope;
- STM32, ESP32-S3, MG996R or another board/actuator substituted without explicit project and teacher change control;
- passive spring or gravity return stated as proven without coupled-mechanism evidence;
- permanent D11 or VPD-C7 sensing/datum hardware added to the semester cell;
- a hybrid with VibeGuard or TrueMoist; or
- any architecture change disguised as a refinement to preserve schedule or patent narrative.

Alternatives may be revisited only in a later authorized change record. They must remain labelled as new or superseded designs rather than being backfilled into the Phase 3C identity.

## 04.16 Current implementation and approval status

> **OPENBRAILLE CURRENT-STATE BOX**
>
> **Established by the attached record**
>
> - The six-servo macro-cell architecture is frozen and sufficiently reconciled for controlled manual drafting.
> - OpenBraille remains a retained, legitimate accessibility/mechatronics concept.
> - Historical planning evidence indicates possible fit within the ₹5,000 hardware ceiling under institutional-printing assumptions.
> - Single-dot-first validation, active retraction, external servo power and command-versus-physical-state separation are controlling requirements.
>
> **Not established by the attached record**
>
> - Teacher approval of OpenBraille as the semester implementation.
> - Teacher/course acceptance of the ESP32 platform.
> - Phase 4 entry, procurement freeze or named role ownership.
> - A built one-dot coupon or integrated six-dot cell.
> - Mechanical, electrical, lifecycle, tactile or user validation.
> - Current manufacturer specifications, Indian prices, availability or supplier authenticity.
> - Standards compliance, commercial readiness or patent readiness.
>
> Validated Part I records VibeGuard as the strongest semester-build recommendation and the OpenBraille-to-VibeGuard change as a request rather than a proved approval. This chapter therefore preserves OpenBraille as a complete retained/fallback implementation path without claiming current authorization.

Before implementation, the project requires an explicit decision on concept and platform, confirmation of FDM and measurement access, current specification and price verification, a controlled budget, named subsystem ownership and approval of safety and tactile-testing procedures. Drafting readiness is not implementation readiness.

## 04.17 Chapter conclusion

OpenBraille is one non-standard macro six-dot cell using six SG90-class servos, six cam/follower channels, six guided pins, ESP32 direct PWM, FDM structure, external servo power, USB command/logging, active retraction and single-dot-first validation. It can support a disciplined student engineering programme only if command state is kept separate from physical truth and the one-dot, power, repeatability, safety and tactile gates are enforced.

A successful result is a bounded educational proof-of-concept, not a commercial Braille product or patent conclusion. This chapter does not authorize procurement, establish semester selection or prove standards compliance.

## 04.S Source notes

The material conclusions in Chapter 04 rely on the following original organized-workspace paths. The attached packet and manifest are not cited as original technical sources.

### TIER_1 — Current architecture and project authority

- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Architecture_Report_Final.md` — frozen servo/cam/pin identity, macro-scale architecture, initial BOM, firmware organization and milestone sequence; corrected where higher authority requires active retraction and measured-state wording.
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Memory_Final.md` — concise frozen architecture record; passive-return language is not controlling.
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_SOP_Final.md` — architecture-selection and implementation-reference procedure.
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md` — current owner decisions, active-retraction control, portfolio and phase status.
- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md` — budget, course, platform, team and proposed-change context; not proof of approval.

### TIER_2 — Supporting status and evidence

- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx` — corrected command/state semantics, power-domain boundary, implementation gates, detailed planning BOM and configuration-control guidance.
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` — duplicate publication format of the same dossier; not independent corroboration.
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md` — unresolved mechanical, power, quantitative and tactile evidence.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` — semester-build and later-research context only.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` — semester-build and later-research context only.
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — treatment of adjudications as context rather than votes.
- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md` — controlled research-set status and exclusion of the failed concept-swapped synthesis.
- `03_CONCEPT_PORTFOLIO/OpenBraille/README.md` — concept-folder status and navigation only where consistent with higher authority.

# Chapter 05 — OpenBraille Patent Evidence and Future Research Path

## 05.1 Chapter purpose and legal boundary

This chapter records the controlled patent-evidence position and a conservative future research path. It is not legal advice, claim construction, a patentability opinion, an infringement conclusion or FTO clearance, and it does not update the historical research cut-offs.

Four layers remain separate: the frozen semester MVP; ordinary refinements; post-semester experiments concerning datum, calibration, observability, wear, replacement and scale; and speculative D11/VPD-C7 mechanisms. Progress between layers requires enabled hardware, direct evidence, strong baselines, transfer and current primary-source/IPR review. Semester engineering value does not imply patent value.

## 05.2 Ordinary MVP patent position

> **OPENBRAILLE PATENT CURRENT-STATUS BOX**
>
> - The frozen macro six-servo MVP is **not established as a credible patent target**.
> - The current decision is **no filing commitment**.
> - No novelty, inventive step, patent eligibility, useful claim scope, infringement clearance, freedom to operate or probable grant is established.
> - D11 and VPD-C7 are separate, unbuilt research hypotheses outside the semester architecture.
> - A later positive experiment may become eligible only for institutional or professional file/no-file evaluation after current primary-source prior-art, legal-status, FTO, confidentiality, ownership and inventorship review.

The ordinary MVP combines known or crowded functional elements: motor-driven or cam-driven Braille pin movement, independently actuated tactile dots, mechanical guides and stops, modular structures, commodity embedded control, PWM, calibration, fixed sequencing, printed fabrication and low-cost open-hardware construction. The reviewed evidence did not show a persuasive technical interaction that transforms this combination into a presently credible invention.

No reviewed independent claim was shown to contain every exact procurement and dimensional detail of the project. That absence is not a positive novelty result. A claim restricted to six SG90 servos, an ESP32 board, FDM parts and an enlarged cell would likely be narrow, predictable and easy to design around. Low cost and student accessibility are valuable project attributes, but they do not themselves establish inventive step.

Macro scale further limits the patent case. It reduces fabrication risk and supports a visible class demonstration, but it does not enable broad claims to standard-scale Braille geometry, compact cell thickness, practical array density, acceptable force, noise, speed, durability or fluent reading. Broad mechanical claims require practical-scale construction and disclosure.

The correct present treatment is therefore:

- preserve the MVP as an engineering prototype;
- collect honest mechanical, power, repeatability and tactile evidence;
- do not file on the baseline architecture as such;
- do not describe it as patented, patent pending, novel or inventive;
- do not infer FTO from a different actuator, low price or an expired/abandoned database label; and
- consider future patent development only around a specifically enabled physical mechanism that survives the gates in this chapter.

## 05.3 Research-lane integrity and limitations

Six lanes are evidence sources, not votes.

| Lane | Permitted use | Material limitation |
|---|---|---|
| ChatGPT Deep Research | Strong patent/publication leads, claim comparisons and experiment framing | Some status and current-signature conclusions need verification |
| Gemini | Search leads and experiment ideas | Several record/family/status descriptions unreliable; positive conclusions downgraded |
| Perplexity — partial | Completed material only | No complete verdict; missing conclusions cannot be reconstructed |
| Qwen | Limited independently supported prompts | Concept contamination and unreliable family/status reasoning in parts |
| Mistral | Conventionality warnings and possible tests | Shallow primary-claim support; status/FTO claims not controlling |
| Microsoft Copilot | High-level calibration/testing prompts | Weak traceability and false/unsupported relationships in material places |

The failed moving-roller/encoder-wheel/RAMPS/Mega synthesis is excluded. The dossier’s DOCX and PDF are one source in two formats. Controlled conclusions depend on audited evidence, not model agreement.

## 05.4 Valid synthesis conclusions and disagreement

The two valid OpenBraille patent syntheses agree on the main present position:

- the frozen MVP alone is not a credible filing target;
- mechanical stops, calibration, sequencing, modularity, printed guides and current monitoring are individually known or predictable;
- the official file and current legal effect of Indian application `5559/CHE/2014` remain unresolved;
- the generic actuator-current, position and anomaly field was not searched to complete professional claim-language depth;
- no OpenBraille experiment demonstrates a non-additive interaction; and
- institutional IPR review and a refreshed primary-source search are mandatory before any filing decision.

They disagree on the classification of D11 before physical evidence exists.

| Valid synthesis | Current classification | Treatment of D11 | Controlled interpretation |
|---|---|---|---|
| Work Max | Track D; no credible patent path established, moderate confidence | D11 is the least-weak experiment but remains Track D until physical-state, ablation, transfer, practical-scale and search gates pass | Controls the conservative current statement because it does not turn an unsearched exact combination into a positive case |
| Valid Secondary / Standard High | Conditional Track B, moderate-low confidence | Allows the integrated mechanism to advance as a bounded candidate if it demonstrates a material physical-control effect | Preserved as a legitimate research hypothesis, not as consensus, filing authority or proof |

The reconciled result is not an average. D11 may be worth a bounded post-MVP experiment, but the current status remains experimental and no-filing. The phrase **advance conditionally** means that engineering research may be authorized under strict controls; it does not mean patentability is established or that a filing should be prepared.

The disagreement is useful because it defines the evidence burden. A permissive interpretation asks whether integration might produce a technical effect. The conservative interpretation asks whether the mechanism can first show direct physical truth, non-additive benefit, transfer and useful scope. Part II adopts the conservative current state while preserving the experiment as an open research question.

## 05.5 Cross-concept adjudication context

Both final cross-concept adjudications support VibeGuard as the strongest semester-build candidate. They disagree on the best later patent-development path.

- The Work Max adjudication favors TrueMoist after a VibeGuard signal-and-access gate and deprioritizes OpenBraille unless later D11-type evidence passes.
- The Deep Research High adjudication identifies conditional OpenBraille D11 as the best post-MVP candidate and proposes a short physical-state-observability gate, with VibeGuard as fallback.

These adjudications use different strategic models. They are decision context, not votes. Neither proves teacher approval, patentability or a project-wide patent winner. No higher-authority record chooses one patent-first gate.

The later OpenBraille pre-build simulation is narrower. It stress-tests the OpenBraille patent case and treats the broad D11 bundle as an aggregation on current evidence. It then selects VPD-C7 as the best hypothesis for redesign and testing within that simulation. This does not override the unresolved cross-concept decision. It means only that, if OpenBraille future research is authorized, the simulation considers direct pin-side endpoint evidence a more coherent technical question than current-led state inference.

The manual must therefore preserve three distinct decisions:

1. which concept, if any, is authorized for the semester build;
2. which short patent-first evidence gate, if any, is authorized after or alongside the semester programme; and
3. whether a mechanism that passes an experiment should proceed to institutional file/no-file evaluation.

None is proved complete in the attached record.

## 05.6 D11 research hypothesis

### Proposed mechanism

D11 is an earlier proposed **mechanically referenced, individually calibrated, sensor-minimal tactile-state verification and bounded-recovery architecture** using the six servo/cam/pin channels. Its prospective relationship combines: upper/lower mechanical datums; per-channel reliable command windows; isolated shared current/voltage observation; independent displacement/force labels; `COMPLETED`, incomplete/jammed or `UNKNOWN` states; at most one qualified low-energy retry followed by isolation; supply-aware sequencing; and recalibration after replacement, remount or drift.

D11 asks whether these familiar controls create a reproducible non-additive physical advantage. A command or current spike may never be treated as proof of tactile state.

### Relationship to the MVP

D11 is outside the frozen semester cell. It retains the actuator channels but adds datum, instrumentation, labelled state logic and recovery experiments. Ordinary per-dot calibration remains routine engineering unless a specifically defined integrated relationship is tested in a separate configuration after the MVP gates.

### Required evidence, baselines and ablations

Required evidence includes direct displacement and preferably force ground truth; labelled normal, incomplete, jam and ambiguous events; held-out data; multiple units/rebuilds; voltage, temperature, load, friction, contamination and wear variation; retry safety; practical-scale evidence; current prior-art search; and institutional IPR review.

Baselines must include fixed PWM, calibrated open loop, datum-only, calibration-only, current-only, fixed sequencing and a direct-sensor oracle. Ablation must remove each claimed indispensable element. The proposed 3,000-transition, zero-silent-wrong-state gate is a research threshold, not an achieved or automatically approved requirement.

### Failure conditions and current status

D11 fails as a patent direction if current reveals only generic effort, a current-only rule silently accepts a wrong state, the full system equals the best partial baseline, thresholds require ad hoc retuning, replacement/reassembly or practical-scale transfer fails, retry is unsafe, closer art is found or useful scope collapses to exact hobby parts.

No D11 hardware, datum, waveform dataset, classifier, ablation, replacement trial, practical-scale coupon or held-out result is attached. No cooperative effect, novelty, inventive step, eligibility, useful scope or FTO is established.

## 05.7 VPD-C7 research hypothesis

### Proposed pin-side datum mechanism

VPD-C7 is a later, separate **Verified Pin-Datum Cell** hypothesis for a post-MVP guide/pin coupon. It asks whether the same pin-side datum that sets an endpoint can also provide direct, low-energy endpoint evidence with less registration error and fewer silent wrong states than a passive stop plus separately mounted sensor.

The proposed coupon uses registered upper/lower endpoint features; a low-energy pin-side event that does not carry servo power; external displacement/force as the oracle; current/voltage only for effort, overload or supply disturbance; endpoint declaration only from qualified pin-side evidence; `UNKNOWN` for absent/conflicting evidence; bounded recovery; and the existing servo/cam/pin actuation. The simulation’s twelve contacts plus one shared current channel are planning architecture, not a mandate or claim.

### Relationship to the MVP

VPD-C7 changes the guide/pin/datum relationship and adds endpoint evidence. It therefore requires separate configuration, budget, folder and disclosure status. Work should begin with one coupon; C7 results may not be represented as frozen-cell results.

### Required evidence and baselines

Required comparisons are passive datum only, calibrated open loop, passive datum plus separate direct sensor, contact without current, current without contact and full C7. Measurements must cover registration error, force, friction, bounce, contact resistance, debounce, false endpoints, energy, practical-scale packing, wear, debris/cleaning, blind replacement and independent reassembly. A locked held-out run must expose silent errors, and current must be removed if it adds no independent diagnostic value.

The decisive baseline is the passive stop plus separate sensor. A dual-purpose datum/contact must provide a measurable physical advantage without unacceptable friction, bounce, wear, contamination or manufacturing cost.

### Failure conditions and current status

C7 fails if it is equivalent or worse than a separate sensor, cannot fit practical geometry, fails lifecycle or transfer, accepts a silent wrong state, depends on current for endpoint certification, is defeated by closer art or has only trivial hobby-part scope.

No C7 datum/contact has been built. Stops and switches are familiar, creating strong obviousness risk. No registration, silent-error, scale, lifecycle, novelty, inventive-step, useful-scope or FTO result exists.

## 05.8 Relationship between D11 and VPD-C7

| Dimension | D11 | VPD-C7 |
|---|---|---|
| Origin | Two valid syntheses | Later pre-build stress test |
| State link | Datum, calibration and shared current/voltage; physical truth remains difficult | Datum itself is intended to provide pin-side endpoint evidence |
| Current role | Possible diagnostic input, never sufficient alone | Effort/overload/supply evidence only |
| Configuration | Post-MVP overlay/research build | Separate guide/pin/datum coupon |
| Main test | Cooperation, observability and transfer | Advantage over passive stop plus separate sensor |
| Current status | Track D or conditional early exploration | Redesign-before-testing hypothesis |

D11 is the earlier integrated verification hypothesis. VPD-C7 is a later, separate pin-datum redesign intended to address D11’s weak physical-state link. D11 configurations may be baselines for C7, but the mechanisms must not be merged or described as one invention. Either may fail and leave only conventional engineering value.

## 05.9 Pre-build simulation boundary

> **PRE-BUILD SIMULATION CAUTION**
>
> The OpenBraille pre-build future patent-case simulation is conditional planning evidence. It did not build hardware, observe a physical effect, conduct a legal opinion, establish novelty or predict patent grant.
>
> It supports only the following management boundaries:
>
> - build and assess the ordinary macro six-servo MVP first;
> - preserve active retraction unless passive return is proved;
> - develop VPD-C7 only on a separate post-MVP coupon;
> - use external physical ground truth;
> - never let current alone certify pin height or completion;
> - preserve `UNKNOWN` for absent or conflicting evidence;
> - compare against strong baselines and ablations;
> - stop when kill criteria are met;
> - protect future CAD, circuits, thresholds and data until IPR review; and
> - do not substitute another OpenBraille architecture.

The simulation’s scenario labels, rough incremental hardware allowance and twelve-month research sequence are planning tools. They are not probabilities of grant, spending approval or a direction to compress future work into the semester. The simulation may prioritize VPD-C7 for redesign/testing inside its own analysis, but this is not project or institutional authorization.

## 05.10 Experimental evidence roadmap

Future research proceeds only through evidence gates:

1. **MVP truth baseline:** versioned one-dot and six-dot travel, power/reset, 100-cycle repeatability, ≥1,000-actuation wear screen and honest tactile record. MVP failure leads to engineering learning, not forced patent work.
2. **Datum/calibration:** compare frozen geometry, datum-only, calibration-only and combined configurations across rebuilds.
3. **Current observability:** collect labelled events with direct displacement oracle across units, voltage, load, temperature, friction and wear; prohibit current-only completion.
4. **D11 cooperation:** compare the full configuration with the best partials using preregistered interaction and kill rules.
5. **VPD-C7 coupon:** measure registration, force, friction, bounce, contact behavior and silent error against a passive stop plus separate sensor.
6. **Practical-scale/lifecycle:** test smaller coupons, packing, wear, dust/fibre, cleaning and contact degradation.
7. **Replacement/reassembly:** use blind component swaps and independent rebuilds to expose hidden tuning.
8. **Locked silent-error gate:** freeze oracle, thresholds, `UNKNOWN` handling and stop rule; any silently accepted wrong tactile state requires genuine redesign.
9. **Search/IPR/FTO:** only after enablement, retrieve the official Indian file, refresh worldwide claims/NPL, document human contribution and conduct ownership, disclosure and FTO review.

| Programme | Strong baseline | Positive gate | Kill/hold outcome |
|---|---|---|---|
| MVP | Fixed PWM plus external measurement | Safe repeatable one/six-dot evidence | Preserve learning; no patent rescue |
| D11 datum/calibration | Datum-only and calibration-only | Transferable reduction in scatter/stall | Routine tuning → no patent lead |
| D11 current | Command/time/voltage and direct oracle | Held-out multi-unit diagnostic value | Ambiguous/silent error → remove current |
| D11 cooperation | Best partial configurations | Non-additive improvement and transfer | Equality with partial → aggregation |
| VPD-C7 | Passive stop plus separate sensor | Better registration/truth without burden | Equivalent/worse → end thesis |
| Practical scale | Macro and smaller coupons | Reproducible practical geometry | Macro-only → no broad claim |
| Lifecycle/transfer | Clean/new and original tuned build | Stable wear, contamination and rebuild results | False endpoint or transfer failure → redesign/kill |
| Search/IPR | Final enabled disclosure | Useful scope after official search/FTO/ownership review | Closer art or unacceptable risk → no filing |

Motion videos, model agreement, low BOM or generic classifier accuracy do not substitute for these gates.

## 05.11 Prior-art and legal-status limitations

The attached patent record remains materially incomplete in several areas.

1. The official specification, claims, prosecution history, descendants, ownership and current legal effect of Indian application `5559/CHE/2014` were not obtained.
2. Official current status was not established for every cited US, EP or national right. Historical database labels are leads, not legal conclusions.
3. The generic actuator-current, position, anomaly-detection and motor-control field was not exhaustively searched at professional claim-language depth.
4. Hidden, non-English, differently classified or later-published references may contain closer combinations.
5. A mechanism that has not been physically enabled cannot support a positive novelty or inventive-step case.
6. Macro-scale evidence cannot enable broad standard-scale mechanical claims.
7. Patentability and FTO are different. An old or expired disclosure can destroy novelty while posing no current claim risk; a live narrow claim can create FTO risk even when a broad concept is old.
8. Jurisdictional eligibility rules differ, especially for software-only calibration, scheduling or classification language.
9. Filing, publication or student construction does not create freedom to operate.
10. The project must not assume that experimental use in India is exempt from infringement without qualified advice.

The manual may identify cited publications as research leads and explain why the field appears crowded. It must not declare a right live, expired, abandoned, irrelevant or non-infringed without official current verification.

## 05.12 Freedom-to-operate boundary

Freedom to operate concerns whether the actual acts of making, using, supplying, selling or importing the final design in particular territories could fall within enforceable claims. It is distinct from whether the team might obtain a patent on an improvement.

No FTO clearance exists for the frozen MVP, D11 or VPD-C7. A meaningful review requires:

- the final geometry, materials, electronics and firmware behavior;
- intended suppliers and manufacturing route;
- intended countries and commercial acts;
- official current legal status and prosecution histories;
- claim charts addressing literal scope and relevant equivalents; and
- documented design-around decisions.

Differences such as using a servo rather than an electromagnetic actuator do not automatically avoid claims. An expired publication may still be prior art. A patent filing by the project would not neutralize third-party rights. Academic publication or defensive publication would not create FTO.

Until counsel-led review is complete, the correct statements are **FTO not assessed** and **no non-infringement conclusion**. The semester team may build only under the institution’s approved educational rules and should not make a commercialization claim from the current record.

## 05.13 Confidentiality, contribution and institutional IPR control

The public-safe semester baseline may include the macro six-dot architecture, six SG90-class servos, cams, guided pins, ESP32 direct PWM, external power, general historical budget, approved build results and honest limitations, subject to course and institutional rules.

The following should remain confidential until institutional IPR review if future research proceeds:

- exact D11 datum/guide geometry;
- calibration procedure and stored operating windows asserted as part of a future mechanism;
- current/voltage waveform definitions, features, thresholds and transfer results;
- retry, derating, isolation and fault-state logic proposed as indispensable;
- exact VPD-C7 contact/datum geometry, materials, dimensions, circuitry, protection and debounce;
- comparative results against passive stops, separate sensors and current-only inference;
- replacement/reassembly, wear, contamination and held-out silent-error data;
- claim-to-experiment maps and draft claim language; and
- contribution, inventorship and disclosure chronology.

Human conception and contribution records should begin before future-mechanism work. Records should identify who conceived each technical feature, who designed the experiment, who created CAD or firmware and who reduced the mechanism to practice. AI/model assistance is not inventorship and must not replace dated human contribution evidence.

Before publishing code, CAD, videos, posters, papers, competition entries or details of D11/VPD-C7, the team should obtain the institution’s IPR and disclosure decision. The project must not rely on an assumed grace period. If the patent route is killed, the institution may later choose academic publication, defensive publication or confidential know-how after appropriate review.

## 05.14 File/no-file decision gate

The present decision is **no filing commitment**. A later counsel-led file/no-file evaluation may be opened only when all of the following are satisfied.

| Gate | Required condition | Evidence needed |
|---|---|---|
| Engineering baseline | Frozen MVP succeeds without architecture substitution | Versioned one-dot and six-dot mechanical, power, firmware and tactile evidence |
| Enabled mechanism | One specifically defined D11 or VPD-C7 configuration is actually built | Complete dimensions, materials, circuitry, firmware/state chart and test setup |
| Physical effect | Mechanism produces a preregistered reproducible advantage | Direct displacement/force ground truth and comparison with strong baselines |
| Ablation | Every asserted indispensable feature contributes materially | Controlled removal studies and interaction analysis |
| Transfer | Effect survives component replacement, independent reassembly and ordinary variation | Blind swaps, rebuilds, environmental and practical-scale results |
| Truthfulness | No locked test silently accepts an incorrect tactile state | Held-out dataset with explicit `UNKNOWN`/isolation outcomes |
| Prior-art status | Official close-prior-art file and current worldwide search are resolved | Official register documents, professional claim-language search and NPL review |
| FTO | Actual design and intended territories are reviewed | Counsel-led claim chart and design-around analysis |
| Ownership/inventorship | Human contribution, ownership and disclosure records are complete | Dated contribution log and institutional determination |
| Institutional value decision | Expected useful scope justifies cost and disclosure risk | IPR cell/counsel recommendation and authorized budget decision |

Failure at the evidence gate should normally produce one of three outcomes: retain the work as a strong semester prototype, convert it into a rigorous engineering/publication study, or close/reduce patent priority. It must not produce a weak filing merely to preserve the original aspiration.

Even if every gate passes, the correct statement is **eligible for counsel-led file/no-file evaluation**. It is not **patentable**, **approved for filing** or **likely to be granted**.

## 05.15 Current patent-development state

The baseline MVP is closed as a present filing target and remains valuable engineering work. No D11 or VPD-C7 experiment is authorized or proved started; no direct ground-truth rig, baseline suite, dataset, contact coupon, practical-scale evidence, transfer trial or silent-error gate is attached. The official Indian file, current worldwide search, legal status, FTO, adjudication gate and institutional confidentiality/ownership rules remain unresolved.

The route must be allowed to fail. Non-informative current should be removed; a C7 datum equivalent to a separate sensor should be closed; macro-only or non-transferable results should not support broad claims; closer art or trivial scope should lead to no filing. The current decision remains no filing commitment.

## 05.16 Chapter conclusion

The macro six-servo MVP is not established as a credible patent target. D11 is an earlier integrated verification hypothesis; VPD-C7 is a later separate pin-datum redesign. Neither is implemented, proved cooperative, novel or part of the semester cell.

Future work requires direct ground truth, strong baselines, ablation, practical-scale and lifecycle evidence, replacement/reassembly and a locked silent-error gate. Only a final enabled mechanism that survives current prior-art, FTO, confidentiality, ownership and institutional review may become eligible for professional file/no-file evaluation. The current state is no filing commitment.

## 05.S Source notes

The material conclusions in Chapter 05 rely on the following original organized-workspace paths. Raw research lanes are supporting leads only; the packet and manifest are not original patent evidence.

### TIER_2 — Valid syntheses, simulation and controlled reference sources

- `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/01_OpenBraille_Patent_Synthesis_Work_Max.md` — conservative Track D conclusion, evidence audit, D11 definition, research gates and unresolved legal/search limits.
- `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/02_OpenBraille_Patent_Synthesis_Valid_Secondary.md` — conditional Track B interpretation and integrated-mechanism hypothesis; not proof or filing authority.
- `03_CONCEPT_PORTFOLIO/OpenBraille/04_PreBuild_Simulation/OpenBraille_PreBuild_Future_Patent_Case_Simulation.md` — later stress test, D11 aggregation attack, VPD-C7 redesign hypothesis, baseline/ablation roadmap and simulation boundaries.
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx` — controlled separation of semester/public work and confidential future research, non-claim mechanism descriptions and practical management rules.
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` — duplicate publication format; not independent corroboration.
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_OpenBraille_Concept_Dossier.docx` — historical concept origin only; not current architecture or patent authority.
- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md` — controlled lane/synthesis identity and exclusion record.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md` — cross-concept context, not vote or approval.
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md` — cross-concept context, not vote or approval.
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md` — treatment rule for adjudications.

### TIER_3 — Controlled raw research lanes

- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/01_OpenBraille_Patent_Research_ChatGPT_Deep_Research.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/02_OpenBraille_Patent_Research_Gemini.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/03_OpenBraille_Patent_Research_Perplexity_PARTIAL.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/04_OpenBraille_Patent_Research_Qwen.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/05_OpenBraille_Patent_Research_Mistral.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/06_OpenBraille_Patent_Research_Microsoft_Copilot.docx`

These lanes are evidence sources rather than votes. The Perplexity lane is partial. The separate moving-roller/encoder-wheel/RAMPS/Mega synthesis is invalid and excluded.

# Part II Open-Decision Register

| ID | Decision or uncertainty | Current status | Required next action |
|---|---|---|---|
| OB-OD01 | Semester concept and ESP32 acceptance | Open; VibeGuard recommended and shift not proved approved | Obtain explicit teacher/project concept and platform decision |
| OB-OD02 | Phase 4 and procurement | Not proved started or frozen | Complete authorization, current verification, budget and ownership record |
| OB-OD03 | FDM and measurement access | Assumed | Confirm printer, material, operator, tools and schedule |
| OB-OD04 | One-dot mechanics and passive return | No result; passive return unproved | Build/version coupon and retain active retraction until loaded evidence passes |
| OB-OD05 | Cam/guide and servo operating windows | Provisional/unmeasured | Print tolerance matrix and establish safe measured upper/lower bands |
| OB-OD06 | Power and grounding | 2 A/3 A planning only | Validate exact wiring, no back-feed, rail droop/current, resets and heating |
| OB-OD07 | Six-dot integration and mapping set | Not tested/frozen | Run interference/power tests and freeze unit-tested patterns |
| OB-OD08 | Repeatability and lifecycle | Proposed thresholds only | Preregister 100-cycle method and ≥1,000-actuation screen |
| OB-OD09 | Tactile and safety protocol | Open blocker | Obtain approved participant, consent, randomization, guards and stop rules |
| OB-OD10 | Current BOM/prices | Historical planning evidence | Verify exact specifications, suppliers, availability and invoices |
| OB-OD11 | Team role ownership | Proposed only | Assign named primary and backup owners after authorization |
| OB-OD12 | Patent-first adjudication gate | Unresolved | Authorize one gate, define replacement rule or defer |
| OB-OD13 | D11 authorization and evidence | Not authorized/started | Decide after MVP baseline; build oracle, baselines and preregistered tests |
| OB-OD14 | VPD-C7 authorization and evidence | Not authorized/started | Create separate configuration, budget, confidentiality and coupon plan if pursued |
| OB-OD15 | Official `5559/CHE/2014` file and legal status | Not obtained/verified | Retrieve official file and check relevant official registers |
| OB-OD16 | Current worldwide search and FTO | Incomplete/not assessed | Search final enabled mechanism and commission target-country claim review |
| OB-OD17 | Practical-scale and transfer evidence | Absent | Build smaller coupons; conduct blind replacement and independent rebuilds |
| OB-OD18 | Locked silent-error gate | Not run | Freeze oracle, thresholds, `UNKNOWN` handling and kill rule |
| OB-OD19 | Confidentiality, ownership and contribution record | Required, not documented | Separate public/private work and obtain institutional IPR rules |
| OB-OD20 | File/no-file decision | No positive gate passed; no commitment | Revisit only after technical, search, FTO and ownership gates |

# Part II Contradiction Summary

| ID | Chapter | Issue | Controlling resolution | Residual uncertainty |
|---|---:|---|---|---|
| OB-C01 | 04 | Passive reset versus active retraction | Active command controls unless coupled return is physically proved | Passive assistance may exist but is untested |
| OB-C02 | 04–05 | Command/current versus physical state | Direct external or qualified pin-side evidence controls | Current’s independent diagnostic value is unknown |
| OB-C03 | 04 | 2 A versus 3 A supply | External regulated power with measured headroom; figures are provisional | Exact current depends on parts/sequence |
| OB-C04 | 04 | Multiple BOM totals | All are dated planning layers, not current totals | Current prices and printing cost unverified |
| OB-C05 | 04 | “Ready for Phase 4” versus approval open | Architecture is frozen; implementation authorization is not proved | Teacher/platform decision missing |
| OB-C06 | 04 | Precise dimensions/ISO language | Values are provisional non-standard targets | Final geometry and tactile threshold experimental |
| OB-C07 | 04 | Fallback boards/actuators | Any substitution requires authorization and revalidation | Availability and course acceptance open |
| OB-C08 | 04–05 | MVP refinements versus future mechanism | Ordinary calibration/tolerance/logging remain MVP work; D11/C7 are separate | Repository/configuration boundary must be enforced |
| OB-C09 | 05 | MVP aspiration versus evidence | Baseline is not a credible current patent target | No positive patent case exists |
| OB-C10 | 05 | Track D versus conditional Track B | Preserve synthesis disagreement; current status is experimental/no-filing | Future data/search may reclassify |
| OB-C11 | 05 | D11 cooperation versus aggregation | No cooperation demonstrated; use as hypothesis/ablation programme | Interaction data absent |
| OB-C12 | 05 | D11 versus VPD-C7 | Historically related, technically separate | Useful feature subset unknown |
| OB-C13 | 05 | Adjudication or simulation as approval | They are context/planning, not votes or authorization | Patent-first gate unselected |
| OB-C14 | 05 | Raw-lane legal-status claims | Audited synthesis treatment controls; raw lanes are leads | Official status unresolved |
| OB-C15 | 05 | Macro evidence supporting broad claims | Practical-scale evidence is mandatory | No practical-scale coupon |
| OB-C16 | 05 | “Advance conditionally” as filing language | Bounded research only; no filing commitment | Search, FTO, ownership and evidence open |
| OB-C17 | 04–05 | Successful prototype versus patent evidence | Engineering success and patent case are separate | Future work may remain conventional |
| OB-C18 | 04–05 | Public MVP versus confidential research | Separate configurations, access/disclosure and contribution records | Institutional IPR process not attached |

# Part II Source Ledger

The following original organized-workspace paths were materially relied upon. They are grouped by chapter and authority tier. The attachment manifest is excluded because it is file control only. The validated reconciliation controls resolved wording but is not substituted for the original evidence paths below.

## Chapter 04 — TIER_1 current architecture and project authority

- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Architecture_Report_Final.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_Memory_Final.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/01_Final_Architecture/Phase3C_OpenBraille_SOP_Final.md`
- `01_GOVERNANCE_AND_CONTROL/02_Decision_Registers/Project_mC_Decision_Register_v1.2.md`
- `01_GOVERNANCE_AND_CONTROL/01_Project_Requirements/Teacher_Project_Requirements_and_Change_Context.md`

## Chapter 04 — TIER_2 supporting status and evidence

- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/README.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` — duplicate publication format of the same controlled dossier; not independent corroboration
- `04_COMPARATIVE_DECISION/01_Common_Evidence_and_Gates/05_Uncertainty_and_Test_Register.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 05 — TIER_2 valid synthesis, simulation and controlled reference sources

- `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/01_OpenBraille_Patent_Synthesis_Work_Max.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/03_Patent_Synthesis/02_OpenBraille_Patent_Synthesis_Valid_Secondary.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/04_PreBuild_Simulation/OpenBraille_PreBuild_Future_Patent_Case_Simulation.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/HISTORICAL_Phase1C_OpenBraille_Concept_Dossier.docx` — historical origin only; not current architecture or patent authority
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/05_Roadmaps_and_Reference_Dossiers/OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.pdf` — duplicate publication format; not independent corroboration
- `03_CONCEPT_PORTFOLIO/OpenBraille/PATENT_EVIDENCE_INDEX.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/01_Project_mC_Final_Adjudication_Work_Max.md`
- `04_COMPARATIVE_DECISION/02_Final_Adjudications/02_Project_mC_Final_Adjudication_Deep_Research_High.md`
- `04_COMPARATIVE_DECISION/COMPARATIVE_DECISION_INDEX.md`

## Chapter 05 — TIER_3 controlled raw research lanes

- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/01_OpenBraille_Patent_Research_ChatGPT_Deep_Research.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/02_OpenBraille_Patent_Research_Gemini.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/03_OpenBraille_Patent_Research_Perplexity_PARTIAL.docx`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/04_OpenBraille_Patent_Research_Qwen.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/05_OpenBraille_Patent_Research_Mistral.md`
- `03_CONCEPT_PORTFOLIO/OpenBraille/02_Raw_Research/06_OpenBraille_Patent_Research_Microsoft_Copilot.docx`

## Explicit exclusions and non-evidence controls

- The failed moving-roller/encoder-wheel/RAMPS/Mega concept-swapped OpenBraille synthesis is excluded and was not attached.
- The attachment manifest is file control only and is not technical or patent evidence.
- The validated Master Manual Part I controls terminology and current project status; it does not replace the original sources above.
- Independent research lanes and syntheses are evidence sources, not votes.
- No prior-chat context, memory, web research, current pricing, fresh patent searching or unstated assumption was used in this drafting stage.
