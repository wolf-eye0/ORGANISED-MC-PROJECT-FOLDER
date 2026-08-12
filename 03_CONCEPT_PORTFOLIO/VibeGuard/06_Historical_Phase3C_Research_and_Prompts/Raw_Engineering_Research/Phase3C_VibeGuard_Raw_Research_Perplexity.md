# Phase 3C Engineering Architecture and Prototype Strategy for VibeGuard

## 1. Executive Summary

VibeGuard aims to demonstrate that a low-cost, standalone embedded system can measure machine vibration locally, learn or recognize a normal operating condition, detect deliberately introduced abnormal vibration, classify states as Normal or Abnormal, and indicate the result on-device without cloud dependence. Phase 3B concluded that the engineering hypothesis is technically feasible for the assigned student team within a ₹3000–₹5000 budget and semester timeline, with single-node vibration discrimination identified as the hardest open problem. This Phase 3C report selects and justifies a concrete architecture centered on a single MEMS accelerometer, an ESP32-class MCU, time-domain and simple spectral features, and threshold/statistical decision logic, with optional TinyML as a stretch goal.[^1][^2][^3]

The recommended prototype uses a digital 3-axis MEMS accelerometer rigidly mounted on a small lab machine or rig, sampled at 1–5 kHz by an ESP32; vibration segments are processed into RMS, peak, standard deviation, and band-limited spectral energy, then classified by calibrated thresholds or a lightweight anomaly detector. The system operates entirely at the edge, logs basic data for debugging, and drives LEDs or a small display to indicate Normal/Abnormal. This architecture balances engineering validity, buildability by three CS/Cybersecurity-focused students, low mechanical complexity, and strong educational value while leaving room for future upgrades.[^4][^5]

***

## 2. Architecture Investigation

### 2.1 Candidate Architecture Classes

Phase 3A and 3B established that industrial condition monitoring commonly uses piezoelectric accelerometers, velocity sensors, and MEMS accelerometers for vibration measurement, with standards such as ISO 10816/20816 governing evaluation on non-rotating parts. Piezoelectric accelerometers offer very wide frequency range and long-term stability and are the de facto standard in high-end predictive maintenance, while MEMS accelerometers have matured enough to be used for condition monitoring in smaller machines.[^6][^7][^5][^4]

For VibeGuard’s student, low-cost, edge-intelligence context, the following architecture families are relevant:

- Single MEMS accelerometer + MCU (digital sensor, moderate bandwidth, simple wiring).
- Piezoelectric accelerometer + analog front-end + MCU (analog sensor, higher bandwidth, more complex electronics).[^4]
- Multi-sensor arrays (multiple accelerometers or mixed sensors on different machine locations).
- Hybrid systems combining analog front-end, digital sensors, and more advanced signal processing.

### 2.2 Comparative Assessment

Industrial piezoelectric accelerometers typically provide usable bandwidth up to 10–20 kHz and superior dynamic range and long-term stability, but require specialized signal conditioning (IEPE or 4–20 mA loops) and are relatively expensive. MEMS accelerometers for condition monitoring, by contrast, are lower-cost, can integrate directly with microcontrollers via SPI/I²C, and come in compact packages suitable for PCB-level integration, but trade off bandwidth and resolution, with typical usable ranges around 2–3 kHz for low-cost parts.[^8][^9][^10][^6][^4]

Multi-sensor architectures can help spatial noise isolation and fault localization but increase cost, mechanical complexity, cabling, and signal-processing burden beyond the project’s student scope and budget. Edge-AI-heavy architectures (dense neural networks, complex anomaly detection) similarly add computational and data-collection complexity that Phase 3B identified as unnecessary for minimum demonstrable success.[^5][^4]

Given VibeGuard’s mission—detect deliberately introduced abnormal vibration on an accessible lab machine rather than industrial turbines—the single-sensor MEMS+MCU architecture offers the best trade-off between feasibility, cost, and educational value.[^2][^3][^6]

***

## 3. Sensor Evaluation

### 3.1 Sensor Classes

Relevant sensor classes include:

- Piezoelectric accelerometers (PE) for high-frequency, high-dynamic-range monitoring.[^8][^4]
- Piezovelocity sensors with integrated velocity output tailored for low-frequency rotating machinery.[^11][^12]
- MEMS accelerometers (variable capacitance) for compact, low-cost vibration sensing.[^6][^4]
- Industrial loop-powered vibration sensors (4–20 mA) for direct PLC integration.[^9][^8]

### 3.2 Operating Principles and Characteristics

Piezoelectric accelerometers generate charge proportional to applied acceleration using PZT ceramics, offering wide temperature range, broad dynamic range, and bandwidth exceeding 10 kHz, with no DC response and minimal zero drift. MEMS variable-capacitance accelerometers measure acceleration via changes in capacitance of a seismic mass between capacitor plates and require integrated electronics to convert tiny capacitance changes to voltage or digital output; they offer lower bandwidth and sometimes higher noise but are cheaper and easier to integrate with embedded systems.[^5][^4][^6]

Industry white papers comparing PE and MEMS accelerometers conclude that PE sensors remain superior for high-end industrial predictive maintenance due to their wide frequency response and long-term stability, but MEMS devices are increasingly viable for condition monitoring where ultra-high bandwidth is not required and cost and integration simplicity matter.[^4][^6]

### 3.3 Comparative Table

| Attribute | Piezoelectric accelerometer | MEMS accelerometer |
|----------|-----------------------------|--------------------|
| Frequency response | Up to >10–20 kHz typical usable >10 kHz[^4][^8] | Usable bandwidth ~2–3 kHz for many VC MEMS designs[^4][^6] |
| Sensitivity & noise | High dynamic range, low noise, suitable for fine diagnostics[^4] | Higher noise, lower resolution, adequate for gross condition monitoring[^4][^6] |
| Long-term drift | Sensitivity drift only; no DC drift[^4] | Zero and sensitivity drift possible over time[^4] |
| Interface complexity | Requires constant-current IEPE or charge amps; analog cabling[^8][^4] | SPI/I²C digital or analog voltage, simple PCB-level integration[^6][^10] |
| Cost | Industrial-grade units often expensive relative to student budgets[^8][^13] | Commodity MEMS accelerometers inexpensive and widely available[^6][^10] |
| Mounting options | Stud/bolt mounting for robust coupling; heavier housings[^5][^14] | Small SMT or module designs; require careful mechanical mounting for good coupling[^6][^15] |

