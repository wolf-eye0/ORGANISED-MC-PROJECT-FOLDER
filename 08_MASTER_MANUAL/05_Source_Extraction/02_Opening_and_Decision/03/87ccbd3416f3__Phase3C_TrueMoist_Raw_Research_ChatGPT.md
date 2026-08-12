# Source Extraction

- Chapter: `03` — Portfolio Evolution and Concept Origins
- Authority tier: `TIER_4`
- Manual treatment: `HISTORICAL_SUPPORT`
- Original source: `03_CONCEPT_PORTFOLIO/TrueMoist/06_Historical_Phase3C_Research_and_Prompts/Raw_Engineering_Research/Phase3C_TrueMoist_Raw_Research_ChatGPT.pdf`
- SHA-256: `87ccbd3416f3f7bb58e544095a1e20560f9561ffe72db82f868d17bf942812e7`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

TrueMoist Phase 3C Architecture Research Report
Executive summary
Because the original topic was unspeciﬁed, I am making one explicit assumption: the intended research
target is TrueMoist Phase 3C architecture deﬁnition, not a generic soil-moisture survey. That is the most
plausible reading of the uploaded material, because the active SOP is speciﬁcally titled “Phase 3C —
TrueMoist Engineering Architecture Deﬁnition”, the Engineering Design Review ﬁxes TrueMoist’s mission
and minimum demonstrable success, and the decision register says Phase 3C still needs a single ﬁnal
architecture rather than preserved forks. ﬁleciteturn0ﬁle10 ﬁleciteturn0ﬁle3
ﬁleciteturn0ﬁle12


The strongest conclusion from the project record and the last ﬁve years of literature is that TrueMoist
should not try to invent a new probe ﬁrst. The most defensible MVP is a software-ﬁrst compensation
architecture built around an oﬀ-the-shelf analog capacitive probe, a soil-temperature sensor, an
external ADC, oﬄine-trained but locally executed regression, and controlled salinity as a calibration
variable rather than live in-soil EC sensing. That aligns with the project’s ﬁxed constraints: local
processing, one homogeneous soil for the MVP, explainability, aﬀordability, and physical gravimetric ground
truth. It also matches the project’s Phase 2 guidance to preserve innovation on the algorithmic layer and
avoid custom probe hardware where the patent fence is strongest. ﬁleciteturn0ﬁle10
ﬁleciteturn0ﬁle9 ﬁleciteturn0ﬁle12


My selected architecture is therefore:


ESP32-WROOM-32 + ADS1115 + one low-cost analog capacitive probe + one waterproof DS18B20 +
oﬄine-trained ridge-regularized second-order regression executed locally + USB serial logging +
gravimetric validation at 105 ± 5 °C.


The key strategic choice is to represent salinity rigorously during calibration and disturbance testing
instead of prematurely integrating a direct soil-EC channel into the MVP. That choice is justiﬁed because soil
salinity, pore-water conductivity, and bulk/apparent soil EC are related but not interchangeable; low-
frequency dielectric sensing is itself sensitive to conductivity and temperature; and EC electrodes require AC
excitation to avoid polarization and electrolysis. In other words, a “live soil EC” channel risks becoming a
second sensor-development project before the ﬁrst compensation loop is proven. 1


Recent work supports this direction. A 2024 comparison found that adding an ADS1115 improved the
maximum RMSE of low-cost capacitive sensors from 3.78% to 1.87% v/v in medium-textured soil, while a
2025 ﬁeld study showed that low-cost capacitive sensors can become practically useful after calibration
plus temperature compensation. At the same time, a 2025 low-cost dual-frequency moisture-and-EC
prototype still reported errors above 15% without stronger calibration discipline, which is a useful warning
against assuming that more complex instrumentation automatically removes the calibration burden. 2


                                                      1

On cost, the selected procurement path remains comfortably inside the project envelope. Using Indian
retail listings for currently available development boards and modules, a practical procurement total is
about ₹1,600–₹2,800 if lab oven access is available, and about ₹2,000–₹3,300 if the team must also buy a
0.01 g pocket scale. That keeps the preferred ≤ ₹3,000 target realistic while leaving the ₹5,000 ceiling
intact. ﬁleciteturn0ﬁle10 3


