# Source Extraction

- Chapter: `02` — Research Methodology and Phase History
- Authority tier: `TIER_4`
- Manual treatment: `HISTORICAL_NARRATIVE`
- Original source: `02_PHASE_HISTORY/Phase_1/Phase_1B5_Portfolio_Optimization/Phase1B5_Portfolio_Optimization_By_Claude.pdf`
- SHA-256: `25130fe434ba2962de3ca241374d9823acced92b088ec6562a77140b80551809`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

Phase 1B.5 — Opportunity Portfolio Optimization
Patent-Oriented Embedded Systems Innovation Pipeline
Board: CTO · IEEE Embedded Systems Researcher · Patent Examiner · VC Partner ·
Industrial Product Architect · Embedded AI Engineer · Cybersecurity Researcher · Systems
Engineer · Innovation Strategist · Engineering Design Review Committee Source of truth:
Phase 1B Opportunity Analysis (32 clusters, structured records, 11-criterion scores) — no
new research performed, no clusters re-derived Objective: Apply hard-constraint gates to
the 32 Phase 1B clusters and decide which deserve to advance into Phase 1C


Method Note
Phase 1B produced eleven soft-weighted scores per cluster and a composite ranking. That
composite answers "how good is this opportunity in general?" Phase 1B.5 asks a different,
harder question: "can this specific team, with this specific budget, in this specific
timeline, actually execute this?" — which is why a cluster can rank highly in Phase 1B and
still fail a gate here, and vice versa.
Gates 1, 2, 3, and 6 are critical (PASS/FAIL) — failure normally eliminates a cluster. Gates 4,
5, 7, and 8 are informational (scored) — they classify quality among survivors but do not
themselves eliminate anything, per the task specification.
Two scoring notes carried over directly from Phase 1B's own eleven-criterion data (to avoid
re-deriving anything):
     Gate 1 (Semester Feasibility) draws on Phase 1B's "Semester Feasibility" score and its
     own explicit prototype-scoping language.
     Gate 2 (Budget) draws on Phase 1B's "Budget Feasibility" score and cost estimate.
     Gate 3 (Embedded Systems Necessity) draws on Phase 1B's "Embedded Systems
     Advantage" score.
     Gate 4 (Patent/Research White Space) draws on Phase 1B's Patent Potential +
     Research Gap scores.

Gates 6, 5, 7, and 8 required fresh judgment against the specific team profile (3
CS/Cybersecurity engineering students; strong in Embedded C/C++, STM32, ESP32,
Raspberry Pi, Linux, networking, cybersecurity, IoT, AI-assisted development, hardware
integration; willing to learn adjacent skills) — this is genuinely new evaluation, not a repeat
of Phase 1B.
A key pattern surfaced repeatedly during Gate 1/2/6 review: several high-value clusters
"fail" only because Phase 1B's own record already flagged that the general/full version of the