### 3.4 Recommended Sensors

**Technically strongest option:** An industrial piezoelectric accelerometer with appropriate frequency range, such as devices conforming to IEPE standards, would maximize sensing fidelity and best reflect industrial practice, but its cost and interface complexity exceed typical student project constraints.[^13][^8][^4]

**Practical student-project option:** A digital MEMS accelerometer (e.g., multi-axis SPI/I²C accelerometer modules used for condition monitoring) offers sufficient bandwidth to capture key fault-related vibration components for small motors and lab rigs and integrates directly with common MCUs, making it the preferred choice for VibeGuard’s minimum demonstrable prototype. This aligns with Phase 3B’s finding that ESP32- or STM32-class boards and commodity accelerometers are widely available and affordable for student teams.[^3][^10][^2][^6]

***

## 4. Embedded Platform Evaluation

### 4.1 Candidate Platforms

Phase 3B synthesis found that ESP32 and STM32-class microcontrollers appear as primary or viable platform choices across multiple concepts, including VibeGuard, thanks to their processing power, floating-point support, and peripheral richness. Other candidate platforms include Arduino-class ATmega boards, RP2040, and low-end STM32 variants; industrial discussions emphasize that embedded vibration analysis requires adequate CPU to perform FFTs or feature extraction at kHz sampling rates.[^2][^5][^4]

### 4.2 Comparative Factors

Key comparison axes include:

- Processing capability (clock speed, FPU availability) for time/frequency-domain processing.
- ADC or digital interface support (SPI/I²C) for sensors.
- Memory for buffering samples and computing features.
- Embedded ML support and libraries.
- Development ecosystem, debugging tools, and community support.
- Cost and board availability in India.

ESP32 offers dual-core tens-of-MHz to >200 MHz processing, integrated Wi-Fi/Bluetooth, and abundant RAM/flash, with strong Arduino/IDF ecosystems and good support for simple TinyML frameworks, making it well-suited for moderate-sophistication edge analytics. STM32 boards, particularly F4-series with FPU, similarly provide strong DSP capabilities and industrial-oriented peripherals but may involve steeper learning curves for students primarily experienced with Arduino-style development.[^3][^2][^5][^4]

Arduino-class ATmega boards have limited computational capacity and RAM, making real-time FFT or feature extraction at useful sampling rates more challenging, whereas RP2040 provides dual-core performance but slightly less mature vibration-analysis tooling.[^2]

### 4.3 Recommended Platform

**Primary architecture:** An ESP32 development board (e.g., widely available modules in India) is recommended as the main platform, combining adequate processing for time-domain statistics and basic FFT, simple sensor interfacing, strong community support, and reuse potential across other project concepts.[^3][^2]

**Alternative:** A mid-range STM32 (e.g., F4-series Nucleo board) is a viable alternative for teams preferring closer-to-industry tooling; however, for this CS/Cybersecurity-dominant student team, ESP32’s high-level development environment and familiarity offer an easier path to reliable implementation within the semester.

***

## 5. Signal Acquisition Architecture

### 5.1 Sampling Requirements

Industrial vibration condition monitoring typically aims for a frequency response 40–50 times the shaft RPM to capture relevant failure modes, implying sampling frequencies several kHz for typical lab motors. Honeywell’s condition monitoring guidelines indicate accelerometer ranges of 10 Hz–10 kHz for general rotating machinery, with key fault bands often below a few kHz.[^5][^4]

For VibeGuard’s minimum demonstrable prototype on small lab machines (e.g., fans, small motors), a sampling rate between 1 kHz and 5 kHz per axis is likely sufficient to detect changes in overall vibration magnitude and simple spectral patterns when an abnormal condition is deliberately introduced. Selecting a modest sampling rate reduces processing load and memory needs while preserving enough information for Normal/Abnormal discrimination.[^4][^5]

### 5.2 Anti-Aliasing and ADC Considerations

When using a digital MEMS accelerometer with an internal ADC and specified bandwidth, external anti-aliasing filters are generally unnecessary for a student-level prototype, provided the sensor is configured within its rated bandwidth and MCU-side sampling respects Nyquist criteria. For analog sensors, industrial practice recommends anti-aliasing filters before ADCs to prevent higher-frequency components from folding into the passband; this adds analog-design complexity that is avoidable with digital sensors.[^15][^6][^5][^4]

Given Phase 3B’s emphasis on keeping ADC choices simple and reserving high-resolution external ADCs for concepts such as TrueMoist, VibeGuard’s architecture will rely on the MEMS sensor’s internal ADC and digital interface rather than discrete external ADCs, minimizing hardware and debugging effort.[^2][^3]

### 5.3 Buffering and Timing Strategy

The MCU should acquire vibration data in fixed-length windows (e.g., 0.5–2 seconds per segment) using interrupt-driven sampling or sensor-driven data-ready signals, buffering data in RAM for feature extraction. For ESP32, a simple ring buffer per axis and timer/interrupt-based sampling or SPI burst reads provide sufficient timing stability; DMA is optional and can be reserved as an advanced optimization if needed.[^5]

***

## 6. Signal Processing Evaluation

### 6.1 Candidate Techniques

Condition monitoring literature and standards use a mix of time-domain and frequency-domain features, including RMS, peak, variance, standard deviation, crest factor, band-limited spectral energy, and FFT-based analysis. FFTs facilitate identification of dominant harmonics and sidebands associated with common faults such as imbalance or misalignment, while time-domain features often suffice for detecting gross changes in vibration magnitude.[^4][^5]

For a resource-constrained educational prototype, potential techniques include:

- Time-domain RMS and peak magnitude over windows.
- Standard deviation and variance as measures of overall vibration energy.
- Moving averages or exponential smoothing to track baseline.
- FFT or periodogram over modest window sizes (e.g., 256–1024 samples).
- Simple band-limited energy metrics (sum of spectral magnitudes in selected bands).

### 6.2 Comparative Assessment

