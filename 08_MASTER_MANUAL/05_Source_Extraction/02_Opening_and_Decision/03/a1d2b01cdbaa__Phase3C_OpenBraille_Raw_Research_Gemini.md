# Source Extraction

- Chapter: `03` — Portfolio Evolution and Concept Origins
- Authority tier: `TIER_4`
- Manual treatment: `HISTORICAL_SUPPORT`
- Original source: `03_CONCEPT_PORTFOLIO/OpenBraille/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_OpenBraille_Raw_Research_Gemini.docx`
- SHA-256: `a1d2b01cdbaa412c79251ffec0b7fad9e606aa16609a664a88b6ebd8149b8b7c`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

Phase 3C — System Architecture & Prototype Planning

Part 1 — Architecture Candidate Exploration

1. Concept Validation

The architectural exploration for the OpenBraille embedded system begins with an uncompromising validation of the core concept against the authoritative Engineering Design Review (EDR) and Phase 3B feasibility constraints.1 The primary mission of the OpenBraille project is to engineer a significantly lower-cost refreshable Braille display cell, thereby dismantling the financial barriers that restrict tactile accessibility for visually impaired users in resource-constrained global environments.1

The defining engineering hypothesis states that a lower-cost actuation strategy can successfully replace conventional piezoelectric bimorph mechanisms while maintaining acceptable tactile performance for a refreshable Braille interface.1 The Minimum Demonstrable Success (MDS) criteria mandate the demonstration of a significantly lower-cost actuation strategy that reliably produces refreshable tactile Braille output for at least one Braille cell, meeting fundamental tactile and repeatability requirements.1

The implementation constraints are exceptionally rigid and dictate the boundaries of the architectural design space. The prototype must be developed within a maximum budget threshold of ₹3000 to ₹5000 INR and completed within a two-month academic timeline.1 Crucially, the development team consists entirely of three Computer Science and Cybersecurity engineering students, explicitly lacking formal mechanical engineering expertise.1 This specific capability mismatch heavily influences the exploration of mechanical vs. software complexity. Finally, the concept explicitly excludes the development of Braille embossers, tactile printers, screen reading software, or high-end full-page commercial displays.1 The following architectural exploration proceeds strictly within this validated scope.

2. Functional Decomposition

To systematically map the available design space, the OpenBraille system must be mathematically and physically decomposed into its fundamental engineering functions. This reduction isolates the electromechanical and software domains required to satisfy the MDS.

The user interaction interface represents the physical contact point where tactile information is transmitted to the reader's finger. The structural integrity of this interface is paramount, as the elevated pin must withstand an average downward reading pressure of 15 to 50 grams of force without collapsing, yielding, or causing reader fatigue.1

The dot actuation function encompasses the physical mechanism that converts stored electrical energy into linear mechanical motion, elevating the Braille pin to the internationally required height. The mechanical transmission and pin guidance function provides the structural pathway that constrains the motion of the actuator. This structural boundary ensures strictly vertical pin translation while adhering to the stringent ISO 17049 standard, which dictates a 2.34 mm dot pitch and a 1.5 mm pin diameter.1

The actuation reset and latching function is arguably the most critical electromechanical barrier. It defines the bistable holding mechanism that maintains the pin in either a raised or lowered state without continuously drawing electrical power, thereby preventing localized thermal overload, minimizing battery drain, and eliminating continuous acoustic noise.1

The controller function serves as the central embedded logic unit, responsible for matrix multiplexing, state management, and the precise orchestration of the actuation signals based on digital text inputs.1 The driver function acts as the high-current switching intermediary, translating the low-voltage, low-current logic signals from the controller into the high-current demands required by the physical actuation mechanism.3 The power subsystem provides the energy regulation and distribution network, ensuring stable voltage rails for sensitive logic components while managing the massive transient current spikes generated during physical actuation.1 Finally, the firmware function encapsulates the low-level embedded software, dictating the microsecond-level timing control, real-time operating system task scheduling, and character translation.1

3. Candidate Actuation Principles

The core of the engineering hypothesis relies on replacing expensive piezoelectric bimorphs.1 All technically credible alternative actuation principles are evaluated based on their operating physics, force characteristics, durability, and viability for a budget-constrained student team.

The piezoelectric bimorph principle utilizes the inverse piezoelectric effect, where applied high voltages (often 60V to 200V) induce microscopic structural bending in ceramic materials. While this incumbent technology achieves approximately 100 grams of force with near-instantaneous 1 to 5 millisecond response times and zero steady-state holding power, it is prohibitively expensive, requires complex DC-DC boost converters, and necessitates precision manual assembly.1 It is fundamentally incompatible with the project's affordability hypothesis.

The electromagnetic (EM) latching principle generates a concentrated magnetic field via custom-wound micro-coils. This field interacts with permanent neodymium magnets (NdFeB) embedded in the Braille pin. By reversing the polarity of the current pulse, the pin is either repelled or attracted. Bistability is achieved by placing passive ferromagnetic anchors (such as steel nuts or washers) at the extremities of the pin's stroke, allowing the permanent magnet to latch into position without continuous power.1 This principle yields over 50 grams of force with response speeds between 10 and 30 milliseconds. Manufacturing relies on inexpensive 0.1mm enameled wire, 3D printed bobbins, and commodity magnets, making it highly suitable for the given budget.8 The known limitation is the requirement for complex bidirectional driver circuitry and the potential for magnetic crosstalk between adjacent pins.1

The Shape Memory Alloy (SMA) principle leverages a thermomechanical phase transformation. Nickel-Titanium (NiTi) wires undergo a shift from a ductile Martensite phase to a rigid Austenite phase when subjected to Joule heating via an electrical current, causing the wire to contract and lift the pin.1 While SMA mechanisms are mechanically simple, silent, and boast extremely low Bill of Materials (BOM) costs, they suffer from profound limitations.11 The heating cycle can be rapid, but the cooling cycle (returning to the Martensite phase) is entirely dependent on ambient thermal dissipation, resulting in sluggish overall response speeds of 50 to 200 milliseconds. Furthermore, dense packing of SMA wires leads to heat buildup within the Braille cell, negatively impacting repeatability and user safety.12

The cam-driven motorization principle converts rotary motion from micro-servos or DC motors into linear motion via precisely profiled camshafts. As the cam rotates, its eccentric lobe pushes a follower pin upward. The geometry of the cam can be designed to provide mechanical locking, resulting in immense lifting force and absolute zero holding power.1 However, response speeds are strictly limited by the RPM of the motors. More critically, the fabrication of miniature, interlocking camshafts and micro-gear reductions requires aerospace-grade CNC machining tolerances.1 This principle is entirely unrealistic for a software-oriented student team lacking mechanical engineering resources.

The pneumatic and microfluidic actuation principle relies on routing pressurized air or fluid through micro-valves to inflate elastic membranes positioned beneath the Braille pins.1 This approach isolates the bulky pressure generation hardware from the reading surface, allowing for dense pin arrays. However, it requires highly specialized latching solenoid valves, microfluidic lithography, and elastomer casting.17 Microscopic leaks lead to catastrophic system failure, rendering it too fragile and complex for a two-month semester prototype.19