Scope, assumptions, and method
TrueMoist is not supposed to become a generic irrigation controller, a lab-grade universal probe, or a cloud
platform. The project documents deﬁne it much more narrowly: an embedded intelligent sensing system
whose contribution is local compensation of low-cost moisture-sensor error caused by temperature,
salinity/EC inﬂuence, drift, and repeatability limits. The MVP only has to prove that compensated estimates
are more stable or closer to gravimetric reference than uncompensated output under controlled
disturbances; it does not need to prove universality across all soils, crops, or seasons.
ﬁleciteturn0ﬁle10 ﬁleciteturn0ﬁle3


The project’s frozen constraints are unusually clear and matter directly to architecture selection. Phase 3C
demands one coherent buildable architecture, not option preservation. The budget is preferred ≤ ₹3,000,
absolute maximum ₹5,000. The timeline is about two months. Processing must be local with no
continuous cloud dependency. The MVP should use one homogeneous soil type, physical ground truth,
and explainable, reproducible methods. Phase 3B also records that TrueMoist already had the portfolio’s
strongest feasibility consensus, with the only major unresolved hardware issue being whether an external
ADC is necessary. ﬁleciteturn0ﬁle10 ﬁleciteturn0ﬁle12 ﬁleciteturn0ﬁle8
ﬁleciteturn0ﬁle9


I treated the evidence in four layers. First, I treated the project’s uploaded documents as binding
constraints. Second, I used peer-reviewed and primary technical literature from roughly the last ﬁve years
to understand what modern low-cost moisture compensation actually looks like in practice. Third, I used
oﬃcial component documentation from Espressif, TI, Analog Devices, Bosch, DFRobot, and Analog Devices/
Maxim for hardware selection. Fourth, I used Indian retailer listings only for current price-range checking,
not for sensor physics. ﬁleciteturn0ﬁle10 4


  Source class     Main examples                          How it was used

                                                          Fixed constraints, MVP success deﬁnition, allowed
                   EDR, Phase 3B synthesis, Phase
  Project                                                 architecture space. ﬁleciteturn0ﬁle3
                   3C TrueMoist SOP, decision
  authority                                               ﬁleciteturn0ﬁle9 ﬁleciteturn0ﬁle10
                   register
                                                          ﬁleciteturn0ﬁle12

                   2022–2025 papers on
  Peer-
                   temperature compensation,              State of the art, recent developments, algorithm
  reviewed
                   calibration, data assimilation,        and validation implications. 5
  research
                   and low-cost sensor evaluation

  Oﬃcial           Espressif, TI ADS1115, DFRobot
                                                          Hardware capability, interfaces, ADC
  component        SEN0193, DS18B20, ST MCU
                                                          characteristics, memory headroom.      6
  docs             docs


                                                      2

  Source class     Main examples                          How it was used

                   Indian electronics retailers and
  Price checks                                            Current BOM range estimation only.    7
                   lab suppliers


Background and recent developments
The core measurement problem is well understood. Low-cost capacitive moisture sensing is attractive
because it is cheap and scalable, but the reading is not a pure moisture signal. Temperature and dissolved
ions aﬀect the dielectric response, especially at lower frequencies where Maxwell–Wagner polarization
becomes important. That means a cheap sensor can be directionally useful yet still drift or misread when
temperature changes, fertilizer or salts are present, or the same amount of water sits in diﬀerent electrical
conditions. 8


That physics matters because the project’s own Phase 3B synthesis already converged on the same idea:
TrueMoist’s practical confounders are not abstract. The uploaded synthesis explicitly says the converged
architecture is capacitive probe + temperature + EC-informed compensation, that calibration is the
critical path, that gravimetric analysis is the required reference, and that the MVP should stay on one soil
type rather than overclaim transfer. ﬁleciteturn0ﬁle9


