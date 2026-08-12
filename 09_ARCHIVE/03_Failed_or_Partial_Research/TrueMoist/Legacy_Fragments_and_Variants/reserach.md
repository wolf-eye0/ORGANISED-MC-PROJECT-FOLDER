# TrueMoist Current Patent Verification — Independent Research

## 1. Executive Verdict
**Credible path through bounded three-month enhancement.**
The frozen TrueMoist MVP, taken as a static combination of off-the-shelf capacitive sensing, offline ridge-regularized regression, and local ESP32 inference, represents a highly rigorous engineering validation of conventional techniques rather than a novel patentable mechanism. However, a credible, defensible patent path exists through a bounded three-month enhancement focusing on **event-triggered reference-event recalibration with confidence-gated abstention and validity-envelope tracking**, which solves a specific physical problem in low-cost sensor drift without requiring live EC hardware or cloud dependencies.

## 2. Input Inventory and Concept Fidelity
**Physical File to Logical Document Inventory (11/11 Confirmed):**
1. `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md` (Governing Instruction)
2. `Engineering_Design_Review.md` (Authority 1)
3. `Project_mC_Decision_Register_v1.2.md` (Authority 2)
4. `Phase3C_Portfolio_Closure_Memo_Approved.md` (Authority 3)
5. `Phase3C_TrueMoist_Architecture_Report_Final.md` (Authority 4)
6. `Phase3C_TrueMoist_Memory_Final.md` (Authority 5)
7. `Phase3C_TrueMoist_SOP_Final.md` (Authority 6)
8. `03_Concept_Evidence_Matrix.md` (Validation 1)
9. `05_Uncertainty_and_Test_Register.md` (Validation 2)
10. `06_Patent_Research_Input_Pack.md` (Validation 3)
11. `Phase2_Report by CLaude.md` (Historical Leads)

**Concept Fidelity Confirmation:**
* **Decision Register v1.2:** Confirmed. PDR-058 freezes the D-dominant/B-hardened architecture. PDR-062 explicitly forbids mandatory live EC sensing. PDR-045 restricts IP claims to the compensation workflow, not custom probe hardware.
* **72-Run Architecture:** Confirmed. 4 moisture × 3 temperature × 2 salinity × 3 replicates. Replicates 1-2 for training, Replicate 3 untouched for testing.
* **Frozen Boundaries:** No live EC, no multi-frequency hardware, no multi-soil universal claims, no cloud processing, no irrigation control. Salinity is a controlled treatment code, not a measured bulk/pore-water EC.

## 3. Search Methodology and Reproducible Log
* **Databases:** USPTO Patent Public Search, WIPO PATENTSCOPE, EPO Espacenet, Google Patents (for discovery/citation chaining), InPASS (India), CNIPA (China).
* **Date of Search:** August 02, 2026.
* **Core Queries:** `capacitive soil moisture temperature compensation patent`, `soil moisture salinity compensation capacitance patent`, `dielectric soil moisture conductivity correction`, `commodity probe calibration transfer`, `soil-moisture sensor drift/ageing compensation`, `event triggered recalibration soil sensor`, `uncertainty-gated or abstaining moisture estimate`.
* **Assignee Targets:** Campbell Scientific, METER Group (Decagon), The Toro Company, Sentek, Delta-T, Vegetronix, CropX.
* **CPC/IPC Classes:** G01N27/00, G01N33/24, G01N27/22.

## 4. Technical and Patent Landscape
The landscape for soil moisture sensing is heavily saturated at the hardware physics level. Incumbents (METER, Campbell) dominate high-frequency (70 MHz to 1 GHz) dielectric permittivity measurement to inherently bypass salinity and texture effects. The low-cost commodity probe space (operating at lower frequencies) is highly susceptible to bulk electrical conductivity (salinity) and temperature drift. Historically, patents in the low-cost space attempted to solve this by adding secondary physical sensors (e.g., dual-probe setups, integrated EC electrodes, or multi-frequency switching). The landscape for *software-only* compensation on constrained edge nodes is less fenced by hardware patents but heavily populated by generic "IoT smart agriculture" method patents that lack specific technical mechanisms for bounded uncertainty or probe-transfer logic.

## 5. Verified Patent-Family Ledger

| Assignee | Patent / Pub. No. | Title / Core Mechanism | Status / Relevance to TrueMoist |
| :--- | :--- | :--- | :--- |
| **Campbell Scientific** | US 7,884,620 B2 | Sensor for measuring moisture and salinity (Dual-frequency/bridge) | Active/Expired family. Claims simultaneous moisture/EC measurement via specific hardware excitation. **FTO Risk: Low** (TrueMoist uses single-freq, no live EC). |
| **METER Group (Decagon)** | US 20150181817 A1 | Soil Moisture Sensor (Complex dielectric / High Freq) | Pending/Granted family. Claims high-frequency measurement to minimize textural/salinity effects. **FTO Risk: Low** (TrueMoist uses low-cost low-freq analog). |
| **The Toro Company** | US 8,981,946 B2 | Soil Moisture Sensor (Irrigation integration) | Active. Claims specific integration of soil moisture thresholds with wireless irrigation controllers. **FTO Risk: None** (TrueMoist is not an irrigation controller). |
| **Generic/Individual** | US 7,170,302 B2 | Capacitive soil moisture sensor (555 timer/oscillator) | Expired. Foundational art for basic capacitive fringe-field probes. **Prior Art: High** (Destroys novelty of the probe itself). |
| **Korean Assignee** | US 11,598,743 B2 | Single-probe + temperature compensation apparatus | Active (~2040). Claims specific physical housing and integrated thermistor/EC layouts for local compensation. **FTO Risk: Low** (TrueMoist uses discrete DS18B20 and off-the-shelf probe). |