4. Candidate Mechanical Architectures

The mechanical architecture governs the transmission of actuation force to the user interface. Adhering to the ISO 17049 requirement of a 2.34 mm dot pitch presents a severe geometric constraint, dictating the physical arrangement of the chosen actuators.1

The direct-drive coaxial architecture aligns the Braille pin directly with the moving actuator core. This arrangement minimizes moving parts, reduces mechanical linkages, and eliminates pivot friction.3 However, it forces the entire actuator mechanism to fit within the 2.34 mm cylindrical footprint. This extreme proximity induces severe magnetic and thermal crosstalk between adjacent cells, requiring highly engineered magnetic shielding or meticulous software timing to prevent interference.1

The scanning or modular carriage architecture decouples the actuators from the pins entirely. In this arrangement, a moving carriage containing a single row of electromagnets sweeps horizontally on a linear rail beneath a matrix of passive, magnetically bistable pins.20 The carriage stops at each row, emits a magnetic pulse to flip the pins into position, and moves on. This radically reduces the total actuator count and eliminates spatial crowding, but it introduces complex dynamic motion control, stepper motors, timing belts, and linear encoders, shifting the failure risk to moving physical tethers.

The rocker and linkage architecture spaces the bulky actuators far apart to mitigate thermal and magnetic interference. Mechanical levers, pantographs, or rockers are then utilized to converge the distant motion paths back into the tight 2.34 mm dot pitch.1 While this solves the spatial constraint, it introduces significant friction, requires precision pivot joints, and multiplies the points of mechanical failure. At the micro-scale, particulate ingress from ambient dust quickly jams these intricate linkages.

The macro-scaled prototyping architecture acknowledges the fundamental incapability of standard Fused Deposition Modeling (FDM) 3D printers to achieve 2.34 mm tolerances. Instead of attempting micro-fabrication immediately, this architecture enlarges the physical dimensions of the cell to a 300% scale.1 This bypasses the ISO 17049 density constraint, allowing the software team to successfully fabricate the mechanism using accessible FDM plastics, thereby validating the electromechanical logic, H-bridge drivers, and embedded firmware before pursuing expensive outsourced micro-manufacturing.1

5. Candidate Control Architectures

The control architecture defines the hierarchical organization of the embedded logic, dictating how the microcontroller orchestrates complex actuation matrices while constrained by pin availability and processing overhead.

The centralized direct control architecture connects a single microcontroller directly to every actuator. While conceptually simple, it suffers from immediate General Purpose Input/Output (GPIO) exhaustion.1 A standard 6-dot cell requiring bidirectional control demands 12 independent GPIO pins. Scaling this to a full line of text is impossible without implementing massive, expensive, high-pin-count Field Programmable Gate Arrays (FPGAs) or Application-Specific Integrated Circuits (ASICs), violating the low-cost hypothesis.1

The matrix multiplexing architecture organizes the actuators into an electrical grid of rows and columns. The microcontroller rapidly scans through this grid, actuating pins sequentially. This approach reduces the required GPIO count exponentially, mathematically mirroring keyboard scanning matrices.1 However, it introduces severe firmware complexity, requiring precise microsecond-level timing and high instantaneous current spikes to maintain acceptable overall cell refresh rates without overheating the multiplexed traces.

The distributed shift-register architecture utilizes cascaded serial-in, parallel-out shift registers (such as the 74HC595) to infinitely expand GPIO capabilities.23 The central microcontroller transmits serialized state vectors via a fast Serial Peripheral Interface (SPI) bus. The registers decode this data and assert parallel outputs to a secondary driver array. This architecture is highly scalable, requires only three MCU pins (MOSI, SCK, LATCH), and provides exceptional educational value regarding digital logic abstraction.1

6. Candidate Driver Strategies

Electromechanical actuators present highly inductive loads. The driver strategy must safely translate low-current logic signals into the high-current demands of coils while protecting the logic controller from destructive back-Electromotive Force (EMF) voltage spikes.

Discrete logic-level MOSFET switching utilizes individual N-channel and P-channel transistors to control current flow. While the component cost is fractions of a cent, constructing a full H-bridge for bidirectional latching solenoids requires four discrete transistors per coil. This consumes massive PCB real estate and introduces critical timing risks; if the firmware accidentally turns on both the high-side and low-side MOSFETs simultaneously, a dead-short (shoot-through) occurs, instantly destroying the circuit.

Integrated H-Bridge ICs (such as the L298N, TB6612FNG, or DRV8833) encapsulate the complex switching logic into a single microchip. These dedicated motor drivers provide built-in shoot-through protection, thermal shutdown, and internal flyback diodes. Crucially, they can reverse the polarity of the current delivered to the coil, a strict requirement for repelling and attracting permanent magnets in a bistable EM latching system.3

Darlington Transistor Arrays (such as the ULN2003) offer robust, multi-channel unipolar driving. They are highly effective for simple solenoids or stepper motors that only require current to flow in one direction. However, because they cannot reverse the current polarity, they are fundamentally incompatible with bistable permanent-magnet latching mechanisms.3

7. Candidate Mechanical Materials

The selection of structural materials directly dictates the kinetic friction, wear resistance, and overall manufacturability of the prototype, especially considering the constraints of a student-led project.1

Stereolithography (SLA) photopolymer resins offer the micron-level isotropic resolution required to achieve the 2.34 mm dot pitch, thin-walled coil bobbins, and microscopically smooth pin channels.1 The smooth surface finish minimizes static friction, a critical factor for low-force actuators. However, standard resins are inherently brittle and prone to shattering under repeated impacts, necessitating the use of specialized, higher-cost "tough" or engineering-grade resins.

Fused Deposition Modeling (FDM) thermoplastics (PLA, ABS, PETG) are ubiquitous, highly accessible, and exceptionally cheap. However, the anisotropic layer-by-layer extrusion process creates a "washboard" surface texture on vertical walls. At the micro-scale required for Braille pins, these layer lines cause severe stiction (static friction), often physically locking the pin in place.18 FDM materials are only viable if the mechanism is aggressively macro-scaled.1

Ferromagnetic materials, specifically neodymium (NdFeB) micro-magnets and commodity steel M2 nuts, are mandatory for establishing the magnetic flux path and generating the bistable holding force in EM designs.7 Highly conductive elements, such as 0.1mm polyurethane-enameled copper wire, are required for winding the micro-coils, allowing hundreds of turns to be packed into a restricted volume to maximize Ampere-turns.8

8. Candidate Power Architectures

The power distribution network must guarantee absolute voltage stability for sensitive logic processors while dynamically satisfying the massive, transient current spikes demanded by inductive electromagnetic actuators.

Relying entirely on a standard 5V USB connection from a host computer simplifies the prototype's physical footprint and provides a unified channel for both power and data.5 However, the USB 2.0 specification strictly limits maximum current draw to 500mA. A single micro-coil undergoing an overdrive pulse can consume 300mA. Exceeding the USB threshold triggers overcurrent protection, dropping the bus voltage and causing the microcontroller to undergo a brown-out reset.

