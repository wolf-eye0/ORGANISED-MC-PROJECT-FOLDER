# Source Extraction

- Chapter: `03` — Portfolio Evolution and Concept Origins
- Authority tier: `TIER_4`
- Manual treatment: `HISTORICAL_SUPPORT`
- Original source: `03_CONCEPT_PORTFOLIO/VibeGuard/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_VibeGuard_Raw_Research_Gemini.docx`
- SHA-256: `39a249ed0b0c9d76b0372e558b04d47a837b6a1849848f84fa9bf88f1ade0921`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

Phase 3C Engineering Architecture Report: VibeGuard

1. Executive Summary

The VibeGuard project represents a localized embedded intelligence paradigm designed for the predictive maintenance of industrial machinery, operating under stringent constraints of cost, edge-based computational capacity, and educational prototype feasibility. The central engineering hypothesis postulates that an affordable, resource-constrained edge device can successfully capture real-time vibrational telemetry and autonomously discern standard operational harmonic baselines from deliberately introduced mechanical anomalies.1 The primary objective is to achieve highly reliable passive detection and alert generation without resorting to continuous cloud connectivity, heavy enterprise monitoring infrastructure, or active vibration cancellation mechanisms.1

Following an exhaustive evaluation of candidate hardware and algorithmic architectures, this report recommends a hybridized digital signal processing (DSP) and lightweight statistical machine learning architecture. The system utilizes the ESP32 embedded microcontroller paired with the ADXL345 digital Micro-Electro-Mechanical Systems (MEMS) accelerometer.2 To ensure phase-accurate data acquisition, the sensor interfaces over a high-speed Serial Peripheral Interface (SPI) bus, leveraged by Direct Memory Access (DMA) controllers to eliminate sampling jitter.3

The signal processing pipeline will rely on the KISS FFT algorithm to transpose time-domain measurements into frequency-domain spectra, isolating structural resonances and mechanical fault harmonics up to a 1600 Hz Nyquist limit.5 Rather than attempting computationally prohibitive Blind Source Separation (BSS) algorithms to filter ambient factory noise 7, the edge intelligence pipeline will employ a baseline spectral subtraction technique coupled with a one-class statistical anomaly detection framework.1

This proposed architecture can be realistically assembled, programmed, and validated by the designated five-member student team. Extensive cost estimates place the prototype Bill of Materials (BOM) strictly under ₹2,000 INR, well within the ₹3,000–₹5,000 INR project ceiling.1 The analysis concludes that the VibeGuard engineering hypothesis is entirely demonstrable using this configuration. Consequently, this report assigns an overall implementation readiness classification of READY WITH MINOR REFINEMENTS, marking the architecture safe for progression into Phase 4 detailed design and implementation.

2. Architecture Investigation

The fundamental engineering problem demands the early detection of abnormal machine vibration patterns within an environment where ambient noise, structural resonances, and neighboring machinery introduce significant signal cross-talk.1 To address this challenge, multiple architectural approaches were rigorously evaluated against the Phase 3B constraints.

Candidate System Architectures

The commercial and academic predictive maintenance landscape offers several approaches for vibration analysis. The multi-sensor array architecture represents the enterprise standard. In this paradigm, spatially distributed sensor arrays are placed across various bearing housings and motor chassis to triangulate fault signatures and perform advanced cross-channel coherence analysis. While this approach provides unparalleled diagnostic fidelity, it inherently violates the VibeGuard project’s low-cost constraint and introduces severe synchronization complexities across multiple independent nodes.1

A secondary architecture identified in early theoretical phases involved active vibration cancellation (AVC). A minority of prior theoretical models erroneously framed VibeGuard as a system requiring actuators, such as heavy voice-coils or piezoelectric stack actuators, to generate anti-phase mechanical interference to physically cancel out the anomalous vibration.1 This approach fundamentally misaligns with the Engineering Design Review (EDR), which explicitly defines VibeGuard as a passive detection and alerting system.1 Attempting mechanical cancellation on industrial machinery via a ₹5,000 INR prototype is thermodynamically and practically unfeasible.

The single-node passive edge-intelligence architecture is the recommended approach. This architecture relies on a singular, standalone edge computing node mounted directly to the target machine housing.1 By executing all high-frequency data acquisition and algorithmic inference locally on the embedded microcontroller, the system entirely bypasses the latency, bandwidth costs, and network reliability issues associated with continuous cloud telemetry.1 The fundamental engineering trade-off for utilizing a single node is the complete reliance on algorithmic signal processing to isolate the target machine’s baseline from adjacent spatial noise.1 The architecture must therefore aggressively prioritize real-time deterministic processing capabilities to compensate for the lack of spatial resolution.

Architecture Trade-Off Analysis

Architecture Type

Implementation Cost

Computational Load

Diagnostic Fidelity

Alignment with EDR Objectives

Multi-Sensor Array

Extremely High

High (Requires synchronization)

Excellent

Poor (Violates budget and simplicity constraints)

Active Cancellation (AVC)

Prohibitive

Extreme (Requires microsecond real-time control)

N/A (Intervention, not diagnostics)

Rejected (Violates passive detection constraint) 1

Cloud-Tethered Node

Low Initial, High Recurring

Low (Offloaded to cloud)

Good

Poor (Violates edge-intelligence constraint) 1

Single-Node Edge Intelligence

Very Low

Moderate to High

Moderate (Requires advanced DSP)

Excellent (Fulfills all EDR constraints) 1

The single-node edge intelligence architecture presents the optimal balance. By constraining the hardware to a single measurement point, the BOM cost drops dramatically, ensuring the project remains within the ₹3000 to ₹5000 INR threshold. The computational complexity shifts from managing network stacks to executing localized digital signal processing, which aligns perfectly with the computer science expertise of the intended implementation team.

3. Sensor Evaluation

Vibration monitoring relies fundamentally on the mechanical and electrical fidelity of the transducer. The selected sensor must possess the dynamic range and bandwidth necessary to capture high-frequency transients indicative of incipient mechanical wear without overwhelming the strictly constrained project budget.

Investigated Sensor Technologies

The engineering investigation analyzed multiple classes of vibration transducers, ranging from simple digital switches to industrial-grade piezoelectric accelerometers.

