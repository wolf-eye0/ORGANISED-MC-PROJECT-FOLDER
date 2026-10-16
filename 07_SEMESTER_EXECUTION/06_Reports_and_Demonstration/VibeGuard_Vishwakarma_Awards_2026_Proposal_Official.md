# VibeGuard: Ultra-Low-Cost Edge-Embedded Vibration Monitoring and Predictive Machine Diagnostics

**National Hardware Challenge:** Vishwakarma Awards 2026–27  
**Organized by:** Maker Bhavan Foundation  
**Host Institute & Thematic Track:** IIT Indore — Theme: *AI in Hardware & Manufacturing*  
**Official Sub-Themes:** *Predictive Maintenance & Machine Diagnostics* | *Edge AI & On-Chip Processing*  
**Submission Document:** Stage 1 Detailed Proposal Document (Official Compliance Baseline)  
**Submission Date:** 20 September 2026  

---

## Team & Institutional Identification

| Field | Details |
| :--- | :--- |
| **Team Name** | **Team AIGHT (VibeGuard)** |
| **Team Members** | 1. **Nihad P C** (Team Lead / Technical Integration & Evidence Lead)<br>2. **Sreehari K** (Firmware, Embedded DSP & Data Lead)<br>3. **Amith Krishna Das** (Hardware, Power, Rig & Safety Lead)<br>4. **Sreeprada K S** (Experimental Operations, Test & Inventory Coordinator)<br>5. **Archa Pramod** (Documentation, Communication & Demonstration Lead) |
| **Faculty Mentor** | **Ms. Sagna L T**, Assistant Professor, Department of Computer Science & Engineering |
| **Department / Program** | Department of Computer Science & Engineering |
| **Academic Affiliation** | APJ Abdul Kalam Technological University (KTU), Kerala, India |
| **Technical Domain** | Edge AI, Cyber-Physical Systems & Embedded IoT Hardware |
| **Target Unit Cost** | **Under ₹3,000 (~$35 USD)** Bill of Materials (BOM) |
| **Development Status** | **Bench-Validated Working Prototype Stage** |

---

## 1. Title of the Project / Product

**VibeGuard: Ultra-Low-Cost Edge-Embedded Vibration Monitoring and Predictive Machine Diagnostics System**

---

## 2. Problem Statement

> **“Unmonitored rotating machinery in small-scale industries and workshops suffers catastrophic mechanical breakdowns, costly production halts, and severe worker safety hazards due to the prohibitive cost (>₹50,000), network fragility, and complex installation of existing commercial vibration diagnostic systems.”**

### Context & Industry Impact
In modern manufacturing plants, machine health revolves around rotating mechanical equipment: induction motors, water pumps, blowers, gearboxes, and spindle drives. Mechanical unbalance, shaft misalignment, bearing raceway flaking, and structural looseness generate distinct periodic kinetic forces that scale with the square of rotational speed:
$$F_c = m \cdot r \cdot \omega^2$$
As speed $\omega$ increases, an off-center mass of only a few grams creates intense cyclical shear stress that degrades bearings and fatigues structural brackets.

Today, over 85% of Micro, Small, and Medium Enterprises (MSMEs) in India cannot afford proprietary condition monitoring suites (such as SKF @ptitude or Bently Nevada 3500), forcing operators into reactive maintenance—waiting until machines physically screech, overheat, or catastrophically seize. Furthermore, emerging IoT vibration pucks rely on continuous cloud streaming, which is brittle on noisy factory floors, vulnerable to RF interference, and introduces recurring SaaS subscription expenses that small industrial workshops flatly reject.

---

## 3. Solution Proposed

**VibeGuard** is an autonomous, ₹3,000 edge-native vibration condition monitor designed to bolt directly onto rotating machinery frames. It combines high-bandwidth MEMS sensing (Analog Devices ADXL345), dual-core 32-bit embedded digital signal processing (ESP32-WROOM-32E), deterministic ISO 10816-3 severity logic, and an interactive 3D WebGL Digital Twin—delivering laboratory-grade vibration intelligence with 100% air-gapped local execution.