opportunity is unrealistic in two months, while a narrowly-scoped version is explicitly
called realistic in that same record (e.g., "a single-leak proof-of-concept is more realistic," "a
narrowly-scoped single-protocol demo is realistic"). Where this pattern held, and the
cluster showed no compensating skill/budget/necessity problem, the board treated it as
exceptional justification rather than an automatic kill — the cluster survives, but only
under an explicit, mandatory scope restriction noted alongside it. Where a cluster failed a
gate and lacked this narrow-scope escape hatch (e.g., it required specialized domain
expertise — biosensor chemistry, advanced applied cryptography research, dedicated ML
research — outside what "willing to learn adjacent skills" can plausibly cover in eight
weeks), no exception was granted.


1. Gate Evaluation Table (All 32 Clusters)
Legend: G1=Semester Feasibility · G2=Budget · G3=Embedded Necessity ·
G4=Patent/White Space (H/M/L) · G5=Demo Impact (1–10) · G6=Technical Capability ·
G7=Learning Return (1–10) · G8=Innovation Density (1–10). P*=Pass with mandatory scope
condition noted.

ID    Cluster (short       Dom G1     G2     G3   G4    G5 G6              G7 G8 Ver
      name)

OC- Offline RPM / Vital-   H   PASS PASS PASS MED       6   P* (use off-   7   6   SUR
01  Sign Monitoring                                         shelf AFE)

OC- Non-Contact Fall       H   P*     P*     PASS HIGH 8    PASS           8   8   SUR
02  Detection

OC- Point-of-Care          H   PASS PASS PASS MED       7   PASS           7   6   SUR
03  Diagnostics

OC- Medication             H   PASS PASS FAIL     LOW   4   PASS           5   3   ELI
04  Adherence

OC- Cold-Chain /           H   PASS PASS PASS HIGH 6        PASS           7   7   SUR
05  Pharma Logistics

OC- Hospital Asset         H   PASS PASS PASS MED       6   PASS           8   7   SUR
06  Tracking + Security

OC- Decoupled              H   FAIL   FAIL   PASS HIGH 6    FAIL           6   6   ELI
07  Continuous Glucose
    Monitor

OC- Assistive              A   P*     P*     PASS HIGH 9    P*             8   8   SUR
08  Communication &
    Mobility

OC- Navigation/Obstacle A      PASS PASS PASS LOW       7   PASS           6   5   SUR
09  Detection (VI)

OC- Vibration-Based        I   PASS PASS PASS MED       7   PASS           8   7   SUR
10  Predictive
    Maintenance

OC- Secure Offline         I   P*     PASS PASS HIGH 6      PASS           9   8   SUR
11  IIoT/OT Anomaly
    Detection

OC- Industrial Process     I   PASS PASS PASS HIGH 6        P* (needs      7   6   SUR
12  Quality Monitoring                                      shop
                                                            access)

ID    Cluster (short       Dom G1     G2   G3   G4    G5 G6          G7 G8 Ver
      name)

OC- Worker Safety          I   PASS PASS PASS MED     6   PASS       7   6   SUR
13  Monitoring

OC- Energy-                I   P*     P*   PASS HIGH 6    P*         7   7   SUR
14  Infrastructure
    Monitoring

OC- Precision Irrigation   E   PASS PASS PASS MED     7   PASS       7   6   SUR
15  & Soil Sensing

OC- Pest/Crop-             E   PASS PASS PASS MED     6   PASS       7   6   SUR
16  Disease/Livestock
    Monitoring

OC- Self-Calibrating       E   PASS PASS PASS MED     6   PASS       7   5   SUR
17  Air/Water Quality

OC- Water-Pipeline Leak E      FAIL   PASS PASS HIGH 7    FAIL       8   8   ELI
18  Detection (DSP)

OC- Climate & Disaster     E   P*     PASS PASS MED   6   PASS       7   6   SUR
19  Early-Warning

OC- Wildlife &             E   PASS PASS PASS LOW     5   PASS       6   5   SUR
20  Biodiversity
    Monitoring

OC- Hardware Root-of-      C   PASS PASS PASS HIGH 7      PASS       9   7   SUR
21  Trust & Secure Boot

OC- Side-Channel           C   P*     P*   PASS HIGH 8    P*         9   9   SUR
22  Attack Defense                                        (equipment
    (PUF/EM)                                              access)

OC- Post-Quantum           C   FAIL   P*   PASS HIGH 5    FAIL       9   7   ELI
23  Cryptography

OC- Smart Parking &        S   PASS PASS FAIL   LOW   4   PASS       4   3   ELI
24  Occupancy Sensing

OC- Pothole/Road           S   PASS PASS PASS MED     7   PASS       7   6   SUR
25  Condition

 ID    Cluster (short      Dom G1        G2     G3      G4     G5 G6             G7 G8 Ver
       name)
       Assessment

 OC- Structural Health     S      PASS PASS PASS MED           6    PASS         7    6    SUR
 26  Monitoring

 OC- HVAC Occupancy /      S      PASS PASS FAIL        LOW    4    PASS         5    4    ELI
 27  Indoor Air Quality

 OC- Asset/Cargo/Tool      L      PASS PASS PASS MED           6    PASS         7    6    SUR
 28  Anti-Theft Tracking

 OC- Retail Inventory      L      PASS PASS FAIL        LOW    4    PASS         4    3    ELI
 29  Automation / ESL

 OC- Battery-Free          X      FAIL   P*     PASS HIGH 6         P*           8    7    ELI
 30  Energy-Harvesting
     Nodes

 OC- Edge-AI Research      X      FAIL   P*     PASS HIGH 6         FAIL         9    9    ELI
 31  Frontier

 OC- Consumer Smart-       X      PASS PASS FAIL        LOW    5    PASS         5    4    ELI
 32  Home Safety
     Sensors


Result: 22 of 32 clusters survive (69%) — 16 with a clean pass on all four critical gates, 6
with a conditional pass requiring a mandatory, explicit scope restriction (marked
SURVIVE* and detailed in Section 3). 10 clusters are eliminated.
(This 69% survival rate is higher than the "typical 40–60%" the task anticipates. Section 3's
closing note addresses this directly rather than silently forcing a lower number.)


2. Eliminated Opportunities — Reasons
Every elimination below is a gate failure with no compensating exceptional circumstance
— either the failure was compounded across multiple gates, or no narrow-scope path
existed to rescue it (unlike the six SURVIVE* clusters in Section 1, where a narrow-scope
path did exist and was used to justify survival).

OC-04 — Medication Adherence & In-Home Care Monitoring
Failed Gate 3 (Embedded Necessity). Phase 1B's own record notes "standalone operation
is useful but not indispensable" — a smartphone-app-based reminder system with a
Bluetooth pill-bottle sensor would solve the actual problem nearly as well. With the lowest
Patent Potential (3) and Research Gap (4) scores of any healthcare cluster, there's no
compensating novelty to justify keeping a project where embedded hardware isn't the load-
bearing element. Eliminated — not because it's a bad idea, but because it isn't an
embedded-systems idea.

OC-07 — Decoupled Continuous Glucose / Metabolic Monitoring
Failed Gate 1, Gate 2, and Gate 6 simultaneously. The compounding is the problem:
Semester Feasibility was already marginal (5/10), Budget Feasibility was under pressure
from sensor front-end sourcing (5/10), and — most decisively — the core technical
challenge is glucose-sensing chemistry/biosensor engineering, a domain outside even an
ambitious "willing to learn" stretch for a CS/Cybersecurity team in eight weeks. Phase 1B
itself flagged the underlying sensing technology as "patent-encumbered." Unlike OC-11 or
OC-22, there is no narrow re-scoping that removes the biosensor-chemistry dependency —
even the decoupled-architecture-only version still needs a working glucose sensor to
demonstrate anything meaningful. Eliminated — genuine domain-expertise mismatch,
not merely a scoping problem.

OC-18 — Water-Pipeline Leak Detection (Acoustic/RF DSP)
Failed Gate 1 and Gate 6. Phase 1B explicitly flagged this as "High difficulty" and noted that
"a full multi-leak localization demo is unrealistic in 2 months." The board considered
whether a narrow single-leak demo (the same rescue pattern used for OC-11/OC-22) could
save it, but the underlying technical bottleneck here is different in kind: it requires
genuinely advanced blind-source-separation/beamforming DSP research (ICA, MUSIC-
like algorithms) that sits outside the team's stated strengths (embedded, networking,
cybersecurity, AI-assisted development) and isn't something a security-focused team
would plausibly pick up competently in the timeframe, even narrowly scoped.
Environment/agriculture is already well-represented among survivors (OC-15, OC-16, OC-
17, OC-19, OC-20), so no diversity argument compensates. Eliminated.

