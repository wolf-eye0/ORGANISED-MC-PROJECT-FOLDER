# VibeGuard: Procurement Ledger, Receipts Metadata Log & Chronological Audit

**Document Reference:** `VG-PROC-LEDGER-2026-09-11`  
**Revision:** 2.1 (Full Order Fulfillment & Physical Delivery Reconciliation)  
**Governance Authority:** Phase 4 Execution Package (`07_SEMESTER_EXECUTION/`)  
**Project:** VibeGuard — Edge AI Vibration Monitoring & Predictive Maintenance System  
**Institution:** Jyothi Engineering College (Autonomous), Cheruthuruthy, Kerala  
**Custodian:** Nihad P C (Project Lead) & Amith Krishna Das (Hardware Lead)  
**Verification Date:** 2026-09-11  

---

## 1. Executive Procurement Status & Milestone Summary

As of **September 11, 2026**, all three major commercial supplier orders have arrived, been unboxed, and been verified against their physical tax invoices. The core computing microcontroller (7Semi ESP32), vibration sensor (ADXL345), drive motor (N20), power system, safety fuses, and jumper wiring are **100% in physical possession**.

```
+-----------------------------------------------------------------------------------------+
|                              VIBEGUARD PROCUREMENT TIMELINE                             |
+-----------------------------------------------------------------------------------------+
  2026-09-05: Initial Cash Advance Disbursed (₹2,124.00)
       |
  2026-09-06: Robu.in Order Invoiced [INV2627/230020] (₹350.98) - Fuses, Switch, Resistors
       |
  2026-09-06: Robocraze Order 1 Invoiced [RC/26-27/59205] (₹868.00) - Motor, ADXL345, 12V PSU
       |
  2026-09-07: Robocraze Order 2 Placed (Order #365744)
       |
  2026-09-08: Robocraze Order 2 Invoiced [RC/26-27/59949] (₹923.95) - 7Semi ESP32, DC Jack, Jumpers
       |
  2026-09-11: Commercial packages unboxed, bills audited, passives verified, CAD/STLs deployed.
       |
  2026-09-12: ET Store Order Received In-Hand (MB102 Breadboard, M3 Hardware, Passives).
       |
  2026-09-12: Rig Baseplate Acquired: Two 150×150×5mm Acrylite Sheets (10mm Laminated Slab) In-Hand.
       |
  2026-09-13: 3D Printing Gated on Measurement Audit (30cm Ruler Guide Deployed to verify N20 D-shaft & ADXL345 pitch).
+-----------------------------------------------------------------------------------------+
```

---

## 2. Chronological Procurement & Milestone Date Log