### Key Technical Subsystems & Architecture

1. **High-Speed Synchronous SPI Sensing (800 Hz ODR):**  
   Employs an Analog Devices ADXL345 3-axis MEMS accelerometer communicating over dedicated 4-wire hardware SPI Mode 2 (`CPOL=1, CPHA=0`) at 1–2 MHz. Samples at 800 Hz Output Data Rate (ODR), delivering an un-aliased Nyquist bandwidth of 400 Hz that fully captures machine harmonics up to 40X rotational speed for standard 600–1200 RPM motors.
2. **Authentic Silicon Hardware Auditing:**  
   Firmware queries register `0x00` at cold boot and halts until the authentic Analog Devices silicon identifier `DEVID 0xE5` is validated, completely preventing execution against floating or damaged buses.
3. **In-Place Zero-Mean DC Elimination:**  
   Raw MEMS accelerometers inherently measure static 1.0g Earth gravity and mounting tilt. VibeGuard dynamically computes window mean acceleration across all three axes (X, Y, Z) and subtracts it in-place ($dx_i = x_i - \bar{x}$), isolating pure dynamic AC vibration oscillations without phase distortion or filter delay.
4. **Triaxial Euclidean Vector RMS Calculation:**  
   Computes the true geometric vibration energy across all 3 spatial axes every 128/256-sample window:
   $$V_{\text{RMS}} = \sqrt{\frac{1}{N} \sum_{i=0}^{N-1} \left(dx_i^2 + dy_i^2 + dz_i^2\right)}$$
5. **Impact Shock & Spall Extraction:**  
   Calculates Peak Acceleration ($a_{\text{peak}} = \max(|x_i|)$), Crest Factor ($\text{CF} = a_{\text{peak}} / a_{\text{RMS}}$), and 4th-Order Kurtosis (fourth statistical moment) to reliably flag impulsive bearing spalls and chipped gear teeth long before continuous RMS energy increases.
6. **Hann-Windowed Cooley-Tukey Radix-2 Real FFT:**  
   Pre-conditions vibration windows with a cosine Hann window ($w_n = 0.5 - 0.5\cos(2\pi n / (N-1))$) to eliminate spectral leakage, executing an optimized in-place 256/512-point FFT on the Xtensa DSP core in under 1.25 ms to isolate the 1X rotational unbalance peak (10.0 Hz at 600 RPM) and 2X/3X misalignment harmonics.
7. **Deterministic ISO 10816-3 Severity Decision Engine:**  
   Maps dynamic Vector RMS into international industrial machinery severity zones: Zone A/B Normal ($<0.35\text{g}$, Solid Green LED), Zone C Warning ($0.35\text{g}–0.70\text{g}$, Amber LED), and Zone D Alarm ($>0.70\text{g}$, Solid Red LED + Piezo Buzzer).
8. **K-out-of-M Persistence Debounce Filter:**  
   Requires qualifying abnormal vibration in $K=3$ out of $M=5$ consecutive analysis windows (1.6 seconds) before asserting Alarm state, completely rejecting nuisance false trips from accidental bench taps or dropped tools.
9. **Galvanically Isolated Electrical Architecture:**  
   Maintains complete galvanic isolation (open-circuit $\infty\ \Omega$) between the 12V 2A motor drive rail (protected by a 1A slow-blow fuse, SPST switch, and 1N4007 flyback suppression diode) and the sensitive 3.3V ESP32 logic rail (buffered with 100 µF low-ESR bulk electrolytic and 100 nF bypass ceramic capacitors to eliminate brownout resets).