OC-23 — Post-Quantum Cryptography for Resource-Constrained Devices
Failed Gate 1 and Gate 6. This is the single highest research-gap/novelty cluster in the
whole Phase 1B dataset, and the board debated it hardest. But Phase 1B's own language is
unusually direct here: "genuinely challenging to build a credible, working demo in 2 months
without prior cryptography-engineering background," and appropriate only "if the team
has unusually strong applied-cryptography background" — which is a materially deeper
and narrower specialization than general "cybersecurity," and nothing in the team profile

confirms it. Unlike OC-11/OC-22 (where the team's general embedded-security skillset
directly transfers), PQC requires dedicated lattice-cryptography and side-channel-aware
implementation expertise that isn't a scoping problem — it's a background problem.
Eliminated from this semester's portfolio; flagged as a strong candidate for a future
extension or thesis-level follow-on if a team member develops the specific cryptography
background.

OC-24 — Smart Parking & Urban Occupancy Sensing
Failed Gate 3 (Embedded Necessity). "Useful but not indispensable — cameras/other
approaches also viable," per Phase 1B. Combined with the lowest Patent Potential (3),
Research Gap (3), Learning Return (4), and Innovation Density (3) scores of any smart-city
cluster, this is the cleanest possible elimination case: easy, cheap, and technically
unremarkable. Eliminated.