The ADXL1002 and IIS3DWB represent high-frequency MEMS accelerometers designed specifically for industrial predictive maintenance. Operating with a bandwidth from DC up to 21 kHz, these sensors can detect the earliest stages of microscopic bearing spallation and gear mesh anomalies.10 However, their ultra-low noise density comes at a severe financial cost. Current market analysis indicates that a single ADXL1002 integrated circuit costs between ₹5,500 and ₹7,900 INR.11 A fully populated evaluation board exceeds ₹10,000 INR.13 This technology instantly breaches the entire project budget before a microcontroller, power supply, or enclosure is considered, rendering it impractical for the student prototype.

Piezoelectric shock sensors, such as the ubiquitous SW-420 module, were also evaluated. These sensors rely on a spring-mass mechanism that briefly breaks an electrical contact during physical impacts, outputting a binary digital signal via an onboard LM393 comparator.14 While exceedingly affordable at approximately ₹37 to ₹63 INR 14, they operate merely as physical threshold switches. They cannot output the continuous time-domain analog or digital waveforms required for Fast Fourier Transform (FFT) analysis or advanced statistical baselining.16 Consequently, they fail to satisfy the requirement for nuanced abnormal vibration detection.

The MPU6050 is a six-degree-of-freedom (6-DoF) Inertial Measurement Unit (IMU) combining a 3-axis accelerometer and a 3-axis gyroscope. It is heavily utilized in educational robotics and is highly affordable, priced between ₹110 and ₹380 INR.17 However, the inclusion of a gyroscope introduces a significant vulnerability; gyroscopic micro-electromechanical structures are inherently sensitive to electromagnetic interference (EMI).19 Given that VibeGuard will be deployed near AC induction motors and industrial switching loads, EMI susceptibility poses a severe risk to signal integrity. Furthermore, the MPU6050's hardware low-pass filter constraints make it less suitable for capturing high-frequency rotational vibration compared to dedicated pure accelerometers.16

The ADXL345 is a 3-axis digital MEMS accelerometer utilizing differential capacitance across microscopic polysilicon springs.3 When subjected to acceleration, the proof mass deflects, altering the capacitance and generating a digital readout via an internal 13-bit analog-to-digital converter (ADC).3 It offers a selectable output data rate (ODR) spanning from 0.1 Hz to 3200 Hz.3 According to the Nyquist-Shannon sampling theorem, a continuous 3200 Hz sampling rate permits the accurate mathematical reconstruction of physical vibration frequencies up to 1600 Hz.6 This bandwidth is more than sufficient to capture fundamental machine rotational frequencies, which typically range from 10 Hz to 60 Hz for standard industrial motors, as well as the primary bearing defect harmonics such as Ball Pass Frequency Outer (BPFO) and Ball Pass Frequency Inner (BPFI).16

Justification for Selected Sensor

Sensor Model

Operating Principle

Bandwidth / Output Rate

EMI Susceptibility

Estimated Cost (INR)

Recommendation Status

ADXL1002

High-Frequency MEMS

21 kHz

Low

₹5,500 - ₹7,900

Eliminated (Exceeds budget constraint) 11

MPU6050

6-DoF MEMS (Accel + Gyro)

Max ~260 Hz LPF

High (Gyroscope)

₹110 - ₹380

Eliminated (EMI risk, low bandwidth) 16

SW-420

Mechanical Piezo Switch

N/A (Binary Threshold)

Low

₹37 - ₹63

Eliminated (Insufficient data fidelity) 14

ADXL345

3-Axis Digital MEMS

Up to 3200 Hz ODR

Low

₹130 - ₹350

Selected (Optimal cost/performance ratio) 3

The ADXL345 is formally recommended as both the technically strongest feasible option and the most practical student-project component. At a market price of approximately ₹130 to ₹350 INR 17, it consumes less than 10% of the project budget. Its 13-bit resolution yields a sensitivity of 3.9 mg/LSB when configured in the  measurement range, providing sufficient granularity to detect microscopic shifts in mechanical balance.3 Crucially, it outputs data via I²C or SPI interfaces, completely removing the need to design complex external analog front-end amplification and filtering circuitry.3

4. Embedded Platform Evaluation

To successfully process the dense time-domain telemetry streaming from the ADXL345 into actionable condition alerts, a highly capable embedded edge processor is required. The processing architecture must support rapid hardware interrupt handling, accelerated floating-point mathematics, and sufficient Static Random-Access Memory (SRAM) for batch signal processing operations.

Investigated Processing Platforms

The traditional Arduino Uno (ATmega328P) represents the baseline for educational embedded systems. However, its 8-bit architecture, 16 MHz clock speed, and restrictive 2 KB of SRAM instantly disqualify it for real-time spectral analysis. The FFT algorithm requires contiguous arrays of floating-point numbers; a modest 1024-point FFT would easily exceed the total available memory of an 8-bit Arduino, causing stack overflows and system crashes.

The Raspberry Pi Pico, powered by the RP2040 microcontroller, offers a massive upgrade. It features a dual-core ARM Cortex-M0+ processor running at 133 MHz and contains 264 KB of SRAM.23 The RP2040 excels in deterministic input/output operations via its unique Programmable I/O (PIO) state machines, which can perfectly time sensor reads without CPU intervention.24 It is extremely affordable at approximately ₹325 to ₹400 INR.23 However, the RP2040 possesses a critical weakness for the VibeGuard application: it lacks a hardware Floating-Point Unit (FPU). Emulating complex floating-point mathematics in software incurs heavy clock-cycle penalties, severely restricting the size and execution speed of the FFT that can be processed in real-time.

The STM32F411, commonly available in the "Black Pill" development board format, is a formidable industrial microcontroller. It features a 100 MHz ARM Cortex-M4 processor equipped with a single-precision hardware FPU and robust Direct Memory Access (DMA) capabilities.26 At a price of approximately ₹275 INR, it is highly cost-effective.27 Nevertheless, the development curve for bare-metal ARM Cortex-M4 programming, specifically configuring advanced DMA streams and nested vectored interrupt controllers (NVIC), presents a significant pedagogical hurdle for a student team predominantly experienced in higher-level computer science languages rather than bare-metal register manipulation.28

