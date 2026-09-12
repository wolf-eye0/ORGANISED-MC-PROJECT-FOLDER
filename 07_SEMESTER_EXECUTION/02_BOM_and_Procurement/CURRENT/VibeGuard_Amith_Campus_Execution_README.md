# VibeGuard: Amith's Campus Execution & Faculty Requisition Action Guide

**Assigned To:** Amith Krishna Das (Hardware & Fabrication Lead)  
**Project:** VibeGuard — Edge AI Industrial Vibration Monitoring & Fault Diagnosis  
**Institution:** Jyothi Engineering College (Autonomous), Cheruthuruthy, Kerala  
**Target Execution Date:** Today / Immediate Campus Turnaround  
**Available Cash Reserve:** Supported from project fund (Est. total out-of-pocket: ~₹150)  

---

## 1. Quick Mission Briefing

Amith, you have already received the main electronic hardware package (ESP32, motor, sensor, power adapter, and jumpers). Your mission today is to visit **three campus facilities** and pick up **four small hardware items** so our physical test rig can be fully assembled:

```
[STOP 1: FabLab]               [STOP 2: Mech Workshop]          [STOP 3: ECE Lab / ET Store]
- 3D Print Rotor Arm (x2)      - Cut 15x15 cm Wood Baseplate    - MB102 Breadboard
- 3D Print Sensor Mount (x1)   - Drill 2mm pilot holes          - M3 Bolt, Washers, Nyloc Nut
Cost: ~₹50.00                  Cost: ₹0.00 (Scrap Bin)          Cost: ₹0.00 (Lab) or ~₹105 (ET Store)
```

---

## 2. Stop 1: College FabLab (3D Printing & Prototyping)

