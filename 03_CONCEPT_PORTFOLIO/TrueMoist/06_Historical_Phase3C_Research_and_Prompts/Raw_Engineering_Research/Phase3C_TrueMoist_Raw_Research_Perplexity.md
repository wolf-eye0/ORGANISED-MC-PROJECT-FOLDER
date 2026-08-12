# TrueMoist Phase 3C Engineering Architecture Definition[^1][^2][^3]

## 1. Executive Summary

The recommended TrueMoist MVP architecture is a **measurement‑focused compensated sensor** built around a low‑cost capacitive soil‑moisture probe, a waterproof DS18B20 soil‑temperature sensor, controlled salinity conditions (calibration‑time only, no live soil‑EC sensing), and an ESP32‑class MCU using its internal ADC plus a carefully designed analog front end and multivariate linear/piecewise regression for local compensation. Raw probe voltage and temperature are logged via USB serial into CSV; gravimetric oven‑drying provides ground truth; compensation coefficients are trained offline and flashed into the MCU for on‑device inference. This architecture keeps total hardware cost within ₹2,500–₹3,500, fits easily in a two‑month student schedule, and provides a clear experimental chain to show statistically significant reduction in MAE/RMSE against uncompensated readings under controlled temperature and salinity disturbances.[^2][^3][^4][^5][^1]

Feasibility is high: all core components (capacitive probe, DS18B20, ESP32, basic lab scale and drying method) are widely available in India at student‑friendly prices; firmware and data‑analysis workload match the stated CS/cybersecurity team skills; and risks concentrate in calibration discipline and test‑rig repeatability rather than exotic hardware or TinyML complexity. The major unresolved issue is whether an external 16‑bit ADC (e.g., ADS1115) yields enough incremental accuracy to justify added cost and complexity; the architecture treats it as an **optional Week‑1/2 comparison**, not a mandatory component. Overall readiness is rated **“Architecture Ready with Mandatory Early Validation”**: the system is buildable within constraints, but success depends on executing the calibration dataset and gravimetric workflow with care in Weeks 3–5.[^3][^6][^5][^2]

## 2. Canonical Concept Restatement

TrueMoist is an affordable embedded intelligent sensing system whose goal is to **improve the trustworthiness of low‑cost soil‑moisture measurements** by compensating predictable measurement error from environmental influences (temperature, salinity/electrical conductivity, sensor drift, nonlinearity, repeatability limits) using local embedded processing. It is explicitly *not* a generic irrigation controller, premium laboratory‑grade sensor, universal calibration‑free probe, cloud analytics platform, or full precision‑agriculture system; its innovation lies in low‑cost compensation of cheap sensors under controlled conditions.[^5][^1][^3]

The project operates under frozen constraints: preferred prototype budget ≤₹3,000 and absolute maximum ₹5,000; approximately two months of development; a five‑member team with three strong CS/cybersecurity students, one learner, and one presenter/support member; off‑the‑shelf or easily fabricated components; local embedded processing without continuous cloud; and a single homogeneous soil type for MVP calibration. Gravimetric oven‑drying is required as physical ground truth; architecture must remain explainable, reproducible, and suitable for Arduino‑class tooling (Arduino IDE, ESP32/STM32 support).[^6][^1][^3]

## 3. Engineering Hypothesis and Minimum Demonstrable Success

The standing engineering hypothesis is: **a low‑cost embedded system can use environmental measurements and calibration data to compensate for predictable error in an inexpensive soil‑moisture sensor, producing estimates that are more stable and closer to gravimetric reference values than uncompensated sensor output under controlled test conditions**.[^1][^3][^5]

Minimum demonstrable success requires that the prototype can: (1) acquire raw data from a low‑cost soil‑moisture sensor; (2) measure or rigorously represent compensation variables, especially temperature and salinity/electrical‑conductivity influence; (3) produce an uncompensated moisture estimate; (4) compute a compensated estimate locally on embedded hardware; (5) compare both against gravimetric reference; (6) show measurable improvement in at least one predefined metric (e.g., MAE, RMSE, R², salinity sensitivity) under controlled disturbances; and (7) operate without continuous cloud processing.[^2][^3][^1]

## 4. Evidence Base and Source Quality

This architecture draws primarily on the **Engineering Design Review**, Phase 3B feasibility synthesis and memory, and the Phase 3C TrueMoist SOP as authoritative project specifications. External technical evidence focuses on low‑cost capacitive soil‑moisture sensor behaviour (temperature and salinity effects, nonlinearity, drift), agricultural sensing calibration studies, DS18B20 soil‑temperature performance, and ADC/analog‑front‑end characteristics for such sensors. Peer‑reviewed articles on capacitive soil moisture sensors show that soil moisture readings are strongly affected by soil texture, temperature, and electrical conductivity, and that calibration under specific conditions can achieve R²≈0.96–0.99 with RMSE on the order of 0.01–0.02 VWC when the analog front end and probe geometry are controlled.[^7][^8][^4][^9][^10][^11][^3][^6][^5][^1][^2]

Evidence on temperature and salinity effects indicates that capacitive sensor readings change significantly with temperature and ionic concentration, with some commercial sensors exhibiting problematic sensitivity at high salinity or temperature. DS18B20‑based soil‑temperature probes are widely used in agricultural monitoring and exhibit ±0.5°C accuracy in the −10–85°C range, sufficient for compensation modelling. The evidence base on external ADCs (e.g., ADS1115) versus MCU internal ADCs suggests that many low‑cost moisture systems achieve acceptable performance with 10‑ or 12‑bit ADCs when sensor‑to‑sensor variability and soil heterogeneity dominate error, while higher‑resolution ADCs are beneficial mainly when sensor and analog circuitry are well‑designed and temperature/salinity compensation aims for research‑grade precision.[^8][^4][^9][^11][^5]

Limitations: (1) published studies often use more controlled lab setups than a student test rig; (2) many designs target volumetric water content (VWC) while TrueMoist’s MVP can remain gravimetric; (3) few open studies explicitly combine low‑cost capacitive probes with multi‑variable compensation on ESP32‑class boards; and (4) patent‑landscape analyses indicate that hardware compensation circuits are heavily patented, while software‑side adaptive calibration remains the cleanest innovation space.[^12][^5]

## 5. Candidate Architectures

Phase 3C defines four baseline architecture families plus optional variants.[^3]

### 5.1 Architecture A — Minimal Compensation Demonstrator

Architecture A uses a low‑cost capacitive moisture probe, a temperature sensor, controlled salinity conditions (pre‑prepared soil EC levels), the MCU’s internal ADC, static or multivariate regression, and USB serial output for logging. It demonstrates that adding temperature as an input and calibrating under known salinity conditions improves trustworthiness compared with raw readings, without live EC measurement or adaptive recalibration.[^2][^3]

### 5.2 Architecture B — Measurement‑Focused Compensated Sensor

Architecture B extends A with direct EC measurement (soil or solution), an external ADC (e.g., ADS1115), and multivariate compensation, plus serial logging or simple local display. It aims to separate temperature and salinity contributions to error and potentially achieve better calibration across controlled salinity regimes, at the cost of additional circuitry and complexity.[^3][^2]

### 5.3 Architecture C — Adaptive Embedded Calibration System

Architecture C adds adaptive or recursive compensation and on‑device recalibration logic using temperature and EC inputs, possibly with an external ADC if justified. The MCU updates coefficients over time based on observed drift and gravimetric feedback; local outputs and logging show how compensation improves as the system learns.[^12][^3]

### 5.4 Architecture D — Offline Training / Embedded Inference

Architecture D emphasises controlled dataset generation, offline model training (in Python/R or similar), deployment of coefficients or a lightweight model to the MCU, and fully local embedded inference without runtime cloud dependency. It can be layered over A–C: raw data and reference values are collected, the model is trained off‑device, then inference runs on the microcontroller with fixed coefficients.[^12][^3]

### 5.5 Additional Variants

Phase 3B evidence and patent findings highlight that the most defensible innovation lies in **software‑side, event‑driven calibration and compensation** rather than custom hardware probes; therefore, adaptive calibration (C) and offline‑trained models (D) form the important upgrade path. However, given the two‑month timeline and budget, the primary MVP architecture must remain closer to **A/B+D**: a measurement‑focused compensated sensor with offline‑trained multivariate regression, with adaptive recalibration treated as a future upgrade.[^6][^12][^2]

## 6. Comparative Decision Matrix

The table below qualitatively scores the four baseline families under project constraints, assuming use of commodity capacitive probes and an ESP32‑class MCU.[^5][^2][^3]

| Criterion | Arch A Minimal | Arch B Meas‑focused | Arch C Adaptive | Arch D Offline Train/Inference |
|----------|----------------|---------------------|-----------------|------------------------------|
| Hypothesis validation | Medium (temp only, controlled salinity) | High (explicit temp+EC effects) | High (drift compensation) | High (strong separation of training vs inference) |
| Accuracy improvement potential | Medium | High | High | High (depends on model) |
| Cost | Very low | Low–medium (ADC, EC circuitry) | Medium–high | Low (mostly software) |
| Complexity | Low | Medium | High | Medium |
| Buildability (2 months, student team) | High | High | Medium–low | High |
| Team fit (CS/cyber) | High | High | Medium (more firmware state, adaptive logic) | High |
| Validation clarity | High | High | Medium (non‑stationary behaviour) | High |
| Reproducibility | High | High | Medium | High |
| Risk | Low–medium (calibration discipline) | Medium (EC measurement reliability) | High (model stability, overfitting) | Medium (offline modelling workload) |
| Innovation preservation | Medium (compensated probe) | High (multi‑variable correction chain) | High (adaptive calibration concept) | High (edge inference + event‑driven calibration) |

Overall, the simplest technically defensible architecture that still preserves TrueMoist’s innovation is a **hybrid of Architecture B (measurement‑focused compensated sensor) plus Architecture D (offline training/embedded inference)**, with adaptive calibration (C) defined as an optional Phase‑4+ direction.[^12][^2]

## 7. Final Architecture Selection

### 7.1 Primary Architecture

The selected primary architecture is:

> **Measurement‑Focused Compensated Sensor with Offline‑Trained Multivariate Regression (Architecture B + D)**.

Key reasons:

- It directly measures the main compensation variable (temperature) and represents salinity via controlled calibration salinity levels rather than fragile live soil‑EC circuitry, aligning with the EDR’s focus on trustworthiness under controlled conditions rather than universal field robustness.[^4][^11][^1][^3]
- It supports gravimetric ground truth and clean comparison of uncompensated vs compensated estimates using simple linear/piecewise multivariate regression, which is interpretable, buildable, and well‑supported by agricultural moisture sensor calibration literature.[^13][^9][^5]
- It avoids over‑ambitious adaptive calibration and TinyML in the MVP, reducing risk while leaving room for future innovation in self‑calibrating algorithms once field data are available.[^2][^12]
- Hardware cost and complexity stay within budget: a single ESP32‑DevKitC‑style board, one or two low‑cost capacitive probes, one DS18B20 soil‑temperature sensor, simple analog front end, and optional ADS1115 for early comparison can be sourced in India for well under ₹3,500.[^8][^5][^2]

### 7.2 Fallback Architecture

The fallback architecture, used only if EC practicalities prove unmanageable or budget/time are tighter than expected, is:

> **Minimal Compensation Demonstrator with Offline‑Trained Regression (Architecture A + D)**.

This variant measures soil temperature and uses **controlled salinity conditions** (prepared soil batches with known salt levels) without any live EC measurement or external ADC, focusing on showing improvement under temperature disturbance alone. It preserves the hypothesis (environmental compensation improves trustworthiness) while sacrificing explicit EC modelling.[^4][^5][^3]