The ESP32 (NodeMCU / DevKit variants) utilizes a dual-core Xtensa LX6 microprocessor running at a blistering 240 MHz.16 It contains 520 KB of SRAM and features a highly capable single-precision FPU.2 The ESP32 provides native support for FreeRTOS, a real-time operating system that inherently supports multi-threading. This allows the computational load to be split; Core 0 can manage background system tasks, while Core 1 is entirely dedicated to deterministic DSP and anomaly detection.16 Furthermore, the ESP32’s SPI master driver supports advanced DMA block transfers, allowing the processor to seamlessly ingest sensor data in the background without CPU intervention.4 Costing between ₹300 and ₹400 INR in India, the ESP32 aligns perfectly with the budget constraints.2

Justification for Selected Embedded Platform

Microcontroller Platform

Clock Speed & Architecture

FPU Support

Memory (SRAM)

Advanced Features

Estimated Cost (INR)

ATmega328P (Uno)

16 MHz (8-bit)

No

2 KB

None

₹400 - ₹600

RP2040 (Pi Pico)

133 MHz (Dual Cortex-M0+)

No (Software Only)

264 KB

PIO State Machines

₹325 - ₹400 23

STM32F411 (Black Pill)

100 MHz (Cortex-M4)

Yes (Hardware FPU)

128 KB

DMA Controller

₹275 27

ESP32 (DevKitC)

240 MHz (Dual Xtensa LX6)

Yes (Hardware FPU)

520 KB

FreeRTOS, DMA, Wi-Fi

₹300 - ₹400 29

The ESP32 is the recommended processing platform. The presence of a hardware FPU significantly accelerates the complex trigonometric calculations required by the FFT algorithm.30 The massive 520 KB SRAM buffer allows for large windowed samples, increasing the frequency resolution of the vibration spectrum. The active community support and robust availability of C++ libraries bridge the knowledge gap for the computer science team, mitigating the implementation risks associated with bare-metal STM32 development.1 While the ESP32 includes Wi-Fi and Bluetooth capabilities, these features will remain strictly dormant during core execution to preserve real-time deterministic behavior, aligning with the mandate that cloud connectivity is not required for minimum demonstrable success.1

5. Signal Processing Evaluation

VibeGuard's efficacy hinges entirely on the robustness of its signal processing pipeline. Raw acceleration data must be accurately acquired, mathematically cleaned, transformed, and parameterized before edge intelligence algorithms can successfully infer the machine's mechanical health.1

Signal Acquisition Architecture

The ADXL345 supports both Inter-Integrated Circuit (I²C) and Serial Peripheral Interface (SPI) protocols.3 However, to achieve the absolute maximum Output Data Rate (ODR) of 3200 Hz required to satisfy the 1600 Hz Nyquist bandwidth, the SPI protocol is strictly required.3 The I²C bus, typically limited to 400 kHz in Fast Mode, incurs excessive protocol overhead. Relying on I²C makes it practically impossible to consistently extract 3200 16-bit samples per second across three spatial axes without risking buffer overflows and critical data loss.3

While the ADXL345 specifies maximum SPI clock speeds up to 5 MHz, practical prototype implementations utilizing standard jumper wires or solderless breadboards experience significant signal degradation, ringing, and capacitive loading above 2 MHz.31 Therefore, the engineering architecture dictates that the SPI clock must be conservatively constrained to between 1 MHz and 2 MHz to ensure data integrity.31

To maintain strict sampling timing stability, the ESP32 must utilize its SPI DMA capabilities.4 Relying on traditional software polling loops to read the sensor leads to sampling jitter, where the time delta between readings fluctuates based on CPU load. Jitter fundamentally destroys the phase accuracy required for a valid FFT. Instead, a hardware interrupt connected to the ADXL345's INT1 pin will signal the ESP32 exactly when the sensor's internal 32-level First-In-First-Out (FIFO) buffer reaches a predefined watermark.3 This hardware trigger initiates a rapid DMA block transfer, moving the vibration data directly from the SPI peripheral into the ESP32’s SRAM, ensuring mathematically perfect sampling intervals.4

Signal Processing Pipeline

The signal processing pipeline will feature a hybrid approach, extracting features in both the time domain and the frequency domain to maximize the diagnostic data available to the classification algorithm.16

Time-Domain Feature Extraction

Before frequency transformation occurs, lightweight statistical features provide immediate insight into vibration intensity and mechanical impulsiveness. These calculations require minimal processing overhead.16

Root Mean Square (RMS): Evaluates the overall vibration energy present in the machine. A slowly rising RMS trajectory correlates strongly with broad mechanical degradation and loosening structural foundations.

Peak Acceleration & Crest Factor: The crest factor is the mathematical ratio of peak acceleration to the RMS value. High crest factors indicate impulsive impacts, such as a localized pit in a bearing race striking a rolling element. A rising crest factor with a stable RMS is a classic early indicator of localized bearing damage.16

Kurtosis: Measures the "tailedness" of the vibration probability distribution. Kurtosis acts as a highly sensitive early indicator of mechanical faults long before overall RMS levels begin to shift.16

Frequency-Domain Transformation

The core of the analysis pipeline relies on the Fast Fourier Transform (FFT). The architecture will utilize the KISS_FFT library, a highly optimized C port wrapped in a C++ class specifically designed for constrained embedded environments like the ESP32.5

Before the FFT calculation is executed, the raw time-domain array must undergo Hann windowing. Because the ESP32 captures data in finite blocks (e.g., 1024 samples), the abrupt truncation at the beginning and end of the sample block causes "spectral leakage," where the energy of a specific frequency bleeds into adjacent frequency bins, blurring the results.32 Multiplying the raw data by a Hann window smoothly tapers the edges of the sample block to zero, dramatically improving the sharpness of the resulting frequency peaks.32 The output of the KISS_FFT process will be a magnitude spectrum array, clearly revealing the dominant rotational frequencies and harmonic resonances present in the machine structure.30

Noise Filtering & Spatial Isolation

The EDR explicitly highlights the profound challenge of single-node spatial isolation—the ability to filter out the structural noise of neighboring machinery without the geometric advantages of a distributed multi-sensor array.1

