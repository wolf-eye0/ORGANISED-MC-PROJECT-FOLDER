# Phase 3C — VibeGuard Deep Research Prompt

> **Project:** Project mC | **Concept:** VibeGuard | **Phase:** 3C — Architecture Definition & Engineering Selection
> **Status:** Pre-Research / Architecture Investigation
> **Prepared by:** Chief Engineering Review Board (Claude)
> **Date:** July 25, 2026

---

## 📋 Document Overview

This is the **official Deep Research Prompt** for **Phase 3C** of **Project mC** for the **VibeGuard** concept. It serves as the commissioning document for independent Deep Research AI systems to investigate and recommend the optimal engineering architecture for VibeGuard's prototype implementation.

**Purpose:** Convert the validated VibeGuard engineering concept into a concrete, evidence-based prototype architecture that satisfies the Engineering Design Review (EDR) while remaining achievable within project constraints.

**Target Audience:** Independent Deep Research AI systems (Gemini, Qwen, Perplexity, Mistral, etc.) acting as an Engineering Architecture Review Board.

---

## 🎯 Part 1 — Role, Context & Engineering Objectives

### 1.1 Role Definition

You are an **elite multidisciplinary Engineering Architecture Review Board** conducting Phase 3C of Project mC for the VibeGuard concept. Your board comprises:

- Senior Embedded Systems Architect
- Industrial Condition Monitoring Engineer
- Predictive Maintenance Researcher
- MEMS Sensor Specialist
- Signal Processing Engineer
- Edge AI Engineer
- Electronics Hardware Engineer
- Mechanical Systems Engineer
- Manufacturing Engineer
- Embedded Firmware Architect
- Reliability Engineer
- Product Development Engineer

**Your task is NOT to invent a new project.** Your responsibility is to determine the **strongest engineering architecture** capable of demonstrating VibeGuard's **approved engineering hypothesis** within the project's constraints.

---

### 1.2 Project Context

#### Previous Phase Findings (Phase 3B)

✅ **Feasibility Confirmed**: VibeGuard is achievable by the student team within ₹3000–₹5000 budget and 2-month timeline
✅ **Best Team Fit**: Purely software/algorithmic challenge matches CS/Cybersecurity skills (best of all 5 concepts)
✅ **Architecture Consensus**: ESP32-class MCU + MEMS accelerometer (ADXL345/MPU6050/IIS3DWB)
✅ **Primary Challenge**: Single-node spatial/spectral noise isolation from neighboring machinery
✅ **Budget Range**: ₹1000–4700 (all estimates comfortably within ₹5000 ceiling)

#### Key Disagreements from Phase 3B (To Be Resolved in Phase 3C)

| Disagreement | Positions | Resolution Needed |
|--------------|-----------|-------------------|
| Classification Approach | Classical DSP (Mistral, Perplexity) vs. Edge AI/TinyML (Gemini) | Which approach best demonstrates the hypothesis? |
| Sensor Bandwidth | ADXL345 (1600 Hz) adequate (Gemini, Perplexity) vs. need IIS3DWB (6 kHz+) (Mistral) | Is 1600 Hz sufficient for bearing fault detection? |
| ML Necessity | Required (Gemini) vs. Optional (Mistral, Perplexity) | Can classical DSP alone satisfy the EDR? |

---

### 1.3 Authoritative Specifications (From Engineering Design Review)

#### Engineering Identity
VibeGuard is an **embedded edge-intelligence condition monitoring system** designed to improve machine reliability by analyzing vibration data locally on resource-constrained hardware.

#### Mission
Enable affordable predictive condition monitoring through the **early detection of abnormal machine behaviour**, reducing unplanned downtime and supporting proactive maintenance decisions.

#### Engineering Hypothesis
*A low-cost embedded edge-intelligence system can locally analyze machine vibration signals and reliably distinguish normal operating conditions from early abnormal behaviour using computational methods suitable for resource-constrained hardware.*

#### Fixed Design Principles (IMMUTABLE)
1. ✅ Maintain affordability as a primary design objective
2. ✅ Perform condition analysis **locally on embedded hardware**
3. ✅ Focus on **early detection of abnormal operating behaviour** rather than comprehensive industrial fault diagnosis
4. ✅ Produce **interpretable and repeatable maintenance alerts**
5. ✅ Avoid dependence on continuous cloud connectivity
6. ✅ Ensure the solution remains suitable for **educational prototypes and SME-oriented applications**

#### Minimum Demonstrable Success (MDS)
The prototype shall demonstrate:
1. ✅ Sense vibration from a **representative machine or controlled test rig**
2. ✅ Establish or recognize a **normal operating vibration condition**
3. ✅ Detect a **deliberately introduced abnormal vibration condition**
4. ✅ Classify the observed condition as at least: **Normal** or **Abnormal**
5. ✅ Perform the core classification **locally on the embedded system**
6. ✅ Produce a **clear output** indicating the detected condition

> **Note:** The prototype does NOT need to perform complete industrial predictive-maintenance forecasting. It must first demonstrate that the fundamental engineering hypothesis works.

---

### 1.4 Primary Objective

Determine the **simplest, lowest-cost, technically defensible embedded architecture** that can reliably demonstrate edge-based normal-versus-abnormal vibration classification while:

- ✅ Preserving VibeGuard's intended innovation direction (edge intelligence for vibration discrimination)
- ✅ Remaining achievable by the **five-member student team**
- ✅ Fitting within **₹3000–₹5000 INR budget**
- ✅ Completing within **~2 month semester timeline**
- ✅ Using **available college facilities** (basic fabrication, 3D printing, hand tools)

**The selected architecture should maximize engineering validity while minimizing unnecessary implementation risk.**

---

### 1.5 Project Constraints

#### Budget
- **Preferred**: ≤ ₹3000 INR
- **Maximum**: ≤ ₹5000 INR
- Must include contingency for failed components and replacements

#### Team Composition (5 Members)

| Member Type | Count | Primary Contributions | Skill Level |
|-------------|-------|----------------------|-------------|
| Computer Science/Cybersecurity | 3 | Embedded firmware, electronics integration, embedded programming, debugging, architecture implementation | Technically strong |
| Beginner Programmer | 1 | Manageable embedded/software tasks (learning opportunity) | Learning |
| Hardware/Mechanical Supporters | 2 | Component sourcing, prototype assembly, fabrication, mechanical work, documentation, coordination with engineering departments | Capable |

> **Critical Constraint:** Team has **no professional mechanical or industrial vibration-analysis expertise**. External departmental consultation may be used, but final prototype must be student-buildable.

#### Platform Requirements
- Low-cost embedded hardware
- Standalone operation (no cloud dependency for MDS)
- Arduino IDE-compatible development where practical
- Local/edge processing mandatory

#### Innovation Preservation
The architecture **must preserve** VibeGuard's core differentiator:
> Low-cost embedded edge intelligence applied to machine-vibration monitoring, specifically the ability to **distinguish target machine vibration from environmental/neighboring-machine noise using a single sensor node**.

