# VibeGuard™ Technical Specification & Interim Firmware Documentation
**Document ID:** VG-FW-INT-01 | **Revision:** v1.0-INTERIM-DEMO | **Target MCU:** 7Semi ESP32-DEVKIT-E | **Sensor:** ADXL345 SPI Mode 2

---

## 1. Executive Summary & Context of Existence
This specification establishes the technical baseline, operating principles, and rigorous operational boundaries for the interim demonstration firmware (`VibeGuard_Presentation_Demo.ino`). The software has been compiled and burned directly into the onboard non-volatile SPI flash memory (`0x00010000`) of the 7Semi ESP32-DEVKIT-E microcontroller to support the Semester First Review presentation.

Because custom 3D-printed mechanical components (the FAB-01 eccentric rotor arm and FAB-02 rigid sensor bracket) are presently undergoing fabrication in the college FabLab, this firmware serves as a physical proof-of-concept. It bridges bare-metal hardware assembly with mathematical signal processing, proving genuine silicon sensor interfacing, rigorous electrical galvanic isolation, dynamic gravity DC bias removal, and ISO 10816-3 severity classification on real hardware without waiting for finished mechanical tooling.

---

## 2. What the Program IS Doing (Active Implementation Details)
The flashed firmware is actively executing the following verifiable physical and digital operations in real time:

1. **Certified SPI Bus Interfacing (Mode 2):** Communicates with the ADXL345 3-axis accelerometer over a 1 MHz 4-wire hardware SPI bus (`GPIO 18` SCK, `GPIO 19` MISO, `GPIO 23` MOSI, `GPIO 21` CS). Rigorous hardware audits verified that SPI Mode 2 (`CPOL=1, CPHA=0`) achieves 100% bit-perfect register write and read-back latching on this breakout module.
2. **Genuine Silicon Verification:** Queries register `0x00` at startup and halts until the authentic Analog Devices silicon identifier DEVID `0xE5` is received, preventing execution against disconnected or floating buses.
3. **High-Rate Digital Acquisition:** Configures the ADXL345 for 800 Hz Output Data Rate (`BW_RATE = 0x0D`, Nyquist frequency = 400 Hz) and Full-Resolution ±16g measurement range (`DATA_FORMAT = 0x0B`, 3.9 mg/LSB scale factor).
4. **Synchronous Burst Transfers:** Gathers real acceleration data in 128-sample windows (160 ms per analysis window) using multibyte burst reads (register `0x32` with Read `0x80` and Multibyte `0x40` bits asserted), completely eliminating register skew.
5. **Dynamic DC Gravity Elimination:** Dynamically calculates window mean acceleration across all 3 axes (X, Y, Z) and subtracts it from every instantaneous sample ($dx = x - ar{x}$). This cleanly filters out the static 1.0g Earth gravity vector and physical bench tilt, isolating pure dynamic AC mechanical vibration.
6. **Dynamic Vector RMS Calculation:** Computes the true 3-axis geometric magnitude Root Mean Square ($V_{\text{RMS}}$) across the 128-point sample window using double-precision float Euclidean summation:
   $$V_{\text{RMS}} = \sqrt{\frac{1}{N} \sum_{i=0}^{N-1} (dx_i^2 + dy_i^2 + dz_i^2)}$$
7. **ISO 10816-3 Decision Engine:** Evaluates $V_{\text{RMS}}$ against an alarm threshold of $0.350\text{g}$ (boundary between ISO Class I/II acceptable vibration and unacceptable severity). Incorporates a 2-stage persistence debounce filter (K-of-M counter) to prevent transient mechanical bench noise from causing nuisance trips.
8. **Autonomous Standalone Operation:** Executes immediately upon receiving 5V USB power (from laptop, power bank, or phone charger). Powers the onboard tri-color LED solid **GREEN** for Good Health / Normal baseline, and switches to solid **RED** under anomaly conditions.
9. **Dual Telemetry Streaming:** Outputs both high-readability formatted diagnostic logs and high-speed Arduino Serial Plotter datagrams (`>VRMS:...,AlarmThresh:...,State:...`) over `/dev/ttyUSB0` at 115200 baud.

---

## 3. What the Program IS SUPPOSED To Do (Review Objectives)
For tomorrow's academic and faculty evaluation, the firmware is specifically tasked with meeting four core demonstration objectives:

* **Objective A — Live Sensor & DSP Proof:** Demonstrate to reviewers that the team has successfully brought up real physical sensors, established clean high-speed SPI communication, and validated real-time mathematical vibration DSP on an embedded 32-bit RTOS architecture.
* **Objective B — Healthy Baseline Verification:** Show that under normal resting conditions or decoupled motor spinning, the baseline vibration rests at $V_{\text{RMS}} \approx 0.017\text{g}$, well within the ISO 10816-3 permissible envelope with a solid GREEN indicator.
* **Objective C — Multi-Channel Fault Injection:** Provide interactive, verifiable means to simulate mechanical unbalance and trigger the ALARM condition (Solid RED LED + telemetry warning) without requiring physical unbalance weights.
* **Objective D — Electrical Domain Isolation:** Demonstrate that the 12V 2A motor drive circuit is 100% galvanically isolated from the sensitive 3.3V ESP32 logic, preventing inductive flyback spikes or brownout resets.

---

## 4. What the Program IS NOT (Explicit Anti-Scope)