Academic literature frequently prescribes advanced Blind Source Separation (BSS) techniques such as Fast Independent Component Analysis (FastICA), Singular Spectrum Analysis (SSA), or Ensemble Empirical Mode Decomposition (EEMD) to unmix single-channel vibration signals into mathematically independent sources.7 However, analyzing the computational mechanics of FastICA reveals that it requires complex, iterative matrix inversions designed to maximize non-Gaussian properties.35 These calculations easily exhaust the deterministic timing budgets and memory limits of an ESP32 microcontroller, rendering BSS architectures inappropriate for this low-cost prototype.

To circumvent this limitation, a computationally frugal Spectral Subtraction methodology is recommended.8 During a dedicated machine calibration sequence, the ESP32 will capture the static ambient noise floor and establish the baseline spectral envelope of the target machine while it operates in a verified "normal" state. This baseline spectrum will be persistently stored. During active monitoring, this learned baseline will be mathematically subtracted from real-time FFT magnitude bins.8 This spectral subtraction effectively mutes persistent background frequencies—such as the 50 Hz hum of an adjacent pump—and aggressively amplifies new harmonic peaks that arise when a mechanical fault is deliberately introduced.

6. Edge Intelligence Evaluation

The final stage of the VibeGuard architecture is the decision-making framework. The objective is to evaluate the extracted time-domain features and the subtracted frequency spectrum to definitively classify the machine's state as "Normal" or "Abnormal" locally on the device, without human intervention or cloud analytics.1

Investigated Decision-Making Strategies

Static thresholding is the simplest approach, involving the comparison of overall RMS or peak acceleration values against a hardcoded scalar limit, such as those defined by ISO 10816 standards.1 While computationally negligible, static thresholding is highly susceptible to false alarms caused by transient motor load changes and entirely ignores the rich, early-warning diagnostic data embedded within the frequency spectrum.16

Supervised Machine Learning algorithms, such as Convolutional Neural Networks (CNNs) executed via TinyML frameworks like TensorFlow Lite for Microcontrollers, represent the modern academic standard.1 However, supervised models mandate vast quantities of carefully labeled training data for both normal and failure states. In the predictive maintenance domain, this is heavily criticized because genuine failure data is exceedingly rare; industrial machines operate normally 99% of the time, leading to a severe class imbalance problem.1 Furthermore, a student team lacks the capability to continuously destroy motors to generate sufficient labeled failure datasets.

Statistical Anomaly Detection, specifically One-Class Classification, offers a powerful unsupervised alternative. In this approach, the system does not need to know what a failure looks like; it only needs to learn the precise mathematical boundaries of "normal" behavior and flag significant statistical deviations from that established cluster.1

Recommended Edge Intelligence Strategy

The recommended intelligence architecture is Lightweight Statistical Anomaly Detection using multivariate distance metrics.

Because labeled failure data for student-built test rigs cannot be reliably sourced, supervised TinyML is unfeasible. Instead, the unsupervised baseline-comparison model directly addresses the project constraints.1

During the initial calibration sequence, the system will record multiple operational epochs of normal machine data. For each epoch, it will calculate a consolidated multi-dimensional feature vector consisting of the RMS value, Crest Factor, Kurtosis, and the magnitudes of the top three dominant FFT spectral peaks post-subtraction.5 The ESP32 will compute the mean and variance for each of these features to construct a statistical profile of normal operation.

During active, real-time monitoring, incoming feature vectors will be continuously evaluated against this established baseline using the Mahalanobis distance algorithm. Unlike simple Euclidean distance, the Mahalanobis calculation incorporates the covariance matrix of the data, meaning it understands that some features (like RMS) might naturally fluctuate more than others (like fundamental frequency peaks). If the calculated distance exceeds a dynamic statistical threshold—for example, exceeding three standard deviations from the mean for a sustained period of five seconds—the ESP32 will definitively classify the state as "Abnormal" and trigger the local alert system.

This approach is highly explainable, entirely circumvents the massive SRAM overhead of deep neural network weight matrices, avoids the class-imbalance problem inherent to supervised ML, and effectively satisfies the minimum demonstrable success criteria.1

7. Mechanical & Electrical Architecture

To ensure reliable data capture and hardware survival in simulated industrial environments, the mechanical coupling and electrical integrity of the prototype must be carefully engineered. Sensor data is entirely useless if the mechanical transmission path attenuates the frequencies of interest.

Mechanical Integration Strategy

The ADXL345 accelerometer relies on physical deflection to generate capacitance changes; therefore, any mechanical compliance or elasticity between the target machine and the sensor acts as a severe low-pass filter, damping the critical high-frequency fault signals before they ever reach the silicon.3

Eliminated mounting methods include magnetic bases and double-sided foam adhesives. While convenient for temporary deployment, foam tapes introduce mechanical resonance and catastrophic high-frequency signal attenuation.1 Magnetic mounts can slip under intense vibration and introduce rattling artifacts that corrupt the FFT spectrum.

The recommended method is Rigid Direct Mounting.1 The ADXL345 breakout board must be firmly secured to a rigid, 3D-printed Polyethylene Terephthalate Glycol (PETG) or Acrylonitrile Butadiene Styrene (ABS) fixture using standard M3 mechanical fasteners. This printed fixture must then be affixed directly to the metallic motor housing using cyanoacrylate adhesive (industrial superglue) or high-strength epoxy. This permanent, rigid bond guarantees the high-fidelity transmission of structural vibrations directly into the MEMS polysilicon structure, preserving the high-frequency harmonics essential for the anomaly detection algorithms.6

Electrical Architecture

The electrical architecture will prioritize signal integrity and power stability. The ADXL345 core chip operates safely at voltages between 2.0V and 3.6V.3 Because the ESP32 utilizes a 3.3V logic level, both devices can seamlessly share a common 3.3V power rail. This architectural decision explicitly eliminates the need for bidirectional logic level shifters, which can introduce propagation delays and distort high-speed SPI clock signals.3

Component Connection

ESP32 GPIO Pin

ADXL345 Pin

Purpose / Function

Power

3V3 / GND

VCC / GND

Common 3.3V Power Rail 3

SPI Clock

GPIO 18 (SCK)

SCL (SCK)

Master Clock (1 - 2 MHz) 3

SPI Master Out

GPIO 23 (MOSI)

SDA (MOSI)

Data out to Sensor 3

SPI Master In

GPIO 19 (MISO)

SDO (MISO)