* **Location:** FabLab / Makerspace (near Innovation & Incubation Center).
* **Whom to Meet:** FabLab Student Coordinator, 3D Printing Operator, or Lab Technician.
* **Exact Files to Give Them (on USB Pen Drive or WhatsApp):**
  1. [`VibeGuard_Rotor_Arm_D_Shaft.stl`](file:///home/paradoxpete/Downloads/VibeGuard_Shareable_Packs/01_College_FabLab_3D_Printing/VibeGuard_Rotor_Arm_D_Shaft.stl) — *The rotating cam arm 3D model.*
  2. [`VibeGuard_ADXL345_Rigid_Mount.stl`](file:///home/paradoxpete/Downloads/VibeGuard_Shareable_Packs/01_College_FabLab_3D_Printing/VibeGuard_ADXL345_Rigid_Mount.stl) — *The sensor bracket 3D model.*
  3. [`VibeGuard_College_FabLab_3D_Printing_Specification.pdf`](file:///home/paradoxpete/Downloads/VibeGuard_Shareable_Packs/01_College_FabLab_3D_Printing/VibeGuard_College_FabLab_3D_Printing_Specification.pdf) — *The official spec sheet with dimensions, infill rules, and billing slip.*

### What to Say to the FabLab Operator (Dialogue Script):
> *"Good morning / Chetta, we are working on our semester microcontroller project, VibeGuard. We have two small 3D parts ready in STL format for our vibration test rig:*  
> *1. **Rotor Cam Arm (print 2 copies):** It needs **80% to 100% infill** in PLA because it spins on a motor shaft at 600 RPM.*  
> *2. **ADXL345 Sensor Bracket (print 1 copy):** Standard **60% infill** in PLA.*  
> *Total weight is only around **12 to 13 grams**, so at the college rate of ₹4/gram, the bill is around **₹50.00**. Here are the STL files and the specification sheet with the billing slip."*

### Key Technical Things to Tell Them:
* **Material:** Standard PLA (Black, Blue, or Grey).
* **Perimeters / Walls:** Minimum **4 wall loops** so the 3.0 mm D-shaft bore is solid plastic.
* **Estimated Print Time:** ~35 to 40 minutes total.

### Acceptance Checklist Before Leaving FabLab:
- [ ] Take your N20 motor shaft from your pocket and push it into the D-bore hole of the printed arm. It should slide on firmly with **no loose wobble**.
- [ ] Ensure the 3.2 mm hole on the outer end is clean and free of plastic burrs.
- [ ] Collect both rotor arms (1 primary + 1 spare) and the sensor bracket.

---

## 3. Stop 2: Mechanical Workshop & Carpentry Section

* **Location:** Mechanical Engineering Workshop (Carpentry & Fitting Hall).
* **Whom to Meet:** Carpentry Instructor / Workshop Superintendent.
* **Exact File to Show / Give (Show on Phone or Print PDF):**
  * [`VibeGuard_College_Mech_Workshop_Baseplate_Requisition.pdf`](file:///home/paradoxpete/Downloads/VibeGuard_Shareable_Packs/02_College_Mech_Workshop_Baseplate/VibeGuard_College_Mech_Workshop_Baseplate_Requisition.pdf)

### What to Say to the Carpentry Instructor (Dialogue Script):
> *"Good morning Sir,*  
> *We are building a machine vibration monitoring testbed for our semester project. We need a small, rigid baseboard from the workshop scrap bin:*  
> *1. Could you help us cut an offcut piece of **plywood or dense hardwood, roughly 15 cm by 15 cm (6 inches square), 10 to 12 mm thick**?*  
> *2. We also have a miniature metal motor bracket. Could you help us drill two small **2.0 mm pilot holes spaced 17 mm apart** so our screws don't split the wood?*  
> *3. Do you have **2 to 4 small self-tapping wood screws (~10 mm length)** to hold the bracket into the wood?*  
> *Here is the layout diagram on my phone, Sir."*

### Key Technical Rule:
* **Why thick plywood?** The baseplate must be **at least 10 mm thick**. If they offer thin 3 mm ply or thin sheet metal, politely ask for thicker plywood offcut. Thin sheets vibrate like a drumhead and ruin sensor data.

### Acceptance Checklist Before Leaving Workshop:
- [ ] The wooden plank rests flat on a table with **zero rocking or wobble**.
- [ ] Place your metal N20 bracket over the drilled pilot holes to verify the 17 mm hole spacing matches.
- [ ] Keep the 4 small wood screws in your pocket.

---

## 4. Stop 3: College ECE Hardware Lab (Breadboard Requisition)

* **Location:** Basic Electronics / Microcontroller Lab.
* **Whom to Meet:** Lab Assistant / Lab in-charge.
* **Mission:** Borrow 1 standard **MB102 830-point solderless breadboard** (saves ₹80).

### What to Say:
> *"Sir / Chetta, for our PBCST504 Microcontroller semester project hardware setup, could you please issue one standard 830-point breadboard from the lab inventory drawer? We will return it safely after our semester final evaluation."*

* **Outcome A:** If they issue the breadboard, you are 100% done on campus!
* **Outcome B:** If lab inventory is locked or unavailable, simply buy it from ET Store in Stop 4 for ₹80.

---

## 5. Stop 4: Local Hardware Store OR ET Store Thrissur

* **Purpose:** Get the unbalance weight bolt, washers, and locknut.
* **Where to Go:** Any local retail nut-and-bolt hardware shop (Cheruthuruthy / Shoranur) **OR** Emerging Technologies (ET Store, Ceeyel Tower near Thrissur Railway Station).

### Exact Shopping List & What to Ask the Shopkeeper:
> *"Chetta / Bhai, I need small metric machine hardware:*  
> *1. One **M3 size, 16 mm or 20 mm bolt** (Star head or Allen key).*  
> *2. Six **M3 flat steel washers** (for weight).*  
> *3. Two **M3 Nyloc nuts** (the locknut with the white nylon plastic ring inside).*  
> *4. *(If breadboard was not obtained at college)*: One **MB102 830-point breadboard**."*

### If Ordering via WhatsApp from ET Store (`+91 9895241319`):
Send them this message:
```text
Hello ET Store, I need to pick up the following items from your Thrissur counter:
1. MB102 830-Point Breadboard (ET8102) - 1 pc (₹80.00)  [Skip if got from college]
2. M3 Lock Nut SS Sunloc (ET6602) - 4 pcs (₹8.24)
3. M3 SS Washers (ET6159) - 10 pcs (₹6.00)
4. M3x16mm Pan Head SS Bolt (ET6134) - 2 pcs (₹2.76)
5. M3x20mm Pan Head SS Bolt (ET6107) - 2 pcs (₹2.90)
Total: ~₹105. Please let me know if ready for pickup. Thank you!
```

---

## 6. What to Say if Faculty Ask Technical Questions (Cheat Sheet)

If a professor or lab instructor asks you about the setup, answer with these exact engineering reasons:

1. **"Why do you need 80%–100% infill for a 3D-printed arm?"**  
   * *Answer:* "The arm carries an eccentric mass spinning at 600 RPM (10 Hz). Standard 15% infill would flex dynamically under centrifugal load, damping the vibration and distorting our FFT frequency harmonics."
2. **"Why 10 mm to 12 mm thick plywood instead of acrylic or metal?"**  
   * *Answer:* "Plywood has high internal damping that suppresses high-frequency acoustic noise and tabletop rattle, while transmitting the low-frequency 10 Hz motor vibration cleanly into the ADXL345 sensor."
3. **"Why use a Nyloc nut instead of a standard nut?"**  
   * *Answer:* "Under continuous 10 Hz vibration, a standard plain nut unthreads and flies off within 30 seconds. The internal nylon ring locks the threads securely without threadlocker glue."
4. **"Why is the motor powered from a separate 12V adapter instead of the ESP32?"**  
   * *Answer:* "Galvanic isolation. The motor induces inductive kickback and brush noise that would crash the ESP32 or trigger brownout resets if grounds were shared."

---

## 7. Master File Directory for Amith's Phone / Pen Drive

All files are neatly arranged on the PC in your `Downloads` folder:
* **All-in-One WhatsApp ZIP:** [`VibeGuard_Complete_Shareable_Pack.zip`](file:///home/paradoxpete/Downloads/VibeGuard_Complete_Shareable_Pack.zip)
* **FabLab Folder:** [`Downloads/VibeGuard_Shareable_Packs/01_College_FabLab_3D_Printing/`](file:///home/paradoxpete/Downloads/VibeGuard_Shareable_Packs/01_College_FabLab_3D_Printing/)
* **Mech Lab Folder:** [`Downloads/VibeGuard_Shareable_Packs/02_College_Mech_Workshop_Baseplate/`](file:///home/paradoxpete/Downloads/VibeGuard_Shareable_Packs/02_College_Mech_Workshop_Baseplate/)
* **Team Manual Folder:** [`Downloads/VibeGuard_Shareable_Packs/03_Team_Assembly_and_Sourcing_Manual/`](file:///home/paradoxpete/Downloads/VibeGuard_Shareable_Packs/03_Team_Assembly_and_Sourcing_Manual/)