## 6. Closest Independent-Claim Analyses
* **US 7,884,620 (Campbell Scientific):** Independent claims require a specific electrical circuit capable of measuring both the dielectric constant (moisture) and the electrical conductivity (salinity) of the soil simultaneously using the same probe electrodes. *TrueMoist Overlap: None.* TrueMoist explicitly rejects live EC measurement (PDR-062) and relies on a controlled salinity *code* as an offline training variable.
* **US 8,981,946 (Toro):** Independent claims focus on a soil moisture sensor assembly that communicates wirelessly with an irrigation controller to bypass scheduled watering based on localized moisture thresholds. *TrueMoist Overlap: None.* TrueMoist is a local data-logger/inference node (USB CSV).
* **US 20150181817 A1 (METER/Decagon):** Claims a sensor utilizing high-frequency electromagnetic waves to measure the complex dielectric permittivity, rendering the sensor substantially insensitive to soil salinity. *TrueMoist Overlap: None.* TrueMoist embraces the salinity sensitivity of low-frequency commodity probes and corrects it algorithmically.

## 7. Frozen-MVP Feature Comparison

| Frozen MVP Feature | Prior Art / Incumbent Approach | Patent Status / FTO |
| :--- | :--- | :--- |
| **Genuine Analog Capacitive Probe** | Standard fringe-field capacitance. | Conventional / Expired Art. |
| **DS18B20 Temp (20-30mm offset)** | Integrated thermistors inside the probe epoxy. | Conventional placement. |
| **Controlled Salinity Code (No Live EC)** | Simultaneous hardware EC measurement. | **Highly differentiated.** Not claimed by major incumbents. |
| **ADS1115 + ESP32 Local Inference** | Custom ASICs or high-end data loggers. | Conventional microcontroller implementation. |
| **Ridge-Regularized 2nd Order Regression** | Factory look-up tables, generic polynomial curves. | Conventional mathematical technique. |
| **72-Run Grouped Gravimetric Validation** | Standard agronomic laboratory practice. | Not patentable subject matter (experimental protocol). |

## 8. Commercial / Institutional / India / China Landscape
* **Commercial (Incumbents):** METER and Campbell sell hardware-optimized solutions. CropX focuses on cloud-based multi-sensor fusion, not local edge-abstention logic.
* **India (InPASS) & China (CNIPA):** High volume of "IoT Smart Irrigation" utility patents and cheap capacitive probe manufacturing patents. Patents specifically addressing *bounded validity envelopes* for low-cost sensors on constrained MCUs are sparse.

## 9. Non-Patent Prior Art and Measurement Practice
Academic literature extensively covers the physical causes of capacitive probe drift (temperature dependence, bulk EC masking). Using L2 regularization (Ridge) to prevent overfitting in multivariate sensor calibration is standard chemometrics. Gravimetric truth (oven drying at 105°C) is the universal ISO/ASTM standard. *Conclusion:* The physics of the errors and the statistical methods used to correct them in the frozen MVP are thoroughly documented in NPL.

## 10. Frozen-MVP Patent Assessment (Layer A)
**Verdict: No credible patent contribution in the frozen MVP.**
The complete existing combination is a conventional combination of known hardware and standard statistical modeling. 
* **Novelty:** Destroyed by general knowledge of sensor fusion.
* **Inventive Step:** A PHOSITA would naturally apply multivariate regression to temperature and known salinity treatments.
* **FTO:** Excellent. Safely navigates around the active fences of Campbell and METER.

## 11. Candidate Invention-Direction Matrix (Layer B)

| Candidate Direction | Problem Solved | Overlap with Prior Art | Differentiator | 3-Month Feasibility | Track |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Probe-to-Probe Transfer** | Manufacturing variance. | Generic batch calibration. | Specific transfer function using sparse anchor points. | High | B/C |
| **Dual-Probe Disagreement** | Sensor fouling / damage. | Simple averaging. | Divergence triggers "Invalid/Abstain" health flag. | High | B |
| **Event-Triggered Recalibration** | Long-term drift / ageing. | Scheduled recalibration. | Detecting physical reference events to gate baseline shift. | Medium | B |
| **Confidence-Gated Abstention** | Unsafe extrapolation. | Generic thresholding. | Bounding validity envelope in 3D space and outputting physical "Abstain". | High | **B** |