10. **Dual Telemetry & WebGL 3D Digital Twin:**  
    Simultaneously outputs 115200 baud USB telemetry datagrams and synchronizes with a standalone, zero-dependency Three.js 3D WebGL Digital Twin featuring procedural CAD assembly, real-time 3-axis oscilloscope, FFT spectrogram, and 2D/3D Lissajous shaft centerline orbit plotters.

---

## 4. Implementation Plan

VibeGuard's deployment strategy is engineered for rapid, friction-free adoption across real-world operational environments without requiring plant downtime or specialized data science staff.

| Implementation Area | Strategic Execution & Operational Baseline |
| :--- | :--- |
| **Target Beneficiaries** | **1. MSME Machine Shops & Fabricators:** Small motor-driven lathes, CNC spindles, milling machines, and industrial air blowers that operate without dedicated maintenance teams.<br>**2. University Laboratories & Technical Institutes:** Precision mechanical testbeds, dynamometers, robotics benches, and student maker spaces requiring affordable condition monitoring tools.<br>**3. Agricultural & Rural Processing Units:** Flour mills, rice hullers, and irrigation pump sets where mechanical breakdown halts village-level economic livelihoods. |
| **Deployment Environment** | Direct inline magnetic or M3 rigid bolt mounting to motor bearing end-bells, pillow block bearings, and gearbox casings. Operates in electrically noisy industrial environments under 5V USB logic power, completely air-gapped from IT networks. |
| **Expected Outcomes** | • **Elimination of Unplanned Machine Stoppages:** Early warning at Zone C prevents unexpected bearing seizure.<br>• **90%+ Reduction in Monitoring Capital Cost:** Equipping 10 machines costs <₹30,000 total (the price of a single commercial sensor probe).<br>• **Zero Subscription Overhead:** No monthly cloud fees, API rate limits, or cellular SIM recurring costs. |
| **Phased Roadmap & Deliverables** | • **Phase 1 (Completed):** Component procurement, dual-trial vernier caliper audit, master circuit schematic, modular C++ DSP firmware, Wokwi WASM simulation, and 3D WebGL Digital Twin.<br>• **Phase 2 (Active / Weeks 1–4):** Acrylic baseplate drilling (1:1 sticker template), 3D printing of FAB-01 rotor arm and FAB-02 sensor bracket in college FabLab, full benchtop rig assembly.<br>• **Phase 3 (Weeks 5–8):** Multi-fault calibration baseline collection, ISO 10816-3 threshold tuning on 12V 600 RPM motor rig, session-split held-out validation.<br>• **Phase 4 (Weeks 9–12):** Field pilot testing in college engineering workshop, enclosure packaging, and final Vishwakarma Grand Finale demonstration. |

---

## 5. Safety and Efficiency Analysis

Industrial rotating equipment poses severe physical and electrical safety risks when operated unmonitored. VibeGuard is architected from the circuit level to physical plant enclosures with uncompromising safety and efficiency controls.

### Safety Engineering Highlights
1. **Galvanic Circuit Isolation:** The 12V 2A inductive motor circuit is completely separated from the 3.3V ESP32 microcontroller logic ground (measured open-circuit $\infty\ \Omega$). Inductive back-EMF flyback spikes are clamped by a dedicated reverse-biased 1N4007 power diode directly across the motor terminals, preventing voltage spikes from reaching the microcontroller or host computer.
2. **Inline Overcurrent & Inrush Protection:** A 5×20 mm inline screw-type fuse holder with a 1A 250V slow-blow cartridge fuse is wired into the positive 12V supply rail, protecting against rotor lockup or short circuits while absorbing inductive startup current inrush.
3. **Worker Hazard Prevention:** In high-speed spinning shafts, uncorrected dynamic unbalance generates destructive centrifugal shear forces that cause coupling bolts to shear, releasing high-velocity projectiles. VibeGuard's instantaneous ISO Zone D alarm and persistence engine trigger visual/audible alarms within <1.6 seconds, permitting safe, controlled operator shutdown.
4. **Rigid Anti-Vibration Baseplate Assembly:** The testbed utilizes an 8.80 mm dual-sheet acrylic stack (Plate 1: 4.20 mm, Plate 2: 4.60 mm) coupled with M3×20 mm Grade 8.8 hex bolts and DIN 985 Nyloc self-locking nuts (engaging 7.4 threads past the locking collar), ensuring zero bolt back-out during extended vibration runs.
5. **Brownout Immunity:** A 100 µF low-ESR bulk electrolytic capacitor in parallel with a 100 nF high-frequency ceramic bypass capacitor across 3.3V/GND buffers against voltage dips below the 2.70V ESP32 brownout threshold (`rst:0x10`).