RMS and peak measures are computationally cheap, robust, and widely used as overall vibration severity indicators tied to fatigue; they are easy to implement and interpret and align with ISO 10816’s velocity-based severity classes when converted appropriately. Standard deviation and variance similarly capture total vibration energy without requiring frequency-domain transforms, making them suitable for baseline vs abnormal discrimination.[^7][^5]

FFT-based frequency-domain analysis offers richer diagnostic insight but requires more computation and memory and careful windowing; still, for ESP32-level platforms, computing a modest FFT using integer or fixed-point libraries is feasible. Envelope analysis and more advanced spectral techniques are common in industry but unnecessary for minimum demonstrable success.[^5]

Given Phase 3B’s emphasis on keeping complexity appropriate and its identification of single-node isolation as the one genuinely hard open problem, VibeGuard’s prototype will adopt a primarily time-domain feature set (RMS, peak, standard deviation, possibly simple spectral energy) sufficient to detect deliberately introduced abnormal vibration on a controlled rig, with FFT as an optional extension if time permits.[^3][^2][^5]

***

## 7. Edge Intelligence Evaluation

### 7.1 Decision-Making Approaches

Common decision strategies for vibration monitoring include threshold-based classification (comparing features to calibrated limits), statistical anomaly detection (detecting deviations from baseline distributions), and lightweight machine-learning models such as decision trees or one-class anomaly detectors trained on normal data.[^4][^5]

Industrial practice often uses thresholds based on standards like ISO 10816 severity classes, with velocity or acceleration metrics categorized into ranges for machine classes. Academic work on edge anomaly detection explores simple clustering or one-class SVM on extracted features, but requires more training data and tuning.[^7][^5]

### 7.2 Comparative Assessment

Threshold-based classification is simple, explainable, and requires minimal data: the prototype can collect baseline segments under Normal operation, compute feature statistics, and set thresholds based on observed variance plus safety margins, then detect deliberate abnormal conditions when features exceed those thresholds. Statistical anomaly detection methods such as moving-mean and standard deviation bands offer similar simplicity and can be implemented without explicit training labels beyond Normal.[^5]

Lightweight TinyML approaches (small decision trees, one-class models) can add sophistication but increase implementation complexity, toolchain demands, and risk of overfitting given the limited dataset available in a student lab. Phase 3B noted that VibeGuard’s core engineering challenge is single-node noise isolation rather than model sophistication, so simpler decision logic aligned with the Engineering Design Review’s minimum success criteria is preferable.[^2][^3]

### 7.3 Recommended Strategy

The primary edge-intelligence strategy will be threshold-based classification on time-domain features, calibrated from Normal-operation measurements and validated against deliberately introduced Abnormal scenarios. A basic statistical anomaly detection layer (e.g., z-score or simple moving band rules) can be added to reduce false alarms and account for variability. TinyML (decision tree or simple anomaly detector trained via frameworks like TensorFlow Lite Micro) will be treated as an optional extension, developed only if core functionality is solid and remaining time permits.[^1][^2][^5]

***

## 8. Environmental Noise and False Alarm Analysis

### 8.1 Noise Sources

Honeywell and TE Connectivity highlight environmental and structural influences on vibration measurements, including nearby machine vibration, structural resonance, transient shocks, startup/shutdown behaviour, and mounting conditions. Mounting method (stud, adhesive, magnetic) significantly affects frequency response and sensor coupling, with poor mounting leading to distorted or attenuated signals.[^4][^5]

### 8.2 Single-Node Noise-Isolation Concept

Phase 3A and 3B identified VibeGuard’s defining innovation as single-node spatial/spectral noise isolation—distinguishing a target machine’s vibration signature from background or neighbouring machinery without an array of sensors. Industrial literature recognizes that accelerometers mounted on non-rotating parts can pick up vibration from multiple sources; spatial isolation is usually achieved with multiple sensors or careful placement.[^16][^2][^5]

For a student prototype, fully proving robust single-node isolation in a noisy industrial environment may be beyond scope, but the concept remains defensible and demonstrable in more controlled lab settings. The architecture can approximate noise isolation by:

- Mounting the sensor directly on the target machine with rigid coupling.
- Using controlled experiments where only the target machine’s operating condition changes while background remains fixed.
- Employing simple band-limited features if target-machine faults affect specific frequency bands more strongly than background.

### 8.3 False-Alarm Reduction Methods

Methods to reduce false alarms include:

- Averaging multiple windows before flagging an abnormal condition (persistence requirement).
- Ignoring transient spikes shorter than a defined duration.
- Using separate modes or thresholds for startup/shutdown vs steady-state.
- Ensuring consistent mounting and avoiding loose fixtures that introduce spurious vibration.

Given project constraints, VibeGuard will focus on demonstrating repeatable detection and classification in controlled scenarios and document environmental limitations, rather than claiming industrial-level false-alarm performance.[^3][^2][^5]

***

## 9. Mechanical Integration

### 9.1 Mounting Strategies

Condition monitoring guidelines emphasize that accelerometer mounting significantly affects measured vibration; stud or bolt mounting provides the best high-frequency coupling, while adhesive or magnetic mounts introduce resonance and may attenuate higher frequencies. For higher-frequency diagnostics, rigid mounting using threaded studs or firm adhesive is recommended.[^14][^5][^4]

For a student prototype on small machines, practical mounting options include:

- Bolt/stud mounting on a machined or drilled boss on the machine housing.
- High-strength adhesive on prepared flat surfaces.
- 3D-printed brackets firmly attached to the machine using screws.

### 9.2 Recommended Mechanical Integration

The preferred approach is to design a small 3D-printed bracket that:

- Holds the MEMS accelerometer PCB securely.
- Bolts to the machine housing using existing or student-drilled holes, providing rigid coupling.

This approach balances repeatability, ease of installation, and fabrication simplicity for the team, while providing adequate vibration transmission for the prototype’s frequency range. Adhesive-only mounting can be used for early lab tests but is less ideal for final demonstrations.[^5]

***

## 10. Electrical Architecture

### 10.1 Essential Interfaces and Circuits

An electrical architecture suitable for VibeGuard’s minimum demonstrable prototype includes:

