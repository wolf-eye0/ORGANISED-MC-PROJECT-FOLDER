# Phase 3C — TrueMoist Engineering Architecture Definition Report

**Project:** Project mC  
**Concept:** TrueMoist  
**Phase:** 3C — Engineering Architecture Definition  
**Status:** Final Architecture Decision  
**Date:** July 27, 2026  

---

## 📌 Executive Summary

**Final Architecture Decision:** Architecture B — Measurement-Focused Compensated Sensor with **mandatory external ADC (ADS1115)**

**Selected Architecture:**
- **Moisture Sensor:** YL-69 / HL-69 capacitive soil moisture probe (analog output, corrosion-resistant)
- **Temperature Sensor:** DS18B20 digital waterproof thermometer
- **EC/Salinity Strategy:** Direct two-electrode soil EC measurement using galvanic method with controlled calibration
- **ADC:** ADS1115 16-bit external ADC (mandatory - justified by error budget)
- **MCU:** ESP32-WROOM-32 Development Board
- **Compensation Algorithm:** Multivariate polynomial regression (Temperature + EC + Raw Capacitance)
- **Training Method:** Offline training with controlled dataset, coefficients deployed to MCU
- **Validation Method:** Gravimetric analysis (oven-drying at 105°C) as absolute ground truth

**Readiness Classification:** ✅ **Architecture Ready with Mandatory Early Validation**

**Cost:** ₹2,840 (preferred) | ₹3,290 (worst-case) — **within both budget ceilings**

**Primary Justification:** This architecture directly addresses TrueMoist's engineering hypothesis while respecting all project constraints. The external ADC is mandated based on error budget analysis showing ESP32 internal ADC is insufficient for detecting microscopic capacitance variations.

---

## 🎯 Canonical Concept Restatement

TrueMoist is an **affordable embedded intelligent sensing system** designed to improve the **trustworthiness of low-cost soil-moisture measurements** through **local compensation of predictable environmental errors** (temperature, salinity/EC, sensor drift, repeatability limitations).

**Core Engineering Problem:** Low-cost capacitive soil moisture sensors suffer from calibration drift, temperature dependence, salinity/EC interference, and poor long-term accuracy.

**Engineering Hypothesis:** A low-cost embedded system can use environmental measurements and calibration data to compensate for predictable error in an inexpensive soil-moisture sensor, producing estimates that are more stable and closer to gravimetric reference values than uncompensated sensor output under controlled test conditions.

**Minimum Demonstrable Success:** Demonstrate that a low-cost embedded prototype can detect and compensate for controlled sensor drift or environmental influences, producing more stable and repeatable soil moisture estimates than an uncompensated low-cost sensor under equivalent test conditions.

---

## 📚 Evidence Base Summary

**Primary Sources:** Engineering Design Review, Phase 3B Feasibility Report (4 independent research passes), Phase 3A Landscape Report, Phase 2 Patent Report

**Key Findings:**
- Architecture consensus across all reports: Capacitive probe + temperature + EC + multivariate regression + ESP32
- Cost range: ₹1,200-3,000 (lowest/tightest of all 5 concepts)
- Primary risk: Calibration discipline and gravimetric validation rigor
- ADC disagreement: 3 reports assume internal ADC sufficient; 1 (Gemini) mandates external ADC
- **Resolution:** Error budget analysis proves external ADC (ADS1115) is mandatory

---

## 🏗️ Final Architecture: Architecture B — Measurement-Focused Compensated Sensor

### Complete Specification