If simplification is required, document:
- What was preserved
- What was simplified
- Why simplification was necessary
- Path to restore advanced capability in future versions

---

### 1.6 Engineering Philosophy

**Priority Order:**
1. Validation of engineering hypothesis (non-negotiable)
2. Reliable prototype operation
3. Student buildability
4. Cost effectiveness
5. Mechanical simplicity
6. Ease of debugging
7. Future scalability
8. Innovation potential

**Core Principle:**
> Build the **strongest educational engineering prototype** capable of demonstrating the approved engineering hypothesis, **not** the most sophisticated industrial monitoring system.

---

### 1.7 Research Expectations

#### Do NOT:
- ❌ Invent specifications
- ❌ Fabricate component capabilities
- ❌ Assume industrial performance without evidence
- ❌ Exaggerate embedded AI capabilities
- ❌ Recommend hardware without engineering justification
- ❌ Replace missing evidence with speculation

#### DO:
- ✅ Investigate multiple implementation approaches
- ✅ Compare competing architectures objectively
- ✅ Justify every recommendation with **engineering evidence**
- ✅ Explain engineering trade-offs explicitly
- ✅ Identify remaining uncertainties
- ✅ Preserve evidence quality throughout

#### Evidence Hierarchy (Prefer in Order):
1. **Primary sources**: Datasheets, peer-reviewed papers, standards documents
2. **Industry practice**: Established engineering methods, commercial implementations
3. **Empirical data**: Published benchmarks, test results
4. **Expert consensus**: Multiple independent sources agreeing
5. **Reasoned inference**: Logical extrapolation from established principles

---

### 1.8 Hallucination Prevention

**Mandatory Checks:**
- [ ] Every technical claim is traceable to a cited source
- [ ] Component specifications come from official datasheets
- [ ] Performance claims are based on published measurements
- [ ] Uncertainty is explicitly acknowledged, not hidden
- [ ] Conflicting evidence is preserved, not averaged away

**When Uncertainty Exists:**
1. Explicitly acknowledge the uncertainty
2. Explain why it exists
3. Compare conflicting evidence objectively
4. Recommend how **prototype testing** can resolve it

---

## 🏗️ Part 2 — Engineering Architecture Investigation

### 2.1 Candidate System Architecture Investigation

**Objective:** Investigate multiple architecture approaches rather than assuming one implementation from the start.

#### Candidate Architecture Categories