## 8. Final System Block Diagram

Textual block diagram of the selected architecture:

1. **Sensing subsystem**
   - Capacitive soil‑moisture probe (analog voltage output, powered at 3.3–5 V via MCU).[^13][^5]
   - Waterproof DS18B20 soil‑temperature probe inserted near the moisture sensor.[^8][^5]
   - Optional EC test electrodes in calibration beakers (not connected for runtime field use in MVP).[^14][^4]

2. **Analog front end and ADC**
   - Simple RC low‑pass filter and buffer (op‑amp voltage follower or high‑input‑impedance stage) between probe output and MCU ADC to reduce noise and loading.[^13][^5]
   - ESP32 internal 12‑bit ADC channel reading probe voltage; optional ADS1115 external 16‑bit ADC on I²C for Week‑1 comparative tests.[^5][^2]

3. **MCU and processing**
   - ESP32‑DevKitC (ESP32‑WROOM‑32) running Arduino‑compatible firmware.[^6][^2]
   - Tasks: sensor reading, basic filtering/averaging, application of regression coefficients, USB serial output, optional SD‑card logging.[^3][^13]

4. **Calibration and compensation model**
   - Offline Python/R script fits multivariate linear or piecewise regression model mapping raw probe voltage and temperature (plus known calibration salinity level) to gravimetric moisture.[^9][^5]
   - Coefficients stored in MCU flash and applied per sample.

5. **Gravimetric reference workflow**
   - Soil samples prepared in containers; wet mass measured; dried in oven/dehydrator to near‑constant mass; dry mass measured; gravimetric water content computed.[^9][^5]

6. **Data logging and interface**
   - USB serial prints CSV lines containing sample ID, raw readings, compensation variables, reference moisture, and compensated estimate.[^3]
   - Optional OLED display showing raw vs compensated vs reference for live demos.

7. **Power subsystem**
   - USB‑powered ESP32 board with local decoupling capacitors, powering sensors from regulated 3.3/5 V.[^5]

## 9. Sensing Subsystem

### 9.1 Moisture Sensor Choice

**Operating principle:** Capacitive soil‑moisture sensors use a fringing electric field between PCB or electrode plates; soil acts as the dielectric, and water content increases effective permittivity, causing capacitance and, via the analog front end, voltage or frequency to change. Cheap “capacitive soil moisture sensor v1.2”‑type modules present an analog voltage output or PWM representing soil moisture and are widely available in India for ₹150–₹300.[^15][^10][^13][^5]

**Key characteristics from literature and modules:**

- Output type: analog voltage typically 0–3 V or 0–5 V, suitable for MCU ADC.[^5]
- Sensitivity: strongly correlated with volumetric water content (VWC) in calibrated setups (R²>0.96 reported for clay soils).[^5]
- Repeatability & sensor‑to‑sensor variability: coefficients of variation under 5–10% across identical sensors; drift over time due to coating, temperature, and salinity effects.[^9][^5]
- Nonlinearity: capacitance vs VWC often quadratic; many studies fit second‑order polynomials or linear segments.[^10][^5]
- Drift and aging: low‑cost probes may drift days‑to‑weeks; protective coatings (acrylic, solder mask) can reduce salinity‑induced changes.[^11][^5]
- Corrosion risk: capacitive designs avoid direct DC between metal electrodes, giving far lower corrosion than resistive two‑probe sensors, which suffer severe electrolysis and rapid degradation.[^16][^13]
- Temperature and salinity sensitivity: dielectric properties of soil and pore water are temperature‑dependent; salinity affects conductivity and permittivity; capacitive sensors show measurable error under varying temperature and EC.[^7][^11][^4][^5]

**Suitability for compensation experiments:**

Published work on low‑cost capacitive probes shows they can be calibrated to provide reasonably accurate moisture estimates within a specific soil type when temperature and salinity are controlled or modelled, but their readings are noticeably influenced by these factors—precisely the behaviour TrueMoist aims to understand and correct. Therefore, a commodity PCB‑based capacitive probe is **appropriate for compensation experiments**: it is cheap, accessible, raw analog outputs can be measured, and its imperfections (temperature and salinity sensitivity, drift, nonlinearity) offer a meaningful error surface for regression and compensation.[^11][^7][^4][^9][^5]

Resistive sensors are rejected as primary probes due to severe corrosion, electrode polarization, strong dependence on ionic composition, and poor repeatability over time; they are suitable only as a comparison baseline if time permits.[^16][^13][^5]

### 9.2 Temperature Sensing Strategy

TrueMoist must resolve whether to measure soil temperature, ambient temperature, or both. Literature indicates that **soil temperature at sensor depth** directly affects dielectric properties and moisture sensor readings; ambient air can differ significantly, especially under greenhouse or field conditions. Therefore, the preferred strategy is **soil temperature measurement** at approximately the same depth and location as the moisture probe, with ambient temperature optionally recorded via MCU or external sensors if easily available.[^7][^9][^5]

**Sensor options:**

- **DS18B20 waterproof probe**: digital 1‑Wire sensor, −55 to +125°C range, ±0.5°C accuracy (−10–85°C), 0.0625°C resolution, waterproof encapsulation suitable for soil insertion.[^8][^5]
- Analog thermistors: cheap, require ADC readout and calibration curves; output nonlinear; need careful waterproofing and series resistors.[^9]
- TMP36‑class analog sensors: moderate accuracy, but not designed for direct burial; better for ambient measurement.[^9]
- BME280 environmental sensor: measures temperature, humidity, pressure; not waterproof for soil; more suitable for ambient conditions in enclosures.[^9]

Given TrueMoist’s emphasis on soil temperature, waterproof digital DS18B20 probes specifically marketed for soil and liquid monitoring in agriculture are ideal: they provide sufficient accuracy, simple digital interface, and are widely used in soil‑moisture studies, including low‑cost capacitive sensor calibration work.[^8][^5]

**Preferred and fallback:**

- **Preferred:** Waterproof DS18B20 soil‑temperature probe, inserted near the moisture probe.
- **Fallback:** Ambient temperature measurement via DS18B20 in air or BME280 if procurement for soil probes fails, plus assumption that soil and air temperature differences are modest in indoor test rigs; this fallback should be documented as increasing uncertainty in compensation rates.[^3][^9]

## 10. Analog Front End and ADC Decision

### 10.1 Internal vs External ADC

ESP32 internal ADCs provide nominal 12‑bit resolution, but practical effective number of bits and linearity are lower; they exhibit nonlinearity and require calibration, and their performance can be affected by input impedance and noise. External ADCs like the ADS1115 offer 16‑bit resolution, programmable gain, high input impedance, and good linearity over low‑frequency signals typical of moisture probes.[^2][^5]

Error sources in the TrueMoist chain include:

- Sensor variability and nonlinearity (dominant).[^9][^5]
- Soil heterogeneity and packing effects (dominant).[^5][^9]
- Temperature and salinity cross‑effects (modelled via regression).[^4][^11][^7][^5]
- ADC quantization, nonlinearity, and noise (smaller if analog front end is clean).[^9][^5]

Studies on low‑cost capacitive sensors achieve strong calibration (R²>0.96, RMSE≈0.014 VWC) using 10‑ or 12‑bit ADCs with well‑designed analog conditioning and stable reference voltages. Many errors arise from sensor geometry and environmental effects rather than ADC resolution; 16‑bit nominal resolution is only fully useful when sensor and analog front end justify it, and when additional bits translate into improved regression fit rather than modelling noise.[^5][^9]

Given this, the architecture treats **ESP32 internal ADC as the default** and **ADS1115 as an optional, Week‑1/2 comparison tool**:

- If internal ADC delivers sufficiently smooth, monotonic sensor curves with regression residuals dominated by sensor/soil effects, the external ADC is **not mandatory**.[^9][^5]
- If internal ADC nonlinearity or noise materially limits calibration quality (e.g., visible staircase artefacts, poor R² even with careful dataset design), ADS1115 can be retained for final implementation.[^5][^9]

### 10.2 Analog Front End Strategy

Published low‑cost capacitive sensor designs use simple RC filters, op‑amp buffers, and stable reference supplies to ensure signal integrity. For TrueMoist:[^9][^5]

- Begin with a breadboard‑level analog front end in Week 1, then migrate to perfboard soldering once the circuit stabilises, to reduce contact noise and improve repeatability.[^3][^5]
- Use a high‑input‑impedance buffer (such as an MCP6002 or LMV358 op‑amp) between the probe and ADC to avoid loading the sensor and to allow consistent scaling.[^5]
- Add RC low‑pass filtering (e.g., tens of kΩ and tens of nF) to suppress high‑frequency noise, tuned empirically so that step changes in moisture appear as smooth transitions over seconds.[^5]
- Maintain short sensor cable lengths and consistent routing; avoid long breadboard jumper wires that introduce parasitic capacitance and noise.[^13][^5]
- Implement solid grounding practice and decoupling capacitors near MCU and op‑amp supplies to reduce digital noise coupling.[^5]

A custom PCB is **not mandatory** for MVP; a well‑soldered perfboard is sufficient given budget and timeline, with breadboard used only in early experiments.[^3][^5]

## 11. MCU and Processing Architecture

### 11.1 MCU Comparison

Phase 3B synthesis and memory show that ESP32 and STM32 microcontrollers recur across multiple concepts and are considered viable platforms for TrueMoist. Key comparative considerations:[^6][^2]

- **ESP32‑WROOM‑32**: dual‑core Tensilica MCU, integrated Wi‑Fi/BLE, 12‑bit ADC, ~520 KB SRAM, 4 MB flash, floating‑point via libraries, wide Arduino IDE support, inexpensive development boards.[^6][^2]
- **ESP32‑S3**: improved ADC and additional features, but slightly higher cost and less entrenched Arduino ecosystem at student level.[^2]
- **STM32F103 (Blue Pill)**: Cortex‑M3, 12‑bit ADC, moderate flash/RAM, good ADC quality, but requires STM32Cube or PlatformIO; Arduino support exists but less straightforward for beginners.[^2]
- **STM32F4‑class**: more powerful, with FPU and better ADC, but higher cost and complexity.[^2]
- **Arduino Uno/Nano (ATmega328P)**: 10‑bit ADC, limited RAM/flash, simple but potentially constrained for multivariate regression, logging, and optional SD/OLED integration.[^6][^2]

TrueMoist’s computational needs are modest: multivariate linear or low‑order polynomial regression, simple filtering, CSV logging over serial, and possibly small OLED display updates; no heavy TinyML or DSP is required in MVP. ESP32 offers sufficient RAM, flash, and compute headroom, plus good ADC resolution and widely available boards within ₹400–₹600, making it a strong fit with student skills and budget.[^13][^6][^2][^3]

### 11.2 Selected MCU and Fallback

- **Primary MCU:** ESP32‑WROOM‑32 development board (e.g., ESP32‑DevKitC), programmed via Arduino IDE.
- **Fallback:** STM32F103‑based “Blue Pill” if ESP32 procurement or ADC calibration proves problematic, with linear regression and logging implemented via STM32 HAL or Arduino‑compatible frameworks.[^6][^2]

ESP32’s popularity is *not* the primary selection reason; rather, its combination of ADC capability, flash/RAM, toolchain familiarity, and cross‑project reuse (ColdTrace, VibeGuard, etc.) make it the most cost‑effective and buildable choice.[^6][^2]

## 12. Compensation Algorithm

### 12.1 Methods Compared

Phase 3C SOP and Phase 3B synthesis recommend comparing several algorithm families: single‑variable calibration curves, multivariate linear regression, polynomial regression, piecewise regression, lookup tables with interpolation, regularized methods like ridge regression, partial least squares, decision trees, random forests, shallow neural networks, adaptive filtering, recursive least squares, and hybrid methods.[^12][^3]