| Subsystem | Selection | Cost (₹) | Justification |
|----------|----------|----------|---------------|
| **Moisture Sensor** | YL-69 / HL-69 capacitive probe | 200-250 | Low-cost, analog output, corrosion-resistant, affected by temp/EC |
| **Temperature Sensor** | DS18B20 digital waterproof | 150-200 | High accuracy (±0.5°C), digital interface, waterproof |
| **EC Measurement** | Two-electrode galvanic method | 50-100 | Live runtime input, low cost, 316L SS electrodes |
| **ADC** | **ADS1115 16-bit external ADC** | 120-150 | **MANDATORY** - 19× better resolution than ESP32 internal |
| **MCU** | ESP32-WROOM-32 DevKit | 600-800 | FPU, memory, peripherals, team familiarity |
| **Algorithm** | 2nd-order multivariate polynomial regression | - | Captures nonlinear relationships, embedded feasible |
| **Training** | Offline (Python/scikit-learn) | - | Coefficients deployed to MCU PROGMEM |
| **Validation** | Gravimetric analysis (105°C oven-drying, 24h) | - | Absolute ground truth, laboratory standard |
| **Output** | USB serial logging + RGB LED status | 20-50 | Simple, effective, meets MDS |
| **Power** | USB 5V/2A adapter | 150 | 10× margin over 202mA requirement |
| **Mechanical** | Plastic bucket + 3D-printed fixtures | 100-200 | Repeatable probe placement |
| **Total Preferred** | | **₹2,840** | Within ₹3,000 budget |
| **Total Worst-Case** | | **₹3,290** | Within ₹5,000 budget |

### System Block Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     TRUEMOIST ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────────────┐                 │
│  │ YL-69   │  │ DS18B20 │  │ EC Electrodes    │                 │
│  │Moisture │  │  Temp   │  │ (316L SS)        │                 │
│  └────┬────┘  └────┬────┘  └─────────┬───────┘                 │
│       │             │                │                         │
│       └─────────────┼────────────────┘                         │
│                     │                                      │
│                     ▼                                      │
│              ┌─────────────────┐                               │
│              │  ADS1115        │                               │
│              │  16-bit ADC     │                               │
│              └─────────┬───────┘                               │
│                        │                                        │
│                        ▼                                        │
│              ┌─────────────────────────┐                       │
│              │      ESP32-WROOM-32      │                       │
│              │  - Xtensa LX6 (240 MHz)  │                       │
│              │  - 4MB Flash, 520KB SRAM│                       │
│              │  - FPU, I2C, 1-Wire      │                       │
│              └─────────────────────────┘                       │
│                            │                                   │
│         ┌──────────────────┼──────────────────┐              │
│         ▼                  ▼                  ▼              │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐     │
│  │ USB Serial   │   │ RGB LED     │   │ Power 5V/2A │     │
│  │ (CSV Logging)│   │ (Status)    │   │ Adapter     │     │
│  └──────────────┘   └──────────────┘   └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Key Technical Decisions

### 1. ADC Selection: ADS1115 is MANDATORY

**Error Budget Analysis:**
- YL-69 signal variations: ~10-50mV (temperature/EC-induced drift)
- Required resolution: <1mV to detect 0.1% moisture change

**Comparison:**
| Parameter | ESP32 Internal | ADS1115 External | Improvement |
|-----------|----------------|------------------|-------------|
| LSB @ 3.3V | 0.806 mV | 0.0625 mV | 12.9× |
| LSB @ 1V | N/A | 0.0156 mV | N/A |
| Total Error | ±6.4 mV | ±0.33 mV | **19× better** |
| Signal-to-Noise (10mV signal) | 1.56:1 | 30:1 | **19× better** |

**Conclusion:** ESP32 internal ADC cannot reliably detect 10mV signals with 6.4mV of error. **ADS1115 is mandatory.**

### 2. EC Measurement: Direct Two-Electrode Galvanic Method

**Why:**
- Live runtime input enables real-time compensation
- Low cost (₹50-100 for electrodes + resistors)
- Demonstrates full hypothesis (temp + EC compensation)
- Suitable for controlled lab conditions

**Circuit:** Square wave excitation (1kHz) via ESP32 GPIO, current limiting resistors (1kΩ), ADS1115 measures voltage difference.

### 3. MCU: ESP32-WROOM-32

**Why:**
- FPU for efficient polynomial evaluation
- 520KB SRAM, 4MB Flash (ample margin)
- I2C, 1-Wire, multiple GPIO
- Arduino IDE support
- Team familiarity
- Cost: ₹600-800

