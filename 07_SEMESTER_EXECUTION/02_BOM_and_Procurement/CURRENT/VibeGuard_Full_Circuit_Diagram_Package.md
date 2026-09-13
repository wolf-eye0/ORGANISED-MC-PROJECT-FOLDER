# VibeGuard: Complete Circuit Diagram & Hardware Interconnect Package
**Document Revision:** Rev 2.0 (Phase 4 Certified Baseline)  
**Classification:** Full Hardware System Schematic & Desk Prototyping Wiring Guide  
**Applicable Hardware:** 7Semi ESP32-DEVKIT-E, ADXL345 SPI Accelerometer, MB102 Breadboard, 12V 600RPM N20 Motor, Common Cathode RGB LED, 100 µF Bulk Capacitor, 1N4007 Diode, KCD1 Switch, 1A Fuse.

---

## 1. Master System Electrical Schematic (Engineering Blueprint)

The official engineering schematic depicts both electrical domains: the **3.3V/5V Digital Sensing & DSP Domain** and the **12V Motor Vibration Excitation Domain**, separated by a strict **Galvanic Isolation Barrier**.

![VibeGuard Master Electrical Schematic](/home/paradoxpete/.gemini/antigravity-cli/brain/f55a1ebc-7c35-4bc1-9341-35878b82ae59/VibeGuard_Master_Circuit_Schematic.png)

### Key Architectural Subsystems in Diagram 1:
1. **7Semi ESP32 Microcontroller Core:** Powered via USB-C from Host PC (5V $\rightarrow$ onboard AMS1117-3.3V LDO).
2. **Brownout Mitigation Network:** 100 µF low-ESR electrolytic bulk capacitor + 100 nF ceramic capacitor placed across 3.3V and GND to suppress voltage sag below the 2.70V Brownout Detector (BOD) reset threshold.
3. **ADXL345 4-Wire SPI Bus:** High-speed SPI interconnect operating at 2.5 MHz with 800 Hz ODR:
   - **CS (Chip Select):** `GPIO 21` (Header J3-6, remapped from default strapping pin GPIO5 to prevent boot-hangs)
   - **SCLK (Serial Clock):** `GPIO 18` (Header J3-9)
   - **MOSI / SDA (Master Out):** `GPIO 23` (Header J3-2)
   - **MISO / SDO (Master In):** `GPIO 19` (Header J3-8)
   - **INT1 (Data Ready):** `GPIO 4` (Header J3-13)
4. **3-State RGB Visual Status Telemetry:** 5mm Common Cathode RGB LED driven via 330 $\Omega$ current-limiting resistors:
   - **Green (Normal State):** `GPIO 25` (Header J1-9) $\rightarrow$ Vector RMS $< 0.45\text{g}$
   - **Blue (Initializing / Calibrating):** `GPIO 26` (Header J1-10) $\rightarrow$ DC offset window
   - **Red (Abnormal / Alarm):** `GPIO 27` (Header J1-11) $\rightarrow$ Vector RMS $> 0.45\text{g}$ persistent
   - **Common Cathode:** Connected directly to system digital ground (GND)

---

## 2. Physical Breadboard & Desk Wiring Assembly Diagram

Designed specifically for desk assembly using **Female-to-Male (F-to-M) DuPont jumper wires**, keeping the ESP32 beside the MB102 breadboard to provide 100% open breadboard area for components.

![VibeGuard Physical Breadboard Wiring Diagram](/home/paradoxpete/.gemini/antigravity-cli/brain/f55a1ebc-7c35-4bc1-9341-35878b82ae59/VibeGuard_Breadboard_Wiring_Diagram.png)

### Step-by-Step Desk Assembly Quick Reference:

| Wire # | Origin (ESP32 Pin) | Target on Breadboard | Wire Color | Function |
| :---: | :--- | :--- | :---: | :--- |
| **1** | `3V3` (Header J1-1, Top-Left) | **Red Power Rail (+)** | Red | +3.3V System Bus |
| **2** | `GND` (Header J1-14, Bottom-Left) | **Blue Power Rail (-)** | Black / Blue | Logic System Ground |
| **3** | `GPIO 27` (Header J1-11) | **Column 12, Row J** (Red 330 $\Omega$ bottom tie-point) | Red | Alarm Red Indicator |
| **4** | `GPIO 25` (Header J1-9) | **Column 14, Row J** (Green 330 $\Omega$ bottom tie-point) | Green | Normal Green Indicator |
| **5** | `GPIO 26` (Header J1-10) | **Column 15, Row J** (Blue 330 $\Omega$ bottom tie-point) | Blue | Calibrating Blue Indicator |
| **6** | `GPIO 21` (Header J3-6) | **Column 22, Row G** (ADXL345 CS tie-point) | Yellow | SPI Chip Select |
| **7** | `GPIO 18` (Header J3-9) | **Column 27, Row G** (ADXL345 SCL tie-point) | Purple | SPI Clock |
| **8** | `GPIO 19` (Header J3-8) | **Column 25, Row G** (ADXL345 SDO tie-point) | Green | SPI MISO |
| **9** | `GPIO 23` (Header J3-2) | **Column 26, Row G** (ADXL345 SDA tie-point) | Blue | SPI MOSI |
| **10** | `GPIO 4` (Header J3-13) | **Column 23, Row G** (ADXL345 INT1 tie-point) | Orange | Data Ready Interrupt |

