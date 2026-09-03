# Project: VibeGuard 3D WebGL Digital Twin & Real-Time DSP Telemetry Simulator

## Architecture
VibeGuard 3D Digital Twin is an industrial-grade, standalone WebGL hardware digital twin and real-time DSP vibration telemetry simulator designed as an interactive physical hardware replacement for the VibeGuard edge monitoring system (ESP32-DevKitC-32E + ADXL345 4-Wire SPI + 12V N20 motor rig).

```
VibeGuard_3D_Digital_Twin.html (Standalone Zero-Dependency Bundle)
├── 3D WebGL Rendering Engine (Three.js r128 + OrbitControls)
│   ├── Procedural CAD Hardware Hierarchy (L-Bracket, N20 Motor, D-Shaft, Eccentric Mass, ADXL345, ESP32, SPI Ribbon)
│   ├── Studio Lighting System (Key Light, Fill Light, Top Spot, Ambient, Dynamic PointLight)
│   ├── Interactive Raycaster (Component picking, smooth camera focus lerp)
│   └── Dynamic 3D Vector Arrow & Rig Vibration Displacements
│
├── Real-Time Kinematics & Physics Engine
│   ├── Variable RPM Shaft Kinematics (300 to 1200 RPM, f0 = 5.0 to 20.0 Hz)
│   ├── Multi-Fault Synthetic Signal Generator (800 Hz ODR)
│   │   ├── Rotor Unbalance (1X Centrifugal Force F = m * r * w^2)
│   │   ├── Shaft Misalignment (1X + 2X Harmonics & 180° Phase Shift)
│   │   ├── Rolling Element Bearing Faults (BPFO = 3.05*f0, BPFI = 4.95*f0 Impact Pulses)
│   │   ├── Mechanical Looseness & Rubbing (0.5X Sub-harmonics & Comb Spectrum)
│   │   └── SPI Bus Disconnect / Line Float
│   └── 3D Rig Group Positional Perturbation & Orbital Precession
│
├── Edge DSP & Signal Processing Subsystem (TypedArray Zero-Allocation)
│   ├── Pre-allocated Float32Array Circular Ring Buffers (N = 256, Fs = 800 Hz)
│   ├── In-Place DC Bias Removal (Zero-mean dynamic AC vibration)
│   ├── Triaxial Euclidean Vector RMS (RMS_vec = sqrt(RMS_x^2 + RMS_y^2 + RMS_z^2))
│   ├── Peak Acceleration, Peak-to-Peak, and Crest Factor (CF = Peak / RMS)
│   ├── 4th-Order Kurtosis Shock Index (Spall / Impact Detection)
│   ├── Drift-Free Double Numerical Integration (Accel -> Vel mm/s -> Disp µm with IIR HPF)
│   ├── In-Place Cooley-Tukey Radix-2 Real FFT with Hann Windowing & Twiddle LUTs
│   ├── Dominant Peak Frequency Tracking & 1X/2X/3X Harmonic Extraction
│   ├── ISO 10816-1 / ISO 10816-3 Machinery Severity Zone Classification (Zones A, B, C, D)
│   └── K-out-of-M Persistence State Machine (K=3 of M=5 consecutive abnormal windows)
│
├── Telemetry HUD & Diagnostics Display Subsystem (Pure Canvas 2D)
│   ├── High-Performance Multi-Channel Oscilloscope (X Cyan, Y Magenta, Z Yellow, |a| Green)
│   ├── Real-Time FFT Spectrogram with Harmonic Peak Indicators & Zoom Modes
│   ├── Dynamic 2D/3D Lissajous Shaft Orbit Trajectory Plotter with ISO Clearance Circles
│   ├── Digital Telemetry KPI Cards (Vector RMS, Peak, Crest Factor, Kurtosis, Velocity RMS)
│   ├── ISO 10816 Severity Status Badges (Good Green, Warning Amber, Alarm Red, Fault Magenta)
│   └── Synchronized 3D ESP32 RGB LED Point Light Illumination
│
├── User Controls & Interaction Subsystem
│   ├── Industrial Cyberpunk Glassmorphism UI Overlay & Responsive Layout
│   ├── Plant Operating Controls (RPM Slider, Eccentric Mass Slider, Fault Mode Selector, Damping/Noise)
│   ├── Sliding Component Engineering Inspector Drawer (Datasheets, Pinouts, Live Registers)
│   └── Simulation Playback Controls (Pause, Resume, Reset, Time Scaling)
│
└── Flight Telemetry Recorder & Data Exporter
    ├── Rolling 30-Second In-Memory Session Buffer (24,000 samples @ 800 Hz)
    ├── One-Click RFC 4180 Compliant CSV Time-Series Exporter
    ├── One-Click Structured JSON Diagnostic Report Exporter
    └── Canvas Viewport PNG Screenshot Capture
```