Utilizing a dedicated external DC power supply (such as a 5V/2A or 12V/3A wall adapter) provides vast current headroom, allowing multiple Braille cells to actuate simultaneously without risking logic stability.25 This approach requires onboard buck converters to step the voltage down to 3.3V for the logic layer, separating the high-noise motor rail from the clean logic rail.

Battery power utilizing Lithium-Polymer (LiPo) cells maximizes portability and form-factor mimicking commercial devices. However, managing severe battery voltage sag during high-current actuation spikes requires sophisticated DC-DC boost converters and complex firmware battery management, introducing significant risk for a rapid prototyping schedule.10

9. Manufacturing Pathways

Given the explicit lack of a dedicated mechanical engineer on the team 1, identifying realistic manufacturing pathways is the strongest predictor of prototype success.

Highly feasible pathways rely on external, standardized services combined with clever hack-arounds. This includes purchasing commercial SLA 3D printing services, procuring off-the-shelf M2 hardware, neodymium micro-magnets, and pre-fabricated breakout boards (ESP32 DevKits, TB6612FNG modules).4 Furthermore, automating the most tedious physical task—coil winding—by building a custom, Arduino-controlled stepper-motor winding jig ensures consistency across all actuators without requiring mechanical dexterity.8

Conditionally feasible pathways involve custom PCB design. Designing a two-layer Printed Circuit Board that serves a dual purpose as both the electrical routing plane and the structural baseplate for the mechanical actuators (akin to the MOLBED approach) 8 is achievable for a CS team willing to learn basic EDA software, provided they rely on rapid turn-around fabrication houses.

Unrealistic pathways involve any process requiring precision subtractive manufacturing. The CNC machining of miniature cam shafts 12, the microfluidic elastomer casting required for pneumatic valves 18, or the proprietary chemical fabrication of custom piezoelectric ceramics 1 are fundamentally impossible within the budget, timeline, and skill constraints of this project.

10. Engineering Constraints

A rigorous synthesis of the academic literature, patent landscape, and project-specific parameters reveals several compounding, non-negotiable engineering constraints.

The dimensional tolerance constraint is absolute. The ISO 17049 standard dictates a 1.5 mm pin diameter situated within a 2.34 mm center-to-center footprint.1 The radial clearance between the moving pin and its stationary guide wall must be mathematically optimized; too tight, and microscopic thermal expansion or stiction will cause binding; too loose, and the pin will wobble laterally, destroying the tactile clarity of the Braille dot.

The magnetic crosstalk constraint emerges when scaling from a single pin to a full cell. Actuating one electromagnetic coil generates a sprawling magnetic flux. Given the extreme 2.34 mm proximity, the flux from Coil A can easily exert enough lateral or vertical force on the permanent magnet of adjacent Pin B to unintentionally flip it out of its bistable latch.1

The thermal dissipation constraint threatens system reliability. Rapid, successive actuations of SMA wires or EM coils within a confined, insulating 3D printed plastic chassis lead to severe localized Joule heating. Without active cooling, this heat accumulation can soften or melt the SLA/FDM resins, alter the magnetic coercivity of the neodymium magnets, or present a burn hazard to the user's reading finger.1

Finally, the capability mismatch constraint must shape every decision. The team consists entirely of software-oriented CS/Cybersecurity students.1 Therefore, physical complexity must be actively avoided, and mechanical problems must be translated into software solutions (e.g., using precise PWM algorithms to overcome mechanical friction rather than machining smoother channels).

Part 2 — Architecture Evaluation & Selection

1. Candidate Architecture Review

The exploratory phase systematically identified four primary architecture candidates capable of addressing the OpenBraille engineering hypothesis.

The Electromagnetic (EM) Latching Array utilizes individual micro-coils, NdFeB magnets, and steel nuts to create a bistable direct-drive pin. This architecture boasts high engineering maturity in open-source assistive technology domains, as evidenced by successful implementations in MOLBED and MagnePins.26 Its mechanical simplicity is offset by high software complexity, requiring precise Pulse Width Modulation (PWM) overdrive and H-bridge multiplexing. This exact balance aligns perfectly with the Computer Science team's capabilities.

The Shape Memory Alloy (SMA) Array relies on NiTi wires that undergo crystalline phase changes to contract upon heating. While mechanically minimalist and incredibly cheap, SMA technology suffers from severe thermal latency, requiring up to 200 milliseconds to complete a cooling cycle.1 This sluggish performance destroys the fluency of reading. Furthermore, the high continuous current draw during the heating phase limits battery life and complicates multiplexing.

The Cam-Driven Servo Array employs rotary motors and precision-machined camshafts to mechanically elevate pins. It provides massive lifting force and true zero holding power without relying on magnetic latching.1 However, it requires extreme mechanical precision to fabricate the intricate cams, gear trains, and interlocking mechanisms, rendering it a disastrous fit for a software-oriented student team.1

The Electromagnetic Scanning Carriage features a single row of electromagnets that moves horizontally on a linear rail to set passive magnetic pins.20 This drastically reduces the actuator count, saving costs. However, it introduces highly complex dynamic motion control—requiring stepper motors, linear encoders, and timing belts—shifting the failure risk from stationary electromagnetics to dynamic mechanical tethers.

2. Evaluation Matrix

The architecture candidates are evaluated strictly against the EDR constraints, the ₹3000 to ₹5000 budget, and the software-heavy capabilities of the engineering team.

Evaluation Criteria

EM Latching Array

SMA Array

Cam-Driven Array

EM Scanning Carriage

Preservation of EDR Hypothesis

High

High

High

High

Mechanical Complexity

Moderate

Low

Extremely High

High

Electrical/Firmware Complexity

High (Favorable)

Moderate

Moderate

Very High

Manufacturing Difficulty (for CS Team)

Moderate

Low

Prohibitive

High

Component Availability / Cost

Excellent (Wire, Magnets)

Moderate (NiTi Wire)

Poor (Custom Gears)

Moderate (Linear Rails)

Educational Value (Embedded Systems)

Very High

Low

Low

High

Reliability (Thermal/Wear)

High

Low (Overheating)

High

Moderate (Belt slip)

Overall Engineering Confidence

High (Selected)

Low

Low

Moderate

Engineering Reasoning: The EM Latching Array is definitively selected because it is the only architecture that successfully shifts the engineering burden away from precision mechanical kinematics (Cam/Scanning) and unpredictable thermal thermodynamics (SMA), moving it directly into the domain of embedded firmware and control logic. This strategic shift maximizes the inherent strengths of the CS/Cybersecurity team while mitigating their lack of mechanical expertise.1

3. Actuation System Selection

Selected Actuation Principle: Direct-Drive Electromagnetic Latching (MOLBED-inspired)

Justification: The selected approach utilizes a custom-wound micro-coil consisting of approximately 300 turns of 0.1mm enameled copper wire surrounding a central cylindrical axis. A movable plunger, serving as the Braille pin, contains a micro neodymium magnet (e.g., 2x2mm or 1x0.5mm NdFeB). Two passive ferromagnetic anchors (commodity M2 steel nuts or washers) are embedded at the absolute top and bottom limits of the pin's physical stroke.8