Data in from Sensor 3

SPI Chip Select

GPIO 5 (CS)

CS

Active Low (Engages SPI Mode) 3

Hardware Interrupt

GPIO 4

INT1

Triggers DMA on FIFO Watermark 3

The SPI bus requires four dedicated data lines. Crucially, the CS (Chip Select) pin must be actively driven low by the ESP32 to forcefully engage the ADXL345's SPI mode; leaving it floating will cause the sensor to default to the slower I²C protocol.3

To mitigate electrical noise, a 0.1 µF ceramic bypass capacitor must be placed as physically close to the ADXL345 VCC and GND pins as possible. This capacitor filters high-frequency switching noise originating from the ESP32's internal voltage regulators and prevents transient voltage dips during Wi-Fi beacon bursts (if wireless features are later enabled).

For system feedback, an onboard common-cathode RGB LED will provide direct local indication, fulfilling the EDR requirement for clear, non-cloud alerting.1 The status logic will map strictly to colors: Green indicates "Normal Operation," Red indicates "Abnormal/Anomaly Detected," and Blue indicates "Calibration in Progress."

8. Prototype Implementation Strategy

Transforming the theoretical architecture into a physical, functional prototype requires a highly disciplined integration sequence to isolate engineering risks. The objective is to minimize debugging difficulty and systematically prove out each subsystem before combining them into a complex pipeline.

System Bring-Up Sequence

The bring-up strategy dictates that the student team must progressively verify the prototype in nine distinct stages:

Stage 1 - Power Subsystem: Supply power to the ESP32 via USB. Verify stable 3.3V delivery to both the ESP32 headers and the ADXL345 rails using a multimeter. Confirm that voltage ripple is minimized and that the system does not brown out.

Stage 2 - Microcontroller Operation: Flash basic "Blink" and serial communication firmware to the ESP32. Verify that the serial monitor outputs expected data and that the internal clock is stable.

Stage 3 - Sensor Communication: Initialize the ADXL345 over the SPI protocol. The firmware must read the DEVID register (address 0x00). According to the datasheet, this register is hardcoded to return the byte 0xE5.3 Successfully reading 0xE5 definitively validates the SPI wiring, clock polarity (CPOL), clock phase (CPHA), and logic levels.

Stage 4 - Raw Vibration Acquisition: Configure the BW_RATE register (address 0x2C) for 3200 Hz output and the DATA_FORMAT register (address 0x31) to enable full resolution and a measurement range of .3 Capture a raw stream of XYZ integers and plot them via the Arduino IDE Serial Plotter to visually confirm a 1g gravitational response on the Z-axis when the sensor is resting flat.6

Stage 5 - Signal Processing Integration: Implement the ESP32 DMA buffering system.4 Pass the time-domain buffers into the KISS_FFT library.32 Feed a known, controlled physical frequency (e.g., a vibrating smartphone emitting a 150 Hz tone) into the sensor block and mathematically verify that the FFT peak correctly aligns with the physical stimulus.

Stage 6 - Feature Extraction & Calibration: Program the baseline statistical averaging loops. Run the test motor in a known normal state and confirm that the ESP32 accurately computes and permanently stores the baseline feature vector.

Stage 7 - Edge-Classification Logic: Implement the Mahalanobis distance algorithm and the spectral subtraction methodology. Verify that distance metrics remain low during normal operation.

Stage 8 - Output Indication: Map the classification logic thresholds to the RGB LED GPIO pins.

Stage 9 - Complete Integrated Operation: Perform the full hardware-in-the-loop test utilizing the physical motor rig.

Prototype Validation & Test Scenarios

Industrial equipment failure cannot be practically or safely induced in a student laboratory environment without risking severe injury or expensive property damage. Therefore, a controlled, low-voltage experimental test rig is required to demonstrate the hypothesis.

The primary test scenario involves a small 12V DC motor or a rigid PC cooling fan securely mounted to a heavy wooden or acrylic base.1 The VibeGuard prototype will be rigidly mounted to the motor housing.

Normal Condition: The motor spins freely at a stable, regulated voltage. The VibeGuard prototype undergoes its calibration sequence, establishing a clean baseline spectrum heavily dominated by the primary rotational frequency.

Abnormal Condition Injection: To safely simulate a critical mechanical failure (such as bearing wear or bent shafting), a small mass—such as a metallic binder clip, a strip of heavy tape, or a piece of epoxy putty—is manually attached to one of the fan blades or the motor shaft.1 This deliberately creates a severely unbalanced rotational mass.

Success Criteria: As the unbalanced motor vibrates violently, the rotational frequency harmonic and structural resonances will spike dramatically in the FFT spectrum. The ESP32 must reliably execute spectral subtraction, compute the statistical deviation, and trigger the red "Abnormal" LED alert within three to five seconds. This effectively and repeatably proves the core engineering hypothesis without requiring actual industrial failure.1

Calibration & Debugging Strategy

Calibration is strictly necessary for this architecture.1 Due to microscopic manufacturing tolerances during the MEMS etching process, the ADXL345 Z-axis will almost never read exactly 1g when stationary, and the X and Y axes will exhibit slight non-zero offsets.36 These hardware offsets must be calculated dynamically during the initial device boot sequence. The system must average 200 static samples across all three axes while the machine is off, and write the inverse values to the hardware offset registers (OFSX 0x1E, OFSY 0x1F, OFSZ 0x20) to digitally zero the sensor prior to analysis.3

The primary debugging challenge will invariably involve SPI clock speeds and signal integrity over prototype wiring.31 If the serial monitor returns 0x00 or 0xFF instead of the expected 0xE5 Device ID, the SPI clock speed (configured via SPI_CLOCK_DIV) is likely too high for the jumper wires to support due to parasitic capacitance.31 The debugging strategy mandates stepping the clock speed down from 5 MHz to 1 MHz or lower until stable communication is achieved.31

9. Cost Assessment

The entire engineering architecture has been highly optimized to ensure absolute compliance with the educational financial constraint of ₹3000–₹5000 INR.1 The following estimates outline the complete prototype Bill of Materials (BOM) based on current Indian electronics market pricing.

Component

Engineering Description

Quantity

Estimated Cost (INR)

ESP32 Dev Board