Agricultural moisture sensor calibration literature shows that:

- Simple linear regression between sensor voltage and VWC can achieve high R² for specific soil types when temperature and salinity are controlled.[^9][^5]
- Second‑order polynomial regression and piecewise linear models can capture nonlinearity in dielectric vs moisture response for capacitive probes.[^10][^5]
- Multivariate linear regression including temperature and EC terms can correct some systematic biases and reduce temperature/salinity sensitivity.[^7][^4][^5]
- Complex ML models (random forests, neural networks) may achieve marginally better accuracy but risk overfitting, require larger datasets, and are harder to interpret and deploy on microcontrollers.[^4][^9]

### 12.2 Selected Baseline and Preferred Models

Given TrueMoist’s constraints, the architecture selects:

- **Baseline model:** Single‑variable calibration curve (sensor voltage vs gravimetric moisture) per soil type, using linear or second‑order polynomial regression, to demonstrate baseline performance.[^10][^9][^5]
- **Preferred model:** **Multivariate linear or low‑order polynomial regression** including temperature and a coded salinity level (e.g., low/medium/high or numerical EC range determined at calibration), implemented offline and deployed as coefficients to the MCU.[^7][^4][^9][^5]
- **Optional upgrade path:** Regularized regression (ridge or partial least squares) and/or simple piecewise regression (different coefficients for distinct moisture ranges), plus possible shallow neural network or decision tree if data volume permits and embedded footprint is manageable.[^4][^9]

TinyML is **not required** for the MVP; training should occur offline on a laptop, and the MCU should perform inference only — computing compensated estimates from stored coefficients. Adaptive recalibration and recursive least squares, though conceptually attractive, are deferred to future phases due to increased complexity in dataset management and stateful firmware.[^2][^3]

## 13. Calibration Dataset Design

### 13.1 Practical Dataset Plan

Building on best practices from capacitance‑based sensor calibration studies, the dataset design for a single homogeneous soil type (e.g., locally available clay or loam) is:[^9][^5]

- **Soil type:** One locally sourced, sieved soil (e.g., clay‑loam) used for all samples.
- **Container size:** Plastic or metal containers of ~500–1,000 mL, diameter ~8–10 cm, depth ~10–12 cm, allowing consistent probe insertion and sample mixing.[^5]
- **Sample mass:** Approximately 300–500 g dry soil per container, enough to bury the probe at 6–8 cm depth with uniform packing.[^5]
- **Packing method:** Soil sieved, then packed to consistent bulk density by adding fixed mass and tamping with a standard tool to a marked depth; avoid air gaps.[^13][^9]

Define experimental levels:

- **Moisture levels:** At least 6–8 gravimetric moisture levels spanning from near oven‑dry (~0–5% water by mass) to near field capacity (~30–35% for clay soils), e.g., 5%, 10%, 15%, 20%, 25%, 30%, 35% water content.[^9][^5]
- **Salinity/EC levels (calibration only):** 3 levels using known salt solutions added to soil water: low (fresh water), medium (e.g., 1 dS/m), high (e.g., 3–4 dS/m) prepared via NaCl solution; actual EC measured in solution or soil‑pore water using a simple EC meter in beakers.[^14][^4]
- **Temperature levels:** 3–4 levels achieved in a controlled environment: cool (~20°C), moderate (~25°C), warm (~30–35°C), attained via room control or incubator; soil temperature tracked via DS18B20.[^7][^9]
- **Replicates:** At least 3 replicates per (moisture, salinity, temperature) combination, with separate containers and independent sample preparation, to capture variability.[^9][^5]

Total sample conditions: 8 moisture × 3 salinity × 3 temperature = 72 conditions; with 3 replicates = 216 containers. For a two‑month student project, this is ambitious; therefore a **practical MVP dataset** reduces scope while preserving multi‑variable coverage:

- 6 moisture levels (5–30%) × 2 salinity levels (low, high) × 2 temperature levels (cool, warm) × 3 replicates = 72 samples.

Each sample involves filling, mixing, tamping, equilibrating, measuring sensor output, then gravimetric drying and weighing; 72 samples can be realistically prepared and processed over several weeks with coordinated team effort.[^9][^5]

### 13.2 Measurement Procedure and Randomization

For each sample:

1. Prepare soil in container to target dry mass.
2. Add measured water volume/mass (with optional salt concentration) to reach target moisture; mix thoroughly; allow equilibration (e.g., 20–30 min) before measurement.[^5]
3. Insert capacitive probe to fixed depth, avoiding container walls and air pockets; insert DS18B20 at same depth and near probe.[^9][^5]
4. Allow sensor stabilization time (e.g., 10–20 min) until readings plateau.[^5]
5. Record multiple readings over a short period (e.g., 10–20 samples over 1–2 min) and average to reduce noise.[^9][^5]
6. Remove sensors; weigh wet soil and container; then dry per gravimetric procedure and weigh dry mass.[^9]

Randomization: do not process all samples of a single condition consecutively. Instead, randomize measurement order across moisture/salinity/temperature levels to minimise drift and systematic bias; use sample IDs to track conditions in the dataset.[^9]

### 13.3 Train/Validation Split and Data Leakage Avoidance

To prevent data leakage, repeated readings from the same physical soil condition must not be arbitrarily split across training and validation sets. Instead, group data by container/sample ID and perform splits at the **condition level**:[^9]

- Use **grouped split by soil‑preparation batch**: for example, 70% of sample IDs assigned to training, 30% to validation, ensuring that all readings from a given batch (same container, same moisture, salinity, temperature) reside entirely in either train or validation.[^5][^9]

This approach is more defensible than random per‑row splitting or leave‑one‑reading‑out, which would artificially inflate validation performance by exposing the model to nearly identical conditions in both sets. Leave‑one‑condition‑out (e.g., hold out one temperature or salinity level entirely) can be used as an additional robustness check to see whether compensation generalises to unseen environmental regimes.[^9]

## 14. Gravimetric Ground Truth Procedure

### 14.1 Reference Equation and Parameters

Gravimetric water content (θ_g) is defined as:

\[ \theta_g = \frac{m_\text{wet} - m_\text{dry}}{m_\text{dry}} \] [^17]

where m_wet is the mass of wet soil plus container (minus tare) and m_dry is the mass after drying; container tare mass is subtracted as appropriate.[^9]

Optional conversion to volumetric water content (θ_v) uses bulk density (ρ_b) and water density (ρ_w):

\[ \theta_v = \theta_g \cdot \frac{\rho_b}{\rho_w} \] [^18]

if bulk density is characterised; however, TrueMoist MVP can remain gravimetric.

### 14.2 Drying Method and Equipment

Standard soil science practice uses oven drying at ~105°C for 24 hours or until constant mass; this yields accurate gravimetric water content for most mineral soils. If a laboratory oven at 105°C is available via institution labs, TrueMoist should use it (preferred method).[^9]

If a lab oven is not accessible, fallback options include:

- **Food dehydrator or controlled hot‑air oven** at lower temperature (e.g., 60–80°C) with extended drying time and repeated weighing until mass change between successive measurements falls below a threshold (e.g., <0.1 g).[^9]
- **Repeated low‑temperature drying to constant mass** using domestic oven at ~80–100°C with careful safety practices and dedicated containers.[^9]
- **Microwave drying** is sometimes used for rapid estimation but can lead to uneven heating and potential soil alteration; for MVP, this method should be used only as a last resort and with clear documentation of expected bias and safety constraints.[^9]

Scale resolution of 0.01 g or better is recommended to capture realistic differences; inexpensive digital kitchen scales with 1 g resolution may be sufficient for coarse calibration but will increase uncertainty.[^9]

**Preferred gravimetric procedure:**

1. Label each container with sample ID.
2. Weigh empty container (tare) and record.
3. After soil and water addition and equilibration, weigh container plus wet soil; compute m_wet (wet mass minus tare).[^9]
4. Dry containers in lab oven at 105°C for ≥24 h or until mass change is negligible; if using fallback oven, extend drying and perform repeated weighings.[^9]
5. Weigh container plus dry soil; compute m_dry (dry mass minus tare).[^9]
6. Compute θ_g via equation  and record as reference moisture.[^17][^9]

Uncertainty sources include scale precision, incomplete drying, soil loss during transfer, and container contamination; replicate samples and careful handling reduce these risks.[^9]

### 14.3 Preferred and Fallback Reference Procedures

- **Preferred:** Lab oven at 105°C with 0.01 g resolution scale, constant mass criterion.
- **Fallback:** Household or departmental oven at 80–100°C with extended drying and repeated weighing to approximate constant mass, using a 1 g resolution scale; this fallback must be explicitly documented in reports as increasing absolute uncertainty but still sufficient to demonstrate relative improvement between uncompensated and compensated sensor outputs.[^9]

## 15. Mechanical and Soil‑Test Arrangement

### 15.1 Test Rig Design

A repeatable soil test rig must control container geometry, probe positioning, soil packing, and sensor placement. Based on calibration studies:[^5][^9]

- **Container material:** Rigid plastic or metal (e.g., PVC, polypropylene) with smooth walls; avoid deformable cups where soil compaction changes volume markedly.[^9]
- **Dimensions:** Diameter ~8–10 cm, height ~10–12 cm, giving volume of ~0.5–1 L; these dimensions allow insertion of standard capacitive probes and DS18B20 without wall interference.[^5]
- **Probe depth:** Insert moisture probe vertically to ~6 cm depth, ensuring the active area is fully surrounded by soil; mark the probe with depth graduations for consistency.[^13][^5]
- **Probe orientation:** Maintain vertical orientation to minimise variations due to geometry; avoid touching container walls.[^13]
- **Temperature sensor placement:** DS18B20 inserted ~1–2 cm away from moisture probe at same depth; ensure good soil contact and minimal air gaps.[^5][^9]

### 15.2 Packing and Variability Control

To minimise variability from packing density, heterogeneity, and water distribution:[^5][^9]

- Use sieved soil to remove large aggregates and stones.
- Add soil by mass, tamp to a fixed depth using a standard tool (e.g., flat plunger) and consistent force; consider simple jig to ensure uniform compaction across samples.[^9]
- Add water by mass or volume, mixing thoroughly with soil in a separate container before packing, to avoid vertical moisture gradients.[^9]
- Allow equilibration time (e.g., 20–30 min at room temperature) after packing and before measurement.
- Use consistent insertion method: mark insertion depth on probes; insert slowly and consistently to avoid disturbing packing; avoid rocking the probe.

A simple text schematic:

- Top view: circular container; moisture probe vertical in center; DS18B20 slightly offset; optional EC electrodes only used in calibration beakers, not in soil.
- Side view: container base; packed soil layer; probes inserted to mid‑depth; cables exiting upward; container labelled with ID.

## 16. Data Logging and Dataset Schema

### 16.1 Sampling and Filtering

For each sample condition:[^3][^5][^9]

- **Sampling rate:** Read moisture and temperature at ~1–2 Hz; average over 10–20 samples to obtain one representative reading per condition.
- **Averaging interval:** 10–20 s of sampling; discard initial transient seconds if the sensor shows warm‑up behaviour.[^5]
- **Warm‑up time:** Allow at least 10 min after probe insertion before recording; some capacitive sensors and DS18B20 probes require several minutes to stabilise.[^8][^5]
- **Filtering:** Use simple moving average; avoid aggressive digital filtering that might distort temperature or drift trends.

### 16.2 Logging Format and Storage

USB serial output from ESP32 can use CSV lines with fields:

