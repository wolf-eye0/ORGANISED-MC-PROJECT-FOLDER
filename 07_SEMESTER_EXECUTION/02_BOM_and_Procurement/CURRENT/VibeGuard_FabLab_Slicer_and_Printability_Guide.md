# VibeGuard: 1-Page FabLab Slicer & Printability Guide
**Document ID:** VG-FAB-SLICER-01  
**Project:** VibeGuard — Edge AI Vibration Monitoring & Predictive Maintenance System  
**Target Facility:** College FabLab / 3D Printing Prototyping Center  
**Target Printers:** FDM Systems (Bambu Lab P1S/X1C, Prusa MK3/MK4/MINI+, Creality Ender-3 v2/S1)  
**Materials:** Standard PLA (Preferred, $E \approx 3.5\text{ GPa}$) or PETG | Nozzle: 0.40 mm  

---

## 1. Quick Slicer Parameter Matrix

| Parameter | FAB-01: Eccentric Rotor Cam Arm (`VibeGuard_Rotor_Arm_D_Shaft.stl`) | FAB-02: ADXL345 Rigid Mount (`VibeGuard_ADXL345_Rigid_Mount.stl`) |
|---|---|---|
| **Function** | Rotates at 10 Hz (600 RPM) carrying M3 unbalance bolt | Rigidly couples ADXL345 sensor to wood baseboard |
| **Print Orientation** | **Flat on bottom face ($Z=0$)**; shaft bore vertical | **Flat on bottom foot flange ($Z=0$)**; upright vertical |
| **Support Material** | **NONE (0% supports required)** | **NONE (0% supports required — 45° gussets are self-supporting)** |
| **Layer Height** | **0.16 mm** (recommended for bore resolution) or 0.20 mm | **0.20 mm** (standard draft/structural) |
| **Perimeter Walls** | **Minimum 4 walls** ($\ge 1.6\text{ mm}$ solid perimeter boundary) | **Minimum 4 walls** ($\ge 1.6\text{ mm}$ solid perimeter boundary) |
| **Top / Bottom Layers** | 4 Top / 4 Bottom solid layers | 4 Top / 4 Bottom solid layers |
| **Infill Density** | **80% to 100%** (Rectilinear or Gyroid) | **60% to 80%** (Gyroid or Grid) |
| **Dynamic Rationale** | Prevents centrifugal fatigue and flexing at 10 Hz | Eliminates compliance/damping to transfer vibrations accurately |
| **Brim / Adhesion** | Skirt only (add 3 mm outer brim only if bed adhesion is weak) | Skirt only (large $24 \times 18\text{ mm}$ footprint provides excellent grip) |
| **Est. Print Time** | ~12 to 15 minutes | ~18 to 22 minutes |
| **Filament Used** | ~3.5 grams PLA | ~5.5 grams PLA |

---

## 2. Geometry, Shrinkage Compensation & Slicing Notes

### A. FAB-01 D-Shaft Bore & Dynamic Unbalance Arm
1. **Shaft Fit & Thermal Shrinkage:**  
   * **N20 Motor Shaft:** Nominal 3.00 mm diameter, 2.50 mm flat-to-back, 9.5 mm usable length.  
   * **CAD Sizing with Shrinkage Compensation:** The certified STL incorporates an internal bore diameter of **$3.15\text{ mm}$** and a flat chord depth of **$2.65\text{ mm}$** ($+0.15\text{ mm}$ diametral clearance). This accommodates the radial inward contraction of molten PLA as it solidifies on small inner radii.  
   * **Wall Perimeter Setting (CRITICAL):** Setting $\ge 4$ perimeters guarantees that the plastic between the inner 3.15 mm D-bore and the outer 8.5 mm hub is **100% solid concentric filament lines**, eliminating fragile infill boundaries that could crack under motor torque.
2. **First-Layer Squish ("Elephant's Foot") Deburring:**  
   * If bed temperature or z-offset causes slight first-layer flare at the bore entry, **do NOT ream with a large drill bit**.  
   * Hand-rotate a 3.0 mm drill bit or use an X-Acto deburring blade with light circular pressure for 1–2 turns to remove the entry lip only. Preserve the internal flat chord intact.
3. **M3 Unbalance Bolt Mass Recess:**  
   * Center-to-center pitch between D-shaft axis and eccentric mass axis is **$12.00\text{ mm}$**.  
   * Clearance hole is **$3.20\text{ mm}$** for standard M3 bolt. The hexagonal top recess captures an M3 nut/Nyloc firmly.

### B. FAB-02 ADXL345 Rigid Accelerometer Mount
1. **Zero-Support Monolithic L-Bracket:**  
   * Built with dual $45^\circ$ triangular gussets ($3.0\text{ mm}$ thick) bracing the $3.5\text{ mm}$ upright flange to the $4.0\text{ mm}$ base flange.  
   * Slice with the baseplate foot seated flat on the build plate. The $45^\circ$ gusset slope prints cleanly without overhang drooping.
2. **Mounting Hole Alignment:**  
   * **Sensor Upright:** Two horizontal $3.20\text{ mm}$ through-holes spaced **$15.00\text{ mm}$ center-to-center** matching the Robocraze ADXL345 PCB (#TJFKQXJUQ).  
   * **Baseboard Foot:** Two vertical $3.20\text{ mm}$ countersunk through-holes spaced **$15.00\text{ mm}$ center-to-center** for wood screw anchoring.

---

## 3. Pre-Handover Dimensional Inspection Checklist

Before handing over fabricated parts to the student team, the FabLab technician should verify the following 5 criteria:

- [ ] **1. Visual & Topological Integrity:** Monolithic, clean outer skin with zero layer separation, zero delamination, and no stringing inside through-holes.
- [ ] **2. D-Shaft Push-Fit (FAB-01):** Rotor arm slides firmly onto a 3.0 mm N20 motor D-shaft by hand. Must seat securely without radial wobble or slipping during manual torque check.
- [ ] **3. Eccentric Pitch (FAB-01):** Center-to-center distance from motor shaft axis to unbalance bolt hole measures $12.0\text{ mm} \pm 0.1\text{ mm}$ via digital vernier caliper.
- [ ] **4. ADXL345 PCB Alignment (FAB-02):** Place a physical ADXL345 breakout board over the vertical upright holes; both M3 bolt holes align without forcing or tilting ($15.0\text{ mm}$ pitch).
- [ ] **5. Base Flange Flatness (FAB-02):** Baseplate foot rests 100% planar on a flat surface without corner lift, warping, or rocking.

---
*VibeGuard Engineering Team — Semester Hardware Execution Baseline*