- Sensor interface: SPI/I²C connection from ESP32 to the MEMS accelerometer, with proper supply decoupling.
- Power regulation: 5 V or 12 V input (e.g., from adapter), regulated down to 3.3 V for ESP32 and sensor using common regulator modules.
- Protection: Basic reverse-polarity protection and transient suppression (TVS) if necessary for lab safety.
- Status indicators: LEDs indicating power, Normal, Abnormal states; optional buzzer for alerts.
- Debug interface: USB/UART for firmware upload and logging.

Industrial sensors often use IEPE constant-current interfaces or 4–20 mA loops, but these are unnecessary for a student design using commodity MEMS modules. Signal conditioning beyond decoupling is minimal for digital sensors.[^9][^8]

### 10.2 Optional Display and Connectivity

An optional small OLED or LCD can show numeric feature values and current classification, enhancing educational value but not required for minimum success. Similarly, optional connectivity (Wi-Fi, Bluetooth) for streaming vibration data can be explored after core functionality is stable, but cloud processing is explicitly outside the minimum demonstrable scope.[^2]

***

## 11. Hardware Comparison and Selection

### 11.1 Candidate Sensor Modules

Available sensor modules suitable for student vibration projects include digital MEMS accelerometer boards based on chips designed for condition monitoring, as well as general-purpose accelerometers such as ADXL-type devices and more recent triaxial MEMS parts. Industrial MEMS vibration modules, like the 883M digital MEMS accelerometer or similar devices, are used in plant monitoring but may be more expensive; teaching labs often use cheaper general-purpose accelerometer breakout boards.[^10][^15][^6]

### 11.2 Candidate MCU Boards

ESP32 development boards are widely available at low cost, with integrated USB and programming support and strong community ecosystems; STM32-based Nucleo boards and Arduino-compatible boards are also common, but Phase 3B synthesis emphasized ESP32/STM32 as shared platform investments across concepts.[^3][^2]

### 11.3 Cost and Availability

Industrial catalogues show piezoelectric accelerometers and industrial vibration sensors at significantly higher price points than MEMS-based modules, reflecting their ruggedization and performance. By contrast, MEMS accelerometer breakout boards and ESP32 development boards are inexpensive and widely sold by electronics vendors and online retailers serving Indian markets, making it realistic to meet the ₹3000–₹5000 budget once sensor, MCU, power, indicators, and mechanical parts are included.[^13][^8][^9][^2][^3]

### 11.4 Recommended Hardware Set

The report therefore recommends:

- One digital triaxial MEMS accelerometer breakout board suitable for vibration monitoring.
- One ESP32 development board as the main MCU.
- Supporting components: power regulator module, LEDs, small buzzer (optional), wiring, connectors, and 3D-printed or simple fabricated bracket.

Fallback alternatives include using an STM32 Nucleo board if ESP32 is unavailable or a different MEMS accelerometer module of similar bandwidth if the preferred sensor cannot be sourced, provided the team validates its frequency response experimentally.

***

## 12. Cost and Manufacturability Assessment

### 12.1 Bill of Materials Considerations

Industrial piezoelectric accelerometers and velocity sensors demonstrate the wide range of possible costs depending on ruggedness and certifications; student-use MEMS sensors are orders of magnitude cheaper. Given typical prices for ESP32 boards and MEMS accelerometer modules in India, plus basic mechanical and electrical parts, a single-node VibeGuard prototype comfortably fits within the ₹3000–₹5000 budget envelope established in Phase 3B.[^8][^9][^2][^3][^4]

Assembly complexity is modest: soldering headers, connecting sensor breakout to MCU via jumper wires or simple PCBs, mounting the sensor bracket to the machine, and integrating indicators and power inputs. Fabrication requirements are limited to 3D printing or simple machining for brackets and basic hand tools.

### 12.2 Manufacturability and Reproducibility

Using commodity, off-the-shelf boards and sensors ensures reproducibility for future student teams, while avoiding specialized industrial components that may be difficult to source or overkill for educational prototypes. The architecture is designed so that one team can build and validate the prototype with standard lab equipment, and subsequent cohorts can replicate or iterate on the design.[^2][^3]

***

## 13. Engineering Trade-Off Analysis

### 13.1 Sensing Subsystem

- **Cost vs accuracy:** Piezoelectric accelerometers offer higher accuracy and bandwidth but at significantly higher cost and interface complexity; MEMS accelerometers sacrifice some performance but align with the budget and student capabilities. For VibeGuard’s educational goals, MEMS provides adequate fidelity.[^6][^4]
- **Complexity vs reliability:** Analog PE sensors require proper IEPE or 4–20 mA conditioning, adding complexity and potential failure points; digital MEMS modules simplify electronics and reduce wiring errors.[^9][^8]

### 13.2 Processing Subsystem

- **Computational load vs feature richness:** Time-domain RMS and simple statistics are cheap and robust; FFT and more advanced spectral features increase load but enable richer diagnostics. The selected pipeline prioritizes time-domain features with optional FFT, balancing reliability and learning opportunities.[^5]
- **Explainability vs sophistication:** Threshold-based logic is transparent and easy to debug; ML-based anomaly detection is more sophisticated but less explainable and likely unnecessary for the prototype’s minimum goals.[^3][^2]

### 13.3 Mechanical and Electrical Integration

- **Manufacturability vs performance:** Rigid stud/bracket mounting yields better vibration coupling but requires drilling or machining; adhesive mounting is simpler but may degrade high-frequency fidelity. The recommended bracket-based bolt mounting provides a good compromise within lab constraints.[^5]
- **Maintainability and scalability:** Using modular sensor and MCU boards makes maintenance and upgrades straightforward, and the architecture can scale to more sensors or features in future iterations without major redesign.

Overall, the selected architecture offers the best engineering balance for demonstrating VibeGuard’s hypothesis: it uses mature industrial principles (accelerometer-based vibration sensing, time-domain severity metrics) adapted to student-friendly hardware and complexity levels.

***

## 14. Prototype Implementation Strategy

### 14.1 Assembly Order

A practical build sequence that minimizes integration risk is:

