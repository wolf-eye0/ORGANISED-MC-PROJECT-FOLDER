# VibeGuard: 1-Page FabLab Slicer & Printability Guide
**Document ID:** VG-FAB-SLICER-01  
**Project:** VibeGuard — Edge AI Vibration Monitoring & Predictive Maintenance System  
**Target Facility:** College FabLab / 3D Printing Prototyping Center  
**Target Printers:** FDM Systems (Bambu Lab P1S/X1C, Prusa MK3/MK4/MINI+, Creality Ender-3 v2/S1)  
**Materials:** Standard PLA (Preferred, $E \approx 3.5\text{ GPa}$) or PETG | Nozzle: 0.40 mm  

---

## 1. Quick Slicer Parameter Matrix

| Parameter | FAB-01: Eccentric Rotor Cam Arm (`VibeGuard_Rotor_Arm_D_Shaft.stl`) | FAB-02: ADXL345 Rigid Mount with Window (`VibeGuard_ADXL345_Rigid_Mount.stl`) | FAB-03: Under-Motor Shim Pads (`VibeGuard_N20_Motor_Shim_Pad_*.stl`) |
|---|---|---|---|
| **Function** | Rotates at 10 Hz (600 RPM) carrying M3 unbalance bolt | Rigidly couples ADXL345 sensor to acrylic baseplate; routes reverse jumper wires | Eliminates 1.0–1.2 mm vertical gap under N20 motor cradle |
| **Print Orientation** | **Flat on bottom face ($Z=0$)**; shaft bore vertical | **Flat on bottom foot flange ($Z=0$)**; upright vertical | **Flat on build plate ($Z=0$)** |
| **Support Material** | **NONE (0% supports required)** | **NONE (0% supports required — 1.0 mm top tie-bar bridges cleanly)** | **NONE (0% supports required)** |
| **Layer Height** | **0.16 mm** (recommended for bore resolution) or 0.20 mm | **0.16 – 0.20 mm** (clean bridge spanning) | **0.16 – 0.20 mm** |
| **Perimeter Walls** | **Minimum 4 walls** ($\ge 1.6\text{ mm}$ solid perimeter boundary) | **Minimum 4 walls** ($\ge 1.6\text{ mm}$ solid perimeter boundary) | **3 walls** |
| **Top / Bottom Layers** | 4 Top / 4 Bottom solid layers | 4 Top / 4 Bottom solid layers | 4 Top / 4 Bottom solid layers |
| **Infill Density** | **100% Solid** (Rectilinear) | **80% to 100%** (Gyroid or Grid) | **100% Solid** |
| **Dynamic Rationale** | Prevents centrifugal fatigue and flexing at 10 Hz | Eliminates compliance/damping; wire window avoids pin collision | High compressive stiffness under bracket clamping force |
| **Brim / Adhesion** | Skirt only (add 3 mm outer brim only if bed adhesion is weak) | Skirt only (large $24 \times 18\text{ mm}$ footprint provides excellent grip) | Skirt only |
| **Est. Print Time** | ~12 to 15 minutes | ~20 to 22 minutes | ~3 to 5 minutes |
| **Filament Used** | ~3.5 grams PLA | ~5.5 grams PLA | ~0.8 grams PLA |

---

## 2. Geometry, Shrinkage Compensation & Slicing Notes

### A. FAB-01 D-Shaft Bore & Dynamic Unbalance Arm
1. **Shaft Fit & Thermal Shrinkage Compensation:**  
   * **N20 Motor Shaft:** Nominal 3.00 mm diameter, 2.50 mm flat-to-back, 9.5 mm usable length.  
   * **Standard Model (`VibeGuard_Rotor_Arm_D_Shaft.stl`):** Internal bore diameter of **$3.35\text{ mm}$** and flat chord depth of **$2.775\text{ mm}$** ($+0.35\text{ mm}$ diametral clearance, $+0.275\text{ mm}$ flat clearance). **Selected for motor installation**: verified via physical bench trial as a secure light interference friction press-fit (firm hand push) that permanently prevents axial "shaft walking" and D-flat backlash chatter during 10 Hz vibration runs.  
   * **Failsafe Model (`VibeGuard_Rotor_Arm_D_Shaft_3p40mm.stl`):** Internal bore diameter of **$3.40\text{ mm}$** and flat chord depth of **$2.825\text{ mm}$** ($+0.40\text{ mm}$ diametral clearance, $+0.325\text{ mm}$ flat clearance). Verified via physical bench trial as a smooth sliding slip-fit; retained as a standby / calibration tool.  
   * **Wall Perimeter Setting (CRITICAL):** Setting $\ge 4$ perimeters guarantees that the plastic between the inner D-bore and the outer 8.5 mm hub is **100% solid concentric filament lines**, eliminating fragile infill boundaries that could crack under motor torque.