Dual-core Wi-Fi/BT MCU with FPU 2

1

₹339 - ₹388

ADXL345 Module

3-Axis Digital MEMS Accelerometer Breakout 17

1

₹130 - ₹169

DC Motor Test Rig

Basic 12V motor, rigid mount base, unbalanced mass

1

₹300 - ₹500

Passive Components

Resistors, 0.1µF capacitors, common-cathode RGB LED, wires

1 set

₹150

Prototyping Board

Perforated fiberglass PCB / Solder breadboard

2

₹100

Power Supply

5V USB adapter, USB cable, and 12V supply for motor

1 set

₹300

Mechanical Fixtures

3D Printed PETG enclosure & rigid mounting hardware (M3 bolts)

1 set

₹250 (material)

Contingency (20%)

Financial buffer for replacement parts / expedited shipping

-

₹350

Total Estimated Cost

Projected Total Prototype Expenditure

₹1,919 - ₹2,207

The proposed architecture comfortably clears the budget feasibility gate.1 Utilizing approximately 60% to 70% of the absolute minimum allotted ₹3000 INR budget, this approach allows ample financial overhead. Should hardware damage occur during soldering or assembly, replacement parts can be easily procured without jeopardizing the project's financial standing.

10. Engineering Risk Assessment

Despite the rigorous architectural planning, implementing a high-frequency vibration analysis system on low-cost hardware inherently carries significant engineering risk.

Risk Category

Engineering Risk Description

Likelihood

Impact

Mitigation & Contingency Strategy

Hardware / Comm.

ADXL345 SPI bus corruption due to breadboard capacitance and aggressive clock speeds.31

High

Critical

Mitigation: Abandon solderless breadboards for the final prototype. Use short, directly soldered wires on a perforated PCB. Start SPI communication at 100 kHz and step up incrementally.31 Contingency: Revert to the slower 400 kHz I²C communication protocol, sacrificing the 3200 Hz sampling rate in favor of guaranteed stability.

Algorithmic

Ambient factory noise floor completely masks the mechanical fault spectrum, causing false negatives.1

Medium

High

Mitigation: Aggressively implement the baseline Spectral Subtraction methodology to mathematically mute static environmental noise before calculating the Mahalanobis distance.8

Firmware

ESP32 memory exhaustion and kernel panics due to large FFT arrays or floating-point memory leaks.39

Medium

High

Mitigation: Utilize the highly memory-efficient KISS_FFT library specifically designed for embedded constraints.5 Constrain the FFT size (e.g., to 512 or 1024 bins) to fit securely within the ESP32's available SRAM limitations.

Mechanical

Poor mechanical coupling acts as a physical low-pass filter, preventing high-frequency fault detection.1

Low

Critical

Mitigation: Strictly enforce rigid mounting protocols (industrial cyanoacrylate or M3 bolts). Under no circumstances should the team rely on elastomeric foam adhesives or weak magnetic bases for the primary prototype.

Schedule / Scope

Feature creep causes the team to focus on building Wi-Fi/Cloud dashboards rather than solving local anomaly detection.

High

Medium

Mitigation: Strictly enforce the Minimum Demonstrable Success criteria outlined in the EDR.1 All cloud connectivity, MQTT telemetry, and Bluetooth features are strictly banned until the local RGB LED alert operates flawlessly and repeatably.

11. Team Feasibility

The specified five-member implementation team comprises three advanced Computer Science/Cybersecurity students, one beginner programmer, and one hardware/fabrication support member.1 This specific team composition is highly synergistic with the proposed VibeGuard architecture, which previous analysis has identified as possessing excellent team-capability alignment.1 Because the primary challenges lie in digital signal processing and algorithmic logic rather than complex analog circuit design, the computer science-heavy team is well-positioned for success.

Recommended Responsibility Allocation:

CS Expert 1 (Firmware & Real-Time Architect): Assigned to ESP32 FreeRTOS management, configuring the SPI DMA bus for jitter-free acquisition, and executing the ADXL345 register initialization (BW_RATE, DATA_FORMAT, FIFO_CTL).3

CS Expert 2 (Signal Processing Engineer): Assigned to implementing the KISS_FFT library, applying Hann windowing functions to prevent spectral leakage, and coding the Time-Domain feature extraction algorithms (RMS, Crest Factor, Kurtosis).16

CS Expert 3 (Edge AI Integrator): Assigned to developing the statistical anomaly detection logic, managing the covariance matrices for baseline distance calculations, and perfecting the Spectral Subtraction noise isolation routines.8

Beginner Programmer (Systems Logic): Assigned to implementing the linear calibration logic sequence, mapping logic thresholds to the RGB LED alerts, and managing the data-logging interface (writing clean output states to the Arduino Serial Monitor).30 This provides a highly manageable learning curve involving discrete logic states and direct visual feedback.

Hardware/Fabrication Lead: Assigned to procuring the entire BOM, assembling the mechanical DC motor test rig, soldering the prototype PCB to eliminate SPI jumper-wire jitter, and ensuring the absolute rigid mechanical coupling of the ADXL345 to the motor housing.

The primary learning curve for the advanced software team will be navigating hardware-level interrupts and memory optimization within an RTOS environment, while the hardware team will face the challenge of eliminating electrical noise from the sensitive SPI bus.

12. Innovation Discussion

While industrial vibration monitoring is recognized as a highly mature engineering domain 1, the specific VibeGuard architecture presents notable innovation opportunities specifically in the realm of severely constrained edge intelligence.

The primary avenue for future innovation lies in refining the single-node spatial noise isolation capability. Utilizing adaptive Spectral Subtraction to mute the operational harmonics of a neighboring machine using only a single ADXL345 sensor and a ₹400 MCU pushes the boundaries of what localized, low-cost predictive maintenance can achieve.1 If the statistical Mahalanobis algorithm can be tuned to dynamically adapt to subtle motor load changes without triggering false positives, this architecture could offer a highly disruptive, low-cost monitoring alternative for small-to-medium enterprises (SMEs) that currently rely entirely on periodic manual inspections or run-to-failure operational models.