1. **Power subsystem:** Assemble and test the power regulation and MCU board with indicators showing stable operation.
2. **Microcontroller bring-up:** Flash simple test firmware to confirm MCU boot, serial communication, and GPIO control.
3. **Sensor integration:** Connect the MEMS accelerometer breakout to the MCU and verify communication (e.g., reading static acceleration).
4. **Mechanical mounting:** Design and fabricate the bracket, then mount the sensor on the machine and verify stable readings.
5. **Raw vibration acquisition:** Implement streaming of sampled vibration data to serial or storage and validate basic signal quality during machine operation.
6. **Signal-processing features:** Add RMS, peak, and standard deviation computations over windows and verify numerical plausibility.
7. **Classification logic:** Implement threshold-based Normal/Abnormal decision and drive LEDs or buzzer accordingly.
8. **System refinement:** Tune thresholds, add optional FFT or anomaly-detection features, and refine mechanical mounting as needed.

### 14.2 Bring-Up Stages and Debugging

Each stage should have expected behaviour and success criteria (e.g., sensor outputs stable static acceleration when the machine is off; vibration features increase during abnormal conditions), with likely failure modes such as wiring errors, misconfigured sensor registers, or timing issues documented and addressed using serial logging and stepwise testing.[^5]

***

## 15. Prototype Validation Strategy and Test Scenarios

### 15.1 Validation Methodology

The prototype must demonstrate:

- A repeatable Normal operating condition with stable feature distributions.
- Deliberately introduced abnormal vibration (e.g., adding an imbalance or loosened fixture) producing statistically significant feature changes.
- Repeatable detection and classification of abnormal episodes as Abnormal.
- Acceptable false-alarm behaviour over multiple Normal runs.

Validation will use lab machines such as small motors, fans, or custom rigs, under controlled conditions that allow safe introduction of fault-like disturbances.

### 15.2 Example Scenarios

Realistic experimental scenarios include:

- **Balanced vs intentionally unbalanced rotating system:** Attach a small weight to a rotating disc to induce imbalance and observe increased vibration magnitude and possibly specific spectral peaks.[^5]
- **Loosened mechanical fixtures:** Gradually loosen a mounting bolt to increase mechanical play and vibration.
- **Induced resonance:** Vary machine speed to approach a resonance and observe increased vibration amplitude.
- **Repeatable mechanical disturbances:** Apply controlled taps or shocks to the machine housing to test transient behaviour and false-alarm handling.

Each scenario demonstrates aspects of the engineering hypothesis and is designed to be repeatable, safe, and educational.

***

## 16. Calibration and Debugging Strategy

### 16.1 Calibration Needs

Calibration is primarily needed for:

- Baseline Normal feature statistics (mean, variance) per machine and mounting configuration.
- Thresholds for classification, derived from baseline plus safety margins.

Industrial practice emphasizes calibration for accurate velocity or displacement measurements, but VibeGuard’s educational prototype focuses on relative changes and classification rather than absolute units. Simple, manual calibration procedures (collect Normal data, compute statistics) are sufficient and can be repeated if mounting or machine conditions change.[^7][^5]

### 16.2 Likely Engineering Issues and Debugging

Probable issues include poor sensor mounting leading to noisy or inconsistent readings, electrical noise from power supplies, unstable sampling due to timer misconfiguration, aliasing if sampling frequency is too low, and mis-set thresholds causing false positives/negatives. Debugging recommendations include inspecting raw time-series plots, checking sensor configuration registers, verifying sampling rates, and performing controlled baseline measurements to confirm feature stability before tuning thresholds.[^5]

***

## 17. Reliability and Team Implementation Assessment

### 17.1 Reliability Considerations

For lab-scale demonstrations, expected operating stability and repeatability are high if mounting and wiring are robust and code is tested under multiple scenarios; long-term drift and sensor durability issues are less critical but should be noted as limitations compared to industrial systems. Environmental sensitivity (temperature, nearby machines) should be documented as factors that may affect classification.[^4][^5]

### 17.2 Team Task Distribution

Given the team composition described in project documents—three stronger CS/Cybersecurity students, one beginner programmer, and two members focused on hardware and fabrication—the architecture supports the following allocation:[^2][^3]

- Experienced members: firmware design and implementation, signal-processing and classification algorithms, sensor integration, system-level debugging.
- Beginner programmer: tasks such as LED/display control, simple data logging, basic configuration modules, and contributing to testing scripts, under guidance.
- Other members: hardware sourcing, mechanical mounting design and fabrication, enclosure construction, assembly, documentation, and coordination with mechanical engineering labs.

This distribution maximizes project success and skill development while keeping critical embedded tasks with the most experienced students.

***

## 18. Procurement, Manufacturing, Risk and Readiness

### 18.1 Component Procurement and Manufacturing

Essential components (ESP32 board, MEMS accelerometer module, power supply, LEDs, wiring) are widely available from electronics suppliers and online marketplaces serving India. Optional components (display, buzzer, enclosures) can be procured as budget permits, and spare sensors or boards are advisable for risk mitigation.[^3][^2]

Manufacturing requirements include simple PCB or perfboard assembly, 3D-printed brackets or basic machined parts, and standard hand tools; no complex PCB fabrication or machining is mandatory.

### 18.2 Risk Assessment and Readiness

Major implementation risks include:

- Insufficient vibration coupling due to poor mounting.
- Single-node noise isolation proving weaker than desired in noisy environments.
- Overly aggressive or conservative thresholds causing misclassification.
- Schedule risk if extensive tuning or data collection is attempted late.

These risks are mitigated by early mechanical design and mounting tests, focusing validation on controlled lab rigs, prioritizing simple, explainable decision rules, and staging development so that basic sensing and classification are working well before optional features are attempted.[^2][^3][^5]

Phase 3B concluded that VibeGuard is highly feasible for the student team, with strong team-fit and budget alignment; the architecture defined here adheres to that feasibility picture and is ready to proceed into Phase 4 detailed design and prototype implementation.[^3][^2]

***

## 19. Phase 3C Memory Summary for VibeGuard

**Selected architecture:** Single-node vibration monitoring using a digital MEMS accelerometer rigidly mounted on a small lab machine, with local processing on an ESP32-class MCU performing time-domain feature extraction and threshold-based classification.[^6][^4][^2]

**Selected sensor:** Practical student choice is a triaxial MEMS accelerometer module with ~2–3 kHz usable bandwidth, SPI/I²C interface, and suitable resolution for condition monitoring; industrial piezoelectric accelerometers are acknowledged as stronger but not selected due to cost and complexity.[^6][^4]