OC-27 — Building Occupancy-Driven HVAC/Lighting & Indoor Air Quality
Failed Gate 3 (Embedded Necessity). Same pattern as OC-24 — "local privacy-preserving
inference is useful but not strictly indispensable." An established, commoditized building-
automation-optimization space with limited technical differentiation (Patent 4, Research
Gap 4). Eliminated.

OC-29 — Retail Inventory Automation & Electronic Shelf Labels
Failed Gate 3 (Embedded Necessity). "The core value is cost/openness, not a unique
embedded capability," per Phase 1B. This cluster also carried the lowest composite score
(5.7) of all 32 clusters in Phase 1B, and nothing in the gate review changes that assessment
— it is simply the weakest opportunity in the dataset on every axis that matters for a patent-
oriented project. Eliminated.

OC-32 — Consumer Smart-Home Predictive Safety Sensors
Failed Gate 3 (Embedded Necessity). "Local fusion is useful but the category is not
fundamentally embedded-dependent," per Phase 1B. Crowded, brand-dominated
consumer market with limited patentable differentiation (Patent 4, Research Gap 4).
Eliminated.

OC-30 — Energy-Autonomous / Battery-Free Wireless Sensor Node Platforms
Failed Gate 1, with a Gate 6 caveat (multi-source energy-harvesting circuit design is
specialized analog power-electronics work, adjacent to but not squarely within the team's
stated strengths). Phase 1B itself already suggested the more useful framing: this may be
"more strategically valuable as a feature integrated into another cluster's prototype... than
as a standalone semester project." The board agrees — eliminated as a standalone cluster,
but explicitly recommended as an optional enhancement to whichever surviving cluster is
ultimately chosen in Phase 1C (most naturally OC-15, OC-19, OC-20, or OC-28, all of which

involve remote/distributed sensor nodes that would benefit from reduced battery-
maintenance burden).

OC-31 — Edge-AI Research Frontier (federated learning, neuromorphic vision,
neurosymbolic AutoML)
Failed Gate 1 and Gate 6. This cluster has the single highest Research Gap (10) and AI
Integration (10) scores in the entire dataset — genuinely the most exciting research
territory here. But Phase 1B's own conclusion is unambiguous: it is "appropriate primarily
for a team explicitly prioritizing publication/patent outcomes over commercial speed,"
which conflicts directly with this team's stated multi-goal profile (patent and research
publication and excellent semester project and startup foundation, with a hard 2-month/
₹3–5k constraint). This is a case where the opportunity is excellent but the fit to this specific
team and constraint set is poor. Eliminated from the semester portfolio; flagged as the
strongest candidate in the entire dataset for a post-semester research extension or a
fourth team member with dedicated ML-research background.


