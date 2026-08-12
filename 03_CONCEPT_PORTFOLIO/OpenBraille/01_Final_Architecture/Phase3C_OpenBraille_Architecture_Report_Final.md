# Phase 3C — OpenBraille Engineering Architecture Report
## Patent-Oriented Embedded Systems Innovation Pipeline — Project mC

**Prepared by:** Final Engineering Architecture Review Board (synthesis of four independent Phase 3C Deep Research passes)
**Concept:** OpenBraille (Low-Cost Refreshable Single-Cell Braille Display)
**Authoritative document hierarchy (per Phase3C SOP/prompt):** Level 1 — Engineering Design Review (EDR) & PROJECT_CONCEPT_CONTEXT.md · Level 2 — Phase 3B Report/Memory · Level 3 — Phase 3A Report/Memory · Level 4 — independent Phase 3C Deep Research reports (Gemini, Mistral, Perplexity, Qwen)
**Status:** Final — mandatory input to Phase 4 (Prototype Engineering)
**Date:** July 23, 2026

---

## How to read this report

This is a synthesis, not new research. Per the Phase 3C SOP, Phase 3C does not redesign OpenBraille, does not change the engineering hypothesis, and does not introduce new functionality — it transforms already-validated engineering knowledge (EDR → Phase 3A → Phase 3B) into **one** authoritative, implementation-ready architecture. Unlike Phase 3A and 3B, this phase's mandate is not to preserve disagreement where it's substantive — it is required to **select one architecture** and justify the rejection of the alternatives, because this document becomes the actual engineering blueprint for prototype construction.

All four Phase 3C reports correctly grounded themselves in the EDR this round — there is no concept-swap or hallucination problem to report, a first for this pipeline. The significant finding this round is different in kind from Phase 3A/3B's findings: the four reports **converge tightly on the strategy** (macro-scaling to eliminate the fabrication-tolerance kill factor) but **diverge substantively on the specific actuation mechanism**, and one report (Gemini) reverses its own Phase 3B position without acknowledging the reversal. Resolving this divergence — on engineering-evidence grounds, not by vote — is the central task of this report.

---

# TASK 1 — Concept-Fidelity Audit Against the EDR

All four reports were checked against the EDR's actual OpenBraille text (Engineering Identity, Mission, Engineering Hypothesis, Fixed Design Principles, Minimum Demonstrable Success), not against PROJECT_CONCEPT_CONTEXT.md's shorter description or inference from the concept name.

| Report | Fidelity | Notes |
|---|---|---|
| **Mistral** | High | Explicit "✅ Understanding confirmed against EDR" block, restating Identity/Mission/Hypothesis/Fixed Design Principles/MDS near-verbatim. Most structurally complete submission of the four — full three-part structure, 5 ADRs, glossary, assumptions log, open-questions appendix. |
| **Gemini** | High (restatement), **flagged** (reasoning) | Correctly restates mission/hypothesis/MDS/team-and-budget constraints. However, this report **reverses Gemini's own Phase 3B recommendation** — Phase 3B's Gemini report recommended macro-scaled servo+cam as the concept's best team-fit mitigation; this Phase 3C Gemini report instead selects electromagnetic latching and explicitly characterizes cam-driven mechanisms as "a disastrous fit for a software-oriented student team" requiring "aerospace-grade CNC machining tolerances" — without engaging the fact that the same macro-scaling logic it applies to justify hand-wound coils (300% enlargement to make FDM-printable) would apply equally to a macro-scaled cam profile (which is exactly what Mistral and Perplexity's independent analyses demonstrate). This is a genuine internal-consistency gap, not a concept-fidelity failure, and is treated as a reasoning-quality flag rather than an exclusion trigger. Gemini's report is also the only one of the four that never totals a Bill of Materials cost for its own recommended architecture — a completeness gap relative to Mistral and Qwen. |
| **Perplexity** | High | Correct, thorough restatement citing the EDR directly; independently converges with Mistral on the selected architecture (see Task 3). Does not, however, produce a dedicated Student Team Assessment or a formal Architecture Readiness declaration (Ready / Ready with Minor Refinements / Requires Investigation) — two structural elements the Phase 3C prompt requires — so it is treated as strong technical evidence but an incomplete deliverable in its own right. |
| **Qwen** | High (restatement), **incomplete submission** | Correctly restates mission/hypothesis; its MDS restatement adds "refresh to display at least two distinct Braille characters," which is not literal EDR text but a reasonable, non-distorting elaboration of "refreshable" and "repeatability requirements." The more serious issue: **Qwen's submitted report is truncated.** It stops mid-sentence immediately after the "3.2 Complete System Block Diagram" heading, with no diagram, no detailed hardware/mechanical/electrical/software architecture write-up, no Part-3 risk assessment, no bring-up strategy, and no readiness declaration — roughly half of the required Document 1 structure is simply absent. This is treated as an evidence-completeness problem, not a fidelity failure (nothing present is wrong), but it materially reduces how much weight Qwen's submission can carry into the synthesis below. |