When the driver circuit injects a brief, high-current pulse through the coil, the resulting induced magnetic field violently repels the permanent magnet from the bottom anchor and attracts it toward the top anchor.3 The kinetic energy carries the plunger across the air gap. Crucially, once the electrical pulse terminates, the permanent magnet latches onto the top steel anchor via natural magnetic attraction, achieving the critical requirement of zero-power bistability.1

This electromagnetic approach easily exceeds the required 15 to 50 grams of tactile holding force and achieves rapid response speeds in the 10 to 30 millisecond range, ensuring fluent reading.1 Power consumption is strictly limited to the transient 2-millisecond switching period, virtually eliminating thermal overheating risks. Manufacturability relies on simple coil-winding—which the CS team can automate via a custom Arduino jig—and standard 3D printed bobbins.8

Rejection of Alternatives: Piezoelectric ceramics are rejected due to astronomical costs and dangerous voltage requirements.1 Shape Memory Alloys are rejected due to thermal management complexities, which would require excessive spacing between cells to dissipate heat, violating strict ISO dimensional constraints.11 Cam-driven mechanisms are comprehensively rejected due to the prohibitive mechanical machining tolerances required, which are outside the capability of the team.1

4. Mechanical Architecture Selection

Selected Arrangement: Macro-Scaled Modular Cartridges (Phase 1) transitioning to SLA Matrix (Phase 2)

Justification: The overarching threat to prototype success is the CS team's profound inability to fabricate moving components at the ISO 17049 standard (2.34 mm pitch) using highly accessible but inaccurate FDM 3D printers.1 To mitigate this existential risk without altering the core EDR hypothesis, the mechanical architecture will utilize a Strategic Macro-Scaling approach.1

The initial prototype Braille cell will be designed in CAD and 3D printed at a 300% scale. This artificially enlarges the dot pitch to approximately 7 mm, allowing standard FDM printers (using PLA or PETG) to successfully manufacture the bobbins, plungers, and guides without the catastrophic friction and jamming issues inherent to micro-scale layer lines.

This macro-scale prototype serves as a physical sandbox, allowing the CS team to fully validate the complex embedded firmware, H-bridge driver logic, SPI multiplexing, PWM overdrive algorithms, and magnetic latching physics entirely independently of micro-manufacturing risks.1 Once the software logic and electromechanical principles are flawlessly validated at the macro level, the exact CAD model will be scaled down to 100% and outsourced to a high-resolution commercial SLA resin printing service for final, ISO-compliant integration.7

5. Control Architecture Selection

Selected Architecture: Distributed Shift-Register Control with Centralized Logic

Justification: To independently drive an 8-dot Braille cell utilizing bidirectional electromagnetic latching, each of the eight coils requires a full H-bridge driver. A direct GPIO control architecture requires two control pins per coil (forward and reverse), totaling 16 GPIO lines for a single character cell, immediately exhausting standard microcontroller resources and destroying any potential for scalability.1

The selected architecture intelligently partitions the system. A powerful central controller handles high-level tasks: USB/Serial communication, asynchronous text-to-Braille translation, and the precise orchestration of timing. The distributed driver layer utilizes cascaded 74HC595 serial-in, parallel-out shift registers. The central MCU transmits serialized state vectors via a high-speed SPI bus to the shift registers, which decode the data and assert parallel outputs to the H-bridge ICs.23

This organization radically minimizes microcontroller GPIO usage to just three pins (MOSI, SCK, LATCH), providing theoretically infinite scalability for future multi-cell displays. Furthermore, managing SPI buses and bit-shifting logic maximizes the educational value for the Computer Science team, perfectly aligning with their academic strengths.1

6. Hardware Platform Selection

MCU Family: ESP32 (Espressif Systems).1

Justification: Highly affordable (<₹400), featuring a dual-core 240MHz architecture and a robust FreeRTOS environment. The ESP32's built-in hardware timers provide the microsecond PWM precision required to overdrive coils without burning them out. The inclusion of Wi-Fi and Bluetooth allows for future expansion into wireless screen-reader integration.1

Rejected: Arduino Uno/Nano (the 8-bit AVR architecture lacks the processing headroom for RTOS and concurrent high-speed multiplexing). STM32 (excellent, but the ESP32 offers superior wireless capability for an identical price).

Driver Approach: TB6612FNG Dual H-Bridge Modules.4

Justification: These highly integrated, inexpensive breakout boards provide built-in shoot-through protection and internal flyback diodes. Crucially, they utilize MOSFETs rather than the lossy bipolar transistors found in older L298N drivers, minimizing voltage drop and delivering maximum instantaneous current to the coils. Four modules perfectly satisfy one 8-dot cell.

Power Subsystem: Dedicated 5V 2A External DC Supply.

Justification: A single micro-coil may draw up to 400mA during the transient overdrive pulse. Relying on a laptop USB port risks triggering overcurrent protection or causing catastrophic brown-out resets on the ESP32 logic rail. An external supply physically isolates the high-current motor power rails from the sensitive logic rails.25

7. Manufacturing Strategy

Fabrication Method: The copper micro-coils will be custom wound utilizing 0.1mm enameled wire. To bypass the need for manual dexterity, the team will construct a simple, automated 3D-printed, stepper-motor-driven winding jig controlled by an Arduino to guarantee exactly 300 turns per bobbin.8 The structural chassis will utilize FDM printing for the 300% macro-scaled validation unit, and commercial SLA resin printing for the 100% scale final unit.7

Assembly Strategy: The system is inherently modular. Each pin—consisting of the actuator core, the embedded magnet, and the return nuts—is assembled as an independent sub-unit and dropped into the monolithic printed chassis.8

Reproducibility: Extremely high. All CAD files, PCB routing traces, and firmware source code will be strictly version-controlled. Relying on standardized M2 steel nuts and 2x2mm neodymium magnets ensures global component sourcing without supply chain bottlenecks.8

8. Architecture Risk Assessment

Risk Category

Description

Severity

Mitigation Strategy

Mechanical

Stiction (static friction) causing pins to jam within the micro-printed channels due to SLA resin shrinkage or layer lines.1

High

Implement PWM overdrive in firmware (an initial 1ms high-current spike to violently break static friction, followed by a rapid decay).1 Lubricate SLA channels with dry PTFE.

Integration

Magnetic crosstalk between adjacent cells in the 100% scale model triggering false actuations due to extreme 2.34mm proximity.1

High

Firmware mitigation: Strictly prohibit simultaneous actuation of adjacent pins. Implement a rapid sequential scanning algorithm.20

Electrical

Coil burnout due to firmware hanging during a HIGH state, drawing continuous massive current.

Medium

Implement a hardware watchdog timer (WDT) on the ESP32. Ensure RTOS thread prioritization prevents blocking delays in the motor control loop.

Manufacturing

Inconsistent manual coil winding leading to wildly varying magnetic flux forces across different pins.8

Medium

Enforce the use of the automated Arduino-based winding jig before producing production-tier coils.8

9. Architecture Decision Records (ADR)