3. Survivor List (22 Clusters)
3.1 Clean Survivors — No Scope Conditions (16 clusters)

 ID      Cluster                                Domain Phase 1B                G4      G7 /
                                                       Composite                       G8

 OC-     Offline RPM / Vital-Sign Monitoring    H         7.5                  MED     7/6
 01

 OC-     Point-of-Care Diagnostics              H         7.3                  MED     7/6
 03

 OC-     Cold-Chain / Pharma Logistics          H         7.4                  HIGH 7 / 7
 05      Monitoring

 OC-     Hospital Asset Tracking + Security     H         6.9                  MED     8/7
 06

 OC-     Navigation/Obstacle Detection (VI)     A         6.7                  LOW     6/5
 09

 OC-     Vibration-Based Predictive             I         8.1                  MED     8/7
 10      Maintenance

 OC-12 Industrial Process Quality Monitoring    I         7.4                  HIGH 7 / 6

 ID      Cluster                                Domain Phase 1B                G4      G7 /
                                                       Composite                       G8

 OC-13 Worker Safety Monitoring                 I          7.0                 MED     7/6

 OC-15 Precision Irrigation & Soil Sensing      E          7.9                 MED     7/6

 OC-     Pest/Crop-Disease/Livestock            E          6.9                 MED     7/6
 16      Monitoring

 OC-17   Self-Calibrating Air/Water Quality     E          7.2                 MED     7/5

 OC-     Wildlife & Biodiversity Monitoring     E          6.2                 LOW     6/5
 20

 OC-21 Hardware Root-of-Trust & Secure Boot     C          8.3                 HIGH 9 / 7

 OC-     Pothole/Road Condition Assessment      S          6.4                 MED     7/6
 25

 OC-     Structural Health Monitoring           S          7.5                 MED     7/6
 26

 OC-     Asset/Cargo/Tool Anti-Theft Tracking   L          6.6                 MED     7/6
 28

(OC-12 carries one logistics caveat, not a gate failure: realistic validation needs physical
access to a welding shop or CNC machine, which the team should confirm before
committing.)

3.2 Conditional Survivors — Mandatory Scope Restriction (6 clusters)
These passed Gate 3 and Gate 6 (core team-skill fit is genuine) but only clear Gate 1 and/or
Gate 2 if the team commits now, at the Phase 1C idea-synthesis stage, to the narrower
version of the opportunity described. This is not a soft suggestion — Phase 1C should not
re-open the broader version of any of these.

ID    Cluster              Domain Composite Mandatory Scope Restriction

OC-   Non-Contact          H       7.6        Use IMU + acoustic sensing as the primary
02    Elderly Fall                            modality; treat mmWave radar as an optional
      Detection                               stretch add-on only if budget allows, not the
                                              core design

OC-   Assistive            A       8.0        Scope to the Braille-display or AAC/sign-
08    Communication &                         language-translation sub-opportunity;
      Mobility Devices                        explicitly exclude the EMG-prosthetic-hand
                                              sub-opportunity, which requires biomedical-
                                              signal and mechanical-actuator expertise
                                              outside the team's profile

OC-   Secure Offline       I       8.2        Scope to one legacy protocol (e.g., Modbus)
11    IIoT/OT Anomaly                         and one anomaly-detection demo; do not
      Detection                               attempt a general-purpose multi-protocol
                                              gateway

OC-   Energy-              I       7.7        Scope to solar-panel micro-crack monitoring
14    Infrastructure                          or battery state-of-health; explicitly exclude
      Monitoring                              the live-power-line TDR anti-theft sub-
                                              opportunity, which carries both an
                                              electrical-safety risk and a specialized-skill
                                              gap

OC-   Climate & Disaster   E       7.3        Scope to a single hazard type and a single
19    Early-Warning                           node (e.g., flood water-level sensor); do not
      Networks                                attempt multi-hazard precursor validation

OC-   Physical & Side-     C       7.8        Scope to one narrow, well-bounded
22    Channel Attack                          demonstration (e.g., PUF key generation
      Defense                                 from SRAM power-up state on an ESP32);
                                              confirm access to basic measurement
                                              equipment (oscilloscope or logic analyzer)
                                              before committing