The last ﬁve years of literature show a very clear trend: most meaningful progress has come less from
“discovering a magical cheap probe” and more from calibration, compensation, better instrumentation
around the probe, and disciplined validation. A 2022 study demonstrated temperature compensation on
a portable soil-water sensor; a 2023 study emphasized the cost-versus-accuracy tradeoﬀ of low-cost
sensors; a 2024 study showed an inexpensive ADS1115 can materially narrow the gap between low-cost and
higher-end sensors; another 2024 paper showed calibration can be improved strongly with data
assimilation; and a 2025 ﬁeld study showed low-cost capacitive sensors can perform usefully after
calibration and temperature correction. 9


                                                      3

                Recent shift in low-cost soil-moisture sensing

                   2022                  2023               2024                     2025


                                    Large low-cost    ADS1115 materially      Field temperature
          Temperature-compensated    sensor study     improves low-cost         compensation
              portable sensor         emphasizes       sensor RMSE in          brings low-cost
                   shows            calibration and    controlled tests       capacitive sensing
             compensation can        cost-accuracy                            closer to practical
             materially reduce         trade-offs                                irrigation use
                    error                              Data assimilation
                                                      improves low-cost
                                                      sensor calibration         Dual-frequency
                                                         in deployed              moisture+EC
                                                          conditions            prototypes show
                                                                                promise but still
                                                                                     remain
                                                                             calibration-dependent


The implication for TrueMoist is straightforward. The most defendable student-scale contribution is not to
chase universal calibration-free moisture sensing. The decision register already warns that such claims
remain unproven and that true multi-soil validation belongs to a longer, later sprint. For Phase 3C, the
architecture should instead maximize trustworthy local compensation on one homogeneous soil under
controlled disturbances, because that is both technically honest and fully aligned with the project’s ﬁxed
scope. ﬁleciteturn0ﬁle12 ﬁleciteturn0ﬁle10


Architecture analysis and selected design

Architecture family comparison

The TrueMoist SOP deﬁned four candidate architecture families. The right question is not “which sounds
most sophisticated,” but “which family most cleanly proves the hypothesis under the team’s time, budget,
and evidence constraints.” ﬁleciteturn0ﬁle10


                                                                                                     Evidence-based
 Family                   What it does well                                What breaks ﬁrst
                                                                                                     verdict

                                                                           Leaves the weakest
                                                                                                     Keep only as a
 Architecture A           Fastest to build; good as a                      unresolved point—ADC
                                                                                                     Week 1
 minimal                  baseline; controlled salinity                    quality—inside the ﬁnal
                                                                                                     baseline, not as
 compensation             compatible.                                      design. 2024 evidence
                                                                                                     the ﬁnal
 demonstrator             ﬁleciteturn0ﬁle10                             suggests that is an
                                                                                                     architecture.
                                                                           avoidable mistake. 10


                                                              4

                                                                                             Evidence-based
 Family               What it does well                        What breaks ﬁrst
                                                                                             verdict

                                                               Direct soil EC sensing        Use the
 Architecture B                                                adds electrode,               external ADC
                      Stronger measurement path and
 measurement-                                                  polarization, excitation,     idea, but do not
                      better analog discipline with an
 focused                                                       and interpretation            make direct in-
                      external ADC.
 compensated                                                   complexity; bulk EC and       soil EC
                      ﬁleciteturn0ﬁle10
 sensor                                                        pore-water EC are not         mandatory in
                                                               interchangeable. 11           the MVP.

                                                               Over-scoped for a two-
 Architecture C       Closest to the long-term research        month student MVP             Defer to later
 adaptive             vision; compatible with future self-     because it needs more         phases after the
 embedded             calibration work.                        data, drift history, and      ﬁxed-model
 calibration          ﬁleciteturn0ﬁle10                     stronger safeguards           MVP is proven.
                                                               against overﬁtting. 12

                      Best ﬁt to local processing,
                      explainability, modest compute,                                        Selected
 Architecture D                                                Still requires disciplined
                      and student workﬂow. It directly                                       family, with an
 oﬄine training                                                dataset generation and
                      answers the SOP’s requirement                                          external ADC
 with embedded                                                 gravimetric reference.
                      for one coherent build blueprint.                                      and controlled
 inference                                                       13
                      ﬁleciteturn0ﬁle10                                                   salinity variable.
                      ﬁleciteturn0ﬁle12

The competing viewpoints inside the uploaded project record map cleanly onto this table. The majority
Phase 3B view supported a simple capacitive probe plus regression, while the minority view pushed either
an ADS1115 or a full AD5933-class impedance path. The best synthesis is not to average those positions,
but to keep the simple compensation architecture while adopting the cheap external ADC that
neutralizes the minority’s strongest unrebutted concern. That is exactly the kind of one-path resolution
Phase 3C is supposed to produce. ﬁleciteturn0ﬁle9 ﬁleciteturn0ﬁle10 ﬁleciteturn0ﬁle12