**Selected MCU:** ESP32 development board as the primary platform, with STM32 as a viable alternative if needed.[^2]

**Processing approach:** Windowed sampling at 1–5 kHz, time-domain RMS, peak, standard deviation, and optional simple spectral energy or FFT for educational insight.[^5]

**Edge-intelligence strategy:** Threshold-based Normal/Abnormal classification calibrated from baseline Normal data, with optional statistical anomaly detection; TinyML considered an extension, not core.

**Electrical architecture:** Digital sensor interface via SPI/I²C, basic power regulation to 3.3 V, LEDs/buzzer for status, optional small display; minimal analog front-end due to digital sensor choice.[^8][^9]

**Mechanical integration:** Rigid bracket-mounted sensor on machine housing using bolts or screws; adhesive mounting used only for early experiments.[^5]

**Estimated cost:** Within ₹3000–₹5000 including MCU, sensor module, mechanical mounting, indicators, and miscellaneous parts, consistent with Phase 3B’s budget feasibility assessment.[^3][^2]

**Major engineering risks:** Single-node noise isolation robustness; mounting quality; threshold tuning; limited bandwidth of MEMS sensor relative to high-end PE sensors.[^4][^5]

**Unresolved questions:** Exact sensor model and its empirically validated frequency response; optimum sampling rate and window size; how well the single-node isolation concept holds in more complex vibration environments.

**Implementation priorities:** Early selection and characterization of the MEMS sensor; robust mechanical mounting; reliable acquisition and feature computation; simple, stable classification; progressive validation in controlled scenarios.

**Rationale:** The architecture uses mature industrial principles adapted to student-friendly hardware and complexity, validates the engineering hypothesis under lab conditions, fits the budget and team skills, and provides a strong foundation for future innovation in single-node isolation and edge intelligence.[^4][^2][^3]

---

## References

1. [Engineering_Design_Review.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/0553839b-c83a-42b8-a3a5-516a4944dccd/Engineering_Design_Review.md?AWSAccessKeyId=ASIA2F3EMEYES6QHR5Y6&Signature=e1teEaUZA6h6CdUxj2WMqttc3Bk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEGUaCXVzLWVhc3QtMSJGMEQCIEzHtHkxQ1t3DJehcfTDZkeWHAcUgmqDni2FvbewLStqAiAnyu4OCtH6K0e%2Brnek7S1fv3iTtXaqd0ASlnczEStoECrzBAguEAEaDDY5OTc1MzMwOTcwNSIMhSn8CJ%2FuTNJrt0YrKtAEtCcLcKsK5RtwPlTWie7w9Xhq%2F66iuzXWwXlQyEWoTvXM47NRmCDLHs5jHRLs%2Bjuokxo2KKQ9UxIUgXCKSQqMu%2BvLdF1rn%2BVFpwrOF9haJ%2FhwH9hLTA%2FWNeHn9js5F%2B0WHqAm4B4WrJ4dWWGunGJXAqsmloC2aIdgkgARAIuVpAAGPo5ErOvU5F%2FLafDKRcbjy81vtWLcANF2ybNOeU4Htrs%2BbUX3wBclo2I2m0oD5q9eFimwJ%2Ba1fG%2F5TxSGNjpFPXYkPefdoFwh9TC6HWdwlzLfhAtRn4nCnCSOlVo3jh9%2Fu1e1mxdjWCZlkKBch4dx63fYUp6Z5FZaxOBRmmZOUdVA06akU0ZqtQ40PMdn9fT%2FdFh7WdDREk4hXzcmKqAEwYTQHSMqA2IOIXWkFzJk0BqDOEPwkwFl9ZiJyNtFCMWiWwQrQPvaWdDE4OY4uPEIqggE7dSjgybltfTxCJ3GDLDDCIRNEhrZYjCx%2Fwro8L%2BuWNmivPTSs3bcJGkDTq%2BayMhsiDAKTHSzAD48vRRl7OKfUKJ7bXRKlffrIJKnRs3N%2FUw1ewyjIgCZSZH%2BmkVoH6gU5AiczUzudk3YFSjqKDNci2QcRn2S2JttHh1xDorJuI%2B%2Fs7%2FlnWE4uKqc71kmomrWkuqsLPKbljC8DMo04%2BNYfWK7I9DmWHNrXp6f56j8jlyBFBz0oepee5hfFdefaHbzEQeKkGBI0ZHvOj2zJJscNOzKra7hnkq1B18NHoFSIHXw1DrfBVJ%2FBoiLEx7lBxk43I%2BYEvu%2BmRqT4zUrGDDjpJbTBjqZAZUvkEXzmQ8t%2F2%2Ft4s6ZtKhbN0NksMWzFINSgyJiWF6cuePoY%2B%2BcuWiHOu4X4kWeUpH6q8HDxQaQaoU6E7zbcQOgbSslV3Xcc0L%2BNVyvFONH%2BiwmH5Mp9xHx32D1DJn1BWDTKHMfDM0cHYg%2BfBgwXqGvcrqSpYg2%2BaVGU9K6Mt9ve2xctw%2Bn1tny4P7br9GVOnT2dQjktvzzjQ%3D%3D&Expires=1785045046) - Phase 3B should determine - Which low-cost sensing technology provides the best foundation for adapt...

