# Phase 3C — System Architecture & Prototype Planning
## OpenBraille — Complete Architecture Report

**Document ID:** P3C-OB-ARCH-001
**Version:** 1.0
**Status:** Final
**Project:** Project mC — OpenBraille
**Date:** July 2026
**Prepared by:** Engineering Architecture Review Board

---

# Table of Contents

- [Part 1 — Architecture Candidate Exploration](#part-1--architecture-candidate-exploration)
- [Part 2 — Architecture Evaluation & Selection](#part-2--architecture-evaluation--selection)
- [Part 3 — Final Architecture Definition & Prototype Blueprint](#part-3--final-architecture-definition--prototype-blueprint)

---

---

# Part 1 — Architecture Candidate Exploration

---

## 1.1 Concept Validation

### Mission
OpenBraille proposes a low-cost refreshable single-cell Braille display that explores alternative embedded actuation mechanisms and modular scalability to significantly reduce manufacturing cost while maintaining practical usability. The concept focuses on affordability, accessibility, modular embedded design, and scalable assistive technology rather than competing directly with premium commercial Braille devices.

### Engineering Hypothesis
A significantly lower-cost actuation principle can replace conventional piezoelectric mechanisms while still producing a refreshable Braille cell with acceptable tactile performance.

### Minimum Demonstrable Success
A single functional Braille cell (6 dots) that can:
- Raise and lower individual Braille pins on command.
- Refresh to display at least two distinct Braille characters.
- Produce tactile output distinguishable by touch.
- Operate at a cost significantly below commercial piezoelectric equivalents.

### Confirmed Understanding
The prototype validates the engineering hypothesis — it does not compete with commercial refreshable Braille displays. Standard Braille dimensions (ISO 17049: 2.34 mm pitch, ~0.5 mm dot height) are the preferred target, but macro-scaled or relaxed-dimension prototypes are acceptable if they substantially reduce manufacturing risk while still providing convincing validation of the actuation principle. The team consists of three CS/Cybersecurity students with no mechanical engineering background. Budget: ₹3000–₹5000. Timeline: ~2 months.

**No uncertainty identified.** The concept is understood as defined.

---

## 1.2 Functional Decomposition

| Function | Purpose |
|---|---|
| **User Interaction** | Accept input (e.g., serial command, button press) specifying which Braille character to display. |
| **Dot Actuation** | Generate the physical force required to raise or lower each individual Braille pin. |
| **Mechanical Transmission** | Transfer actuator force to the Braille pin along the correct axis of motion. |
| **Pin Guidance** | Constrain each pin to move only vertically, preventing lateral wobble or binding. |
| **Actuation Reset** | Return each pin to its resting (lowered) position when the actuator is de-energized. |
| **Controller** | Interpret user input, map it to a Braille pattern, and issue actuation commands. |
| **Driver Electronics** | Amplify low-power MCU signals to the current/voltage levels required by the actuators. |
| **Power** | Provide stable, regulated electrical power to all subsystems. |
| **Firmware** | Execute the control logic, timing, and communication protocols on the MCU. |
| **Diagnostics** | Provide feedback on system state for debugging and validation (optional for MVP). |

---

## 1.3 Candidate Actuation Principles

### 1.3.1 Electromagnetic Solenoid (Miniature Push-Pull)

- **Operating Principle:** A coil of insulated copper wire generates a magnetic field when energized, pulling a ferrous plunger linearly into the coil core. De-energizing the coil allows a return spring to push the plunger back.
- **Expected Force:** 20–200 gf depending on size and current. Sufficient for Braille pin actuation.
- **Response Speed:** 5–20 ms (fast).
- **Repeatability:** High. Binary on/off behavior is inherently repeatable.
- **Durability:** High for commercial solenoids (100K+ cycles). Lower for improvised designs.
- **Manufacturing Considerations:** Off-the-shelf 5V miniature solenoids are available in India (₹30–80/unit). At macro scale, larger solenoids are even easier to source. Mounting requires alignment but is straightforward at relaxed dimensions.
- **Educational Suitability:** Excellent. Demonstrates electromagnetism, H-bridge/MOSFET driving, and inductive load management.
- **Known Limitations:** High inrush current. Heat generation under sustained activation. Requires mechanical stops to prevent plunger over-travel. Audible click on actuation.

### 1.3.2 Electromagnetic Latching Solenoid

- **Operating Principle:** Similar to a standard solenoid but incorporates a permanent magnet that holds the plunger in the last position without continuous power. A reverse-polarity pulse releases the latch.
- **Expected Force:** 50–150 gf.
- **Response Speed:** 10–30 ms.
- **Repeatability:** High.
- **Durability:** High. Reduced heat compared to non-latching solenoids.
- **Manufacturing Considerations:** Latching solenoids are less commonly stocked in Indian hobbyist markets. May require sourcing from specialized suppliers or salvaging from relays.
- **Educational Suitability:** Good. Introduces magnetic latching and bipolar pulse driving.
- **Known Limitations:** More complex driver circuitry (H-bridge required for bipolar pulses). Higher unit cost. Limited availability domestically.

### 1.3.3 Custom-Wound Electromagnet

- **Operating Principle:** Insulated copper wire wound around a ferrous core (iron nail, steel rod) creates a controllable electromagnet. A separate ferrous plunger is attracted when energized.
- **Expected Force:** 10–100 gf depending on turns, current, and core material.
- **Response Speed:** 10–50 ms.
- **Repeatability:** Moderate. Depends on winding consistency and core properties.
- **Durability:** Moderate. Wire insulation can degrade with heat.
- **Manufacturing Considerations:** Extremely low cost (copper wire + iron nails). Highly customizable. Requires manual winding, which introduces variability.
- **Educational Suitability:** Excellent. Hands-on electromagnetism.
- **Known Limitations:** Difficult to optimize magnetic circuit. Plunger may stick due to residual magnetism. Inconsistent force across hand-wound units.

### 1.3.4 Servo Motor + Cam Mechanism

- **Operating Principle:** A rotary servo motor drives a cam profile. A follower (lever arm or push-rod) rides on the cam surface, converting rotary motion to linear pin displacement. The cam profile can be designed to provide a self-resetting return stroke.
- **Expected Force:** Moderate (SG90 servo: ~1.8 kg·cm torque, sufficient through mechanical advantage).
- **Response Speed:** 50–200 ms (slower than solenoids, limited by servo slew rate).
- **Repeatability:** High (servo position control is closed-loop).
- **Durability:** Moderate. Cam-follower contact surfaces wear over time. SG90 plastic gears can strip under shock loads.
- **Manufacturing Considerations:** SG90 servos are extremely cheap (₹89–149) and widely available. Cam profiles can be 3D printed. At macro scale, cam geometry is forgiving.
- **Educational Suitability:** Excellent. Demonstrates rotary-to-linear conversion, cam design, and PWM control.
- **Known Limitations:** Mechanically more complex than direct drive. Backlash in servo gears. Wear at cam-follower interface. Slower refresh rate.

### 1.3.5 Pico-Motor (Vibration Motor) + Cam

- **Operating Principle:** A small DC vibration motor (eccentric rotating mass type) is modified by replacing the eccentric mass with a cam profile. Rotation pushes a lever arm connected to the Braille pin.
- **Expected Force:** Low to moderate.
- **Response Speed:** 50–150 ms.
- **Repeatability:** Low to moderate. Open-loop speed control makes precise positioning difficult.
- **Durability:** Low. Vibration motors are not designed for sustained directional loading.
- **Manufacturing Considerations:** Very low cost. Motors are ubiquitous (salvaged from phones). Cam attachment requires improvisation.
- **Educational Suitability:** Moderate. Creative but unreliable.
- **Known Limitations:** No position feedback. Difficult to control precisely. High wear. Not recommended for reliable operation.

### 1.3.6 Shape Memory Alloy (SMA / Nitinol Wire)

- **Operating Principle:** A Nitinol wire contracts when heated by electrical current (Joule heating). The contraction pulls a lever arm or directly lifts a Braille pin. When current is removed, the wire cools and elongates, allowing a return spring to lower the pin.
- **Expected Force:** 20–100 gf (depending on wire diameter and length).
- **Response Speed:** 50–200 ms (heating is fast; cooling is slow without active cooling).
- **Repeatability:** Moderate. Degrades over thermal cycles due to fatigue.
- **Durability:** Moderate to low. Typical cycle life: 10K–100K cycles before fatigue failure.
- **Manufacturing Considerations:** Nitinol wire is available in India (₹299–499/meter). Requires precise current control (PWM). Mechanical amplification (cantilever) needed due to small stroke (~4–5% of wire length).
- **Educational Suitability:** High. Novel technology, demonstrates materials science.
- **Known Limitations:** Slow cooling limits refresh rate. Complex current control. Fatigue life uncertainty. Small stroke requires mechanical amplification. Hysteresis in temperature-force relationship.

### 1.3.7 Voice Coil Actuator

- **Operating Principle:** A coil of wire suspended in a permanent magnetic field experiences a Lorentz force proportional to the current. Bidirectional linear motion is possible.
- **Expected Force:** 10–100 gf.
- **Response Speed:** Very fast (<5 ms).
- **Repeatability:** High with closed-loop control.
- **Durability:** High (no mechanical contact in the moving element).
- **Manufacturing Considerations:** Difficult to fabricate at small scale without precision tooling. Commercial voice coils are expensive. Salvaging from small speakers is possible but inconsistent.
- **Educational Suitability:** Moderate. Demonstrates Lorentz force but fabrication is challenging.
- **Known Limitations:** Requires precision alignment of coil and magnet. Expensive or difficult to source. Analog current control needed for position (not binary).

### 1.3.8 Piezoelectric Actuator (Reference Only)

- **Operating Principle:** A piezoelectric ceramic element expands when a high voltage is applied, pushing a Braille pin upward.
- **Expected Force:** 50–200 gf.
- **Response Speed:** <1 ms (fastest of all candidates).
- **Repeatability:** Very high.
- **Durability:** Very high (100M+ cycles).
- **Manufacturing Considerations:** Prohibitively expensive (~$100/cell for commercial units). Requires high-voltage driver (100–200V). Not compatible with the engineering hypothesis of finding a *lower-cost* alternative.
- **Educational Suitability:** Low for this project (cost-prohibitive).
- **Known Limitations:** Cost directly contradicts the engineering hypothesis. High-voltage safety concerns. **Included for reference only — not a viable candidate.**

---

## 1.4 Candidate Mechanical Architectures

### 1.4.1 Direct-Drive (Actuator → Pin)

- **Motion Path:** Actuator plunger pushes or pulls the Braille pin directly along its vertical axis.
- **Complexity:** Low. Fewest moving parts.
- **Fabrication Challenges:** Actuator must be precisely aligned with the pin axis. At standard dot pitch (2.34 mm), packing six actuators is extremely tight. At macro scale (>4 mm pitch), alignment becomes forgiving.
- **Maintenance:** Minimal. No linkages to wear.
- **Alignment Sensitivity:** High at standard pitch; low at macro scale.
- **Scalability:** Good for modular single-cell designs.

### 1.4.2 Lever System

- **Motion Path:** Actuator pushes one end of a pivoting lever; the other end pushes the Braille pin. Provides mechanical advantage (force amplification) at the cost of increased stroke at the actuator end.
- **Complexity:** Moderate. Requires pivot bearings and precise lever arm ratios.
- **Fabrication Challenges:** Pivot points must be low-friction. 3D-printed pivots tend to wear quickly.
- **Maintenance:** Moderate. Pivot wear over time.
- **Alignment Sensitivity:** Moderate.
- **Scalability:** Moderate. Each cell requires six levers, increasing part count.

### 1.4.3 Rocker Mechanism

- **Motion Path:** A seesaw-like rocker converts a lateral actuator push into vertical pin motion.
- **Complexity:** Moderate to high.
- **Fabrication Challenges:** Similar to lever systems. Requires precise pivot alignment.
- **Maintenance:** Moderate.
- **Alignment Sensitivity:** High.
- **Scalability:** Low. Complex geometry at small scale.

### 1.4.4 Cam System (Rotary-to-Linear)

- **Motion Path:** A rotating cam pushes a follower connected to the Braille pin. The cam profile determines the pin's displacement profile.
- **Complexity:** Moderate. Requires rotary actuator (servo/motor) and cam-follower interface.
- **Fabrication Challenges:** Cam profile must be smooth. 3D-printed cams may have layer-line roughness causing friction.
- **Maintenance:** Moderate. Cam-follower wear.
- **Alignment Sensitivity:** Moderate.
- **Scalability:** Moderate. One servo per cam (or one servo driving a shaft with multiple cams).

### 1.4.5 Linkage System

- **Motion Path:** A series of rigid links and joints transmit motion from a remote actuator to the pin.
- **Complexity:** High. Multiple joints, each a potential failure point.
- **Fabrication Challenges:** Very high for student-level fabrication. Tolerance stack-up across multiple joints.
- **Maintenance:** High.
- **Alignment Sensitivity:** Very high.
- **Scalability:** Poor.

### 1.4.6 Rack-and-Pinion

- **Motion Path:** A rotary actuator drives a pinion gear that engages a linear rack attached to the Braille pin.
- **Complexity:** Moderate to high.
- **Fabrication Challenges:** Gear teeth must be precise. 3D-printed gears at small scale are unreliable.
- **Maintenance:** Moderate. Gear wear and backlash.
- **Alignment Sensitivity:** High.
- **Scalability:** Poor at Braille scale.

### 1.4.7 Magnetic Coupling (Non-Contact)

- **Motion Path:** An actuator moves a magnet beneath the frame; a second magnet attached to the pin is repelled/attracted through the frame material, moving the pin without mechanical contact.
- **Complexity:** Moderate.
- **Fabrication Challenges:** Requires precise magnet alignment and consistent magnetic field strength. Frame material must be non-magnetic.
- **Maintenance:** Low (no contact wear).
- **Alignment Sensitivity:** High.
- **Scalability:** Moderate.

### 1.4.8 Modular Cartridge

- **Motion Path:** Each Braille dot is a self-contained cartridge (actuator + pin + spring + guide) that plugs into a common frame.
- **Complexity:** Low per module; moderate for the frame.
- **Fabrication Challenges:** Cartridge dimensions must be consistent. At macro scale, this is achievable with 3D printing.
- **Maintenance:** Excellent. Individual cartridges can be replaced.
- **Alignment Sensitivity:** Low (each cartridge is self-aligning).
- **Scalability:** Excellent. Add modules to expand the display.

---

## 1.5 Candidate Control Architectures

### 1.5.1 Centralized Control

- **Description:** A single MCU manages all input processing, Braille pattern mapping, and actuator driving. All six dot drivers connect directly to the MCU's GPIO pins.
- **Advantages:** Simplest firmware. No inter-processor communication. Easiest to debug. Lowest component count.
- **Disadvantages:** All I/O pins consumed by one cell. Scaling to many cells requires I/O expansion (shift registers, I2C expanders).
- **Suitability:** Ideal for a single-cell prototype.

### 1.5.2 Distributed Control

- **Description:** Multiple smaller MCUs, each controlling a subset of dots or a single cell. A master MCU coordinates the slaves via a bus (I2C, SPI, UART).
- **Advantages:** Highly scalable. Each cell is independently addressable.
- **Disadvantages:** Complex firmware (communication protocols, synchronization). Higher component cost. More failure points.
- **Suitability:** Overkill for a single-cell MVP. Appropriate for future multi-cell expansion.

### 1.5.3 Modular Driver Arrangement

- **Description:** A single master MCU with modular driver boards (e.g., shift-register-based driver modules) that can be daisy-chained.
- **Advantages:** Balances simplicity and scalability. Master firmware remains simple; scaling is handled by adding driver modules.
- **Disadvantages:** Moderate complexity. Requires shift-register or I2C-expander integration.
- **Suitability:** Good for future expansion beyond the MVP.

---

## 1.6 Candidate Driver Strategies

### 1.6.1 H-Bridge IC (L293D / L298N)

- **Advantages:** Integrated protection diodes. Bidirectional current (useful for latching solenoids). Simple logic-level interface. Low cost (₹49–179).
- **Disadvantages:** Voltage drop across internal transistors (~1.2–2V). Limited current per channel (600 mA for L293D). Heat dissipation at high currents.
- **Scalability:** Moderate. Each L293D drives two actuators.
- **Educational Suitability:** Excellent. Standard introductory motor-driver IC.

### 1.6.2 Discrete MOSFET Switching (N-Channel, e.g., IRF540N / IRLZ44N)

- **Advantages:** Very low on-resistance (minimal voltage drop). High current capability. Low cost per unit (₹15–30).
- **Disadvantages:** Requires external flyback diodes for inductive loads. More wiring. Unidirectional only (suitable for non-latching solenoids).
- **Scalability:** Good. One MOSFET per actuator.
- **Educational Suitability:** Good. Teaches transistor switching and inductive load protection.

### 1.6.3 Transistor Arrays (ULN2003 / ULN2803)

- **Advantages:** Darlington array with built-in flyback diodes. Seven or eight channels per IC. Very simple interface (logic-level input, open-collector output). Low cost (₹30–60).
- **Disadvantages:** High voltage drop (~1V per Darlington pair). Limited to ~500 mA per channel. Unidirectional only.
- **Scalability:** Good. One IC drives six to eight actuators.
- **Educational Suitability:** Excellent. Simplest driver option for solenoids.

### 1.6.4 Dedicated Driver ICs (e.g., DRV8833, TB6612FNG)

- **Advantages:** Modern, efficient MOSFET-based H-bridges. Lower voltage drop than L293D. Higher current capability. PWM support.
- **Disadvantages:** Higher cost (₹100–250). May be overkill for simple on/off solenoid control.
- **Scalability:** Good.
- **Educational Suitability:** Good.

---

## 1.7 Candidate Mechanical Materials

### 1.7.1 Frame

| Material | Suitability | Notes |
|---|---|---|
| **PLA (3D printed)** | High | Easiest to print. Adequate rigidity for macro-scale frame. Low heat resistance (may soften near solenoids). |
| **PETG (3D printed)** | High | Better heat resistance than PLA. Good rigidity. Slightly harder to print. |
| **ABS (3D printed)** | Moderate | Good heat resistance and strength. Warping issues during printing. Requires heated bed. |
| **Acrylic (laser cut)** | High | Excellent dimensional accuracy. Rigid. Easy to laser-cut flat panels and stack. Brittle under impact. |
| **Aluminum (machined)** | Low feasibility | Excellent rigidity and heat dissipation. Requires CNC machining or manual milling — beyond team capability and budget for custom parts. |
| **Plywood / MDF (laser cut)** | Moderate | Cheap and easy to laser-cut. Susceptible to moisture. Adequate for a prototype frame. |

### 1.7.2 Moving Components (Pins, Plungers)

| Material | Suitability | Notes |
|---|---|---|
| **3D-printed PLA/PETG rods** | Moderate | Dimensional accuracy depends on printer. Surface roughness may cause friction. |
| **Acetal (Delrin) rods** | High | Low friction, excellent dimensional stability. Available as off-the-shelf rods. Can be cut to length. |
| **Brass rods** | High | Smooth surface, good weight for tactile feel. Available from hardware stores. |
| **Steel pins / nails** | High | Very smooth, strong. Ferrous — compatible with electromagnetic actuation. |
| **Nylon rods** | Moderate | Low friction but can absorb moisture and swell. |

### 1.7.3 Guides

| Material | Suitability | Notes |
|---|---|---|
| **3D-printed sleeves** | High | Integrated into the frame. Tolerance depends on printer. Oversized holes + post-drilling can improve fit. |
| **PTFE tubing** | High | Extremely low friction. Available in small diameters. Can be inserted into 3D-printed holes as liners. |
| **Brass tubing** | Moderate | Smooth inner surface. Available from hobby shops. |

### 1.7.4 Return Mechanisms

| Material | Suitability | Notes |
|---|---|---|
| **Steel compression springs** | High | Off-the-shelf, predictable force. Available in small sizes (₹1–5/spring). |
| **Silicone rubber pads** | Moderate | Provide gentle return force. Less predictable than springs. |
| **Elastic lever arms (3D printed)** | Moderate | Eliminates separate spring. Depends on material fatigue properties. |

---

## 1.8 Candidate Power Architectures

### 1.8.1 5V External USB/Adapter Supply

- **Voltage:** 5V DC.
- **Current:** 1–3A depending on actuator count and type.
- **Advantages:** Simplest. No battery management. Stable voltage. USB power banks or phone chargers are ubiquitous.
- **Disadvantages:** Tethered operation. Not portable.
- **Suitability:** Ideal for benchtop prototype validation.

### 1.8.2 Li-Ion / LiPo Battery (3.7V nominal)

- **Voltage:** 3.7V nominal (4.2V full, 3.0V empty).
- **Current:** 1–3A capable (18650 cells).
- **Advantages:** Portable. Rechargeable.
- **Disadvantages:** Requires charging circuit (TP4056 module). Voltage drops during discharge. Safety concerns (overcharge, short circuit).
- **Suitability:** Good for a portable demonstration, but adds complexity.

### 1.8.3 9V Battery

- **Voltage:** 9V.
- **Current:** Limited (~500 mA for alkaline).
- **Advantages:** Simple. Readily available.
- **Disadvantages:** Low current capacity. Voltage drops rapidly under load. Not suitable for multiple solenoids.
- **Suitability:** Poor for this application.

### 1.8.4 12V External Supply

- **Voltage:** 12V DC.
- **Current:** 1–5A.
- **Advantages:** Compatible with industrial solenoids. Higher force output.
- **Disadvantages:** Requires voltage regulation for MCU (5V/3.3V). Less convenient than USB.
- **Suitability:** Only if 12V solenoids are selected.

---

## 1.9 Manufacturing Pathways

| Method | Feasibility | Notes |
|---|---|---|
| **FDM 3D Printing** | **Highly Feasible** | Primary fabrication method. Suitable for frame, pin guides, mounting brackets, cam profiles (if used). Tolerance: ±0.2–0.5 mm. Macro-scale designs are forgiving. |
| **Laser Cutting (Acrylic/Plywood)** | **Highly Feasible** | Excellent for flat frame panels. Dimensional accuracy: ±0.1 mm. Fast and cheap at local fab labs. |
| **Off-the-Shelf Assembly** | **Highly Feasible** | Solenoids, servos, springs, rods, screws — all available from Indian suppliers (Robu, Quartz Components, SunRobotics). |
| **Basic Soldering** | **Highly Feasible** | Team has embedded programming experience; basic through-hole soldering is within capability. |
| **Breadboard Prototyping** | **Highly Feasible** | Suitable for initial electronics validation. Not recommended for final assembly due to loose connections. |
| **Perfboard / Stripboard** | **Conditionally Feasible** | More reliable than breadboard for final assembly. Requires soldering skill. |
| **Custom PCB** | **Conditionally Feasible** | Possible via online services (JLCPCB, PCBWay) with ~2-week lead time. Adds cost and complexity. Not necessary for MVP. |
| **Simple Machining (Drilling, Tapping)** | **Conditionally Feasible** | Available at local machine shops for metal parts. Useful for drilling precise holes in acrylic or aluminum. |
| **CNC Machining** | **Unrealistic** | Beyond team capability and budget for custom parts. |
| **Injection Molding** | **Unrealistic** | Industrial process. Not applicable to a single-unit prototype. |

---

## 1.10 Engineering Constraints (Literature-Supported)

| Constraint | Evidence | Implication |
|---|---|---|
| **Force** | Braille pins require 20–100 gf for reliable tactile perception (Phase 3A, commercial teardowns). | Actuator must reliably exceed minimum force threshold. |
| **Stroke** | ISO 17049 specifies ~0.5 mm dot height. Macro-scale prototypes may use 1–3 mm. | Actuator stroke must match mechanical design. |
| **Tolerance** | Standard dot pitch (2.34 mm) is extremely tight for FDM printing (±0.2–0.5 mm). Phase 3B unanimously identified this as the central manufacturing constraint. | Macro-scaling or precision post-processing required. |
| **Friction** | Pin-guide friction directly affects actuation reliability and consistency. | Low-friction materials (PTFE, Delrin) or oversized guides recommended. |
| **Wear** | Repeated actuation causes wear at contact surfaces (cam-follower, pin-guide). | Material selection and modular replacement strategy. |
| **Heat** | Solenoids and SMA wires generate heat under sustained activation. | Thermal management (duty cycle limits, heat sinks, ventilation). |
| **Alignment** | Actuator-to-pin misalignment causes binding and inconsistent force. | Direct-drive at macro scale minimizes alignment sensitivity. |
| **Tactile Consistency** | All six dots must feel uniform to the reader. | Consistent actuator force and spring return across all dots. |
| **Assembly Complexity** | Team has no mechanical engineering background (Phase 3B, EDR). | Minimize part count, avoid precision fits, use modular design. |

---

---

# Part 2 — Architecture Evaluation & Selection

---

## 2.1 Candidate Architecture Review

| Candidate | Operating Principle | Engineering Maturity | Expected Performance | Manufacturing Complexity | Educational Suitability | EDR Compatibility |
|---|---|---|---|---|---|---|
| **A: Solenoid Direct-Drive (Macro)** | EM solenoid pushes pin directly | High | High force, fast (5–20 ms) | Low at macro scale | High | Full |
| **B: Latching Solenoid** | EM + permanent magnet latch | Moderate | Good force, zero holding power | Moderate (sourcing) | Good | Full |
| **C: Custom Electromagnet** | Hand-wound coil + iron core | Moderate | Variable force, moderate speed | Moderate (winding consistency) | Very High | Full |
| **D: Servo + Cam (Macro)** | SG90 servo drives 3D-printed cam | High | Moderate force, slower (50–200 ms) | Moderate (cam profile) | Very High | Full |
| **E: SMA Wire + Cantilever** | Nitinol wire pulls lever arm | Low-Moderate | Low force, slow (50–200 ms) | High (amplification mechanism) | High | Partial (risk of insufficient force) |
| **F: Voice Coil** | Lorentz force on coil in magnet field | Moderate | Fast, precise | High (precision alignment) | Moderate | Full |

---

## 2.2 Evaluation Matrix

| Criterion | A: Solenoid (Macro) | B: Latching Solenoid | C: Custom EM | D: Servo+Cam | E: SMA | F: Voice Coil |
|---|---|---|---|---|---|---|
| Preservation of hypothesis | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★☆☆ | ★★★★☆ |
| Mechanical complexity | ★★★★★ (Low) | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ |
| Electrical complexity | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★★★ (Low) | ★★☆☆☆ | ★★☆☆☆ |
| Firmware complexity | ★★★★★ (Low) | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★★★☆☆ |
| Manufacturing difficulty | ★★★★★ (Easy) | ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★☆☆☆ | ★☆☆☆☆ |
| Component availability | ★★★★☆ | ★★☆☆☆ | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★☆☆☆ |
| Educational value | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★☆ |
| Reliability | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★☆☆☆ | ★★★☆☆ |
| Maintenance | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★☆☆☆ | ★★★☆☆ |
| Expandability | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |
| Cost confidence | ★★★★☆ | ★★★☆☆ | ★★★★★ | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| Prototype suitability | ★★★★★ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★☆☆☆ | ★★☆☆☆ |
| Overall confidence | **HIGH** | MODERATE | MODERATE | HIGH | LOW | LOW |

---

## 2.3 Actuation System Selection

### Selected: **Miniature Electromagnetic Solenoid (Non-Latching, Direct-Drive, Macro-Scaled)**

### Justification

1. **Highest engineering maturity.** Solenoids are the most proven electromagnetic actuator technology. Their force-displacement characteristics are well-documented and predictable.
2. **Fastest response time** (5–20 ms) among the viable candidates, enabling rapid Braille refresh.
3. **Electrically trivial for this team.** Binary on/off control via MOSFET or driver IC — directly within the CS/Cybersecurity team's embedded programming competence.
4. **Macro-scaling neutralizes the primary kill factor.** At relaxed dimensions (>4 mm pitch), standard 5V push-pull solenoids (readily available from Indian suppliers at ₹30–80/unit) can be mounted without precision alignment. This directly addresses the Phase 3B finding that fabrication tolerance at ISO 17049 pitch is the dominant risk.
5. **High force output.** Even small 5V solenoids produce 50–200 gf, well above the 20–100 gf threshold for tactile legibility.
6. **Budget compliant.** Six solenoids + driver ICs + ESP32 + frame materials ≈ ₹1500–2500, comfortably within the ₹3000 preferred budget.

### Why Others Were Not Selected

| Candidate | Reason for Rejection |
|---|---|
| **Latching Solenoid** | Limited domestic availability. Requires H-bridge for bipolar pulses (added complexity). The zero-holding-power advantage is not critical for a benchtop prototype powered by an external supply. |
| **Custom Electromagnet** | Inconsistent force across hand-wound units undermines tactile consistency. Plunger sticking due to residual magnetism is a reliability risk. The educational value does not outweigh the reliability penalty. |
| **Servo + Cam** | Mechanically more complex (cam profile, follower, pivot points). Slower refresh rate (50–200 ms). Cam-follower wear over time. At macro scale, the solenoid's direct-drive simplicity is superior. |
| **SMA Wire** | High implementation risk. Slow cooling limits refresh rate. Complex PWM current control. Fatigue life uncertainty. The team's lack of analog electronics experience makes this particularly risky. |
| **Voice Coil** | Requires precision alignment of coil and magnet gap. Difficult to fabricate or source at low cost. Analog current control needed for position — overkill for binary Braille dots. |
| **Piezoelectric** | Directly contradicts the engineering hypothesis (lower-cost alternative). Cost-prohibitive. |

---

## 2.4 Mechanical Architecture Selection

### Selected: **Direct-Drive, Macro-Scaled, Modular Single-Cell with Self-Guiding Pins and Passive Spring Return**

### Decisions

| Aspect | Selection | Justification |
|---|---|---|
| **Motion Transmission** | Direct drive (solenoid plunger → pin base) | Fewest moving parts. No linkages, cams, or pivots to fabricate or wear out. |
| **Pin Guidance** | Self-guiding pins in 3D-printed cylindrical sleeves | Pins serve as their own guide shafts. Oversized holes (pin diameter + 0.3–0.5 mm clearance) accommodate 3D-printing tolerances. PTFE tubing liners if friction is excessive. |
| **Alignment Strategy** | Macro-scaled pitch (≥5 mm) with individual solenoid mounting pockets | Wide spacing eliminates inter-actuator interference. Each solenoid sits in a dedicated 3D-printed pocket, ensuring axial alignment with its pin. |
| **Reset Mechanism** | Passive compression spring above each pin | Off-the-shelf steel springs (₹1–5/unit). Predictable, reliable, zero-power reset. Placed above the pin cap, pushing downward. |
| **Structural Design** | Two-layer sandwich frame (3D-printed or laser-cut acrylic) | Bottom layer: solenoid mounting plate. Top layer: pin guide plate. Spacers separate the layers. Simple to fabricate and assemble. |

---

## 2.5 Control Architecture Selection

### Selected: **Centralized Single-MCU Control**

| Aspect | Selection | Justification |
|---|---|---|
| **Controller Organization** | Single ESP32 DevKit | All six dot drivers connect directly to GPIO pins. No inter-processor communication needed. Simplest firmware. ESP32 is the cross-portfolio standard (Phase 3B). |
| **Driver Organization** | ULN2003 Darlington array (or L293D) | One ULN2003 IC drives all six solenoids (7 channels available). Built-in flyback diodes. Logic-level input from ESP32 GPIO. Simplest wiring. |
| **Subsystem Partitioning** | MCU → Driver IC → Solenoids (three-tier) | Clean separation of logic, power amplification, and mechanical actuation. Each tier can be tested independently. |

---

## 2.6 Hardware Platform Selection

| Component | Recommendation | Justification | Alternatives Rejected |
|---|---|---|---|
| **MCU** | ESP32 DevKit V1 (₹450–550) | Dual-core, Wi-Fi/BT, 34 GPIO, Arduino IDE support, cross-portfolio standard. Overkill for 6 pins but provides expansion headroom. | Arduino Uno (fewer pins, no wireless, 8-bit); STM32 Blue Pill (steeper learning curve, less community support for beginners). |
| **Driver** | ULN2003A Darlington Array (₹30–60) | 7 channels, built-in flyback diodes, 500 mA/channel, logic-level compatible. Single IC drives all 6 solenoids. | L293D (unnecessary bidirectional capability, higher voltage drop); Discrete MOSFETs (more wiring, external diodes needed). |
| **Actuators** | 5V Miniature Push-Pull Solenoids × 6 (₹30–80 each) | Readily available, strong force, fast response. At macro scale, standard sizes (e.g., 10×20 mm) are suitable. | Servos (slower, mechanically complex); SMA (unreliable, complex control). |
| **Power** | 5V 2A USB Adapter or Power Bank (₹100–250) | Stable 5V supply. No battery management complexity. Sufficient current for 6 solenoids (estimated peak: ~1.2A). | LiPo battery (adds charging circuit complexity); 9V battery (insufficient current). |
| **Interface** | USB Serial (built into ESP32) | Zero additional hardware. Character input via serial monitor. | Bluetooth (adds firmware complexity for MVP); Physical buttons (unnecessary for validation). |

---

## 2.7 Manufacturing Strategy

| Aspect | Recommendation | Justification |
|---|---|---|
| **Fabrication Method** | FDM 3D printing (PLA/PETG) for frame + laser-cut acrylic for guide plate (optional) | 3D printing is the team's most accessible fabrication method. Acrylic laser cutting provides better dimensional accuracy for pin guide holes if available. |
| **Assembly Strategy** | Layered sandwich: bottom plate (solenoids) → spacers → top plate (pin guides) → pins + springs | Simple, tool-free assembly with M3 screws. Each layer can be fabricated and tested independently. |
| **Expected Tolerances** | ±0.3–0.5 mm (FDM); ±0.1 mm (laser-cut acrylic) | Macro-scaled design (≥5 mm pitch) is forgiving of FDM tolerances. Pin guide holes should be designed 0.3–0.5 mm oversized and post-drilled if needed. |
| **Serviceability** | Modular cartridge design: each solenoid+pin+spring unit can be individually removed and replaced | Faulty dots can be repaired without disassembling the entire cell. |
| **Repairability** | High. All components are off-the-shelf and individually replaceable. | No custom-fabricated parts that cannot be reprinted. |
| **Prototype Reproducibility** | Moderate. 3D-printed parts may vary between prints, but macro-scale tolerances are forgiving. | STL files can be shared for replication. |

---

## 2.8 Architecture Risk Assessment

| Risk | Severity | Mitigation |
|---|---|---|
| **Solenoid force insufficient at macro stroke** | Medium | Select solenoids with rated force >100 gf at the target stroke. Test single solenoid before building full cell. |
| **Pin binding in guides** | Medium | Oversize guide holes by 0.3–0.5 mm. Use PTFE tubing liners. Polish pin surfaces. Test each pin individually. |
| **Solenoid heat buildup** | Medium | Limit duty cycle (activate solenoids only during refresh, not continuously). Use momentary activation (pulse to raise, spring to lower). Ensure ventilation. |
| **ESP32 GPIO current limit** | Low | ULN2003 draws <1 mA per input from GPIO. Well within ESP32's 40 mA per pin limit. |
| **Power supply voltage sag under load** | Medium | Use a 5V 2A+ supply. Add bulk decoupling capacitors (100–470 µF) near solenoid power rail. Activate solenoids sequentially rather than simultaneously if sag occurs. |
| **3D-printed frame warping** | Low | Use PETG or annealed PLA. Design frame with adequate wall thickness (≥3 mm). Use flat build orientation. |
| **Tactile output not distinguishable** | Medium | Ensure pin protrusion ≥1 mm above surface. Use rounded pin tips. Test with sighted and (if possible) visually impaired users. |
| **Mechanical misalignment** | Low (at macro scale) | Macro pitch (≥5 mm) provides ample clearance. Individual solenoid mounting pockets ensure axial alignment. |

---

## 2.9 Architecture Decision Records (ADR)

### ADR-001: Macro-Scaled Mechanical Design

- **Decision:** Adopt macro-scaled Braille cell dimensions (≥5 mm dot pitch, ≥1.5 mm dot height) instead of ISO 17049 standard (2.34 mm pitch, 0.5 mm height).
- **Context:** Phase 3B unanimously identified fabrication tolerance at ISO 17049 pitch as the dominant kill factor. The team has no mechanical engineering background. Standard FDM 3D printing cannot reliably achieve 2.34 mm pitch with the required precision.
- **Alternatives Considered:** (a) ISO 17049 compliance with iterative fabrication; (b) External mechanical mentorship; (c) Macro-scaled simplification.
- **Selected Option:** (c) Macro-scaled simplification.
- **Reasoning:** Directly neutralizes the primary kill factor. The engineering hypothesis concerns actuation cost, not dimensional compliance. A macro-scaled cell still validates the core hypothesis convincingly.
- **Trade-offs Accepted:** Non-standard Braille dimensions. Output is not readable as standard Braille by touch (too large). The prototype demonstrates the actuation principle, not a usable reading device.
- **Engineering Consequences:** Larger frame. Standard 5V solenoids can be used without miniaturization. Assembly is straightforward.
- **Future Flexibility:** A future iteration with precision manufacturing (CNC, injection molding) could shrink the design to standard pitch using the same actuation principle.

### ADR-002: Solenoid Actuation

- **Decision:** Use non-latching 5V miniature push-pull solenoids with passive spring return.
- **Context:** The engineering hypothesis requires a lower-cost alternative to piezoelectric actuation. Multiple actuator families were evaluated.
- **Alternatives Considered:** Latching solenoid, custom electromagnet, servo+cam, SMA, voice coil.
- **Selected Option:** Non-latching solenoid.
- **Reasoning:** Highest maturity, fastest response, simplest control, adequate force, good availability. Macro scale eliminates the geometric packing constraint that makes solenoids challenging at standard pitch.
- **Trade-offs Accepted:** Continuous power required to hold pins up (mitigated by momentary activation strategy). Audible click. Heat generation under sustained use.
- **Engineering Consequences:** Simple driver circuit (ULN2003). Binary on/off firmware. Spring return ensures fail-safe pin retraction.
- **Future Flexibility:** Latching solenoids or SMA could replace non-latching solenoids in a future low-power iteration without changing the mechanical architecture.

### ADR-003: ESP32 Controller

- **Decision:** Use ESP32 DevKit V1 as the central controller.
- **Context:** The team has ESP32 experience. Phase 3B identified ESP32/STM32 as the cross-portfolio standard.
- **Alternatives Considered:** Arduino Uno/Nano, STM32 Blue Pill, Arduino Mega.
- **Selected Option:** ESP32 DevKit V1.
- **Reasoning:** Sufficient GPIO, integrated Wi-Fi/BT for future expansion, Arduino IDE compatibility, low cost, team familiarity.
- **Trade-offs Accepted:** Overkill for 6 GPIO outputs. Higher power consumption than STM32 in deep sleep (irrelevant for benchtop prototype).
- **Engineering Consequences:** Familiar development environment. Expansion headroom for multi-cell or wireless input.
- **Future Flexibility:** Wi-Fi/BT enables wireless Braille input in future iterations.

### ADR-004: ULN2003 Driver

- **Decision:** Use ULN2003A Darlington array IC for solenoid driving.
- **Context:** Six solenoids need to be driven from ESP32 GPIO pins. The driver must handle inductive loads.
- **Alternatives Considered:** L293D, discrete MOSFETs, DRV8833.
- **Selected Option:** ULN2003A.
- **Reasoning:** Single IC drives all 6 solenoids. Built-in flyback diodes. Logic-level compatible. Lowest wiring complexity. Cheapest option.
- **Trade-offs Accepted:** ~1V voltage drop across Darlington pair (solenoids receive ~4V from 5V supply — acceptable). 500 mA per channel limit (sufficient for miniature solenoids drawing 100–200 mA).
- **Engineering Consequences:** Simplest possible driver circuit. One IC, six wires to solenoids, six wires to ESP32.
- **Future Flexibility:** Can be replaced with MOSFET array for higher current if larger solenoids are used.

### ADR-005: External 5V Power Supply

- **Decision:** Use an external 5V 2A USB power adapter or power bank.
- **Context:** Six solenoids drawing ~100–200 mA each require up to 1.2A peak. The ESP32 requires ~240 mA.
- **Alternatives Considered:** LiPo battery, 9V battery, 12V adapter.
- **Selected Option:** 5V USB supply.
- **Reasoning:** Simplest. No battery management. Stable voltage. Ubiquitous (phone chargers).
- **Trade-offs Accepted:** Tethered operation. Not portable.
- **Engineering Consequences:** Single 5V rail powers everything. No voltage regulators needed (ESP32 DevKit has onboard 3.3V regulator).
- **Future Flexibility:** A LiPo + TP4056 module can be added for portable operation in a future iteration.

---

## 2.10 Architecture Confidence

| Aspect | Confidence | Basis |
|---|---|---|
| Actuation principle (solenoid) | **High** | Well-documented technology. Proven in commercial and DIY Braille projects. |
| Mechanical architecture (macro direct-drive) | **High** | Macro scaling eliminates the primary fabrication risk identified in Phase 3B. Direct drive minimizes complexity. |
| Control architecture (ESP32 + ULN2003) | **High** | Standard, well-documented combination. Team has ESP32 experience. |
| Tactile performance | **Moderate** | Force and stroke are theoretically sufficient, but subjective tactile quality requires empirical validation. |
| Budget compliance | **High** | Estimated BOM: ₹1500–2500. Well within ₹3000 preferred budget. |
| Timeline compliance | **High** | Simple architecture. No precision fabrication. Electronics are straightforward. 2 months is adequate. |
| Team capability alignment | **High** | Electrical and firmware work is within CS/Cybersecurity competence. Mechanical work is minimized by macro scaling. |

**Overall Architecture Confidence: HIGH**

---

---

# Part 3 — Final Architecture Definition & Prototype Blueprint

---

## 3.1 Final Architecture Overview

The OpenBraille prototype is a macro-scaled, single-cell (6-dot) refreshable Braille display driven by miniature electromagnetic solenoids. An ESP32 microcontroller receives character input via USB serial, maps it to a 6-dot Braille pattern, and activates the corresponding solenoids through a ULN2003 Darlington driver array. Each solenoid pushes a spring-loaded pin upward through a guide hole in the top plate. When the solenoid is de-energized, a compression spring returns the pin to its resting position.

The engineering hypothesis is validated by demonstrating that:
1. A low-cost electromagnetic actuation system (total BOM <₹3000) can produce refreshable Braille output.
2. The system can reliably raise and lower individual pins on command.
3. At least two distinct Braille characters can be displayed and refreshed.
4. The tactile output is distinguishable by touch.

The macro-scaled design (≥5 mm dot pitch) trades ISO 17049 dimensional compliance for manufacturability, directly neutralizing the primary fabrication-tolerance kill factor identified in Phase 3B.

---

## 3.2 Complete System Block Diagram
