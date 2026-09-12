# VibeGuard: Hardware Physical Measurement & Fit-Audit Guide

**Project:** VibeGuard — Edge AI Mechanical Vibration Diagnostic Testbed  
**Document ID:** VG-GUIDE-MEAS-01  
**Target Hardware:** N20 Micro Metal Gear Motor, Robocraze ADXL345 Breakout (#TJFKQXJUQ), M3 Fasteners, 12 mm Wooden Baseplate  
**Purpose:** Precise physical dimensional audit mapping real hardware measurements to 3D-printed parts (`FAB-01` Rotor Arm & `FAB-02` Rigid Sensor Mount).

---

## 1. System Architecture: The Physical-to-CAD Connection

In precision additive manufacturing (FDM 3D printing in PLA), nominal CAD models must account for real hardware manufacturing tolerances and material thermal shrinkage. The following table establishes the direct causal connection between physical dimensions and CAD features:

| Physical Measurement | Physical Component Feature | Affected 3D Print Part | Target CAD Feature in Model | Functional Impact |
| :--- | :--- | :--- | :--- | :--- |
| **$D_{\text{shaft}}$** | N20 D-Shaft Outer Diameter | `FAB-01` Rotor Arm | Hub D-Bore Diameter | Snug press-fit on shaft without radial play or splitting |
| **$T_{\text{flat}}$** | N20 D-Shaft Flat Thickness | `FAB-01` Rotor Arm | Hub Internal Flat Chord | Anti-slip torque lock preventing rotor arm free-spinning |
| **$L_{\text{shaft}}$** | N20 Usable Shaft Length | `FAB-01` Rotor Arm | Hub Internal Bore Depth | Ensures 1 mm air gap from brass gearbox face (prevents friction drag) |
| **$D_{\text{washer}}$** | M3 Steel Washer Outer Diameter | `FAB-01` Mass Boss & Baseplate | Riser Pedestal Height ($15\text{ mm}$) | Rotational sweep radius clearance; guarantees +6.5 mm daylight gap |
| **$P_{\text{hole}}$** | ADXL345 PCB Mounting Hole Pitch | `FAB-02` Sensor Mount | Upright Wall Dual M3 Hole Pitch | Dual bolt alignment; prevents tilted PCB mounting and axis cross-talk |
| **$D_{\text{pcb\_hole}}$** | ADXL345 PCB Hole Diameter | `FAB-02` Sensor Mount | Upright Hole Clearance ($3.2\text{ mm}$) | M3 screw pass-through without binding |
| **$T_{\text{solder}}$** | ADXL345 Backside Solder Blobs | `FAB-02` Sensor Mount | Upright Face Relief Cavity | Flush planar seating against bracket wall (prevents 5°–10° tilt) |
| **$P_{\text{bracket}}$** | N20 Aluminum U-Bracket Pitch | Baseplate & Riser | Riser Through-Hole Spacing ($17\text{ mm}$) | Direct through-bolting through U-bracket and riser into wood |
| **$T_{\text{plank}}$** | Baseplate Actual Thickness | Baseplate & Feet | M3 Mounting Screw Length Selection | Ensures screw threads grip wood without poking out the bottom |

---

## 2. Exhaustive Caliper Measurement Protocol

Use a digital or vernier caliper set to metric ($0.01\text{ mm}$ or $0.05\text{ mm}$ resolution).

```
          [ CALIPER OUTSIDE JAWS ]          [ CALIPER DEPTH ROD ]
                  |       |                          |
               [==== COMPONENT ====]             [========] ===| (Depth)
```

### 2.1 N20 Micro Metal Gear Motor

#### Measurement 1: Shaft Round Outer Diameter ($D_{\text{shaft}}$)
* **Where to place jaws:** Across the cylindrical, curved section of the steel output shaft.
* **How to measure:** Clamp the wide outside jaws perpendicularly across the shaft. Take 2 readings at 90° to check circularity.
* **Nominal:** $3.00\text{ mm}$ (typical range: $2.95\text{–}3.02\text{ mm}$).
* **CAD Connection:** FDM PLA shrinks inward by $\sim 0.15\text{ mm}$ inside small cylindrical bores. If your measured shaft is $2.98\text{ mm}$, the CAD bore is modeled at $3.15\text{ mm}$ to achieve a perfect push-fit.

#### Measurement 2: Shaft Flat-to-Back Thickness ($T_{\text{flat}}$)
* **Where to place jaws:** Across the D-cut profile.
* **How to measure:** Place one caliper flat jaw directly on the flat milled face of the D-shaft and the opposing jaw against the curved back.
* **Nominal:** $2.50\text{ mm}$ (cut depth is $0.50\text{ mm}$; typical range: $2.42\text{–}2.55\text{ mm}$).
* **CAD Connection:** The chord height inside `FAB-01` must be modeled as $T_{\text{flat}} + 0.125\text{ mm}$ ($2.625\text{ mm}$). If too thick, the arm wobbles; if too thin, it cannot be pressed on.

#### Measurement 3: Shaft Usable Length ($L_{\text{shaft}}$)
* **Where to place probe:** From the tip of the D-shaft back to the brass bearing collar on the gearbox front plate.
* **How to measure:** Extend the caliper depth rod out the bottom. Rest the caliper base against the shaft tip and slide the depth rod until it touches the front brass face.
* **Nominal:** $9.5\text{–}10.0\text{ mm}$.
* **CAD Connection:** Hub depth is modeled at $L_{\text{shaft}} - 1.0\text{ mm}$ ($8.5\text{ mm}$). This ensures the plastic never rubs against the rotating brass gearbox casing.

---

### 2.2 Robocraze ADXL345 Accelerometer Breakout Board

```
      +-------------------------------------------------+
      |   ( O ) <---------- Pitch P ----------> ( O )   |
      |     |                                     |     |  <-- Mounting Holes
      |   [Edge]                                [Edge]  |
      |                                                 |
      |              [ ADXL345 IC CHIP ]                |
      |                                                 |
      |       [ O   O   O   O   O   O   O   O ]         |  <-- 8-pin Header
      +-------------------------------------------------+
```

#### Measurement 4: PCB Mounting Hole Diameter ($D_{\text{pcb\_hole}}$)
* **Where to place jaws:** Inside either of the two copper-ringed mounting holes.
* **How to measure:** Use the upper, pointed **inside jaws**. Insert them into the hole and expand gently until both knife edges touch the copper rim.
* **Nominal:** $3.1\text{–}3.2\text{ mm}$ (clearance for M3).
* **CAD Connection:** Verifies that M3 machine screws pass through without binding. If a board has $2.6\text{ mm}$ holes, it requires M2.5 screws.

#### Measurement 5: Center-to-Center Hole Pitch ($P_{\text{hole}}$)
* **Where to place jaws:** Between the two mounting holes.
* **How to measure (The Pro Caliper Trick):**
  1. Measure the diameter of Hole 1: $D$.
  2. Measure from the **outer left rim** of Hole 1 to the **outer right rim** of Hole 2: $W_{\text{outer}}$.
  3. Calculate pitch: $P = W_{\text{outer}} - D$.
  *(Alternatively: Measure from the left inner rim of Hole 1 to the left inner rim of Hole 2 directly).*
* **Nominal:** $15.0\text{ mm}$ (or $15.24\text{ mm}$ / 0.6 inch grid).
* **CAD Connection:** Dictates the exact center-to-center distance between the two horizontal M3 through-holes on the vertical wall of `FAB-02`. A $0.5\text{ mm}$ error will wedge the screws and stress the PCB.

#### Measurement 6: Backside Pin Solder Protrusion ($T_{\text{solder}}$)
* **Where to place probe:** On the rear surface of the PCB behind the soldered 8-pin header.
* **How to measure:** Measure how far the clipped pin ends or solder joints protrude beyond the flat fiberglass surface.
* **Nominal:** $1.0\text{–}1.8\text{ mm}$.
* **CAD Connection:** If pins protrude, the vertical mounting wall of `FAB-02` incorporates a clearance pocket so the PCB sits 100% flush and orthogonal without tilting.

---

### 2.3 Fasteners & Unbalance Counterweight

#### Measurement 7: Washer Outer Diameter ($D_{\text{washer}}$)
* **Where to place jaws:** Across the diameter of the steel washers used on the M3 unbalance bolt.
* **How to measure:** Clamp caliper outside jaws across the widest diameter of the washer.
* **Nominal:** Standard DIN 125 is $7.0\text{ mm}$; Wide DIN 9021 is $9.0\text{ mm}$.
* **CAD Connection:** Directly determines the **Rotational Sweep Radius**:
  $$R_{\text{sweep}} = 12.0\text{ mm} + \frac{D_{\text{washer}}}{2}$$
  At $D = 9.0\text{ mm}$, $R_{\text{sweep}} = 16.5\text{ mm}$. With our $15\text{ mm}$ riser, the shaft sits at $Y = 35.0\text{ mm}$, yielding $+6.5\text{ mm}$ daylight clearance above the $12\text{ mm}$ baseplate.

---

## 3. Caliper Audit Checklist

Copy and record your exact readings below:

| Component | Target Feature | Nominal (mm) | Your Caliper Reading (mm) | Difference ($\Delta$) |
| :--- | :--- | :--- | :--- | :--- |
| **N20 Motor** | Shaft Round OD ($D_{\text{shaft}}$) | 3.00 | _____ | _____ |
| **N20 Motor** | Shaft Flat Thickness ($T_{\text{flat}}$) | 2.50 | _____ | _____ |
| **N20 Motor** | Usable Shaft Length ($L_{\text{shaft}}$) | 9.50 | _____ | _____ |
| **N20 Motor** | Brass Collar Diameter | 4.20 | _____ | _____ |
| **N20 U-Bracket** | Base Mounting Hole Pitch | 17.00 | _____ | _____ |
| **N20 U-Bracket** | Base Plate Thickness | 2.00 | _____ | _____ |
| **ADXL345 Board** | PCB Hole Diameter | 3.20 | _____ | _____ |
| **ADXL345 Board** | Hole Center-to-Center Pitch | 15.00 | _____ | _____ |
| **ADXL345 Board** | Backside Solder Protrusion | 1.20 | _____ | _____ |
| **M3 Fasteners** | Washer Outer Diameter ($D_{\text{washer}}$) | 9.00 | _____ | _____ |
| **M3 Fasteners** | M3 Bolt Under-Head Length | 15.00 | _____ | _____ |
| **Wood Plank** | Actual Baseplate Thickness | 12.00 | _____ | _____ |

---