ADR-01: Adoption of Macro-Scaled Development Pathway

Context: The engineering team consists entirely of software students lacking mechanical expertise, posing a severe, existential risk to fabricating tight ISO 17049 compliant structures using accessible tools.1

Alternatives Considered: (1) Attempt 100% scale immediately using high-end commercial services, risking rapid budget depletion on failed iterations. (2) Seek external mechanical mentorship to design the chassis.

Selected Option: Two-stage physical development (300% FDM macro-scale physical sandbox, followed by 100% SLA scale deployment).1

Reasoning: This strategically decouples logical and electrical debugging from micro-manufacturing tolerances. It allows the CS team to prove their complex software logic immediately without being blocked by physical jamming.

Trade-offs Accepted: Increases total CAD design time, as it requires maintaining two distinctly scaled sets of models.

Engineering Consequences: The 300% scale model possesses vastly different thermal mass and magnetic reluctance characteristics; therefore, the firmware timing parameters (PWM duration) will require empirical retuning upon downscaling to the 100% model.

ADR-02: Actuation Topology

Decision: Direct-drive electromagnetic latching utilizing permanent NdFeB magnets and steel anchors.

Reasoning: Elegantly solves the zero-power bistability requirement.1 Crucially, it shifts the system complexity away from mechanics into embedded software (H-bridge multiplexing and PWM), actively favoring the team's academic strengths.

Future Flexibility: The SPI logic and driver architecture is completely hardware-agnostic and can be effortlessly scaled to 40-cell multi-line displays by simply cascading additional inexpensive shift registers.

10. Architecture Confidence

Overall Confidence: High

The selected architecture inspires high confidence due to its strong evidentiary backing. The chosen electromagnetic latching mechanism is extensively supported by open-source assistive technology successes (such as MOLBED and MagnePins), which definitively prove the physical viability of achieving ISO-compliant tactile force using 3D printed bobbins, micro-magnets, and 0.1mm wire.8 The remaining uncertainty centers strictly on the transition from the 300% macro-scale to the 100% SLA scale, which involves unpredictable fluid dynamics during resin curing and shrinkage variables that may narrow the pin channels. The architecture assumes the CS team is fully capable of implementing microsecond-accurate, non-blocking timer interrupts within a FreeRTOS environment to manage the overdrive pulses without crashing the core.

Part 3 — Final Architecture Definition & Prototype Blueprint

1. Final Architecture Overview

The finalized OpenBraille architecture represents a modular, single-cell, electromagnetically actuated tactile display that strictly adheres to the approved Engineering Design Review. The system utilizes an ESP32 microcontroller as the central brain to parse incoming digital text, translating it dynamically into standard Braille bitmasks. These bitmasks are serialized over a high-speed SPI bus to a distributed network of shift registers, which in turn command an array of dual H-bridge motor drivers.

The drivers inject precise, microsecond-length, high-current pulses into custom-wound micro-coils. The resulting intense magnetic flux acts upon neodymium magnets embedded within the Braille pins, violently repelling them upward or pulling them downward. Once the physical translation is complete, the magnets latch onto passive ferromagnetic steel anchors, maintaining the tactile state indefinitely with zero continuous electrical power consumption. This deeply integrated cyber-physical approach definitively validates the engineering hypothesis by substituting expensive piezoceramics with intelligent, software-compensated commodity electromagnetics.

2. Complete System Block Diagram

(Textual Representation)

Supplies raw 5V VCC directly to the H-Bridge Motor Rails to handle transient spikes.

Steps down 5V to provide clean, noise-free 3.3V VCC to the ESP32 logic and Shift Registers.

[ User Interface / Host ]

Facilitates data transfer from the host PC/Smartphone to the ESP32 Microcontroller.

Executes FreeRTOS, handles translation logic, and generates SPI clock/data signals.

Transmits serialized state vectors.

Decodes SPI data into 16 parallel output pins.

Receives logic-level signals and switches the 5V high-current rail.

[ Micro-Coils (~300 turns, 0.1mm wire) ]  Receives bidirectional PWM current to generate magnetic flux.

[ Magnetic Flux ]  Interacts with.

[ Plungers ]  Convert magnetic force into linear vertical motion, elevating.

[ Ferromagnetic Anchors (M2 Nuts) ]  Provide passive latching force to the NdFeB Magnets.

3. Hardware Architecture

Microcontroller (MCU): ESP32 WROOM-32 DevKit.

Justification: The 240MHz dual-core clock provides immense computational headroom for FreeRTOS task scheduling, ensuring motor control interrupts are never delayed. Built-in Wi-Fi/BLE ensures seamless testing via PC host software without physical cable tethering.

Fallback Option: STM32F401 "Black Pill" (sacrifices wireless capabilities, but maintains robust hardware timers for precise PWM).

Driver ICs: 4x TB6612FNG Dual Motor Driver Modules.

Justification: Each highly integrated IC handles two distinct coils bidirectionally. Four ICs perfectly cover the requirements of an 8-dot Braille cell. The MOSFET-based internal architecture minimizes voltage drop, delivering maximum instantaneous current to the inductive coils without massive heat generation.4

Fallback Option: DRV8833 or discrete L293D modules (though L293D introduces high thermal losses due to bipolar transistors).

Logic Expansion: 2x 74HC595 8-bit Shift Registers.

Justification: Daisy-chaining two inexpensive registers provides exactly 16 output bits, matching the required input pins for the 4 dual H-bridges (requiring 2 logic pins per coil for forward, reverse, and brake states). This effectively expands the ESP32's capabilities while consuming minimal board space.

Power Regulation: External 5V/2A DC Adapter feeding an LM2596 buck converter (stepped down to 3.3V for logic).

Justification: Electromagnets generate massive current spikes when energized. Separating the sensitive logic power through a dedicated buck converter with bulk electrolytic decoupling capacitors prevents catastrophic brown-out resets.25

4. Mechanical Architecture

The mechanical frame structure consists of a monolithic 3D-printed chassis containing eight vertical cylindrical channels, arranged in the standard 2x4 Braille cell configuration. Each channel serves a dual purpose: acting as the physical bobbin around which the copper wire is wound, and serving as the internal guide rail for the sliding pin.

Force transmission is direct-drive. A 2x2mm neodymium magnet is glued directly into the base of the plastic Braille plunger.8 The magnetic flux generated by the surrounding coil acts directly on this magnet, providing 1:1 linear translation with zero mechanical linkage loss.

The return mechanism relies entirely on bistable magnetic latching. A commodity M2 steel nut is embedded at the base of the channel, and another at the top.8 The permanent magnet is attracted to whichever nut it is closest to, holding the pin up or down indefinitely without power.

Critical mechanical tolerances center on the diametrical clearance between the pin's outer diameter and the channel's inner diameter. The target clearance is 0.1mm to 0.15mm. If the tolerance is too tight, microscopic thermal expansion or stiction will cause binding; if it is too loose, the pin will wobble laterally. Fabrication for Stage 1 will utilize standard PLA FDM printing at 300% scale. Stage 2 will employ commercial SLA resin printing (utilizing rigid engineering resins) at 100% scale to achieve the ISO 17049 requirements.7