Selected architecture

The selected architecture is a D-dominant architecture with B-style signal hardening:


 Design                                                   Rejected
                  Selected choice                                            Why this wins
 element                                                  alternatives

                                                                             Oﬀ-the-shelf, analog-
                                                          Resistive probe
                  One analog capacitive probe,                               accessible, cheap, and
                                                          as primary
                  preferably SEN0193-class or                                consistent with the project’s
 Moisture                                                 sensor; custom
                  equivalent, with a second                                  instruction to stay on
 sensor                                                   probe; direct
                  identical spare/proﬁling unit for                          commodity hardware and keep
                                                          AD5933 probe
                  characterization. 14                                       IP ambition on the software
                                                          front end. 15
                                                                             layer. ﬁleciteturn0ﬁle12


                                                      5

Design                                                Rejected
               Selected choice                                         Why this wins
element                                               alternatives

                                                                       DS18B20 is digital, simple,
                                                                       waterproof, and accurate
                                                      Ambient-only
               Soil temperature near the                               enough for compensation.
Temperature                                           sensing; TMP36
               moisture probe using a                                  Ambient temperature can be
input                                                 analog;
               waterproof DS18B20. 16                                  logged later, but soil
                                                      BME280. 17
                                                                       temperature is the more direct
                                                                       confounder for this MVP. 18

               Controlled salinity as a               Direct in-soil
               calibration/disturbance                two-electrode
               variable, not a mandatory live         EC; water-EC     This satisﬁes the SOP’s
               in-soil sensor channel. If             proxy used       “measure or represent”
Salinity       available, solution EC may be          alone;           requirement while avoiding a
treatment      measured oﬄine during                  destructive      second diﬃcult analog
               preparation, but the runtime           pore-water       subsystem before the core
               architecture must not depend on        extraction in    compensation loop is proven.
               a ﬁeld-robust soil EC subsystem.       routine
               ﬁleciteturn0ﬁle10                   runtime. 11

                                                                       The decision is justiﬁed by
                                                                       error budget, not by “more
                                                                       bits” alone: ESP32 ADC
ADC and
               ADS1115 included by default.           ESP32 internal   variation and nonlinearity are
analog front
                19                                    ADC only. 20     documented, and controlled
end
                                                                       testing shows the ADS1115 can
                                                                       materially improve low-cost
                                                                       sensor RMSE. 21

                                                                       Cheapest board with ample
                                                                       memory, broad library
                                                                       support, and strong alignment
                                                      ESP32-S3;
                                                                       with the project’s shared-
               ESP32-WROOM-32                         STM32F103;
MCU                                                                    platform guidance; once
               development board.    22               STM32F401.
                                                                       ADS1115 is added, the
                                                       23
                                                                       onboard ADC weakness stops
                                                                       dominating selection.
                                                                       ﬁleciteturn0ﬁle12

                                                      Pure linear-     More expressive than a plain
                                                      only model;      linear ﬁt, still interpretable,
               Oﬄine-trained ridge-
                                                      random forest;   trivial to compute locally, and
               regularized second-order
Model                                                 TinyML;          much safer than data-hungry
               regression, deployed as ﬁxed
                                                      recursive/       adaptive methods in a one-soil
               coeﬃcients on the MCU.
                                                      adaptive         two-month MVP.
                                                      calibration.     ﬁleciteturn0ﬁle10 24


                                                  6

  Design                                                                     Rejected
                              Selected choice                                                    Why this wins
  element                                                                    alternatives

                                                                                                 The project prioritizes evidence
                                                                             App, OLED,
  Interface                   USB serial + CSV logging, with                                     collection and interpretability
                                                                             cloud
  and logging                 optional simple status LED only.                                   over interface complexity.
                                                                             dashboard.
                                                                                                 ﬁleciteturn0ﬁle10

                                                                                                 Battery behavior adds nothing
                                                                                                 to the proof of compensation
                                                                                                 and complicates measurement
                              USB 5 V benchtop power,
                                                                             Battery-            hygiene. The SOP explicitly
  Power                       sensors and ADC on the
                                                                             powered MVP.        tells Phase 3C to decide
                              regulated low-voltage rail.
                                                                                                 whether battery operation is
                                                                                                 necessary; here it is not.
                                                                                                 ﬁleciteturn0ﬁle10