No report invented a Braille printer, embosser, OCR system, or full-page display (the historical Phase 2 failure mode). Concept-fidelity risk for OpenBraille in Phase 3C: **low** on interpretation, **moderate** on report reliability (one internally inconsistent report, one incomplete report).

---

# TASK 2 — Confidence Level per Report

| Report | Confidence | Reasoning |
|---|---|---|
| **Mistral** | **Very High** | Zero fidelity issues, fully complete against the SOP's required structure (all three parts, ADRs, appendices), itemized and internally-consistent BOM, and its selected architecture is independently corroborated by a second report (Perplexity). |
| **Perplexity** | **High** | Zero fidelity issues, independently converges with Mistral on the same architecture via its own separate literature review (a strong cross-validation signal, not an artifact of shared reasoning) — but incomplete relative to the required document structure (no team assessment, no formal readiness declaration, no itemized budget total). |
| **Gemini** | **Moderate-High** | Zero fidelity issues and the strongest *evidentiary* backing of any report — its selected mechanism is grounded in named, real, working open-source precedents (MOLBED, MagnePins, and several cited academic/hobbyist EM-latching Braille builds), which is genuinely valuable engineering evidence the other three reports lack. Its confidence is capped below Mistral/Perplexity by (a) the unacknowledged reversal from its own Phase 3B position, (b) the internal inconsistency in how macro-scaling logic is applied selectively, and (c) the absence of a totaled BOM. |
| **Qwen** | **Moderate** | Correct where present, and its actuation choice (non-latching solenoid) surfaces a real engineering trade-off (fastest response, simplest driver) worth recording — but the submission is incomplete, and its own stated mitigation for continuous-hold power draw ("momentary activation strategy") is not actually specified in a way that is mechanically coherent for a non-latching, spring-return actuator that must hold a pin up against reading pressure. This is a real, unresolved gap in Qwen's own proposal, not just an incompleteness issue. |

**Consequence for synthesis:** Mistral is treated as the structural backbone of this report, cross-validated by Perplexity's independent convergence on the same actuation and mechanical architecture. Gemini's real-world precedent research is retained in full as documented evidence for the *rejected* alternative and as a flagged future pathway. Qwen's actuation analysis is retained as supporting evidence for the "why not a non-latching solenoid" reasoning below, but its incomplete Part 3 content is not treated as authoritative for implementation detail.

---

# TASK 3 — Cross-Report Agreements (Decision-Grade)

These are points where three or four of the four reports converge independently, and are treated as settled for this architecture.

1. **Macro-scaling is the correct, unanimous mitigation for Phase 3B's #1 kill factor.** All four reports — despite disagreeing on *what* to macro-scale — independently propose enlarging the physical cell (roughly 2–3× the ISO 17049 2.34 mm dot pitch) specifically to make the mechanism fabricable on accessible FDM 3D printers. This is the single highest-confidence decision in this report and is adopted without qualification.
2. **ESP32 is the unanimous MCU choice.** All four reports select ESP32 over STM32/Arduino alternatives, citing GPIO headroom, hardware PWM timers, cost, and — critically — the team's stated ESP32/STM32 familiarity per PROJECT_CONCEPT_CONTEXT.md and Phase 3B's cross-portfolio finding.
3. **A single 6-dot cell is the correct MDS-aligned prototype scope.** All four reports independently scope to one Braille cell, matching the EDR's Minimum Demonstrable Success exactly — no report proposes a multi-cell or full-line prototype.
4. **Component procurement carries no material risk**, with one narrow exception: Gemini alone flags that *true micro-scale* solenoids/coils sized for actual dot pitch are poorly stocked domestically. This exception dissolves once macro-scaling is adopted, since macro-scale components (standard servos, standard-size solenoids, standard magnet/wire stock) are confirmed available by at least two reports each.
5. **The dominant remaining risk, regardless of which actuator is chosen, is mechanical — not electrical or firmware.** All four reports agree the team's electrical and firmware skills are more than sufficient; none identify the MCU, driver electronics, or control logic as a risk driver.
6. **Budget is comfortably achievable** once macro-scaling and a servo- or solenoid-class actuator are adopted. Only the EM-latching path (Gemini) leaves this unquantified.

---

# TASK 4 — The Central Disagreement: Actuation Principle

Unlike Phase 3A/3B, where disagreements were either interpretation drift (resolved by exclusion) or genuinely irresolvable strategic forks (preserved for a later phase), this disagreement **must** be resolved here, because Phase 3C's output is the actual build blueprint.

### The three candidates on the table