### Operational Efficiency Gains
* **Reduction in Machine Downtime:** Detecting misalignment and unbalance weeks before mechanical failure allows maintenance to be scheduled during normal shift changeovers rather than halting critical production runs.
* **Energy Waste Mitigation:** Vibrating machines consume up to 8–15% more electrical energy due to frictional dissipation and eccentric loads. Aligning and balancing machinery via VibeGuard telemetry restores electrical efficiency.
* **Zero Bandwidth & Cloud Power Overhead:** Computing 800 Hz DSP locally on the dual-core Xtensa processor consumes <160 mA @ 3.3V (~0.5 Watts), avoiding continuous 500 mA Wi-Fi transmission bursts that congest industrial RF bands.

---

## 6. Scalability and Future Development

VibeGuard's modular hardware and software architecture provides an expansive development runway, scaling seamlessly from a single benchtop appliance to a plant-wide industrial telemetry mesh.

1. **TinyML On-Chip Anomaly Detection:** With the Level-1 RMS + persistence baseline frozen and proven, the secondary Xtensa core can host quantized Edge AI models (e.g., 1D Convolutional Autoencoders or One-Class SVMs via TensorFlow Lite for Microcontrollers) to classify specific defect signatures (bearing inner/outer race flaking BPFO/BPFI, gear mesh friction) without external servers.
2. **Multi-Drop RS-485 / Modbus RTU Industrial Bus:** Adding a low-cost MAX485 transceiver enables daisy-chaining up to 32 VibeGuard pods across a 1,200-meter industrial plant floor, streaming register telemetry directly into existing factory SCADA and PLC systems without cloud dependencies.
3. **ESP-NOW Ultra-Low-Latency Local Wireless Mesh:** For rotating assets where cabling is impractical, ESP-NOW peer-to-peer 2.4 GHz protocol enables battery-backed VibeGuard nodes to transmit 16-byte alert datagrams in <5 ms to a central shop-floor alarm console.
4. **Universal Asset Adaptability:** While demonstrated on an N20 geared plant, VibeGuard's configurable Output Data Rate (up to 3200 Hz) and dynamic g-range (up to $\pm 16\text{g}$) allow plug-and-play adaptation to heavy industrial centrifuges, slurry pumps, CNC machine tool spindles, and commercial HVAC fan banks.

---

## 7. Innovation Advantage

VibeGuard fundamentally disrupts the industrial predictive maintenance market by proving that high-integrity vibration analytics do not require multi-lakh instrumentation racks or recurring cloud SaaS subscriptions.

### Benchmark Comparison Matrix

