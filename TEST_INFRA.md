# E2E Test Infra: VibeGuard 3D Digital Twin

## Test Philosophy
- **Opaque-Box & Requirement-Driven**: Derived strictly from `ORIGINAL_REQUEST.md` and user specifications, not internal implementation code.
- **Methodology**: Systematic 4-tier approach (Category-Partition, Boundary Value Analysis, Pairwise Combinatorial Testing, Real-World Workload Testing).
- **Execution Harness**: Automated dual test runner:
  1. Headless Browser Runner: Mozilla Firefox 152.0.6 (`firefox --headless --profile ... --screenshot ... file://...`) to verify WebGL context creation, 60 FPS rendering, DOM/Canvas element existence, and visual rendering without console errors.
  2. Mathematical & Protocol Verification Suite: Node.js test runner executing pure black-box verification of the DSP algorithms, FFT bin precision ($f_0 = \text{RPM}/60$), Hann windowing, ISO 10816 thresholds, Lissajous orbits, and RFC 4180 CSV export compliance.

---

## Feature Inventory & Test Tier Mapping
| # | Feature | Source (Requirement) | Tier 1 (Feature) | Tier 2 (Boundary) | Tier 3 (Pairwise) | Tier 4 (Scenario) |
|---|---------|----------------------|:----------------:|:-----------------:|:-----------------:|:-----------------:|
| 1 | CAD Assembly Mesh Hierarchy | R1 | 5 | 5 | ✓ | ✓ |
| 2 | Studio Lighting & Shadows | R1 | 5 | 5 | ✓ | ✓ |
| 3 | 360° Orbit Camera Controls | R1 | 5 | 5 | ✓ | ✓ |
| 4 | Raycast Click-to-Inspect | R2 | 5 | 5 | ✓ | ✓ |
| 5 | Sliding Component Inspector | R2 | 5 | 5 | ✓ | ✓ |
| 6 | Variable RPM Shaft Rotation | R3 | 5 | 5 | ✓ | ✓ |
| 7 | Dynamic 3D Rig Vibration | R3 | 5 | 5 | ✓ | ✓ |
| 8 | Dynamic 3D Vector Arrow | R3 | 5 | 5 | ✓ | ✓ |
| 9 | Unbalance Fault Injection | R3 | 5 | 5 | ✓ | ✓ |
| 10 | Misalignment Fault Injection | R3 | 5 | 5 | ✓ | ✓ |
| 11 | Bearing Fault Injection | R3 | 5 | 5 | ✓ | ✓ |
| 12 | Looseness / Rubbing Injection | R3 | 5 | 5 | ✓ | ✓ |
| 13 | SPI Sensor Disconnect Fault | R3, R4 | 5 | 5 | ✓ | ✓ |
| 14 | In-Place DC Removal | C++ features.cpp | 5 | 5 | ✓ | ✓ |
| 15 | 3-Axis Euclidean Vector RMS | C++ features.cpp | 5 | 5 | ✓ | ✓ |
| 16 | Peak Accel & Crest Factor | R4 | 5 | 5 | ✓ | ✓ |
| 17 | Hann Windowing | C++ features.cpp | 5 | 5 | ✓ | ✓ |
| 18 | Cooley-Tukey Radix-2 FFT | C++ features.cpp | 5 | 5 | ✓ | ✓ |
| 19 | Dominant Peak & Harmonics | C++ features.cpp | 5 | 5 | ✓ | ✓ |
| 20 | ISO 10816 Severity Integration | ISO 10816-3 | 5 | 5 | ✓ | ✓ |
| 21 | K-out-of-M Persistence Engine | C++ state.cpp | 5 | 5 | ✓ | ✓ |
| 22 | Lissajous Orbit Integration | R4 | 5 | 5 | ✓ | ✓ |
| 23 | Real-Time Waveform Oscilloscope | R4 | 5 | 5 | ✓ | ✓ |
| 24 | FFT Spectrogram Display | R4 | 5 | 5 | ✓ | ✓ |
| 25 | 2D/3D Lissajous Orbit Plotter | R4 | 5 | 5 | ✓ | ✓ |
| 26 | Digital Readouts & ISO Badge | R4 | 5 | 5 | ✓ | ✓ |
| 27 | Virtual RGB LED Point Light | R4 | 5 | 5 | ✓ | ✓ |
| 28 | Simulation Playback Controls | R3 | 5 | 5 | ✓ | ✓ |
| 29 | Telemetry Session Recorder | R5 | 5 | 5 | ✓ | ✓ |
| 30 | CSV Time-Series Exporter | R5 | 5 | 5 | ✓ | ✓ |
| 31 | JSON Diagnostic Report Exporter | R5 | 5 | 5 | ✓ | ✓ |
| 32 | Viewport Screenshot Snapshot | R5 | 5 | 5 | ✓ | ✓ |
| 33 | Zero-CDN Standalone Packaging | R6 | 5 | 5 | ✓ | ✓ |