| Event Timestamp | Milestone Event | Entity / Channel | Documentation / Reference | Financial Impact | Cumulative Spend |
|---|---|---|---|---:|---:|
| **2026-09-05 10:30 IST** | **Initial Project Cash Disbursement** | Project Faculty Sponsor | Formal semester project operational advance | +₹2,124.00 (Inflow) | ₹0.00 |
| **2026-09-06 14:03 IST** | **Robocraze Order 1 Placed & Invoiced** | Robocraze (TIF Labs Pvt Ltd) | Tax Invoice `RC/26-27/59205` / Order `#365012` | -₹868.00 | ₹868.00 |
| **2026-09-06 15:45 IST** | **Robu.in Order Placed & Invoiced** | Robu.in (Macfos Limited) | Tax Invoice `INV2627/230020` / Order `#3684676` | -₹350.98 | ₹1,218.98 |
| **2026-09-06 20:30 IST** | **Interim Cash Custody Reconciliation** | Hardware Lead $\rightarrow$ Project Lead | Cash advance balance returned to project lead custody | Handover (₹1,106.00) | ₹1,218.98 |
| **2026-09-07 23:53 IST** | **Robocraze Order 2 Placed** | Robocraze (Shopify) | Order `#365744` (7Semi ESP32, DC Jack, Jumpers) | Staged | ₹1,218.98 |
| **2026-09-08 11:20 IST** | **Robocraze Order 2 Invoiced & Dispatched**| Robocraze (TIF Labs Pvt Ltd) | Tax Invoice `RC/26-27/59949` / AWB `90656163776` | -₹923.95 | ₹2,142.93 |
| **2026-09-11 08:30 IST** | **Physical Package Receiving & Inspection** | Campus Delivery Reception | BlueDart Air packages received at Jyothi Engineering College | Physical Delivery | ₹2,142.93 |
| **2026-09-11 09:30 IST** | **Hardware Verification & Audit** | Integration Team | 3 Tax Invoices checked off with pen ticks; components audited | Verified In-Hand | ₹2,142.93 |
| **2026-09-11 10:00 IST** | **CAD Models & Job Requisitions Deployed**| FabLab & Mech Workshop | Generated binary STLs, 3D WebGL viewer, PDF/DOCX specs | Planned (~₹50.00) | ₹2,142.93 |
| **2026-09-12 16:30 IST** | **ET Store Order Received & Verified** | ET Store (Thrissur) | MB102 Breadboard, M3 Bolts, Washers, Nyloc Nuts received | -₹105.00 | ~₹2,247.93 |
| **2026-09-12 18:00 IST** | **Baseplate Acrylite Sheets Acquired** | Local Acrylic Supplier | 2× 5mm 150×150mm Cast Acrylic Sheets ($10\text{ mm}$ laminated slab) | In Hand | ~₹2,247.93 |
| **2026-09-13 00:00 IST** | **3D Print Measurement Audit Protocol** | FabLab Quality Assurance | 30cm Ruler Measurement Guide deployed; prints paused for physical audit | Active Audit | ~₹2,247.93 |

---

## 3. Verified Invoice Metadata & Receipt Records

### 3.1 Invoice 1: Robu.in (Macfos Limited)
* **Local Receipt Archive:** [`./invoices/Robu_Invoice_230020_Fuses_Switch_Resistors.jpeg`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/02_BOM_and_Procurement/CURRENT/invoices/Robu_Invoice_230020_Fuses_Switch_Resistors.jpeg)
* **Invoice Number:** `INV2627/230020`
* **Sale Order Reference:** `3684676`
* **Invoice Date:** `06/09/2026`
* **Seller:** Macfos Limited, Dynamic Logistics Trade Park, Bhosari Alandi Road, Pune 411015, Maharashtra
* **GSTIN (Seller):** `27AALCM3536H1ZA` | **Place of Supply:** 32 - Kerala
* **Customer:** Amith Krishna Das, Jyothi Engineering College, Vettikattiri, Cheruthuruthy, Thrissur 679531
* **Shipping Carrier:** Bluedart Air

#### Itemized Line Items:
| Line | SKU | Description | HSN | Unit Price (Excl. Tax) | Qty | Disc | Taxable Value | IGST (18%) | Total (₹) | Status |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `R261532` | 5*20mm Fuse Casing Pipe with 20AWG | 84799090 | ₹25.425 | 2.00 | ₹0.00 | ₹50.85 | ₹9.15 | **₹60.00** | In Hand |
| 2 | `R122949` | Littelfuse 0213001.MXP 1A 250V Time Delay Cartridge Fuse (5×20mm) | 85361090 | ₹2.491 | 9.00 | ₹0.00 | ₹22.42 | ₹4.04 | **₹26.46** | In Hand |
| 3 | `662916` | 330 Ohm 1/8W Through Hole Resistor | 85331000 | ₹0.220 | 52.00 | ₹0.00 | ₹11.46 | ₹2.06 | **₹13.52** | In Hand |
| 4 | `1265367` | KCD1 12V-24V ON-OFF 2 PIN Rocker Switch | 85365010 | ₹86.440 | 1.00 | ₹0.00 | ₹86.44 | ₹15.56 | **₹102.00** | In Hand |
| 5 | `SHP-01` | Bluedart Air Priority Shipping | 996819 | ₹126.270 | 1.00 | ₹0.00 | ₹126.27 | ₹22.73 | **₹149.00** | Paid |
| **Total** | | | | | **65.00** | | **₹297.44** | **₹53.54** | **₹350.98** | **Audited** |