---

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | CAD Assembly Mesh Hierarchy | Procedural 3D models for L-Bracket, N20 Motor, Gearbox, Shaft, Eccentric Hub, ADXL345, ESP32, RGB LED, SPI Wires | M1 | ORIGINAL_REQUEST.md R1 |
| 2 | Studio Lighting & Shadows | 3-point studio lighting (Key, Fill, Spot, Ambient) with PCF soft shadows and specular highlights | M1 | ORIGINAL_REQUEST.md R1 |
| 3 | 360° Orbit Camera Controls | Smooth spherical coordinate camera rotation, pan, zoom with damping and polar angle constraints | M1 | ORIGINAL_REQUEST.md R1 |
| 4 | Raycast Click-to-Inspect | Mouse raycaster detects clicked hardware part, animates camera focus, highlights mesh | M5 | ORIGINAL_REQUEST.md R2 |
| 5 | Sliding Component Inspector | Glassmorphism panel displaying component datasheet, voltage, pinouts, live register/telemetry | M5 | ORIGINAL_REQUEST.md R2 |
| 6 | Variable RPM Shaft Rotation | Continuous rotation of motor shaft and eccentric mass coupling matching RPM (300-1200 RPM) | M2 | ORIGINAL_REQUEST.md R3 |
| 7 | Dynamic 3D Rig Vibration | Physical shaking and orbital wobble of motor, bracket, and sensor proportional to unbalance mass | M2 | ORIGINAL_REQUEST.md R3 |
| 8 | Dynamic 3D Vector Arrow | 3D arrow radiating from ADXL345 chip indicating resultant dynamic acceleration magnitude & direction | M2 | ORIGINAL_REQUEST.md R3 |
| 9 | Unbalance Fault Injection | Synchronous 1X centrifugal rotating force F = m * r * w^2 generating orthogonal sinusoidal acceleration | M2 | ORIGINAL_REQUEST.md R3 |
| 10 | Misalignment Fault Injection | Angular and parallel shaft misalignment generating pronounced 1X and 2X harmonic vibration | M2 | ORIGINAL_REQUEST.md R3 |
| 11 | Bearing Fault Injection | Localized impact pulses at characteristic bearing defect frequencies (BPFO, BPFI, BSF, FTF) | M2 | ORIGINAL_REQUEST.md R3 |
| 12 | Looseness / Rubbing Injection | Structural loose foot and non-linear rubbing generating sub-harmonics (0.5X) and comb harmonics | M2 | ORIGINAL_REQUEST.md R3 |
| 13 | SPI Sensor Disconnect Fault | Simulates broken wiring or SPI bus communication failure (flatline, register error, alarm state) | M2 | ORIGINAL_REQUEST.md R3 |
| 14 | In-Place DC Removal | Eliminates static gravity (1.0g on Z) and sensor offset to isolate dynamic AC vibration | M3 | C++ features.cpp |
| 15 | 3-Axis Euclidean Vector RMS | Computes root-mean-square of total dynamic acceleration vector |a| = sqrt(ax^2 + ay^2 + az^2) | M3 | C++ features.cpp |
| 16 | Peak Accel & Crest Factor | Calculates true peak dynamic acceleration and shock impact index (CF = a_peak / RMS) | M3 | ORIGINAL_REQUEST.md R4 |
| 17 | Hann Windowing | Smooths window edges with Hann function to eliminate spectral leakage prior to FFT | M3 | C++ features.cpp |
| 18 | Cooley-Tukey Radix-2 FFT | Fast Fourier Transform converting 256 time-domain samples to 128 frequency bins (0 - 400 Hz) | M3 | C++ features.cpp |
| 19 | Dominant Peak & Harmonics | Scans spectrum for dominant peak frequency and quantifies 1X, 2X, 3X harmonic energy | M3 | C++ features.cpp |
| 20 | ISO 10816 Severity Integration | Integrates acceleration spectrum to velocity RMS (mm/s RMS) and maps to ISO severity zones | M3 | ISO 10816-3 |
| 21 | K-out-of-M Persistence Engine | State machine requiring K=3 of M=5 abnormal windows before triggering persistent alarm state | M3 | C++ state.cpp |
| 22 | Lissajous Orbit Integration | Integrates radial X and tangential Y acceleration into shaft center-line orbit trajectory | M3 | ORIGINAL_REQUEST.md R4 |
| 23 | Real-Time Waveform Oscilloscope | High-speed Canvas 2D oscilloscope displaying X, Y, Z, and Vector |a| traces with ISO threshold lines | M4 | ORIGINAL_REQUEST.md R4 |
| 24 | FFT Spectrogram Display | Canvas frequency spectrum display with color-coded bars, harmonic markers (1X, 2X, 3X), peak tag | M4 | ORIGINAL_REQUEST.md R4 |
| 25 | 2D/3D Lissajous Orbit Plotter | Polar/Cartesian orbit display showing shaft centerline precession, figure-8, and eccentricity | M4 | ORIGINAL_REQUEST.md R4 |
| 26 | Digital Readouts & ISO Badge | Real-time digital gauges for Vector RMS, Peak Accel, Crest Factor, 1X Freq, Velocity RMS, Status Badge | M4 | ORIGINAL_REQUEST.md R4 |
| 27 | Virtual RGB LED Point Light | Synchronized 3D point light & emissive sphere on ESP32 mesh mirroring hardware LED state | M4 | ORIGINAL_REQUEST.md R4 |
| 28 | Simulation Playback Controls | User controls for Pause, Resume, Reset, and Time Scaling (0.25X, 0.5X, 1.0X, 2.0X) | M5 | ORIGINAL_REQUEST.md R3 |
| 29 | Telemetry Session Recorder | Captures 10 to 30 seconds of high-frequency 800 Hz triaxial telemetry and DSP metrics into memory | M5 | ORIGINAL_REQUEST.md R5 |
| 30 | CSV Time-Series Exporter | Generates and triggers browser download of RFC 4180 compliant .csv time-series telemetry | M5 | ORIGINAL_REQUEST.md R5 |
| 31 | JSON Diagnostic Report Exporter | Generates structured .json session report with device info, session summary, FFT snapshot, raw data | M5 | ORIGINAL_REQUEST.md R5 |
| 32 | Viewport Screenshot Snapshot | Captures high-resolution PNG image of the 3D WebGL twin and HUD dashboard | M5 | ORIGINAL_REQUEST.md R5 |
| 33 | Zero-CDN Standalone Packaging | 100% offline self-contained single .html file embedding all JS engines, shaders, styles, fonts | M5 | ORIGINAL_REQUEST.md R6 |