**Resource Usage:**
- Flash: ~251KB (6% of 4MB)
- SRAM: ~12KB (2.3% of 520KB)
- **Margins: 94% Flash, 97.7% SRAM**

### 4. Algorithm: 2nd-Order Multivariate Polynomial Regression

**Model:** VWC_comp = a + b·Raw + c·Temp + d·EC + e·Raw² + f·Temp² + g·EC² + h·Raw·Temp + i·Raw·EC + j·Temp·EC

**Why:**
- Interpretable coefficients
- Captures nonlinear relationships
- Dataset: 50-100 samples sufficient
- Embedded: <1ms execution, ~140 bytes
- Phase 3B consensus: 3 of 4 reports

---

## 📊 Calibration Dataset Design

**Soil Type:** Sandy Loam (single homogeneous, per PDR-049)

**Levels:**
- Moisture: 5 levels (5%, 15%, 25%, 35%, 45% VWC)
- Temperature: 3 levels (15°C, 25°C, 35°C)
- EC: 3 levels (0.5, 2.0, 5.0 mS/cm)

**Total:** 45 conditions × 3 replicates = **135 samples**

**Validation Split:** 100 training (74%), 35 validation (26%)

**Data Leakage Prevention:** All readings from same physical soil condition = 1 data point (average before adding to dataset)

---

## ⚖️ Gravimetric Ground Truth

**Primary Method:** Laboratory oven-drying at 105°C for 24 hours
- **Accuracy:** ±1-1.5% VWC
- **Procedure:** Weigh wet soil → dry at 105°C × 24h → weigh dry soil → calculate VWC

**Fallback:** Food dehydrator (₹2,500, ±1% VWC, 24-48 hours)

---

## 🎯 Validation Metrics

| Metric | Target (Good) | Minimum (Acceptable) | Failure |
|--------|----------------|----------------------|---------|
| **MAE** (Primary) | <1.5% VWC | <2.0% VWC | ≥2.0% VWC |
| **RMSE** (Secondary) | <2.0% VWC | <2.5% VWC | ≥2.5% VWC |
| **Improvement Ratio** | >1.5× | >1.2× | ≤1.2× |
| **R²** | >0.95 | >0.90 | ≤0.90 |

**MDS Success:** Improvement Ratio > 1.2× **AND** MAE_compensated < MAE_uncompensated

---

## 🧪 Test Matrix (10 Tests)

### Critical Tests (Must Pass)
| # | Test | Purpose | Pass Criteria | Week |
|---|------|---------|---------------|------|
| 1 | Raw Sensor Repeatability | Verify YL-69 stability | σ < 50 counts | 1 |
| 4 | ADC Validation | Internal vs. external ADC | External error <1mV | **1** |
| 5 | Gravimetric Accuracy | Validate reference method | σ < 0.5% VWC | 1 |
| 7 | Model Training | Train and validate algorithm | Improvement >1.2× | 5 |
| 8 | Embedded Deployment | Verify MCU implementation | Max diff <0.1% VWC | 6 |
| 9 | Comparative Demo | Final MDS demonstration | Compensated closer to gravimetric | 7 |

### Secondary Tests
| # | Test | Purpose | Pass Criteria | Week |
|---|------|---------|---------------|------|
| 2 | Temperature Sensitivity | Measure temp effect | >0.5% VWC/10°C | 2-3 |
| 3 | EC Sensitivity | Measure EC effect | >1% VWC/2 mS/cm | 2-3 |
| 6 | Full Dataset Collection | Generate calibration data | ≥130 samples | 4 |
| 10 | Repeatability | Verify consistent performance | Ratio change <10% | 8 |

---

## ⚡ Electrical Architecture

**Power Budget:** ~202mA active, ~101mA idle → **1.0W total**
- USB 5V/2A adapter provides **10× margin**