Furthermore, the highly modular nature of the KISS_FFT integration and the statistical baseline code provides a foundational architecture that can be massively scaled. Future iterations beyond the academic semester could easily unlock the ESP32’s native Wi-Fi capabilities to broadcast lightweight, 1-byte alert flags to a centralized MQTT broker. This would transform the standalone edge node into the foundation for a massive, low-bandwidth industrial mesh network, achieving enterprise-scale visibility at a fraction of commercial costs.

13. Final Engineering Recommendation

The VibeGuard concept demonstrates a highly robust engineering foundation. By aggressively shifting the complexity from expensive analog hardware (e.g., ADXL1002) to advanced embedded software algorithms (KISS_FFT and statistical anomaly detection) running on the highly capable but low-cost ESP32, the architecture perfectly addresses the dual requirements of extreme affordability and true edge-intelligence.1

The explicit selection of the ADXL345 accelerometer over the SPI bus guarantees sufficient Nyquist bandwidth to capture primary machine harmonics, while decisively avoiding the EMI vulnerabilities inherent to gyroscopic IMUs like the MPU6050.3 The reliance on statistical anomaly detection rather than supervised machine learning gracefully bypasses the industrial data-scarcity problem.1

The project constraints regarding budget, timeline, and educational team capabilities are comfortably satisfied. The most critical engineering hurdles will be tuning the SPI bus speed to prevent data corruption and ensuring uncompromisingly rigid mechanical coupling to prevent physical signal loss.

Therefore, the Phase 3C Engineering Architecture Review Board concludes that this implementation plan is technically sound, highly achievable, and precisely optimized for engineering demonstration success.

Phase 3C Final Readiness Classification: READY WITH MINOR REFINEMENTS

PHASE 3C MEMORY GENERATION

Project VibeGuard - Architecture Finalization Memory

Selected Architecture: Single-Node Passive Edge-Intelligence (The Active Cancellation approach was explicitly rejected as a fundamental conceptual error contradicting the EDR).

Selected Sensor: ADXL345 (Digital MEMS Accelerometer). Chosen for its 3200 Hz Output Data Rate (ODR), SPI interface capability, 13-bit resolution, and exceptional low cost (₹130–₹170 INR).

Selected MCU: ESP32 (DevKitC). Chosen for its dual-core 240 MHz processing speed, hardware Floating-Point Unit (FPU) for rapid FFT calculations, FreeRTOS support, and DMA-capable SPI bus.

Selected Processing Approach: Hardware-timed SPI DMA data acquisition triggered by the INT1 pin into a First-In-First-Out (FIFO) buffer. The pipeline executes time-domain feature extraction (RMS, Crest Factor, Kurtosis) alongside frequency-domain transformation using the highly optimized KISS_FFT library with Hann windowing.

Selected Edge-Intelligence Strategy: Unsupervised One-Class Statistical Anomaly Detection. Spectral Subtraction is employed for localized spatial noise isolation, followed by multivariate Mahalanobis distance comparisons against a calibrated normal baseline to trigger local alerts. Supervised ML was rejected due to lack of failure data.

Electrical Architecture: 3.3V unified logic level, direct SPI wiring (CS driven low to engage SPI), with 0.1 µF bypass capacitors to filter ESP32 switching noise.

Mechanical Integration: Absolute rigid mounting is required. The breakout board must be secured to a 3D-printed fixture and affixed via cyanoacrylate or epoxy directly to the test rig to prevent mechanical low-pass filtering. Adhesives and magnets are banned.

Estimated Cost: ~₹1,900 - ₹2,200 INR. This safely utilizes only ~60% to 70% of the minimum ₹3000 budget, providing excellent contingency overhead.

Major Engineering Risks: SPI signal degradation at high clock frequencies over prototype wiring causing read failures (DEVID missing 0xE5); ambient noise masking the subtle fault spectrum; FFT processing exhausting SRAM.

Unresolved Questions: The exact statistical threshold multiplier (number of standard deviations) required to avoid false positives during transient motor loads must be determined empirically during Phase 7 physical testing.

Implementation Priorities: Establish stable SPI communication and DMA buffering first. The team must not attempt FFT processing until raw gravitational acceleration vectors (Z-axis = 1g) are cleanly plotted and verified.

Rationale Behind Major Decisions: The ADXL1002 was abandoned due to exorbitant costs exceeding the entire project budget. The MPU6050 was abandoned due to EMI susceptibility from its gyroscope and lower bandwidth limits. The ESP32 was selected over the RP2040 and STM32 due to the presence of an FPU and broader accessibility for a computer science-heavy student team. The architecture aggressively leverages computational software to achieve diagnostics that typically require expensive enterprise hardware.

Works cited

Engineering_Design_Review.md

ESP32S 38Pin Development Board (WIFI+BLUETOOTH) - Quartz Components, accessed on July 25, 2026, https://quartzcomponents.com/products/esp32-development-board-wifi-bluetooth

ADXL345 Guide: Datasheet, Pinout, Arduino, ESP32 & Calibration - Bettlink, accessed on July 25, 2026, https://www.bettlink.com/blog/adxl345-guide

lovyan03/ESP32_DmaSamples: ESP32 DMA Samples - GitHub, accessed on July 25, 2026, https://github.com/lovyan03/ESP32_DmaSamples

The KISS FFT Arduino & ESP32 library - Adafruit Blog, accessed on July 25, 2026, https://blog.adafruit.com/2026/04/28/the-kiss-fft-arduino-esp32-library/

ADXL345 Accelerometer: Tilt and Vibration Sensing with Arduino - Zbotic, accessed on July 25, 2026, https://zbotic.in/adxl345-accelerometer-tilt-and-vibration-sensing-with-arduino/

Single-Channel Blind Signal Separation of the MHD Linear Vibration Sensor Based on Singular Spectrum Analysis and Fast Independent Component Analysis - MDPI, accessed on July 25, 2026, https://www.mdpi.com/1424-8220/22/24/9657

An Improved Spectral Subtraction Method for Eliminating Additive Noise in Condition Monitoring System Using Fiber Bragg Grating Sensors - MDPI, accessed on July 25, 2026, https://www.mdpi.com/1424-8220/24/2/443

A Rolling Bearing Vibration Signal Noise Reduction Processing Algorithm Using the Fusion HPO-VMD and Improved Wavelet Threshold - MDPI, accessed on July 25, 2026, https://www.mdpi.com/2073-8994/17/8/1316

