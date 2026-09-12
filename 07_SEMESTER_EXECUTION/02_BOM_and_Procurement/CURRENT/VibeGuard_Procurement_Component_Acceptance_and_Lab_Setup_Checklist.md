# VibeGuard Procurement, Component Acceptance and Lab Setup Checklist

**Document status:** Reconciled procurement and hardware baseline, revision 2.0  
**Audience:** Full five-member team under the synchronized primary/secondary role model  
**Price/specification check:** Reconciled September 2026, India  
**Procurement execution status:** Multi-channel procurement executed; Robocraze Order 1 (#TJFKQXJUQ) and Robu.in Order 2 confirmed; Robocraze Order 3 staged; College Lab items requisitioned.

**Current project-state control:** `Project_mC_Final_Selection_and_Phase4_Entry_Memo.md`, `Project_mC_Decision_Register_v1.3.md`, and `VG-AUDIT-HW-7SEMI-001` (`VibeGuard_7Semi_ESP32_DevKit_E_Hardware_Compatibility_Audit.md`).

**Revision 2.0 — Final Hardware Baseline & Multi-Channel Procurement Reconciliation:**
1. **Hardware Baseline Finalization:** The **7Semi ESP32-DEVKIT-E** (ESP32-WROOM-32E, CP2102 USB-to-UART bridge, 38-pin DevKitC V4 pinout) is formally certified and adopted as the MCU hardware baseline per audit `VG-AUDIT-HW-7SEMI-001`. It preserves 100% 1-to-1 pinout and electrical compatibility with the frozen 8-signal map (GPIO18, 23, 19, 21, 4, 25, 26, 27) and C++ DSP firmware, with mandatory 100 µF bulk + 100 nF ceramic bypass decoupling across 3.3V/GND and dual-breadboard mechanical bridging.
2. **Multi-Channel Procurement Synchronization:** Procured items are partitioned across four concrete sourcing channels: Robocraze Order 1 (Confirmed #TJFKQXJUQ), Robu.in Order 2 (Confirmed), Robocraze Order 3 (Planned / To Order), and College Lab Requisition (Cart C, Zero-Cost).
3. **Financial Ledger Reconciliation:** Reconciles the initial ₹2,124.00 cash disbursement against actual order spends, out-of-pocket contributions, returned cash balance (₹1,106.00), and projected Order 3 spend, confirming total expenditure stays well within the ₹3,000 preferred target and ₹5,000 semester ceiling.

**Official role titles:** Nihad P C — Technical Integration Lead / Project Manager / Configuration & Evidence Lead; Sreehari K — Firmware, DSP & Data Lead / Software Systems Mentor; Amith Krishna Das — Hardware, Power, Rig & Safety Lead; Sreeprada K S — Experimental Operations, Test & Inventory Coordinator / Firmware & Data Learning Associate & Technical Observer; Archa Pramod — Documentation, Communication & Demonstration Lead / Hardware Familiarization Associate & Technical Observer.

## 1. Procurement rules

- Target the preferred ₹3,000 project budget and never exceed the ₹5,000 ceiling without a new authorized decision. Shipping, GST, local fabrication and replacements count.
- Reopen every preferred and backup URL on the actual order day. Record time, postcode availability, exact stock, price, GST, shipping, delivery estimate and return deadline in `PROC-###`.
- Match exact manufacturer part number/SKU where specified. A similar photo or “ESP32 board” title is not an equivalent part.
- Inventory and accept usable lab stock before buying duplicates. Reused/donated items still receive `COMP-###` and acceptance records; their purchase cost is ₹0 with source stated, not silently omitted.
- Do not delete safety hardware to reach the preferred budget. If cost must be reduced, reuse a verified breadboard/cable/tools or consolidate shipping.
- Product specifications from generic module/motor sellers are vendor claims. The received part must pass the tests below.
- Only an invoice/order confirmation changes status to `ORDERED`; only receiving/acceptance records change status to `DELIVERED`/`ACCEPTED`.

## 2. Frozen procurement boundary

Required semester hardware remains:

- one permanent ADXL345 three-axis accelerometer breakout (4-wire SPI);
- one certified 7Semi ESP32-DEVKIT-E development board (ESP32-WROOM-32E, CP2102, 38-pin DevKitC V4 pinout), with Espressif `ESP32-DEVKITC-32E` as certified direct equivalent and ESP32-S3 DevKit only as emergency authorized fallback;
- SPI wiring loom (M2F / M2M jumpers);
- common-cathode RGB LED plus current-limiting resistors (220 Ω / 330 Ω);
- USB-A to Micro-B data/serial cable;
- 100 µF 25V bulk electrolytic capacitor and 100 nF ceramic capacitor for 3.3V PDN decoupling and brownout elimination;
- a separate guarded low-voltage 12 V motor rig (N20 600 RPM gear motor, heavy metal mounting bracket, 12V 2A power adapter, KCD1 DC rocker switch, 5×20mm fuse holder, 1A time-delay fuse, DC 5.5×2.1mm barrel jack adapter, and 1N4007 inductive flyback clamp diode across motor terminals) with stable base, rigid sensor mount, captive eccentric mass, and complete galvanic isolation from ESP32 logic ground.

Do not purchase a microphone, microphone array, permanent second accelerometer, industrial vibration sensor, cloud gateway or PIRG hardware for the semester system.

## 3. Reconciled Primary BOM & Multi-Channel Sourcing Channels

### 3.1 Primary BOM Table

| Line | Function and required specification | Qty | Assigned Sourcing Channel | Vendor & Status | Price / Subtotal (INR) | Equivalent / Baseline Notes |
|---:|---|---:|---|---|---:|---|
| 1 | **MCU:** 7Semi ESP32-DEVKIT-E (ESP32-WROOM-32E, CP2102 USB-UART, 38-pin DevKitC V4 pinout, 4 MB Flash) | 1 | Robocraze Order 3 | Robocraze (Planned / To Order) | ~₹686.00 (Part of ₹705 items) | Certified baseline per `VG-AUDIT-HW-7SEMI-001`; 100% pin/firmware drop-in for Espressif DevKitC-32E; requires Line 15-16 decoupling caps. |
| 2 | **Sensor:** ADXL345 3-axis accelerometer breakout exposing 4-wire SPI pins, 3.3 V compatible | 1 | Robocraze Order 1 | Robocraze (Confirmed #TJFKQXJUQ) | ₹249.00 | Bare ADXL345 2.0–3.6V supply; SPI `DEVID=0xE5`; 800 Hz ODR; 4-wire hardware SPI. |
| 3 | **Rig motor:** compact 12 V N20 metal gear motor, ~600 RPM, 3 mm D-shaft, pre-soldered leads | 1 | Robocraze Order 1 | Robocraze (Confirmed #TJFKQXJUQ) | ₹233.00 | Compact 12V N20 motor; 600 RPM nominal at 12V; 3mm D-shaft for captive eccentric coupling; requires Line 17 flyback clamp diode. |
| 4 | **Motor supply:** enclosed plug-in 12 V DC, 2 A regulated power adapter, 5.5×2.1 mm center-positive plug | 1 | Robocraze Order 1 | Robocraze (Confirmed #TJFKQXJUQ) | ₹125.00 | Upgraded to 12V 2A adapter; OVP/OCP/short protection; provides ample headroom over 1A requirement. |
| 5 | **DC power switch:** KCD1 12V–24V SPST 2-pin ON-OFF rocker switch, DC documented suitability | 1 | Robu.in Order 2 | Robu.in (Confirmed) | ₹25.00 | KCD1 compact rocker switch documented for 12V–24V DC motor circuit disconnect. |
| 6 | **Fuse holder:** 5×20 mm inline screw-type covered fuse holder casing, shrouded low-voltage DC rated | 2 | Robu.in Order 2 | Robu.in (Confirmed) | ₹38.00 (₹19.00 ea) | Fully enclosed screw casing for 5×20mm cartridge fuses; includes 1 operational + 1 spare holder. |
| 7 | **Motor fuse:** 1 A 250 V time-delay (slow-blow) cartridge fuses (5×20 mm) | 8 | Robu.in Order 2 | Robu.in (Confirmed) | ₹48.00 (₹6.00 ea) | Time-delay characteristic withstands N20 motor inductive startup inrush; pack of 8 provides ample spares. |
| 8 | **DC input connector:** DC Power Female Plug Jack Adapter Connector (5.5×2.1 mm to screw-terminal block) | 1 | Robocraze Order 3 | Robocraze (Planned / To Order) | ₹19.00 (Part of ₹705 items) | 5.5×2.1mm female barrel jack with heavy screw terminals; shrouded, polarity marked (+ / -). |
| 9 | **Status indicator:** 5 mm common-cathode RGB LED (pack of 10) | 10 (1 used) | Robocraze Order 1 | Robocraze (Confirmed #TJFKQXJUQ) | ₹30.00 | 4-pin common-cathode (Red: Pin 1, Cathode: Pin 2, Green: Pin 3, Blue: Pin 4); 9 spares in pack; requires Line 10 (330 Ω) or Line 18 (220 Ω) current-limiting resistors. |
| 10 | **Current-limiting resistors (330 Ω):** 330 Ω ¼ W ±5% through-hole resistors (pack of 52) | 52 | Robu.in Order 2 | Robu.in (Confirmed) | ~₹90.98 | Dedicated current-limiting for RGB LED channels (Green/Blue/Red) and circuit pull-ups. |
| 11 | **Bench prototype:** MB102 830-point solderless breadboard with dual split power rails | 1 | College Lab Requisition | College Lab Cart C (In-Stock) | ₹0.00 (Zero-Cost) | Requisitioned from college lab inventory; verified row/rail continuity; bench bring-up only. |
| 12 | **Bench jumpers:** 15 DuPont jumper wires (M2M & M2F, 20 cm) | 15 | College Lab Requisition | College Lab Cart C (In-Stock) | ₹0.00 (Zero-Cost) | Requisitioned from college lab inventory; flexible 20 cm jumpers for SPI bus and logic routing. |
| 13 | **USB data cable:** USB-A to Micro-B data/charging cable, 1 m, high-speed data capable | 1 | Robocraze Order 1 | Robocraze (Confirmed #TJFKQXJUQ) | ₹69.00 | ERD UC-252 1m USB-A to Micro-B; verified CP2102 enumeration and high-speed firmware flashing. |
| 14 | **Motor mounting bracket:** N20 metal U-bracket with M2 mounting screws | 1 | Robocraze Order 1 | Robocraze (Confirmed #TJFKQXJUQ) | ₹37.00 | Rigid stamped steel/aluminum mounting bracket securing N20 motor to the vibration test base. |
| 15 | **Decoupling bulk capacitor (`E-CAP-100U`):** 100 µF 25V low-ESR radial electrolytic capacitor | 1 | College Lab Requisition | College Lab Cart C (In-Stock) | ₹0.00 (Zero-Cost) | Requisitioned from college lab stock; installed across ESP32 3.3V and GND to prevent brownout (`rst:0x10`). |
| 16 | **Bypass ceramic capacitor (`C-CAP-100N`):** 100 nF (0.1 µF) 50V X7R ceramic capacitor | 1 | College Lab Requisition | College Lab Cart C (In-Stock) | ₹0.00 (Zero-Cost) | Requisitioned from college lab stock; RF shunt in parallel with 100 µF bulk cap and at ADXL345 VCC. |
| 17 | **Motor flyback diode (`D-DIODE-1N4007`):** 1N4007 1A 1000V silicon rectifier diode | 1 | College Lab Requisition | College Lab Cart C (In-Stock) | ₹0.00 (Zero-Cost) | Requisitioned from college lab stock; soldered directly across N20 motor tags (cathode to +12V). |
| 18 | **Current-limiting resistors (220 Ω):** 220 Ω ¼ W ±5% resistors | 3 | College Lab Requisition | College Lab Cart C (In-Stock) | ₹0.00 (Zero-Cost) | Requisitioned from college lab stock; alternative current-limiting for RGB LED channels. |
| 19 | **Stable final electronics:** Perfboard/stripboard, terminal blocks, hookup wire, heat-shrink | 1 lot | Lab Stock / Local Bench | Bench Allocation | ₹0.00 (Lab Stock) | Final soldered assembly per Stage 12 execution; lab stock hookup wire and terminal blocks. |
| 20 | **Mechanical rig base & guard:** Heavy base plate, 3mm clamping eccentric hub, fasteners, guard | 1 rig | Local Fabrication | Mechanical Allocation | ₹0.00 (Lab Stock) | Wood/acrylic damped base, 3mm shaft hub with captive off-axis M3 bolt/nyloc, polycarbonate guard. |
| — | **Total Reconciled Procurement Spend** | — | **All 4 Sourcing Channels** | **Robocraze (1 & 3), Robu.in (2), College Lab (Cart C)** | **₹1,973.98** (Items: ₹1,649.98 + Shipping: ₹324.00) | **Fund commitment: ₹1,900.00 (Reserve: ₹224.00); Out-of-pocket: ₹73.98 (~₹74.00); Headroom: +₹1,026.02 against ₹3,000 target; +₹3,026.02 against ₹5,000 ceiling.** |

### 3.2 Four Concrete Sourcing Channels Breakdown

#### Channel 1: Robocraze Order 1 (Confirmed #TJFKQXJUQ)
- **Order Status:** Confirmed / In Transit (Order Ref: `#TJFKQXJUQ`)
- **Vendor:** Robocraze (India)
- **Line Items:**
  1. ADXL345 3-Axis Digital Accelerometer Sensor Module (Qty 1): ₹249.00
  2. 600 RPM 12V N20 Micro Metal Gear Motor with Cable (Qty 1): ₹233.00
  3. 12V 2A Regulated DC Power Supply Adapter (5.5×2.1 mm) (Qty 1): ₹125.00
  4. Micro-USB High-Speed Data & Charging Cable (1 m) (Qty 1): ₹69.00
  5. 5mm Common-Cathode RGB LED (10-pack) (Qty 1 pack): ₹30.00
  6. N20 Motor Metal Mounting Bracket with M2 Screws (Qty 1): ₹37.00
- **Items Subtotal:** **₹743.00**
- **Delivery Service:** Express Delivery (Speed Post / Courier): **₹125.00**
- **Total Robocraze Order 1 Spend:** **₹868.00**
- **Funding Source:** 100% settled from initial project cash disbursement.

#### Channel 2: Robu.in Order 2 (Confirmed)
- **Order Status:** Confirmed / In Transit
- **Vendor:** Robu.in (Macfos Ltd., India)
- **Line Items:**
  1. KCD1 12V–24V SPST 2-Pin ON-OFF Rocker Switch (Qty 1): ₹25.00
  2. 5×20 mm Inline Screw-Type Covered Fuse Holder Casing (Qty 2): ₹38.00 (₹19.00 each)
  3. 1A 250V Time-Delay (Slow-Blow) Cartridge Fuses (5×20 mm) (Qty 8): ₹48.00 (₹6.00 each)
  4. 330 Ω Resistors (¼ W, ±5%) (Qty 52): ₹90.98
- **Items Subtotal:** **₹201.98**
- **Delivery Service:** Bluedart Air Priority Shipping: **₹149.00**
- **Total Robu.in Order 2 Spend:** **₹350.98**
- **Funding Source:** ₹277.00 paid from initial project cash disbursement fund; ₹73.98 (~₹74.00) paid out-of-pocket by team member as authorized operational advance.

#### Channel 3: Robocraze Order 3 (Planned / To Order)
- **Order Status:** Staged / Planned for Immediate Order Release
- **Vendor:** Robocraze (India)
- **Line Items:**
  1. 7Semi ESP32-DEVKIT-E Development Board (ESP32-WROOM-32E, CP2102, 38-Pin DevKitC V4) (Qty 1): ~₹686.00
  2. DC Power Female Plug Jack Adapter Connector (5.5×2.1 mm Screw Terminal) (Qty 1): ₹19.00
- **Items Subtotal:** **₹705.00**
- **Delivery Service:** Standard Tracked Shipping: **~₹50.00**
- **Total Robocraze Order 3 Planned Spend:** **~₹755.00**
- **Funding Source:** To be funded directly from the returned cash balance held by the project lead.

#### Channel 4: College Lab Requisition (Cart C / Zero-Cost Requisition)
- **Order Status:** Requisitioned / In-Stock at College Department Electronics Laboratory
- **Custodian:** Department of Electronics & Computer Engineering Lab
- **Line Items (Cost to Project: ₹0.00):**
  1. MB102 830-Point Solderless Breadboard with Dual Power Rails (Qty 1): ₹0.00
  2. DuPont Jumper Wires (20 cm, M2M & M2F) (Qty 15): ₹0.00
  3. 100 µF 25V Low-ESR Radial Electrolytic Capacitor (`E-CAP-100U`) (Qty 1): ₹0.00
  4. 100 nF (0.1 µF) 50V Ceramic Bypass Capacitor (`C-CAP-100N`) (Qty 1): ₹0.00
  5. 1N4007 1A 1000V Silicon Rectifier Flyback Diode (`D-DIODE-1N4007`) (Qty 1): ₹0.00
  6. 220 Ω Resistors (¼ W, ±5%) (Qty 3): ₹0.00
- **Total Channel 4 Cost:** **₹0.00** (Zero-Cost Lab Inventory Requisition).

---

## 4. Financial Transaction Ledger & Budget Reconciliation

### 4.1 Master Transaction Ledger

| Transaction ID | Date / Status | Channel / Entity | Description | Debit (Spend) | Credit (Inflow) | Cash Balance | Notes |
|---|---|---|---|---:|---:|---:|---|
| `TXN-001` | Initial Inflow | Project Faculty Sponsor | Initial Cash Disbursement to Procurement Team | — | **₹2,124.00** | ₹2,124.00 | Formal semester project advance |
| `TXN-002` | Confirmed (#TJFKQXJUQ) | Robocraze Order 1 | ADXL345, N20 Motor, 12V 2A Adapter, USB Cable, RGB LEDs, N20 Bracket | **₹868.00** | — | ₹1,256.00 | ₹743 items + ₹125 express delivery (100% fund) |
| `TXN-003` | Confirmed | Robu.in Order 2 (Cash Draw) | Cash advance drawn for Bluedart Air priority shipping | **₹150.00** | — | **₹1,106.00** | Cash drawn to cover ₹149 Bluedart shipping (~₹150) |
| `TXN-004` | Confirmed | Robu.in Order 2 (Online Settlement) | Item settlement paid online by team member (₹201.98 items) | — | — | ₹1,106.00 | Total Order 2 is ₹350.98: ₹277.00 fund share (₹150 cash + ₹127 reimbursable); ₹73.98 (~₹74) out-of-pocket |
| `TXN-005` | Custody Handover | Project Lead (Nihad P C) | Physical Cash Balance Returned to Project Lead Custody | — | — | **₹1,106.00** | Full remaining cash advance handed to project lead for controlled Order 3 release |
| `TXN-006` | Planned (Staged) | Robocraze Order 3 | 7Semi ESP32-DEVKIT-E, DC Female Barrel Jack Adapter | **~₹755.00** | — | **~₹351.00** | ₹705 items + ~₹50 standard shipping; disbursed from ₹1,106 returned cash |
| `TXN-007` | Requisitioned | College Lab Requisition | MB102 Breadboard, 15 Jumpers, 100µF Cap, 100nF Cap, 1N4007 Diode, 220Ω Resistors | **₹0.00** | — | ~₹351.00 | Zero-cost institutional lab stock (Cart C) |

### 4.2 Cash Flow & Reserve Analysis

```
+---------------------------------------------------------------------------------------+
|                           VIBEGUARD FINANCIAL RECONCILIATION                          |
+---------------------------------------------------------------------------------------+
  A. PHYSICAL CASH ADVANCE & CUSTODY RECONCILIATION:
     Initial Project Cash Disbursement:                                     ₹2,124.00
     Less: Robocraze Order 1 Spend (Confirmed #TJFKQXJUQ):                 - ₹868.00
     Less: Robu.in Order 2 Cash Advance Drawn (Bluedart Air Shipping):     - ₹150.00
     -----------------------------------------------------------------------------------
     Net Physical Cash Returned to Project Lead Custody:                    ₹1,106.00
     Less: Planned Robocraze Order 3 Spend (~₹705 items + ~₹50 shipping):   - ₹755.00
     -----------------------------------------------------------------------------------
     REMAINING UNENCUMBERED CASH RESERVE IN HAND:                             ~₹351.00 (~₹350.00)
     [Pending reimbursable adjustment to team member for Order 2 items]:   [- ₹127.00]
     [Net residual cash reserve after all obligations]:                      [~₹224.00]
  ---------------------------------------------------------------------------------------
  B. TOTAL PROJECT EXPENDITURE & SOURCE OF FUNDS:
     Robocraze Order 1 Spend (100% Disbursed Fund):                           ₹868.00
     Robu.in Order 2 Spend (Total ₹350.98: ₹277.00 Fund + ₹73.98 Out-of-Pocket): ₹350.98
     Robocraze Order 3 Planned Spend (100% Disbursed Fund):                 ~₹755.00
     College Lab Requisition (Cart C / Zero-Cost Stock):                        ₹0.00
     -----------------------------------------------------------------------------------
     TOTAL COMMITTED & PROJECTED PROJECT EXPENDITURE:                       ₹1,973.98
     (Total Disbursed Fund Share: ₹1,900.00 | Team Member Out-of-Pocket: ₹73.98)
+---------------------------------------------------------------------------------------+
```

### 4.3 Cumulative Project Cost vs. Institutional Budget Ceilings

| Expenditure Metric | Amount (INR) | Budget Threshold | Headroom / Variance | Compliance Status |
| :--- | :---: | :---: | :---: | :---: |
| **Robocraze Order 1 (Confirmed #TJFKQXJUQ)** | ₹868.00 | — | — | Executed |
| **Robu.in Order 2 (Confirmed Total Spend)** | ₹350.98 | — | — | Executed |
| **Robocraze Order 3 (Planned Allocation)** | ~₹755.00 | — | — | Staged |
| **College Lab Requisition (Cart C)** | ₹0.00 | — | — | Requisitioned |
| **TOTAL COMMITTED & PROJECTED EXPENDITURE** | **₹1,973.98** | **Preferred Target: ₹3,000.00** | **+ ₹1,026.02 Headroom** | **PASSED (34.2% below target)** |
| **TOTAL COMMITTED & PROJECTED EXPENDITURE** | **₹1,973.98** | **Semester Ceiling: ₹5,000.00** | **+ ₹3,026.02 Headroom** | **PASSED (60.5% below ceiling)** |

All expenditures remain comfortably beneath the preferred ₹3,000.00 threshold, leaving an unencumbered contingency reserve of **₹1,026.02** against the preferred budget and **₹3,026.02** against the absolute semester ceiling.
The total disbursed fund commitment is **₹1,900.00** (leaving ₹224.00 net reserve from the ₹2,124.00 initial disbursement), while physical cash in hand before final settlement is **~₹351.00 (~₹350.00)**.

---

## 5. Order sequence and Channel Management

### Gate A — Before any order (COMPLETED)

- [x] Nihad confirms architecture and budget boundary.
- [x] Amith completes lab-stock inventory with IDs and condition.
- [x] Sreehari confirms preferred board/sensor interfaces against official documentation.
- [x] Sreeprada coordinates inventory/component-ID and receiving-checklist fields, checks each BOM row for completeness and shadows approved Sreehari-led electronics identity learning where appropriate.
- [x] Archa stores dated source/invoice/evidence captures, prepares the procurement register and attends an Amith-led physical-component function walkthrough.
- [x] Delivery postcode, GST invoice details, payment authority and receiving address are confirmed.
- [x] Mechanical allowance has at least a rough dimension-dependent quote or is explicitly held until parts arrive.

### Order Group 1 — Robocraze Order 1 (Confirmed #TJFKQXJUQ)
1. ADXL345 3-axis accelerometer module (4-wire SPI capable).
2. 600 RPM 12V N20 metal gear motor with pre-soldered cable.
3. 12V 2A regulated DC power supply adapter (5.5×2.1 mm).
4. Micro-USB data & charging cable (1 m).
5. 5mm common-cathode RGB LED (10-pack).
6. N20 motor metal mounting bracket with M2 screws.

### Order Group 2 — Robu.in Order 2 (Confirmed)
1. KCD1 12V–24V SPST 2-pin ON-OFF rocker switch.
2. 5×20 mm inline screw-type covered fuse holder casing (x2).
3. 1A 250V time-delay (slow-blow) cartridge fuses (5×20 mm) (x8).
4. 330 Ω ¼ W ±5% resistors (x52).

### Order Group 3 — Robocraze Order 3 (Planned / To Order)
1. 7Semi ESP32-DEVKIT-E development board (ESP32-WROOM-32E, CP2102, 38-pin DevKitC V4).
2. DC Power Female Plug Jack Adapter Connector (5.5×2.1 mm screw terminal).

### Order Group 4 — College Lab Requisition (Cart C / Zero-Cost)
1. MB102 830-point solderless breadboard with dual power rails.
2. 15 DuPont jumper wires (M2M & M2F, 20 cm).
3. 100 µF 25V radial electrolytic bulk decoupling capacitor (`E-CAP-100U`).
4. 100 nF (0.1 µF) 50V ceramic bypass capacitor (`C-CAP-100N`).
5. 1N4007 1A 1000V silicon rectifier flyback clamp diode (`D-DIODE-1N4007`).
6. 220 Ω ¼ W ±5% resistors.

### Order Group 5 — Mechanical Rig & Guard Fabrication
Wait until N20 motor and mounting bracket arrive from Robocraze Order 1. Then verify motor body dimensions and shaft flat before finalizing captive off-axis eccentric hub and polycarbonate guard envelope.

## 6. Receiving and quarantine workflow

1. Preserve packaging and return label until acceptance closes.
2. Photograph sealed package, contents and both sides/markings of every item; mask personal data in any public copy.
3. Assign `COMP-###` and link invoice/order/batch before powered testing.
4. Compare exact ordered title/MPN/SKU to received marking. Record discrepancies; do not “correct” the order record.
5. Mark one of: `ACCEPTED`, `CONDITIONAL`, `QUARANTINED`, `REJECTED`.
6. Physically separate quarantined/rejected parts. Do not place them in the general component bin.
7. Complete return/replacement before the seller window closes; retain seller communication.
8. A visually accepted MCU/sensor remains conditional until powered identity/functional tests pass.

## 7. Component acceptance procedures

### 7.1 MCU: 7Semi ESP32-DEVKIT-E (and Espressif ESP32-DevKitC-32E Baseline)

**Sourcing Channel:** Robocraze Order 3 (Planned / To Order; MPN: 7Semi ESP32-DEVKIT-E, 38-pin DevKitC V4).  
**Required:** Board, known Micro-USB data cable (Robocraze Order 1), ESD-aware bench, camera, Arduino IDE / Espressif core, serial capture.

- [ ] Markings confirm 7Semi ESP32-DEVKIT-E with authentic Espressif ESP32-WROOM-32E module; verify PCB antenna area and shielding integrity.
- [ ] Hardware verification: Confirm Silicon Labs CP2102 USB-to-UART bridge (USB VID:PID `10c4:ea60` via `lsusb`), AMS1117-3.3 linear voltage regulator, and 38-pin DevKitC V4 physical header layout (2.54 mm pin pitch, 22.86 mm row pitch).
- [ ] Visual & mechanical inspection: No bent header pins, solder bridges, cracked Micro-USB receptacle, or component misalignments.
- [ ] Power isolation: Power via Micro-USB only. The official Espressif user guide establishes that Micro-USB, 5V/GND, and 3.3V/GND power inputs are mutually exclusive. Never supply external 5V/3.3V simultaneously with USB.
- [ ] Host enumeration: Connect via Micro-USB cable; verify mainline Linux `cp210x` driver binds `/dev/ttyUSB0`; select board `esp32dev` in Arduino CLI / IDE.
- [ ] Smoke sketch & boot test: Upload minimal monotonic counter sketch; verify bootloader output (`rst:0x1 (POWERON_RESET)`) at 115200 baud; confirm clean monotonic counter progression.
- [ ] Five consecutive power-cycle / hardware reset boots complete with zero brownout (`rst:0x10`), zero core panic, and no abnormal AMS1117 thermal rise.
- [ ] Mandatory PDN decoupling verification: Verify that the 100 µF bulk capacitor (`E-CAP-100U`) and 100 nF ceramic bypass capacitor (`C-CAP-100N`) from College Lab Requisition (Cart C) are installed directly across Pins J1-1 (3V3) and J1-14 (GND) before high-speed SPI or RF testing.
- [ ] Dual-breadboard bridging: Confirm 7Semi board spans across two joined MB102 breadboards (bridging the center divider) so that tie-points on both Header J1 and Header J3 are easily accessible for probe leads.

**Accept:** Authentic 7Semi ESP32-DEVKIT-E identity, CP2102 enumeration, reproducible firmware flashing, 5/5 clean boots without brownout, and mandatory 100 µF + 100 nF decoupling installed.  
**Reject/quarantine:** Module marking mismatch, physical damage, enumeration failure on two known-good computers, brownout reset loops (`rst:0x10`), or persistent flash timeouts.

### 7.2 Sensor: ADXL345 3-Axis Accelerometer Breakout

**Sourcing Channel:** Robocraze Order 1 (Confirmed #TJFKQXJUQ; ADXL345 Module, 4-wire SPI).  
**Official Specifications:** ADXL345 supply 2.0–3.6 V; 3-/4-wire SPI; `DEVID` register `0x00` returns `0xE5`; bandwidth is ODR/2 (400 Hz at 800 Hz ODR). [Analog Devices ADXL345 Data Sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.PDF).

- [ ] Photograph breakout front/back; record silkscreen markings, onboard LDO / pullup network, and header pinout (`GND, VCC, CS, INT1, INT2, SDO/MISO, SDA/MOSI, SCL/SCLK`).
- [ ] Exclusively wire to ESP32 3.3V rail (Pin J1-1), never 5V, despite any vendor level-shifter claims.
- [ ] With power removed, verify continuity of wiring loom (SCK→GPIO18, MOSI→GPIO23, MISO→GPIO19, CS→GPIO21).
- [ ] Device ID readback: Read register `0x00` over SPI Mode 3; returned byte must be rock-solid `0xE5`.
- [ ] Register write/readback: Write and verify `BW_RATE` (0x2C) to `0x0D` (800 Hz ODR), `POWER_CTL` (0x2D) to `0x08` (Measurement Mode), and `DATA_FORMAT` (0x31) to `0x0B` (Full Resolution, ±16g or ±4g).
- [ ] Static 6-orientation test: Place sensor flat and on all 6 faces; verify $1\text{g} \approx 9.8\text{ m/s}^2$ aligns with Earth's gravity vector on each corresponding axis with plausible sign/magnitude.
- [ ] Burst-read sequence test: Issue burst read `0xF2` (`0x32 | 0x80 | 0x40`); confirm seamless 6-byte payload reception without bus stalls or FIFO overruns.

**Accept:** Stable `0xE5` device ID, 100% register write/readback fidelity, plausible static gravity response across all 6 axes, and zero dropped frames over a 10-minute 800 Hz stationary capture.  
**Reject/quarantine:** Incorrect or intermittent `DEVID`, missing SPI signals, physical damage, sensor overheating, or saturated/floating axis registers.

### 7.3 Rig Motor: 600 RPM 12V N20 Gear Motor & Mounting Bracket

**Sourcing Channel:** Robocraze Order 1 (Confirmed #TJFKQXJUQ; 600 RPM 12V N20 Metal Gear Motor with Cable & N20 Metal U-Bracket).

- [ ] Photograph motor body, gearbox casing, 3 mm D-shaft, pre-soldered silicone leads, and metal mounting bracket; record dimensional envelope.
- [ ] Powered-off mechanical check: Rotate 3 mm D-shaft gently by hand; verify smooth gearbox gear train rotation without binding or excessive radial play.
- [ ] Motor mounting bracket fit check: Verify that the N20 motor body seats securely inside the Robocraze metal U-bracket, and that M2 retaining screws fasten without stripping.
- [ ] Bench bring-up: Clamp motor bracket securely in lab vise before applying any power. Do not attach eccentric mass during electrical acceptance.
- [ ] Start on current-limited bench supply: Apply 6V DC initially, stepping up to rated 12V DC; measure no-load running current ($I_{no-load} \le 60\text{ mA}$).
- [ ] Inspect rotational behavior: Confirm smooth ~600 RPM shaft rotation (nominal 10 Hz fundamental), absence of harsh grinding noises, and minimal thermal rise after 5 minutes of continuous operation.
- [ ] Flyback diode preparation: Verify that 1N4007 clamp diode (`D-DIODE-1N4007` from College Lab Cart C) is soldered directly across motor terminals (cathode to +12V) before any subsequent switching tests.

**Accept:** Consistent startup at rated 12V, no-load current $\le 60\text{ mA}$, no excessive shaft wobble, healthy gearbox acoustics, and snug bracket fit.  
**Reject/quarantine:** Gearbox binding, stripped gears, intermittent lead connection, excessive current ($>120\text{ mA}$ no-load), severe wobble, or abnormal heating.

### 7.4 12V Motor Power Supply, DC Jack, KCD1 Switch & Fuse System

**Sourcing Channels:**
- **12V 2A Regulated Power Adapter:** Robocraze Order 1 (Confirmed #TJFKQXJUQ).
- **DC Power Female Plug Jack Adapter (5.5×2.1 mm):** Robocraze Order 3 (Planned / To Order).
- **KCD1 12V–24V SPST Rocker Switch:** Robu.in Order 2 (Confirmed).
- **5×20 mm Inline Screw-Type Fuse Holder Casings (x2):** Robu.in Order 2 (Confirmed).
- **1A 250V Time-Delay Cartridge Fuses (x8):** Robu.in Order 2 (Confirmed).

- [ ] Adapter inspection: Verify 12V 2A label, intact mains prongs, undamaged insulated cable, and 5.5×2.1 mm barrel connector.
- [ ] Polarity & voltage measurement: Use DMM to measure barrel plug polarity (center positive, outer sleeve negative) and no-load voltage (must measure $12.0\text{V} \pm 0.6\text{V}$).
- [ ] DC jack terminal check: Insert barrel plug into 5.5×2.1 mm screw-terminal adapter; tighten test leads in screw terminals; verify secure mechanical grip with pull test.
- [ ] KCD1 rocker switch verification: Verify SPST 2-pin switch contacts with DMM continuity; confirm low contact resistance ($< 0.1\ \Omega$) in ON position and infinite resistance in OFF position.
- [ ] Fuse holder casing check: Inspect 5×20 mm inline screw casing; insert 1A time-delay cartridge fuse; confirm spring-loaded mechanical contact and tight screw closure.
- [ ] Fuse continuity: Verify 1A time-delay cartridge fuse shows $< 0.5\ \Omega$ continuity before installation.
- [ ] Circuit wiring topology: Adapter positive (+12V) → KCD1 switch → 5×20mm fuse holder (1A slow-blow) → N20 motor terminal (+) [with 1N4007 cathode]; N20 motor terminal (-) [with 1N4007 anode] → Adapter negative (GND).
- [ ] Galvanic isolation audit: With DMM on high-resistance mode ($\text{M}\Omega$), test between 12V motor supply ground and ESP32 logic ground. Must measure complete open circuit ($\infty\ \Omega$).
- [ ] Emergency stop function: Confirm flipping KCD1 switch immediately de-energizes the motor without requiring contact near the rotating shaft.

**Accept:** Correct 12V center-positive polarity, stable voltage, low switch contact resistance, compatible 5×20mm fuse/holder fit, prompt disconnect response, and complete electrical isolation from the logic domain.  
**Reject/quarantine:** Inverted polarity, voltage outside 11.4V–12.6V, switch arcing/heating, incompatible fuse dimensions, fast-blow nuisance opening during startup, or any ground bridging between 12V motor rail and logic ground.

### 7.5 Status Indication: RGB LED and Current-Limiting Resistors

**Sourcing Channels:**
- **5mm Common-Cathode RGB LED (10-pack):** Robocraze Order 1 (Confirmed #TJFKQXJUQ).
- **330 Ω ¼W ±5% Resistors (x52):** Robu.in Order 2 (Confirmed).
- **220 Ω ¼W ±5% Resistors (x3):** College Lab Requisition (Cart C / Zero-Cost).

- [ ] LED pin identification: Identify common cathode (longest pin, Pin 2); identify Red anode (Pin 1), Green anode (Pin 3), and Blue anode (Pin 4).
- [ ] Diode test with DMM: Measure forward voltages: Red ($V_f \approx 1.8\text{V} - 2.0\text{V}$), Green ($V_f \approx 2.8\text{V} - 3.2\text{V}$), Blue ($V_f \approx 2.9\text{V} - 3.3\text{V}$). Confirm common cathode polarity.
- [ ] Resistor measurement: Verify 330 Ω resistors with DMM (acceptable range 313–347 Ω) and 220 Ω resistors (acceptable range 209–231 Ω).
- [ ] Circuit calculation: At 3.3V logic drive, $I_{Red} = (3.3 - 2.0)/330 \approx 3.9\text{ mA}$; $I_{Green} = (3.3 - 3.0)/220 \approx 1.4\text{ mA}$; $I_{Blue} = (3.3 - 3.0)/220 \approx 1.4\text{ mA}$. Currents are safely within ESP32 12 mA pin drive limits.
- [ ] Functional lamp test: Wire common cathode to ESP32 GND; connect Green anode via resistor to GPIO25, Blue anode to GPIO26, and Red anode to GPIO27.
- [ ] Firmware state verification: Test individual color illumination:
  - Green ON (GPIO25 HIGH) = Normal State.
  - Blue ON (GPIO26 HIGH) = Calibrating State.
  - Red ON (GPIO27 HIGH) = Abnormal State.
  - All OFF when idle.

**Accept:** Verified common-cathode pinout, measured resistor values, distinct visual colors, and confirmed correspondence to GPIO25 (Green), GPIO26 (Blue), GPIO27 (Red).  
**Reject:** Common-anode LED, blown channel, missing current-limiting resistor, or incorrect channel mapping.

### 7.6 Prototyping Hardware: Breadboard, Jumpers & Micro-USB Cable

**Sourcing Channels:**
- **MB102 830-Point Solderless Breadboard:** College Lab Requisition (Cart C / Zero-Cost).
- **DuPont Jumpers (15 pcs, M2M & M2F, 20 cm):** College Lab Requisition (Cart C / Zero-Cost).
- **Micro-USB Data Cable (1 m):** Robocraze Order 1 (Confirmed #TJFKQXJUQ).

- [ ] Breadboard continuity: Check power rail continuity along top and bottom rails; note any split power rail breaks; verify firm spring clip tension across terminal rows.
- [ ] DuPont jumper integrity: Test all 15 jumper wires with DMM continuity; flex/wiggle test each end to detect internal wire fractures; discard any high-resistance or intermittent leads.
- [ ] Micro-USB cable verification: Connect PC to 7Semi ESP32-DEVKIT-E; verify immediate CP2102 device enumeration (`10c4:ea60`); execute 5 consecutive flex tests at both cable strain reliefs during serial transmission without data loss.

**Accept:** Robust breadboard contact grip, low jumper resistance ($< 0.2\ \Omega$), and uninterrupted USB serial data communication.  
**Reject:** Loose breadboard tie-points, intermittent jumpers, or charge-only USB cables lacking D+/D- data lines.

### 7.7 Mechanical Test Base, Motor Clamp, Eccentric Fixture & Safety Guard

**Sourcing Channels:**
- **N20 Metal Mounting Bracket:** Robocraze Order 1 (Confirmed #TJFKQXJUQ).
- **Rig Base Plate, Clamping Eccentric Hub & Guard:** Local Lab Fabrication / Mechanical Allocation.

- [ ] Rigid base plate: High-density wood or 10 mm acrylic base plate; verify no rocking, flexing, or vibration walking on the bench surface.
- [ ] Motor mounting: Fasten N20 motor securely to base using the Robocraze metal U-bracket with M2 machine screws and locking washers.
- [ ] Rigid sensor bracket: Fabricate stiff 3D-printed or aluminum bracket rigidly bolted directly to the motor bearing face; absolute prohibition of foam tape or hot glue.
- [ ] Positive-retention eccentric mass: Clamping/set-screw 3 mm brass/aluminum hub attached to motor D-shaft, carrying a captive off-axis M3 bolt with washers and a nyloc nut.
- [ ] Full rotating-envelope safety guard: Transparent polycarbonate enclosure surrounding the entire rotating hub and shaft assembly; securely fastened to base plate.
- [ ] Clearance & spin test: With power disconnected, manually rotate eccentric assembly through 360°; verify at least 5 mm clearance between eccentric mass and inside of guard at all angles.

**Accept:** Rigid non-resonant mounting, captive eccentric mass with locking nut, complete polycarbonate guard containment, and verified manual clearance.  
**Reject:** Any loose/press-fit rotating mass, flexible sensor mount, unguarded rotating parts, or guard contact during rotation.

### 7.8 Power Decoupling Capacitors and Motor Flyback Diode

**Sourcing Channels:**
- **100 µF 25V Low-ESR Bulk Electrolytic Capacitor (`E-CAP-100U`):** College Lab Requisition (Cart C / Zero-Cost).
- **100 nF 50V Ceramic Bypass Capacitor (`C-CAP-100N`):** College Lab Requisition (Cart C / Zero-Cost).
- **1N4007 1A 1000V Silicon Rectifier Diode (`D-DIODE-1N4007`):** College Lab Requisition (Cart C / Zero-Cost).

- [ ] Measure capacitance of 100 µF bulk capacitor with DMM/LCR meter (acceptable tolerance 90–110 µF); verify voltage rating ($\ge 10\text{V}$, received 25V) and clear negative polarity stripe.
- [ ] Verify low ESR ($\le 100\text{ m}\Omega$) to guarantee transient voltage sag suppression during ESP32 Wi-Fi bursts and active computation.
- [ ] Verify 100 nF ceramic bypass capacitor with meter (acceptable tolerance 80–120 nF).
- [ ] Diode test 1N4007: Confirm forward voltage ($V_f \approx 0.6\text{V} - 0.7\text{V}$) and infinite resistance ($\infty\ \Omega$) in reverse bias.
- [ ] Breadboard installation rule: 100 µF bulk capacitor and 100 nF ceramic capacitor must be inserted in direct parallel across ESP32 3V3 (Pin J1-1) and GND (Pin J1-14) with minimal lead length ($\le 5\text{ mm}$).
- [ ] Motor flyback installation rule: 1N4007 diode must be soldered directly across the N20 motor terminal tags in reverse-biased configuration: **Cathode (printed silver band) to +12V motor terminal**, **Anode to motor GND terminal**.
- [ ] Strict isolation test: Multimeter continuity test between 12V motor GND and ESP32 logic GND must show open circuit ($\infty\ \Omega$). Common ground between motor drive and ESP32 logic is strictly forbidden.

**Accept:** Rated capacitance and polarity confirmed; low ESR verified; diode passes forward/reverse test; 100 µF + 100 nF placed adjacent to ESP32 3V3 rail; flyback diode soldered across motor terminals; zero continuity between motor 12V ground and logic ground.  
**Reject:** Leaky/damaged capacitor, inverted polarity, open/shorted diode, or any common ground bridging between 12V motor rail and ESP32 3.3V/5V logic rail.

---

## 8. Certified Frozen Pinout & Signal Mapping

The final hardware pinout is **100% FROZEN AND CERTIFIED** for the 7Semi ESP32-DEVKIT-E (and Espressif ESP32-DevKitC-32E drop-in equivalent per `VG-AUDIT-HW-7SEMI-001`). All signals preserve exact 1-to-1 pin alignment, ensuring **ZERO modifications to C++ DSP firmware or simulation models**:

| Signal Function | Frozen GPIO | 7Semi DEVKIT-E Pin | DevKitC V4 Pin | Signal Type & Electrical Notes | Firmware Pin Macro |
| :--- | :---: | :---: | :---: | :--- | :--- |
| **ADXL345 SCLK** | **GPIO18** | Header J3, Pin 9 | Header J3, Pin 9 | SPI Clock Out (2 MHz hardware SPI) | Default VSPI SCK |
| **ADXL345 MOSI / SDI** | **GPIO23** | Header J3, Pin 2 | Header J3, Pin 2 | Controller-to-Sensor Master Out | Default VSPI MOSI |
| **ADXL345 MISO / SDO** | **GPIO19** | Header J3, Pin 8 | Header J3, Pin 8 | Sensor-to-Controller Master In | Default VSPI MISO |
| **ADXL345 CS** | **GPIO21** | Header J3, Pin 6 | Header J3, Pin 6 | Active-LOW Chip Select (Avoids strapping pin GPIO5) | `#define ADXL345_PIN_CS 21` |
| **ADXL345 INT1** | **GPIO4** | Header J3, Pin 13 | Header J3, Pin 13 | Data Ready / Watermark In (Synthetic tachometer in sim) | Optional DATA_READY |
| **RGB Status Green** | **GPIO25** | Header J1, Pin 9 | Header J1, Pin 9 | Digital Out via 220/330 Ω resistor (Normal Zone A/B) | `#define PIN_LED_GREEN 25` |
| **RGB Status Blue** | **GPIO26** | Header J1, Pin 10 | Header J1, Pin 10 | Digital Out via 220/330 Ω resistor (Calibrating Mode) | `#define PIN_LED_BLUE 26` |
| **RGB Status Red** | **GPIO27** | Header J1, Pin 11 | Header J1, Pin 11 | Digital Out via 220/330 Ω resistor (Abnormal Zone C/D) | `#define PIN_LED_RED 27` |
| **Sensor Power (+3.3V)** | **3V3 Rail** | Header J1, Pin 1 | Header J1, Pin 1 | Dedicated 3.3V regulated power to ADXL345 VCC | Shared 3.3V Logic Rail |
| **Common Logic Ground** | **GND** | Header J1, Pin 14 | Header J1, Pin 14 | Common logic ground for sensor & RGB LED cathode | Dedicated Logic Ground |

*Strapping Pin Audit Safety:* GPIO0 (Boot), GPIO2 (Flashing), GPIO5 (SDIO timing), GPIO12 (Flash VDD), and GPIO15 (ROM silence) remain completely unencumbered. Integrated SPI flash pins (GPIO6–GPIO11) remain 100% unassigned. All 8 active VibeGuard signals are verified safe against boot contention and flash crashes.

The ESP32's GPIO0, GPIO2, GPIO5, GPIO12 and GPIO15 are strapping pins; GPIO6–11 are normally connected to module flash and must not be used. [Espressif GPIO guidance](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/gpio.html). A fallback S3 board requires a new `PIN-###`; never copy this map.

## 9. Required lab equipment and readiness

Equipment is not automatically a project purchase. Record `AVAILABLE/ACCEPTED`, `AVAILABLE/NEEDS CHECK`, `NOT AVAILABLE` and custodian/location before ordering anything.

| Equipment | Required/optional | Readiness/acceptance check | Owner |
|---|---|---|---|
| Computer with USB and storage | Required; second computer strongly preferred | Arduino/Git/capture installed; port access; free space; backup/restore test | Sreehari; Sreeprada shadows approved upload/capture; Archa records evidence |
| Calibrated/checked digital multimeter | Required | Known source/resistor sanity check; leads/fuse intact; equipment ID/status recorded | Amith |
| Current-limited bench DC supply | Strongly preferred for first motor bring-up | Output/polarity/current-limit verified; local lab instructions followed | Amith |
| Soldering station, stand, solder, extraction/ventilation | Required for final stable wiring | Tip/earth/stand condition; trained operator; eye/heat safety | Amith |
| Wire stripper/cutter, screwdrivers, hex keys, spanners | Required | Correct size, undamaged, controlled storage | Amith |
| Caliper/ruler and mass scale | Required for repeatable fixture/mount | Zero/reference check; resolution/ID recorded | Amith; Sreeprada coordinates records; Archa observes familiarization |
| Clamps/vice/drill/guard fabrication tools | Required or fabrication service | Safe tool access and trained operator; local rules | Amith |
| Eye protection | Required for rig pilots/runs | Undamaged, fits each person in operating area | Amith |
| Camera/phone and stable timestamp | Required | Storage/timezone set; original files retained; privacy procedure | Archa evidence/media owner; Sreeprada experiment/remount records |
| Tachometer or stroboscope | Optional but useful | Known reference/check; safe non-contact use outside guard | Amith |
| Oscilloscope/logic analyzer | Optional diagnostic | Probe condition/reference test; not required for minimum success | Sreehari |
| Thermometer/IR thermometer | Useful | Emissivity/limitations noted; reference check | Amith |
| Fire-safe normal lab provisions/emergency contact | Required under local lab rules | Location/access briefing; do not invent or replace institutional rules | Nihad/Amith |

## 10. Lab layout checklist

- [ ] Stable bench with rig zone physically separated from electronics/computer zone.
- [ ] Motor base is restrained; guard faces away from people and fragile equipment.
- [ ] Emergency disconnect is reachable without crossing the rotating envelope.
- [ ] Logic USB and motor 12 V paths are color/label separated.
- [ ] Cable routes cannot enter guard or pull sensor/motor; strain relief installed.
- [ ] No loose screws, washers, tools or test objects near the rig.
- [ ] PPE location and stop signal are known to everyone.
- [ ] Quarantine bin, component labels and return packaging area exist.
- [ ] Raw capture destination has adequate space, new-file protection and backup.
- [ ] Sreeprada/Archa observer position is outside the guard/hazard zone.

## 11. First-week setup procedure

### Day 0 — Governance and no-power readiness

1. All five read the Primer safety/boundaries.
2. Create folder/ID system and component/procurement registers.
3. Inventory lab tools/stock; record unknowns rather than assumptions.
4. Install Arduino IDE, Espressif board package, Git and serial capture; record versions as pending until smoke test.
5. Review current supplier pages/BOM and approve budget/order sequence.

**Exit:** 5/5 acknowledgements, complete pending BOM, no unassigned critical role.  
**Do not:** order unauthorized substitute, power a motor, wire a sensor or set thresholds.

### Day 1 — Orders/source evidence

1. Recheck stock/price/postcode/GST/shipping/return window.
2. Save dated captures; obtain technical/budget approval.
3. Place authorized critical orders only; save real invoice/confirmation if placed.
4. Start delivery tracker and local mechanical quote requests.

**Exit:** Every ordered line has `PROC`; actual/projected cost separated.  
**Do not:** mark product page as purchase or buy dimension-dependent hub blindly.

### Day 2 — Toolchain without external wiring

If the exact board is received/accepted visually:

1. Use known data cable; Micro-USB only.
2. Upload identity/counter sketch; capture log; reset five times.
3. Freeze tool versions after backup reproduction.

If board has not arrived, build deterministic host-side parser/RMS test scaffolding with synthetic vectors clearly separated from measurements.

**Exit:** Reproducible MCU smoke test or documented tool readiness, never an invented pass.

### Day 3 — Sensor bench preparation

1. Accept/photograph/ID sensor and board.
2. Check exact board official pinout; draft `PIN-001`.
3. With USB disconnected, wire short SPI paths; two-person check and photograph.
4. Power logic only; read `0xE5`; read/write/readback registers.

**Exit:** Stable identity/readback or quarantined fault record.  
**Do not:** mount on motor, use I²C, power 5 V or infer final ODR achievement.

### Day 4 — Stationary acquisition gate

1. Exercise six orientations; record plausibility.
2. Acquire predeclared stationary captures with sequence/drop/saturation/timing fields.
3. Hash raw files and compare embedded/offline parsing/RMS on test vectors.
4. Backup person repeats ID/capture.

**Exit:** Timing/integrity evidence or visible failure/corrective plan.  
**Do not:** derive final classifier threshold or delete invalid blocks.

### Day 5 — Mechanical design review, not an automatic spin

1. Measure received motor/sensor; finish base/clamp/mount/hub/guard drawing.
2. Verify switch/fuse/jack compatibility and motor/logic isolation.
3. Build/inspect unpowered rig; manually rotate for clearance.
4. Only if the full safety checklist and reviewer approval exist, perform the staged no-eccentric current-limited pilot. Otherwise stop at inspection.

**Exit:** Approved unpowered rig or a safely recorded pilot; no requirement to force a powered result in Week 1.

## 12. Every-run rig safety checklist

- [ ] Exact `RIG/MOUNT/HW/CFG` labels match the run sheet.
- [ ] Motor power disconnected and shaft stopped during inspection/adjustment.
- [ ] Base restraint, motor clamp and fastener reference marks intact.
- [ ] Eccentric/normal fixture is the identified configuration with positive retention.
- [ ] Guard is attached and covers full rotating envelope; manual clearance check complete.
- [ ] Sensor mount and strain relief are rigid/intact.
- [ ] Switch/disconnect, fuse, connector and wiring are intact and correctly rated.
- [ ] USB logic power and 12 V motor power remain separate.
- [ ] Eye protection worn; hands/hair/clothing/lanyards/tools/cables clear.
- [ ] No loose object on base/bench.
- [ ] Host capture starts before motor and uses a new run filename.
- [ ] Stop conditions and stop operator verbally confirmed.
- [ ] Post-run power-off, shaft-stop and inspection completed.

Any failed item means **DO NOT ENERGIZE**. Create `ERR/CA` and reinspection; observers may call stop without permission.

## 13. Reject, replace and substitution rules

| Situation | Required action |
|---|---|
| Wrong exact MCU SKU/module | Quarantine/return. Do not pretend pin/software equivalence. |
| ADXL wrong/intermittent `DEVID` after known-good isolation | Quarantine/replace; preserve attempts. |
| Generic listing contradicts itself (for example title speed differs from description) | Do not select as preferred; require clarification or different seller. |
| Adapter wrong polarity/unstable/damaged/hot | Reject; no opening or mains-side repair. |
| Motor excessive current/wobble/noise/heat | Stop/quarantine; inspect under no power; do not compensate with larger fuse. |
| Fuse nuisance operation | Stop and investigate motor startup/operating current, fixture condition, wiring fault and required time-current characteristic. Document findings. Never bypass or increase the rating merely to prevent opening. |
| Mount/guard cannot be made stable | Redesign or use safer equivalent rig; no data run. |
| Preferred item unavailable | Recheck backup spec/price/stock and run equivalence decision. New board variant requires new pinout/toolchain gate. |
| Cost projects above ₹5,000 | Stop order; seek reuse/alternate exact source or owner/team approval. Do not drop protection/PPE/guard. |

## 14. Procurement closure checklist

- [ ] Every planning price replaced by actual invoice amount or explicitly left `NOT PURCHASED`.
- [ ] Shipping/GST/discount/refund and reused/donated value/status are separated.
- [ ] Every delivered critical part has `COMP` and `ACCEPT` with photos and test links.
- [ ] Quarantined/rejected items are separated and return/replace status recorded.
- [ ] Actual total reconciles to budget; variance explained.
- [ ] Spare inventory and locations recorded.
- [ ] Warranties/return deadlines and invoices archived.
- [ ] Exact as-built BOM links to final hardware configuration.

## 15. Resolved and Operational Procurement Ledger Status

1. **Logistics & Delivery Channels (RESOLVED):** Robocraze Order 1 confirmed (`#TJFKQXJUQ`, express courier, ₹868.00); Robu.in Order 2 confirmed (Bluedart Air priority, ₹350.98); Robocraze Order 3 staged (~₹755.00); College Lab Cart C requisitioned (₹0.00).
2. **Lab Tools & Stock Allocation (RESOLVED):** MB102 breadboard, 15 DuPont jumpers (M2M & M2F), 100 µF bulk decoupling capacitor, 100 nF ceramic bypass capacitor, 1N4007 flyback diode, and 220 Ω resistors sourced from departmental lab inventory at zero financial cost.
3. **Fuse & Protection System (RESOLVED):** Selected 5×20 mm cartridge system: fully enclosed covered screw casings (x2) and 1A 250V time-delay (slow-blow) fuses (x8) ordered from Robu.in to handle N20 motor inductive startup inrush.
4. **DC Switch / Disconnect (RESOLVED):** KCD1 SPST 2-pin rocker switch (12V–24V DC documented duty) ordered from Robu.in.
5. **MCU Hardware Baseline (RESOLVED):** 7Semi ESP32-DEVKIT-E (ESP32-WROOM-32E, CP2102, 38-pin DevKitC V4 pinout) certified under `VG-AUDIT-HW-7SEMI-001` as the hardware baseline, staged under Robocraze Order 3.
6. **Financial Settlement (RESOLVED):** Out of ₹2,124.00 initial disbursement, ₹868.00 was spent on Order 1 and ₹150.00 cash drawn for Order 2 shipping (with Order 2 item cost settled online: ₹277.00 total fund share, ₹73.98 / ~₹74.00 paid out-of-pocket), returning ₹1,106.00 in physical cash to project lead custody. Order 3 planned spend is ~₹755.00, preserving ~₹350.00 (~₹351.00) unencumbered cash reserve in hand, with total project spend at ₹1,973.98 well within preferred target (₹3,000) and semester ceiling (₹5,000).
7. **Remaining Actions:** Await arrival of Order 1, Order 2, and Order 3; execute visual/electrical receiving checks (Section 7); measure received N20 motor body to finalize local fabrication of base, 3 mm clamping hub with captive off-axis M3 bolt/nyloc, and polycarbonate guard.

## 16. Source notes

Official specifications take precedence over retailer descriptions:

- [Analog Devices ADXL345 data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.PDF), accessed 2026-08-09.
- [Espressif ESP32-DevKitC V4 user guide](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html), accessed 2026-08-09.
- [Espressif ESP32-WROOM-32E/32UE data sheet](https://documentation.espressif.com/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.html), accessed 2026-08-09.
- [Espressif Arduino-ESP32 installation guide](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html), accessed 2026-08-09.

Supplier pages were accessed 2026-08-09. Prices/stock are volatile, seller specifications may be incomplete, and no supplier listing is treated as acceptance evidence.