---

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| E2E | E2E Testing Track | Requirement-driven test harness, automated test runner (Firefox headless & Node.js), Tiers 1-4 test scenarios, publish TEST_READY.md | none | IN_PROGRESS |
| M1 | 3D CAD Hardware Twin & Scene Rendering | Procedural Three.js 3D meshes for all 8 components, PBR materials, studio lighting, shadows, OrbitControls | none | PLANNED |
| M2 | Kinematics, Rig Vibration & Multi-Fault Signal Generator | Variable RPM shaft rotation, 3D rig vibration shaking & wobble, dynamic 3D acceleration vector arrow, 800 Hz multi-fault physics generator | M1 | PLANNED |
| M3 | TypedArray Zero-Allocation DSP Engine | Circular ring buffers, in-place DC removal, Vector RMS, Peak, Crest factor, Kurtosis, drift-free double numerical integration, Cooley-Tukey Radix-2 FFT with Hann window, ISO 10816 evaluation, persistence engine | M2 | PLANNED |
| M4 | Canvas 2D Telemetry HUD & Diagnostics Visualizers | High-performance Canvas 2D Oscilloscope, FFT Spectrogram with harmonic tags, Lissajous Orbit Plotter, ISO 10816 status badges, synchronized 3D RGB LED point light | M3 | PLANNED |
| M5 | Cyberpunk UI, Raycast Inspector, Flight Recorder & Standalone Integration | Glassmorphism controls, Raycast click-to-inspect & camera lerp, session recording & RFC 4180 CSV/JSON export, single-file standalone integration | M4 | PLANNED |
| M6 | Full E2E Verification & Adversarial Coverage Hardening | 100% pass of E2E test suite (Tiers 1-4), Tier 5 adversarial stress testing (Challenger), forensic audit verification | M5, E2E | PLANNED |