| | **Servo + Cam (macro-scaled)** — Mistral, Perplexity | **EM Latching micro-coils (macro→SLA two-stage)** — Gemini | **Non-latching solenoid (macro, direct-drive)** — Qwen |
|---|---|---|---|
| Driver electronics | None needed — SG90 has integral driver, direct PWM from ESP32 | 4× H-bridge ICs (TB6612FNG) + 74HC595 shift registers + SPI bus | 1× ULN2003A Darlington array |
| Actuator fabrication | Off-the-shelf SG90 servos | **Custom-wound** micro-coils (~300 turns of 0.1 mm wire per coil, ×6–8), requires building an automated winding jig as a sub-project | Off-the-shelf push-pull solenoids |
| Holding state | Servo holds position via internal PWM (mature, self-contained) | True zero-power magnetic latch (bistable) | **Continuous current required to hold pin up** against spring + reading force — an unresolved gap in Qwen's own proposal |
| ISO 17049 compliance path | Not attempted in this phase (explicitly deferred) | Two-stage: 300% FDM validation → 100% SLA-outsourced final stage attempting true compliance | Not attempted; permanently macro |
| Itemized BOM total | ₹2,060–2,850 (Mistral, detailed) | **Not quantified** by Gemini | ₹1,500–2,500 (Qwen, detailed) |
| Firmware/control complexity | Low — position PWM only | High — sequential-actuation scheduling to prevent magnetic crosstalk, thermal watchdog, brown-out handling | Low-Moderate — binary on/off, but no fail-safe against a stuck-HIGH thermal fault |
| Real-world precedent | Servo/cam Braille mechanisms exist in the literature Mistral/Perplexity both cite, but less as a single named open-hardware project | **Strong** — MOLBED and MagnePins are named, working, open-hardware Braille projects using this exact mechanism | Solenoid-based Braille projects exist but are typically non-latching-with-continuous-hold designs of the same type Qwen proposes, with the same thermal caveat |
| Outsourcing dependency | None | **Yes** — Stage 2 requires a commercial SLA printing service, a schedule/budget dependency outside team control | None |

### Engineering reasoning (not vote-counting)

**Why EM latching is not selected, despite its genuine strengths.** Gemini's research is the most evidentially rich of the four — MOLBED and MagnePins are real, working precedents, and zero-power bistable latching is a legitimate engineering advantage over both alternatives. But three problems disqualify it as the Phase 3C selection:

1. **It re-introduces the risk it was supposed to retire.** Gemini's own risk table rates "100% Scale SLA Friction" as **High** and "Magnetic Crosstalk at 2.34 mm" as **Medium** — both are the *same* fabrication-tolerance failure mode Phase 3B named as the portfolio's dominant kill factor for this concept. Gemini's architecture defers that risk to a second stage rather than retiring it, unlike the servo+cam and solenoid paths, which retire it permanently within this phase's scope.
2. **It exceeds the EDR's actual Minimum Demonstrable Success.** The MDS requires "reliably produce refreshable tactile Braille output for at least one Braille cell while meeting basic tactile and repeatability requirements" — it does **not** require ISO 17049 compliance (a point Mistral's and Perplexity's concept-validation sections state explicitly, and which Gemini's own Phase 3B report itself previously argued). Pursuing a compliant 100%-scale stage is a legitimate *future* engineering goal but is not required to validate the hypothesis this phase, and it adds a commercial-service outsourcing dependency, an unquantified cost, and the highest firmware/driver complexity of the three candidates, for a requirement the team is not actually obligated to meet within the semester.
3. **It is the weakest team-capability fit of the three, on the EDR's own terms.** The EDR and PROJECT_CONCEPT_CONTEXT.md both specify the team as three CS/Cybersecurity students with two additional members supporting fabrication/sourcing/documentation — no team member has analog electronics, magnetics, or coil-winding experience. Custom coil winding (with consistency-critical turn counts), H-bridge driver design, shift-register SPI multiplexing, and firmware-enforced sequential-actuation scheduling to prevent magnetic crosstalk collectively represent the highest analog/EE skill demand of the three candidates — directly contrary to the Fixed Design Principle that the architecture should fit the team that exists, not the team the architecture would prefer.

**Why the non-latching solenoid (Qwen) is not selected.** It is simpler electrically than EM latching, but it carries a real, unresolved engineering defect: holding a pin in the raised position against spring return and reading force requires continuous coil energization, which is exactly the thermal/reliability failure mode Gemini's own risk table warns against ("Coil Overheating... a software crash or RTOS lockup while a pin is commanded HIGH... will melt the surrounding plastic chassis within seconds"). Qwen's own proposed mitigation — a "momentary activation strategy" — is not mechanically specified: a momentary pulse cannot hold a pin up without either a latch (which this design does not have) or a self-locking mechanical geometry (which this design also does not specify). This is a gap in the proposal itself, not a matter of report completeness, and it is disqualifying for a design that must run reliably during multi-week user testing.