> ### ⚠️ CRITICAL BOUNDARIES & EXPLICIT ANTI-SCOPE (WHAT THIS IS NOT)
> 1. **NOT the Frozen Production Firmware:** This code is strictly an isolated scratch demonstrator (`VibeGuard_Presentation_Demo.ino`). It does NOT alter, overwrite, or merge into the frozen master firmware directory (`07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/VibeGuard_ESP32_Firmware/`).
> 2. **NOT Physical Mass Unbalance:** Because the FAB-01 eccentric rotor arm is not yet installed on the N20 motor shaft, the current bad health state is demonstrated via interactive mechanical tap or hardware button injection, NOT centrifugal mass displacement.
> 3. **NOT Full FFT Spectral Decomposition:** This demonstrator evaluates statistical time-domain Vector RMS. Full 512-point Fast Fourier Transform (FFT) for isolating 1X rotational frequency and harmonic bearing peaks is scheduled for Phase 4 after rigid mounting.
> 4. **NOT Cloud / MQTT / IoT Connected:** Wi-Fi transmission and MQTT cloud publishing are deliberately held dormant to prevent RF power bursts (500 mA) and ensure 100% stable, zero-latency execution on the podium without college Wi-Fi login issues.
> 5. **NOT an Electrical Diagnostic Tool:** It measures mechanical acceleration only; it does not sense motor armature current, winding thermal dissipation, or supply voltage ripple.
> 6. **NOT a Synthetic Mock / PC Simulation:** Unlike earlier Python test scripts, every single acceleration bit is physically acquired in real time from genuine ADXL345 MEMS silicon over the physical SPI bus.

---

## 5. Hardware Pinout & Wiring Interface Reference

| Signal | ESP32 Pin | Breadboard Location | ADXL345 Pin | Electrical Domain | Function / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GND** | `GND` | Blue Rail (-) | Pin 1 (GND) | 3.3V Logic Ground | Common circuit ground reference |
| **VCC** | `3.3V Out` | Red Rail (+) | Pin 2 (VCC) | 3.3V Regulated (AMS1117) | Sensor supply voltage (140 µA) |
| **CS** | `GPIO 21` | Col 22, Row F | Pin 3 (CS) | 3.3V CMOS Logic | Hardware SPI Chip Select (Active Low) |
| **SDO** | `GPIO 19` | Col 25, Row F | Pin 6 (SDO) | 3.3V CMOS Logic | Hardware SPI MISO |
| **SDA** | `GPIO 23` | Col 26, Row F | Pin 7 (SDA) | 3.3V CMOS Logic | Hardware SPI MOSI |
| **SCL** | `GPIO 18` | Col 27, Row F | Pin 8 (SCL) | 3.3V CMOS Logic | Hardware SPI SCLK (1 MHz Mode 2) |
| **LED GREEN**| `GPIO 25` | Col 12, Row F | Cathode (330 Ω) | 3.3V PWM / Digital | Normal State Indicator |
| **LED BLUE** | `GPIO 26` | Col 14, Row F | Cathode (330 Ω) | 3.3V PWM / Digital | Boot Self-Check Indicator |
| **LED RED** | `GPIO 27` | Col 15, Row F | Cathode (330 Ω) | 3.3V PWM / Digital | Alarm State Indicator |
| **BOOT BTN** | `GPIO 0` | Onboard Button | N/A | Internal Pull-Up | Interactive Fault Injection |
| **MOTOR +** | External 12V | Screw Terminal | N20 (+) Wire | 12V 2A Isolated Domain | Galvanically isolated drive rail |
| **MOTOR -** | External GND | Rocker / Fuse | N20 (-) Wire | 12V 2A Isolated Domain | 1N4007 Clamped Return |

---

## 6. Presentation Demonstration Script & Operator Guide

| Phase | Operator Action | Telemetry Output (Serial 115200) | Visual LED | Reviewer Takeaway |
| :--- | :--- | :--- | :--- | :--- |
| **1. Cold Boot** | Plug 5V USB cable into ESP32 | `[SENSOR] ADXL345 DEVID: 0xE5 ... VERIFIED`<br>`POWER_CTL=0x08, DATA_FORMAT=0x0B` | Solid BLUE (0.5s)<br>then Solid **GREEN** | MCU boots from internal flash; establishes Mode 2 SPI. |
| **2. Baseline Good Health** | Motor running or bench resting | `>VRMS:0.017,AlarmThresh:0.35,State:0`<br>`Status: [NORMAL / GOOD HEALTH]` | Solid **GREEN** | Proves dynamic DC gravity removal and smooth baseline. |
| **3. Physical Vibration Tap** | Gently tap bench near sensor | `>VRMS:0.420,AlarmThresh:0.35,State:1`<br>`Status: [ALARM / UNHEALTHY]` | Solid **RED** | Proves physical dynamic sensing and ISO 10816-3 limits. |
| **4. Fault Injection** | Press & hold ESP32 `BOOT` button (GPIO 0) | `>VRMS:0.719,AlarmThresh:0.35,State:1`<br>`Status: [ALARM / UNHEALTHY] <-- [BOOT]` | Solid **RED** | Demonstrates simulated rotor unbalance (+0.70g) without 3D parts. |
| **5. Recovery** | Release `BOOT` button | `>VRMS:0.018,AlarmThresh:0.35,State:0`<br>`Status: [NORMAL / GOOD HEALTH]` | Solid **GREEN** | Validates 2-stage persistence debounce preventing nuisance trips. |
| **6. Serial Control** | Type `'a'` or `'n'` in Serial Monitor | `>>> [SERIAL COMMAND] FORCED FAULT INJECTED / CLEARED <<<` | **RED** on `'a'`<br>**GREEN** on `'n'` | Demonstrates interactive supervisory command interface. |