2. [Phase3B_Report_by_Claude.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/e11e8d60-1688-48c9-8129-36253ba89f18/Phase3B_Report_by_Claude.md?AWSAccessKeyId=ASIA2F3EMEYES6QHR5Y6&Signature=p%2BAdsh5E3lz6rzE7GMEjMKRaHdg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEGUaCXVzLWVhc3QtMSJGMEQCIEzHtHkxQ1t3DJehcfTDZkeWHAcUgmqDni2FvbewLStqAiAnyu4OCtH6K0e%2Brnek7S1fv3iTtXaqd0ASlnczEStoECrzBAguEAEaDDY5OTc1MzMwOTcwNSIMhSn8CJ%2FuTNJrt0YrKtAEtCcLcKsK5RtwPlTWie7w9Xhq%2F66iuzXWwXlQyEWoTvXM47NRmCDLHs5jHRLs%2Bjuokxo2KKQ9UxIUgXCKSQqMu%2BvLdF1rn%2BVFpwrOF9haJ%2FhwH9hLTA%2FWNeHn9js5F%2B0WHqAm4B4WrJ4dWWGunGJXAqsmloC2aIdgkgARAIuVpAAGPo5ErOvU5F%2FLafDKRcbjy81vtWLcANF2ybNOeU4Htrs%2BbUX3wBclo2I2m0oD5q9eFimwJ%2Ba1fG%2F5TxSGNjpFPXYkPefdoFwh9TC6HWdwlzLfhAtRn4nCnCSOlVo3jh9%2Fu1e1mxdjWCZlkKBch4dx63fYUp6Z5FZaxOBRmmZOUdVA06akU0ZqtQ40PMdn9fT%2FdFh7WdDREk4hXzcmKqAEwYTQHSMqA2IOIXWkFzJk0BqDOEPwkwFl9ZiJyNtFCMWiWwQrQPvaWdDE4OY4uPEIqggE7dSjgybltfTxCJ3GDLDDCIRNEhrZYjCx%2Fwro8L%2BuWNmivPTSs3bcJGkDTq%2BayMhsiDAKTHSzAD48vRRl7OKfUKJ7bXRKlffrIJKnRs3N%2FUw1ewyjIgCZSZH%2BmkVoH6gU5AiczUzudk3YFSjqKDNci2QcRn2S2JttHh1xDorJuI%2B%2Fs7%2FlnWE4uKqc71kmomrWkuqsLPKbljC8DMo04%2BNYfWK7I9DmWHNrXp6f56j8jlyBFBz0oepee5hfFdefaHbzEQeKkGBI0ZHvOj2zJJscNOzKra7hnkq1B18NHoFSIHXw1DrfBVJ%2FBoiLEx7lBxk43I%2BYEvu%2BmRqT4zUrGDDjpJbTBjqZAZUvkEXzmQ8t%2F2%2Ft4s6ZtKhbN0NksMWzFINSgyJiWF6cuePoY%2B%2BcuWiHOu4X4kWeUpH6q8HDxQaQaoU6E7zbcQOgbSslV3Xcc0L%2BNVyvFONH%2BiwmH5Mp9xHx32D1DJn1BWDTKHMfDM0cHYg%2BfBgwXqGvcrqSpYg2%2BaVGU9K6Mt9ve2xctw%2Bn1tny4P7br9GVOnT2dQjktvzzjQ%3D%3D&Expires=1785045046) - Prepared by Chief Engineering Review Board synthesis of four independent Phase 3B Deep Research pass...

3. [Phase3B_MEMORY.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/3c72c147-be84-4982-b35e-7f694f6d28d9/Phase3B_MEMORY.md?AWSAccessKeyId=ASIA2F3EMEYES6QHR5Y6&Signature=upEu%2BLSy3nYb2rs4KLaulcJ%2B8P8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEGUaCXVzLWVhc3QtMSJGMEQCIEzHtHkxQ1t3DJehcfTDZkeWHAcUgmqDni2FvbewLStqAiAnyu4OCtH6K0e%2Brnek7S1fv3iTtXaqd0ASlnczEStoECrzBAguEAEaDDY5OTc1MzMwOTcwNSIMhSn8CJ%2FuTNJrt0YrKtAEtCcLcKsK5RtwPlTWie7w9Xhq%2F66iuzXWwXlQyEWoTvXM47NRmCDLHs5jHRLs%2Bjuokxo2KKQ9UxIUgXCKSQqMu%2BvLdF1rn%2BVFpwrOF9haJ%2FhwH9hLTA%2FWNeHn9js5F%2B0WHqAm4B4WrJ4dWWGunGJXAqsmloC2aIdgkgARAIuVpAAGPo5ErOvU5F%2FLafDKRcbjy81vtWLcANF2ybNOeU4Htrs%2BbUX3wBclo2I2m0oD5q9eFimwJ%2Ba1fG%2F5TxSGNjpFPXYkPefdoFwh9TC6HWdwlzLfhAtRn4nCnCSOlVo3jh9%2Fu1e1mxdjWCZlkKBch4dx63fYUp6Z5FZaxOBRmmZOUdVA06akU0ZqtQ40PMdn9fT%2FdFh7WdDREk4hXzcmKqAEwYTQHSMqA2IOIXWkFzJk0BqDOEPwkwFl9ZiJyNtFCMWiWwQrQPvaWdDE4OY4uPEIqggE7dSjgybltfTxCJ3GDLDDCIRNEhrZYjCx%2Fwro8L%2BuWNmivPTSs3bcJGkDTq%2BayMhsiDAKTHSzAD48vRRl7OKfUKJ7bXRKlffrIJKnRs3N%2FUw1ewyjIgCZSZH%2BmkVoH6gU5AiczUzudk3YFSjqKDNci2QcRn2S2JttHh1xDorJuI%2B%2Fs7%2FlnWE4uKqc71kmomrWkuqsLPKbljC8DMo04%2BNYfWK7I9DmWHNrXp6f56j8jlyBFBz0oepee5hfFdefaHbzEQeKkGBI0ZHvOj2zJJscNOzKra7hnkq1B18NHoFSIHXw1DrfBVJ%2FBoiLEx7lBxk43I%2BYEvu%2BmRqT4zUrGDDjpJbTBjqZAZUvkEXzmQ8t%2F2%2Ft4s6ZtKhbN0NksMWzFINSgyJiWF6cuePoY%2B%2BcuWiHOu4X4kWeUpH6q8HDxQaQaoU6E7zbcQOgbSslV3Xcc0L%2BNVyvFONH%2BiwmH5Mp9xHx32D1DJn1BWDTKHMfDM0cHYg%2BfBgwXqGvcrqSpYg2%2BaVGU9K6Mt9ve2xctw%2Bn1tny4P7br9GVOnT2dQjktvzzjQ%3D%3D&Expires=1785045046) - Version 1.0 Status COMPLETE Methodology Version Phase 3B --- TITLE Project mC - Phase 3B Memory - En...