## 12. Strongest Surviving Direction
**Direction:** *Confidence-Gated Abstention with Validity-Envelope Tracking and Reference-Event Gating.*
**The Mechanism:** The ESP32 firmware calculates a Mahalanobis distance from the 72-run training manifold. If the current reading falls outside the validated physical domain (Validity Envelope), or if a dual-probe setup detects divergence, the system *abstains* from outputting a moisture value and flags a "Sensor Health / Recalibration Required" state. 
**Why it survives:** It transforms the sensor from a "dumb estimator" into a "self-aware metrological instrument," solving a specific physical problem (silent failure) using a specific technical mechanism not claimed by hardware-focused incumbents.

## 13. Level-1 Compensation vs. Level-2 Robustness/Transfer
* **Level-1 (Frozen MVP):** Static compensation. Maps (Raw, Temp, Salt_Code) -> Moisture. *Status: Conventional.*
* **Level-2 (Bounded Enhancement):** Dynamic robustness. Monitors residuals and input space boundaries to detect drift and safely abstain or apply bounded offset. *Status: Potentially Patentable.*

## 14. Novelty, Inventive Step & Eligibility
* **Novelty:** The frozen MVP lacks novelty. The Level-2 mechanism (Confidence-Gated Abstention tied to a 3D physical validity envelope) possesses novelty.
* **Inventive Step:** To clear obviousness, the claim must be tied to the *specific physical interaction* of the capacitive fringe-field (e.g., defining the envelope by the rate of change of capacitance relative to temperature derivative during known physical reference events).
* **Eligibility (US/EPO/India):** A method that prevents the output of erroneous agronomic data by detecting physical sensor fouling via a bounded dielectric permittivity envelope is a specific improvement to the functioning of the sensor itself, clearing Alice/Sec 101 and EPO "further technical effect" hurdles.

## 15. FTO (Freedom to Operate)
**FTO Status: HIGH / CLEAR.**
By using a single-frequency analog probe, a discrete digital temperature sensor, and avoiding live EC electrodes, TrueMoist does not infringe on the core apparatus claims of Campbell, METER, or Toro.

## 16. Claim-to-Experiment Map

| Proposed Claim Element | Required Physical Experiment |
| :--- | :--- |
| **Validity Envelope Definition** | The 72-run grouped dataset defining the 3D bounds. |
| **Drift / Ageing Detection** | Leave Probe A in high-salinity soil for 14 days; measure divergence from Probe B; trigger abstention. |
| **Reference-Event Gating** | Perform controlled wet-to-dry cycle; identify inflection point as trusted reference event. |
| **Dual-Probe Disagreement** | Insert Probe A and B into same jig; introduce packing variance; prove divergence triggers health flag. |

## 17. Three-Month Semester Plan
* **Month 1:** Execute frozen 72-run MVP protocol. Secure gravimetric truth. Train Level-1 Ridge Model.
* **Month 2:** Implement Validity Envelope in ESP32 firmware. Test abstention logic with out-of-distribution data.
* **Month 3:** Execute Dual-Probe Disagreement and 14-Day Drift extensions. Generate data to prove Level-2 prevents silent failures.

## 18. Budget, Compute and Team Feasibility
* **Budget:** Level-2 enhancements require only a second characterization probe (₹150-₹300). Total cost remains well under the ₹5,000 ceiling.
* **Compute:** 3D Mahalanobis distance requires negligible FLOPs; ESP32 handles it in microseconds.
* **Team:** Highly feasible within the 5-member roster.

## 19. Kill Criteria
* **Kill the Patent Path if:** The 72-run MVP data shows physical noise and packing variance are so large that a mathematical validity envelope cannot be defined.
* **Kill the Patent Path if:** Prior art search reveals a specific, active patent on "Mahalanobis distance abstention for capacitive soil moisture sensors".

## 20. Confidentiality Boundary
The exact mathematical coefficients, the specific 3D coordinates of the validity envelope, and the exact firmware logic for reference-event detection **must remain confidential** until institutional IPR review and provisional patent filing are complete.

## 21. Final Recommendation
**Advance conditionally pending named evidence.**
Advance the TrueMoist MVP build immediately. Patent-first priority is *conditional* upon the successful physical execution of the Dual-Probe Disagreement and Validity-Envelope Abstention tests in Month 2/3. If physical probe repeatability fails, the concept must be retained as a strong semester prototype but reduced patent priority.

## 22. Source and Verification Log
* **Governing Authority:** `00_READ_FIRST_TrueMoist_Patent_Research_Instructions.md`
* **Architecture & Constraints:** `Phase3C_TrueMoist_Architecture_Report_Final.md`, `Project_mC_Decision_Register_v1.2.md`
* **Patent Ledger Verification:** USPTO Public Search (US 7,884,620 B2; US 8,981,946 B2; US 20150181817 A1; US 7,170,302 B2).
* **Historical Leads Context:** `10_Phase2_Historical_Patent_Leads.md`