The most controversial design choice is the salinity strategy, so it deserves plain language. I am not
recommending that salinity be ignored. I am recommending that it be handled in the only way that is both
rigorous and feasible for the MVP: as a known experimental variable used to create held-out disturbance
conditions and model terms, rather than as a promise of reliable live in-soil EC estimation from a second
improvised sensor. That keeps the architecture faithful to the project’s deﬁnition of TrueMoist without
overextending the prototype into a fresh electrochemistry problem. ﬁleciteturn0ﬁle10 25


The second controversial choice is the rejection of the AD5933 path. The AD5933 is a capable impedance
converter/network analyzer with programmable frequency sweep to 100 kHz and a much richer impedance
workﬂow than a simple ADC path. But that sophistication is exactly why it is the wrong MVP default here: it
adds excitation design, calibration, spectral interpretation, and extra integration work, while recent dual-
frequency literature shows that richer measurement still does not eliminate the need for disciplined
calibration. The right use of the AD5933 is as a later research upgrade if the simpler architecture proves the
hypothesis and the team wants to extend toward deeper salinity/impedance modeling. 26


                                                                  DS18B20 soil temperature


                                                                                                                 Raw moisture estimate


                                      Analog capacitive probe            ADS1115


                                                                                                                 Compensated moisture
                                                                                             ESP32-WROOM-32
                                                                                                                      estimate

                                                                  Known salinity condition
                                                                  from sample preparation


                                                                                                                 USB serial CSV logging


     Offline calibration dataset                                    Store coefficients in
                                       Train regression offline
      + gravimetric reference                                            firmware


                                                                         7

Validation, metrics, and bill of materials

Dataset and gravimetric reference

The MVP should validate against gravimetric water content on a dry-mass basis ﬁrst, not against another
low-cost sensor. Drying soil to constant mass at 105 ± 5 °C is the standard reference method; volumetric
water content can be derived later if bulk density is measured, but gravimetric water content is the cleaner
ﬁrst truth because it does not require introducing a second estimated variable. That is fully consistent with
both the project’s decision register and ISO soil-water standards. ﬁleciteturn0ﬁle12 13


A defensible Phase 3C dataset should be grouped by physical sample preparation, not by rows, because
the SOP correctly warns against apparent accuracy created by repeated readings from the same soil state.
The design below is a realistic compromise between statistical discipline and a two-month student schedule.
ﬁleciteturn0ﬁle10


 Dataset
                     Recommended MVP setting                   Why
 element

                                                               The project docs explicitly prohibit
                     One homogeneous, sieved local
 Soil scope                                                    overclaiming cross-soil generalization in the
                     soil with texture documented once
                                                               MVP. ﬁleciteturn0ﬁle10

                     6 levels across the intended
                     operating band, for example 5%,           Enough structure for nonlinearity without
 Moisture levels
                     10%, 15%, 20%, 25%, 30%                   exploding workload.
                     gravimetric water content

                                                               Satisﬁes same-moisture diﬀerent-salinity
                     3 prepared solution bands, such as
 Salinity levels                                               testing without requiring a live soil-EC
                     fresh / moderate / elevated salinity
                                                               subsystem. ﬁleciteturn0ﬁle10

                     2 controlled soil temperatures for        Keeps workload realistic while still testing
 Temperature
                     the core dataset, with a third            the confounder identiﬁed in the literature.
 levels
                     optional stress level if time remains      18


                     3 independent soil preparations           Separates physical repeatability from
 Replicates
                     per condition                             electronic read noise.

                     10 sequential readings, aggregated
 Reads per                                                     Soil is slow; repeated reads help estimate
                     by median and mean after
 condition                                                     short-term repeatability.
                     stabilization

 Total physical      108 = 6 moisture × 3 salinity × 2         Large enough for a small regression model,
 conditions          temperature × 3 replicates                still feasible in a semester prototype.

                                                               Prevents leakage from repeated reads of
                     Grouped train/validation/test split
 Split strategy                                                the same cup or state.
                     by physical-condition batch
                                                               ﬁleciteturn0ﬁle10


                                                         8