5. Electrical Architecture

Power distribution relies on a strict star-topology wiring scheme for the 5V rail, running directly from the power supply to the VMOT (Motor Voltage) pins of the H-bridges. This routing philosophy ensures that high ground-return currents from the coils do not flow across the sensitive logic ground plane, preventing ground bounce and logic corruption.

Signal flow progresses linearly: the ESP32 generates data, serializes it via SPI to the Shift Registers, which output parallel logic vectors to the H-Bridge Logic Inputs, finally driving the high-current coil terminals.

Electrical isolation via bulky optocouplers is deemed unnecessary given the low 5V operating voltage, provided robust flyback diodes are present. The selected TB6612FNG modules feature internal flyback protection diodes, which effectively clamp the dangerous back-EMF voltage spikes generated when the highly inductive coils are rapidly deactivated.4 The prototype will initially utilize solderless breadboards for the logic layer, but connections between the H-bridges and the micro-coils must be physically soldered, as breadboard contact resistance will severely throttle the required transient current spikes.

6. Embedded Software Architecture

The firmware is organized under a Real-Time Operating System (FreeRTOS) running on the ESP32, ensuring deterministic execution of time-critical motor tasks.

Initialization (Boot): The system configures SPI peripherals, initializes the shift registers to a zero state (ensuring all coils are OFF), sets up hardware timers for precise PWM generation, and establishes Serial/BLE communication.

Host Interface Task: A dedicated thread listens asynchronously for incoming text strings via Serial. Upon receipt, it utilizes a static lookup table to translate ASCII characters into standard 8-bit Braille dot masks.

Control Loop Task: The core logic evaluates the current physical cell state against the newly requested state, identifying exactly which pins require toggling via an XOR masking operation to prevent redundant actuations.

Actuator Sequence Generator: To strictly prevent magnetic crosstalk and electrical bus sag, pins are fired sequentially, never simultaneously.20 The generator queues the firing commands into a safe, ordered execution buffer.

PWM Overdrive Execution: When a pin requires elevation, the shift register is loaded to set the corresponding H-bridge to "Forward." The hardware PWM channel applies a 100% duty cycle for approximately 2 milliseconds (providing a massive kinetic kick to overcome static friction and the latching force of the bottom nut), followed by a rapid decay to 0%. To lower the pin, the H-bridge is set to "Reverse," and the pulse is mirrored.1

Diagnostics and Error Handling: The firmware continuously monitors the ESP32's internal brown-out detector. If voltage sag is detected during a pulse, the system automatically increases the sequential delay between subsequent pin actuations, allowing the power supply's bulk capacitors sufficient time to recharge.

7. Interface Definitions

Firmware  Host: Serial UART (115200 baud). The host computer transmits ASCII characters (e.g., "A"). The firmware acknowledges receipt, providing a closed-loop data handshake.

ESP32 MCU  Shift Registers: Standard SPI Protocol (utilizing SCK and MOSI lines). The MCU transmits a 16-bit payload representing the required state of all 8 H-bridges. The dedicated LATCH pin asserts the data instantly to the output pins.

Shift Registers  H-Bridge Drivers: Standard 3.3V GPIO logic. Two lines are required per coil (IN1, IN2). A state of 1,0 triggers an upward thrust; 0,1 triggers a downward thrust; and 0,0 sets the bridge to high impedance (Off).

H-Bridge Drivers  Micro-Coils: High-current 5V analog path. The driver reverses the electrical polarity across the coil terminals.

Actuator  Mechanical Assembly: A magnetic flux gradient that transfers kinetic energy to the NdFeB magnet, moving the physical mass of the Braille pin.

8. Operating Sequence

A complete operational workflow from power-on through a full Braille refresh cycle proceeds as follows:

Power On: The ESP32 boots, initializes the SPI bus, and flushes the shift registers with a 0x0000 payload. At this exact microsecond, all pins are assumed to be in unknown mechanical states.

Homing Cycle: The firmware cycles through all 8 pins sequentially. It applies a 2-millisecond "Reverse" pulse to each coil, forcing all pins into the retracted (down) position, securely latching them to the bottom steel anchors. The cell is now zeroed.

Data Reception: The host PC transmits the ASCII character "C" (representing Braille dots 1 and 4).

Translation: The firmware intercepts "C" and translates it to the binary bitmask 00001001.

Actuation Execution:

The system isolates Dot 1. It loads the shift register to drive H-Bridge 1 "Forward." A 2ms PWM pulse is applied. The intense magnetic field breaks the latch, Dot 1 snaps upward, and latches to the top anchor. H-bridge 1 is immediately disabled.

The system imposes a strict 5-millisecond delay, allowing the magnetic field to fully collapse and the capacitors to recharge.

The system isolates Dot 4. It loads the shift register to drive H-Bridge 4 "Forward." The 2ms PWM pulse is applied. Dot 4 snaps upward and latches. H-bridge 4 is disabled.

Idle State: The system returns to a deep idle state. The coils draw absolutely 0mA of current. The pins remain held firmly upward against reading pressure indefinitely by the permanent magnets.1

9. Prototype Validation Plan

Milestone 1: Electromagnetic Verification. The team will wind a single coil and connect it directly to a current-limited lab bench power supply. Verify that applying 5V physically forces the magnet to shuttle and latch. Measurable indicator:  gf holding force (measured empirically with a digital push-scale).

Milestone 2: Logic Verification. Breadboard the ESP32, shift registers, and one TB6612FNG module. Verify via an oscilloscope that the traces show precise 2-millisecond forward and reverse pulses matching the software commands, confirming that FreeRTOS is not delaying the interrupts.

Milestone 3: Single-Pin Integration. Install one completed coil and pin into the 300% macro-scaled chassis. Actuate it via the firmware. Acceptance criteria: The pin successfully latches up and down 100 consecutive times without sticking, binding, or suffering thermal failure.

Milestone 4: Full Cell Macro-Scale Integration. Integrate all 8 pins into the 300% chassis. Execute a script running the full ASCII alphabet sequence. Acceptance criteria: Sequential actuation entirely prevents magnetic crosstalk, and no uncommanded pin drops occur.

Milestone 5: 100% Scale Final Validation. SLA print the ISO 17049 compliant chassis and integrate the micro-components. Acceptance criteria: Successfully output a refreshable Braille character meeting the 2.34 mm dot pitch 1, definitively validating the Minimum Demonstrable Success.

10. High-Level Component Summary

Component

Purpose

Reason for Selection

Fallback Option

ESP32 DevKit

Central MCU and logic timing.

Cheap, highly capable, hardware timers, excellent CS team familiarity.1

STM32F401 Black Pill

74HC595 Shift Reg.

GPIO multiplexing expansion.

Infinite scalability, robust and simple SPI control.

PCA9685 I2C Expander

TB6612FNG Module

Bidirectional high-current coil driving.

Built-in flyback diodes, dual-channel, low voltage drop.4

DRV8833 or L293D

0.1mm Enameled Wire

Micro-Coil generation.