---

## Test Architecture
- **Location**: `/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/Visual_Digital_Twin/tests/`
- **Master Test Runner**: `node /home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/Visual_Digital_Twin/tests/run_all_e2e_tests.js`
- **Pass/Fail Semantics**: All test suites must pass with exit code 0. Any assertion failure, precision error ($>1\%$), NaN/infinite value, or unhandled exception fails the suite.

---

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Description & Acceptance Benchmark |
|---|----------|--------------------|-----------------------------------|
| 1 | Commissioning Baseline Validation | F1, F2, F3, F6, F14, F15, F26, F27 | Normal balanced run at 600 RPM ($f_0 = 10.0\text{ Hz}$). Verify $RMS < 0.35g$, Green LED, clean circular orbit, Zone A. |
| 2 | Heavy Unbalance Degradation & Trip | F6, F7, F8, F9, F15, F18, F19, F21, F26, F27 | Ramp mass from 0.0g to 4.5g at 900 RPM ($15.0\text{ Hz}$). Verify $RMS > 0.70g$, Red LED trigger after $K=3$ windows, dominant peak at 15.0 Hz. |
| 3 | Coupling Misalignment Investigation | F10, F18, F19, F22, F25 | Inject shaft misalignment at 600 RPM. Verify $2X$ (20.0 Hz) harmonic peak $> 50\%$ of $1X$ peak, figure-8 Lissajous orbit. |
| 4 | Bearing Race Spall Defect Identification | F11, F16, F18, F19, F26 | Inject BPFO fault at 600 RPM ($f_{BPFO} = 30.5\text{ Hz}$). Verify sharp impulse crest factor ($CF > 3.5$), BPFO spectral sidebands. |
| 5 | Mechanical Looseness & Chattering | F12, F18, F19, F22, F25 | Inject looseness. Verify $0.5X$ subharmonic ($5.0\text{ Hz}$ at 600 RPM), dense harmonic comb, asymmetric chaotic orbit. |
| 6 | Broken Sensor SPI Disconnect Alarm | F13, F21, F26, F27 | Trigger SPI bus fault. Verify instant $0g$ flatline, register error state, flashing Magenta LED, `FaultInvalid` badge. |
| 7 | Flight Recording & CSV Telemetry Audit | F29, F30, F31, F32 | Record 10s session under dynamic fault, export CSV. Parse exported CSV; verify RFC 4180 headers, chronological timestamps ($1.25\text{ ms}$ intervals), valid numeric columns. |
| 8 | Complete Standalone Offline Execution | F33, F1, F4, F23, F24, F25 | Headless browser execution on local `file://` URL without internet access. Verify 60 FPS WebGL rendering, canvas HUD updates, zero network errors. |

---

## Coverage Thresholds
- **Tier 1 (Feature Coverage)**: $\ge 165$ test cases ($\ge 5$ per feature across all 33 features).
- **Tier 2 (Boundary & Corner Cases)**: $\ge 165$ test cases (min/max RPM, 0.0g vs 5.0g mass, DC offset edge, noise limit, buffer overflow).
- **Tier 3 (Cross-Feature Combinations)**: $\ge 33$ pairwise interaction tests (RPM scaling $\times$ Fault modes, Recording $\times$ Fault transitions, Raycasting $\times$ Playback states).
- **Tier 4 (Real-World Scenarios)**: $\ge 8$ complete end-to-end operational workflows.
- **Total Test Suite Target**: $\ge 371$ test cases.