The gravimetric workﬂow should be boring and disciplined. Each soil batch should be mixed thoroughly,
packed to a consistent ﬁll mass and depth, probed using a ﬁxed insertion guide, weighed wet, dried to
constant mass at 105 ± 5 °C, cooled in a desiccator or sealed container, weighed dry, and then linked back to
every electrical record from that batch. If lab oven access is uncertain, a microwave fallback exists in ASTM
practice, but it is explicitly a faster substitute with lower reliability in some soil types, especially where salts
or certain minerals are present. That makes microwave drying acceptable for intermediate checks, but not
the preferred ﬁnal reference for this project. 27


I recommend RMSE versus gravimetric water content as the primary metric, because it is standard in the
recent low-cost sensor literature and penalizes large misses. The secondary metrics should be repeatability
under repeated insertion or repeated read conditions, and disturbance sensitivity reduction, which can
be expressed as the percent error reduction of the compensated estimate versus the raw estimate under
temperature and salinity changes. A practical success target for the MVP is a 20–30% reduction in
grouped-test RMSE, with this report recommending 25% as the internal design target. That target is an
engineering recommendation, not a published standard. It is chosen because the project only needs to
show a meaningful, interpretable improvement over raw output, and recent literature indicates that
materially better low-cost performance is achievable when compensation and instrumentation are handled
carefully. ﬁleciteturn0ﬁle10 28


Error budget, compute, and power

Before empirical characterization, the cleanest qualitative pre-build error budget is this: the biggest likely
uncertainties are soil packing and insertion consistency, gravimetric discipline, probe-to-probe
variability, temperature gradients inside the sample, and then only after that ADC/reference quality.
That ordering matters. It means the ADS1115 is worth including because it removes one avoidable
electronics penalty, but it also means the project will still fail if cups are packed inconsistently, soil
evaporates during handling, or the dataset split leaks repeated states into both training and testing.
ﬁleciteturn0ﬁle9 ﬁleciteturn0ﬁle10 29


The compute budget is very comfortable. ESP32 provides 520 KB SRAM on chip, and common WROOM-
class development boards oﬀer 4 MB ﬂash. A ﬁxed regression model with roughly 8–12 stored coeﬃcients,
a small moving-average buﬀer, and serial logging uses negligible memory and negligible compute by
comparison. This is one reason to prefer a ﬁxed, interpretable regression model over TinyML for the MVP:
the constraint is not compute scarcity, but validation discipline and clarity. 22


The power budget is similarly nonbinding for a benchtop MVP. The ADS1115 is a low-power ADC with typical
power consumption around 0.3 mW, and the DS18B20 was designed for low-component-count digital
temperature sensing. Since the proof target is compensation quality rather than ﬁeld endurance, USB
power is the right architectural choice. It removes batteries, chargers, and brownout analysis from the
critical path and makes analog repeatability easier to debug. 30 ﬁleciteturn0ﬁle10


Bill of materials

The BOM below separates project-essential procurement from institutional equipment. That distinction
matters, because gravimetric truth depends much more on oven access than on any single electronic part.
ﬁleciteturn0ﬁle12


                                                         9

                                                   Current
                                 Suggested
  Item                                               India     Notes
                                   quantity
                                                    range

  ESP32 development                                  ₹399–     Widely available 30-pin and 38-pin dev
                                           1
  board                                               ₹549     boards. 31

                                                     ₹119–
  ADS1115 module                           1                   Cheap enough to include by default.     32
                                                      ₹325

                                                               Low-cost clones are very cheap; branded
  Analog capacitive                              ₹60–₹710      SEN0193-class parts cost more. Two units
                                           2
  moisture probe                                     each      help characterize sensor-to-sensor spread.
                                                                33


  Waterproof DS18B20
                                           1      ₹64–₹72      Soil-temperature input.    34
  probe

  Perfboard, headers,
                                                     ₹150–     Engineering estimate; use soldered ﬁnal
  resistors, capacitors,               1 set
                                                      ₹300     analog path after early characterization.
  jumper wire

  Containers, labels,
                                                     ₹150–
  insertion guide                      1 set                   Engineering estimate.
                                                      ₹300
  materials

  Lab-grade NaCl for                               ~₹342 /
                                     1 pack                    Enough for many prepared conditions.         35
  controlled salinity                                500 g

  Optional 0.01 g scale if                           ₹349–
                                           1                   Only if institutional equipment is missing.       36
  lab scale unavailable                               ₹499