---

## Interface Contracts

### 1. Kinematics & Fault Generator $\rightarrow$ DSP Engine
```typescript
interface RawSample {
    timestampMs: number;
    sampleIndex: number;
    rpm: number;
    rawAx: number;  // g
    rawAy: number;  // g
    rawAz: number;  // g
}
```

### 2. DSP Engine Output $\rightarrow$ HUD & UI Controllers
```typescript
interface ProcessedTelemetryFrame {
    timestampMs: number;
    sampleIndex: number;
    rpm: number;
    fundamentalFreqHz: number;
    rawAccel: { x: number; y: number; z: number };
    acAccel: { x: number; y: number; z: number };
    velocity: { x: number; y: number; z: number };       // mm/s
    displacement: { x: number; y: number; z: number };   // µm
    vectorMag: number;
    vectorRms: number;
    peakAccel: number;
    peakToPeak: number;
    crestFactor: number;
    kurtosis: number;
    dominantFreqHz: number;
    dominantFreqMag: number;
    harmonicPeaks: { h1: number; h2: number; h3: number };
    isoZone: 'Zone_A' | 'Zone_B' | 'Zone_C' | 'Zone_D';
    systemState: 'Normal' | 'Warning' | 'Abnormal' | 'FaultInvalid';
    fftMagnitudes: Float32Array; // 128 bins
    fftFrequencies: Float32Array;
}
```

### 3. UI Controller $\rightarrow$ Physics & 3D Scene
```typescript
interface PlantControlState {
    rpm: number;                  // 300 to 1200 RPM
    faultMode: 'NORMAL' | 'UNBALANCE' | 'MISALIGNMENT' | 'BEARING_BPFO' | 'BEARING_BPFI' | 'LOOSENESS' | 'SPI_DISCONNECT';
    eccentricMassG: number;       // 0.0 to 5.0 g
    faultSeverityPct: number;     // 0 to 100%
    noiseStdDevG: number;         // 0.0 to 0.1 g
    isPaused: boolean;
    timeScale: number;            // 0.25 to 2.0
}
```

---

## Code Layout
- Target application file: `/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/Visual_Digital_Twin/VibeGuard_3D_Digital_Twin.html`
- E2E Test Suite directory: `/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/Visual_Digital_Twin/tests/`
- Test Infrastructure Document: `/home/paradoxpete/Documents/PROJECT_ORGANIZED/TEST_INFRA.md`
- Test Readiness Signal: `/home/paradoxpete/Documents/PROJECT_ORGANIZED/TEST_READY.md`