| Feature / Capability | Traditional Industrial (SKF / Bently Nevada) | Generic IoT Cloud Pucks | VibeGuard (Our System) |
| :--- | :--- | :--- | :--- |
| **Hardware Unit Cost** | ₹1,50,000 – ₹5,00,000+ | ₹15,000 – ₹40,000 | **Under ₹3,000 (~$35 USD)** |
| **Recurring Subscription** | High Annual Support Contracts | ₹500 – ₹2,000 / month / node | **₹0 (100% Free & Open Edge)** |
| **Computing Location** | Central Server Rack / Engineering PC | Cloud AWS / Azure / IoT Core | **Zero-Latency On-Chip DSP** |
| **Network Dependency** | Heavy Coaxial / Industrial Ethernet | Continuous High-Bandwidth Wi-Fi | **Zero (Air-Gapped Autonomous)** |
| **Sampling Performance** | High-end 10 kHz+ Accelerometers | Low (often 50–100 Hz due to Wi-Fi) | **800 Hz Synchronous Hardware SPI** |
| **DC Gravity Rejection** | Analog High-Pass Filters | Cloud Post-Processing | **In-Place Dynamic Zero-Mean Vector** |
| **Real-Time Visualization**| Proprietary Desktop Software Suites | Web Graph Dashboard | **3D WebGL Digital Twin + Lissajous** |
| **False Alarm Protection**| Manual Engineering Review | Heuristic Thresholds | **K-out-of-M Persistence State Engine** |

---

## 8. Visual Impact & User Journey

### Operational Transformation Comparison

| Operational Phase | BEFORE VibeGuard (Reactive Maintenance) | AFTER VibeGuard (Continuous Edge Diagnostics) |
| :--- | :--- | :--- |
| **1. Daily Machine Startup** | Operator boots motor blindly; baseline vibration is completely unknown; no quantitative health ledger exists. | ESP32 boots in 0.5s, confirms authentic ADXL345 DEVID 0xE5, illuminates Solid Blue self-check, then turns Solid Green Normal. |
| **2. Normal Machine Running** | Subtle misalignment or looseness goes unnoticed by human ear; internal fatigue builds silently inside raceways. | 800 Hz SPI sampling continuously computes Vector RMS ($V_{\text{RMS}} \approx 0.017\text{g}$); live serial plot streams clean zero-mean oscillations. |
| **3. Fault Onset (Unbalance)** | Eccentric wear or loose bolt occurs; machine vibrates heavily; human operator cannot determine severity. | RMS crosses 0.35g into ISO Zone C Warning (Amber) $\rightarrow$ crosses 0.70g into Alarm (Solid Red LED + Buzzer); 3-of-5 persistence eliminates false alarms. |
| **4. Maintenance Action** | Operator runs machine until catastrophic seizure; coupling snaps, throwing debris; plant halts unexpectedly. | Operator receives immediate local visual/audible alert; checks 3D Digital Twin showing 10 Hz 1X unbalance peak; schedules 30-min balance fix. |
| **5. Financial & Safety Result** | ₹1,50,000+ repair bill, 3 weeks lost production, severe worker safety hazard. | Zero unplanned downtime, planned bolt retorquing/balancing, 100% worker safety, capital cost <₹3,000. |

---

### Visual Evidence & Engineering Assets

The proposal includes four high-resolution engineering visual representations:
* **Figure 1:** Detailed 6-stage embedded DSP and SPI signal processing pipeline (`slide 15 diagrm.png`).
* **Figure 2:** Master electrical schematic showing 3.3V Logic Domain A (ESP32, ADXL345 SPI, brownout capacitors, RGB telemetry), Isolated 12V Power Domain B (N20 motor, 1N4007 flyback suppression clamp across terminals, 1A fuse, KCD1 switch), and Master Wire Harness Matrix (`VibeGuard_Master_Circuit_Schematic.png`).
* **Figure 3:** User Journey Map & Operational Transformation storyboard illustrating reactive breakdown versus proactive edge diagnostics (`VibeGuard_User_Journey_Before_After.png`).
* **Figure 4:** Mechanical testbed engineering drawing sheet comprising 150×150 mm acrylic baseplate drilling blueprint, precision 3D CAD projections of FAB-01 eccentric rotor arm and FAB-02 rigid sensor L-bracket, and 6-point structural assembly/isolation protocol (`VibeGuard_Mechanical_Rig_Engineering_Assembly.png`).

---
*Certified Official Stage 1 Submission Proposal for Vishwakarma Awards 2026–27.*
