# VibeGuard Micro Project Academic Report — Overleaf Package Guide

## 1. Executive Summary & Delivery Overview
- **Course Title:** `PBCST504 - MICROCONTROLLERS` (Micro Project Report)
- **Project Title:** *VibeGuard: An Embedded Vibration Condition Monitoring System*
- **Institution:** Jyothi Engineering College (Autonomous), Cheruthuruthy, Thrissur 679 531
- **University:** APJ Abdul Kalam Technological University (KTU), Kerala
- **Department:** Department of Computer Science & Engineering (Cyber Security)
- **Academic Term / Submission Date:** October 2026 (Semester 5 B.Tech)
- **Official Zip Package for Overleaf:** [`/home/paradoxpete/Downloads/VibeGuard_Overleaf_Report.zip`](file:///home/paradoxpete/Downloads/VibeGuard_Overleaf_Report.zip)
- **Repository LaTeX Source Tree:** [`07_SEMESTER_EXECUTION/06_Reports_and_Demonstration/VibeGuard_Overleaf_Report/`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/06_Reports_and_Demonstration/VibeGuard_Overleaf_Report/)

---

## 2. Team & Faculty Metadata

| Member Name | University Register No. | Project Role |
| :--- | :---: | :--- |
| **Amith Krishna Das** | `JEC24CC016` | Hardware, Electrical Safety & Rig Assembly Lead |
| **Archa Pramod** | `JEC24CC023` | Documentation, Demonstration & Reporting Lead |
| **Nihad P C** | `JEC24CC044` | Project Lead & Hardware-Software Integration Lead |
| **Sreehari K** | `JEC24CC055` | Embedded Firmware, DSP & Real-Time Analytics Lead |
| **Sreeprada K S** | `JEC24CC056` | Experimental Testing & Validation Protocol Lead |

- **Project Guide & Coordinator:** **Ms. Sagna L T**, Assistant Professor, Dept. of CSE (Cyber Security)
- **Head of Department:** **Dr. Geethu Mary George**, Associate Professor & HOD, Dept. of CSE (Cyber Security)
- **Principal:** **Dr. Sojan P Lal**, Principal, Jyothi Engineering College (Autonomous)

---

## 3. Package File Structure
The generated report follows a clean, modular LaTeX2e architecture compatible with pdfLaTeX / TeX Live on Overleaf:

```
VibeGuard_Overleaf_Report/
├── main.tex                                    # Master LaTeX root document (Frontmatter, Setup, Appendices)
├── references.bib                              # IEEE-formatted BibTeX citations database
├── logos/
│   ├── college_banner.png                      # Official Jyothi Engineering College Header Banner
│   └── college_crest.png                       # Official College Seal / Emblem
├── figures/
│   ├── fig_system_architecture.png             # Level-1 System Architecture Block Diagram
│   ├── fig_dsp_pipeline.png                    # Level-2 DSP & Finite State Machine Pipeline
│   ├── fig_circuit_schematic.png               # Master Electrical Schematic (ESP32 + ADXL345 + 12V Loop)
│   ├── fig_breadboard_wiring.png               # Complete Breadboard Layout with Decoupling Network
│   ├── fig_motor_safety_circuit.png            # 12V Motor Flyback Clamp (1N4007) & Fuse Circuit
│   ├── fig_baseplate_blueprint.png             # Certified 1:1 Acrylic Baseplate Drilling Blueprint
│   ├── fig_rotor_arm_fab01.png                 # Monolithic 3D-Printed Rotor Cam Arm (FAB-01)
│   ├── fig_sensor_mount_fab02.png              # Monolithic 3D-Printed Rigid Sensor L-Bracket (FAB-02)
│   └── fig_user_journey.png                    # Transition Journey: Manual -> Cloud -> VibeGuard Edge
└── chapters/
    ├── ch1_introduction.tex                    # Overview, Motivation, Problem Statement, Objectives, Scope
    ├── ch2_literature_review.tex               # CBM Evolution, ISO 10816, MEMS vs Piezo, SPI, DC/RMS/FFT
    ├── ch3_system_architecture.tex             # Nyquist Sampling, 4-Wire SPI, Power Isolation, BOD, FSM
    ├── ch4_hardware_and_mechanical.tex         # 7Semi ESP32, ADXL345, Acrylic Baseplate, 3D Solvents, BOM
    ├── ch5_firmware_and_dsp.tex                # Modular C++, DEVID 0xE5, Ping-Pong Buffers, Vector RMS, FFT
    ├── ch6_results_and_discussion.tex          # Bring-up, Normal Baseline, Unbalance Fault, Harmonics, Latency
    ├── ch7_advantages_and_challenges.tex       # Edge Autonomy, Mechanical/Electrical Fixes, Leakage Control
    └── ch8_conclusion_and_future_scope.tex      # Summary of Deliverables, CO/SDG Attainment, Future Trajectory
```

---

## 4. Institutional Frontmatter & Curricular Compliance
The report faithfully preserves all mandatory Jyothi Engineering College / KTU frontmatter components:
1. **Title Cover Page:** Official high-resolution top banner, course details, group members with register numbers, supervisor details, college crest, and KTU degree citation.
2. **Declaration:** Formal KTU declaration statement affirming academic integrity and zero data fabrication.
3. **Bonafide Certificate:** Department certification with designated signature blocks for Project Guide (Ms. Sagna L T), Project Coordinator (Ms. Sagna L T), and Head of Department (Dr. Geethu Mary George).
4. **College Vision & Mission:** Official institutional statements.
5. **Department Vision & Mission:** Department of Computer Science & Engineering (Cyber Security) Vision and Missions M1, M2, M3, and M4.
6. **Programme Outcomes (POs):** Complete NBA PO1 through PO11.
7. **PEOs & PSOs:** Department Programme Educational Objectives (PEO1--PEO3) and Programme Specific Objectives (PSO1--PSO3).
8. **Course Outcomes & PO-CO Mapping Matrix:** Explicit mapping of `PBCST504` CO1 through CO5 against PO1--PO11 and PSO1--PSO4 with correlation weights (1, 2, 3).
9. **Acknowledgement:** Formal institutional gratitude to Management, Principal Dr. Sojan P Lal, HOD Dr. Geethu Mary George, Coordinator Ms. Sagna L T, FabLab, and Workshop technicians.
10. **Sustainable Development Goals (SDGs):** Enumeration of all 17 UN SDGs followed by an extensive justification matrix covering **SDG 9** (Industry, Innovation & Infrastructure), **SDG 12** (Responsible Consumption & Production), and **SDG 8** (Decent Work & Economic Growth).
11. **Abstract:** Comprehensive 350-word technical abstract encapsulating sampling theory, vector RMS equations, persistence mechanics, and mechanical testbed fabrication.
12. **Nomenclature & Tables:** Table of Contents, List of Tables, List of Figures, List of Abbreviations, and List of Notations.

---

## 5. Technical Chapter Summary

### Chapter 1: Introduction
- Examines the industrial necessity for vibration condition monitoring in rotating assets (pumps, motors, compressors).
- Compares conventional approaches (expensive piezoelectric systems, bandwidth-heavy cloud streaming) with VibeGuard's edge-autonomous model.
- Outlines the 7 core project objectives, problem statement, and explicit scope boundaries (e.g., bounded to a guarded 12V test rig; no premature claims of bearing spall depth or multi-year RUL).

### Chapter 2: Literature Review & Theoretical Background
- Reviews maintenance paradigms: reactive $\rightarrow$ calendar preventive $\rightarrow$ condition-based predictive.
- Formulates the mechanical physics of rotating unbalance ($F = m \cdot r \cdot \omega^2$).
- Tabulates ISO 10816-3 vibration severity zones (A, B, C, D) for industrial machinery.
- Compares industrial piezoelectric transducers vs. ADXL345 capacitive MEMS sensors.
- Details SPI vs. $\mathrm{I^2C}$ bus timing constraints at 800\,Hz ODR.
- Mathematical formulations for DC gravity removal, single-axis RMS, triaxial Vector RMS, and the Cooley-Tukey Radix-2 FFT with Hann windowing.
- Analyzes temporal data leakage in machinery datasets and justifies session-level validation.

### Chapter 3: VibeGuard System Design & Architecture
- Details Level-1 and Level-2 block diagrams and the separation of continuous time-domain sampling from on-demand spectral processing.
- Establishes sampling parameters: 800\,Hz ODR yields a 400\,Hz Nyquist bandwidth ($\ge 40X$ of 10\,Hz shaft speed) and 3.125\,Hz spectral bin resolution across 256-sample windows.
- Elaborates electrical power isolation: 12V N20 motor loop isolated from the 3.3V/5.0V ESP32 rail, protected by a 1A fuse, KCD1 rocker switch, and 1N4007 flyback suppression diode.
- Decoupling network: 100\,$\mu$F bulk electrolytic + 100\,nF ceramic capacitor preventing ESP32 brownout detector resets (`rst:0x10`).
- Remaps SPI Chip Select from strapping pin GPIO5 to GPIO21 to eliminate bootloader bootloops.
- Defines the 5-state Finite State Machine (Self-Test, Calibrating, Normal, Abnormal, Fault).
- Outlines the standardized NMEA-style serial telemetry protocol at 115200 baud.

### Chapter 4: Hardware Implementation & Mechanical Testbed Fabrication
- Specifications of 7Semi ESP32-DEVKIT-E (dual-core Xtensa, 520\,KB SRAM, CP2102 bridge, 22.86\,mm breadboard clearance).
- ADXL345 Full-Resolution Mode ($\pm 4g$) with constant $3.9\,\text{mg/LSB}$ scale factor and 32-level Stream FIFO.
- 12V N20 gear motor characteristics (1:50 spur gearbox, 600\,RPM / 10.0\,Hz, 3.0\,mm D-shaft).
- 10\,mm laminated cast acrylic baseplate ($150 \times 150$\,mm, mass $\approx 265$\,g) with dual-datum precision coordinate matrix.
- 3D-printed monolithic solid components:
  - **FAB-01:** Rotor cam arm with 1.5\% shrinkage compensation (3.15\,mm bore), 12.0\,mm pitch, and calibrated M3 unbalance bolt counter-recess ($F = 0.0876$\,N).
  - **FAB-02:** Gusseted high-rigidity sensor L-bracket pushing resonance modes $>1.2$\,kHz.
  - **FAB-03:** Motor cradle shim (1.0\,mm) eliminating cantilever acoustic rattle.
- M3 through-bolting with nylon locknuts and silicone rubber benchtop isolation pads.
- Sourcing BOM ledger: \rupee 2,124.00 actual expenditure against the \rupee 3,000.00 ceiling.

### Chapter 5: Embedded Firmware & Digital Signal Processing
- Modular C++ architecture under Arduino-ESP32 / FreeRTOS.
- Hardware identity handshake: checking register `DEVID` for `0xE5`.
- Ping-Pong double buffering eliminating race conditions and buffer overruns at 800\,Hz.
- In-place two-pass zero-mean DC removal ($x'_i = x_i - \bar{x}$) converting acceleration to $g$.
- Composite Vector RMS calculation ($a_{\mathrm{vec}} = \sqrt{\mathrm{RMS}_x^2 + \mathrm{RMS}_y^2 + \mathrm{RMS}_z^2}$).
- Temporal $K$-of-$M$ persistence filtering ($K=4, M=5$) suppressing transient jolts while achieving $1.28$\,s alert latency.
- Triggered Cooley-Tukey Radix-2 FFT with compile-time Hann window lookup tables.
- Resource profiling: total RAM $<12$\,KB; DSP execution duration of $1.36$\,ms per 320\,ms window; CPU load $<0.43\%$.

### Chapter 6: Results, Testing & Discussion
- Static verification: multi-axis Earth gravity testing confirming $1.0g$ scaling on $+Z$ and $0g$ on $X/Y$.
- Baseline healthy calibration: mean baseline Vector RMS $\mu_{\mathrm{base}} = 0.0602\,g$, $\sigma_{\mathrm{base}} = 0.0058\,g$, yielding frozen threshold $\theta_{\mathrm{RMS}} = 0.081\,g$.
- Dynamic unbalance testing: attaching $1.85$\,g eccentric mass induces a \textbf{423\% increase} in Vector RMS ($0.315\,g$).
- Spectral harmonic extraction: unbalance produces a sharp 16-fold energy spike at the $1X$ fundamental frequency ($10.0$\,Hz).
- Persistence filter evaluation: screwdriver impact jolt rejected ($V=1 < 4$, LED stays Green); continuous unbalance asserted on window 4 at $t = 1.28$\,s (LED turns Red).
- Benchmarking matrix comparing VibeGuard with manual stethoscope, cloud IIoT, continuous embedded FFT, and supervised ML classifiers.

### Chapter 7: Advantages & Implementation Challenges
- Details core advantages: edge autonomy, physical explainability, multi-planar sensitivity, low cost, and strict data provenance.
- Examines mechanical resolutions: baseplate foundation rigidity, through-bolting, acoustic shim pads, monolithic rotor redesign, and FDM shrinkage compensation.
- Examines electrical resolutions: motor flyback clamping, brownout bulk decoupling, and GPIO21 strapping pin remapping.
- Algorithmic and validation governance: session-level splitting and on-demand triggered FFT execution.

### Chapter 8: Conclusion & Future Scope
- Summarizes project deliverables and milestone attainment.
- Verifies curriculum alignment with `PBCST504` CO1--CO5 and UN SDGs 9, 12, and 8.
- Outlines post-semester research extensions: LoRaWAN long-range telemetry, on-device TinyML autoencoders, multi-accelerometer spatial attribution (PIRG), and vibration energy harvesting.
- Concludes with appendices detailing the master GPIO interconnect table, breadboard layout, and certified 1:1 baseplate coordinates.

---

## 6. Overleaf Deployment Instructions
1. Download or locate the pre-compiled zip archive:
   ```bash
   /home/paradoxpete/Downloads/VibeGuard_Overleaf_Report.zip
   ```
2. Log in to [Overleaf](https://www.overleaf.com/).
3. Click **New Project** $\rightarrow$ **Upload Project**.
4. Drag and drop `VibeGuard_Overleaf_Report.zip`.
5. Ensure compiler is set to **pdfLaTeX** (default) with **TeX Live 2024 / 2023**.
6. Click **Recompile**. The complete document will compile cleanly into a publication-grade PDF report.