4. Portfolio Diversity Analysis
Domain Distribution of the 22 Survivors

 Domain                                 Survivors               Count    % of Portfolio

 Healthcare (H)                         OC-01, 03, 05, 06       4        18%

 Assistive Technology (A)               OC-08, 09               2        9%

 Industrial (I)                         OC-10, 11, 12, 13, 14   5        23%

 Agriculture/Environment (E)            OC-15, 16, 17, 19, 20   5        23%

 Cybersecurity-Hardware (C)             OC-21, 22               2        9%

 Smart City/Infrastructure (S)          OC-25, 26               2        9%

 Supply Chain/Logistics (L)             OC-28                   1        4.5%

 Cross-Cutting Enabling Tech (X)        (none)                  0        0%


Is the Portfolio Over-Concentrated?
No single domain dominates. Industrial and Agriculture/Environment tie at 23% each,
Healthcare sits at 18% — no domain exceeds roughly one-quarter of the surviving portfolio.
This is a meaningfully healthier distribution than a naive reading of the raw Phase 1A
source material would suggest (recall the four Deep Research reports individually skewed
heavily toward healthcare and assistive-tech narratives, especially Qwen's report) — the
gate system's Embedded-Necessity filter (Gate 3) did real work here, disproportionately
removing weaker healthcare/consumer clusters (OC-04, OC-07) and smart-city/consumer
clusters (OC-24, OC-27, OC-29, OC-32) rather than industrial or environmental ones, which
naturally rebalanced the portfolio toward domains where embedded hardware is more
clearly load-bearing.
Three domains are thin but not necessarily under-represented: Assistive Technology,
Cybersecurity-Hardware, and Smart City/Infrastructure each carry only 2 survivors. This
looks concerning only if it's read as a raw count. Read qualitatively, it isn't:
      Cybersecurity-Hardware (OC-21, OC-22) — only 2 clusters, but they are ranked #1
      and #6 overall in Phase 1B's composite ranking, carry the two highest Patent
      Potential-adjacent (HIGH/HIGH) classifications, and are the most direct match to the
      team's stated Computer Science/Cybersecurity specialization. This is a case of quality

     concentration, not weakness — it would be a mistake for Phase 1C to "dilute" this
     domain in the name of diversity when it's arguably the team's strongest strategic fit.
     Assistive Technology (OC-08, OC-09) — thin in count, but OC-08 alone carries the
     single highest Patent Potential score (9) in the entire 32-cluster dataset (the Braille-
     actuator sub-opportunity specifically).
     Smart City/Infrastructure (OC-25, OC-26) — genuinely the weaker end of the thin
     group; neither is a standout on novelty or patent potential (both MED), and both are
     present mainly on feasibility/budget/market-size merits rather than differentiation.
One domain (Cross-Cutting Enabling Tech) fully dropped out. This isn't a diversity gap in
the usual sense — OC-30 (energy harvesting) and OC-31 (edge-AI research frontier) were
eliminated for feasibility/skill-fit reasons specific to this team and timeline, not because the
domain itself is weak (OC-31 in particular had the single highest research-gap score in the
dataset). OC-30's harvesting concept remains available as a feature, not a project — see
Section 2.

Diversification Recommendation
No forced diversification is recommended. The natural post-gate distribution is already
reasonably balanced across the three largest domains (Healthcare, Industrial,
Agriculture/Environment), and the "thin" domains are thin for defensible, quality-driven
reasons rather than an artifact of the gate process. The one actionable recommendation is:
Phase 1C should not be shy about weighting Cybersecurity-Hardware (OC-21, OC-22)
heavily despite its low count — with only 2 candidates, it would take very little for this
domain to be crowded out by sheer numerical minority in a naive vote-counting exercise,
when in fact it represents the strongest alignment between team specialization, patent
potential, and Phase 1B's own composite ranking.


5. Final Recommended Opportunity Clusters to Advance into Phase 1C
All 22 survivors are recommended to advance — the gate system already did the
elimination work, and further cutting would risk discarding legitimate options before Phase
1C's idea-synthesis step has had a chance to combine them with specific technology
building blocks. They are organized into two tiers to make the mandatory scope conditions
impossible to miss.

Tier A — Advance Without Reservation (16 clusters)
No scope restrictions beyond ordinary engineering discipline. Ordered by Phase 1B
composite score:
  1. OC-21 — Hardware Root-of-Trust & Secure Boot (8.3)
  2. OC-10 — Vibration-Based Predictive Maintenance (8.1)

 3. OC-15 — Precision Irrigation & Soil Sensing (7.9)
 4. OC-26 — Structural Health Monitoring (7.5)
 5. OC-01 — Offline RPM / Vital-Sign Monitoring (7.5)
 6. OC-05 — Cold-Chain / Pharma Logistics Monitoring (7.4)
 7. OC-12 — Industrial Process Quality Monitoring (7.4)
 8. OC-03 — Point-of-Care Diagnostics (7.3)
 9. OC-17 — Self-Calibrating Air/Water Quality (7.2)
10. OC-13 — Worker Safety Monitoring (7.0)
11. OC-06 — Hospital Asset Tracking + Security (6.9)
12. OC-16 — Pest/Crop-Disease/Livestock Monitoring (6.9)
13. OC-09 — Navigation/Obstacle Detection (VI) (6.7)
14. OC-28 — Asset/Cargo/Tool Anti-Theft Tracking (6.6)
15. OC-25 — Pothole/Road Condition Assessment (6.4)
16. OC-20 — Wildlife & Biodiversity Monitoring (6.2)

Tier B — Advance With Mandatory Scope Narrowing (6 clusters)
High strategic value — three of these (OC-11, OC-08, OC-22) rank in Phase 1B's overall top 6
— but each carries a binding scope restriction from Section 3.2 that Phase 1C must respect,
not revisit:
  1. OC-11 — Secure Offline IIoT/OT Anomaly Detection (8.2) — single protocol, single
     anomaly demo
  2. OC-08 — Assistive Communication & Mobility Devices (8.0) — Braille/AAC/sign-
     language only, not EMG-prosthetic
  3. OC-22 — Physical & Side-Channel Attack Defense (7.8) — single narrow demo,
     confirm equipment access
  4. OC-14 — Energy-Infrastructure Monitoring (7.7) — solar/battery only, not live-line
     TDR
  5. OC-02 — Non-Contact Fall Detection (7.6) — IMU+acoustic primary, radar optional
     stretch only
  6. OC-19 — Climate & Disaster Early-Warning Networks (7.3) — single hazard, single
     node

Board's Closing Observation
If Phase 1C needs to narrow further before generating concepts, the board's collective view
(CTO, VC Partner, Cybersecurity Researcher, and Patent Examiner roles particularly) is
that OC-21, OC-11, OC-10, OC-08, OC-15, and OC-22 represent the six strongest bets by the
combined weight of composite score, patent classification, and team-skill fit — four of

which sit in the team's stated cybersecurity specialization or its immediate adjacency
(embedded security), which is a legitimate factor to weight even though it isn't one of the
eight formal gates. This is offered as a steer, not a further elimination — Phase 1C should
still work from the full 22-cluster survivor list.


Summary
     32 clusters evaluated against 8 gates (4 critical PASS/FAIL, 4 informational scored)
     10 eliminated: OC-04, OC-07, OC-18, OC-23, OC-24, OC-27, OC-29, OC-30, OC-31,
     OC-32
     22 survive (69% — above the anticipated 40–60%, explained by Phase 1B having
     already performed substantial quality filtering before this gate pass ever began): 16
     clean, 6 conditional on explicit scope narrowing
     Portfolio is reasonably diversified across Healthcare, Industrial, and
     Agriculture/Environment (18–23% each); Cybersecurity-Hardware is numerically
     thin (9%) but disproportionately high-quality and should not be diluted in the name
     of raw domain balance
     No new opportunities, products, architectures, or implementations were proposed
     — this document stays strictly within Opportunity Portfolio Optimization, as
     instructed, and hands off 22 evidence-vetted clusters (2 tiers) to Phase 1C.
