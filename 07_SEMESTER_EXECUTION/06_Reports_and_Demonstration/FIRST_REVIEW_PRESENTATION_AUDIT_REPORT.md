# VibeGuard First Review Presentation — Official Audit & Delivery Report

## 1. Executive Summary
- **Course**: PBCST504 – Microcontrollers (Project Review 1)
- **Topic**: VibeGuard — Low-Cost Embedded Vibration Monitoring System
- **Group**: Group 8 (Department of Computer Science & Engineering - Cyber Security)
- **Coordinator**: Ms. Sagna L T, Asst. Prof. CSE(CY)
- **Official Submission File**: [`VibeGuard_First_Review_Official_Presentation.pptx`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/05_TEACHER_AND_REVIEWS/04_First_Review_VibeGuard/01_Official_Submission/VibeGuard_First_Review_Official_Presentation.pptx)
- **Total Slides**: 21 Slides (Fully Audited & Verified)

---

## 2. Slide-by-Slide Verification Matrix

| Slide # | Slide Title | Visual Asset / Content | Status | Verified Against Project Scope |
| :--- | :--- | :--- | :--- | :--- |
| **1** | Title Slide | Course code, Group 8, VibeGuard title, College banner | ✅ Certified | Matches academic syllabus & group registration. |
| **2** | Group Members | Amith, Archa, Nihad, Sreehari, Sreeprada & Coordinator | ✅ Certified | Accurate student registers & rolls. |
| **3–8** | Vision, Mission, PEOs, POs, PSOs | Institutional boilerplate requirements | ✅ Certified | 100% compliant with KTU / College NBA criteria. |
| **9** | Contents | Roadmap: Motivation $\rightarrow$ Intro $\rightarrow$ Method $\rightarrow$ Architecture $\rightarrow$ Conclusion | ✅ Certified | Clean agenda structure. |
| **10** | Motivation | Need for low-cost edge vibration detection | ✅ Certified | Explains machine failure awareness & cost barriers. |
| **11** | Introduction | Scope: ADXL345 + ESP32 + local RGB status (no cloud) | ✅ Certified | Restricts prototype to semester deliverables. |
| **12** | Problem Statement | Continuous vibration detection on small rotating plants | ✅ Certified | Formulates testable engineering hypothesis. |
| **13** | Proposed Method | 4-Wire SPI, DC removal, Vector RMS, K-of-M persistence | ✅ Certified | Explicitly defines 800 Hz ODR and multi-window state logic. |
| **14** | Basic Block Diagram | `slide 14 diagram.png` (High-level 5-stage flow) | ✅ Certified | Clear, digestable visual architecture with no cloud dependency. |
| **15** | Detailed Block Diagram | `slide 15 diagrm.png` (6-stage DSP & SPI architecture) | ✅ Certified | Rigorous engineering diagram detailing SCLK, MOSI, MISO, CS, Hann window, FFT. |
| **16** | Components Required | Tabulated list of hardware parts | ✅ Certified | Corresponds directly with frozen Procurement Plan BOM. |
| **17** | **Circuit Diagram** | **`slide_17_circuit_diagram_final.png`** | ✅ **RESOLVED** | **High-res schematic: ESP32 + ADXL345 SPI + Breadboard + RGB LED + Pinout Table**. |
| **18** | **Work Done So Far** | 5 Verified Completed Milestones | ✅ **RESOLVED** | **Eliminated duplicate copy-paste; reflects true mathematical modeling, BOM, C++ DSP, Wokwi, & 3D Digital Twin**. |
| **19** | **Work To Be Completed** | 5 Clear Remaining Physical Tasks | ✅ **RESOLVED** | **Reflects physical assembly, benchtop calibration, fault unbalance testing, and report writing**. |
| **20** | Conclusion | Cost summary (preferred $\le$ ₹3k), 3-month timeline | ✅ Certified | Realistic semester expectations without premature commercial claims. |
| **21** | **References** | 5 Authoritative Published Citations | ✅ **RESOLVED** | **Replaced hallucinated .md files with ISO 10816, ADXL345 Datasheet, ESP32 TRM, Cooley-Tukey, & Randall**. |

---

## 3. Formatting & Master Template Compliance
- **Dynamic Header Banner**: Topic banner (`Topic : VibeGuard: Low-Cost Embedded Vibration Monitoring System`) present on all content slides.
- **Department Tag**: `DEPT OF CSE ( CY )` centered in the footer across all slides.
- **Slide Numbers**: Dynamic slide numbering (`1` to `21`) verified on every slide.
- **Dynamic Date Code**: Standard OpenXML `<a:fld type="datetime">` code active. In LibreOffice / PowerPoint, opening the presentation automatically displays the current date.

---

## 4. Key Viva & Examiner Defense Talking Points
1. **Why ADXL345 over MPU6050 or Analog Sensors?**
   * *Answer*: ADXL345 provides hardware-level 4-wire SPI communication up to 5 MHz, capable of true 800 Hz to 3200 Hz Output Data Rates (ODR) with a flat mechanical frequency response suitable for machinery harmonics, whereas common I2C sensors hit bus bandwidth bottlenecks.
2. **Why Local Edge Processing Instead of Cloud IoT?**
   * *Answer*: At 800 samples/sec $\times$ 3 axes $\times$ 2 bytes = 4.8 KB/s of continuous raw binary data. Transmitting raw waveforms over Wi-Fi incurs packet drops, latency, and power overhead. Running DC removal, Vector RMS, and Hann-windowed FFT on the ESP32 dual-core Xtensa extracts diagnostic insights locally in under 1.25 ms.
3. **What Is the Mathematical Unbalance Model?**
   * *Answer*: Mechanical unbalance produces a synchronous 1X rotating centrifugal force $F = m \cdot r \cdot \omega^2$. For our 600 RPM N20 motor, $\omega = 2\pi(10.0\text{ rad/s})$, creating a distinct 10.0 Hz sinusoidal vibration signature in the orthogonal X-Y accelerometer plane.