2. **First-Layer Squish ("Elephant's Foot") Deburring:**  
   * If bed temperature or z-offset causes slight first-layer flare at the bore entry, **do NOT ream with a large drill bit**.  
   * Hand-rotate a 3.0 mm drill bit or use an X-Acto deburring blade with light circular pressure for 1–2 turns to remove the entry lip only. Preserve the internal flat chord intact.
3. **M3 Unbalance Bolt Mass Recess:**  
   * Center-to-center pitch between D-shaft axis and eccentric mass axis is **$12.00\text{ mm}$** (strictly preserved on both models).  
   * Clearance hole is **$3.20\text{ mm}$** for standard M3 bolt (strictly preserved on both models). The recess captures an M3 bolt head/washer firmly.

### B. FAB-02 ADXL345 Rigid Accelerometer Mount with Enlarged Wire Window
1. **Zero-Support Monolithic Solid with Enlarged Wire Passthrough Window:**  
   * Incorporates an enlarged $21.60\text{ mm wide} \times 10.50\text{ mm high}$ rectangular window ($X \in [-10.8, +10.8]$, $Z = 10.5\text{ to }21.0\text{ mm}$) through the upright wall.
   * This provides full clearance for the $20.32\text{ mm}$ black plastic base of the 8-pin male header soldered on the rear of the ADXL345 PCB (#TJFKQXJUQ) and allows all 8 square female DuPont jumper wire housings ($\approx 20.8\text{ mm}$ total span) to plug directly onto the pins without mechanical collision or binding.
   * A $1.00\text{ mm}$ top tie-bar ($Z = 21.0\text{ to }22.0\text{ mm}$) preserves ring stiffness across the top of the frame and bridges cleanly with 0% supports.
   * **OpenTop Variant (`VibeGuard_ADXL345_Rigid_Mount_OpenTop.stl`):** Also provided in the print pack with the top tie-bar removed ($Z = 10.5\text{ to }22.0\text{ mm}$ open U-channel) for completely unobstructed, drop-in cable routing.
2. **Mounting Hole Alignment:**  
   * **Sensor Upright:** Two horizontal $3.20\text{ mm}$ through-holes spaced **$15.00\text{ mm}$ center-to-center** at $Z = 7.00\text{ mm}$ matching the Robocraze ADXL345 PCB.  
   * **Baseplate Foot:** Two vertical $3.20\text{ mm}$ through-holes spaced **$15.00\text{ mm}$ center-to-center** at $Y = 11.00\text{ mm}$ matching the drilled baseplate acrylic.

### C. FAB-03 Under-Motor Bed Shims
1. **Variants Provided:**
   * `VibeGuard_N20_Motor_Shim_Pad_1mm.stl` ($1.00\text{ mm}$ flat bed)
   * `VibeGuard_N20_Motor_Shim_Pad_1p2mm.stl` ($1.20\text{ mm}$ flat bed)
   * `VibeGuard_N20_Motor_Cradle_Shim_1mm.stl` ($1.00\text{ mm}$ bed with $0.8\text{ mm}$ side guide rails)
2. **Purpose:** Eliminates the measured $1.0\text{ – }1.2\text{ mm}$ under-motor air gap between the N20 motor body and acrylic baseplate when clamped with the white U-bracket.

---

## 3. Pre-Handover Dimensional Inspection Checklist

Before handing over fabricated parts to the student team, the FabLab technician should verify the following 5 criteria:

- [ ] **1. Visual & Topological Integrity:** Monolithic, clean outer skin with zero layer separation, zero delamination, and no stringing inside through-holes or window.
- [ ] **2. D-Shaft Push-Fit (FAB-01):** Rotor arm slides firmly onto a 3.0 mm N20 motor D-shaft by hand. Must seat securely without radial wobble or slipping during manual torque check.
- [ ] **3. Eccentric Pitch (FAB-01):** Center-to-center distance from motor shaft axis to unbalance bolt hole measures $12.0\text{ mm} \pm 0.1\text{ mm}$ via digital vernier caliper.
- [ ] **4. ADXL345 PCB Alignment (FAB-02):** Place a physical ADXL345 breakout board over the vertical upright holes; both M3 bolt holes align without forcing or tilting ($15.0\text{ mm}$ pitch) and the reverse pin header points freely through the rectangular window.
- [ ] **5. Base Flange Flatness (FAB-02 & FAB-03):** Baseplate foot rests 100% planar on a flat surface without corner lift, warping, or rocking.

---
*VibeGuard Engineering Team — Semester Hardware Execution Baseline*
