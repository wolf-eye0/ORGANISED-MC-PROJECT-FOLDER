# VibeGuard Deep Research Brief: Precision 4-Stage Calibration & Surface-Invariant Vibration DSP

**Target System:** VibeGuard Autonomous Edge Vibration Monitoring & Fault Diagnostic Testbed  
**Target Hardware:** 7Semi ESP32-DEVKIT-E (ESP32-WROOM-32E @ 240 MHz) + Robocraze ADXL345 (4-Wire SPI Mode 2 @ 800 Hz)  
**Actuator Rig:** 12V N20 Micro Metal Gear Motor (600 RPM nominal) + 12 mm radius eccentric arm (FAB-01) + rigid sensor bracket (FAB-02)  
**Date:** October 2026  

---

## 1. Executive Problem Statement & Engineering Objective

VibeGuard is an industrial-grade edge vibration monitoring testbed designed to demonstrate ISO 10816-3 severity tracking and early mechanical fault progression across **four discrete operating stages**:

1. **Stage 0 (Bare Arm):** Normal / Healthy Baseline (0.0 g added mass).
2. **Stage 1 (M3x20mm Bolt Alone):** Incipient Fault / Warning Level ($\approx +2.5\text{ g}$ mass at $r = 12\text{ mm}$).
3. **Stage 2 (M3 Bolt + 1 Steel Nut):** Moderate Fault / Elevated Imbalance ($\approx +3.4\text{ g}$ mass).
4. **Stage 3 (M3 Bolt + 2 Steel Nuts):** Severe Imbalance / Critical Alarm ($\approx +4.3\text{ g}$ mass).

### The Real-World Engineering Failure Modes Observed:
1. **Surface / Substrate Sensitivity (Transmissibility Drift):**  
   When the testbed baseplate is moved from a wooden lab bench to an acrylic display panel or a metallic surface, the baseline vibration reading shifts significantly ($\Delta \text{RMS} \pm 25-35\%$) due to changing structural stiffness and boundary damping. Hardcoded absolute thresholds fail immediately upon moving the rig.
2. **Spur Gear Tooth Chatter vs. Unbalance SNR:**  
   The N20 gearbox operates with high-frequency spur gear tooth meshing ($150 - 350\text{ Hz}$) that produces a flat isotropic vibration floor ($\approx 0.65 - 0.70\text{ g}$). The rotational unbalance is low frequency ($1\times$ shaft rate $\approx 10 - 15\text{ Hz}$). In standard broad-band Vector RMS ($\sqrt{R_x^2 + R_y^2 + R_z^2}$), the gear noise dominates the unbalance delta.
3. **Rotordynamic Motor Drag (Bushing Speed Sag):**  
   Because centrifugal force is $F = m \cdot r \cdot \omega^2$, adding eccentric mass increases radial bushing friction on the micro motor, causing shaft speed $\omega$ to drop slightly. The reduction in $\omega^2$ partially offsets the mass increase $m$ in broad-band RMS, compressing the contrast between Stage 1, Stage 2, and Stage 3 to as little as $30 - 50\text{ mg}$.
4. **Transient Mechanical Spikes & Handling Shocks:**  
   Bumping the testbed, touching the power cable, or switching transients create high-crest-factor spikes ($> 2.5\text{ g}$) that can cause false alarm trips if simple thresholding or under-damped filtering is used.

### The Objective:
Develop a **robust, placement-invariant, mathematically rigorous calibration and classification engine** that:
- Executes deterministically on the ESP32 in C++ under real-time constraints (800 Hz ODR, 128-sample windows = 160 ms budget).
- Automatically normalizes out substrate/mounting surface differences.
- Discard transient spikes while providing sub-2-second reaction times to genuine physical mass changes.
- Clearly, repeatability, and non-overlappingly separates all 4 stages with guaranteed mathematical margins.

---

## 2. Hardware Architecture & Empirical Signal Parameters

### 2.1 Microcontroller & Acquisition Parameters
- **MCU:** Espressif ESP32-WROOM-32E (Tensilica Xtensa Dual-Core 32-bit LX6 @ 240 MHz).
- **Available SRAM:** ~320 KB heap, ~512 KB SRAM. Real-time budget per window: $< 15\text{ ms}$.
- **Persistent Storage:** ESP32 Non-Volatile Storage (Preferences / NVRAM).
- **Sensor:** Analog Devices ADXL345 3-Axis Digital MEMS Accelerometer.
- **Bus Interface:** Hardware SPI Mode 2 (CPOL=1, CPHA=0), 1 MHz clock, 4-wire configuration:
  - `SCK`: GPIO 18, `MOSI`: GPIO 23, `MISO`: GPIO 19, `CS`: GPIO 21.
- **Sampling Rate (ODR):** 800 Hz ($T_s = 1250\ \mu\text{s}$).
- **Dynamic Range:** $\pm 16\text{ g}$ Full Resolution ($3.90625\text{ mg/LSB}$).
- **Analysis Window:** $N = 128$ samples ($160\text{ ms}$ window length).
- **Physical Cycle Integration:** At 600 RPM ($10\text{ Hz}$ rotational frequency), a 160 ms window captures exactly 1.6 full shaft rotations.

### 2.2 Empirical Sensor Measurements (Logged from Physical Testbed)
Direct telemetry captures across the orthogonal axes ($X$ = transverse horizontal, $Y$ = vertical rocking against mounting screws, $Z$ = axial along shaft):