> [!NOTE]
> **Internal Breadboard Node Topology:**
> - **Resistor Trough Straddling:** In Columns 12, 14, and 15, the 330 $\Omega$ resistors bridge across the center divider trough from **Row C** (top 5-hole clip, shared with the RGB LED in Row E) to **Row F** (bottom 5-hole clip). ESP32 control lines connect into **Row J**, sharing the bottom metal strip with the resistor's lower lead. This prevents any short-circuit across the resistor body!
> - **ADXL345 Row F Seating & Row G Tap:** The 8-pin male header of the ADXL345 breakout is seated directly into **Row F** (Columns 20 to 27). The DuPont jumper wires connect into **Row G** immediately adjacent in each column, accessing the same electrical node with zero pin crowding or bent leads.


---

## 3. 12V Motor Rig Safety & Back-EMF Suppression Circuit

The mechanical shaker rig is powered by an independent 12V DC domain with three critical safety features:

![VibeGuard 12V Motor Safety Circuit](/home/paradoxpete/.gemini/antigravity-cli/brain/f55a1ebc-7c35-4bc1-9341-35878b82ae59/VibeGuard_12V_Motor_Safety_Circuit.png)

### Safety Directives & Protective Features:
1. **1N4007 Flyback Suppression Diode:** Connected anti-parallel across the motor terminals (Cathode / silver band to $+12\text{V}$, Anode to $12\text{V GND}$). Clamps inductive armature turn-off spikes ($V = -L \frac{di}{dt}$) from destructive levels ($-80\text{V}$ to $-120\text{V}$) down to a safe $-0.7\text{V}$.
2. **1.0A Time-Delay Fuse (5×20 mm):** Protects against motor coil burnout or wiring overheating if the eccentric rotor arm is obstructed or stalled.
3. **KCD1 Rocker Switch:** Provides an instant physical emergency disconnect for the 12V rail.
4. **Strict Galvanic Domain Isolation (Zero Ground Loop Risk):**
   > [!CAUTION]
   > **NEVER connect 12V Motor Ground to ESP32 Ground or Breadboard Ground!**  
   > DC motor commutators generate severe brush sparking noise ($10\text{ kHz}$ to $50\text{ MHz}$) and high-current return currents. Connecting grounds will inject ripple into the sensitive ADXL345 SPI bus, induce ADC jitter, and risk back-feeding overvoltage into the host PC's USB root hub controller. Vibration transfers mechanically through the rigid acrylic slab — no electrical common ground is required.

---

## 4. 3D Workbench Perspective Overview

Photorealistic spatial rendering showing the complete physical layout on the workbench:

![VibeGuard 3D Testbed Overview](/home/paradoxpete/.gemini/antigravity-cli/brain/f55a1ebc-7c35-4bc1-9341-35878b82ae59/vibeguard_complete_circuit_rig_1789309804087.jpg)

---

## 5. Pre-Power Continuity & Isolation Protocol (Multimeter Check)

Before connecting the 12V power adapter or plugging in the USB cable, execute this **3-point multimeter audit**:

1. **Galvanic Isolation Audit:**
   - DMM setting: **Continuity / Resistance ($\Omega$)**
   - Probe 1: N20 Motor $(-)$ terminal (or 12V DC Jack negative lug)
   - Probe 2: ESP32 `GND` pin (or Breadboard Blue Rail)
   - **Expected Reading:** **Open Loop ($\text{OL} / \infty\ \Omega$) — NO BEEP.** (If a beep sounds, find and break the illegal ground bridge before proceeding).
2. **3.3V Power Rail Short Check:**
   - Probe 1: Breadboard Red Rail ($+$)
   - Probe 2: Breadboard Blue Rail ($-$)
   - **Expected Reading:** High resistance ($> 10\text{ k}\Omega$) or initial capacitor charging beep that fades to open. Zero ohms indicates a shorted capacitor or jumper error.
3. **1N4007 Diode Polarity Check:**
   - Verify the **silver painted band (Cathode)** is connected to the positive $+12\text{V}$ wire, and the plain black side (Anode) connects to the negative return wire.