Strictly required to achieve 300+ turns within micro-space tolerances.8

0.15mm wire (yields fewer turns)

2x2mm NdFeB Magnets

Plunger core / Latching element.

Exceptional magnetic flux density per volume.8

1x0.5mm NdFeB magnets 7

M2 Steel Nuts

Passive latching anchors.

Incredibly cheap, universally available ferromagnetic targets.8

Steel washers

11. Remaining Engineering Risks

Risk 1: 100% Scale SLA Friction (Classification: High)

Unresolved Dependency: SLA photopolymer resin inherently shrinks during post-print UV curing. This unpredictable shrinkage may dynamically alter the critical 0.1mm clearance, causing the pins to bind permanently in the micro-channels.

Mitigation Strategy: Before ordering the final ISO-compliant chassis, print a calibration block containing 5 different test channels with tolerances ranging progressively from 0.05mm to 0.25mm to empirically determine the optimal post-cure clearance.

Risk 2: Magnetic Crosstalk at 2.34mm Pitch (Classification: Medium)

Unresolved Dependency: At the true ISO scale, the sprawling magnetic field generated from Coil 1 may exert enough unintended lateral force on Pin 2's permanent magnet to dislodge it from its delicate latch.1

Mitigation Strategy: Implement strict firmware serialization (never actuate adjacent coils). If static crosstalk persists despite firmware delays, physically wrap the exterior of the coils in mu-metal foil or highly permeable steel tape to actively contain and guide the flux path.

Risk 3: Coil Overheating (Classification: Medium)

Unresolved Dependency: A software crash or RTOS lockup while a pin is commanded HIGH could leave a coil continuously energized. Without thermal limits, the coil will melt the surrounding plastic chassis within seconds.1

Mitigation Strategy: Implement an aggressive hardware watchdog timer (WDT) on the ESP32. As a physical fail-safe, power the H-bridge VCC rail through a hardware monostable multivibrator (e.g., a 555 timer circuit) designed to physically sever power if any pulse exceeds 10 milliseconds.

12. Prototype Assembly & Bring-Up Strategy

To minimize catastrophic integration failures, the engineering team shall execute a rigid, evidence-based build sequence, systematically isolating mechanical variables from software variables.1

A. Assembly Sequence

Fabricate the Winding Jig: Assemble the automated Arduino-based coil winder.8

Wind the Micro-Coils: Produce 10 identical coils (8 for the cell, plus 2 spares). Measure the resistance of each with a multimeter to ensure strict uniformity.

Mechanical Frame (300% Scale): 3D print the macro-chassis. Test-fit the bare plastic pins (without magnets) to verify they drop freely under their own gravity.

Actuator Installation: Apply cyanoacrylate glue to secure the magnets to the plungers. Insert the ferromagnetic anchors (M2 nuts) and the wound coils into the chassis.8

Electronics Mounting: Breadboard the logic layer (ESP32, Shift Registers, H-Bridges) entirely independently of the mechanical chassis to prevent shorts.

Final System Integration: Carefully solder the fragile coil leads to the heavy H-bridge output terminals.

Justification: This sequence meticulously isolates the highly sensitive, error-prone coil manufacturing process from the logic breadboarding. Ensuring the pins slide smoothly under gravity alone (Step 3) guarantees that structural friction is minimized before complex magnetic forces are introduced into the equation.

B. Bring-Up Strategy

Stage 1 - Mechanical Verification Only: Manually push the pins upward and downward using a non-magnetic stylus. Verify they magnetically snap and latch against the top and bottom anchors without any electrical power applied.

Stage 2 - Direct Actuator Verification: Completely bypass the microcontroller. Tap a current-limited 5V bench power supply directly to a single coil's terminals. Verify the pin violently shoots upward. Reverse the electrical leads; verify it shoots downward.

Stage 3 - Driver Electronics Verification: Connect the MCU directly to the H-bridges (temporarily bypassing the shift registers). Use simple, slow GPIO toggles to flip the pin. Verify the H-bridge handles the inductive load without triggering thermal shutdown.

Stage 4 - MCU & Shift Register Communication: Route the logic through the 74HC595 registers. Send SPI commands to toggle diagnostic LEDs instead of the coils. Verify the bit-shifting logic arrays are correct.

Stage 5 - Single Actuation Test: Connect one coil to the fully completed logic chain. Command an "UP" pulse via the serial monitor. Verify actuation.

Stage 6 - Complete Braille Refresh Cycle: Connect all 8 coils. Run an automated script cycling through the entire alphabet. Verify power supply stability and cross-talk resilience under continuous load.

C. Subsystem Verification

Coil/Magnetic Subsystem:

Expected Behavior: High instantaneous thrust resulting in firm, audible latching.

Common Failure Mode: The coil acts as a dead short circuit (resistance too low, indicating damaged enamel) or an open circuit (broken wire).

Troubleshooting: Verify coil resistance is consistently . Rewind immediately if internal shorts exist.

Logic Subsystem:

Expected Behavior: Precise 2-millisecond SPI payload delivery synchronized with the LATCH pin.

Common Failure Mode: Random, uncommanded pin firings due to floating logic inputs.

Troubleshooting: Install 10k pull-down resistors to the shift register latch and clock lines to ensure stability during ESP32 boot.

D. Integration Checkpoints

Coils Validated: The electrical resistance variance between all 8 hand-wound coils is strictly .

Mechanical Homing Validated: All 8 pins latch firmly at both the top and bottom limits when manipulated manually.

Logic Validated: SPI accurately and consistently commands H-bridge polarity changes.

Single Cell Validated: One fully assembled cell (at the 300% macro-scale) correctly displays a complex string like "Hello World" sequentially without error.

E. Critical Failure Points

Power Instability (Brown-out): Actuating a coil pulls the primary bus voltage below 2.7V, causing the ESP32 to reset mid-cycle.

Mitigation: Install a massive 1000µF electrolytic decoupling capacitor across the 5V H-bridge rail, and ensure the ESP32 is powered via a completely separate 3.3V LDO regulator.

Mechanical Wear: Over hundreds of cycles, skin oils, sweat, and ambient dust jam the SLA printed channels, overcoming the magnetic lifting force.

Mitigation: Lubricate the internal channels heavily with dry PTFE (Teflon) spray during assembly. Strictly prohibit the use of wet oils or greases, which act as magnets for particulate dust.

F. Required Tools and Fabrication Resources

Essential: Digital Multimeter (for rigorous coil resistance testing), temperature-controlled soldering station, FDM 3D Printer (for Stage 1 macro-scale fabrication), access to commercial SLA printing services (for Stage 2 final scale), fine wire strippers, and digital calipers.

Recommended: A variable bench power supply (featuring strict current limiting to prevent catastrophic coil fires during Stage 2 testing), and a digital Oscilloscope (to visually verify the 2-millisecond PWM timing and detect invisible voltage sag).

Optional: A USB logic analyzer (to debug complex SPI shift-register payloads if the data vectors become corrupted).

G. Prototype Readiness Checklist

[x] Mechanical architecture finalized (Macro-scaled transitioning to SLA).

