# Source Extraction

- Chapter: `03` — Portfolio Evolution and Concept Origins
- Authority tier: `TIER_4`
- Manual treatment: `HISTORICAL_SUPPORT`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_TrueMoist_Raw_Research_Gemini.docx`
- SHA-256: `b0eab8009831f5b719bf9d20ad1f25e9bcc549fc260a078a5be2531dc86e5b24`
- Extraction method: `DOCX_XML`
- Rule: source text only; no synthesis, correction or reconciliation.

---

Phase 3C — TrueMoist Engineering Architecture Definition

1. Executive Summary

The engineering architecture analysis for the TrueMoist system has concluded with the definitive selection of a highly feasible, mathematically rigorous, and structurally low-cost prototype architecture. This report establishes a buildable pathway designed explicitly to validate the core hypothesis of edge-based environmental compensation without violating strict academic and financial constraints. The recommended architecture formally adopts an Offline Training with Embedded Inference approach (Architecture D). This methodology utilizes an ESP32-WROOM-32 microcontroller paired with an external ADS1115 sixteen-bit analog-to-digital converter to condition and process signals from a generic V2.0 capacitive soil moisture probe and a DS18B20 waterproof digital temperature sensor. To ensure the project remains firmly within the predefined budget and timeline boundaries while successfully validating the core engineering hypothesis, soil electrical conductivity (representing salinity) will be treated as a rigorously controlled experimental variable during the offline calibration phase rather than relying on live, runtime sensor instrumentation.

The estimated bill of materials for this primary prototype architecture is approximately ₹1,551, securely situating the project well below the preferred ₹3,000 budget constraint and providing a massive safety margin against the absolute ₹5,000 maximum ceiling. By migrating complex multivariate compensation algorithms away from active runtime training and instead utilizing a lightweight pre-trained embedded inference model, the architecture bypasses heavily saturated physical hardware patents, directing all technical innovation strictly toward the algorithmic software layer. Consequently, the system is classified as Architecture Ready, possessing exceptionally high buildability for a five-member student team dominated by computer science and cybersecurity profiles operating under an eight-week academic timeline.

2. Canonical Concept Restatement

TrueMoist represents an affordable, intelligent embedded sensing system engineered specifically to elevate the trustworthiness and operational stability of low-cost soil-moisture measurements. The defining engineering contribution of this system resides entirely apart from the physical acquisition of raw moisture data; rather, its central novelty is the local, edge-computed compensation of predictable measurement errors. These inherent sensing errors are predictably induced by environmental confounders, primarily temperature fluctuations, bulk soil salinity or electrical conductivity variations, inherent physical sensor drift, sensor nonlinearity, and generalized repeatability limitations under controlled environmental variation.1

To strictly bound the scope of the prototype, it is imperative to state what TrueMoist is not. The system is not designed to function as a generic automated irrigation controller, a premium laboratory-grade dielectric instrument, a universal calibration-free probe capable of cross-soil generalization without tuning, a cloud-dependent analytics platform, or a comprehensive precision-agriculture suite.1 The project constraints mandate that all processing—specifically the mathematical compensation of the raw data—must occur locally on the embedded hardware without any required continuous cloud connectivity, ensuring the system remains a frugal innovation suitable for highly constrained smallholder or educational deployments. The physical prototype must be executed by a five-member student team, comprising three technically strong computer science or cybersecurity students, one learner, and one support member, within a maximum two-month timeframe. The physical build must utilize easily sourced, off-the-shelf, or student-fabricated components within a strict budget ceiling of ₹5,000, with an operational preference to remain under ₹3,000.1 Finally, all prototype validation must rely on a rigorous gravimetric reference acting as the physical ground truth, restricted to a single homogeneous soil type to isolate the specific variables of thermal and saline drift.

3. Engineering Hypothesis and Minimum Demonstrable Success

The core engineering hypothesis guiding this architectural definition posits that a low-cost embedded system can utilize supplementary environmental measurements and pre-established empirical calibration data to mathematically compensate for predictable, physics-based error in an inexpensive soil-moisture sensor.1 When deployed under strictly controlled experimental test conditions, this algorithmic compensation strategy will produce volumetric soil moisture estimates that exhibit statistically significantly greater stability and a closer numerical alignment with physical gravimetric reference values than the uncompensated, raw analog sensor output.

Minimum demonstrable success for the TrueMoist prototype is strictly defined by the mechanical and software execution of this specific hypothesis. The selected architecture must support the fabrication of a physical prototype capable of acquiring raw analog voltage data from a low-cost capacitive soil-moisture sensor while simultaneously measuring, or rigorously representing through controlled conditions, the relevant compensation variables—specifically the localized thermal state and the salinity or electrical-conductivity influence. The embedded microcontroller must seamlessly generate both a raw, uncompensated moisture estimate and a locally computed, compensated moisture estimate. Both digital outputs must be quantitatively compared against a rigorous, offline gravimetric ground truth. Ultimately, to achieve validation success, the system must demonstrate a measurable, repeatable reduction in prediction error metrics under deliberately induced environmental disturbance conditions, entirely independent of external cloud processing or remote computational offloading. The prototype is explicitly relieved of the burden of proving universal performance across heterogeneous soil types, varying crop profiles, dynamic seasonal shifts, or uncontrolled field environments.

4. Evidence Base and Source Quality

The technical claims, hardware selections, and mathematical decisions synthesized throughout this report derive from a meticulously structured multi-tiered evidence base characterized by high cross-report convergence and historical project validation. The primary architectural constraints, budgetary ceilings, and foundational concept definitions are drawn directly from the authoritative project documents, notably the Engineering Design Review, the Phase 3C Standard Operating Procedure, and the cumulative Phase 1 through Phase 3 Memory records.1 Insights regarding the underlying physics of low-cost capacitive sensing, specifically the Maxwell-Wagner interfacial polarization effect and the fundamental temperature dependencies of dielectric permittivity, are heavily corroborated by established academic principles governing frequency-domain reflectometry.1

Financial viability and component procurement strategies are strictly grounded in live Indian marketplace distributor data, confirming that the prototype can be built within the fractional limits of the budget constraint.2 The strategic navigation of the intellectual property landscape relies on corroborated findings from Phase 2, which highlighted aggressive utility patent enforcement by incumbent entities, thereby mandating a complete strategic pivot away from custom hardware fabrication toward algorithmic software compensation.1 While the evidentiary base provides ironclad support for the selected hardware and the general efficacy of multivariate regression techniques, the overarching industry claims regarding "universal, cross-soil calibration" remain distinctly unproven in the open literature.1 This evidentiary gap specifically validates the decision to restrict the prototype to a single homogeneous soil type, acting as an essential safeguard against project failure. All interpretations strictly adhere to the project's evidence exclusion rules, rejecting down-weighting in favor of absolute exclusion wherever historical concept drift or model hallucination was observed in prior research passes.1

5. Candidate Architectures

To ensure a comprehensive and scientifically rigorous selection process, four distinct architectural families were synthesized, investigated, and compared to determine the optimal pathway for testing the engineering hypothesis under the rigid two-month timeline and budget constraints.

Architecture A, designated as the Minimal Compensation Demonstrator, represents the simplest mechanically viable baseline. This architecture pairs a generic low-cost capacitive moisture probe with a standard digital temperature sensor, routing the analog signals directly through the internal analog-to-digital converter natively present on the selected microcontroller. Within this framework, soil salinity is maintained strictly as a manually controlled experimental condition rather than a live instrumented variable. The computational compensation relies on static or highly simplified multivariate linear regression, outputting the final data streams via a standard USB serial connection to a host workstation. While this architecture prioritizes extreme cost reduction and rapid physical deployment, it introduces severe engineering risks regarding quantization error due to the notoriously poor linearity of internal microcontroller converters, potentially masking the very sensor drift the project seeks to correct.

Architecture B, designated as the Measurement-Focused Compensated Sensor, dramatically expands the hardware complexity by attempting to dynamically measure soil electrical conductivity directly alongside the capacitance and temperature readings. This architecture necessitates the integration of an external high-precision analog-to-digital converter and relies on complex, real-time multivariate compensation algorithms logged serially or displayed on a local screen. While this approach theoretically offers a richer real-time data tapestry, it introduces severe, potentially project-killing analog front-end complexity. Reliable electrical conductivity measurement in soil requires sophisticated alternating current bipolar pulse excitation circuitry to prevent rapid electrode polarization and destructive electrolysis, presenting an electrical engineering challenge that fundamentally exceeds the capabilities of a computer-science-oriented student team.

Architecture C, designated as the Adaptive Embedded Calibration System, pushes the computational and algorithmic boundaries by implementing adaptive or recursive compensation logic that theoretically recalibrates itself directly on the edge device. It incorporates temperature tracking, external high-resolution analog-to-digital conversion, and dynamic firmware updates to the regression model weights over time as new data is acquired. While conceptually highly innovative, this approach introduces extreme technical risks, including rapid model overfitting, severe computational bottlenecking, and the phenomenon of "catastrophic forgetting," wherein the algorithm overwrites highly valid baseline data due to a short-term environmental anomaly.

Architecture D, designated as Offline Training with Embedded Inference, elegantly isolates the complex mathematical modeling workload from the constrained embedded runtime environment. In this architecture, controlled dataset generation occurs physically through rigorous benchtop testing, but the computationally heavy model training—whether utilizing multivariate polynomial regression or lightweight machine learning—is executed entirely offline on a standard desktop workstation using advanced Python libraries. The resulting optimized mathematical coefficients and model weights are subsequently deployed directly into the microcontroller firmware as a static, pre-trained inference engine. The edge device then performs fully local embedded inference at runtime, strictly satisfying the cloud-independence constraint without risking on-device training failures. This architecture balances advanced, highly accurate mathematical compensation with the absolute reliability required for a constrained academic embedded deployment.

6. Comparative Decision Matrix

The four candidate architectures were systematically evaluated against strict project constraints, the specific computer science team profile, and overall engineering viability to ensure a mathematically defensible selection.

Evaluation Metric

Arch A: Minimal Demonstrator

Arch B: Measurement Focused

Arch C: Adaptive Calibration

Arch D: Offline Inference

Hypothesis Validation Capability

Moderate (Restricted by internal ADC noise)

High (Full parameter instrumentation)

High (Dynamic response capability)

Very High (Clean mathematical isolation)

Accuracy Improvement Potential

Low (Quantization limits correction)

High (Direct EC tracking)

Very High (Self-adjusting weights)

High (Non-linear polynomial mapping)

Estimated Hardware Cost

Lowest (Approx. ₹700)

Highest (Often exceeds ₹5,000)

Moderate (Approx. ₹1,500)

Low (Approx. ₹1,200)

Analog Front-End Complexity

Low (Direct wiring, no AC circuits)

Very High (Requires anti-polarization EC)

High (Adaptive signal conditioning)

Low (External ADC handles conditioning)

Buildability (CS Team Profile)

Very High (Simple C++ scripting)

Low (Requires heavy analog EE skills)

Low (Requires complex edge ML)

Very High (Python to C++ porting)

Validation Clarity and Rigor

High (Simple linear comparisons)

Low (Confounded by live EC noise)

Low (Moving target due to adaptive weights)

Very High (Static deterministic output)

Model Overfitting Risk

Low (Simple linear model)

Moderate (Confounded variables)

Very High (On-device retraining errors)

Low (Offline cross-validation applied)

System Reproducibility

High (Commodity components)

Low (Custom AC excitation required)

Low (State-dependent firmware)

Very High (Deterministic coefficients)

Patent and Innovation Preservation

Low (Trivial implementation)

Moderate (Crowded hardware space)

High (Novel edge retraining)

High (Unique error decomposition workflow)

7. Final Architecture Selection

Based on the exhaustive comparative analysis of the decision matrix, Architecture D (Offline Training with Embedded Inference) is formally selected as the primary engineering architecture for the TrueMoist prototype. This approach aligns perfectly with the designated team profile, which features three technically strong computer science and cybersecurity students who are highly capable of writing robust offline machine learning or regression scripts in Python and subsequently porting the resulting deterministic mathematical coefficients into embedded C++ firmware. By physically separating the model training from the edge device, Architecture D completely mitigates the severe risks associated with on-device model overfitting and computational failure while perfectly satisfying the absolute project requirement for local, cloud-independent runtime compensation.1

Architecture A (Minimal Compensation Demonstrator) is formally designated as the solitary fallback architecture. Should the student team encounter critical, insurmountable failures in integrating the external I2C analog-to-digital converter or managing the embedded inference arrays via C++, Architecture A provides a highly simplified, rapid-retreat pathway. This fallback ensures that the team can still execute a basic validation of temperature-compensated soil moisture readings using the microcontroller's internal peripherals, guaranteeing an academic deliverable. Architectures B and C are rejected outright due to their blatant violation of budget ceilings, the extreme timeline constraints imposed by complex analog front-end design, and the high probability of total project failure during the implementation phase.

8. Final System Block Diagram

The system architecture is explicitly designed to operate in a strictly unidirectional data flow during runtime, rigorously isolating the highly sensitive analog signal acquisition from the digital processing and mathematical compensation logic.

Subsystem Layer

Components and Directed Data Flow

Physical Environmental State

A homogeneous soil matrix subjected to controlled salinity concentrations and precisely manipulated volumetric water content, housed in a geometrically consistent test rig.

Analog Sensing Layer

A Capacitive Moisture Probe V2.0 generating a raw analog voltage, physically co-located with a DS18B20 digital temperature sensor operating on a OneWire protocol.

Signal Conditioning Layer

An ADS1115 16-bit external Analog-to-Digital Converter intercepting the moisture probe voltage and transmitting digitized packets via a stable I2C interface.

Embedded Compute Node

An ESP32-WROOM-32 microcontroller acting as the central processing hub, simultaneously acquiring I2C and OneWire data to execute the pre-loaded local polynomial inference model.

User Interface and Data Output

A high-speed Serial USB transmission protocol yielding timestamped arrays of raw capacitance, temperature, uncompensated volumetric water content, and mathematically compensated volumetric water content.

9. Sensing Subsystem

The physical sensing subsystem is engineered to capture the precise variables necessary to decouple the Maxwell-Wagner interfacial polarization effect from genuine volumetric water content variations, a phenomenon that heavily plagues low-cost sensors.1

The primary moisture acquisition instrument will be a generic, low-cost V2.0 Capacitive Soil Moisture Sensor.2 This ubiquitous module functions by utilizing an onboard 555-timer-based high-frequency oscillator to measure the dielectric permittivity of the surrounding soil matrix, subsequently outputting a continuous analog voltage ranging inversely from approximately 3.0V in completely dry air down to lower voltages in saturated soil.2 The fundamental operating principle relies on the fringing electrical field extending outward from the interdigitated PCB traces into the soil medium. Because these internal copper traces are thoroughly shielded by a waterproof epoxy solder mask, the risk of galvanic corrosion is significantly mitigated compared to traditional bare-metal resistive sensors. However, the raw analog output of this sensor is highly susceptible to localized temperature fluctuations and bulk soil conductivity, primarily because elevated temperatures increase ion mobility within the soil pore water, artificially inflating the apparent dielectric permittivity and falsely indicating an increase in moisture. This specific physical flaw makes it an ideal candidate for testing the algorithmic compensation hypothesis.

Temperature sensing will be achieved by utilizing a DS18B20 waterproof digital thermometer.6 This sensor provides exceptional  accuracy and communicates efficiently via the digital OneWire protocol, requiring only a single digital pin on the microcontroller. Soil temperature will be measured directly adjacent to the capacitive probe to accurately capture the specific thermal state of the exact soil volume interacting with the fringing electric field. Relying on ambient air temperature sensing is explicitly excluded from this architecture, as the high thermal inertia of a wet soil mass dictates that ambient air temperature lags significantly behind actual soil temperature, breaking the temporal correlation necessary to fix the dielectric drift.

The overarching strategy for measuring electrical conductivity represents a critical, defining boundary of this architecture. Direct, live soil electrical conductivity measurement utilizing commercial laboratory-grade analog sensors (such as the DFRobot K=10 model) costs between ₹5,895 and ₹7,860, immediately and catastrophically violating the absolute project budget ceiling.7 Conversely, engineering a low-cost, DIY two-electrode or four-electrode Wenner array probe necessitates the creation of complex alternating current bipolar pulse excitation circuits to prevent rapid electrode polarization, electrolysis, and the buildup of electrochemical double layers.9 Designing, tuning, and debugging this sensitive analog circuitry falls completely outside the capabilities of a two-month, computer-science-focused student team and introduces an unacceptable rate of expected failure. Therefore, the architecture dictates that controlled salt concentration will be utilized strictly as a known experimental variable without any live electrical conductivity instrumentation during runtime. Salinity will act exclusively as an offline calibration variable, allowing the regression model to prove mathematically that compensation is entirely possible when the conductivity state is known, thereby fulfilling the minimum demonstrable success criteria without breaching either the budget limits or timeline constraints.1

10. Analog Front End and ADC Decision

A mathematically rigorous analysis of the system error budget dictates that the inclusion of an external, dedicated analog-to-digital converter is absolutely mandatory for this architecture. The selected component to fulfill this role is the ADS1115 16-bit ADC module, which features an integrated programmable gain amplifier.3

The primary error budget principle dictates that the internal quantization noise and non-linearity of the microcontroller must never dominate the sensor's inherent environmental noise floor. The internal analog-to-digital converters integrated into low-cost microcontrollers, particularly the selected ESP32 platform, are notorious for severe non-linearity, high internal electrical noise coupling from the radio frequency subsystem, and wildly fluctuating internal reference voltages. These flaws frequently yield an effective number of bits (ENOB) of less than 9, despite the nominal 12-bit hardware specification. The V2.0 capacitive sensor outputs a relatively narrow active voltage swing between its completely dry and fully saturated physical states. If the raw analog signal variation representing a single percentage point of volumetric water content falls below or near the quantization step size of the ESP32's internal converter, the sophisticated offline compensation algorithm will mathematically fit itself to random electrical noise rather than the underlying physical phenomena.

The ADS1115 module, highly accessible at approximately ₹118 to ₹145, provides true 16 bits of differential resolution, exceptional internal reference stability, and continuous conversion modes.3 Integrating this module completely eliminates the ADC quantization error from the mathematical error budget, allowing the embedded regression model to operate on a pristine, highly stable digital representation of the sensor's raw analog voltage. The analog front end architecture will utilize basic RC low-pass filtering on the prototyping breadboard, with heavily shielded, shortened jumper cables minimizing parasitic capacitance between the physical sensor head and the conversion module. To guarantee signal integrity, soldered physical connections are highly recommended by the second week of the project timeline to eliminate the unpredictable contact resistance fluctuations inherent to standard solderless breadboards.1

11. MCU and Processing Architecture

The ESP32-WROOM-32 development board is selected as the primary processing platform to drive the TrueMoist architecture.5 The STM32F103C8T6 (commonly known as the Bluepill) is designated as the strict fallback option.4

The selection of the ESP32-WROOM-32 is driven decisively by the advanced computational requirements of the embedded inference engine. The dual-core Tensilica architecture running at 240 MHz, coupled with a dedicated hardware floating-point unit (FPU) and 520 KB of internal SRAM, provides vast computational headroom for executing complex multivariate polynomial regression mathematics in real time without bottlenecking. Furthermore, the expansive flash memory capacity easily accommodates pre-trained inference models, extensive data lookup tables, and the necessary driver libraries for both the ADS1115 and DS18B20 peripherals. The ESP32 natively supports a high-speed USB-to-serial interface, which is critical for the rapid, high-frequency dataset logging required to stream physical data directly to a connected workstation during the calibration phase.

While the STM32F103C8T6 offers an excellent, highly deterministic Cortex-M3 core at a lower price point, it critically lacks an integrated hardware floating-point unit, forcing the compiler into significantly slower software-based floating-point emulation for complex decimal math.4 Given that the specific student team composition leans heavily toward computer science students who are deeply familiar with the C++ Arduino IDE and the broader ESP32 ecosystem, adopting the ESP32 dramatically reduces implementation friction, minimizes firmware configuration time, and ensures that the team spends their limited hours on mathematical modeling rather than debugging low-level hardware abstraction layers.

12. Compensation Algorithm

The core compensation logic driving the true innovation of the TrueMoist system will utilize a specifically tuned multivariate polynomial regression model. This statistical technique offers the absolute optimal balance between high interpretability, strong resistance to model overfitting, and ease of embedded C++ deployment, making it vastly superior for an academic timeline than opaque deep learning models or overly simplistic single-variable linear techniques.

The baseline comparative model will take the form of a first-order multivariate linear regression, serving as the mathematical floor. However, the preferred, operational model will introduce explicit interaction terms and second-order polynomial features to accurately account for the inherently non-linear nature of dielectric temperature dependency. The generalized mathematical formulation estimating the final volumetric water content () is expressed as:

Where  represents the stabilized raw capacitance voltage isolated by the ADS1115,  is the localized soil temperature captured by the DS18B20,  is the controlled salinity state (treated as a known scalar during offline calibration),  represents the highly optimized coefficients calculated offline, and  represents the unmodeled residual error.

The entire model training sequence will be executed completely offline using Python and the scikit-learn statistical library. The resulting optimal  coefficients will be hard-coded into the ESP32 firmware as a highly efficient, static inference function. This explicit methodology completely fulfills the project requirement for local embedded execution without introducing the catastrophic timeline risk of attempting recursive least squares, adaptive filtering, or on-device matrix inversion within the constrained two-month window. Should the standard polynomial regression fail to capture highly complex non-linearities discovered in the physical soil, the optional upgrade path will involve a highly constrained Random Forest regressor deployed via the micromlgen or eloquentarduino TinyML conversion frameworks.

13. Calibration Dataset Design

To rigorously prevent statistical data leakage and ensure robust, interpolative model training, the dataset generation plan must be highly structured and executed with extreme physical discipline. The experiment will utilize a single homogeneous soil type, specifically a standard, finely sifted loamy potting mix, packed consistently into geometrically uniform containers.

The explicit dataset topological design includes:

Moisture Levels: Five discrete, physically controlled levels (Air dry, 15%, 30%, 45%, and complete saturation).

Temperature Levels: Three strictly controlled environmental levels (Ambient ~25°C, Cooled ~15°C, and Heated ~35°C).

Salinity Levels: Three known, distinct conditions (Distilled water baseline, a moderate 2 mS/cm fertilizer solution, and a high salinity 5 mS/cm sodium chloride solution).

Replicate Count: Four independent, physically distinct packings per condition to mathematically average out minute variations in bulk soil density.

Total Expected Samples: A matrix resulting in  independent physical states.

Data leakage will be strictly prevented by employing a grouped split methodology during offline analysis. Repeated, rapid-fire readings from the exact same physical container at a specific moment in time will be aggregated into a single median data point to prevent artificial inflation of the sample size and a false sense of model confidence. The critical train/validation split will be conducted utilizing a leave-one-condition-out (LOCO) cross-validation scheme. This involves holding out an entire temperature or salinity block during the training phase to rigorously assess the model's true interpolative capability on unseen environmental conditions. The capacitive sensor will require a strict minimum of five minutes of physical equilibration time per insertion before any data is authorized to be logged.

14. Gravimetric Ground Truth Procedure

Gravimetric analysis constitutes the absolute, unassailable physical reference for all sensor calibration within this architecture. The primary reference procedure will utilize the industry-standard laboratory oven drying technique to isolate the exact ratio of dry soil mass to water mass.

The rigorous step-by-step methodology is defined as follows:

Tare the mass of a clean, completely dry borosilicate glass or aluminum container on a high-precision scale ().

Extract the specific volume of soil immediately surrounding the capacitive probe's active sensing zone to ensure spatial correlation.

Weigh the wet soil and container together immediately to determine the total wet mass ().

Place the sample in a controlled laboratory oven set precisely at  for a continuous 24-hour period to guarantee the complete evaporation of all free and loosely bound water within the matrix.

Remove the sample, cool in a desiccator, and weigh to determine the final dry mass ().

Calculate the true Gravimetric Water Content () using the standard equation:

If a dedicated  laboratory oven is entirely unavailable to the student team due to facility constraints, a highly calibrated commercial food dehydrator or a repeated low-temperature microwave heating method (heating in short, 1-minute bursts until the mass entirely stabilizes without burning) will serve as the designated fallback. While the microwave method introduces a slightly higher expected error band (approximately  due to the potential combustion of organic matter), it remains highly repeatable, accessible, and scientifically safe for an academic MVP, provided the scale resolution is at least 0.1 grams.

15. Mechanical and Soil-Test Arrangement

The physical test rig must be explicitly designed to minimize mathematical variability introduced by soil heterogeneity, microscopic air gaps at the sensor interface, and inconsistent packing density. The physical arrangement will consist of a rigid, non-conductive PVC cylinder (measuring approximately 15 cm in diameter and 20 cm in depth) to entirely eliminate container wall effects and block external electromagnetic boundary interference from skewing the fringing field.

The physical soil matrix will be mechanically mixed in a separate, much larger container to ensure completely uniform moisture and salinity distribution before being systematically transferred to the PVC test cylinder. Soil compaction will be strictly controlled by applying a standard mass (e.g., a flat 2 kg steel weight) to a rigid compression plate resting on the soil surface for precisely 30 seconds, ensuring a highly repeatable bulk density across all 180 dataset samples.

The capacitive probe will be inserted vertically into the absolute center of the PVC cylinder using a basic 3D-printed or precisely routed wooden alignment jig. This jig ensures the insertion angle remains perfectly perpendicular and the depth profile is perfectly constant across every sample run. The DS18B20 temperature sensor will be inserted into a pre-drilled lateral port on the side of the PVC pipe, placing its metal tip exactly 2 cm away from the planar face of the capacitive probe. This specific geometry guarantees it measures the thermal state of the active sensing volume without introducing metal that interferes with the capacitive fringing electric field.

16. Data Logging and Dataset Schema

Data logging operations will rely entirely on the high-speed USB serial connection streaming directly to a tethered host computer running a simple Python serial capture script or a standard terminal logger. This deliberately avoids the massive firmware complexity of implementing SD-card fat-file systems and SPI bus management on the MCU, keeping the code footprint small and stable.

The raw sampling rate will be set to 10 Hz, with the MCU immediately applying a 50-sample moving average filter in memory to smooth high-frequency jitter. Every 5 seconds, a stabilized composite record will be transmitted via the serial port formatted in a strict comma-separated values (CSV) schema.

The schema will strictly follow this exact column structure to ensure immediate compatibility with pandas dataframes:Sample_ID, Timestamp_ms, Raw_ADC_Value, Temp_C, Salinity_Class, Raw_Uncomp_Moisture, Comp_Moisture_Est, Model_Version, Ground_Truth_Target

During the initial data collection and calibration phase, the Comp_Moisture_Est column will output null values, and the Ground_Truth_Target will contain the manual string identifier correlating to the specific gravimetric test run. During the later runtime validation phase, the MCU will populate the compensated estimate column in real-time, proving the efficacy of the embedded inference engine.

17. Validation Metrics and Success Thresholds

The primary mathematical validation metric will be the Root Mean Square Error (RMSE) calculated between the sensor's embedded estimated moisture content and the physical gravimetric ground truth. The secondary metric will be the Maximum Absolute Error (MAE) observed strictly during extreme temperature disturbance events.

The RMSE formulation is defined as:

The project success threshold is defined in strictly relative terms to completely avoid unsupported, marketing-driven claims of laboratory-grade absolute accuracy. The architecture will achieve a definitive "Pass" condition if the locally computed, mathematically compensated moisture estimate exhibits at least a 30% reduction in RMSE compared to the uncompensated raw sensor output across a severe  temperature disturbance within a fixed, stable moisture state. This threshold realistically and rigorously demonstrates that local environmental compensation materially improves the trustworthiness of the sensor data.1

18. Prototype Test Matrix

The final validation sequence requires the team to execute a rigorous, ten-step test matrix designed to isolate variables and definitively prove the engineering hypothesis.

Test Scenario

Setup and Disturbance

Output Metric

Pass/Fail Rule

1. Baseline Electrical Noise

Fixed soil, ambient temp. Log continuously for 1 hour.

Signal Variance

Variance  of the full analog scale.

2. Internal vs Ext ADC Comparison

Side-by-side read of the exact same probe state using both ADCs.

Noise Floor Width

Ext ADC exhibits  lower noise band.

3. Isolated Thermal Disturbance

Fixed moisture state. Ramp environment temp .

Comparative RMSE

Compensated RMSE is 30% lower than raw RMSE.

4. Salinity Confounding

Fixed moisture state. Swap distilled water matrix for highly saline matrix.

Maximum Absolute Error

Compensated MAE  volumetric shift.

5. Standard Wetting Cycle

Fixed temp/salinity. Incremental physical wetting from dry to saturation.

Coefficient of Determination ()

Compensated  against gravimetric data.

6. Repeated Physical Insertion

Pull and completely re-insert the probe 10 times in identical soil.

Repeatability Deviation

Total deviation  across all physical insertions.

7. Short-term Static Drift

Fixed soil, fixed temp. Log continuously for 24 hours.

Drift Rate

Unexplained drift  over the 24-hour window.

8. Held-out Condition Validation

Test the model on an entirely unseen temperature dataset block.

Generalization RMSE

Held-out RMSE remains within 15% of training RMSE.

9. Live Runtime Inference Speed

Deploy coefficients. Stream USB data and track clock cycles.

Execution Time

Inference mathematics calculate in  ms.

10. Fresh Sample Soil Transfer

Test the finalized model on a new physical batch of identical soil type.

Transfer RMSE

Model generalizes with an absolute RMSE .

The most highly anticipated critical failure mode is expected to be observed in Test 6. Microscopic air gaps induced by physical probe insertion frequently and severely alter the dielectric coupling between the PCB traces and the soil. This leads to artificially low capacitance readings regardless of the sophistication of the mathematical compensation logic. If Test 6 fails, the team must focus intensely on the mechanical alignment jig rather than altering the software algorithm.

19. Electrical and Power Architecture

The power architecture is designed strictly for a tethered, benchtop prototyping environment, rejecting unnecessary mobile complexity. The entire system will be powered continuously via the 5V USB connection from the host computer, utilizing the ESP32 development board's internal low-dropout (LDO) linear regulator to step down and generate the critical 3.3V logic supply for the peripherals.

The analog supply stability is absolutely critical to the error budget. The ADS1115 converter and the V2.0 Capacitive Sensor will both be powered directly from this 3.3V rail. To aggressively mitigate shared-ground voltage ripples and digital switching noise emanating from the ESP32's Wi-Fi antenna (which occurs even when the radio is disabled in firmware), a large  electrolytic capacitor and a fast  ceramic decoupling capacitor will be placed physically as close as possible to the power pins of the ADS1115 and the capacitive probe on the breadboard.

The continuous current consumption of the ESP32 (running in active mathematical mode without Wi-Fi transmission), the generic sensor, and the high-precision ADC is estimated at approximately 60 mA, which is easily and safely sustained by a standard 500 mA USB 2.0 port. Standalone battery operation utilizing a TP4056 charging module and a standard Lithium-Ion cell is deemed entirely unnecessary for the MVP, as it adds zero engineering value to validating the compensation hypothesis while actively introducing falling-voltage anomalies that could severely skew the analog readings as the battery discharges over time.12

20. User Interface and Demonstration

The user interface will adhere to extreme minimalism, deliberately avoiding "gold-plating" the academic prototype with unnecessary visual complexity. The primary interface for data analysis will be the standard Arduino IDE Serial Plotter. This built-in tool provides an immediate, highly visual, multi-axis scrolling graph demonstrating the real-time, undeniable divergence between the raw, drifting uncompensated value and the highly stable, mathematically compensated estimate.

For physical, standalone demonstration purposes during academic presentations or reviews, a low-cost 0.96" I2C OLED display will be integrated into the physical rig.13 The display firmware will cleanly format four distinct lines of real-time data:

Raw Cap: [Voltage]

Temp: [Celsius]

Raw VWC: [%]

Comp VWC: [%]

This specific, highly transparent hardware interface definitively proves to the review board that the embedded microcontroller is calculating the mathematical correction entirely locally, confirming that a tethered PC is not secretly manipulating the data output.

21. Costed BOM

The bill of materials utilizes realistic, current marketplace pricing sourced directly from primary Indian electronics distributors to ensure the project remains firmly within the defined project constraints.1

Component Role

Specific Model

Qty

Unit Price (₹)

Total (₹)

Source / Procurement Risk

Compute / Main MCU

ESP32-WROOM-32 Dev Board

1

373

373

Robu.in / Low

Moisture Sensing

Capacitive Soil Moisture V2.0

2

61

122

ElectronicsComp / Low

Temperature Sensing

DS18B20 Waterproof (1m)

1

249

249

Robu.in / Low

Analog Front End / ADC

ADS1115 16-bit I2C

1

118

118

Robu.in / Low

Display (Optional UI)

0.96" I2C OLED (Blue)

1

209

209

Robu.in / Low

Passive Hardware

Jumper Wires, Decoupling Caps

1

80

80

Assorted Local / Low

Physical Test Rig

PVC Pipe, Plastic Bins

1

150

150

Local Hardware / Low

Contingency Fund

Replacements / Spares

1

250

250

Reserve Allocation

Preferred Total

₹ 1,551

The worst-case financial total, assuming total catastrophic component destruction requiring a complete secondary purchase of every electronic component, peaks at approximately ₹3,100. This scenario remains comfortably under the absolute ₹5,000 project kill threshold. Heavy laboratory equipment such as a digital precision scale and a  laboratory oven are assumed to be standard university inventory available for student use and do not deduct from the prototype hardware budget.

22. Compute, Memory, and Storage Budget

The chosen offline training/embedded inference architecture is highly optimized for resource-constrained embedded environments.1 A multivariate polynomial equation featuring six terms utilizes minimal system resources, leaving massive margins for error.

Flash Usage: The core firmware execution, OneWire protocols, I2C bus management, and OLED display libraries will consume roughly 250 KB of the ESP32's massive 4 MB flash memory (representing an approximate 6% utilization rate). The pre-computed coefficient array requires less than 1 KB of static storage.

RAM Usage: The 50-sample float array required for the moving average filter requires a mere 200 bytes of allocation. The ESP32's 520 KB internal SRAM yields massive, completely safe operational margins, totally avoiding stack overflow risks.

CPU Load: Executing the polynomial equation requires fewer than 20 distinct floating-point operations. Utilizing the ESP32's hardware FPU, the complete model execution time will consistently register under 0.1 milliseconds, completely avoiding any RTOS blocking issues or watchdog timer resets.

23. Risk Register and Kill Factors

A proactive engineering approach mandates strict, continuous awareness of potential physical and software failure modalities, accompanied by predefined kill criteria.

Risk Description

Likelihood

Impact

Mitigation Strategy

Fallback Action

Kill Criterion

Moisture/Salinity Confounding

High

Severe

Control salinity independently in highly discrete batches; strictly do not mix salts during temperature runs.

Reduce prototype scope to Temperature-compensation exclusively.

Outputs remain completely unpredictable across salinity bands.

Sensor Packing Variation

High

Severe

Utilize a fixed-weight physical compaction plate and a rigid vertical alignment jig for every insertion.

Increase replicates aggressively and discard statistical outliers.

Probe readings deviate >20% in the exact same physical soil.

Model Overfitting

Moderate

High

Restrict regression to 1st or 2nd order polynomials; enforce strict LOCO cross-validation mathematically.

Revert to a simple static linear calibration curve.

Held-out validation RMSE doubles the training RMSE.

Gravimetric Error

Low

High

Use a scale with at least 0.1g resolution; strictly enforce the 24hr/105°C baking rule without exception.

Resort to the microwave dehydration method.

Reference physical data directly contradicts known physical reality.

Internal ADC Noise Masking

High

Moderate

Mandate the integration of the ADS1115 early in Week 1 design phase.

Attempt extreme hardware oversampling via the ESP32 logic.

-

Electrical Interference Noise

Moderate

Moderate

Keep analog breadboard traces extremely short; apply 10uF bypass capacitors; solder all critical analog paths.

Apply aggressive software median filtering on the data stream.

Noise floor width entirely masks true sensor variance.

24. Rejected Alternatives

Several highly plausible engineering pathways were rigorously evaluated and explicitly rejected to maintain architectural coherence, timeline safety, and budget discipline.

Direct soil electrical conductivity measurement was the primary rejected alternative. Attempting live electrical conductivity instrumentation with commercial probes (priced ₹5,895 and above) instantly destroys the project budget.7 Furthermore, developing a custom DIY four-electrode Wenner array demands highly complex AC signal generation to prevent severe electrode polarization and double-layer capacitance build-up. Pursuing this shifts the entire project focus from software compensation algorithms to basic analog electrical engineering, introducing a near-certain timeline failure.9

Internal ADC utilization on the ESP32 was entirely rejected based on its profound non-linearity and notoriously poor effective bit resolution. The mathematical evidence firmly dictates that correcting subtle sensor drift requires establishing a highly stable, noiseless baseline; an erratic, drifting internal ADC fundamentally defeats the mathematical error budget.1

Adaptive recalibration using TinyML, which involves training neural networks dynamically on the edge hardware (Architecture C), was decisively rejected. Given the strict two-month timeline, forcing an undergraduate team to debug highly volatile edge-training pipelines risks catastrophic, unrecoverable failure. Offline regression provides identical operational runtime benefits with zero embedded training risk.

Finally, the STM32F103C8T6 (Bluepill) was rejected as the primary MCU in favor of the ESP32. While marginally cheaper, the lack of an integrated FPU and the significantly steeper toolchain learning curve for an Arduino-centric student team introduces unnecessary friction that does not improve the final deliverable.4

25. Patent and Innovation Implications

The selected architecture strictly respects the exhaustive findings of the Phase 2 IP Landscape Report (PDR-045). This foundational decision mandated the total abandonment of any custom hardware probe development due to an aggressively defended, highly saturated utility patent landscape controlled by deep-pocketed industry incumbents like Toro, Meter Group, and Campbell.1 Additionally, the architecture acknowledges the active blocking fence of US Patent 11,598,743.1

Engineering differentiation for this prototype is achieved strictly by transforming a highly flawed, ₹60 capacitive sensor into a highly reliable instrument entirely through mathematical error decomposition, avoiding the legal and mechanical complexity of physical sensor redesign. The semester-project novelty lies distinctly in the disciplined empirical dataset collection methodology and the successful, stable embedded execution of a multivariate thermal and salinity correction model on a sub-₹500 microcontroller. If this project is pursued commercially in the future, patentable claims must completely avoid the physical sensor apparatus. Instead, future intellectual property generation must be framed specifically around the unique sequence of the calibration workflow, the specific error-decomposition mathematical model, and the autonomous logic used to deploy these weights into a constrained memory environment.

26. Team Allocation

The five-member student team is optimally leveraged to execute Architecture D within the rigid eight-week timeframe, preventing single points of failure.1

Member 1 will serve as the Embedded Systems Lead, taking primary responsibility for writing the ESP32 firmware, managing the I2C and OneWire peripheral integration, crafting the ADC sampling routines, and ultimately porting the final Python coefficients into the C++ inference function. Member 2 will operate as the Data and Modeling Lead, responsible for offline dataset curation, managing the LOCO cross-validation execution, authoring the Python scikit-learn modeling scripts, and conducting all statistical error analysis. Member 3 is designated the Hardware and Validation Lead, tasked with physically assembling the PVC test rig, executing the rigorous gravimetric soil baking protocols, managing the induced salinity and temperature disturbances, and soldering the highly sensitive analog front end. Member 4, the Learner, is assigned isolated tasks with low critical-path risk to build confidence, specifically coding the 0.96" OLED display driver, formatting the USB serial CSV strings, and assisting Member 3 with soil sample weighing. Finally, Member 5 will act as Presenter and Support, responsible for comprehensive experiment documentation, strictly tracking the BOM and budget limits, generating the final data visualizations from the serial logs for the academic panel, and supporting overall project management.

27. Eight-Week Roadmap

The project will execute against a tightly bound, sequential schedule to guarantee timely prototype delivery and allow sufficient padding for expected debugging.

During Week 1, the primary focus is Component Verification. The team will source all physical hardware, flash simple blink sketches to verify board health, characterize raw sensor noise, and conclusively validate the mathematical necessity of the ADS1115 to pass the ADC Gate. In Week 2, the team transitions to Rig Construction, finalizing the analog front end by migrating from breadboards to soldered perfboards to ensure signal integrity. The team will also physically construct the PVC soil compaction rig and finalize the gravimetric baking workflow logistics. Week 3 is dedicated to the Pilot Dataset, executing a small-scale trial run of approximately 20 samples to debug the serial logging schema, test the 105°C oven process, and ensure the team coordinates smoothly under live testing conditions.

Week 4 represents the most labor-intensive phase: Calibration Dataset Collection. The team will collect all 180 samples across the full temperature, salinity, and moisture matrix, ensuring strict, unbending adherence to the bulk-density packing protocol. Week 5 shifts entirely to software with Model Development, where Member 2 executes Python scripts against the collected CSV data, compares static linear versus multivariate polynomial models, and isolates the optimal mathematical coefficients. In Week 6, Embedded Deployment occurs, with Member 1 hardcoding the optimal model into the ESP32 and rigorously verifying that the MCU outputs match the offline Python predictions exactly down to the decimal. Week 7 involves Comparative Testing, executing live physical disturbance tests to observe the raw versus compensated real-time output and debug any real-world mathematical anomalies. Finally, Week 8 focuses on Finalization, running the repeat-insertion and fresh-soil transfer tests, finalizing the OLED display UI, and completing the comprehensive academic documentation and presentation materials.

28. Phase 4 Readiness Decision

Decision: Architecture Ready. The TrueMoist architectural plan is highly robust, strictly adheres to all defined boundaries, mitigates all identified patent and hardware risks, and fits the technical profile of the specific academic team perfectly. The deliberate limitation to offline model training and the total exclusion of complex, live-EC analog circuitry ensures that the project remains feasible within two months. The prototype is fully authorized to transition into Phase 4 procurement and physical engineering build phases.

29. Project Decision Register Updates

Following the comprehensive completion of the Phase 3C architecture definition, the Project Decision Register requires the following explicit updates in strict accordance with SOP Section 24 and 28 guidelines 1:

PDR ID

Status

Update Rationale

PDR-031

Accepted

The integration strategy cleanly aligns with earlier IP scoping recommendations.1

PDR-032

Resolved

Complex sensor architecture variables are fully resolved via the definitive selection of external ADC compensation.1

PDR-045

Retained

TrueMoist IP efforts remain strictly confined to the edge-AI algorithmic layer; custom hardware probes remain strictly forbidden due to heavily defended FTO limits.1

PDR-048

Confirmed

Multi-soil validation requirements are formally structured within the validation matrix and future test phases.1

PDR-049

Confirmed

Extended validation gates remain absolutely essential to verifying the specific polynomial coefficients.1

PDR-050

Confirmed

Software compensation boundaries are definitively set; future IP exploration is confirmed strictly within algorithmic pathways.1

30. Phase 3C Memory

JSON

{  "concept": "TrueMoist",  "phase": "3C",  "status": "Architecture Ready",  "final_architecture": "Architecture D - Offline Training / Embedded Inference",  "selected_components": {    "mcu": "ESP32-WROOM-32",    "adc": "ADS1115 16-bit I2C",    "moisture_sensor": "Capacitive Soil Moisture V2.0",    "temp_sensor": "DS18B20 OneWire",    "display": "0.96 inch I2C OLED",    "ec_sensor": "Excluded (Controlled Offline Experimental Variable)"  },  "selected_algorithm": "Multivariate Polynomial Regression",  "calibration_method": "Physical laboratory oven baking (105C) for definitive gravimetric reference",  "validation_method": "RMSE statistical comparison of Raw vs Compensated values against induced thermal/salinity disturbances",  "cost_estimate_inr": 1551,  "risks":,  "unresolved_questions": "Long-term generalizability of specific polynomial coefficients across highly heterogeneous soil types.",  "pdr_changes":}

Works cited

PROJECT_CONCEPT_CONTEXT.md

Capacitive Soil Moisture Sensor V2.0 buy online at Low Price in India, accessed on July 27, 2026, https://www.electronicscomp.com/capacitive-soil-moisture-sensor-v2

ADS1115 16-Bit ADC- 4 Channel with Programmable Gain Amplifier - Robu.in, accessed on July 27, 2026, https://robu.in/product/ads1115-16-bit-adc-4-channel-programmable-gain-amplifier/

Buy WeAct Studio STM32F103C8T6 Bluepill Plus ARM STM32 Minimum System Development Board Module online | Robu.in, accessed on July 27, 2026, https://robu.in/product/weact-studio-stm32f103c8t6-bluepill-plus-arm-stm32-minimum-system-development-board-module/

ESP32-WROOM-32 38Pin Development Board WiFi+Bluetooth Ultra-Low Power Consumption Dual Core - Robu.in, accessed on July 27, 2026, https://robu.in/product/esp32-38pin-development-board-wifibluetooth-ultra-low-power-consumption-dual-core/

Buy Temperature Sensor Modules Online | Accurate Temp Sensors & Probes - Robu.in, accessed on July 27, 2026, https://robu.in/product-category/temperature-sensor-modules/

DFRobot Gravity Lab Grade Analog Electrical Conductivity Sensor / Meter(K=10), accessed on July 27, 2026, https://www.electronicscomp.com/dfrobot-gravity-lab-grade-analog-electrical-conductivity-sensor-meterk10

Buy Now DFRobot Gravity Lab Grade Analog Electrical Conductivity Sensor /Meter V2 (K=1), accessed on July 27, 2026, https://robu.in/product/dfrobot-gravity-lab-grade-analog-electrical-conductivity-sensor-meter-v2-k1/

Development of a Low-Cost Measurement System for Soil Electrical Conductivity and Water Content - ResearchGate, accessed on July 27, 2026, https://www.researchgate.net/publication/396104581_Development_of_a_Low-Cost_Measurement_System_for_Soil_Electrical_Conductivity_and_Water_Content

Audio Amplifier Module - ElectronicsComp.com, accessed on July 27, 2026, https://www.electronicscomp.com/audio-amplifier-module?sort=p.model&order=DESC&page=2

Buy STM32F103C8T6 STMICROELECTRONICS ARM MCU, Motor Control, STM32 Family STM32F1 Series Microcontrollers | Robu.in, accessed on July 27, 2026, https://robu.in/product/stm32f103c8t6-stmicroelectronics-arm-mcu-motor/

TP4056 1A Li-ion lithium Battery Charging Module With Current Protection - Mini USB, accessed on July 27, 2026, https://robu.in/product/tp4056-1a-li-ion-lithium-battery-charging-module-with-current-protection-mini-usb/

0.96" OLED Display Module - SPI/I2C - 128x64 - 7 Pin (Blue) | Robu.in, accessed on July 27, 2026, https://robu.in/product/0-96-oled-display-module/