**Wiring:**
- ESP32 ↔ ADS1115: I2C (SCL: GPIO21, SDA: GPIO22)
- ADS1115 A0: YL-69 signal
- ADS1115 A1: GND (reference)
- ADS1115 A2-A3: EC electrodes (differential)
- ESP32 GPIO19: DS18B20 (1-Wire, 4.7kΩ pull-up)
- ESP32 GPIO5/16/17: RGB LED (common cathode)

---

## 💰 Costed BOM

### Preferred: ₹2,840
| Component | Qty | Price (₹) | Total (₹) |
|-----------|-----|-----------|-----------|
| ESP32-WROOM-32 DevKit | 1 | 700 | 700 |
| ADS1115 16-bit ADC | 1 | 150 | 150 |
| YL-69 Capacitive Probe | 1 | 220 | 220 |
| DS18B20 Temperature | 1 | 180 | 180 |
| 316L SS Electrodes | 2 | 25 | 50 |
| Resistors (1kΩ, 220Ω) | 5 | 5-10 | 35 |
| Breadboard | 1 | 150 | 150 |
| Jumper Wires | 40 | 100 | 100 |
| RGB LED | 1 | 20 | 20 |
| Plastic Bucket | 1 | 100 | 100 |
| Aluminum Containers (10) | 10 | 20 | 200 |
| USB Adapter 5V/2A | 1 | 150 | 150 |
| Perfboard | 1 | 50 | 50 |
| Soldering Kit | 1 | 300 | 300 |
| Contingency (10%) | - | - | 284 |
| **Total** | | | **₹2,840** |

### Worst-Case: ₹3,290
- Same components at higher prices + contingency
- **Still within ₹5,000 maximum** ✅

---

## ⚠️ Risk Register (Top 5)

| ID | Risk | Likelihood | Impact | Mitigation | Kill Criterion |
|----|------|------------|--------|------------|----------------|
| R1 | ADC Insufficiency | Medium | High | Week 1 validation | Internal error >5mV |
| R9 | **No Measurable Improvement** | Medium | **Critical** | Linear → Polynomial | Ratio ≤1.1× |
| R6 | Gravimetric Error | Low | High | 3 samples/condition | Uncertainty >2% |
| R8 | Model Overfitting | Medium | Medium | Validation set | MAE >2.5% |
| R4 | Moisture-EC Confounding | Medium | Medium | Interaction terms | Correlation >0.9 |

**Total Risks Identified:** 13

---

## 👥 Team Allocation

| Member | Role | Primary Responsibilities | Critical Path |
|--------|------|-------------------------|---------------|
| 1 | Embedded Integration Lead | MCU firmware, sensor interfaces, polynomial eval | ✅ Yes |
| 2 | Data & Compensation Lead | Dataset design, model training, validation | ✅ Yes |
| 3 | Hardware & Validation Lead | AFE, soldering, sensor char., soil rig, gravimetric | ✅ Yes |
| 4 | Learner | Logging, CSV formatting, test scripts | ❌ No |
| 5 | Documentation & Support | BOM, records, photos, presentation | ❌ No |

**Critical Path Protection:** No critical work assigned exclusively to Member 4 or 5.

---

## 📅 Eight-Week Roadmap

| Week | Tasks | Deliverables | Gates |
|------|-------|-------------|-------|
| 1 | Component verification, ADC validation, solder AFE, procurement | ADC decision, baseline data | ✅ **M1** |
| 2 | Test rig construction, EC circuit, breadboard MCU, firmware | Functional test rig | |
| 3 | Pilot dataset, temp/EC sensitivity tests | Pilot data | |
| 4 | Full calibration dataset (45×3 conditions) | 135 samples | ✅ **M4** |
| 5 | Model training (Python), offline validation | Trained model, metrics | ✅ **M5** |
| 6 | Embedded deployment, MCU validation | Firmware with compensation | ✅ **M6** |
| 7 | Comparative testing, disturbance tests | Improvement demo, validation | ✅ **M7** |
| 8 | Repeatability testing, documentation, demo | Final report, presentation | ✅ **M8** |

---

## ✅ Phase 4 Readiness