[x] Hardware architecture finalized (ESP32, 74HC595, TB6612FNG).

[x] Component selections completed (0.1mm wire, 2x2mm NdFeB).

[x] Assembly pathway defined (Winding jig  Mechanical fit  Electrical Integration).

[x] Validation plan completed (Stages 1 through 6).

[x] Engineering risks documented (Stiction, Crosstalk, Burnout).

[x] Bring-up strategy completed.

13. Architecture Readiness Assessment

Assessment: Ready with Minor Refinements

The proposed architecture successfully and comprehensively satisfies the core EDR mandate to design a significantly lower-cost refreshable Braille cell without relying on expensive, incumbent piezoelectric bimorphs.1 By selecting a direct-drive electromagnetic latching topology paired with a highly scalable, distributed shift-register logic layer, the system effectively validates the engineering hypothesis while driving the Bill of Materials cost toward the absolute minimum.3

The most severe vulnerability threatening the project—the computer science team's profound lack of mechanical engineering expertise—has been proactively neutralized by adopting a two-stage physical scaling architecture (300% initial validation, transitioning to 100% final deployment). This strategic decision transforms a highly prohibitive mechanical machining barrier into a manageable, highly educational software and electrical integration challenge.1

The architecture boasts exceptionally high confidence at both the logical and electrical tiers. The minor refinements remaining involve empirical, hands-on tuning during the physical implementation phase: precisely calibrating the PWM overdrive millisecond timing in firmware to optimize pin thrust against SLA friction, and tuning the sequential actuation delay buffers to eliminate magnetic crosstalk at the dense 100% ISO scale. The blueprint is robust, evidence-backed, fully defined, and strictly authorized to transition immediately into Phase 6 Prototype Engineering.

Works cited

PROJECT_CONCEPT_CONTEXT.md

MagnePins: A Modular, Affordable, and DIY Refreshable Braille and Tactile Display, accessed on July 23, 2026, https://www.youtube.com/watch?v=KqWBjqGEdGI

GitHub - amarpersaud/BrailleDisplay: Electronic Refreshable Braille Display Module, accessed on July 23, 2026, https://github.com/amarpersaud/BrailleDisplay

Braillingo Design Specification - SFU Summit, accessed on July 23, 2026, https://summit.sfu.ca/_flysystem/fedora/2023-03/Braillingo-design-specifications-2022.pdf

BrailleMe - MIT Solve, accessed on July 23, 2026, https://solve.mit.edu/challenges/community-driven-innovation/solutions/10672

The Application of Micro-Vibratory Phenomena of a Shape-Memory Alloy Wire to a Novel Vibrator - MDPI, accessed on July 23, 2026, https://www.mdpi.com/2571-631X/6/3/36

Electromechanical Refreshable Braille Module | Details - Hackaday.io, accessed on July 23, 2026, https://hackaday.io/project/191181-electromechanical-refreshable-braille-module/details

MOLBED - Modular Low Cost Braille Electronic Display - Instructables, accessed on July 23, 2026, https://www.instructables.com/MOLBED-Modular-Low-Cost-Braille-Electronic-Display/

Low-Cost Refreshable Braille Display | PDF | Art | Technology & Engineering - Scribd, accessed on July 23, 2026, https://www.scribd.com/document/559593174/TacRead

Engineering a Portable, Low-Cost Refreshable Braille Display for Communication with the Deaf-Blind Population - Full Abstract - Society for Science, accessed on July 23, 2026, https://abstracts.societyforscience.org/Home/FullAbstract?ProjectId=17443

DETC2013-13159 - Soundability Lab, accessed on July 23, 2026, https://soundability.eecs.umich.edu/img/portfolio/Jain_Tacread_MESA2013.pdf

Design and Development of a Mechanical Braille Display - AIP Publishing, accessed on July 23, 2026, https://pubs.aip.org/aip/acp/article-pdf/doi/10.1063/5.0262623/20498219/020007_1_5.0262623.pdf

Shape memory alloys in modern engineering: progress, problems, and prospects - PMC, accessed on July 23, 2026, https://pmc.ncbi.nlm.nih.gov/articles/PMC12424394/

Full text of "73 Magazine (January 1979)" - Internet Archive, accessed on July 23, 2026, https://archive.org/stream/73-magazine-1979-01/01_January_1979_djvu.txt

Refreshable Braille Module Using Cam Actuated Mechanism - ResearchGate, accessed on July 23, 2026, https://www.researchgate.net/publication/351539848_Refreshable_Braille_Module_Using_Cam_Actuated_Mechanism

Perspiration Compensated Transdermal Alcohol Sensor for Personalized Medicine, accessed on July 23, 2026, https://search.proquest.com/openview/0502cae84669b7fadf8b9eed8af85a83/1?pq-origsite=gscholar&cbl=18750&diss=y

(PDF) Hardware Methods for Onboard Control of Fluidically Actuated Soft Robots, accessed on July 23, 2026, https://www.researchgate.net/publication/353953361_Hardware_Methods_for_Onboard_Control_of_Fluidically_Actuated_Soft_Robots

Hardware Methods for Onboard Control of Fluidically Actuated Soft Robots - Frontiers, accessed on July 23, 2026, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.720702/full

Microfabricated Platforms for Mimicking the Biomechanics of the Human Cardiovascular System Sergio Aguilera Suarez, accessed on July 23, 2026, https://research-repository.rmit.edu.au/ndownloader/files/46283953

Novel mechanism makes refreshable braille displays practical - Arduino Blog, accessed on July 23, 2026, https://blog.arduino.cc/2025/10/10/novel-mechanism-makes-refreshable-braille-displays-practical/

Feedback on moving electromagnetic actuator for braille display - EEVblog, accessed on July 23, 2026, https://www.eevblog.com/forum/projects/feedback-on-my-moving-electromagnetic-actuator-for-braille-display/

Electromechanical Refreshable Braille Module - Hackaday.io, accessed on July 23, 2026, https://hackaday.io/project/191181-electromechanical-refreshable-braille-module

A simple refreshable braille display using the Arduino - General Guidance, accessed on July 23, 2026, https://forum.arduino.cc/t/a-simple-refreshable-braille-display-using-the-arduino/1105305

Affordable DIY Braille Display System | PDF | Arduino | 3 D Printing - Scribd, accessed on July 23, 2026, https://www.scribd.com/document/797601816/MOLBED-Modular-Low-Cost-Braille-Electronic-Display

Friday, December 5, 2025 Veale Convocation, Recreation, and Athletic Center - Case Western Reserve University, accessed on July 23, 2026, https://case.edu/studentlife/ugresearch/sites/default/files/2025-12/Fall%202025%20Intersections%20Abstract%20Compendium.pdf

MagnePins: A Modular, Affordable, and DIY Refreshable Braille and Tactile Display, accessed on July 23, 2026, https://research.monash.edu/en/publications/magnepins-a-modular-affordable-and-diy-refreshable-braille-and-ta/

MOLBED Modular Low cost Braille Electronic Display - Hackaday.io, accessed on July 23, 2026, https://hackaday.io/project/12442-molbed-modular-low-cost-braille-electronic-display