Analog Devices Inc. ADXL1002 Series Accelerometers – Mouser India, accessed on July 25, 2026, https://www.mouser.in/c/sensors/motion-position-sensors/accelerometers/?m=Analog%20Devices%20Inc.&series=ADXL1002

ADXL1002BCPZ-RL7 Analog Devices - Mouser Electronics India, accessed on July 25, 2026, https://www.mouser.in/en/ProductDetail/Analog-Devices/ADXL1002BCPZ-RL7?qs=5aG0NVq1C4yp4sXR7poivg%3D%3D

ADXL1002BCPZ Analog Devices Inc. | Accelerometers - DigiKey, accessed on July 25, 2026, https://www.digikey.in/en/products/detail/analog-devices-inc/ADXL1002BCPZ/7041452

ADXL1002 Analog Devices Inc. | Evaluation Boards - DigiKey, accessed on July 25, 2026, https://www.digikey.in/en/products/base-product/analog-devices-inc/505/ADXL1002/301217

Vibration/Shock Sensor Module (SW420) - Quartz Components, accessed on July 25, 2026, https://quartzcomponents.com/products/vibration-sensor-module-sw420

Buy Sensors Online - Electronic Components Store in India, accessed on July 25, 2026, https://www.electronicscomp.com/sensors-module/sensors?sort=p.model&order=DESC&page=9

IoT Predictive Maintenance: Vibration Sensors on ESP32 - Zbotic, accessed on July 25, 2026, https://zbotic.in/iot-predictive-maintenance-vibration-sensors-on-esp32/

Adxl345 Triple-axis Accelerometer Sensor at 157.00 INR in Delhi | R And D Control Systems, accessed on July 25, 2026, https://www.tradeindia.com/products/adxl345-triple-axis-accelerometer-sensor-c12687515.html

MPU6050 3-Axis Gyro/Accelerometer IC - QFN-24 SMD Package – QuartzComponents, accessed on July 25, 2026, https://quartzcomponents.com/products/mpu-6050-3-axis-gyro-accelerometer-ic-tdk-invensense-qfn-24-smd-package

MPU6050 vs ADXL345: A Comparative Analysis of Accelerometers, accessed on July 25, 2026, https://thecustomizewindows.com/2024/06/mpu6050-vs-adxl345-a-comparative-analysis-of-accelerometers/

Adxl345 vs mpu6050 vs bno055 - Sensors - Arduino Forum, accessed on July 25, 2026, https://forum.arduino.cc/t/adxl345-vs-mpu6050-vs-bno055/1218136

ADXL345 3-Axis Digital Acceleration Sensor - IndiaMART, accessed on July 25, 2026, https://www.indiamart.com/proddetail/adxl345-3-axis-digital-acceleration-sensor-17156300548.html

Buy ADXL345- 3-axis MEMS accelerometerFrom India's Best Electronics Components Store!, accessed on July 25, 2026, https://www.mathaelectronics.com/product/adxl345/

Raspberry Pi Pico - Original – QuartzComponents, accessed on July 25, 2026, https://quartzcomponents.com/products/raspberry-pi-pico

Raspberry Pi Pico: What you should know and How to get started? - Quartz Components, accessed on July 25, 2026, https://quartzcomponents.com/blogs/electronics-projects/raspberry-pi-pico-what-you-should-know-and-how-to-get-started

Raspberry Pi Pico - Robu.in, accessed on July 25, 2026, https://robu.in/product-category/raspberry-pi-pico/

Black Pill - Robu.in, accessed on July 25, 2026, https://robu.in/product-tag/black-pill/

Esp32 Series - Robu.in, accessed on July 25, 2026, https://robu.in/product-tag/esp32-series/

What's the difference between these s two boards? : r/embedded - Reddit, accessed on July 25, 2026, https://www.reddit.com/r/embedded/comments/1by6b7l/whats_the_difference_between_these_s_two_boards/

ESP32 Development Board with Wifi & Bluetooth buy online at Low Price in India, accessed on July 25, 2026, https://www.electronicscomp.com/esp32-development-board-with-wifi-bluetooth-india

FFT (Fast Fourier Transform) on the ESP32 Development Board - Elektor Magazine, accessed on July 25, 2026, https://www.elektormagazine.com/articles/fast-fourier-transform-fft-on-the-esp32

ADXL345 SPI output 000 on the serial monitor – ESP32 & ESP8266 - DroneBot Workshop Forums, accessed on July 25, 2026, https://forum.dronebotworkshop.com/esp32-esp8266/adxl345-spi-output-000-on-the-serial-monitor/

meerzafarnoohani/KISS_FFT: Lightweight FFT library for Arduino & ESP32. Frequency analysis, audio spectrum, pitch detection - GitHub, accessed on July 25, 2026, https://github.com/meerzafarnoohani/KISS_FFT

KISS_FFT - Arduino Library List, accessed on July 25, 2026, https://www.arduinolibraries.info/libraries/kiss_fft

Single-Channel Blind Source Separation and Its Application on Arc Sound Signal Processing, accessed on July 25, 2026, https://rwlab.sjtu.edu.cn/tiwm/papers/V1N2-8.pdf

Single-channel blind source separation of underwater acoustic signals using improved NMF and FastICA - Frontiers, accessed on July 25, 2026, https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2022.1097003/full

Interfacing ADXL345 with Arduino using I2C (Complete Beginner-Friendly Tutorial), accessed on July 25, 2026, https://controllerstech.com/adxl345-arduino-i2c-tutorial/

AnuElectronics ADXL345 3-Axis Digital Accelerometer Sensor Module... more - Flipkart, accessed on July 25, 2026, https://www.flipkart.com/anuelectronics-adxl345-3-axis-digital-accelerometer-sensor-module-i2c-spi-electronic-components-hobby-kit/p/itmbdc79ce36c73f

ADXL345 Digital Accelerometer - Trustworthy Motion Sensor by DNA Solutions, accessed on July 25, 2026, https://www.dnatechindia.com/adxl345_3_axis_mems_accelerometer_module_india.html

ESP32/FFT_on_ESP32_Arduino/Readme.md at master - GitHub, accessed on July 25, 2026, https://github.com/yash-sanghvi/ESP32/blob/master/FFT_on_ESP32_Arduino/Readme.md