**Classification:** ✅ **Architecture Ready with Mandatory Early Validation**

**All Phase 4 Inputs Ready:**
- ✅ Final System Block Diagram
- ✅ Selected Sensing Architecture
- ✅ ADC Decision (ADS1115 mandatory)
- ✅ MCU Selection (ESP32-WROOM-32)
- ✅ Compensation Algorithm (2nd-order polynomial)
- ✅ Calibration Dataset Design (135 samples)
- ✅ Gravimetric Procedure (105°C oven-drying)
- ✅ Validation Metrics (MAE, Improvement Ratio)
- ✅ Test Matrix (10 tests)
- ✅ Electrical/Power Architecture
- ✅ User Interface (USB + RGB LED)
- ✅ Costed BOM (₹2,840-3,290)
- ✅ Resource Budget (6% Flash, 2.3% SRAM)
- ✅ Risk Register (13 risks)
- ✅ Rejected Alternatives (7 decisions)
- ✅ Patent/Innovation Analysis
- ✅ Team Allocation (5 members)
- ✅ Eight-Week Roadmap (8 milestones)

**Mandatory Early Validation (Week 1):**
1. ADC validation (internal vs. external)
2. Sensor characterization (repeatability, noise)
3. Soldered AFE validation

**If Week 1 fails:** Fallback to Architecture A with controlled EC. Still meets MDS.

---

## 📋 Decision Register Updates

**New Decisions (11):**
- PDR-058: Architecture B selected
- PDR-059: YL-69 moisture sensor
- PDR-060: DS18B20 temperature sensor
- PDR-061: Direct two-electrode EC measurement
- PDR-062: **ADS1115 mandatory**
- PDR-063: ESP32-WROOM-32 MCU
- PDR-064: 2nd-order polynomial regression
- PDR-065: Single soil type (Sandy Loam)
- PDR-066: Gravimetric validation method
- PDR-067: Success metrics (Improvement Ratio >1.2×)
- PDR-068: Budget compliance (₹2,840-3,290)

**Existing Decisions Updated:**
- PDR-031: Accepted (Multivariate polynomial regression)
- PDR-032: **Accepted (Mandate ADS1115)**
- PDR-045: Accepted (Confine IP to software)
- PDR-048: Accepted (Gravimetric validation)
- PDR-049: Accepted (Single-soil limit)
- PDR-050: Accepted (Solder AFE early)

---

## 🧠 Phase 3C Memory

```yaml
architecture:
  primary: "Architecture B - Measurement-Focused Compensated Sensor"
  fallback: "Architecture A (with EC)"
  readiness: "Architecture Ready with Mandatory Early Validation"

sensing:
  moisture: "YL-69 / HL-69"
  temperature: "DS18B20"
  ec: "Direct two-electrode galvanic"

adc: "ADS1115 (MANDATORY)"
mcu: "ESP32-WROOM-32"
algorithm: "2nd-order multivariate polynomial regression"

calibration:
  soil: "Sandy Loam"
  samples: 135
  levels: "5 moisture × 3 temp × 3 EC"

gravimetric: "105°C oven-drying, 24 hours"
validation_metrics: "MAE (primary), Improvement Ratio >1.2×"

cost:
  preferred: 2840
  worst_case: 3290
  currency: "INR"

risks: 13
team: 5
 timeline: "8 weeks"

next_phase: "Phase 4 - Prototype Engineering"
```

---

## 🏁 Conclusion

**Phase 3C for TrueMoist is COMPLETE.**

This report provides a **complete, evidence-backed, buildable architecture** that:
- Directly addresses the engineering hypothesis
- Respects all project constraints (budget, timeline, team, local processing)
- Resolves all major technical disagreements
- Provides a complete blueprint for Phase 4
- Identifies and mitigates all significant risks

**The architecture is ready for Phase 4 Prototype Engineering.**

**Next Step:** Begin Phase 4 with Week 1 mandatory early validation.

---

*Document Version: 1.0 | Date: July 27, 2026 | Status: Final*