**Why servo + cam (macro-scaled) is selected.** It is the only one of the three candidates that:
- Fully retires the fabrication-tolerance kill factor within this phase's scope (no deferred second stage, no outsourcing dependency);
- Requires no custom driver electronics (SG90's integral driver + direct ESP32 PWM);
- Has no continuous-hold thermal-risk gap (servo position-holding is a mature, self-contained, commodity-solved problem, unlike a bare non-latching solenoid);
- Has the most conservative, cross-validated, itemized budget (₹2,060–2,850 against a ₹5,000 ceiling and ₹3,000 preferred target — the largest safety margin of the three);
- Is independently arrived at by two of the four reports (Mistral, Perplexity) via separate literature reviews — a genuine convergence signal, not vote-counting, since their reasoning chains (team-fit, budget, complexity) agree even though their source citations differ;
- Matches the *original* Phase 3B finding (including Gemini's own Phase 3B recommendation) that macro-scaled servo+cam is the mitigation that "directly neutralizes... rather than just budgeting time to fight" the kill factor.

**Decision:** Servo + cam macro-scaled electromechanical actuation, ESP32-controlled, is adopted as the Phase 3C architecture. EM-latching micro-coils and non-latching solenoids are retained as documented, deliberately-rejected alternatives — see ADR-001 and "Rejected Alternatives" in the companion Memory document — and EM latching specifically is flagged as a legitimate future-phase pathway *if and only if* the project later gains mechanical/EE mentorship and chooses to pursue ISO 17049 compliance, consistent with Phase 3B's own still-open question about seeking external mechanical mentorship.

---

# FINAL ARCHITECTURE

## Architecture Overview

OpenBraille's Phase 3C architecture is a **single-cell (6-dot), macro-scaled, servo-and-cam-driven refreshable Braille display**, controlled by a centralized ESP32 microcontroller with direct PWM drive to six SG90-class micro servos. Each servo rotates a 3D-printed eccentric cam that lifts a spring-returned pin through a printed guide channel. The cell is deliberately built at approximately 300% of ISO 17049 scale (≈7 mm dot pitch, ≈1.5 mm dot height) to make FDM 3D printing tolerances (±0.1–0.2 mm) adequate for reliable, repeatable motion — trading commercial dot-pitch compliance for buildability, exactly as the EDR's Fixed Design Principles permit ("preserve compatibility with standard Braille principles **where appropriate**").

This architecture validates the engineering hypothesis — that a lower-cost actuation strategy can replace piezoelectric bimorphs while maintaining acceptable tactile performance — through three concrete substitutions: SG90 servos (₹89–149 each) replace piezo bimorphs (₹500–1,000+ each); 3D-printed cams and frame replace precision-machined piezo assemblies; and direct PWM control replaces high-voltage (60–200 V) piezo drive circuitry.

## Subsystem Organization

```
┌───────────────────────────────────────────────────────────────────┐
│                         OPENBRAILLE SYSTEM                         │
├───────────────────────────────────────────────────────────────────┤
│  ┌───────────┐      ┌───────────────┐      ┌─────────────────┐    │
│  │  Power    │◄────►│  ESP32 MCU    │◄────►│  User Interface  │    │
│  │  Supply   │      │  (Controller) │      │ (USB Serial +    │    │
│  │  (5V/2A)  │      │               │      │  optional buttons)│   │
│  └───────────┘      └───────┬───────┘      └─────────────────┘    │
│                              │ Direct PWM (GPIO 16–21)             │
│                              ▼                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │           ACTUATOR BANK — 6× {Servo + Cam + Pin}             │  │
│  │   Dot1   Dot2   Dot3   Dot4   Dot5   Dot6                    │  │
│  └───────────────────────────┬─────────────────────────────────┘  │
│                              ▼                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │        MECHANICAL FRAME — 3D-printed ABS/PETG chassis         │  │
│  │   Base plate (servo mounts) · Guide walls (pin channels)      │  │
│  │   Top plate (cam-follower slots) · Cable channels              │  │
│  └─────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────┘
```

**Operating principle, end to end:** The host (PC/serial terminal) sends an ASCII character → firmware looks up its 6-dot Braille pattern in a Unicode-to-Braille table → firmware computes target servo angles (0° = pin down, ~90° = pin up) for the six dots that differ from the current state → ESP32 hardware timers generate the six PWM signals → servos rotate their cams → cam eccentricity (major/minor radius difference, ≈2 mm) is mechanically amplified through the follower to ≈1.5 mm of vertical pin travel → pins settle in their commanded up/down state, held by the servo's own internal position control (no additional latch needed) → system acknowledges over serial and awaits the next command.

---

## Hardware Architecture

| Subsystem | Selection | Justification | Fallback |
|---|---|---|---|
| **MCU** | ESP32-WROOM-32 DevKit | 30+ GPIO (six PWM channels used, ample headroom), hardware timers for jitter-free PWM, dual-core, team familiarity (PROJECT_CONCEPT_CONTEXT.md), ₹300–800 | STM32F103 "Blue Pill" (loses Wi-Fi/BLE, retains hardware timers) |
| **Actuators** | 6× SG90 micro servo, ₹89–149 each | 20–50 gf torque at 5 V, 0.1 s/60° slew, native PWM control, ubiquitous multi-supplier Indian availability (Robu, Quartz Components, SunRobotics) | MG996R (higher torque, larger footprint, ₹250–350) |
| **Driver electronics** | **None required** — direct GPIO PWM to servo signal line | SG90 servos integrate their own driver circuitry; this eliminates an entire subsystem (and its failure modes) relative to both rejected alternatives | — |
| **Frame** | 3D-printed ABS (0.2 mm layer height, 20% infill) | Durable, opaque (hides internal wiring), adequate ±0.2 mm tolerance at macro scale, fully in-house fabricable | Laser-cut acrylic top guide plate as a precision refinement for the pin-guide layer specifically (combines Mistral's ABS base structure with Perplexity's acrylic-guide-plate suggestion for the highest-tolerance-sensitive component) |
| **Cams** | 3D-printed PETG or Nylon | Low-friction, self-lubricating, durable under macro-scale loads | Delrin, if sourced |
| **Pins** | 2 mm stainless-steel rod, polished/rounded tips | Smooth, durable, off-the-shelf, safe for repeated finger contact | Hardened steel rod |
| **Return mechanism** | Integrated servo torsion spring (no external return spring needed) | Built into SG90 design; removes a component and a failure mode present in both solenoid-based alternatives | External compression/leaf spring, if a non-servo actuator is substituted later |
| **Power** | 5 V/2 A external DC adapter, 1,000 µF decoupling capacitor across the servo rail | Servos draw up to ~500 mA peak individually but are never all six active simultaneously in normal operation; USB-bus power (500 mA limit) is explicitly avoided to prevent brown-out resets | 6 V battery pack (4×AA) with regulator |
| **User interface** | USB serial (115200 baud) for the prototype; optional tactile buttons for standalone demo | Minimal hardware for MDS; direct host-driven test sequences | Physical keypad |

**Total estimated BOM: ₹2,060–2,850**, comfortably inside the ₹3,000 preferred budget and well under the ₹5,000 ceiling (cross-validated in order of magnitude by Qwen's independent, different-actuator BOM of ₹1,500–2,500).

---

## Mechanical Architecture

- **Scale:** 300% of ISO 17049 — dot pitch ≈ 7 mm (vs. 2.34 mm), dot height ≈ 1.5 mm (vs. ~0.5 mm). This is a deliberate, permanent, documented departure from commercial compliance for this prototype phase (see ADR-002), not an interim step toward it.
- **Frame:** single-piece (or base+wall) 3D-printed ABS chassis — base plate for servo mounting (M3 screws), vertical guide walls with pin channels (2.1 mm bore for 2 mm pins, 0.05 mm running clearance), top plate with cam-follower slots, integrated cable-management channels.
- **Force transmission:** each servo horn directly drives an eccentric cam (major radius ≈ 8 mm, minor radius ≈ 6 mm) against a 3D-printed follower (≈5 mm diameter roller) attached to the pin base, converting the cam's ≈2 mm radial throw into ≈1.5 mm of vertical pin travel via mechanical advantage in the follower geometry.
- **Pin guidance:** vertical printed slots (width 2.1 mm, length 15 mm) constrain the pin to pure vertical motion; PETG/Nylon slot material minimizes friction.
- **Reset:** handled entirely by the servo's own internal torsion spring returning to 0° — no external return spring, and no separate reset subsystem to design, fabricate, or maintain.
- **Assembly philosophy:** each {servo + cam + follower + pin + guide} is a self-contained, independently testable and replaceable module — six identical modules dropped into one shared frame. This directly supports the bring-up strategy below (validate one dot in isolation before assembling all six).
- **Critical tolerances to hold:** pin spacing 7.0 mm ± 0.2 mm, pin height 1.5 mm ± 0.1 mm, cam radii ± 0.1 mm, frame flatness ± 0.05 mm, pin verticality ± 1° — all measurable with calipers and a machinist's square, no specialized metrology required.

---

## Embedded Software Architecture

**Initialization (boot):** configure six GPIO pins for hardware-timer PWM output; initialize serial (115200 baud); drive all six servos to 0° (rest); load stored PWM calibration values (0°/90° pulse widths per servo) from EEPROM if present, otherwise use defaults; run a self-test (actuate each pin individually, verify full travel and return, report pass/fail per channel over serial) before entering the ready state.

**Control loop:** event-driven, command-based. Main loop: (1) listen for a serial command; (2) parse it (`SET <dots>`, `CLEAR <dots>`, `SET ALL`, `CLEAR ALL`, `TEST`, `CALIBRATE`); (3) map the requested character/pattern to target servo angles via a Unicode-to-Braille lookup table; (4) update only the servos whose target state has changed (avoid redundant re-actuation); (5) generate PWM via hardware timers (50 Hz, 1000–2000 µs pulse width, 1500 µs ≈ 90°/raised); (6) monitor for servo-timeout (100 ms) and report an error if a channel fails to settle; (7) acknowledge completion over serial.

**Timing:** ESP32 hardware timers provide 1 µs PWM resolution with <10 µs jitter — far tighter than the ~100 µs human tactile-perception threshold, so no custom timing work is needed beyond configuring the built-in timer peripherals correctly.

**Diagnostics & safety:** self-test mode on boot and on demand; per-channel error logging to serial; servo-timeout detection with single retry before reporting failure. Because this architecture has no continuous-hold thermal-fault mode (unlike both rejected alternatives), no watchdog-driven thermal cutoff circuit is required — a direct, structural safety benefit of the selected actuation principle.

**Configuration:** Braille character-to-pattern mapping table (embedded, standard 6-dot Braille), configurable GPIO-to-dot-position assignment, EEPROM-stored per-servo PWM calibration (accounts for manufacturing variance between individual SG90 units).

---

## Electrical Architecture

- **Power distribution:** single 5 V rail from the external adapter feeds both the ESP32 (via its 5 V input pin) and the six servos (via a separate, decoupled 5 V branch — never through the ESP32's onboard 3.3 V regulator). A 1,000 µF electrolytic capacitor sits across the servo rail to absorb switching transients and prevent brown-out resets during simultaneous or rapid-sequence actuation.
- **Signal flow:** ESP32 GPIO 16–21 → six independent hardware-PWM lines → servo control inputs, directly, with no intermediate driver stage. USB serial (UART) carries the host command/acknowledge protocol. Optional GPIO 0–5 reserved for standalone tactile buttons.
- **Wiring convention:** red = 5 V, black = ground, yellow/orange = PWM signal; Dupont connectors for prototyping, soldered joints for the final assembly; 3D-printed cable channels in the frame prevent tangling and strain on servo leads.
- **Isolation:** not required — the entire system operates on a single, low-voltage (5 V) logic-and-power domain; there is no high-voltage or high-current driver stage to isolate, unlike either rejected alternative.

---

## Prototype Validation Strategy

Validation proceeds bottom-up, isolating mechanical variables from electrical and firmware variables before integrating them, consistent with all four reports' shared instinct to de-risk incrementally.

| Milestone | Success criterion | Method | Target week |
|---|---|---|---|
| M1 — Electrical bring-up | ESP32 boots; serial communication works; a bench-driven test servo responds to hand-written PWM | Multimeter, serial monitor | Week 1 |
| M2 — Single servo motion | One bare servo (no cam/pin attached) sweeps smoothly 0°→90°→0° | Visual inspection, calipers | Week 1 |
| M3 — Single-dot mechanical integration | One complete {servo+cam+follower+pin} module raises/lowers 1.5 mm reliably | Calipers, stopwatch | Week 1–2 |
| M4 — All-dot integration | All six dots actuate independently, no mechanical interference between adjacent modules | Visual inspection | Week 2 |
| M5 — Repeatability | 100 consecutive actuation cycles with <0.1 mm pin-position variance | Calipers, automated test script | Week 2 |
| M6 — Tactile validation | A human reader (ideally a visually impaired participant) can reliably distinguish raised vs. lowered dots by touch | Structured user testing | Week 3 |
| M7 — Braille pattern test | Full alphanumeric character set (A–Z, 0–9) displays and clears correctly | Visual + tactile check | Week 3 |
| M8 — Minimum Demonstrable Success | System reliably produces refreshable, repeatable, tactilely legible Braille output for one 6-dot cell — the EDR's literal MDS text | Full end-to-end demonstration | Week 4 |

**Acceptance criteria (EDR-aligned):** tactile distinguishability by touch; ≤0.1 mm repeatability over 100 cycles; ≥1,000 actuations without mechanical failure; BOM ≤ ₹5,000 (target ≤ ₹3,000); functional prototype within the ~2-month timeline.

---

## Implementation Readiness & Prototype Bring-Up Strategy

**Recommended fabrication/assembly order** (each step independently testable before the next, minimizing compounded-failure debugging):

1. Print the chassis (base + walls + top plate) in ABS; verify bare (un-actuated) pins slide freely under gravity alone in their printed guides — this isolates *structural* friction before any actuator or magnetic/mechanical force is introduced.
2. Mount and bench-test one servo in isolation (M1–M2 above).
3. Attach one cam and follower to that servo; verify smooth cam rotation drives the expected ≈1.5 mm follower travel (M3).
4. Install the completed single-dot module into the frame; run the repeatability test on that one dot before building the remaining five.
5. Repeat steps 2–4 for the remaining five servo/cam/pin modules, testing each independently before final assembly.
6. Wire all six servos to ESP32 GPIO; verify each channel independently via the serial `TEST` command before running combined patterns.
7. Run the full self-test, then the M6/M7/M8 validation milestones.

**Required tools:** digital calipers (0.01 mm resolution), multimeter, 5 V/2 A bench or wall power supply, PC with serial terminal, FDM 3D printer (0.2 mm tolerance class), basic hand tools (screwdrivers, wire strippers, pliers). An oscilloscope and stopwatch are recommended but not essential.

**Common failure modes to watch for:** cam-profile roughness causing follower stiction (mitigate with light PTFE lubrication and/or a second print iteration with adjusted clearance); pin binding from print-tolerance stack-up (mitigate with the 0.05 mm designed clearance and light sanding if needed); servo brown-out under simultaneous multi-channel actuation (mitigate with the specified decoupling capacitor and an external, non-USB power source).

---

## Architecture Decision Records

**ADR-001 — Actuation Principle**
- *Decision:* Servo + cam linkage, macro-scaled (~300%).
- *Alternatives considered:* Electromagnetic latching micro-coils (Gemini); non-latching push-pull solenoid (Qwen); Shape Memory Alloy (all four reports, none recommend as primary); voice coil, EAP, pneumatic (all four reports, all rejected as immature/overcomplex for this team).
- *Reasoning:* Only candidate that retires the fabrication-tolerance kill factor permanently within this phase, requires no custom driver electronics, has no continuous-hold thermal-fault mode, and carries the most conservative, itemized, cross-validated budget. See Task 4 above for the full comparative reasoning.
- *Trade-offs accepted:* Non-ISO-compliant dimensions; 50–200 ms response (vs. 5–30 ms for EM/solenoid alternatives) — acceptable, since the MDS specifies "repeatability," not a response-time threshold.
- *Confidence:* High.

**ADR-002 — Dot-Pitch Compliance**
- *Decision:* Accept permanent, documented non-compliance with ISO 17049 for this prototype phase; do not attempt a subsequent true-scale conversion within Phase 3C/4 scope.
- *Reasoning:* The EDR's Minimum Demonstrable Success does not require ISO compliance. Attempting it (as Gemini's two-stage proposal does) reintroduces the exact fabrication-tolerance risk this architecture exists to retire, adds an outsourcing dependency (commercial SLA printing), and is not needed to validate the engineering hypothesis.
- *Future flexibility:* If the project later gains mechanical-engineering mentorship (an option Phase 3B left explicitly open) and elects to pursue commercial-format compliance, Gemini's EM-latching two-stage research — including its named real-world precedents (MOLBED, MagnePins) — should be the starting point for that future work. This is a legitimate, well-evidenced path; it is simply not the correct choice for this team, this budget, and this timeline.
- *Confidence:* High.

**ADR-003 — MCU Platform**
- *Decision:* ESP32-WROOM-32 DevKit.
- *Reasoning:* Unanimous across all four reports; ample I/O and timer resources, team familiarity, low cost.
- *Fallback:* STM32F103 "Blue Pill."
- *Confidence:* High.

**ADR-004 — Driver/Control Architecture**
- *Decision:* Centralized ESP32 control, direct PWM to each servo, no intermediate driver ICs.
- *Reasoning:* SG90 servos are self-driving; adding H-bridges, shift registers, or Darlington arrays (as required by the two rejected actuation principles) would add complexity with no corresponding benefit at single-cell scale.
- *Future flexibility:* If the project scales to a multi-cell line in a later phase, a PCA9685 I²C PWM expander (₹300–500) is the documented upgrade path without changing the actuation principle.
- *Confidence:* High.

**ADR-005 — Manufacturing Pathway**
- *Decision:* In-house FDM 3D printing (ABS frame, PETG/Nylon cams) plus off-the-shelf components; no outsourced fabrication.
- *Reasoning:* Fully within team-accessible tools and timeline; avoids the schedule/cost/quality dependency an outsourced SLA service would introduce.
- *Fallback:* Laser-cut acrylic top plate specifically for the pin-guide layer, if FDM tolerance on that one part proves inadequate in practice.
- *Confidence:* High.

**ADR-006 — Power Architecture**
- *Decision:* External 5 V/2 A DC adapter with 1,000 µF decoupling, not USB-bus power.
- *Reasoning:* USB's 500 mA limit risks brown-out under multi-servo actuation; an external supply removes this risk entirely at negligible cost.
- *Confidence:* High.

**ADR-007 — Rejected Alternative: Electromagnetic Latching (documented for future reference)**
- *Not selected this phase* for the reasons in Task 4. Retained as the recommended starting point for any *future* phase that pursues true ISO 17049 compliance, given its strong real-world precedent (MOLBED, MagnePins) and genuine zero-power-latching advantage.

**ADR-008 — Rejected Alternative: Non-Latching Solenoid (documented for future reference)**
- *Not selected this phase*, due to the unresolved continuous-hold thermal/reliability gap identified in Task 4. Could be revisited if a genuine latching mechanism (magnetic or mechanical detent) is added to close that gap.

---

## Remaining Engineering Risks

| Risk | Category | Severity | Likelihood | Mitigation |
|---|---|---|---|---|
| Insufficient tactile force from SG90 servos at macro scale | Mechanical | Medium | Low | Select higher-torque servo (MG996R) if SG90 proves marginal; optimize cam mechanical advantage |
| Pin misalignment from 3D-print tolerance stack-up | Mechanical | Medium | Medium | Designed-in 0.05 mm clearance; post-process (light sanding) if needed; laser-cut acrylic fallback for the guide layer |
| Cam-follower wear after extended cycling | Mechanical | Low | Medium | PETG/Nylon cam material (self-lubricating); monitor wear during the 1,000-cycle reliability test |
| Servo brown-out under simultaneous actuation | Electrical | Low | Low | External 5 V/2 A supply (not USB bus power) + 1,000 µF decoupling capacitor |
| User cannot reliably distinguish 1.5 mm pins by touch | Validation | Medium | Medium | Structured user testing with visually impaired participants (M6); iterate pin height/spacing if needed — this is an explicitly open assumption, not yet empirically validated by any of the four reports |
| Firmware bugs in Braille character mapping | Software | Low | Low | Use standard, verified Braille lookup tables; unit-test the mapping independent of hardware |
| Schedule slippage from fabrication iteration | Schedule | Medium | Medium | Modular single-dot-first bring-up allows parallel work across the team and limits the blast radius of any one module's rework |

**Overall residual risk after architecture selection: Low–Medium.** Every risk rated High by Phase 3B (fabrication-tolerance failure, actuator force/speed shortfall, team mechanical-CAD inexperience) has been structurally mitigated by the macro-scaling decision and the choice of a driver-free, self-resetting actuator; what remains are ordinary prototype-iteration risks, not kill factors.

---

## Student Team Guidance

The Phase 3C prompt's project team context specifies three CS/Cybersecurity-strong members (firmware, MCU programming, electronics integration, debugging), one beginner programmer seeking a learning opportunity, and two members supporting mechanical fabrication, CAD, sourcing, documentation, and liaison with faculty/lab mechanical expertise.

- **The three technically strong members** should own the ESP32 firmware (state machine, PWM control, serial command protocol, EEPROM calibration), the electrical bring-up (M1–M2), and system integration/debugging (M4 onward). This is squarely within their stated skillset and is where this architecture places the least residual risk.
- **The two fabrication-focused members** should own CAD design and iteration of the frame, cam, and pin-guide geometry, print-tolerance troubleshooting, and physical assembly/testing (the mechanical bring-up steps 1–5 above) — consulting faculty or lab mechanical staff as needed for cam-profile optimization or print-quality issues, per the project's standing assumption that such consultation is available. This is the team's stated growth area, and this architecture (no coil-winding, no magnetics, no precision micro-tolerances) is the least demanding of the three candidates on exactly this dimension.
- **The beginner programmer's learning task:** implementing and unit-testing the Unicode-to-Braille lookup table and the self-test/diagnostic routine. This is a well-scoped, self-contained software module with a clear specification and no dependency on the mechanical build being finished — it can be developed and tested against a bench-mounted single servo early in the schedule, giving a genuine, low-risk embedded-systems learning opportunity without placing any critical-path milestone at risk.
- **Recommended effort allocation:** the majority of team time should go to mechanical iteration (steps 1–5 of the bring-up sequence), not firmware — consistent with every one of the four Phase 3C reports' shared finding that this architecture shifts the dominant remaining risk to mechanical fit-and-finish, not code.

---

## Architecture Readiness Assessment

**Classification: Ready with Minor Refinements.**

**Why not simply "Ready":** several assumptions remain genuinely open and unvalidated by any of the four reports — SG90 torque sufficiency at the chosen mechanical advantage, cam/follower cycle life under the macro-scale design's specific geometry, and (most importantly) whether a 1.5 mm pin height is comfortably tactilely distinguishable, which is an empirical question no report resolves and which directly bears on the EDR's "acceptable tactile performance" language. These are exactly the kind of first-iteration unknowns a Ready-with-Minor-Refinements architecture should carry into prototyping — they require hands-on validation, not further research or redesign, and none of them threaten the core hypothesis.

**Why not "Requires Additional Investigation":** every High-severity risk identified in Phase 3B (fabrication-tolerance failure, actuator force/speed shortfall, team mechanical-CAD inexperience compounding the fabrication risk) has been structurally addressed by this architecture's specific choices — macro-scaling, a driver-free self-resetting actuator, and a fabrication pathway entirely within the team's accessible tools. No open question in this report requires new research, a new deep-research commissioning round, or a strategic decision from the project owner before implementation can begin. This is a genuine improvement over Phase 3B's own "Moderate" prototype-success classification for OpenBraille — the specific mechanism uncertainty that classification reflected has now been resolved.

---

# FINAL ENGINEERING DECLARATION

The OpenBraille architecture defined in this report — a single-cell, macro-scaled, servo-and-cam-driven refreshable Braille display on an ESP32 platform — is judged **technically sound**. It satisfies every element of the Engineering Design Review: it preserves the Engineering Identity (an assistive system exploring alternative low-cost actuation), the Mission (affordability and accessibility), the Engineering Hypothesis (a lower-cost actuation strategy replacing piezoelectric actuation with acceptable tactile performance), all five Fixed Design Principles, and the Minimum Demonstrable Success as literally written — without requiring ISO 17049 compliance, which the EDR does not mandate.

It is **suitable for implementation by the intended five-member student team**: the electrical and firmware work matches the three technically strong members' stated skills precisely; the mechanical work, while the team's acknowledged growth area, has been deliberately reduced to the least analytically demanding form available among the three candidate actuation principles (no coil-winding, no magnetics tuning, no micro-tolerance machining); and a genuine, well-scoped learning task exists for the team's beginner programmer without endangering the critical path.

**Overall engineering confidence: High**, with explicitly flagged, non-blocking open assumptions (tactile-height adequacy, cam cycle life) reserved for empirical validation during Weeks 1–4 of implementation rather than for further architectural research.

**Recommendation: This architecture is formally frozen as the official Phase 3C OpenBraille architecture for Project mC.** It is ready to proceed directly into Phase 4 (Prototype Engineering) without requiring an additional research or synthesis pass. The rejected electromagnetic-latching pathway (Gemini) is preserved in this document, not discarded, as the recommended starting point for any later phase that pursues true commercial-format compliance under different team-capability or mentorship conditions.

---

*This report and its companion memory document (`Phase3C_OpenBraille_Memory_Final.md`) constitute the authoritative Phase 3C engineering reference for OpenBraille and take precedence over the four individual Deep Research reports (Gemini, Mistral, Perplexity, Qwen) wherever they differ from the synthesis above.*