Using the low-cost-to-midrange procurement path, electronics and consumables stay around ₹1,600–₹2,800
before optional scale purchase. Even with a purchased portable scale, the build remains near or under the
preferred budget band, provided the team uses institutional oven access for ﬁnal gravimetric validation.
 37


Implications, gaps, and prioritized recommendations
The practical implication of this architecture is that it gives TrueMoist a clean, honest claim: not “universal,
calibration-free soil sensing,” but demonstrable error reduction from local compensation on
constrained hardware. That is exactly the right level of ambition for the semester prototype. It also
preserves the project’s longer-term innovation path, because the decision register already directs TrueMoist
away from custom hardware IP and toward the algorithmic/software layer. The ﬁrst MVP should therefore
be judged by trustworthiness improvement, not by novelty theater. ﬁleciteturn0ﬁle12
ﬁleciteturn0ﬁle10


There are still real gaps. This architecture does not prove multi-soil generalization, long-term self-
recalibration, or robust live in-soil EC estimation. The decision register rightly keeps those as later validation
problems, and the literature supports that caution: multi-soil or calibration-free claims remain much harder


                                                       10

than single-soil compensated sensing. Likewise, the selected model may be technically successful while still
not being patentable on its own; the SOP is explicit that ordinary polynomial regression on commodity
sensors must not be mistaken for IP. ﬁleciteturn0ﬁle12 ﬁleciteturn0ﬁle10 38


The highest-risk open question is not actually the regression model. It is experimental discipline. If soil
packing varies, if evaporation is not controlled, if the probe is inserted at inconsistent depth or angle, or if
the ground-truth pipeline is sloppy, the project can still produce attractive graphs and weak evidence. That
is why the architecture should be implemented with a simple ﬁxed insertion jig, a written sample-prep SOP,
grouped data splits, and a rule that every test record remains traceable to one physical batch ID and one
gravimetric measurement pair. ﬁleciteturn0ﬁle10 39


The prioritized next steps are therefore:


  Priority    Action                                         Why it must happen ﬁrst

              Characterize one probe on ESP32                This closes the only major unresolved
  Highest     internal ADC versus ADS1115 in Week            instrumentation dispute quickly and cheaply.
              1                                              ﬁleciteturn0ﬁle9 10

              Freeze the gravimetric SOP and                 True ground truth and repeatable packing
  High        physical sample-prep SOP before                matter more than model sophistication.
              collecting the main dataset                    ﬁleciteturn0ﬁle12 13

              Collect grouped data on one soil               This is the minimum evidence needed to prove
  High        across moisture, temperature, and              the compensation hypothesis honestly.
              salinity conditions                            ﬁleciteturn0ﬁle10

              Fit and compare three models only:             Keeps the model comparison interpretable and
  Medium      raw baseline, linear regression, ridge-        prevents over-scoping into novelty ML.
              regularized second-order regression            ﬁleciteturn0ﬁle10

              Deploy only the winning ﬁxed model             Local inference is the point of the concept;
  Medium      to the MCU and validate it on held-out         held-out physical batches are the real test.
              physical batches                               ﬁleciteturn0ﬁle10

              Treat live EC sensing, adaptive                These are valid next steps, but they are not
  Later       recalibration, and multi-soil transfer         required to prove the Phase 3C hypothesis.
              as post-MVP research extensions                ﬁleciteturn0ﬁle12 40

The ﬁnal recommendation is therefore unambiguous: build TrueMoist as a one-soil, local-inference,
ADS1115-backed capacitive compensation prototype using soil temperature and controlled salinity
conditions, validate it gravimetrically, and judge success by grouped-test error reduction over the
raw sensor. That architecture is the best match to the uploaded project constraints, the best synthesis of
the competing internal viewpoints, and the most evidence-backed way to produce a credible semester-scale
demonstration. ﬁleciteturn0ﬁle10 ﬁleciteturn0ﬁle9 41


                                                       11

 1 11 25 Salinity: Electrical conductivity and total dissolved solids - Corwin - 2020 - Soil Science Society of

America Journal - Wiley Online Library
https://acsess.onlinelibrary.wiley.com/doi/abs/10.1002/saj2.20154?utm_source=chatgpt.com

 2   10   28   29Assessment of Low-Cost and Higher-End Soil Moisture Sensors across Various Moisture
                    41