- sample_id
- condition_id (e.g., moisture_level, salinity_level, temperature_level)
- timestamp
- raw_moisture_reading (ADC counts or voltage)
- temperature_C
- ec_condition (coded calibration salinity level; numeric EC for calibration beakers)
- reference_moisture (θ_g from gravimetric procedure, added later during offline merging)
- compensated_moisture_estimate
- model_version_id (e.g., baseline_v1, multivar_v2)

Data can be logged via serial capture (e.g., Arduino Serial Plotter or terminal) and saved as CSV; SD‑card logging is optional and not strictly necessary for MVP.[^3]

## 17. Validation Metrics and Success Thresholds

### 17.1 Metrics Compared

Common metrics include mean absolute error (MAE), root mean square error (RMSE), maximum absolute error, R² (coefficient of determination), coefficient of variation (CV), repeatability, hysteresis, drift, temperature coefficient, and salinity sensitivity.[^11][^4][^5][^9]

Calibration studies often report R², RMSE, and sensor‑to‑sensor CV as primary indicators of performance. For TrueMoist, emphasis should be on **relative improvement over uncompensated output** rather than achieving commercial‑grade absolute accuracy.[^5][^9]

### 17.2 Selected Metrics and Success Thresholds

- **Primary metric:** RMSE between sensor‑derived moisture estimate and gravimetric reference across validation conditions.[^5][^9]
- **Secondary metrics:** R² and temperature/salinity sensitivity (difference in error across temperature or salinity levels at fixed moisture).[^11][^4]

A realistic success threshold within MVP constraints is:

- **RMSE reduction of at least 25–30%** between uncompensated and compensated estimates over validation set; e.g., if uncompensated RMSE is 0.04 θ_g units, compensated RMSE ≤0.028–0.03.[^5][^9]
- **Improved R²** (e.g., increase from 0.85–0.9 uncompensated to ≥0.93 compensated) for the chosen soil type.[^5][^9]
- **Reduced temperature/salinity sensitivity:** lower variation in error across temperature or salinity levels at fixed moisture when compensation is applied compared to raw output.[^11][^4][^7]

These thresholds are grounded in reported calibration improvements for low‑cost capacitive sensors and are ambitious yet achievable for a student prototype focused on a single soil type.[^5][^9]

## 18. Prototype Test Matrix

TrueMoist’s architecture must support a set of controlled test scenarios to validate compensation performance under specific disturbances. For each test, define purpose, setup, controlled/disturbed variables, repeats, metrics, and pass/fail criteria.[^2][^3]

1. **Same moisture, different temperature**
   - Purpose: evaluate temperature compensation effectiveness.
   - Setup: prepare samples at fixed moisture (e.g., 20%) at two temperature levels (~20°C, ~30°C); measure raw and compensated estimates.[^7]
   - Controlled variable: moisture; disturbed variable: temperature.
   - Repeats: ≥3 samples per temperature level.
   - Metrics: RMSE, R², temperature coefficient (change in error per °C).
   - Pass rule: compensated RMSE and temperature coefficient significantly lower than uncompensated; fail if compensation increases error or fails to reduce temperature sensitivity.

2. **Same moisture, different salinity (calibration conditions)**
   - Purpose: evaluate salinity compensation using coded salinity levels.
   - Setup: fixed moisture (e.g., 20%) with low vs high EC soil (via salt solutions); measure sensor outputs and apply compensation model.[^4][^11]
   - Controlled variable: moisture; disturbed variable: salinity.
   - Repeats: ≥3 per salinity level.
   - Metrics: RMSE, salinity sensitivity (error difference across EC levels).
   - Pass rule: compensated error less sensitive to salinity than uncompensated.

3. **Multiple moisture levels under fixed temperature and salinity**
   - Purpose: evaluate overall calibration curve performance.
   - Setup: full range of moisture levels at standard temperature and salinity; measure raw and compensated estimates.[^5][^9]
   - Controlled variables: temperature, salinity; disturbed variable: moisture.
   - Repeats: ≥3 per level.
   - Metrics: RMSE, R², maximum absolute error.
   - Pass rule: RMSE reduction ≥25–30%; R² improvement; fail if improvement is marginal.

4. **Repeated wetting/drying cycle**
   - Purpose: examine hysteresis and drift across cycles.
   - Setup: one or more containers repeatedly wetted and dried over several cycles; sensor readings tracked.[^9]
   - Controlled variable: soil and sensor identity; disturbed variable: time and cycles.
   - Repeats: ≥3 cycles.
   - Metrics: drift, hysteresis in calibrated curves; difference between cycles.
   - Pass rule: compensated estimates show reduced hysteresis and drift compared to raw readings.

5. **Sensor warm‑up / short‑term drift**
   - Purpose: characterise sensor behaviour immediately after insertion.
   - Setup: insert probes into a stable sample and record readings at high sampling rate for 30–60 min.[^5]
   - Disturbed variable: time since insertion.
   - Metrics: drift magnitude; time to stable reading.
   - Pass rule: warm‑up window and drift characterised; model uses stable region; failure only if drift is so severe that stable readings cannot be obtained.

6. **Repeated insertion or repositioning**
   - Purpose: evaluate sensitivity to insertion technique and small positional changes.
   - Setup: multiple insertions into the same sample with controlled variations (slight depth changes, small lateral shifts).[^13]
   - Metrics: variation in raw and compensated estimates.
   - Pass rule: variability quantified; compensation does not amplify insertion‑induced noise.

7. **Raw versus compensated output comparison (global)**
   - Purpose: demonstrate overall benefit in a summarised plot or table.
   - Setup: collect validation data across conditions; compute raw vs compensated error metrics.
   - Pass rule: global RMSE reduction and improved R²; ideally, present a plot showing compensation improvement.

8. **Held‑out condition validation**
   - Purpose: test generalisation to a condition not used in training (e.g., mid‑range temperature or salinity level).[^9]
   - Setup: hold out one condition during training and test model on that condition.
   - Metrics: error metrics.
   - Pass rule: compensated performance remains acceptable; fail if error spikes suggest overfitting.

9. **Internal versus external ADC comparison (Week‑1/2 if ADS1115 used)**
   - Purpose: quantify any accuracy improvement from ADS1115.
   - Setup: read sensor via both internal ADC and ADS1115 for identical samples; perform separate calibration fits.[^5]
   - Metrics: RMSE, R², noise characteristics.
   - Pass rule: adopt external ADC only if improvement is clearly measurable and justified; otherwise use internal ADC.

10. **Calibration transfer to fresh sample of same soil type**
    - Purpose: verify that calibration applies to new containers prepared independently but with same soil type and protocol.[^9]
    - Setup: prepare new samples without retraining; apply existing model.
    - Metrics: error metrics.
    - Pass rule: performance similar to original validation; failure indicates strong dependence on specific batch conditions.

## 19. Electrical and Power Architecture

### 19.1 Power Strategy and Budget

TrueMoist MVP does not require battery operation; USB‑powered MCU is acceptable and simpler. Power architecture:[^2][^3]

- USB 5 V input from laptop or charger to ESP32 board.
- On‑board 3.3 V regulator powering MCU, DS18B20, and, if required, moisture sensor (some probes need 3.3 or 5 V, check datasheet).[^5]
- Total current consumption: ESP32 (~80–200 mA depending on Wi‑Fi usage), DS18B20 (~1 mA per conversion), moisture probe (~5–20 mA), ADS1115 (~150 µA), op‑amp (~1–2 mA).[^8][^5]

The analog front end must ensure stable supply and reference voltages; decoupling capacitors near MCU and op‑amp supply pins mitigate noise.[^5]

Battery operation (e.g., Li‑ion or AA cells) is optional: it may be considered for field demonstration but is not required for MVP; if used, additional regulator and battery‑monitoring circuitry must be added, increasing complexity and risk.[^2][^5]

## 20. User Interface and Demonstration

The simplest effective interface is a combination of **USB serial logging** and optional small **OLED display**:[^3][^2]

