# VibeGuard: College FabLab 3D Printing Specification & Job Requisition
**Project:** VibeGuard — Edge AI Vibration Monitoring & Predictive Maintenance System  
**Institution:** Jyothi Engineering College (Autonomous), Cheruthuruthy, Kerala  
**Department:** Computer Science & Engineering / Electronics & Communication Engineering  
**Facility:** College FabLab / 3D Printing & Prototyping Center  
**Lab Rate:** ₹4.00 per gram (Standard College FabLab PLA/PETG Tariff)  
**Primary Contact:** Amith Krishna Das (Hardware & Mechanical Lead)  

---

## 1. Executive Summary for FabLab Operator / Technician

> [!NOTE]
> **Context:** This project investigates rotational unbalance and structural bearing vibration at low frequencies (10 Hz / 600 RPM). We need precision 3D-printed components to couple a miniature DC gear motor to an eccentric test mass and to rigidly mount an ADXL345 3-axis digital accelerometer.

We request the fabrication of **Two Essential Mechanical Parts** (and one optional safety shroud) on an FDM printer (Ender-3, Prusa MK3/MK4, or Bambu Lab):

| Part ID | Component Name | Function | Material | Infill | Est. Mass | Est. Cost (@ ₹4/g) | Priority |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|
| **FAB-01** | **3 mm D-Shaft Eccentric Rotor Arm** | Slides onto N20 motor shaft; carries M3 unbalance bolt & washers | PLA / PETG | 80%–100% | **3.5 g** | **₹14.00** | **CRITICAL (Mandatory)** |
| **FAB-02** | **ADXL345 Rigid Sensor Mounting Bracket** | Rigidly couples accelerometer to baseplate without vibration damping | PLA | 60%–80% | **5.5 g** | **₹22.00** | **HIGH (Recommended)** |
| **FAB-03** | **Perforated Rotor Safety Shroud** *(Optional)* | Protective containment cage over spinning 600 RPM rotor arm | PLA | 20% | **18.0 g** | **₹72.00** | *Optional (Can use ₹0 clear cup)* |
| **FAB-04** | **FAB-01 Spare / Backup Unit** | Duplicate rotor arm for calibration bench backup | PLA / PETG | 80%–100% | **3.5 g** | **₹14.00** | **Recommended** |

* **Total Essential Print Package (FAB-01 × 2 + FAB-02):** **~12.5 grams $\rightarrow$ Total Expected Cost: ₹50.00**  
* **Total If Including Full Printed Shroud (FAB-01 × 2 + FAB-02 + FAB-03):** **~30.5 grams $\rightarrow$ Total Expected Cost: ₹122.00**

---

## 2. Detailed Technical Specifications & CAD Dimensions

### Part FAB-01: 3 mm D-Shaft Eccentric Rotor Arm (Cam)

```
        Top View (mm)
          +-----------------------------+
          |  ( O )              ( O )   |
          +-----------------------------+
          |<---- 8 mm ---->|   |< 8 mm >|
             Shaft Hub           Mass Hub
          |<--------- 20.0 mm --------->|
                  (Center-to-Center)
                     Radius r = 12 mm
```

#### Exact Functional Dimensions
1. **Motor Shaft Interface (D-Bore Hub):**
   * **Nominal Shaft Diameter:** 3.00 mm (N20 Micro Metal Gear Motor output shaft).
   * **D-Profile Geometry:** Circular bore of diameter **$3.15\text{ mm}$** (accounting for FDM hole shrinkage) with a **flat chord face at $2.65\text{ mm}$ across the flat**.
   * **Hub Outer Diameter ($OD$):** $8.50\text{ mm}$.
   * **Hub Height / Depth:** $9.00\text{ mm}$ (covers the full 9.5 mm flat of the N20 shaft).
   * **Set Screw Hole (Lateral):** $2.50\text{ mm}$ through-hole perpendicular to the flat face (to optionally tap an M3 grub screw for positive retention).
2. **Connecting Arm Linkage:**
   * **Length (Shaft center to weight hole center):** **$12.00\text{ mm}$** (governing dynamic eccentric radius $r$).
   * **Width:** $7.50\text{ mm}$.
   * **Thickness:** $4.00\text{ mm}$.
3. **Eccentric Mass Mounting Hole:**
   * **Through-hole Diameter:** **$3.20\text{ mm}$** (clearance for standard M3 bolt).
   * **Hub Outer Diameter around hole:** $8.00\text{ mm}$.
   * **Counterbore / Nut Recess (Top Face):** Hexagonal recess of **$5.60\text{ mm}$ across flats**, depth $2.50\text{ mm}$ (to capture an M3 hex nut or Nyloc nut firmly without spinning).

#### Recommended Slicer Settings for FAB-01
* **Layer Height:** 0.16 mm or 0.20 mm.
* **Perimeters / Wall Loops:** 4 walls (minimum) — crucial so the shaft bore is solid plastic, not infill.
* **Top & Bottom Solid Layers:** 4 layers.
* **Infill:** 80% to 100% (Gyroid or Rectilinear). High density is required to withstand 10 Hz rotational centrifugal force without dynamic flexing.
* **Material:** PLA or PETG (Black, Grey, or Blue).

---

### Part FAB-02: ADXL345 Rigid Accelerometer Mounting Bracket