| Feature / Axis | Stage 0 (Bare Arm) | Stage 1 (Bolt Only) | Stage 2 (Bolt + 1 Nut) | Stage 3 (Bolt + 2 Nuts) | Physical Mechanism |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **$R_x$ (Transverse Horizontal)** | $0.244 \pm 0.017\text{ g}$ | $0.462 \pm 0.044\text{ g}$ | $0.475 \pm 0.046\text{ g}$ | $0.490 \pm 0.049\text{ g}$ | Surges upon adding initial bolt; flattens out |
| **$R_y$ (Vertical Rocking)** | $0.587 \pm 0.030\text{ g}$ | $0.619 \pm 0.071\text{ g}$ | $0.670 \pm 0.082\text{ g}$ | $0.725 \pm 0.098\text{ g}$ | Monotonically surges as mass increases (vertical couple) |
| **$R_z$ (Shaft Axial Thrust)** | $0.236 \pm 0.005\text{ g}$ | $0.178 \pm 0.010\text{ g}$ | $0.195 \pm 0.010\text{ g}$ | $0.212 \pm 0.010\text{ g}$ | High-frequency spur gear axial thrust slop |
| **Raw Broad-Band 3D RMS** | $\mathbf{0.679 \pm 0.028\text{ g}}$ | $\mathbf{0.792 \pm 0.035\text{ g}}$ | $\mathbf{0.860 \pm 0.040\text{ g}}$ | $\mathbf{0.935 \pm 0.045\text{ g}}$ | Standard scalar norm $\sqrt{R_x^2 + R_y^2 + R_z^2}$ |
| **Planar Asymmetry ($R_y - R_x$)** | $+0.344\text{ g}$ (baseline mount flex) | $+0.158\text{ g}$ | $+0.195\text{ g}$ | $+0.235\text{ g}$ | Inverted between S0 and S1 due to $R_x$ doubling |
| **Peak Impact Vector** | $1.76 \pm 0.35\text{ g}$ | $2.95 \pm 0.82\text{ g}$ | $3.20 \pm 0.85\text{ g}$ | $3.54 \pm 0.91\text{ g}$ | Unbalance impacts against bracket stops |
| **Crest Factor ($\text{Peak}/\text{RMS}$)** | $2.4 - 2.8$ | $3.2 - 4.1$ | $3.5 - 4.4$ | $3.8 - 5.3$ | Elevated impulsiveness with heavier unbalance |

---

## 3. Core Technical Research Inquiries

The deep research investigation must resolve four fundamental domains:

### Domain 1: Surface & Substrate Invariant Feature Formulation
- **The Problem:** When the baseboard is clamped or placed on acrylic vs wood, the entire baseline shifts upwards or downwards by $0.15 - 0.25\text{ g}$. Absolute thresholds immediately produce false warnings or miss alarms.
- **Research Question:** What mathematical normalization techniques (e.g., dimensionless ratios $V / V_{\text{base}}$, relative energy indices, baseline spectral cancellation, normalized rotordynamic harmonic ratios, or adaptive drift-compensating baselines) allow the classifier to remain invariant to substrate transmissibility?

### Domain 2: Noise-Immune $1\times$ Rotational Imbalance Demodulation
- **The Problem:** The N20 micro motor has no tachometer or encoder. Shaft speed fluctuates between 9 Hz and 13 Hz depending on battery/supply voltage and mechanical friction. High-frequency spur gear tooth meshing ($150 - 350\text{ Hz}$) injects broad-band noise.
- **Research Question:** How can an ESP32 extract the synchronous rotational unbalance component ($1\times$) in real-time without an optical tachometer?
  - Options to evaluate: Software sensorless tachometer (dominant peak tracking via zero-crossing / autocorrelation), recursive low-pass / bandpass IIR biquad filters, synchronous energy demodulation, or spectral kurtosis debiasing.

### Domain 3: Transient Spike Rejection & Hysteresis State Machine
- **The Problem:** External shocks (table taps, handling vibrations) produce short transient spikes. If smoothed too aggressively with a heavy low-pass filter, the system takes $> 10\text{ seconds}$ to detect a real mass change. If smoothed too lightly, table bumps trigger false alarms.
- **Research Question:** What is the optimal statistical filter and hysteresis engine (e.g., dual-rate asymmetric exponential moving average, trimmed Huber/Tukey estimator, Kalman filter with innovation-gating, or persistent sliding window counter) that:
  - Rejects $100\%$ of single-window shock spikes ($< 300\text{ ms}$).
  - Reliably converges to a true physical state change in under $1.5\text{ seconds}$.
  - Prevents state chatter/flicker at stage boundaries.

### Domain 4: Automated 4-Stage Calibration Protocol
- **The Problem:** Requiring a human engineer to hand-tune float thresholds for every motor rig is unscalable and error-prone.
- **Research Question:** What is the optimal mathematical workflow for an on-device guided calibration routine?
  - Specifically: How should the system learn Stage 0 (Healthy Baseline) and establish adaptive boundary margins for Stage 1, Stage 2, and Stage 3?
  - Can statistical dispersion metrics (e.g., Median Absolute Deviation $\text{MAD}$, interquartile range $\text{IQR}$, or variance modeling) automatically synthesize robust, non-overlapping threshold ladders?

---

## 4. Deliverable Format Expected from Deep Research

The deep research model should output:
1. **Mathematical Derivation & Equations:** Clear formulation of the proposed feature metric $J_{\text{condition}}$, normalization equation, and threshold boundaries.
2. **DSP Pipeline Flowchart:** Step-by-step block diagram from raw 800 Hz samples $\to$ DC removal $\to$ feature calculation $\to$ outlier rejection $\to$ condition classification.
3. **ESP32 C++ Production Implementation:** Clean, optimized, non-blocking C++ code snippet suitable for direct inclusion in `VibeGuard_Autotune_Synchronized.ino`.
4. **Comparative Trade-Off Matrix:** Comparison against standard ISO 10816-3 RMS, envelope analysis, and bandpass filtering in terms of CPU cycles, memory, and substrate resilience.