- USB terminal shows per‑sample lines: raw sensor reading, temperature, reference moisture (added later for lab display), compensated moisture, and model version, enabling plotting and analysis in Python/R.
- Arduino Serial Plotter or external plotting tools can visualise raw vs compensated values across conditions and highlight improvement.
- A small OLED (e.g., 0.96" I²C module) can display side‑by‑side values for live demos: raw, compensated, and reference moisture for currently measured sample, along with temperature and salinity condition code.

No LCD, buzzer, RGB LED, or smartphone app is required beyond this; avoiding gold‑plating keeps the team focused on measurement, calibration, and compensation chain.

## 21. Costed BOM

Indian pricing estimates are based on typical online suppliers and prior feasibility studies; actual prices may vary but should remain within budget.[^8][^2][^5]

| Component | Role | Qty | Preferred model | Substitute | Est. price (₹) | Source type | Availability risk |
|-----------|-----|-----|------------------|-----------|----------------|------------|------------------|
| ESP32‑DevKitC board | MCU & processing | 1 | ESP32‑WROOM‑32 dev board | NodeMCU‑32S | 400–600 | Indian electronics e‑commerce | Low |
| Capacitive soil‑moisture probes | Moisture sensing | 2 | Generic v1.2 capacitive sensor module | Raw capacitive PCB probe | 150–300 each | Maker stores, marketplaces | Low |
| DS18B20 waterproof probe | Soil temperature | 1–2 | Stainless steel waterproof DS18B20 | Generic DS18B20 module | 200–350 | Indian e‑commerce, agri vendors | Low |
| ADS1115 module (optional) | External ADC | 1 | ADS1115 16‑bit ADC breakout | MCP3421 or similar | 150–250 | Maker stores | Medium (optional) |
| Op‑amp (MCP6002/LMV358) | Buffer/filter | 1–2 | Low‑power rail‑to‑rail op‑amp | LM358 | 50–100 | Electronics vendors | Low |
| OLED 0.96" I²C | Local display (optional) | 1 | SSD1306 OLED module | 16x2 LCD | 150–250 | Maker stores | Low |
| Perfboard & headers | Analog front end & wiring | 1–2 | Generic perfboard | Small PCB | 100–150 | Local electronics shops | Low |
| Jumpers, connectors, resistors, capacitors | Wiring & AFE | assorted | Standard components | — | 200–300 | Electronics vendors | Low |
| Soil containers | Mechanical test rig | 10–20 | Plastic cylinders or cups | Metal cans | 200–300 | Local shops | Low |
| Digital scale | Gravimetric weighing | 1 | 0.01–1 g resolution scale | Lab balance | 500–800 | Online marketplace | Medium (if lab balance available, cost disappears) |
| Drying equipment | Gravimetric oven | 0–1 | Lab oven (existing) | Food dehydrator / domestic oven | 0–1,500 | Lab asset / marketplace | Medium (likely existing in institution) |
| Misc. tools | Tamping tool, labels, etc. | — | Simple tools | — | 200–300 | Local shops | Low |

**Preferred total (assuming lab oven and lab scale available):** ~₹1,800–₹2,500 (MCU, sensors, analog front end, containers, misc.).[^8][^2][^5]

**Worst‑case total (including purchase of a decent kitchen scale and simple dehydrator/oven):** ~₹3,500–₹4,000. Both totals remain under the preferred ₹3,000 target in typical institutional contexts and clearly below ₹5,000 absolute maximum when scale/oven must be purchased.[^2][^5]

## 22. Compute, Memory, and Storage Budget

ESP32 resources are ample for TrueMoist:[^6][^2]

- RAM: ~520 KB; compensation inference requires storing a small number of regression coefficients (<20) and buffers for averaging (dozens of samples), well within capacity.
- Flash: 4 MB; firmware and coefficient storage occupy <<1 MB.
- ADC sample rate: ESP32 ADC can handle kHz rates; TrueMoist needs only 1–2 Hz per sample, so CPU load is minimal.[^5]
- CPU load: simple arithmetic per sample (a few multiplications and additions) plus serial print; negligible relative to MCU capacity.
- Data buffer size: tens of readings per condition; serial throughput at 115,200 baud easily supports logging.

Storage: dataset logging occurs on the host laptop via serial; optional SD card (4–8 GB) and simple file system code can store CSVs locally, but is not necessary for MVP. Overall, the selected MCU has abundant margin.[^3]

## 23. Risk Register

Major risks, likelihood, impact, mitigations, fallbacks, and kill criteria:

1. **Sensor instability and drift**
   - Likelihood: Medium; low‑cost capacitive probes exhibit drift and temperature/salinity sensitivity.[^11][^5]
   - Impact: High; may obscure compensation benefits.
   - Early indicator: inconsistent readings across replicates; large drift during warm‑up.
   - Mitigation: use multiple probes; characterise drift in Week 1; select more stable probe or adjust dataset design; apply protective coating if needed.[^5]
   - Fallback: narrow experimental scope to conditions where sensor is stable.
   - Kill criterion: if sensor variability exceeds gravimetric uncertainty and cannot be reduced by calibration or improved probe selection.

2. **Soil packing variation and heterogeneity**
   - Likelihood: Medium‑high.[^9]
   - Impact: High; adds noise and confounding.
   - Indicator: high variance across nominally identical samples.
   - Mitigation: strict packing protocol, jigs, sieving, controlled mixing, increased replicates.
   - Fallback: reduce condition count, increase replicates per condition.
   - Kill criterion: if packing variation dominates all other errors such that compensation cannot be distinguished.

3. **Moisture‑salinity confounding**
   - Likelihood: Medium.[^4][^11]
   - Impact: Medium‑high.
   - Indicator: difficulty separating EC effects from moisture changes; inconsistent error trends.
   - Mitigation: treat salinity as calibration‑only; avoid live EC measurement in soil; perform solution‑EC measurement under controlled conditions.[^4]
   - Fallback: exclude salinity from MVP and focus on temperature compensation.
   - Kill criterion: if salinity confounding prevents clear demonstration of improvement even for temperature‑controlled tests.

4. **Unreliable EC measurement (if attempted)**
   - Likelihood: Medium‑high.[^14][^4]
   - Impact: Medium.
   - Indicator: noisy EC readings, electrode corrosion.
   - Mitigation: limit EC measurement to solution or pore‑water extraction; use proper AC excitation and non‑polarising electrodes; or omit EC measurement entirely.[^4]
   - Fallback: calibration‑only salinity design.
   - Kill criterion: if EC measurement adds more error than it helps; architecture should then revert to temperature‑only compensation.

5. **ADC error and analog noise**
   - Likelihood: Medium.[^5]
   - Impact: Medium.
   - Indicator: poor linearity or step‑like sensor curves.
   - Mitigation: analog front end improvements; optional ADS1115 testing; calibrate ESP32 ADC.[^5]
   - Fallback: adopt external ADC if internal is clearly limiting.
   - Kill criterion: if neither internal nor external ADC yields usable calibration within budget.

6. **Insufficient dataset**
   - Likelihood: Medium.[^9]
   - Impact: High.
   - Indicator: few samples per condition; model overfitting or unstable coefficients.
   - Mitigation: prioritise dataset generation Weeks 3–4; reduce condition count; maintain replicates; ensure grouped train/validation split.
   - Fallback: focus on a smaller set of conditions that demonstrate improvement.
   - Kill criterion: if dataset size is too small to compute meaningful regression.

7. **Model overfitting and poor generalisation**
   - Likelihood: Medium.[^9]
   - Impact: Medium‑high.
   - Indicator: excellent training performance but poor held‑out condition results.
   - Mitigation: use simple models (linear or low‑order polynomial), regularisation, grouped split, held‑out condition tests.
   - Fallback: simpler model, fewer variables.
   - Kill criterion: if no model yields consistent improvement across validation conditions.

8. **Gravimetric‑reference error**
   - Likelihood: Medium.
   - Impact: High.
   - Indicator: inconsistent θ_g across replicates; visible mass loss not due to water.
   - Mitigation: careful drying, weighing, and handling; repeated mass measurements to constant weight; use lab equipment if possible.[^9]
   - Fallback: thoroughly document increased uncertainty; shift focus to relative improvement.
   - Kill criterion: if gravimetric reference is too unreliable to serve as ground truth.

9. **Calibration workload and time overrun**
   - Likelihood: Medium‑high.
   - Impact: High.
   - Indicator: dataset generation lagging schedule.
   - Mitigation: structured team allocation; pre‑defined dataset plan; timeboxing conditions.
   - Fallback: reduce number of conditions and replicates; extend working hours if feasible.
   - Kill criterion: if insufficient calibration data can be collected by Week 5.

10. **Component availability and budget overrun**
    - Likelihood: Low–medium.[^2]
    - Impact: Medium.
    - Indicator: shipping delays or higher than expected prices.
    - Mitigation: multiple supplier options; early procurement; component substitutes.
    - Fallback: use alternate MCU (e.g., STM32F103) or omit optional hardware.
    - Kill criterion: if total cost cannot be kept under ₹5,000.

11. **Electrical noise and interference**
    - Likelihood: Medium.[^5]
    - Impact: Medium.
    - Indicator: noisy readings; sensitivity to cable movement.
    - Mitigation: good grounding, shielding if needed, short cables, filtering.
    - Fallback: reduce measurement speed; average more samples.
    - Kill criterion: if noise dominates sensor signal.

12. **Failure to demonstrate measurable improvement**
    - Likelihood: Medium.
    - Impact: Very high.
    - Indicator: compensated model fails to reduce error metrics.
    - Mitigation: revisit dataset design, model selection, and calibration; focus on temperature compensation and simple conditions.
    - Fallback: narrow demonstration to specific scenario (e.g., temperature variation) where improvement is clear.
    - Kill criterion: if, by Week 7, no scenario shows meaningful improvement; architecture may need to be simplified or re‑scoped.

## 24. Rejected Alternatives

Major rejected options and rationales:

1. **Direct bulk soil EC measurement as runtime input**
   - Considered: using electrodes to measure soil apparent EC.[^14][^4]
   - Rejected for MVP due to complexity of AC excitation, electrode polarization, corrosion, and confounding with moisture; treated instead as calibration‑time variable via solution‑EC measurement.[^11][^4]
   - May be viable in future if robust EC circuitry and electrodes are added.

2. **External ADC as mandatory component**
   - Considered: always using ADS1115.[^2][^5]
   - Rejected as mandatory due to likely dominance of sensor/soil variability over ADC resolution and added complexity; reserved as optional comparison in Week 1–2.

3. **ESP32 vs STM32 vs Arduino Uno**
   - Arduino Uno rejected as primary MCU due to limited ADC resolution and memory for multi‑variable logging and display.[^2]
   - STM32 viable but requires more complex toolchains; ESP32 chosen for better team fit and reuse across projects.[^6][^2]

4. **High‑order polynomial regression and complex ML (TinyML)**
   - Considered: polynomial regression of degree >2, random forests, shallow neural networks.[^4][^9]
   - Rejected for MVP due to overfitting risk, dataset size constraints, and embedded deployment complexity; simpler models chosen.

5. **Adaptive calibration and recursive least squares**
   - Considered: on‑device model updating based on ongoing data.[^12]
   - Deferred: adds significant firmware and dataset‑management complexity; MVP focuses on static calibration and compensation.

6. **Display‑heavy UI and smartphone interface**
   - Rejected to avoid gold‑plating; minimal OLED/serial interface suffices.[^3]

7. **Custom PCB for analog front end**
   - Considered but rejected for MVP; perfboard soldering is adequate and faster.[^5]

## 25. Patent and Innovation Implications

### 25.1 Engineering Differentiation

TrueMoist is more than an ordinary moisture meter because it explicitly:

- Uses gravimetric ground truth to calibrate low‑cost capacitive probes for a specific soil type.[^5][^9]
- Models and compensates predictable error from temperature and controlled salinity conditions using embedded regression.[^7][^4][^5]
- Demonstrates improved trustworthiness (reduced RMSE, improved R², reduced environmental sensitivity) under controlled disturbances, rather than merely reporting raw readings.[^3][^2]

This measurement‑chain focus — from cheap sensor through calibration, compensation, and validation — differentiates TrueMoist from generic irrigation controllers and simple moisture meters.

### 25.2 Semester‑Project Novelty

Within an academic semester, the project’s distinctiveness lies in:

- Rigorous lab‑style calibration and dataset design for a low‑cost soil‑moisture probe.[^5][^9]
- Implementation of multi‑variable compensation on a student‑friendly MCU, with clear demonstration of improved metrics under scripted disturbances.
- Honest handling of gravimetric reference and uncertainty, including fallback methods and their limitations.

These features make TrueMoist an advanced measurement and calibration project rather than a basic sensor integration exercise.

### 25.3 Future Patent Direction

Phase 2 patent analysis indicates that hardware compensation circuits for soil moisture (dual‑frequency EC/temperature compensation) are heavily patented; the most promising IP space lies in **software‑side, event‑driven adaptive calibration and edge intelligence**. Potential future non‑obvious developments include:[^12][^4]

- Self‑updating correction algorithms that use irrigation/dry‑down cycles and gravimetric or reference moisture events to adapt coefficients over time without manual recalibration.[^12]
- Embedded confidence estimation and sensor‑health tracking based on drift and hysteresis metrics.
- Calibration workflows that combine small, controlled lab datasets with field data via transfer learning.

TrueMoist MVP should avoid claiming patentability merely for combining moisture, temperature, and EC inputs with regression; novelty must derive from specific calibration workflows, adaptive algorithms, or low‑cost compensation methods not obvious from existing literature, which requires further field validation beyond Phase 3C.[^12][^4]

Freedom‑to‑operate considerations: staying on the software side (no custom probe hardware) and avoiding replication of specific hardware compensation circuits described in patents (e.g., dual‑frequency bridges) reduces IP risk, but any future patent filing must be guided by detailed claim‑charting and legal counsel.[^12][^4]

## 26. Team Allocation

Given the five‑member team composition:[^6][^3]

- **Member 1 — Embedded systems and integration lead:** responsible for MCU firmware, sensor drivers (DS18B20, moisture probe, optional ADS1115), USB serial logging, OLED display, and overall code integration.
- **Member 2 — Data, modelling, and compensation lead:** designs dataset, performs offline regression, evaluates models, tunes compensation algorithms, and documents validation metrics.
- **Member 3 — Hardware, analog front end, and validation lead:** designs and builds analog front end on perfboard, manages wiring and signal integrity, constructs mechanical test rig, and oversees calibration experiments.
- **Member 4 — Learner (software, logging, UI, test support):** implements simple logging utilities, assists with firmware testing, helps with data capture scripts, and supports mechanical and gravimetric workflows under guidance.
- **Member 5 — Documentation, experiment records, BOM tracking, and presentation support:** maintains detailed lab notebooks and digital records, tracks BOM and procurement, prepares figures and slides, and coordinates final demonstration narrative.

Critical‑path tasks (firmware, AFE, dataset design) are assigned to technically strong members; the learner and presenter perform supporting roles that are important but not single‑point‑of‑failure.

## 27. Eight‑Week Roadmap

A realistic eight‑week plan, assuming some overlap and parallel work:[^6][^3][^2]

- **Week 1: Component verification and sensor characterisation**
  - Tasks: procure MCU, probes, DS18B20, AFE parts; build basic breadboard circuit; read raw moisture and temperature; characterise sensor warm‑up and drift; compare ESP32 internal ADC vs ADS1115 if available.[^5]
  - Owners: Members 1 & 3; Member 5 logs experiments.
  - Deliverables: initial sensor behaviour plots; decision on whether external ADC is worth keeping.
  - Risks: sensor instability; ADC nonlinearity; early detection triggers fallback.

- **Week 2: ADC/AFE decision and test‑rig construction**
  - Tasks: finalise analog front end design; solder perfboard; build mechanical test rig (containers, insertion guides); finalise MCU choice and pin assignment.[^5][^9]
  - Owners: Member 3 (AFE and rig), Member 1 (firmware); Member 5 (document wiring diagrams).
  - Deliverables: stable hardware chain; mechanical rig ready.
  - Risks: noise and wiring issues; mitigated by iterative testing.

- **Week 3: Pilot dataset and experimental refinement**
  - Tasks: run small pilot dataset (e.g., 3 moisture × 2 temperature × 2 salinity); exercise gravimetric workflow using chosen drying method; refine packing and equilibration protocols; test CSV logging.[^9][^5]
  - Owners: Members 2 & 3; Member 4 supports logging; Member 5 records procedures.
  - Deliverables: pilot dataset, initial regression fits, updated protocols.
  - Risks: gravimetric errors; packing variation; adjust protocols accordingly.

- **Week 4: Calibration dataset collection**
  - Tasks: collect full MVP dataset (~72 samples) following agreed plan; label and track each sample; ensure grouped condition IDs for later splitting.[^9]
  - Owners: Members 2 & 3; Member 4 assists mixing and weighing; Member 5 manages record‑keeping.
  - Deliverables: complete calibration dataset file; sample IDs mapped to conditions.
  - Risks: schedule pressure; mitigate via daily targets and division of labour.

- **Week 5: Model development and offline validation**
  - Tasks: perform regression modelling with training/validation splits; compare baseline vs multivariate models; evaluate RMSE, R², temperature/salinity sensitivity; select final compensation model.[^5][^9]
  - Owners: Member 2; Member 1 supports test code for coefficient application.
  - Deliverables: chosen model with coefficients; validation report; success‑threshold assessment.
  - Risks: overfitting; limited data; mitigate via simple models and grouped splits.

- **Week 6: Embedded deployment**
  - Tasks: embed final coefficients into firmware; implement compensation inference; integrate OLED display (if used); refine USB logging format and metadata.[^3]
  - Owners: Member 1; Member 4 assists UI; Member 2 validates firmware output against offline calculations.
  - Deliverables: working TrueMoist prototype performing local compensation; consistent outputs.
  - Risks: firmware bugs; coefficient mis‑loading; mitigated by cross‑checking.

- **Week 7: Comparative testing and debugging**
  - Tasks: run full test matrix (temperature/salinity disturbances, held‑out conditions, ADC comparison if relevant); compute metrics; refine documentation and plots.[^3][^9]
  - Owners: Members 2 & 3; Member 5 assembles figures; Member 4 helps tests.
  - Deliverables: validation results showing improvement; bug fixes.
  - Risks: failure to show improvement; fallback to simplified scenarios (e.g., temperature‑only) while documenting lessons.

- **Week 8: Repeatability testing, documentation, and demonstration**
  - Tasks: perform repeated insertion and cycle tests; finalise risk register; prepare technical report and presentation; rehearse demo showing raw vs compensated vs reference values.[^3]
  - Owners: Member 5 (documentation and presentation); all members contribute.
  - Deliverables: complete Phase 3C report, slides, and a demonstrable prototype.
  - Risks: documentation gaps; mitigated by early drafting and iterative review.

## 28. Phase 4 Readiness Decision

Given the above investigation and architecture definition, TrueMoist is rated:

> **Architecture Ready with Mandatory Early Validation.**

The architecture is coherent, buildable within two months and ₹5,000, and aligned with the project’s engineering identity, hypothesis, and minimum demonstrable success. However, success hinges on early validation gates in Weeks 1–3 (sensor stability, AFE/ADC adequacy, gravimetric workflow feasibility, pilot dataset) being passed; if those gates fail, architecture must revert to a simpler minimal‑compensation demonstrator or adjust test scope accordingly.[^1][^6][^2][^3]

## 29. Project Decision Register Updates

Based on Phase 3C findings, recommended updates to Project mC Decision Register entries for TrueMoist (PDR‑031, PDR‑032, PDR‑045, PDR‑048, PDR‑049, PDR‑050) are:

- **PDR‑031 (TrueMoist Engineering Identity/Hypothesis):** Confirm that identity remains focused on improving trustworthiness of low‑cost soil‑moisture sensors via local compensation, not on building a high‑accuracy universal probe or generic irrigation controller.[^1][^3]
- **PDR‑032 (Measurement vs Control Focus):** Fix TrueMoist’s MVP scope firmly on measurement and compensation with gravimetric validation; irrigation control logic (valves, pumps) explicitly deferred to future applications.[^1][^3]
- **PDR‑045 (EC Strategy):** Update to specify that EC/salinity is treated as a calibration‑time variable using solution or controlled soil batches, not as a runtime soil‑EC measurement in MVP; direct soil EC sensing may be explored in later phases if justified.[^11][^4][^3]
- **PDR‑048 (ADC Choice):** Record that ESP32 internal ADC is the default, with ADS1115 optional for comparative testing; external ADC inclusion in final build depends on Week‑1/2 evidence of measurable improvement.[^2][^5]
- **PDR‑049 (Compensation Algorithm):** Fix multivariate linear/low‑order polynomial regression as the baseline compensation method for MVP, with TinyML/adaptive calibration treated as upgrade paths requiring further data and separate feasibility assessment.[^12][^5][^9]
- **PDR‑050 (Gravimetric Reference and Dataset Requirements):** Codify the chosen gravimetric drying method (lab oven preferred, fallback documented) and dataset‑design principles (single soil type, multi‑level moisture/temperature/salinity, grouped train/validation split, minimum sample count) as mandatory for TrueMoist validation.[^3][^9]

New PDR decisions to add:

- **New PDR‑0XX (Mechanical Test Rig Standard):** Define standard container dimensions, probe insertion depths, packing protocol, and equilibration times as fixed test‑rig design parameters for TrueMoist.
- **New PDR‑0XY (Validation Metrics and Success Threshold):** Record RMSE reduction and R² improvement thresholds as the formal success conditions for Phase 4 evaluation.
- **New PDR‑0XZ (Phase 3C Architecture Selection):** Log the choice of “Measurement‑Focused Compensated Sensor with Offline‑Trained Multivariate Regression (ESP32, capacitive probe, DS18B20, calibration‑time EC)” as the primary TrueMoist architecture, with minimal‑compensation demonstrator as fallback.

## 30. Phase 3C Memory

**Final Architecture:** Measurement‑focused compensated sensor using a low‑cost capacitive soil‑moisture probe, DS18B20 soil‑temperature sensor, calibration‑time salinity/EC representation, ESP32 MCU with internal ADC (ADS1115 optional), perfboard‑based analog front end, and offline‑trained multivariate regression deployed for embedded inference.[^1][^2][^3][^5][^9]

**Selected Components:** ESP32‑DevKitC; generic capacitive soil‑moisture probe(s); waterproof DS18B20 soil‑temperature probe; optional ADS1115; low‑power op‑amp (e.g., MCP6002); perfboard, wiring, and small OLED; lab or household oven and digital scale for gravimetric reference.[^8][^2][^5]

**Selected Algorithm:** Baseline single‑variable calibration; preferred multivariate linear/low‑order polynomial regression including temperature and coded salinity; offline training on grouped dataset; embedded inference only.[^5][^9]

**Calibration Method:** Single homogeneous soil type; ~6 moisture levels × 2 salinity levels × 2 temperature levels with ≥3 replicates (~72 samples); controlled packing and equilibration; gravimetric oven‑drying to constant mass; grouped train/validation split by sample ID; held‑out condition tests.[^3][^9][^5]

**Validation Method:** RMSE, R², temperature and salinity sensitivity; tests for same moisture/different temperature, same moisture/different salinity (calibration), multiple moisture levels, wetting/drying cycles, warm‑up, insertion variability, raw vs compensated comparison, internal vs external ADC comparison (if ADS1115 used), calibration transfer to fresh samples.[^3][^9][^5]

**Cost:** Preferred total ~₹1,800–₹2,500 assuming lab oven/scale availability; worst‑case total (including basic scale and drying equipment) ~₹3,500–₹4,000; both within project ceiling and preferred budget where lab equipment is provided.[^8][^2][^5]

**Risks:** Sensor instability and drift; soil packing variation; moisture‑salinity confounding; unreliable EC measurement; ADC/AFE noise; insufficient dataset; model overfitting; gravimetric error; calibration workload; component availability and budget; electrical noise; failure to demonstrate measurable improvement; each with explicit mitigation, fallback, and kill criteria.[^12][^2][^3][^9][^5]

**Unresolved Questions:** Need to empirically determine impact of external ADC on calibration quality; practicality of EC strategy beyond calibration‑time representation; feasibility and benefit of adaptive calibration algorithms given dataset size; potential for field deployment beyond lab environment.

**Readiness:** Architecture Ready with Mandatory Early Validation — buildable and concept‑faithful, but contingent on Week‑1/3 gates for sensor behaviour, analog front end, gravimetric workflow, and pilot dataset success.[^6][^2]

**PDR Changes:** Confirm and refine TrueMoist identity and scope (PDR‑031, PDR‑032); set EC strategy as calibration‑only in MVP (PDR‑045); define ADC decision as evidence‑based with ESP32 internal default and optional ADS1115 (PDR‑048); codify compensation algorithm choice (PDR‑049); formalise gravimetric and dataset requirements (PDR‑050); add new decisions for mechanical test rig, validation metrics, and architecture selection.

---

## References

1. [Engineering_Design_Review.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/798f8d53-67c1-401c-af91-8ed8f4d78127/Engineering_Design_Review.md?AWSAccessKeyId=ASIA2F3EMEYEVELCGW3H&Signature=PvA2HoatgYcSqL%2BnAowCQGX1uyY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCdbTHCZJp7QKQ0utjGpV%2FloKJCTCwUgrYnr8jLrEZV1QIgPsN%2FHzh05jc9R9PL4g5glmtAX57TkUdQaWdYXboOPEUq8wQIURABGgw2OTk3NTMzMDk3MDUiDKruZiIPVZSYaW2TKyrQBNr7kaTdytNzJJvEtXhgEpvdD5JgKhLLpuosiCn8x%2BP7F%2F1Q4Unjij6zcOlonJk1UI3GIi7VD4bC%2FKCnedWCAFwB5j1aZUQM5NlQIb1dJ61cS2aHMcKF7n2oMGGw8DMR9iPfQaREthROByc5p3BzYrYJlkOG8%2FoL6NKasQowi3IG6Zsn9i3bryz0X5cnhhp1gFWvrOcg00ZLs%2BnxPdnDHW0FQS%2FlysrIhmq80ij2je4lkYabbFYhJbPYRbazSK9WxJyoNk6PEr97T2uAfF1E00koBhjYn0vHqAjqeV%2BrzBHEDCDDW%2BkRygmy2RlRUJK7LgOEzGrTly8Xrek6o%2BdysFG%2BrMGnytAA8tWXoBMeErLnUpn5zc1%2FxpX8%2B6xRs10DLjNWNMb5036Df1ou3R8FVQQgCGD8DdOVpZnKPJeOUxh4WQlwmuV0VMH6PVClW%2FJaspOAWwLIJGw5C414VjgR%2BXiYjO8%2BvUFMrQ%2F8c0vV9OcCDZnAv1t45ZP1Zyhb8avCNzNEa4mPynU6X8Mx8b4KHf4EiuxtugdP3PueXnVlk2YMEGVIFTptu6TRMJmEqCs6PJKX%2FbrMcUtXAmt4G7eXwPCK0wZqHnzerECaYqjgMfQFIK%2FLT9NksW96HNXy3XA57j2AY6Nv62VoQI5yBIU%2FlUniIiTkcC%2BRCp12XDdrD5QP%2FWPmWknYgfvurA%2BKyvmYGKRbAYE7hTkt7L5u9pcML54DmZWfNC%2BsDQBXRkgN50XwGvKrSb7ubu%2BxCeGoFGsVvzSgkqNF4FNx%2FWDZyAICFPww9%2F6d0wY6mAGWvK22c4%2BxrTFVnWI621UX4CSCwaCyVfzWfVveLnM%2Fo1KPPLkpleKh%2BwGVL%2BrP3xP5C8%2FjkjkTFnKpFDVyPpPXRQ%2F8k0vZy2kiPPsAaByfKjHscLnG%2Bbl9mpFCL15SwWCz1%2B3z8e2a8xKTi2tz%2F0N7pC3nHtBBbMJq4Oh3pGGL4OVYQVQEeAdFrW42JuBhLRGWj1BuuLxqpg%3D%3D&Expires=1785171274) - Engineering Design Review Overview Purpose The Engineering Design Review EDR serves as the transitio...

2. [Phase3B_Report_by_Claude.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/b606b32c-b264-43f2-a386-ae78909dd40f/Phase3B_Report_by_Claude.md?AWSAccessKeyId=ASIA2F3EMEYEVELCGW3H&Signature=FjMj4ByRtjW4CV4dWmZrSW3CKhg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCdbTHCZJp7QKQ0utjGpV%2FloKJCTCwUgrYnr8jLrEZV1QIgPsN%2FHzh05jc9R9PL4g5glmtAX57TkUdQaWdYXboOPEUq8wQIURABGgw2OTk3NTMzMDk3MDUiDKruZiIPVZSYaW2TKyrQBNr7kaTdytNzJJvEtXhgEpvdD5JgKhLLpuosiCn8x%2BP7F%2F1Q4Unjij6zcOlonJk1UI3GIi7VD4bC%2FKCnedWCAFwB5j1aZUQM5NlQIb1dJ61cS2aHMcKF7n2oMGGw8DMR9iPfQaREthROByc5p3BzYrYJlkOG8%2FoL6NKasQowi3IG6Zsn9i3bryz0X5cnhhp1gFWvrOcg00ZLs%2BnxPdnDHW0FQS%2FlysrIhmq80ij2je4lkYabbFYhJbPYRbazSK9WxJyoNk6PEr97T2uAfF1E00koBhjYn0vHqAjqeV%2BrzBHEDCDDW%2BkRygmy2RlRUJK7LgOEzGrTly8Xrek6o%2BdysFG%2BrMGnytAA8tWXoBMeErLnUpn5zc1%2FxpX8%2B6xRs10DLjNWNMb5036Df1ou3R8FVQQgCGD8DdOVpZnKPJeOUxh4WQlwmuV0VMH6PVClW%2FJaspOAWwLIJGw5C414VjgR%2BXiYjO8%2BvUFMrQ%2F8c0vV9OcCDZnAv1t45ZP1Zyhb8avCNzNEa4mPynU6X8Mx8b4KHf4EiuxtugdP3PueXnVlk2YMEGVIFTptu6TRMJmEqCs6PJKX%2FbrMcUtXAmt4G7eXwPCK0wZqHnzerECaYqjgMfQFIK%2FLT9NksW96HNXy3XA57j2AY6Nv62VoQI5yBIU%2FlUniIiTkcC%2BRCp12XDdrD5QP%2FWPmWknYgfvurA%2BKyvmYGKRbAYE7hTkt7L5u9pcML54DmZWfNC%2BsDQBXRkgN50XwGvKrSb7ubu%2BxCeGoFGsVvzSgkqNF4FNx%2FWDZyAICFPww9%2F6d0wY6mAGWvK22c4%2BxrTFVnWI621UX4CSCwaCyVfzWfVveLnM%2Fo1KPPLkpleKh%2BwGVL%2BrP3xP5C8%2FjkjkTFnKpFDVyPpPXRQ%2F8k0vZy2kiPPsAaByfKjHscLnG%2Bbl9mpFCL15SwWCz1%2B3z8e2a8xKTi2tz%2F0N7pC3nHtBBbMJq4Oh3pGGL4OVYQVQEeAdFrW42JuBhLRGWj1BuuLxqpg%3D%3D&Expires=1785171274) - Prepared by Chief Engineering Review Board synthesis of four independent Phase 3B Deep Research pass...

3. [Phase3C_TrueMoist_SOP.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/b4ed255f-4496-41f5-986a-3f2990c0abc8/Phase3C_TrueMoist_SOP.md?AWSAccessKeyId=ASIA2F3EMEYEVELCGW3H&Signature=Q4Ezjn0Jtwdc5I33NIbHgQ92%2FFk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCdbTHCZJp7QKQ0utjGpV%2FloKJCTCwUgrYnr8jLrEZV1QIgPsN%2FHzh05jc9R9PL4g5glmtAX57TkUdQaWdYXboOPEUq8wQIURABGgw2OTk3NTMzMDk3MDUiDKruZiIPVZSYaW2TKyrQBNr7kaTdytNzJJvEtXhgEpvdD5JgKhLLpuosiCn8x%2BP7F%2F1Q4Unjij6zcOlonJk1UI3GIi7VD4bC%2FKCnedWCAFwB5j1aZUQM5NlQIb1dJ61cS2aHMcKF7n2oMGGw8DMR9iPfQaREthROByc5p3BzYrYJlkOG8%2FoL6NKasQowi3IG6Zsn9i3bryz0X5cnhhp1gFWvrOcg00ZLs%2BnxPdnDHW0FQS%2FlysrIhmq80ij2je4lkYabbFYhJbPYRbazSK9WxJyoNk6PEr97T2uAfF1E00koBhjYn0vHqAjqeV%2BrzBHEDCDDW%2BkRygmy2RlRUJK7LgOEzGrTly8Xrek6o%2BdysFG%2BrMGnytAA8tWXoBMeErLnUpn5zc1%2FxpX8%2B6xRs10DLjNWNMb5036Df1ou3R8FVQQgCGD8DdOVpZnKPJeOUxh4WQlwmuV0VMH6PVClW%2FJaspOAWwLIJGw5C414VjgR%2BXiYjO8%2BvUFMrQ%2F8c0vV9OcCDZnAv1t45ZP1Zyhb8avCNzNEa4mPynU6X8Mx8b4KHf4EiuxtugdP3PueXnVlk2YMEGVIFTptu6TRMJmEqCs6PJKX%2FbrMcUtXAmt4G7eXwPCK0wZqHnzerECaYqjgMfQFIK%2FLT9NksW96HNXy3XA57j2AY6Nv62VoQI5yBIU%2FlUniIiTkcC%2BRCp12XDdrD5QP%2FWPmWknYgfvurA%2BKyvmYGKRbAYE7hTkt7L5u9pcML54DmZWfNC%2BsDQBXRkgN50XwGvKrSb7ubu%2BxCeGoFGsVvzSgkqNF4FNx%2FWDZyAICFPww9%2F6d0wY6mAGWvK22c4%2BxrTFVnWI621UX4CSCwaCyVfzWfVveLnM%2Fo1KPPLkpleKh%2BwGVL%2BrP3xP5C8%2FjkjkTFnKpFDVyPpPXRQ%2F8k0vZy2kiPPsAaByfKjHscLnG%2Bbl9mpFCL15SwWCz1%2B3z8e2a8xKTi2tz%2F0N7pC3nHtBBbMJq4Oh3pGGL4OVYQVQEeAdFrW42JuBhLRGWj1BuuLxqpg%3D%3D&Expires=1785171274) - - Project Project mC - Concept TrueMoist - Phase 3C Engineering Architecture Definition - Status Act...

4. [Monitoring soil water content and its salinity with high-precision and low-cost in-situ sensors](https://www.tandfonline.com/doi/full/10.1080/19648189.2022.2051076) - The article presents an in situ sensor to monitor soil moisture and water salinity by measuring soil...

5. [Designing Low-Cost Capacitive-Based Soil Moisture Sensor ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC8399650/) - Precise and quick estimates of soil moisture content for the purpose of irrigation scheduling are fu...

6. [Phase3B_MEMORY.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/9f5cfc9c-30a5-4af0-af19-64aab897f25a/Phase3B_MEMORY.md?AWSAccessKeyId=ASIA2F3EMEYEVELCGW3H&Signature=Lg1RJCaylhim5RojPg9NMfAjioU%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCdbTHCZJp7QKQ0utjGpV%2FloKJCTCwUgrYnr8jLrEZV1QIgPsN%2FHzh05jc9R9PL4g5glmtAX57TkUdQaWdYXboOPEUq8wQIURABGgw2OTk3NTMzMDk3MDUiDKruZiIPVZSYaW2TKyrQBNr7kaTdytNzJJvEtXhgEpvdD5JgKhLLpuosiCn8x%2BP7F%2F1Q4Unjij6zcOlonJk1UI3GIi7VD4bC%2FKCnedWCAFwB5j1aZUQM5NlQIb1dJ61cS2aHMcKF7n2oMGGw8DMR9iPfQaREthROByc5p3BzYrYJlkOG8%2FoL6NKasQowi3IG6Zsn9i3bryz0X5cnhhp1gFWvrOcg00ZLs%2BnxPdnDHW0FQS%2FlysrIhmq80ij2je4lkYabbFYhJbPYRbazSK9WxJyoNk6PEr97T2uAfF1E00koBhjYn0vHqAjqeV%2BrzBHEDCDDW%2BkRygmy2RlRUJK7LgOEzGrTly8Xrek6o%2BdysFG%2BrMGnytAA8tWXoBMeErLnUpn5zc1%2FxpX8%2B6xRs10DLjNWNMb5036Df1ou3R8FVQQgCGD8DdOVpZnKPJeOUxh4WQlwmuV0VMH6PVClW%2FJaspOAWwLIJGw5C414VjgR%2BXiYjO8%2BvUFMrQ%2F8c0vV9OcCDZnAv1t45ZP1Zyhb8avCNzNEa4mPynU6X8Mx8b4KHf4EiuxtugdP3PueXnVlk2YMEGVIFTptu6TRMJmEqCs6PJKX%2FbrMcUtXAmt4G7eXwPCK0wZqHnzerECaYqjgMfQFIK%2FLT9NksW96HNXy3XA57j2AY6Nv62VoQI5yBIU%2FlUniIiTkcC%2BRCp12XDdrD5QP%2FWPmWknYgfvurA%2BKyvmYGKRbAYE7hTkt7L5u9pcML54DmZWfNC%2BsDQBXRkgN50XwGvKrSb7ubu%2BxCeGoFGsVvzSgkqNF4FNx%2FWDZyAICFPww9%2F6d0wY6mAGWvK22c4%2BxrTFVnWI621UX4CSCwaCyVfzWfVveLnM%2Fo1KPPLkpleKh%2BwGVL%2BrP3xP5C8%2FjkjkTFnKpFDVyPpPXRQ%2F8k0vZy2kiPPsAaByfKjHscLnG%2Bbl9mpFCL15SwWCz1%2B3z8e2a8xKTi2tz%2F0N7pC3nHtBBbMJq4Oh3pGGL4OVYQVQEeAdFrW42JuBhLRGWj1BuuLxqpg%3D%3D&Expires=1785171274) - Version 1.0 Status COMPLETE Methodology Version Phase 3B --- TITLE Project mC - Phase 3B Memory - En...

7. [Simulated Effects of Soil Temperature and Salinity on Capacitance Sensor Measurements](https://pmc.ncbi.nlm.nih.gov/articles/PMC3800364/) - Dielectric measurement techniques are used widely for estimation of water content in environmental m...

8. [Soil temperature (DS18B20) sensor probe](https://www.mgsuperlabs.co.in/estore/Soil-temperature-DS18B20-sensor-probe) - Buy Soil temperature (DS18B20) sensor probe in India at MG Super Labs

9. [Laboratory Calibration and Performance Evaluation of Low ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC7014303/) - Soil volumetric water content (VWC) is a vital parameter to understand several ecohydrological and e...

10. [A New Single-Shape Sensor for Capacitive Moisture and ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC7730333/) - Modern agriculture imposes the need for better knowledge of the soil moisture content to rationalize...

11. [Performance of the capacitive moisture sensor under different saline conditions](https://www.scielo.br/j/rca/a/XhFvbZGrWy7Z4NYGWMK9hRn/?lang=en) - ABSTRACT Capacitive methods for determining soil moisture are extremely practical and easily...

12. [Phase2_Report-by-CLaude.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/611ecba7-701b-477e-b44c-9075dac6f4f4/Phase2_Report-by-CLaude.md?AWSAccessKeyId=ASIA2F3EMEYEVELCGW3H&Signature=On8od7kjX0GePtP7jOSTI7L%2BuAM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCdbTHCZJp7QKQ0utjGpV%2FloKJCTCwUgrYnr8jLrEZV1QIgPsN%2FHzh05jc9R9PL4g5glmtAX57TkUdQaWdYXboOPEUq8wQIURABGgw2OTk3NTMzMDk3MDUiDKruZiIPVZSYaW2TKyrQBNr7kaTdytNzJJvEtXhgEpvdD5JgKhLLpuosiCn8x%2BP7F%2F1Q4Unjij6zcOlonJk1UI3GIi7VD4bC%2FKCnedWCAFwB5j1aZUQM5NlQIb1dJ61cS2aHMcKF7n2oMGGw8DMR9iPfQaREthROByc5p3BzYrYJlkOG8%2FoL6NKasQowi3IG6Zsn9i3bryz0X5cnhhp1gFWvrOcg00ZLs%2BnxPdnDHW0FQS%2FlysrIhmq80ij2je4lkYabbFYhJbPYRbazSK9WxJyoNk6PEr97T2uAfF1E00koBhjYn0vHqAjqeV%2BrzBHEDCDDW%2BkRygmy2RlRUJK7LgOEzGrTly8Xrek6o%2BdysFG%2BrMGnytAA8tWXoBMeErLnUpn5zc1%2FxpX8%2B6xRs10DLjNWNMb5036Df1ou3R8FVQQgCGD8DdOVpZnKPJeOUxh4WQlwmuV0VMH6PVClW%2FJaspOAWwLIJGw5C414VjgR%2BXiYjO8%2BvUFMrQ%2F8c0vV9OcCDZnAv1t45ZP1Zyhb8avCNzNEa4mPynU6X8Mx8b4KHf4EiuxtugdP3PueXnVlk2YMEGVIFTptu6TRMJmEqCs6PJKX%2FbrMcUtXAmt4G7eXwPCK0wZqHnzerECaYqjgMfQFIK%2FLT9NksW96HNXy3XA57j2AY6Nv62VoQI5yBIU%2FlUniIiTkcC%2BRCp12XDdrD5QP%2FWPmWknYgfvurA%2BKyvmYGKRbAYE7hTkt7L5u9pcML54DmZWfNC%2BsDQBXRkgN50XwGvKrSb7ubu%2BxCeGoFGsVvzSgkqNF4FNx%2FWDZyAICFPww9%2F6d0wY6mAGWvK22c4%2BxrTFVnWI621UX4CSCwaCyVfzWfVveLnM%2Fo1KPPLkpleKh%2BwGVL%2BrP3xP5C8%2FjkjkTFnKpFDVyPpPXRQ%2F8k0vZy2kiPPsAaByfKjHscLnG%2Bbl9mpFCL15SwWCz1%2B3z8e2a8xKTi2tz%2F0N7pC3nHtBBbMJq4Oh3pGGL4OVYQVQEeAdFrW42JuBhLRGWj1BuuLxqpg%3D%3D&Expires=1785171274) - Prepared by Claude, acting as the Engineering RD IP Review Board synthesis function Inputs Phase 1C ...

13. [How capacitive moisture sensor works?](https://hackmd.io/@ampheo/how-capacitive-moisture-sensor-works) - A capacitive moisture sensor measures how much the material under test (soil, wood, air, etc.) chang...

14. [A Sensor to Monitor Soil Moisture, Salinity, and Temperature Profiles for Wireless Networks](https://pdfs.semanticscholar.org/22c8/3e25f04e5ffbd604a507f6d1fb448ebe7ac8.pdf)

15. [JOURNAL OF APPLIED](https://jurnal.polibatam.ac.id/index.php/JAGI/article/download/6545/2208)

16. [Capacitive Soil Moisture Sensor Explained + Demo](https://www.youtube.com/watch?v=UkJ1cks4ueA) - Get yours here: https://www.sparkfun.com/sparkfun-qwiic-soil-moisture-sensor-capacitive.html

This v...

17. [Phase2_Memory.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/334d1deb-985e-49da-b2ca-624f8e4b51e6/Phase2_Memory.md?AWSAccessKeyId=ASIA2F3EMEYEVELCGW3H&Signature=PN6pHKKS255HjZ7%2B2SzctJCvuCI%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCdbTHCZJp7QKQ0utjGpV%2FloKJCTCwUgrYnr8jLrEZV1QIgPsN%2FHzh05jc9R9PL4g5glmtAX57TkUdQaWdYXboOPEUq8wQIURABGgw2OTk3NTMzMDk3MDUiDKruZiIPVZSYaW2TKyrQBNr7kaTdytNzJJvEtXhgEpvdD5JgKhLLpuosiCn8x%2BP7F%2F1Q4Unjij6zcOlonJk1UI3GIi7VD4bC%2FKCnedWCAFwB5j1aZUQM5NlQIb1dJ61cS2aHMcKF7n2oMGGw8DMR9iPfQaREthROByc5p3BzYrYJlkOG8%2FoL6NKasQowi3IG6Zsn9i3bryz0X5cnhhp1gFWvrOcg00ZLs%2BnxPdnDHW0FQS%2FlysrIhmq80ij2je4lkYabbFYhJbPYRbazSK9WxJyoNk6PEr97T2uAfF1E00koBhjYn0vHqAjqeV%2BrzBHEDCDDW%2BkRygmy2RlRUJK7LgOEzGrTly8Xrek6o%2BdysFG%2BrMGnytAA8tWXoBMeErLnUpn5zc1%2FxpX8%2B6xRs10DLjNWNMb5036Df1ou3R8FVQQgCGD8DdOVpZnKPJeOUxh4WQlwmuV0VMH6PVClW%2FJaspOAWwLIJGw5C414VjgR%2BXiYjO8%2BvUFMrQ%2F8c0vV9OcCDZnAv1t45ZP1Zyhb8avCNzNEa4mPynU6X8Mx8b4KHf4EiuxtugdP3PueXnVlk2YMEGVIFTptu6TRMJmEqCs6PJKX%2FbrMcUtXAmt4G7eXwPCK0wZqHnzerECaYqjgMfQFIK%2FLT9NksW96HNXy3XA57j2AY6Nv62VoQI5yBIU%2FlUniIiTkcC%2BRCp12XDdrD5QP%2FWPmWknYgfvurA%2BKyvmYGKRbAYE7hTkt7L5u9pcML54DmZWfNC%2BsDQBXRkgN50XwGvKrSb7ubu%2BxCeGoFGsVvzSgkqNF4FNx%2FWDZyAICFPww9%2F6d0wY6mAGWvK22c4%2BxrTFVnWI621UX4CSCwaCyVfzWfVveLnM%2Fo1KPPLkpleKh%2BwGVL%2BrP3xP5C8%2FjkjkTFnKpFDVyPpPXRQ%2F8k0vZy2kiPPsAaByfKjHscLnG%2Bbl9mpFCL15SwWCz1%2B3z8e2a8xKTi2tz%2F0N7pC3nHtBBbMJq4Oh3pGGL4OVYQVQEeAdFrW42JuBhLRGWj1BuuLxqpg%3D%3D&Expires=1785171274)

18. [PROJECT_CONCEPT_CONTEXT.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/a978089e-09cc-4969-b16a-1a564fbd05c2/PROJECT_CONCEPT_CONTEXT.md?AWSAccessKeyId=ASIA2F3EMEYEVELCGW3H&Signature=DqxBApvNlH9IrTHwu8sggirLsS8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCdbTHCZJp7QKQ0utjGpV%2FloKJCTCwUgrYnr8jLrEZV1QIgPsN%2FHzh05jc9R9PL4g5glmtAX57TkUdQaWdYXboOPEUq8wQIURABGgw2OTk3NTMzMDk3MDUiDKruZiIPVZSYaW2TKyrQBNr7kaTdytNzJJvEtXhgEpvdD5JgKhLLpuosiCn8x%2BP7F%2F1Q4Unjij6zcOlonJk1UI3GIi7VD4bC%2FKCnedWCAFwB5j1aZUQM5NlQIb1dJ61cS2aHMcKF7n2oMGGw8DMR9iPfQaREthROByc5p3BzYrYJlkOG8%2FoL6NKasQowi3IG6Zsn9i3bryz0X5cnhhp1gFWvrOcg00ZLs%2BnxPdnDHW0FQS%2FlysrIhmq80ij2je4lkYabbFYhJbPYRbazSK9WxJyoNk6PEr97T2uAfF1E00koBhjYn0vHqAjqeV%2BrzBHEDCDDW%2BkRygmy2RlRUJK7LgOEzGrTly8Xrek6o%2BdysFG%2BrMGnytAA8tWXoBMeErLnUpn5zc1%2FxpX8%2B6xRs10DLjNWNMb5036Df1ou3R8FVQQgCGD8DdOVpZnKPJeOUxh4WQlwmuV0VMH6PVClW%2FJaspOAWwLIJGw5C414VjgR%2BXiYjO8%2BvUFMrQ%2F8c0vV9OcCDZnAv1t45ZP1Zyhb8avCNzNEa4mPynU6X8Mx8b4KHf4EiuxtugdP3PueXnVlk2YMEGVIFTptu6TRMJmEqCs6PJKX%2FbrMcUtXAmt4G7eXwPCK0wZqHnzerECaYqjgMfQFIK%2FLT9NksW96HNXy3XA57j2AY6Nv62VoQI5yBIU%2FlUniIiTkcC%2BRCp12XDdrD5QP%2FWPmWknYgfvurA%2BKyvmYGKRbAYE7hTkt7L5u9pcML54DmZWfNC%2BsDQBXRkgN50XwGvKrSb7ubu%2BxCeGoFGsVvzSgkqNF4FNx%2FWDZyAICFPww9%2F6d0wY6mAGWvK22c4%2BxrTFVnWI621UX4CSCwaCyVfzWfVveLnM%2Fo1KPPLkpleKh%2BwGVL%2BrP3xP5C8%2FjkjkTFnKpFDVyPpPXRQ%2F8k0vZy2kiPPsAaByfKjHscLnG%2Bbl9mpFCL15SwWCz1%2B3z8e2a8xKTi2tz%2F0N7pC3nHtBBbMJq4Oh3pGGL4OVYQVQEeAdFrW42JuBhLRGWj1BuuLxqpg%3D%3D&Expires=1785171274)