4. [[PDF] Predictive Maintenance with Vibration Sensors | TE Connectivity](https://www.te.com/content/dam/te-com/documents/sensors/global/vibration-condition-monitoring-whitepaper.pdf)

5. [Introduction to Vibration Based Condition Monitoring](https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/hps/products/pmc/field-instruments/honeywell-versatilis-transmitter/hon-ia-pmc-introduction-to-vibration-based-condition-monitoring.pdf) - ISO 10816-1 is a document that sets out guidelines for the measurement and evaluation of mechanical ...

6. [MEMS Vibration Monitoring: From Acceleration to Velocity](https://www.analog.com/en/resources/analog-dialogue/articles/mems-vibration-monitoring-acceleration-to-velocity.html) - MEMS accelerometers have finally reached a point where they are able to measure vibration on a broad...

7. [ISO 10816-3:2009](https://www.iso.org/standard/50528.html) - Mechanical vibration — Evaluation of machine vibration by measurements on non-rotating parts — Part ...

8. [[PDF] CATALOG 2014](http://5.imimg.com/data5/SELLER/Doc/2026/4/597201462/FW/TL/OK/53842997/bently-nevada-vibration-sensors.pdf)

9. [Contact type Vibration Sensors](https://www.masibus.com/vibration-monitoring/vibration-sensors/contact-type-vibration-sensors/) - [vc_row full_width=stretch_row bg_type=image parallax_style=vcpb-default bg_image_new=id^10151|url^/...

10. [Digital triaxial MEMS accelerometer for precise industrial condition-based maintenance](https://www.electropages.com/2025/08/digital-triaxial-mems-accelerometer-precise-industrial-condition-based-maintenance) - Latest News from the Electronics Industry - Electropages

11. [Industrial vibration sensor selection: Piezovelocity transducers](https://rotorlab.tamu.edu/me459/sensors/Industrial%20velocity%20sensors.pdf)

12. [Piëzoelectric Velocity Vibration Sensors (VE + PV Series) - Istec](https://www.istec.com/product/piezoelectric-velocity-vibration-sensors/) - Meggitt VE and PV series sensors provide low-frequency vibration monitoring for turbines, with versa...

13. [Fluke 3563 Analysis Vibration Sensor system](https://www.fluke.com/en/product/condition-monitoring/vibration/3563) - The Fluke 3563 uses a high-frequency piezoelectric sensor & software to enable continuous vibration ...

14. [Acceleration sensors detect the "machine's health"](https://www.ifm.com/au/en/shared/productnews/2017/sps/new-accelerometers-for-your-machine-health) - Piezoelectric acceleration sensor with IEPE interface, robust housing and wide measuring range offer...

15. [883M Digital MEMS Accelerometer and Temperature Sensor](https://www.althensensors.com/sensors/acceleration-sensors/multi-axis-accelerometers/883m-digital-mems-accelerometer-and-temperature-sensor/) - The 883M was developed for condition monitoring applications. It is used in plant and process monito...

16. [Claudes-report-on-the-research-Phases-3a.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/ec6aa977-a87f-4525-92fe-eac92716ce57/Claudes-report-on-the-research-Phases-3a.pdf?AWSAccessKeyId=ASIA2F3EMEYES6QHR5Y6&Signature=oWIEHAcq5h3A2fdtphXVgUnux5Q%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEGUaCXVzLWVhc3QtMSJGMEQCIEzHtHkxQ1t3DJehcfTDZkeWHAcUgmqDni2FvbewLStqAiAnyu4OCtH6K0e%2Brnek7S1fv3iTtXaqd0ASlnczEStoECrzBAguEAEaDDY5OTc1MzMwOTcwNSIMhSn8CJ%2FuTNJrt0YrKtAEtCcLcKsK5RtwPlTWie7w9Xhq%2F66iuzXWwXlQyEWoTvXM47NRmCDLHs5jHRLs%2Bjuokxo2KKQ9UxIUgXCKSQqMu%2BvLdF1rn%2BVFpwrOF9haJ%2FhwH9hLTA%2FWNeHn9js5F%2B0WHqAm4B4WrJ4dWWGunGJXAqsmloC2aIdgkgARAIuVpAAGPo5ErOvU5F%2FLafDKRcbjy81vtWLcANF2ybNOeU4Htrs%2BbUX3wBclo2I2m0oD5q9eFimwJ%2Ba1fG%2F5TxSGNjpFPXYkPefdoFwh9TC6HWdwlzLfhAtRn4nCnCSOlVo3jh9%2Fu1e1mxdjWCZlkKBch4dx63fYUp6Z5FZaxOBRmmZOUdVA06akU0ZqtQ40PMdn9fT%2FdFh7WdDREk4hXzcmKqAEwYTQHSMqA2IOIXWkFzJk0BqDOEPwkwFl9ZiJyNtFCMWiWwQrQPvaWdDE4OY4uPEIqggE7dSjgybltfTxCJ3GDLDDCIRNEhrZYjCx%2Fwro8L%2BuWNmivPTSs3bcJGkDTq%2BayMhsiDAKTHSzAD48vRRl7OKfUKJ7bXRKlffrIJKnRs3N%2FUw1ewyjIgCZSZH%2BmkVoH6gU5AiczUzudk3YFSjqKDNci2QcRn2S2JttHh1xDorJuI%2B%2Fs7%2FlnWE4uKqc71kmomrWkuqsLPKbljC8DMo04%2BNYfWK7I9DmWHNrXp6f56j8jlyBFBz0oepee5hfFdefaHbzEQeKkGBI0ZHvOj2zJJscNOzKra7hnkq1B18NHoFSIHXw1DrfBVJ%2FBoiLEx7lBxk43I%2BYEvu%2BmRqT4zUrGDDjpJbTBjqZAZUvkEXzmQ8t%2F2%2Ft4s6ZtKhbN0NksMWzFINSgyJiWF6cuePoY%2B%2BcuWiHOu4X4kWeUpH6q8HDxQaQaoU6E7zbcQOgbSslV3Xcc0L%2BNVyvFONH%2BiwmH5Mp9xHx32D1DJn1BWDTKHMfDM0cHYg%2BfBgwXqGvcrqSpYg2%2BaVGU9K6Mt9ve2xctw%2Bn1tny4P7br9GVOnT2dQjktvzzjQ%3D%3D&Expires=1785045046) - page-1 Phase 3A Engineering Landscape AssessmentPatent-Oriented Embedded Systems Innovation Pipeline...