Ranges and Soil Textures
https://www.mdpi.com/1424-8220/24/18/5886?utm_source=chatgpt.com

 3    7   ESP32 Development Board CP2102 30 PIN | KSP Electronics
https://kspelectronics.in/product/esp32-development-board-cp2102-30-pin/?utm_source=chatgpt.com

 4    5   18   Calibration and Temperature Compensation of a Low-Cost Capacitive Soil Moisture Sensor for
               24

Precision Irrigation in Thailand | Engineering, Technology & Applied Science Research
https://etasr.com/index.php/ETASR/article/view/9677?utm_source=chatgpt.com

 6   20   21   Analog to Digital Converter (ADC) - ESP32 - — ESP-IDF Programming Guide latest documentation
https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc.html?utm_source=chatgpt.com

 8 Eﬀects of Maxwell‐Wagner polarization on soil complex dielectric permittivity under variable
temperature and electrical conductivity - Chen - 2006 - Water Resources Research - Wiley Online Library
https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005WR004590?utm_source=chatgpt.com

 9 A Novel Portable Soil Water Sensor Based on Temperature Compensation - Tian - 2022 - Journal of
Sensors - Wiley Online Library
https://onlinelibrary.wiley.com/doi/10.1155/2022/1061569?utm_source=chatgpt.com

12   38   40   Improving the Calibration of Low-Cost Sensors Using Data Assimilation | MDPI
https://www.mdpi.com/1424-8220/24/23/7846?utm_source=chatgpt.com

13   27   39   ISO 11465:1993 - Soil dry matter & water (gravimetric)
https://standards.iteh.ai/catalog/standards/iso/8f91301d-8ﬀ6-4745-a884-3c8aac5c8ac9/iso-11465-1993?utm_source=chatgpt.com

14   Gravity: Corrosion-Resistant Capacitive Soil Moisture Sensor for Arduino & Raspberry Pi | DFRobot Wiki
https://wiki.dfrobot.com/sen0193/?utm_source=chatgpt.com

15   26   AD5933 Datasheet and Product Info | Analog Devices
https://www.analog.com/en/products/ad5933.html?utm_source=chatgpt.com

16   DS18B20 Datasheet and Product Info | Analog Devices
https://www.analog.com/en/products/DS18B20.html?utm_source=chatgpt.com

17   TMP36 Datasheet and Product Info | Analog Devices
https://www.analog.com/en/products/tmp36.html?utm_source=chatgpt.com

19   30   ADS1115 data sheet, product information and support | TI.com
https://www.ti.com/product/ADS1115?utm_source=chatgpt.com

22   ESP32 Datasheet
https://documentation.espressif.com/esp32_datasheet_en.html?utm_source=chatgpt.com

23   ESP32-S3-WROOM-2 Datasheet
https://documentation.espressif.com/esp32-s3-wroom-2_datasheet_en.html?utm_source=chatgpt.com

31   37   Buy ESP32 WiFi Bluetooth Development Board 30 Pin Dual Core ESP32 Module | Techtonics
https://techtonics.in/product/espressif-esp32-development-board-with-wiﬁ-and-bluetooth/?utm_source=chatgpt.com


                                                             12

32   Buy AD1115 Module Online in India | Robocraze
https://robocraze.com/products/16-bit-i2c-4-channel-ads1115-module?utm_source=chatgpt.com

33   Capacitive SOIL MOISTURE SENSOR - Iotwebplanet.com
https://iotwebplanet.com/product/capacitive-soil-moisture-sensor/?utm_source=chatgpt.com

34 DS18B20 Water Proof Temperature Sensor Probe - Robo Bazar | Online Electronics Components Store in
India - Quality Electronic Components Shop
https://robobazar.in/product/ds18b20-water-proof-temperature-sensor-probe/?utm_source=chatgpt.com

35   Sodium Chloride ER (500 Grams)
https://labwale.co/product/sodium-chloride-er-500-grams/?utm_source=chatgpt.com

36   Digital Pocket Scale 200 gm * 0.01 Readability Weighing Scale – Shop Zero 1
https://shopzero1.in/products/digital-pocket-scale-200-gm-0-01-readability-weighing-scale?utm_source=chatgpt.com


                                                            13