```
           Front View (L-Bracket)
           | |  <-- 3.0 mm thick rigid upright
           | |  <-- 2x M3 holes spaced 15.0 mm apart (for ADXL345 board)
           | |
        ___| |_______
       |_____________|  <-- Stiff base flange (4.0 mm thick) with 2x wood screw holes
```

#### Exact Functional Dimensions
1. **Sensor Flange (Vertical Face):**
   * **Height:** $22.00\text{ mm}$, **Width:** $24.00\text{ mm}$, **Thickness:** $3.50\text{ mm}$.
   * **Sensor Mounting Holes:** Two **$3.20\text{ mm}$ diameter holes**, spaced exactly **$15.00\text{ mm}$ center-to-center** horizontally, elevated $10.00\text{ mm}$ from the base.
2. **Baseplate Mounting Flange (Horizontal Face):**
   * **Depth:** $18.00\text{ mm}$, **Width:** $24.00\text{ mm}$, **Thickness:** $4.00\text{ mm}$.
   * **Base Screw Holes:** Two **$3.50\text{ mm}$ countersunk holes** spaced $16.00\text{ mm}$ apart for securing into the wooden baseplate with wood screws.
3. **Stiffening Gussets:** Two triangular 45° gussets ($3.0\text{ mm}$ thick) joining vertical and horizontal walls to prevent high-frequency cantilever resonance.

#### Recommended Slicer Settings for FAB-02
* **Layer Height:** 0.20 mm.
* **Infill:** 60% Gyroid.
* **Perimeters:** 3 to 4 walls.
* **Orientation:** Print resting on the flat base flange (no support required).

---

### Part FAB-03: Perforated Safety Containment Shroud *(Optional)*

```
              Isometric Shroud Wireframe
                 +-------------------+
                /                   /|
               +-------------------+ |
               |   [ VENT SLOTS ]  | | Height: 35 mm
               |   [    ///     ]  | +
               |                   |/
               +-------------------+
                 Base: 42 x 38 mm
```

#### Exact Functional Dimensions
* **External Footprint:** $42.00\text{ mm} \times 38.00\text{ mm} \times 35.00\text{ mm}$ height.
* **Internal Clearance:** Guarantees $\ge 6.00\text{ mm}$ clearance around the $12\text{ mm}$ rotating arm + M3 bolt head at all 360° positions.
* **Wall Thickness:** $1.60\text{ mm}$ (4 perimeters with 0.4 mm nozzle).
* **Observation & Airflow Slots:** Three $3\text{ mm} \times 20\text{ mm}$ vertical viewing slots on top and side to observe rotation without opening the guard.
* **Mounting Lugs:** Two $10\text{ mm}$ exterior ears at base with $3.5\text{ mm}$ holes to screw directly onto the wood baseplate.

---

## 3. Step-by-Step Instructions for FabLab Technician

1. **CAD File Generation / Import:**
   * Import the STL/STEP files into PrusaSlicer / Bambu Studio / Cura.
   * If generating CAD from scratch in Fusion 360 / SolidWorks / Onshape, use the parametric sketches defined in Section 2.
2. **Material Selection:**
   * **Preferred:** Standard PLA (1.75 mm) — high Young's modulus ($E \approx 3.5\text{ GPa}$) ensures exceptional rigidity for vibration transfer.
   * **Alternative:** PETG — good layer adhesion and impact resistance.
3. **Print Execution:**
   * Clean print bed with Isopropyl Alcohol (IPA) to ensure flat first layer without warping.
   * Total print duration:
     * FAB-01 (Rotor Arm): ~12 minutes per piece.
     * FAB-02 (Sensor Bracket): ~18 minutes.
     * Total runtime: **~40 minutes** for the essential set.
4. **Post-Processing & Quality Check:**
   * **Bore Fit Check:** Take a 3.0 mm steel rod or N20 motor shaft and test the D-profile fit. The rotor arm should slide on snugly by hand with zero radial wobble.
   * **Deburring:** Clean any brim or elephants-foot brim from the bottom of the D-bore using a 3 mm hobby drill bit or craft blade.

---

## 4. Billing & Requisition Approval Slip

```text
========================================================================
             JYOTHI ENGINEERING COLLEGE - FABLAB REQUISITION
========================================================================
Project Title    : VibeGuard (Edge AI Vibration Monitoring Rig)
Academic Course  : PBCST504 / Final Year Embedded Project
Student Name     : Amith Krishna Das & Team
Department       : CSE / ECE

Items Ordered:
1. 3mm D-Shaft Eccentric Rotor Arm (FAB-01 x 2)   :  ~7.0 grams
2. ADXL345 Rigid Sensor Bracket (FAB-02 x 1)      :  ~5.5 grams
3. Optional Safety Shroud (FAB-03 x 1)           : [ ] Check if requested (~18g)

Calculated Weight (Essential Set)                 : 12.5 grams
FabLab Tariff Rate                                : ₹4.00 per gram
------------------------------------------------------------------------
ESTIMATED LAB FEE PAYABLE                         : ₹50.00 (or ₹122.00 w/ shroud)
------------------------------------------------------------------------

Technician Signature : ___________________   Date: ___________________
Lab Supervisor Stamp : ___________________
========================================================================
```