---

### 3.2 Invoice 2: Robocraze (TIF Labs Pvt Ltd) — Order 1
* **Local Receipt Archive:** [`./invoices/Robocraze_Invoice_365012_Motor_Sensor_Adapter.jpeg`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/02_BOM_and_Procurement/CURRENT/invoices/Robocraze_Invoice_365012_Motor_Sensor_Adapter.jpeg)
* **Invoice Number:** `RC/26-27/59205`
* **Order Number:** `365012`
* **Invoice Date:** `2026-09-06 14:03:31 IST`
* **Seller:** TIF Labs Pvt Ltd, Kalyan Nagar WH BLR, Bengaluru 560043, Karnataka
* **GSTIN (Seller):** `29AAFCT7562C1Z5` | **PAN:** `AAFCT7562C`
* **AWB Number:** `90654232642` | **Carrier:** Bluedart
* **Customer:** Amith Krishna Das, Jyothi Engineering College, Cheruthuruthy, Kerala 679531

#### Itemized Line Items:
| Line | SKU | Description | HSN | Unit Price (Excl. Tax) | Qty | Disc | Taxable Value | IGST (18%) | Total (₹) | Status |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `TIFAC0268` | Mounting Bracket for N20 Metal Gear Motors | 84439910 | ₹12.71 | 1 | ₹0.00 | ₹12.71 | ₹2.29 | **₹15.00** | In Hand |
| 2 | `TIFEC0081` | 5MM RGB LED Common Cathode - Clear | 85414020 | ₹2.54 | 10 | ₹0.00 | ₹25.42 | ₹4.58 | **₹30.00** | In Hand |
| 3 | `TIFPS0172` | 12V 2AMP Power Adapter | 85049090 | ₹149.15 | 1 | ₹0.00 | ₹149.15 | ₹26.85 | **₹176.00** | In Hand |
| 4 | `TIFMC0318` | N20 Motor 600 RPM with Cable (12V) | 85011019 | ₹197.46 | 1 | ₹0.00 | ₹197.46 | ₹35.54 | **₹233.00** | In Hand |
| 5 | `TIFCW0030` | MICRO USB Data Cable | 85441990 | ₹32.20 | 1 | ₹0.00 | ₹32.20 | ₹5.80 | **₹38.00** | In Hand |
| 6 | `TIFSS0018` | ADXL345 3-Axis Digital Accelerometer Module | 90318000 | ₹212.71 | 1 | ₹0.00 | ₹212.71 | ₹38.29 | **₹251.00** | In Hand |
| 7 | `SHP-02` | Shipping Method: Premium Shipping | — | ₹105.93 | 1 | ₹0.00 | ₹105.93 | ₹19.07 | **₹125.00** | Paid |
| **Total** | | | | | **16** | | **₹735.58** | **₹132.42** | **₹868.00** | **Audited** |

---