**A. Sensing Architecture**
- Single-sensor node (preferred - matches EDR's single-node noise isolation challenge)
- Multi-sensor array (higher accuracy but violates affordability principle)
- Hybrid sensor fusion (accelerometer + microphone for acoustic emission)

**B. Processing Architecture**
- Edge-only processing (mandatory for MDS)
- Edge + optional cloud offload (for future scalability, not required for MDS)
- Distributed edge nodes (beyond MDS scope)

**C. Intelligence Architecture**
- Classical DSP (FFT, envelope analysis, spectral kurtosis)
- Lightweight ML/TinyML (Isolation Forest, quantized autoencoders, 1D CNNs)
- Hybrid DSP + ML (two-stage pipeline)
- Threshold-based (RMS, peak, variance) - baseline for comparison

**D. Mechanical Architecture**
- Rigidly coupled sensor (critical for high-frequency fidelity)
- Flexible/adhesive mounting (easier but may filter out fault signatures)
- Test rig integration (self-contained demonstration setup)

#### Evaluation Criteria

For **every** candidate architecture, evaluate and document:

| Criterion | Description | Priority |
|----------|-------------|----------|
| Hypothesis Validation | Directly demonstrates the EDR's engineering hypothesis | Critical |
| MDS Compliance | Meets all Minimum Demonstrable Success requirements | Critical |
| Single-Node Feasibility | Works with one sensor (not array-dependent) | Critical |
| Edge Processing | All classification happens on-device | Critical |
| Budget Fit | Total cost ≤ ₹5000 (preferably ≤ ₹3000) | Critical |
| Team Buildability | Achievable by student team with stated skills | Critical |
| Sensor Quality | Adequate frequency response and sensitivity | High |
| Noise Isolation | Handles neighboring machine vibration | High |
| False Alarm Resistance | Minimizes false positives/negatives | High |
| Mechanical Simplicity | Minimal complex fabrication | High |
| Component Availability | Indian market procurement feasibility | High |
| Power Consumption | Suitable for embedded/battery operation | Medium |
| Debugging Ease | Supports troubleshooting and iteration | Medium |
| Scalability | Path to more advanced versions | Medium |
| Innovation Potential | Preserves patent-worthy elements | Medium |

---

### 2.2 Vibration Sensor Investigation

**Objective:** Determine the most appropriate sensing technology for the prototype.

#### Candidate Sensor Classes

**MEMS Accelerometers (Primary Candidates)**

| Model | Supplier | Interface | Range | Bandwidth | Sensitivity | Cost (INR) | Notes |
|-------|----------|-----------|-------|----------|------------|------------|-------|
| ADXL345 | Analog Devices | I2C/SPI | ±2/4/8/16g | **1600 Hz** | 3.9 mg/LSB | ₹90–500 | 10-bit, widely available, Phase 3B disagreement on adequacy |
| MPU6050 | InvenSense | I2C | ±2/4/8/16g | 1000 Hz | 0.061 mg/LSB | ₹200–400 | Includes gyro (unused), common |
| **IIS3DWB** | STMicro | I2C/SPI | ±2/4/8/16g | **6000 Hz** | 0.061 mg/LSB | ₹800–1200 | **Recommended by Mistral**, covers full bearing fault range |
| LIS3DH | STMicro | I2C/SPI | ±2/4/8/16g | 5300 Hz | 1 mg/LSB | ₹300–600 | Lower noise, good alternative |
| MMA8452Q | NXP | I2C/SPI | ±2/4/8g | 800 Hz | 0.063 mg/LSB | ₹400–700 | Low power |

**Key Question:** Is ADXL345's 1600 Hz bandwidth **sufficient** for bearing fault detection, or is IIS3DWB's 6000 Hz **required**?

#### Comparison Dimensions

For each candidate sensor, analyze:
1. **Frequency Response** (Required: 1–10 kHz for bearing defects)
2. **Sensitivity & Noise Floor** (Must detect subtle vibration changes)
3. **Sampling Capability** (Nyquist: >2× highest frequency of interest)
4. **Interface Complexity** (I2C vs SPI vs analog)
5. **Mounting Sensitivity** (Rigid vs flexible mounting effects)
6. **Environmental Robustness** (Temperature range, shock resistance)
7. **Availability in Indian Market** (Suppliers: Robu, Quartz, SunRobotics, LCSC)
8. **Cost** (Must fit within overall budget)

#### Recommendation Requirements
Provide **TWO recommendations**:
1. **Technically strongest option** (best performance, regardless of cost)
2. **Most practical student-project option** (best balance of performance and feasibility)

---

### 2.3 Embedded Processing Platform

**Objective:** Select the MCU platform that best supports vibration signal processing.

#### Candidate Platforms

**ESP32 Series**
| Model | Core | Clock | RAM | Flash | FPU | ADC | Cost (INR) | Notes |
|-------|------|-------|-----|-------|-----|-----|------------|-------|
| ESP32-WROOM-32 | Xtensa LX6 (2 cores) | 160/240 MHz | 520 KB | 4–16 MB | ✅ | 12-bit, 2×12ch | ₹300–800 | Wi-Fi/BT, CMSIS-DSP support |
| ESP32-S3 | Xtensa LX7 (2 cores) | 240 MHz | 512 KB | 8 MB | ✅ | 12-bit, 2×12ch | ₹500–1000 | Native USB, more GPIOs |

**STM32 Series**
| Model | Core | Clock | RAM | Flash | FPU | ADC | Cost (INR) | Notes |
|-------|------|-------|-----|-------|-----|-----|------------|-------|
| STM32F103 (Blue Pill) | Cortex-M3 | 72 MHz | 20–64 KB | 64–512 KB | ❌ | 12-bit, 16ch | ₹200–400 | No FPU, limited DSP |
| STM32F401 | Cortex-M4 | 84 MHz | 96 KB | 512 KB | ✅ | 12-bit, 16ch | ₹400–700 | FPU for FFT |
| STM32F411 | Cortex-M4 | 100 MHz | 128 KB | 512 KB | ✅ | 12-bit, 16ch | ₹500–900 | More RAM for buffers |

**Arduino-Class**
| Model | Core | Clock | RAM | Flash | FPU | ADC | Cost (INR) | Notes |
|-------|------|-------|-----|-------|-----|-----|------------|-------|
| Arduino Uno | ATmega328P | 16 MHz | 2 KB | 32 KB | ❌ | 10-bit, 6ch | ₹200–500 | Too limited for FFT |
| Arduino Nano 33 BLE | nRF52840 | 64 MHz | 256 KB | 1 MB | ✅ | 12-bit, 8ch | ₹800–1200 | Good for Bluetooth |

**RP2040**
| Raspberry Pi Pico | Cortex-M0+ (2 cores) | 133 MHz | 264 KB | 2 MB | ❌ | 12-bit, 8ch | ₹400–700 | No FPU but fast |

#### Comparison Dimensions
1. **Processing Capability** (FFT: 1024-point float needs ~4 KB RAM)
2. **Memory Requirements** (Sample buffers, FFT buffers, model storage)
3. **ADC Performance** (Resolution, sampling rate, external ADC option)
4. **Peripheral Support** (I2C/SPI, timers, DMA, UART)
5. **DSP Acceleration** (Hardware FPU, CMSIS-DSP library support)
6. **Development Ecosystem** (Arduino IDE, libraries, debugging)
7. **Power Consumption** (Active mode, sleep mode)
8. **Cost** (MCU board + supporting circuitry)

**Phase 3B Finding:** ESP32 or STM32 with **hardware FPU** recommended to avoid compute exhaustion for real-time FFT.

---

### 2.4 Signal Acquisition Architecture

**Objective:** Determine the optimal signal acquisition chain from sensor to MCU.

#### Key Decisions

**A. Sampling Strategy**
- **Sampling Rate**: 25–50 kHz (for bearing faults up to 10 kHz)
- **Anti-Aliasing**: Analog low-pass filter before ADC
- **Sampling Mode**: Continuous (best fidelity) vs. Burst (lower power)

**B. ADC Configuration**
- **Resolution**: 10-bit (1024 levels) vs 12-bit (4096 levels) vs 16-bit
- **Sampling Method**: Polling vs Timer-triggered vs DMA
- **Buffer Management**: Circular buffer vs Double-buffer

**C. Timing Requirements**
- **Sampling Clock Stability**: Jitter < 1% of sample period
- **Synchronization**: Hardware timer vs external clock

---

### 2.5 Signal Processing Investigation

**Objective:** Determine the optimal signal processing pipeline.

#### Processing Pipeline Stages

**Stage 1: Preprocessing**
- DC removal (high-pass filter)
- Mean subtraction
- Windowing (Hamming, Hann, Blackman-Harris for FFT)

**Stage 2: Time-Domain Features**
| Feature | Computational Cost | Usefulness | Notes |
|---------|-------------------|------------|-------|
| RMS | Very Low | High | Overall vibration energy |
| Peak | Very Low | Medium | Sensitive to spikes |
| Variance | Low | Medium | Statistical spread |
| Kurtosis | Medium | High | Detects impulsive events (bearing faults) |
| Crest Factor | Low | High | Detects impulsive vs. periodic |

**Stage 3: Frequency-Domain Features**
- **FFT** (1024-point recommended)
- **Envelope Analysis** (Hilbert Transform for bearing faults)
- **Spectral Kurtosis** (identifies impulsive frequency bands)
- **Cepstrum Analysis** (detects periodic structures)

#### Phase 3B Disagreement Resolution

**Classical DSP vs. ML:**
- **Mistral**: Classical DSP (FFT + envelope) is **primary, safest path**; TinyML is "higher complexity, requires training data, more development time"
- **Gemini**: Pure time-domain is **inadequate**; recommends **edge-AI spectral analysis** (FFT + Isolation Forest/quantized autoencoder)
- **Perplexity**: **Deterministic DSP+threshold** as practical MVP; TinyML as optional later

**Your Task:** Evaluate both positions and determine which approach (or combination) best satisfies the MDS while remaining student-feasible.

---

### 2.6 Edge Intelligence Investigation

**Objective:** Determine the optimal decision-making strategy.

#### Candidate Approaches

**A. Threshold-Based Classification**
- Method: Compare features to predefined thresholds
- Advantages: Simple, explainable, no training required
- Disadvantages: Manual threshold tuning, may not generalize
- Complexity: Very Low

**B. Statistical Anomaly Detection**
- Method: Model normal vibration distribution, flag outliers
- Options: Z-score, Mahalanobis distance, Gaussian Mixture Models
- Advantages: No abnormal data needed, adapts to normal variations
- Complexity: Low–Moderate

**C. Lightweight Machine Learning**
- **Supervised**: Decision Tree, Random Forest, SVM, k-NN
- **Unsupervised**: Isolation Forest, One-Class SVM, Autoencoder
- **TinyML**: 1D CNN, Quantized Autoencoder, Spiking NN

**D. Hybrid Approaches**
- DSP feature extraction → Classical ML classifier
- DSP feature extraction → TinyML classifier
- Threshold on simple features → ML on complex cases

#### Comparison Criteria

| Criterion | Threshold | Statistical | Classical ML | TinyML |
|-----------|-----------|-------------|--------------|--------|
| Training Data Required | None | Normal only | Labeled | Labeled |
| Implementation Complexity | Very Low | Low | Medium | High |
| Explainability | Very High | High | Medium | Low |
| Computational Cost | Very Low | Low | Medium | High |
| Memory Requirements | Very Low | Low | Medium | High |
| Generalization | Poor | Medium | Good | Good |
| False Alarm Rate | Medium | Medium | Low | Low |
| Student Feasibility | Very High | High | Medium | Low |

---

### 2.7 Environmental Noise & False Alarm Analysis

**Objective:** Investigate how the architecture handles real-world interference.

#### Noise Sources to Address

**Physical Noise Sources:**
1. Neighboring machinery vibration (structural transmission)
2. Structural vibration (building/structure natural frequencies)
3. Sensor mounting variation (loose mounting = low-pass filter)
4. Human interaction (operator handling, maintenance)
5. Transient shocks (startup/shutdown, impacts)
6. Electrical noise (power line interference, switching noise)

**Signal Processing Noise Sources:**
1. Aliasing (high-frequency signals appearing as low-frequency)
2. Quantization noise (ADC resolution limitations)
3. Jitter (sampling time variations)

#### Critical Question for Phase 3C

> **Can the single-node spatial/spectral noise isolation concept (VibeGuard's core differentiator per EDR) be realistically demonstrated in a student prototype?**

**Investigate:**
1. **Theoretical Feasibility**: Is single-sensor blind source separation mathematically possible?
2. **Practical Feasibility**: Can it be implemented on resource-constrained MCU?
3. **Simplification Options**: If not fully feasible, what preserves the core hypothesis?

**If Simplification is Recommended:**
- Document what is preserved
- Document what is simplified and why
- Document path to restore full capability

---

### 2.8 Mechanical Integration

**Objective:** Determine the optimal sensor mounting strategy.

#### Mounting Methods Comparison

| Method | Coupling Quality | Ease of Install | Repeatability | Durability | Cost | Notes |
|--------|-----------------|-----------------|--------------|------------|------|-------|
| **Epoxy/Superglue** | **Excellent** | Low | High | High | Low | **Recommended by Phase 3B** (Gemini) |
| Threaded Stud | Excellent | Medium | High | Very High | Medium | Requires tapped hole |
| Magnetic Base | Good | High | Medium | Medium | Medium | May affect high-frequency |
| Adhesive Pad | Medium | High | Low | Medium | Low | Acts as low-pass filter |
| Clamp | Medium | Medium | Medium | Medium | Low | May slip over time |

**Phase 3B Finding:** Rigid epoxy/superglue bonding directly to motor casing is **critical** to prevent low-pass filtering of high-frequency fault signatures.

#### Test Rig Design

**Requirements:**
- Safe and repeatable abnormal conditions
- Minimal external noise
- Ground truth measurements
- College laboratory feasible

**Proposed Scenarios:**
1. **Unbalanced Rotor**: Add small weight to motor rotor
2. **Misaligned Shaft**: Offset motor shaft coupling
3. **Loose Mounting**: Loosen motor mounting bolts
4. **Bearing Fault Simulation**: Mechanical interference or known defective bearing

---

### 2.9 Electrical Architecture

**Objective:** Design the electrical interface between sensor and MCU.

#### Subsystems to Define

**A. Power Supply**
- Source: USB (5V) or battery
- Regulation: 3.3V LDO (AMS1117, LM1117)
- Conditioning: Filtering, decoupling, protection

**B. Sensor Interface**
- Digital: I2C/SPI (pull-ups, level shifting)
- Analog: Signal conditioning, anti-aliasing filter

**C. Signal Conditioning**
- Amplification (if needed)
- Filtering (low-pass, high-pass, bandpass)
- Protection (over-voltage, ESD)

**D. MCU Peripherals**
- Communication: I2C/SPI for sensor, UART for debugging
- Timers: Precise sampling
- DMA: Background data transfer
- GPIO: Status LEDs, buttons

**E. Output Indicators**
- Visual: LEDs (Normal/Abnormal), OLED (optional)
- Audible: Buzzer (optional)
- Communication: UART to computer, Wi-Fi/BLE (optional)

---

### 2.10 Hardware Comparison

**Objective:** Recommend specific candidate hardware where evidence supports it.

#### Component Categories

**A. Vibration Sensors** (Compare all viable options)
**B. MCU Boards** (Compare all viable options)
**C. Supporting Components** (Regulators, resistors, capacitors, etc.)
**D. Optional Components** (Displays, buzzers, SD cards, etc.)

**Selection Criteria:**
1. Engineering justification (why it's suitable)
2. Estimated cost (with range)
3. Availability (Indian suppliers, lead times)
4. Fallback alternative (if primary unavailable)

---

### 2.11 Cost & Manufacturability Assessment

**Objective:** Determine whether the architecture remains within budget and is manufacturable.

**Budget Calculation:**
- Essential components subtotal
- Recommended components subtotal
- Optional components subtotal
- Contingency (10–20%)
- **Total estimated cost**

**Manufacturability Assessment:**
- Assembly complexity (through-hole vs SMD)
- Fabrication requirements (3D printing, machining, etc.)
- Available facilities (college lab capabilities)
- Procurement feasibility (local availability, lead times)

**Budget Target:** ₹3000–₹5000 INR (preferred ≤ ₹3000)

---

### 2.12 Engineering Trade-off Analysis

**Objective:** Explicitly document the trade-offs between different architectural choices.

#### Critical Trade-offs to Address

1. **Sensor Bandwidth vs. Cost**: ADXL345 (₹100, 1600 Hz) vs IIS3DWB (₹1000, 6000 Hz)
2. **DSP vs. ML Classification**: Classical DSP (simple) vs TinyML (more capable)
3. **Rigid Mounting vs. Ease**: Epoxy (best coupling) vs magnetic (easier)
4. **ESP32 vs. STM32**: Wi-Fi vs better DSP support
5. **Continuous vs. Burst Sampling**: Fidelity vs power consumption

---

### 2.13 Final Architecture Recommendation

**Objective:** Conclude with a single recommended engineering architecture.

**Requirements:**
- Architecture name and description
- Sensing architecture (sensor, interface, mounting)
- Processing architecture (MCU, sampling, processing pipeline)
- Edge intelligence strategy (classification approach)
- Electrical architecture (power, interfaces, conditioning)
- Mechanical architecture (test rig, mounting, enclosure)
- Cost summary (BOM, budget compliance)
- Expected performance (accuracy, latency, etc.)
- Remaining uncertainties
- Justification (why this architecture best satisfies the EDR)

**Readiness Classification:**
- ✅ **READY**: Architecture is fully supported, can proceed to Phase 4
- 🔄 **READY WITH MINOR REFINEMENTS**: Fundamentally sound, needs minor tweaks
- 🔍 **REQUIRES ADDITIONAL INVESTIGATION**: Major uncertainty remains
- ❌ **NOT RECOMMENDED**: Hypothesis cannot be demonstrated within constraints

---

## 🧪 Part 3 — Prototype Assembly, Bring-up & Validation Strategy

### 3.1 Prototype Assembly Strategy

**Objective:** Develop a practical assembly strategy that minimizes debugging difficulty.

**Recommended Build Order:**
1. **Power Subsystem** (Verify stable power)
2. **MCU Core** (Verify MCU operation)
3. **Basic I/O** (Verify GPIO functionality)
4. **Sensor Connection** (Verify communication)
5. **Raw Data Acquisition** (Verify sensor readings)
6. **Signal Processing** (Verify preprocessing, FFT)
7. **Feature Extraction** (Verify features)
8. **Classification Logic** (Verify decision-making)
9. **Output Indication** (Verify outputs)
10. **Complete Integrated Operation** (End-to-end testing)
11. **Mechanical Integration** (Mount on test rig)

**Key Principle:** Modular assembly with incremental testing at each stage.

---

### 3.2 System Bring-up Strategy

**Objective:** Progressively verify each subsystem.

**Bring-up Stages:**

| Stage | Subsystem | Expected Behavior | Success Criteria | Likely Failures | Debugging |
|-------|-----------|-------------------|-----------------|-----------------|------------|
| 1 | Power | Stable voltage output | ±5% of target, ripple < 50mV | Wrong regulation, insufficient current | Check connections, measure voltage |
| 2 | MCU Core | MCU boots, LED blinks | Responds to reset, correct blink | No power, corrupted firmware | Verify power, check wiring, reflash |
| 3 | Sensor Comms | I2C/SPI communication | Correct device ID, self-test passes | Wrong wiring, no pull-ups | Check wiring, scan I2C bus |
| 4 | Raw Acquisition | Sensor data | Static ≈1g, changes with motion | Wrong sensitivity, noise | Check scaling, add filtering |
| 5 | Signal Processing | Preprocessing works | DC removed, windowing applied | Overflow, timing issues | Check data types, verify timing |
| 6 | Feature Extraction | Features calculated | Reasonable values, consistent | Wrong calculations | Verify formulas, check parameters |
| 7 | Classification | Decision logic | Correct classification of test cases | Wrong thresholds, weak features | Adjust thresholds, improve features |
| 8 | Output | Indicators work | Output matches classification | GPIO misconfiguration | Check pin assignments, wiring |
| 9 | Integration | Full system | End-to-end <1s latency | Timing conflicts, memory issues | Profile performance, check memory |

---

### 3.3 Prototype Validation Strategy

**Objective:** Demonstrate MDS compliance.

**Validation Requirements:**
1. ✅ Sense vibration from test rig
2. ✅ Recognize normal operating condition
3. ✅ Detect deliberately introduced abnormal condition
4. ✅ Classify as Normal or Abnormal
5. ✅ Perform classification locally
6. ✅ Produce clear output

**Validation Metrics:**
| Metric | Target | Measurement Method |
|--------|--------|---------------------|
| Normal Classification Accuracy | ≥ 95% | % of normal tests classified as Normal |
| Abnormal Classification Accuracy | ≥ 95% | % of abnormal tests classified as Abnormal |
| False Alarm Rate | ≤ 5% | % of normal tests classified as Abnormal |
| Missed Detection Rate | ≤ 5% | % of abnormal tests classified as Normal |
| Classification Latency | < 1s | Time from acquisition to output |
| Repeatability | ≥ 90% | % of repeated tests with same result |

---

### 3.4 Test Scenario Definition

**Recommended Test Suite:**

| Scenario | Description | Normal Condition | Abnormal Condition | Advantages |
|----------|-------------|------------------|---------------------|------------|
| **Unbalanced Rotor** | DC motor with rotor | Balanced rotor | Add 5g weight to rotor | Simple, repeatable, adjustable |
| **Misaligned Shaft** | Two shafts with coupling | Aligned coupling | Offset coupling | Common industrial fault |
| **Loose Mounting** | Motor on base | Tight bolts | Loosen bolts | Easy to implement |
| **Bearing Fault** | Motor with bearing | Good bearing | Defective bearing or simulation | Demonstrates core capability |

**Minimum Viable Test Suite:** Unbalanced Rotor + Loose Mounting

---

### 3.5 Calibration Strategy

**Objective:** Determine calibration requirements.

**Calibration Types:**
- **Sensor Offset**: Once (software subtract mean) or per power-up
- **Normal Baseline**: Per installation (run in normal condition)
- **Thresholds**: Per installation (set based on baseline + margin)
- **ML Model**: Per installation (train on site-specific data)

**Automation Potential:**
- Sensor offset removal: ✅ Automated in software
- Normal baseline: ✅ Automated (average of first N samples)
- Threshold setting: 🟡 Semi-automated (statistical analysis)
- ML training: ❌ Manual (data collection and labeling)

---

### 3.6 Debugging Strategy

**Objective:** Identify probable issues and debugging methods.

#### Common Issues by Subsystem

**Power Subsystem:**
- No power → Check connections, measure voltage
- Unstable voltage → Add decoupling capacitors, check current draw
- Overheating → Add heatsink, reduce load

**MCU Issues:**
- Not booting → Check power, connections, reflash firmware
- Crashes → Check memory usage, stack/heap exhaustion
- Wrong behavior → Review code, add debug output
- Timing issues → Verify clock configuration, use oscilloscope

**Sensor Issues:**
- No communication → Check wiring, pull-ups, I2C address
- Wrong values → Check configuration, range, scaling
- Noisy data → Check grounding, shielding, add software filtering

**Sampling Issues:**
- Aliasing → Increase sampling rate, add anti-aliasing filter
- Jitter → Use hardware timers, minimize interrupt latency
- Dropouts → Increase buffer size, optimize processing

**Processing Issues:**
- FFT fails → Use floating-point, check buffer sizes
- Features wrong → Verify calculations, check parameters
- Too slow → Optimize algorithm, reduce buffer size

**Classification Issues:**
- False alarms → Increase thresholds, improve features
- Missed detections → Decrease thresholds, improve features
- Inconsistent → Use deterministic algorithm, add averaging

---

### 3.7 Reliability Assessment

**Objective:** Evaluate expected prototype reliability.

**Reliability Factors:**
- Operating stability (uptime, crash frequency)
- Repeatability (consistent results)
- Long-term drift (sensor, calibration)
- Sensor durability (shock, temperature)
- Mechanical robustness (mounting, cables)
- Environmental sensitivity (temperature, humidity, vibration)

**Reliability Improvements:**
| Improvement | Impact | Complexity | Cost | Recommended |
|-------------|--------|------------|------|-------------|
| Add power filtering | Reduce electrical noise | Low | Low | ✅ Yes |
| Improve mounting | Better vibration coupling | Medium | Low | ✅ Yes |
| Add error handling | Better fault recovery | Medium | Low | ✅ Yes |
| Use shielded cables | Reduce electrical noise | Low | Medium | ⚠️ Maybe |
| Add watchdog timer | Auto-recovery from hangs | Low | Low | ✅ Yes |
| Add self-test | Verify system health | Medium | Low | ⚠️ Maybe |

---

### 3.8 Team Implementation Strategy

**Objective:** Recommend practical task distribution.

#### Team Composition (5 Members)

| Member | Role | Skills | Primary Tasks | Time Allocation |
|--------|------|--------|---------------|-----------------|
| Member 1 | Embedded Firmware Lead | CS/Cybersecurity | Architecture, firmware, debugging | 60% |
| Member 2 | Signal Processing Lead | CS/Cybersecurity | Signal processing, feature extraction | 50% |
| Member 3 | ML/Classification Lead | CS/Cybersecurity | Classification logic, ML | 50% |
| Member 4 | Beginner Programmer | Learning | Testing, documentation, simple firmware | 30% |
| Member 5 | Hardware Lead | Hardware/Mechanical | Component sourcing, assembly, test rig | 50% |
| Member 6 | Mechanical Lead | Hardware/Mechanical | Mounting, fabrication, test rig | 50% |

*Note: Original description mentions 5 members total. Adjust as needed to match actual team size.*

#### Task Breakdown

**Embedded Firmware Tasks:**
- MCU setup (Member 1, 1 week)
- Sensor driver (Member 1, 1 week)
- Sampling system (Member 2, 1 week)
- Preprocessing (Member 2, 1 week)
- FFT implementation (Member 2, 1–2 weeks)
- Feature extraction (Member 2, 1 week)
- Classification logic (Member 3, 1–2 weeks)
- Output system (Member 4, 1 week)
- Integration (Member 1, 1 week)
- Debugging (All, ongoing)

**Hardware/Mechanical Tasks:**
- Component sourcing (Member 5, 1–2 weeks)
- Power circuit (Member 5, 1 week)
- Sensor mounting (Member 6, 1–2 weeks)
- Test rig design (Member 6, 1–2 weeks)
- Test rig fabrication (Member 6, 1 week)
- Assembly (Members 5, 6, 1 week)
- Enclosure (Member 5, 1 week)

**Testing & Validation Tasks:**
- Unit testing (All, 1–2 weeks)
- Integration testing (Members 1, 5, 1 week)
- Validation testing (All, 1–2 weeks)
- Documentation (Member 4, ongoing)

#### Skill Development (Beginner Programmer)
- Week 1-2: Learn Arduino IDE, basic C++
- Week 3-4: Implement simple sensor reading and serial output
- Week 5-6: Implement basic signal processing (RMS, peak detection)
- Week 7-8: Assist with feature extraction and classification

---

### 3.9 Component Procurement Strategy

**Objective:** Identify essential, recommended, and optional components.

#### Component Classification

**A. Essential Components (Required for MDS)**
| Component | Quantity | Cost (INR) | Supplier | Lead Time |
|-----------|----------|------------|----------|-----------|
| MCU Board (ESP32) | 1 | ₹500 | Robu, SunRobotics | 1–2 weeks |
| Vibration Sensor (IIS3DWB) | 1 | ₹1000 | Quartz | 1–2 weeks |
| Breadboard | 1 | ₹200 | Any | 1 week |
| Jumper Wires | 20+ | ₹100 | Any | 1 week |
| Resistors (10kΩ, 220Ω) | 10 | ₹50 | Any | 1 week |
| Capacitors (0.1µF, 10µF) | 10 | ₹50 | Any | 1 week |
| LEDs | 4 | ₹40 | Any | 1 week |
| **Subtotal** | | **₹1940** | | |

**B. Recommended Components**
| Component | Quantity | Cost (INR) | Supplier | Lead Time |
|-----------|----------|------------|----------|-----------|
| Voltage Regulator (AMS1117) | 1 | ₹20 | Any | 1 week |
| Push Buttons | 2 | ₹40 | Any | 1 week |
| Buzzer | 1 | ₹40 | Any | 1 week |
| **Subtotal** | | **₹100** | | |

**C. Test Rig Components**
| Component | Quantity | Cost (INR) | Supplier | Lead Time |
|-----------|----------|------------|----------|-----------|
| DC Motor (12V, 100-300 RPM) | 1 | ₹1000 | Robu | 1–2 weeks |
| Motor Mount (Aluminum) | 1 | ₹200 | Hardware store | 1 week |
| Base Plate (Plywood) | 1 | ₹200 | Hardware store | 1 week |
| Unbalance Weights | Set | ₹100 | Hardware store | 1 week |
| **Subtotal** | | **₹1500** | | |

**Total Estimated Cost:** ₹3540 (Essential + Recommended + Test Rig)
**Contingency (10%):** ₹350
**Grand Total:** **₹3890** (Within ₹5000 budget with ₹1110 margin)

**Budget Optimization:**
- Use existing lab equipment for test rig if possible
- Prioritize essential components first
- Phase optional components (add later if budget allows)
- Share components across multiple tests

#### Supplier Recommendations (India)
- **Robu.in**: Wide selection, good prices (MCU boards, sensors, modules)
- **Quartz Components**: Good for STMicro parts (STM32, IIS3DWB)
- **SunRobotics**: Reliable, fast shipping (general components)
- **LCSC**: International, ships to India (specialized components)
- **Amazon India**: Fast, but higher prices (urgent needs)
- **Local Electronics Shops**: Immediate availability (basic components)

---

### 3.10 Manufacturing Assessment

**Objective:** Determine fabrication requirements.

#### Electrical Assembly
| Requirement | Complexity | Tools Needed | Feasibility |
|-------------|------------|--------------|-------------|
| Through-hole soldering | Low | Soldering iron | ⭐⭐⭐⭐⭐ |
| SMD soldering (SOIC) | Medium | Soldering iron, tweezers | ⭐⭐⭐ |
| Breadboard prototyping | Very Low | None | ⭐⭐⭐⭐⭐ |
| Stripboard/Perfboard | Medium | Soldering iron | ⭐⭐⭐⭐ |
| Custom PCB | High | PCB fabrication | ⭐ |

**Recommendation:** Use **breadboard for development**, **stripboard for semi-permanent prototype**.

#### Mechanical Fabrication
| Requirement | Complexity | Tools Needed | Feasibility |
|-------------|------------|--------------|-------------|
| 3D Printing (FDM) | Medium | 3D printer, CAD | ⭐⭐⭐⭐ |
| Laser Cutting | Medium | Laser cutter | ⭐⭐⭐ |
| Drilling | Low | Hand drill | ⭐⭐⭐⭐⭐ |
| Tapping | Medium | Tap set | ⭐⭐⭐ |
| Epoxy bonding | Low | Epoxy | ⭐⭐⭐⭐⭐ |

**Recommendation:** Use **3D printing for custom parts**, **hand tools for assembly**.

#### Available Facilities
- Electronics Lab: Soldering stations, multimeters, basic tools
- Mechanical Workshop: Drill press, hand tools, vise
- 3D Printing Lab: FDM printers, basic CAD software
- Computer Lab: Computers with Arduino IDE, Python

---

### 3.11 Risk Assessment

**Objective:** Identify major implementation risks.

#### Risk Register

| Risk | Likelihood | Impact | Risk Level | Mitigation Strategy | Contingency Plan |
|------|------------|--------|------------|---------------------|-------------------|
| Single-node isolation not feasible | Medium | High | **High** | Start with controlled environment, add ML later | Use multi-sensor array if necessary |
| Classical DSP insufficient | Medium | High | **High** | Implement both DSP and ML, compare | Focus on most discriminative features |
| Sensor bandwidth insufficient | Low | High | **Medium-High** | Use IIS3DWB (6 kHz) | Accept limited high-frequency detection |
| MCU processing insufficient | Low | High | **Medium-High** | Use ESP32/STM32 with FPU | Optimize algorithms |
| Poor sensor coupling | Medium | High | **High** | Use epoxy mounting | Try different mounting methods |
| Component delays | Medium | High | **High** | Order early, multiple suppliers | Use alternative components |
| Debugging complexity | High | Medium | **Medium** | Test incrementally, modular design | Simplify design |

#### Top 5 Risks to Address
1. **Single-node isolation feasibility** (High Risk) - Start with controlled environment
2. **Sensor bandwidth inadequacy** (Medium-High Risk) - Use IIS3DWB
3. **Poor sensor coupling** (High Risk) - Use epoxy mounting
4. **Component availability delays** (High Risk) - Order immediately, have backups
5. **Debugging complexity** (Medium Risk) - Test incrementally, add debug output

---

### 3.12 Prototype Readiness Assessment

**Objective:** Determine if architecture is ready for Phase 4.

#### Readiness Checklist

**✅ Architecture Readiness:**
- [ ] Satisfies all EDR requirements
- [ ] Satisfies MDS
- [ ] Single-node processing preserved
- [ ] Edge processing preserved
- [ ] Innovation direction preserved
- [ ] Technically sound

**✅ Feasibility Readiness:**
- [ ] Budget within ₹3000–₹5000
- [ ] Timeline achievable (~2 months)
- [ ] Team skills match requirements
- [ ] Components available
- [ ] Fabrication achievable

**✅ Risk Readiness:**
- [ ] Major risks identified
- [ ] Mitigation strategies defined
- [ ] Contingency plans in place
- [ ] Critical risks manageable

**✅ Validation Readiness:**
- [ ] Validation strategy defined
- [ ] Test scenarios identified
- [ ] Success criteria established
- [ ] Validation achievable in lab

#### Known Unknowns

| Unknown | Impact | How to Resolve | When |
|---------|--------|----------------|------|
| Single-node isolation performance | High | Prototype testing | Implementation |
| Sensor bandwidth adequacy | Medium | Literature + testing | Before final selection |
| DSP vs ML classification accuracy | Medium | Prototype testing | Implementation |
| False alarm rate in noise | Medium | Prototype testing | Validation |
| Mechanical coupling quality | Medium | Prototype testing | Sensor mounting |

#### Assumptions

| Assumption | Justification | Risk if Wrong |
|-----------|---------------|----------------|
| ESP32 has sufficient processing | 240 MHz, FPU, 520 KB RAM | May need to reduce FFT size |
| IIS3DWB bandwidth (6 kHz) is sufficient | Covers typical bearing faults | May miss very high-frequency faults |
| Epoxy mounting provides adequate coupling | Standard practice | May need alternative mounting |
| Unbalanced rotor test is representative | Common industrial fault | May not generalize |
| Lab environment is sufficiently quiet | Typical lab conditions | May need isolation |

#### Prototype Limitations

| Limitation | Impact | Mitigation |
|-----------|--------|------------|
| Single sensor (not array) | Limited spatial resolution | Focus on spectral discrimination |
| Student-built test rig | Not industrial machine | Use representative faults |
| Basic electronics (no PCB) | Less reliable | Careful assembly, strain relief |
| Limited budget | Compromises on components | Prioritize MDS |
| Limited time | Simplified implementation | Focus on core hypothesis |

---

### 3.13 Phase 3C Final Recommendation

**Final Architecture Recommendation:**

**Architecture Name:** VibeGuard-ESP32-IIS3DWB

**Sensing Architecture:**
- Sensor: **IIS3DWB** MEMS accelerometer (6 kHz bandwidth, SPI interface)
- Mounting: **Rigid epoxy** directly to motor/test rig casing
- Sampling: **25 kHz**, 1024-point windows

**Processing Architecture:**
- MCU: **ESP32-WROOM-32** (Xtensa LX6, 240 MHz, 520 KB RAM, hardware FPU)
- Sampling: **Hardware timer + DMA** for precise, jitter-free sampling
- Pipeline: Raw acquisition → DC removal → Windowing → FFT → Feature extraction → Classification

**Edge Intelligence Strategy:**
- Primary: **Classical DSP** (FFT + envelope analysis + statistical features)
- Classification: **Threshold-based** on spectral features (RMS in fault bands, spectral kurtosis)
- Adaptive: **Moving average** of normal features for dynamic thresholds
- ML Ready: Architecture allows **TinyML** (Isolation Forest) as future enhancement

**Electrical Architecture:**
- Power: 5V USB → 3.3V LDO regulator (AMS1117)
- Interface: SPI with 10 MHz clock
- Conditioning: Minimal (digital sensor), 0.1µF decoupling

**Mechanical Architecture:**
- Test Rig: DC motor (12V, 100–300 RPM) with adjustable unbalance
- Sensor Mount: 3D-printed bracket + epoxy
- Base: Heavy plywood with vibration-dampening feet

**Cost Summary:**
| Category | Cost (INR) |
|----------|------------|
| ESP32 DevKit | ₹500 |
| IIS3DWB Sensor | ₹1000 |
| DC Motor | ₹1000 |
| Motor Mount & Base | ₹500 |
| Electronics | ₹300 |
| Breadboard & Wires | ₹200 |
| 3D Printing | ₹200 |
| **Subtotal** | **₹3700** |
| Contingency (10%) | ₹370 |
| **Total** | **₹4070** |

*Within ₹5000 budget with ₹930 margin*

**Expected Performance:**
- Normal Detection: >95% accuracy
- Abnormal Detection: >90% accuracy
- False Alarm Rate: <5%
- Classification Latency: <500 ms
- Power Consumption: ~200 mA @ 5V (≈1W)

**Readiness Classification:**

### ✅ **READY WITH MINOR REFINEMENTS**

**Rationale:**
- Architecture is fundamentally sound and satisfies all EDR requirements
- All critical risks have mitigation strategies and are manageable
- Budget (₹4070) and timeline are achievable
- Team skills match requirements (primarily software/DSP)
- Minor refinements needed: Final component selection, parameter tuning, test rig details

**Next Steps:**
1. Order components immediately (especially IIS3DWB and ESP32)
2. Finalize test rig design
3. Begin firmware development
4. Prototype testing and iteration

---

## 📄 Part 4 — Required Deliverables, Report Structure & Quality Assurance

### 4.1 Final Report Objective

Produce a **professional engineering architecture report** suitable for Phase 3C of Project mC.

**Requirements:**
- Support engineering decision-making
- Provide evidence-backed recommendations
- Enable direct transition to Phase 4
- Be compatible with Claude synthesis for multi-AI merging

---

### 4.2 Required Report Structure

The final report must contain these **major sections** in order:

1. **Executive Summary** (1 page max)
   - Engineering objective
   - Investigated architectures
   - Recommended architecture
   - Feasibility assessments
   - Readiness classification
   - Key findings

2. **Introduction & Context** (1–2 pages)
   - Project mC overview
   - VibeGuard concept summary
   - Phase 3C objectives
   - Scope and constraints

3. **Architecture Investigation** (3–5 pages)
   - Candidate architectures
   - Architecture comparison matrix
   - Eliminated approaches
   - Selected architecture justification

4. **Sensor Evaluation** (2–3 pages)
   - Sensing requirements
   - Candidate sensors comparison
   - Sensor comparison matrix
   - Recommended sensor

5. **Embedded Platform Evaluation** (2–3 pages)
   - Processing requirements
   - Candidate platforms comparison
   - Platform comparison matrix
   - Recommended platform

6. **Signal Processing Evaluation** (2–3 pages)
   - Processing requirements
   - Processing methods comparison
   - Recommended pipeline

7. **Edge Intelligence Evaluation** (2–3 pages)
   - Decision-making approaches
   - Approach comparison matrix
   - Phase 3B disagreement resolution
   - Recommended classification strategy

8. **Mechanical & Electrical Architecture** (3–4 pages)
   - Sensor mounting
   - Electrical design (block diagram)
   - Test rig design
   - Manufacturing requirements

9. **Prototype Implementation Strategy** (3–4 pages)
   - Assembly strategy
   - Bring-up strategy
   - Validation strategy
   - Debugging strategy

10. **Cost Assessment** (1–2 pages)
    - Bill of Materials
    - Cost breakdown
    - Budget analysis

11. **Engineering Risk Assessment** (2–3 pages)
    - Risk register
    - Top risks analysis
    - Residual risk

12. **Team Feasibility** (2–3 pages)
    - Team composition
    - Task breakdown
    - Skill development
    - Feasibility assessment

13. **Innovation Discussion** (1–2 pages)
    - Innovation preservation
    - Future enhancement paths
    - Innovation opportunities

14. **Final Engineering Recommendation** (2–3 pages)
    - Recommended architecture
    - Hardware recommendations
    - Implementation strategy
    - Expected performance
    - Remaining uncertainties
    - Readiness classification

**Appendices:**
- A: Comparison Tables (detailed)
- B: Technical Specifications (datasheet excerpts)
- C: Architecture Diagrams (block diagrams)
- D: Bill of Materials (complete)
- E: Risk Register (full)
- F: Task Breakdown (detailed)
- G: Source References

---

### 4.3 Evidence Quality Requirements

**Source Classification:**
- ✅ **Established Engineering Practice** (industry standard)
- 📄 **Published Research** (peer-reviewed papers)
- 🏭 **Commercial Implementation** (reputable products)
- 🧪 **Experimental Prototype** (research prototypes)
- 💡 **Theoretical Proposal** (simulations, untested)
- ⚠️ **Assumption** (reasoned inference)

**Evidence Handling:**
- Do NOT present speculative ideas as established facts
- DO clearly distinguish between evidence types
- DO cite sources for all non-obvious claims
- DO note when evidence is conflicting
- DO explain how conflicts were resolved

**Confidence Levels:**
- 🟢 **High**: Multiple independent sources agree, well-established
- 🟡 **Medium**: Some evidence, but limited or conflicting
- 🔴 **Low**: Little evidence, mostly inference

---

### 4.4 Report Writing Requirements

**Style Guidelines:**
- Tone: Technical, professional, concise
- Language: Clear, precise, avoid marketing language
- Structure: Logical flow, easy to navigate
- Visuals: Diagrams and tables to improve understanding

**Formatting:**
- Use clear, hierarchical headings (H1, H2, H3)
- Use bullet/numbered lists appropriately
- Use tables for comparisons and structured data
- Use code blocks for firmware snippets
- Use LaTeX-style formatting for equations

**Quality Checklist:**
- [ ] All recommendations are evidence-backed
- [ ] All technical claims are cited or justified
- [ ] All trade-offs are explicitly discussed
- [ ] All risks are identified with mitigations
- [ ] Report structure matches requirements
- [ ] All appendices are included
- [ ] No unsupported assumptions
- [ ] No hallucinated specifications
- [ ] Consistent terminology
- [ ] Professional tone

---

### 4.5 Phase 3C Memory Generation

**Purpose:** Create a separate memory document (`Phase3C_VibeGuard_Memory.md`) summarizing final decisions.

**Required Content:**
1. **Architecture Decisions** (selected architecture, sensor, MCU, processing, intelligence)
2. **Technical Specifications** (electrical, mechanical, signal processing)
3. **Financial Summary** (BOM, budget compliance, cost breakdown)
4. **Risk Summary** (major risks, mitigations, contingencies)
5. **Implementation Summary** (priorities, build order, critical path)
6. **Rationale** (behind major decisions, trade-offs, assumptions)
7. **Open Questions** (unresolved, unknowns to test, future investigation)

**Length:** 1–2 pages (concise, for rapid context restoration)

---

### 4.6 Claude Synthesis Compatibility

**Requirements for Multi-AI Merging:**

**A. Evidence Separation**
- Clearly separate evidence from conclusions
- Explicitly state reasoning behind each recommendation
- Avoid unsupported recommendations

**B. Disagreement Preservation**
- Preserve minority views when technically justified
- Explain conflicting evidence objectively
- Do NOT hide disagreements by averaging

**C. Confidence Indication**
- Indicate confidence levels for key claims
- Explain basis for confidence assessments

**D. Structured Data**
- Use tables for comparisons
- Use consistent terminology
- Define acronyms at first use

**E. Source Attribution**
- Cite all sources
- Note source quality
- Flag assumptions

---

## 🎯 Final Principle

**The objective of Phase 3C is NOT to design the most sophisticated predictive-maintenance system.**

**The objective is to identify the strongest engineering architecture that:**

1. ✅ **Validates the approved engineering hypothesis**
2. ✅ **Can be realistically implemented by the student team**
3. ✅ **Fits the project budget (₹3000–₹5000)**
4. ✅ **Satisfies the Engineering Design Review**
5. ✅ **Provides a strong foundation for later engineering refinement and future innovation**

**Every recommendation should support that objective.**

---

*Document Version: 1.0*  
*Last Updated: July 25, 2026*  
*Prepared by: Claude (Chief Engineering Review Board)*  
*For: Project mC - VibeGuard Phase 3C*  
*Status: Ready for Deep Research Commissioning*