### 3.3 Invoice 3: Robocraze (TIF Labs Pvt Ltd) — Order 2
* **Local Receipt Archive:** [`./invoices/Robocraze_Invoice_365744_ESP32_DCJack_Jumpers.jpeg`](file:///home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/02_BOM_and_Procurement/CURRENT/invoices/Robocraze_Invoice_365744_ESP32_DCJack_Jumpers.jpeg)
* **Invoice Number:** `RC/26-27/59949`
* **Order Number:** `365744`
* **Order Date:** `2026-09-07 23:53:35 IST` | **Invoice Date:** `2026-09-08`
* **Seller:** TIF Labs Pvt Ltd, Kalyan Nagar WH BLR, Bengaluru 560043, Karnataka
* **GSTIN (Seller):** `29AAFCT7562C1Z5` | **PAN:** `AAFCT7562C`
* **AWB Number:** `90656163776` | **Carrier:** Bluedart
* **Customer:** Amith Krishna Das, Jyothi Engineering College, Cheruthuruthy, Kerala 679531

#### Itemized Line Items:
| Line | SKU | Description | HSN | Unit Price (Excl. Tax) | Qty | Disc | Taxable Value | IGST (18%) | Total (₹) | Status |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `TIFCW0038` | Male to Female Jumper Wire - 20 pcs 20cm | 85441910 | ₹18.96 | 2 (40 pcs) | -₹1.90 | ₹36.02 | ₹6.48 | **₹42.51** | In Hand |
| 2 | `TIFCW0039` | Female to Female Jumper Wire - 20 pcs 20cm | 85441910 | ₹17.49 | 2 (40 pcs) | -₹1.75 | ₹33.24 | ₹5.98 | **₹39.22** | In Hand |
| 3 | `TIFCW0037` | Male to Male Jumper Wire - 20 pcs 20cm | 85441910 | ₹21.17 | 2 (40 pcs) | -₹2.12 | ₹40.23 | ₹7.24 | **₹47.47** | In Hand |
| 4 | `TIFPS0017` | DC Jack Female Plug Adapter (5.5×2.1mm) | 85177010 | ₹16.10 | 1 | -₹0.81 | ₹15.30 | ₹2.75 | **₹18.05** | In Hand |
| 5 | `TIFCC0294` | 7Semi ESP32-DEVKIT-E Development Board | 85141000 | ₹581.36 | 1 | -₹29.07 | ₹552.29 | ₹99.41 | **₹651.70** | In Hand |
| 6 | `SHP-03` | Shipping Method: Premium Shipping | — | ₹105.93 | 1 | ₹0.00 | ₹105.93 | ₹19.07 | **₹125.00** | Paid |
| **Total** | | | | | **8 pk** | | **₹677.08** | **₹121.87** | **₹923.95** | **Audited** |

---

## 4. Master Financial Reconciliation Ledger

```
+---------------------------------------------------------------------------------------+
|                          VIBEGUARD COMPREHENSIVE FINANCIAL AUDIT                      |
+---------------------------------------------------------------------------------------+
  Total Inflow (Faculty Advance Cash Fund):                                 ₹2,124.00
  
  ACTUAL COMMERCIAL DISBURSEMENTS (VERIFIED VIA TAX INVOICES):
  1. Robocraze Order 1 (Invoice RC/26-27/59205):                          - ₹868.00
  2. Robu.in Order 2 (Invoice INV2627/230020):                             - ₹350.98
  3. Robocraze Order 2 (Invoice RC/26-27/59949):                          - ₹923.95
  ---------------------------------------------------------------------------------------
  Total Commercial Sourcing Spend:                                          ₹2,142.93
  Net Variance against Initial Advance:                                     - ₹18.93
  
  PROJECTED FINAL FABRICATION & HARDWARE OUTLAY:
  4. College FabLab 3D Printing (12.5g @ ₹4/g):                           ~ ₹50.00
  5. Mechanical Workshop Baseplate (15x15cm Plywood Scrap):                   ₹0.00
  6. ECE Lab Breadboard Requisition:                                          ₹0.00
  7. Local M3 Hardware (Bolt, Washers, Nyloc Nut):                         ~ ₹15.00
  ---------------------------------------------------------------------------------------
  PROJECTED TOTAL FINAL SYSTEM COST:                                       ~ ₹2,207.93
  (Comfortably below ₹3,000 preferred target and ₹5,000 semester budget ceiling)
+---------------------------------------------------------------------------------------+
```

---

## 5. Master Inventory Reconciliation Table

| Master Item ID | Component Description | Sourcing Channel | Reference Bill / ID | Unit Cost | Total Cost | In Hand? |
|:---:|---|---|---|---:|---:|:---:|
| **MCU-01** | 7Semi ESP32-DEVKIT-E (CP2102, 38-Pin) | Robocraze Order 2 | `RC/26-27/59949` | ₹651.70 | ₹651.70 | **YES** |
| **ACC-01** | ADXL345 3-Axis Digital Accelerometer | Robocraze Order 1 | `RC/26-27/59205` | ₹251.00 | ₹251.00 | **YES** |
| **MOT-01** | N20 12V 600 RPM Metal Gear Motor + Cable | Robocraze Order 1 | `RC/26-27/59205` | ₹233.00 | ₹233.00 | **YES** |
| **BRK-01** | N20 Aluminum Mounting U-Bracket | Robocraze Order 1 | `RC/26-27/59205` | ₹15.00 | ₹15.00 | **YES** |
| **PWR-01** | 12V 2A AC-DC Wall Power Supply | Robocraze Order 1 | `RC/26-27/59205` | ₹176.00 | ₹176.00 | **YES** |
| **PWR-02** | DC Barrel Jack 5.5×2.1mm Screw Terminal | Robocraze Order 2 | `RC/26-27/59949` | ₹18.05 | ₹18.05 | **YES** |
| **SW-01** | KCD1 12V–24V ON-OFF 2-Pin Rocker Switch | Robu.in | `INV2627/230020` | ₹102.00 | ₹102.00 | **YES** |
| **FUS-01** | 5×20mm Inline Fuse Casing Pipe (20AWG) (×2) | Robu.in | `INV2627/230020` | ₹30.00 | ₹60.00 | **YES** |
| **FUS-02** | Littelfuse 1A 250V Time Delay Cartridge Fuse (×9) | Robu.in | `INV2627/230020` | ₹2.94 | ₹26.46 | **YES** |
| **CAB-01** | Micro-USB 1m Data Cable | Robocraze Order 1 | `RC/26-27/59205` | ₹38.00 | ₹38.00 | **YES** |
| **CAB-02** | DuPont Jumper Wires (40 M-F, 40 F-F, 40 M-M) | Robocraze Order 2 | `RC/26-27/59949` | ₹129.20 | ₹129.20 | **YES** |
| **LED-01** | 5mm Common Cathode Clear RGB LED (×10) | Robocraze Order 1 | `RC/26-27/59205` | ₹3.00 | ₹30.00 | **YES** |
| **RES-01** | 330 Ω 1/8W Through-Hole Resistors (×52) | Robu.in | `INV2627/230020` | ₹0.26 | ₹13.52 | **YES** |
| **CAP-01** | 100 µF 25V Low-ESR Bulk Electrolytic Cap (×2) | College ECE Lab | Lab Drawer Stock | ₹0.00 | ₹0.00 | **YES** |
| **CAP-02** | 100 nF (0.1 µF "104") Ceramic Bypass Cap (×2) | College ECE Lab | Lab Drawer Stock | ₹0.00 | ₹0.00 | **YES** |
| **DIO-01** | 1N4007 1A 1000V Silicon Rectifier Diode (×1) | College ECE Lab | Lab Drawer Stock | ₹0.00 | ₹0.00 | **YES** |
| **BRD-01** | MB102 830-Point Solderless Breadboard | ET Store Thrissur | `ET8102` | ₹80.00 | ₹80.00 | **YES** |
| **BOLT-01**| M3 × 16mm & 20mm Pan Head SS Bolts (×4) | ET Store Thrissur | `ET6134` / `ET6107` | ₹1.45 | ₹8.42 | **YES** |
| **WASH-01**| M3 Flat Stainless Steel Washers (×10) | ET Store Thrissur | `ET6159` | ₹0.60 | ₹6.00 | **YES** |
| **NUT-01** | M3 Nyloc Nuts (×4) & Hex Nuts (×4) | ET Store Thrissur | `ET6602` / `ET6110` | ₹2.06 | ₹10.92 | **YES** |
| **PLK-01** | $150 \times 150 \times 5\text{ mm}$ Cast Acrylic Sheets (×2, $10\text{ mm}$ laminated) | Local Sourcing | Acrylite Transparent PMMA | Sourced | — | **YES** |
| **FAB-01** | 3mm D-Shaft Eccentric Rotor Arm (Monolithic Solid) | College FabLab | Measurement Audit | ~₹14.00 | ~₹28.00 | **Audit Active** |
| **FAB-02** | ADXL345 Rigid Accelerometer Mount (Monolithic Solid)| College FabLab | Measurement Audit | ~₹22.00 | ~₹22.00 | **Audit Active** |
