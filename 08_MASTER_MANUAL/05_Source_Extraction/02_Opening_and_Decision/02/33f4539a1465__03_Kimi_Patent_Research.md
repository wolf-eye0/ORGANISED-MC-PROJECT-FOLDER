# Source Extraction

- Chapter: `02` — Research Methodology and Phase History
- Authority tier: `TIER_4`
- Manual treatment: `HISTORICAL_SUPPORT`
- Original source: `02_PHASE_HISTORY/Phase_2_Patent_Landscape/Raw_Research/03_Kimi_Patent_Research.pdf`
- SHA-256: `33f4539a14653b55c0b73e0fbcd140827e2131ed9c3ca5d9bc896d4553f4a904`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Rule: source text only; no synthesis, correction or reconciliation.

---

MC PROJECT               ·   I N N O VAT I O N P I P E L I N E          ·   PHASE 2


Patent Landscape Analysis
Prior-art, white-space and portfolio assessment of five embedded-systems
concepts:
OpenBraille · VibeGuard · TrueMoist · TrustLatch · ColdTrace


Prepared for the Engineering R&D Decision Board
Evidence base: 121 indexed sources · USPTO full-text records · peer-reviewed and program literature
As of 17 July 2026 · Final for board review · Not legal advice / not an FTO opinion

Contents

   Executive Summary                                                  4
   Method & Evidence Conventions                                      5

1. OpenBraille — Low-Cost Refreshable Braille Display Module          6
   1.1 Problem Summary                                                6
   1.2 Commercial Ecosystem Scan                                      6
   1.3 Patent & Prior-Art Landscape                                   6
   1.4 Technical Prior-Art and Feasibility                            7
   1.5 White-Space Assessment                                         7
   1.6 Competitive & Defensibility Analysis                           8
   1.7 Regulatory / Standards Context                                 8
   1.8 Risk Matrix                                                    8
   1.9 Recommended Next Step                                          9
   1.10 Key Patent & Prior-Art Table                                  9
   1.11 Commercial Landscape Table                                   10
   1.12 Confidence Score & Evidence Gaps                             10
2. VibeGuard — Spatially-Isolated Bearing Fault Early-Warning Node   11
   2.1 Problem Summary                                               11
   2.2 Commercial Ecosystem Scan                                     11
   2.3 Patent & Prior-Art Landscape                                  11
   2.4 Technical Prior-Art and Feasibility                           12
   2.5 White-Space Assessment                                        12
   2.6 Competitive & Defensibility Analysis                          12
   2.7 Regulatory / Standards Context                                13
   2.8 Risk Matrix                                                   13
   2.9 Recommended Next Step                                         13
   2.10 Key Patent & Prior-Art Table                                 14
   2.11 Commercial Landscape Table                                   14
   2.12 Confidence Score & Evidence Gaps                             15

3. TrueMoist — Drift-Self-Correcting Soil Moisture Controller        16
   3.1 Problem Summary                                               16
   3.2 Commercial Ecosystem Scan                                     16
   3.3 Patent & Prior-Art Landscape                                  16
   3.4 Technical Prior-Art and Feasibility                           17
   3.5 White-Space Assessment                                        17
   3.6 Competitive & Defensibility Analysis                          17
   3.7 Regulatory / Standards Context                                18

   3.8 Risk Matrix                                                                 18
   3.9 Recommended Next Step                                                       18
   3.10 Key Patent & Prior-Art Table                                               19
   3.11 Commercial Landscape Table                                                 19
   3.12 Confidence Score & Evidence Gaps                                           19
4. TrustLatch — Accessible Secure-Boot & Signed-OTA Toolkit for Constrained MCUs   21
   4.1 Problem Summary                                                             21
   4.2 Commercial & Open-Source Ecosystem Scan                                     21
   4.3 Patent & Prior-Art Landscape                                                21
   4.4 Technical Prior-Art and Feasibility                                         22
   4.5 White-Space Assessment                                                      22
   4.6 Competitive & Defensibility Analysis                                        23
   4.7 Regulatory / Standards Context                                              23
   4.8 Risk Matrix                                                                 23
   4.9 Recommended Next Step                                                       24
   4.10 Key Patent & Prior-Art Table                                               24
   4.11 Commercial & OSS Landscape Table                                           24
   4.12 Confidence Score & Evidence Gaps                                           25

5. ColdTrace — Multi-Modal Cold-Chain Integrity Logger                             26
   5.1 Problem Summary                                                             26
   5.2 Commercial Ecosystem Scan                                                   26
   5.3 Patent & Prior-Art Landscape                                                26
   5.4 Technical Prior-Art and Feasibility                                         27
   5.5 White-Space Assessment                                                      27
   5.6 Competitive & Defensibility Analysis                                        28
   5.7 Regulatory / Standards Context                                              28
   5.8 Risk Matrix                                                                 28
   5.9 Recommended Next Step                                                       29
   5.10 Key Patent & Prior-Art Table                                               29
   5.11 Commercial Landscape Table                                                 29
   5.12 Confidence Score & Evidence Gaps                                           30

6. Comparative Portfolio Analysis                                                  31
   6.1 Cross-Concept Evidence Matrix                                               31
   6.2 Portfolio Maps                                                              31
   6.3 Scoring Rationale                                                           33

7. Final Ranking & Portfolio Recommendations                                       34
8. Evidence Gaps & Phase 3 Hooks                                                   35
Annex A — References                                                               36

    Document
    control

    Project         MC Project — Innovation Pipeline

    Phase           Phase 2: Patent Landscape & White-Space Analysis

    Inputs          Phase 1C Concept Synthesis (five fixed concepts); Phase 1C Memory; Phase Doc

    Audience        Engineering R&D decision board

    Evidence base   121 indexed sources: USPTO full-text records (via FreePatentsOnline), vendor/product literature, peer-reviewed
                    journals, WHO/CDC program documents

    As-of date      17 July 2026

    Status          Final for board review


Scope note and legal disclaimer. This report is a technology-landscape and white-space assessment prepared to
support R&D prioritization. It is not a freedom-to-operate (FTO) opinion, not a validity study, and not legal advice.
Patent identifiers, titles, and priorities were verified against full-text records; expiry estimates are indicative only
and must be confirmed by counsel (term adjustments, continuations, and family members can shift dates). Several
primary databases (Google Patents, Espacenet, USPTO Patent Public Search, InPASS) were partially access-
restricted during this pass; US records were therefore retrieved through a mirrored full-text index, and JP/CN/IN
coverage is representative rather than exhaustive. Where evidence is thin, the gap is stated explicitly in each
concept's Section 12.


Executive Summary

Phase 1C fixed five concepts for landscape analysis. This phase subjected each to a twelve-section assessment
covering problem framing, commercial ecosystem, patent and prior-art density, technical feasibility, white space,
defensibility, regulatory pull, risk, and confidence. Three structural findings cut across the portfolio.

Finding 1 — The strongest opportunities sit where foundational patents have just expired, not where the
field is empty. OpenBraille is the clearest case: the shape-memory-alloy cell (US 5,685,721, 1997) [27] and the
electroactive-polymer cell (US 6,881,063, 2005) [26] have both lapsed into the public domain, and the Orbit Reader
20 has already proven that a non-piezoelectric cell can ship at $449 against a $3,500–$15,000 incumbent range [2][10
7]
     . ColdTrace shows the same pattern in algorithms: the electronic time-temperature "stability bank" indicator (US
7,102,526, 2003 priority) [116] is at/past expiry, freeing model-based excursion logic — even as one active patent
(US 10,887,735) fences off the buffered-probe implementation [117].

Finding 2 — Two concepts face red-ocean patent density where further invention is low-yield. VibeGuard's
bearing-fault-detection space is saturated: signature-detection methods explicitly robust to unrelated spectral peaks
were already patented by 2008 (US 7,421,349) [118], platform-scale IIoT analytics families and a dense stream of
CNN-based filings crowd the detection layer [46][47], and a venture-backed incumbent (Infinite Uptime) already
occupies the SME wedge with patented technology [54][56]. TrustLatch's core cryptography is equally unpatentable


4

— but deliberately so, because MCUboot/TF-M/Mender have made it open infrastructure [75][79][80]. Its opportunity
is compliance-driven usability, not IP.

Finding 3 — Regulatory calendars now differentiate the portfolio more than technology does. TrustLatch
rides the EU Cyber Resilience Act / UK PSTI wave that is converting secure update from option to obligation [74][7
6]
     ; ColdTrace rides WHO/CDC vaccine-handling rules and GDP [93][96][100]; OpenBraille rides accessibility funding
channels (APH Quota, ADIP) [109][110]. VibeGuard and TrueMoist have no equivalent forcing function, which
lengthens their sales cycles.

Composite ranking (equal-weighted six-dimension score, 0–10):

    Rank   Concept       Composite   Patent saturation        White space                Headline recommendation

    1      OpenBraille   7.0         Moderate                 Moderate–High              Advance to Phase 3; file provisional on
                                                                                         low-cost actuation kinematics

    2      TrustLatch    6.8         Moderate (mis-aimed at   Moderate–High              Advance as open-core compliance toolkit;
                                     PCs/servers)             (usability, not crypto)    speed over patents

    3      ColdTrace     6.3         Moderate–High            Moderate        (design-   Advance     with     FTO   review   of    US
                                                              around required)           10,887,735; virtual thermal mass

    4      TrueMoist     5.5         Moderate                 Low–Moderate               Hold;     validate   calibration-free    field
                                                                                         performance first

    5      VibeGuard     5.0         High                     Low                        Demote; revisit only with a sharper
                                                                                         vertical wedge


Scores are analyst assessments on a 0–10 ordinal scale derived from the evidence assembled in Sections 1–5 of this
report; they are prioritization aids, not measurements. The full scoring rubric and cross-concept evidence matrix
appear in Part 6.


Method & Evidence Conventions

Each concept chapter follows the mandated twelve-section template: (1) Problem Summary, (2) Commercial
Ecosystem Scan, (3) Patent & Prior-Art Landscape, (4) Technical Prior-Art and Feasibility, (5) White-Space
Assessment, (6) Competitive & Defensibility Analysis, (7) Regulatory / Standards Context, (8) Risk Matrix, (9)
Recommended Next Step, (10) Key Patent & Prior-Art Table, (11) Commercial Landscape Table, (12) Confidence
Score & Evidence Gaps. Patent records were read at full-text level for the highest-relevance documents in each
domain — nine patents in depth (US 5,685,721; US 6,881,063; US 11,410,574; US 2024/0363022; US 7,884,620;
US 11,598,743; US 7,102,526; US 10,887,735; US 7,421,349; US 10,740,084; US 9,953,166; US 11,042,609), with
hundreds of further records screened through result-set metadata [25][46][47][68][69][82][83][88][89].

Three conventions apply throughout. Citations use bracketed source IDs that resolve to the reference annex; a
maximum of two IDs is attached to any single claim. Patent expiry language is deliberately hedged ("expected",
"at/near expiry") because exact term depends on adjustments and family data outside this pass. And every
confidence score in Section 12 of each chapter is accompanied by the evidence gap that most threatens it, so the
board can see what an additional research sprint would need to close.


5

1. OpenBraille — Low-Cost Refreshable Braille Display Module

1.1 Problem Summary

Refreshable braille displays (RBDs) are the only channel through which blind users can access text — and, via
multiline variants, spatial content such as tables, math, and graphics — in a non-transient, literacy-preserving form.
The category has been structurally expensive for four decades: the American Foundation for the Blind places
typical single-line display prices at $3,500 to $15,000 [2], a price band widely corroborated by user communities
and charities that frame affordability as the field's central barrier [8][9]. The cost driver is the actuation cell:
incumbent devices use piezoelectric bimorph stacks whose per-cell cost has historically been estimated in the $100-
plus range, so a 40-cell line embeds thousands of dollars of actuators before electronics, housing, or margin [11].

The user need splits into two segments with different willingness-to-pay structures. In wealthy markets, users and
agencies want cheaper single-line companion displays and, increasingly, multiline tactile-graphics capability [14][22].
In low- and middle-income markets — where the majority of the world's blind population lives and where braille
literacy correlates strongly with employment — the need is an order-of-magnitude price break with offline content
loading, exactly the profile that led a Transforming Braille Group consortium including RNIB to back the Orbit
Reader program [109]. OpenBraille, as framed in Phase 1C, targets a low-cost refreshable braille display module
— the cell-plus-driver building block — rather than a finished consumer device, positioning it to serve OEMs,
education programs, and the multiline frontier simultaneously.


1.2 Commercial Ecosystem Scan

The commercial landscape has bifurcated since ~2017 into an incumbent piezoelectric tier and a disruptor tier built
on alternative actuation. In the disruptor tier, the Orbit Reader 20 sells at $449 (20 cells) and its Plus variant at $899
[107][112]
             ; Innovision's Braille Me, developed in India and distributed by National Braille Press, sells at $515.50 and
is marketed as built on patented cell technology [110][34]. Orbit Research describes its cell as using "mainstream
components and manufacturing processes" to deliver signage-quality dots "at a fraction of the cost of the
piezoelectric technology" [113]. Bristol Braille's Canute line pursues multiline reading through an open-source,
community-supported model [36][37][39], and the Blitab project demonstrated sustained investor/press appetite for a
~$500 tactile tablet concept [1][5].

At the premium end, HumanWare's Monarch multiline tablet — built on Dot Incorporation's actuator cells in
partnership with APH — lists at $15,500 [15][20], while Dot's own Dot Pad X targets tactile graphics for developers
and prosumers [19][16]. The surrounding software ecosystem (JAWS at $895, NVDA free, VoiceOver/BrailleBack) is
display-agnostic, so hardware differentiation rests on cell cost, dot quality, refresh speed, and reliability [107]. The
ecosystem read: the sub-$1,000 single-line segment is proven but thinly supplied, and the multiline segment is at
its expensive infancy — both are module-opportunity windows rather than finished-device windows (see Figure 3).


1.3 Patent & Prior-Art Landscape

The patent record shows a 50-year cadence of actuation approaches, with the oldest now expiring into a usable
public-domain base. Representative anchors read at full text: US 5,685,721 (granted 1997) — a refreshable braille


6

cell implemented with shape-memory alloys, now expired [27]; US 6,881,063 (granted 2005) — an electroactive-
polymer actuator braille cell, expected expired (~2022) [26]; US 11,410,574 (granted 2022) — a layered
electromagnetic braille display structure, active [29]; and US 2024/0363022 A1 — a refreshable braille display
system published in 2024, pending [28]. The surrounding result set is dense with expired or aging mechanism
patents — rotary/wheel displays (e.g., US 7,744,372; US 8,133,055; US 6,776,619), reed-based cells (US
9,424,759; US 8,690,576), an early system patent US 6,354,839 (2002), and electrothermal cell concepts —
alongside a continuing trickle of new filings, including a 2026 publication on braille display cell systems, indicating
the field is technically re-activating after the multiline wave [25].

Two portfolio-scale players matter most for freedom-to-operate. Dot Incorporation has built a substantial patent
estate around its miniaturized electromagnetic latching actuator ("Dot cell") and supplies the cells inside the
Monarch; any multiline or latching-pin approach must be claim-charted against this family [19][17]. Orbit Research
protects its low-cost cell architecture — the mechanism behind the $449 display — meaning OpenBraille cannot
simply clone the proven disruptor either [113]. The academic and maker prior-art layer is also thick: ultra-low-cost
device designs appear in journals, ISEF projects, and design contests [3][4][6][33], and an ACM TOCHI survey of pin-
array product architectures documents essentially every historical kinematic approach [21]. Net: the concept of a
low-cost cell is old and heavily published; patentable residue lies in specific new kinematics, latching schemes,
drive electronics, or manufacturing methods that clear both the expired art (which is free to use but also
anticipates) and the two active estates.


1.4 Technical Prior-Art and Feasibility

Feasibility is the strongest in the portfolio because the market has already executed natural experiments at the target
price point. The Orbit Reader 20 demonstrates that a non-piezo cell can meet everyday reading duty at $449 in a
mainstream commercial product [107][111]; Braille Me demonstrates an India-developed alternative at $515.50 with
routing buttons [110]; Canute demonstrates that a small team can ship multiline refreshable braille at all [36][38]. The
known engineering constraints are equally well documented in user and reviewer communities: refresh rate, dot
firmness ("signage quality"), acoustic noise, and cell durability are the axes on which cheap cells are judged against
piezo [107][108].

Prior art defines the actuation design space almost completely: piezoelectric bimorph (incumbent, expensive,
excellent tactility), electromagnetic latching (Dot; Orbit-variant EM), SMA (expired US 5,685,721 — slow, power-
hungry, but cheap) [27], electroactive polymers (expired US 6,881,063 — materials risk) [26], electrothermal (US
2007/0020589 A1), pneumatic/microfluidic (US 12,555,492), and rotary/continuous-surface schemes [25]. A Phase 3
prototype can therefore start from public-domain mechanisms and concentrate invention on cost-out engineering
— e.g., shared-driver multiplexing, stamped rather than machined parts, or a novel low-force latching geometry —
rather than on discovering a new physics. Technical risk is moderate; the binding constraint is demonstrating piezo-
comparable dot force and >10⁷-cycle endurance at a cell cost under roughly $10–15, the threshold implied by the
$449/20-cell market proof.


1.5 White-Space Assessment

White space is moderate-to-high, and it is structural rather than conceptual. The expired base (SMA, EAP, early
rotary/system patents) creates a legal free zone for mechanism choice; the demand gap is verified by the fact that


7

two products (Orbit, Braille Me) could not fully supply the sub-$1,000 segment they created [9][110]. The un-
crowded zones with genuine novelty potential are: (a) multiline-capable low-cost cells — Dot's estate is the main
fence here, and Monarch's $15,500 price shows the cost problem is unsolved [15]; (b) module-level products (cell +
driver + reference firmware sold to OEMs/education programs) — no dominant merchant supplier exists; and (c)
manufacturing-method IP (injection-molded cell arrays, automated pin assembly) where publication is thinner
than mechanism patents [21][25].

Conversely, two zones are closed: single-line low-cost devices (Orbit/Braille Me own the reference designs and
price expectations), and electromagnetic latching-pin multiline (Dot's active filings plus the layered-EM structure
of US 11,410,574) [29][19]. The white-space verdict: pursue the module, not the gadget; pursue manufacturing
innovation, not another wheel patent.


1.6 Competitive & Defensibility Analysis

Direct competitors in the module sense are few; device competitors are Orbit Research (cell IP + APH distribution),
Innovision (patented low-cost cell), Dot (premium multiline cells), and the piezo incumbents (HumanWare, HIMS,
BAUM, Help Tech) whose cost structure is locked to bimorph stacks [107][110][19][2]. Indirect competition is audio:
free screen readers keep improving, and any RBD must justify its existence against "good-enough speech," which is
why literacy-critical and education use-cases are the defensible beachhead [8][107].

Defensibility would rest on three layers: a mechanism patent on the specific low-cost kinematics (must clear US
11,410,574, Dot's estate, and the expired art that anticipates generic approaches); process/manufacturing IP,
which competitors cannot easily design around once a $5–10 cell cost is demonstrated; and ecosystem lock-in
through reference firmware and education-program relationships (NBP/APH-style channels) [34][109]. Speed
matters: the 2024–2026 publication uptick (US 2024/0363022; a 2026 cell-system publication) shows others are re-
entering the space [28][25].


1.7 Regulatory / Standards Context

Demand-side regulation is favorable and unusually concrete. US federal procurement (Section 508), the ADA, and
the European Accessibility Act / EN 301 549 obligate accessible interfaces in public contexts, sustaining agency
purchasing; APH Quota funds explicitly subsidize displays for US students — the Orbit Reader 20 is a Quota-
eligible product, a material sales channel [110]. India's ADIP scheme performs the same function domestically, and
RNIB's direct distribution role in the UK shows how charity-channel endorsement functions as a regulatory-
adjacent demand lever [109].

On standards, braille cell geometry (dot height/diameter/spacing) follows established norms that constrain
mechanical design but are public; there is no safety-certification moat (CE/FCC suffice for a module). The
Marrakesh Treaty eases cross-border accessible-format content, indirectly expanding the content base that justifies
display purchases. None of these factors block OpenBraille; several actively subsidize its target customers.


1.8 Risk Matrix

    Risk              Likelihood                         Impact                        Mitigation


8

    FTO conflict with Dot latching-actuator or               Medium        High           Early claim-charting; choose kinematics outside latching EM;
    layered-EM claims                                                                     license if multiline pursued

    Cannot       hit      piezo-comparable             dot   Medium        High           Phase 3 gate: 10⁷-cycle + force test before any filing
    force/endurance at target cost

    Orbit/Braille      Me      extend         downward,      Medium        Medium         Differentiate          on   module/OEM    channel      and   multiline
    commoditizing the segment                                                             readiness, not on single-line devices

    Screen-reader      audio   substitution      shrinks     Low–          Medium         Anchor in education/literacy and tactile-graphics use-cases [14]
    addressable demand                                       Med                          [21]


    Charity/agency procurement cycles slow                   High          Medium         Design for Quota/ADIP eligibility from day one [110][109]
    revenue

    Expired-art anticipation kills patent claims             Medium        Medium         File on manufacturing method + specific kinematics, not on
                                                                                          "low-cost cell" as such [21][25]


1.9 Recommended Next Step

Advance to Phase 3. Build a cell-level prototype targeting <$15 cell cost at volume, using public-domain actuation
physics, with invention concentrated on (i) a specific latching/drive kinematic cleared against US 11,410,574 and
Dot's estate, and (ii) a manufacturability method (molded array, automated pin insertion). File a provisional on
those two layers once the endurance gate (10⁷ cycles, dot-force parity with piezo) is passed; in parallel, open
OEM/education-channel conversations patterned on the NBP/Braille Me and APH/Orbit precedents [34][110].


1.10 Key Patent & Prior-Art Table

    Document                                    Year         Holder / type                  Content                                     Status & relevance

    US 5,685,721                                1997         SMA braille cell               Shape-memory-alloy            refreshable   Expired — free design
                                                                                                   [27]                                 base
                                                                                            cell

    US 6,881,063                                2005         EAP braille cell               Electroactive-polymer            actuator   Expected expired —
                                                                                                   [26]                                 free design base
                                                                                            cell

    US 6,354,839                                2002         Refreshable        braille     Early system-level claims [25]              Expired/near            —
                                                             display system                                                             background

    US 11,410,574                               2022         Layered                        Stacked EM structure for pin                Active — key FTO
                                                             electromagnetic                              [29]                          fence
                                                                                            actuation
                                                             display

    US 2024/0363022 A1                          2024         Refreshable        display     Recent system filing [28]                   Pending — monitor
                                                             system

    Dot actuator estate                         2015–        Dot Incorporation              Latching             EM    micro-actuator   Active — key FTO
                                                                                                                                   [1   fence
                                                                                            family behind Dot Pad/Monarch
                                                                                            9][17]


    Rotary/wheel          family        (US     2006–        Various                        Continuous-surface                refresh   Mostly     expired      —
    7,744,372; US 8,133,055; US                 2011                                                        [25]                        free, but anticipates
                                                                                            approaches
    6,776,619)


9

 ACM TOCHI pin-array          2023    Academic         Architectural taxonomy of pin-array         Non-patent     prior     art        —
 survey                                                devices [21]                                anticipation risk

 Ultra-low-cost      device   2018–   Academic/maker   Servo/motor-based teaching devices [3]      Non-patent prior art
 literature                   2020                     [4][33]


1.11 Commercial Landscape Table

 Player                                                          Product / role                    Price point            Evidence

 Orbit Research / APH                                            Orbit Reader 20 / 20 Plus         $449 / $899            [107][112]


 Innovision / NBP                                                Braille Me (patented cell)        $515.50                [110][34]


 HumanWare / APH / Dot                                           Monarch multiline tablet          $15,500                [15][20]


 Dot Incorporation                                               Dot Pad X + cell supply           Premium                [19][16]


 Bristol Braille                                                 Canute multiline (open source)    Community-priced       [36][37][39]


 Blitab                                                          Tactile tablet project            ~$500 target           [1][5]


 Piezo incumbents (HumanWare, HIMS, BAUM, Help Tech)             Traditional 14–80-cell displays   $3,500–$15,000         [2]


1.12 Confidence Score & Evidence Gaps

Confidence: 8/10 — the highest in the portfolio. Price points, the expired-patent base, and the two active FTO
fences are all verified at primary-source level; feasibility is market-proven.

Evidence gaps: (1) Dot estate claim charts — the exact claim scope of Dot's latching-actuator family needs
professional charting before multiline work; (2) Orbit Research's own patent numbers were identified via product
literature rather than direct record reads [113]; (3) Indian (InPASS) filings by Innovision and others were outside this
pass's reach and may contain module-relevant art; (4) no cell-cost teardown of the Orbit/Braille Me mechanisms
was available, so the <$15 cell-cost target is an inference from retail prices, not a measured bill of materials.


10

2. VibeGuard — Spatially-Isolated Bearing Fault Early-Warning Node

2.1 Problem Summary

Unplanned rotating-machinery downtime is a well-quantified economic drain, and vibration-based condition
monitoring is the standard early-warning modality for bearing degradation. Predictive-maintenance (PdM) vendors
promise double-digit reductions in downtime and maintenance cost [43][51], yet adoption concentrates in large
plants: small and mid-sized enterprises face per-point costs, analytics complexity, and alarm fatigue that make
classic PdM uneconomic — a gap explicitly targeted by newer entrants [54][55]. The problem VibeGuard addresses,
as framed in Phase 1C, is sharper than "cheap PdM": a monitoring node bolted to one machine in a dense shop floor
also feels the vibration of neighboring machines through floors, benches, and shafts, so generic low-cost nodes
generate false alarms or miss early faults — a noise-discrimination problem that the bearing-fault literature has
studied for decades [118][50].

The technical question is therefore not whether bearing faults are detectable (a solved problem at the research level)
but whether a single, cheap, self-contained node can attribute spectral energy to its own machine with sufficient
confidence to be trusted by a non-specialist operator. The severity of the cross-talk problem depends on mounting,
machine spacing, and rotational-speed separation between neighbors — worst in dense SME workshops, which is
exactly the commercial target.


2.2 Commercial Ecosystem Scan

The market stratifies into three tiers. At the top, Augury sells an enterprise machine-/process-health platform with
proprietary sensors and has achieved top-tier industry recognition [43][44][45]; Tractian markets a similar sensor-
                                                                         [51]
plus-platform bundle with aggressive SMB-adjacent pricing                       . Incumbent instrument houses (SKF,
Fluke/PRÜFTECHNIK, Emerson/AMS) dominate wired and route-based monitoring, with per-point economics
aimed at critical assets [50][46]. The third tier is the one VibeGuard would enter: Infinite Uptime (India) explicitly
targets SME plants, publicizes patented diagnostic technology, and raised a $35M growth round on that positioning
[54][56][52]
               — simultaneously validating the wedge and demonstrating that it is already defended.

Adjacent commoditization pressure comes from the component layer: industrial MEMS vibration sensors and
MCU-class edge inference are now catalog parts, and research-grade open designs for wireless MEMS monitoring
nodes appear regularly in the literature [42][48]. The ecosystem read: detection-as-a-feature is commoditizing fast;
the scarce commodity is trustworthy attribution (whose fault is it?) in acoustically coupled environments — but
the patent record below shows even that layer is heavily worked.


2.3 Patent & Prior-Art Landscape

This is the most saturated landscape of the five concepts. Two FreePatentsOnline result sets — "vibration
monitoring bearing fault diagnosis" and "predictive maintenance vibration edge machine learning" — return dense
layers of filings spanning decades, from the US Navy's US 7,421,349 "Bearing fault signature detection" (2008)
through automated-diagnosis-with-confidence publications (US 2016/0041070 A1), platform-scale industrial-data
families (the US 2020/0150643 A1 cluster), and a continuing stream of CNN-based diagnosis filings into 2024–


11

2025 (e.g., US 12,067,486) [46][47]. The 2008 Navy patent is particularly instructive: it explicitly solves the problem
of distinguishing fault-generated spectral peaks from coincidental peaks produced by unrelated processes —
using phase coupling between sidebands — which is the exact discrimination mechanism VibeGuard's "spatial
isolation" framing implies [118]. In other words, the core signal-processing claim is anticipated by 20-year-old art.

Ownership spans the US government (Navy), platform industrials (GE-family IIoT analytics), condition-monitoring
specialists, and a heavy tail of Chinese university assignees on CNN/attention-based diagnosis [46][47]. Academic
prior art compounds the saturation: envelope analysis/high-frequency resonance is textbook; noise-robust and
cross-machine fault diagnosis is an active journal topic with hundreds of papers [42][48][49][50]. The practical
consequence: almost any detection algorithm VibeGuard might ship is either anticipated, obvious over, or
affirmatively claimed by existing art; patentable residue would have to live in an unusually specific mechanical or
deployment innovation.


2.4 Technical Prior-Art and Feasibility

Feasibility of the node itself is high and unremarkable: triaxial MEMS accelerometers with ≥10 kHz bandwidth,
MCU-class FFT/envelope computation, and BLE/LoRa/Wi-Fi backhaul are all catalog engineering, and reference
designs abound [48][42]. The discriminating feature — call it spatial attribution — has three candidate mechanisms,
each with established prior art: (i) spectral separation using known neighbor speeds/orders (classical order
tracking); (ii) phase-coupling tests that verify whether sideband families originate from one physical process
(patented, US 7,421,349, at/near expiry, hence free to use but not protectable) [118]; and (iii) blind source
separation / multi-sensor fusion, which is journal-active but rarely reduced to a robust single-node product [48][49].

The honest engineering assessment: a demonstration of spatial attribution on a bench rig is achievable in weeks; a
robust product that maintains attribution across variable-speed machines, belt-driven loads, and structurally coupled
neighbors is a multi-year data problem — the same problem the entire industry already works on [50][51]. No physics
barrier exists; no shortcut exists either. VibeGuard's concept is feasible but undifferentiated at the invention layer.


2.5 White-Space Assessment

White space is low. At the algorithm layer, signature detection, noise rejection, confidence scoring, and edge
deployment are all heavily claimed [46][47][118]. At the business-model layer, the SME wedge that justified the
concept is occupied by a funded incumbent marketing patented technology [54][56]. The residual gaps are narrow: (a)
ultra-low-cost single-node hardware sold without a cloud subscription — a pricing stance more than an
invention; (b) installation-physics innovations (mounts, mechanical isolation, coupling-aware placement
guidance) that reduce cross-talk mechanically rather than algorithmically — comparatively under-published; and
(c) vertical niches (low-speed machinery, specific industries) where generic platforms underperform [50].

None of these gaps supports a strong patent position; all support at best a lean commercial entry. For a portfolio
whose currency is defensible novelty, VibeGuard offers the least.


2.6 Competitive & Defensibility Analysis


12

Competitors include platform vendors (Augury, Tractian), instrument incumbents (SKF, Fluke), the SME-focused
Infinite Uptime, and — increasingly — free/cheap reference designs plus the customers' own maintenance intuition
[43][51][54]
               . Defensibility through patents is weak: detection IP is crowded, and enforcement against algorithmic
lookalikes is notoriously difficult. Defensibility through data is theoretically possible (labeled cross-machine
datasets are scarce) but requires deployments to accumulate — a chicken-and-egg dynamic that funded competitors
are already past [56].

The realistic moat, if any, is deployment economics: a node cheap enough to be a consumable, with zero-config
commissioning. That is a supply-chain and UX achievement, not IP — and it is perishable the moment a platform
vendor ships a $99 sensor.


2.7 Regulatory / Standards Context

No mandate drives adoption; PdM is economically self-justifying where it works. Relevant standards are ISO
10816/20816 (vibration severity evaluation — useful as an alarm-threshold anchor), ISO 13373 (condition-
monitoring data communication), and IECEx/ATEX only if hazardous-area variants are pursued, which would
multiply certification cost. The absence of a forcing function means long, ROI-proof-driven sales cycles in the
SME segment — consistent with how Infinite Uptime sells (outcome-based, subscription) [54][55].

A secondary consideration: because the node processes operational data, enterprise customers increasingly impose
security review on connected sensors — an argument for pairing any such product with a TrustLatch-class secure-
update foundation, linking two concepts in this portfolio.


2.8 Risk Matrix

 Risk                                         Likelihood   Impact   Mitigation

 Detection claims anticipated by crowded      High         High     Do not file on detection; limit IP to mechanical/deployment
 prior art                                                          specifics [46][118]

 Cross-machine false alarms erode trust in    Medium–      High     Field-trial gate in a dense-machine environment before
 the node                                     High                  commitment

 Funded incumbents compress the SME           High         High     Compete on no-subscription economics or exit [56]
 wedge

 Platform vendors ship cheap hardware,        Medium       High     Treat hardware margin as temporary; services/vertical focus
 killing the cost moat

 Long SME sales cycles with no regulatory     High         Medium   Outcome-based pricing; anchor on ISO 10816 alarms
 pull

 Data-access catch-22 for attribution model   Medium       Medium   Partnerships with shop-floor networks; public datasets for
 training                                                           bootstrap [48]


2.9 Recommended Next Step


13

Demote. Do not fund a patent-track prototype. If strategic interest persists, re-scope toward one of the two
defensible niches — mechanical cross-talk mitigation or a named vertical — and run a 90-day field validation of
single-node attribution accuracy in a real dense-machine workshop before any further investment. Reuse the
concept's security requirements as a TrustLatch pilot use-case instead.


2.10 Key Patent & Prior-Art Table

 Document                      Year      Holder / type            Content                                           Status & relevance

 US 7,421,349                  2008      US Navy                  Phase-coupling      fault-signature   detection   At/near expiry — free to
                                                                  robust to unrelated peaks [118]                   use, anticipates the core
                                                                                                                    claim

 US 2016/0041070 A1            2016      Industrial assignee      Automatic fault diagnosis with confidence         Active family possible —
                                                                  output [47]                                       FTO check

 US 2020/0150643 A1            2020      Platform industrial      IIoT data collection/learning/streaming for       Active — platform fence
 cluster                                 (GE-family)                                 [47]
                                                                  asset monitoring

 US 12,067,486                 2024/25   Recent filing            Fault-diagnosis method (CNN-class) [46]           Active — shows filing
                                                                                                                    velocity

 CNN/attention                 2019–     Chinese                  Dense application layer [46]                      Active — saturation signal
 diagnosis filings             2025      universities

 Noise-robust        bearing   2023      Academic (MDPI           Cross-condition/noise-robust diagnosis [48][4     Non-patent prior art
 diagnosis literature                    Sensors et al.)          2]


 Brunel         condition-     2015+     Academic                 Field survey of techniques and vendors [50]       Non-patent prior art
 monitoring thesis

 Infinite            Uptime    —         Corporate       (India   Patented diagnostics, SME deployment              Competitor IP — FTO +
 patented               IDE              SME)                             [54][52]                                  market fence
                                                                  model
 technology


2.11 Commercial Landscape Table

 Player                                       Positioning                                    Business model                          Evidence

 Augury                                       Enterprise machine/process health              Sensor + SaaS subscription              [43][44][45]


 Tractian                                     Sensor + platform, aggressive SMB              Subscription                            [51]

                                              pricing

 Infinite Uptime                              SME-focused, patented diagnostics              Outcome-based subscription; raised      [54][56]

                                                                                             $35M

 SKF / Fluke / Emerson                        Incumbent instruments + services               Hardware + service contracts            [50]


 Component layer (ADI/ST/TI MEMS +            Enabling commoditization                       Catalog silicon                         [48]

 MCUs)

 Open/academic node designs                   Zero-cost reference designs                    n/a                                     [42][48]


14

2.12 Confidence Score & Evidence Gaps

Confidence: 7/10. The saturation verdict is robust — it rests on two independent result sets, a full-text read of the
foundational noise-rejection patent, and convergent academic literature [46][47][118][48].

Evidence gaps: (1) CPC-level filing counts (G01M 13/04, G01H 1/00) were not retrievable in this pass, so
saturation is assessed from result-set density rather than bibliometrics; (2) the exact claim scope of Infinite
Uptime's patented technology is inferred from press coverage [54][52]; (3) no measured data exists on single-node
attribution accuracy in dense shops — the concept's pivotal performance claim remains untested by anyone,
including incumbents.


15

3. TrueMoist — Drift-Self-Correcting Soil Moisture Controller

3.1 Problem Summary

Capacitive (dielectric) soil-moisture sensors are the default low-cost irrigation input, but their raw readings drift
with soil salinity (electrical conductivity), temperature, and aging/corrosion, so a probe calibrated at
installation can be materially wrong months later — driving over- or under-irrigation precisely in the fertigated,
high-value crops where accuracy pays [63][64]. The physics is unforgiving: water's relative permittivity (~80)
dominates the soil dielectric, but it is itself temperature-dependent, and bulk EC couples into low-frequency
capacitance measurements, as the patent record itself explains in detail [115][114]. Peer-reviewed studies repeatedly
show that salinity and temperature materially bias capacitive probes unless compensation is applied [63][64][65][66].

The unmet need, as framed in Phase 1C, is a controller that self-corrects drift on-node — estimating and
compensating salinity/temperature effects continuously, without the user re-calibrating or sending soil samples to a
lab. The target users are commercial horticulture and smallholder drip-irrigation operations that cannot justify
research-grade probes (METER TEROS-class) but are ruined by hobby-grade drift [59][70].


3.2 Commercial Ecosystem Scan

The market splits into three layers. Research-grade vendors — METER (TEROS dielectric line), Campbell
Scientific, Sentek — deliver accurate, temperature/EC-aware instruments at prices that reflect lab positioning [59][6
0]
     . Mid-market agronomy platforms — CropX being the most visible, with substantial venture backing — bundle
decent sensors with analytics and irrigation advice, monetizing the service rather than the probe [70][71]. At the
bottom, hobbyist capacitive probes sell for a few dollars and are notorious for corrosion and drift, a failure mode
documented across maker and academic evaluations [64][66].

The structural gap is a mid-price probe with research-grade correction: vendors at the top embed multi-
parameter compensation in expensive instruments; vendors at the bottom ship raw RC-time-constant boards with no
compensation at all. CropX-class platforms partially close the gap but lock customers into subscriptions and their
own hardware [70][71]. TrueMoist's controller positioning (sensor-agnostic correction + irrigation actuation) would
sit between the layers, but the patent record shows the compensation concept is far from new — the commercial
gap persists because of calibration economics and soil-specificity, not because nobody thought of correcting for EC
and temperature.


3.3 Patent & Prior-Art Landscape

The compensation space is well-populated at the circuit and probe level. Read at full text: US 7,884,620 — "Sensor
for measuring moisture and salinity" (dual-frequency bridge: high-frequency capacitance channel for moisture,
low-frequency resistance channel for salinity, with ratiometric, self-taring detectors that null temperature drift;
priority 2008, expected expiry ~2028) [114]; and US 11,598,743 — "Soil monitoring sensor including single probe
and temperature compensation" (resonant single-probe sensor with an integrated temperature sensor compensating
the moisture determination; Korean priority 2020, active to ~2040) [115]. The surrounding result sets add
temperature-adjusted probe electronics (US 9,949,450), automatic calibration methods (US 9,585,307), absolute-


16

reading calibration-free claims (US 6,657,443), and a 1974 temperature-and-salinity compensation patent (US
3,782,179, long expired) [68][69]. The '620 patent itself situates US 5,479,104 as prior art on simultaneous
capacitance/conductance measurement [114].

Academic prior art is equally thick: temperature and salinity effects on capacitive/TDR probes are a standard study
topic with published correction regressions per soil type [63][64][65][66]. Net assessment: "measure EC and
temperature, then correct" is anticipated many times over at both the circuit and method level. The '743 patent
is the sharpest fence — its claims cover a single probe plus temperature sensor plus compensated determination,
which reads uncomfortably close to a naive version of TrueMoist [115]. Residual novelty would need to live in the
self-correcting aspect: on-line, in-situ estimation that tracks drift over seasons without user calibration events,
ideally soil-agnostic — a harder, more specific method claim than anything screened in this pass, but not provably
clear of the dense Korean/CN filing tail [68][69].


3.4 Technical Prior-Art and Feasibility

A working TrueMoist prototype is straightforward: a capacitive front-end, a bulk-EC channel (two- or four-
electrode), a soil-temperature sensor, and a regression/polynomial correction running on any MCU — the '620
patent demonstrates a complete, manufacturable embodiment of exactly this architecture, and its expiry (~2028)
will soon free even that specific circuit [114]. The academic literature supplies correction models and quantifies the
residual errors [63][64]. Feasibility risk concentrates in soil-specificity: dielectric-EC-moisture coupling varies with
texture, clay mineralogy, and organic matter, so a single factory calibration cannot be universal; research probes
solve this with soil-specific calibration routines that TrueMoist explicitly wants to eliminate [65][66].

The credible technical path is in-situ self-calibration: using long-horizon signal structure (diurnal temperature
cycles, irrigation/dry-down events) as natural excitation to continuously re-fit correction parameters on-node. This
is implementable with known statistics, but its accuracy claim must be validated across soil types — a season-scale
field program, not a bench exercise. Feasibility: moderate-to-high for assisted correction; unproven for fully
calibration-free operation.


3.5 White-Space Assessment

White space is low-to-moderate. Closed zones: dual-frequency moisture+salinity circuits ('620, expiring) [114];
single-probe + temperature compensation ('743, active) [115]; generic auto-calibration and absolute-reading claims [6
9]
     . Open or thin zones: (a) event-driven self-recalibration methods (using irrigation/dry-down signatures as
reference points) — not found in this pass, plausibly novel as a specific method; (b) soil-agnostic universal
correction with published multi-soil validation — a credibility gap in the whole market [65]; (c) the controller
integration layer — correction feeding closed-loop irrigation decisions with audit trails, where product (not
patent) differentiation lives [70].

The board should treat TrueMoist as a product-engineering play with a possible narrow method filing, not as a
platform-IP opportunity.


3.6 Competitive & Defensibility Analysis


17

Competition: METER/Campbell at the top (accuracy brand), CropX/Sensoterra in the service-bundled middle [70][7
1]
     , and commodity probes below. A TrueMoist product would fight on "research-grade readings at prosumer prices,
no subscription." Defensibility through patents is narrow (see §3.3–3.5); defensibility through validation data is
more realistic — a published, multi-soil accuracy benchmark would be a genuine market asset because no low-cost
vendor has one [64][66]. Distribution through drip-irrigation dealers and government micro-irrigation programs
matters more than IP in this category.

A second defensive angle: the correction algorithm is embedded firmware — keep it as a trade secret, publish only
the validation results. This avoids disclosing method claims that a Korean/CN filing tail might surround anyway [68]
[115]
        .


3.7 Regulatory / Standards Context

No device-level mandate exists for soil sensors. Demand-side programs are the relevant context: micro-irrigation
subsidies (e.g., India's PMKSY) and water-use-efficiency regulations in water-stressed regions indirectly fund
sensor-equipped drip systems; pesticide/fertilizer stewardship programs favor documented irrigation control.
Metrological self-declaration (CE) suffices; there is no certification moat either way. The regulatory tailwind is real
but soft — it subsidizes the customer's purchase rather than obligating it.


3.8 Risk Matrix

 Risk                                             Likelihood   Impact   Mitigation

 '743 single-probe temp-compensation claims       Medium       High     Claim-chart before design freeze; consider two-probe or
 read onto product                                                      method-level design-around [115]

 Calibration-free accuracy fails on clay/saline   Medium–      High     Multi-soil field validation as Phase 3 gate [65][66]
 soils                                            High

 '620 expiry (~2028) floods market with free      Medium       Medium   Differentiate on self-calibration software + validation data,
 dual-frequency designs                                                 not circuit [114]

 CropX-class platforms add correction as a        Medium       High     Sensor-agnostic positioning; dealer channels [70]
 feature

 Commodity probe price erosion                    High         Medium   Sell controller + correction, not bare probes

 Long agri sales cycles, no mandate               High         Medium   Ride subsidy programs; co-market with drip OEMs


3.9 Recommended Next Step

Hold pending a validation sprint. Before any filing or product commitment, run a two-season, three-soil-type
field trial comparing on-node self-corrected readings against gravimetric truth and a research-grade reference.
Advance only if the self-correcting loop demonstrably holds accuracy without user recalibration; if it does, protect
the specific event-driven recalibration method (narrow filing) and compete on published accuracy data. If the loop
underperforms, fold the concept into a CropX-style service analysis and exit hardware.


18

3.10 Key Patent & Prior-Art Table

                                         Holder /
 Document                       Year                     Content                                                        Status & relevance
                                         type

 US 3,782,179                   1974     —               Temperature-             and       salinity-compensated        Expired — concept is 50
                                                                             [68]                                       years old
                                                         measurement

 US 5,479,104                   1995     —               Simultaneous soil capacitance/conductance                      Expired — cited as prior art
                                                                  [114]                                                 inside '620
                                                         sensor

 US 7,884,620                   2011     Campbell-       Dual-frequency moisture + salinity bridge,                     Expected expiry ~2028 —
                                         family                                         [114]                           soon free
                                                         self-taring detectors

 US 6,657,443                   2003     —               "Absolute         reading,"            no-calibration   soil   Likely expired — anticipates
                                                         sensor [69]                                                    calibration-free claims

 US 9,585,307                   2017     —               Automatic calibration method (optical) [69]                    Active — calibration-method
                                                                                                                        fence

 US 9,949,450                   2018     —               Probe            with           temperature-adjustment         Active — circuit fence
                                                                          [68]
                                                         electronics

 US 11,598,743                  2023     Korean          Single probe + temperature compensation [11                    Active — sharpest fence
                                         assignee        5]


 Salinity/temperature effect    2020–    Academic        Quantified              EC/temperature           bias     +    Non-patent prior art
 studies                        2024                                      [63][64][66]
                                                         corrections


3.11 Commercial Landscape Table

 Player                                 Layer                          Positioning                                                        Evidence

 METER (TEROS)                          Research grade                 Accurate dielectric probes, premium pricing                        [59][60]


 Campbell Scientific / Sentek           Research grade                 Full monitoring stations                                           [68]


 CropX                                  Mid-market platform            Sensor + agronomy SaaS, venture-backed                             [70][71]


 Sensoterra                             Mid-market                     LoRa probe fleet                                                   [70]


 Commodity capacitive probes            Hobby/OEM                      $-class boards, drift/corrosion-prone                              [64][66]


3.12 Confidence Score & Evidence Gaps

Confidence: 7/10. Both on-point patents were read in full; the academic drift literature is convergent; commercial
layering is well-evidenced [114][115][63].

Evidence gaps: (1) Korean/CN application tail (the '743 family and siblings) not fully enumerated — needed before
any filing; (2) no published data on fully calibration-free multi-season accuracy exists anywhere, so the concept's
core performance claim is unproven in the open literature [65][66]; (3) mid-market vendor pricing (CropX/Sensoterra


19

per-point costs) is partly opaque — Crunchbase-tier data only [71]; (4) InPASS coverage of Indian agri-sensor
filings was out of reach this pass.


20

4. TrustLatch — Accessible Secure-Boot & Signed-OTA Toolkit for
Constrained MCUs

4.1 Problem Summary

Every connected embedded product now needs two security primitives: assurance that only authentic firmware
executes (secure boot) and a channel to deliver signed updates that cannot be tampered with in transit or rollback-
attacked (signed OTA). The primitives are mature — the open-source MCUboot project documents and implements
exactly this chain for 32-bit MCUs [75][79] — yet field evidence and practitioner literature consistently show small
teams shipping products without them, because correct integration (key generation, secure storage, image signing,
slot management, recovery) is a multi-week specialist effort per MCU family [74][76]. The result is a large population
of fielded devices that cannot be patched safely — a systemic vulnerability that regulators have now moved to
eliminate (see §4.7).

TrustLatch, as framed in Phase 1C, is a toolkit — curated bootloader configurations, key-management workflow,
signing service, and reference integrations for constrained targets (ESP32, STM32, nRF52, AVR/PIC-class) — that
compresses adoption from weeks to hours. The concept is explicitly accessibility-driven: the invention is not new
cryptography but the removal of everything that makes existing cryptography go unused [74][78].


4.2 Commercial & Open-Source Ecosystem Scan

Uniquely among the five concepts, TrustLatch's "competitors" are mostly free. MCUboot (Linux Foundation)
provides a secure bootloader with image signing and swap/rollback logic and is the default in Zephyr [75][78][79];
TF-M provides PSA-certified security services on ARMv8-M; silicon vendors ship their own chains (ESP32
Secure Boot v2, ST SBSFU). On the OTA side, Mender anchors the update-server category with an open-source
core and commercial SaaS [80][81], flanked by RAUC, SWUpdate, and hawkBit for Linux-class targets, while
practitioner guides codify secure-OTA patterns for resource-constrained fleets [74].

Commercial security silicon (secure elements, HSMs) and cloud provisioning services cover the top of the market,
and academic work keeps publishing MCU secure-boot frameworks — confirming that the knowledge is abundant
[76][77]
           . What nobody sells well is opinionated, cross-vendor, constrained-MCU onboarding: the ecosystem is a
box of parts. The commercial read: the money is not in the boot chain but in compliance tooling, fleet key
management, and update operations — Mender's SaaS trajectory demonstrates willingness to pay for exactly that
adjacent value [80][81].


4.3 Patent & Prior-Art Landscape

The patent layer is dense but mis-aimed relative to TrustLatch's niche. Read at full text: US 10,740,084 — SoC-
assisted resilient boot, in which an immutable root of trust inside an SoC authenticates and applies firmware
updates, with recovery paths; the specification explicitly references Intel CSME-class architecture [119]. US
9,953,166 — a Microsemi/Microchip-family method for securely booting processors that lack built-in secure
boot, using an external secure root-of-trust chip that emulates boot memory, serves a nonce, and verifies a
challenge–response MAC (with PUF hardware binding and penalty responses); priority 2013, expected active into


21

~2033 [120]. US 11,042,609 — secure-element registration and provisioning systems for IoT devices (deferred
PKI provisioning, certificate monetization at the vendor level) [121]. Result sets add Microsoft/Dell/HP-class filings
on secure boot firmware update (e.g., US 8,589,302; US 9,483,246) and hardware-enforced firmware security (US
10,839,080) [82][83].

Three conclusions follow. One: everything cryptographic is either open source or patented by someone else —
there is no IP to originate in algorithms, chains of trust, or signed-image formats [75][79][119]. Two: the active patents
concentrate on richer platforms (SoCs with ROM roots of trust, TPM/secure-element provisioning) — the
constrained-MCU, no-hardware-RoT segment is comparatively thin precisely because the open-source stack
already serves it, which deters filing [120][83]. Three: the one patent that does read onto the constrained segment —
US 9,953,166's external-RoT challenge–response — does not block a software toolkit that relies on the MCU's own
boot ROM or flash protection (the mainstream ESP32/STM32 path), but it would matter if TrustLatch ever shipped
a companion hardware root-of-trust dongle [120]. Prior-art risk to the toolkit concept itself is low because toolkits are
product/service constructs, not patent claims.


4.4 Technical Prior-Art and Feasibility

Feasibility is the highest in the portfolio: every component exists, is documented, and has production deployments.
MCUboot's docs and repositories provide the bootloader, image format, and signing tools; vendor ROMs provide
                                                                                                          [75][79][80]
first-stage verification; Mender/RAUC-class systems provide server-side update operations                                . The
engineering content of TrustLatch is integration curation — per-MCU reference ports, a key ceremony workflow,
CI signing, and recovery drills — plus the documentation and default configurations that determine whether a small
team actually finishes the job [74][78].

The real technical risks are adoption-friction details rather than feasibility: key custody on Windows-based factory
floors, rollback-counter management across silicon quirks, and secure storage on MCUs without TrustZone. All are
solvable with opinionated defaults; none is novel enough to patent. The concept can reach a usable v1 in weeks,
and its compliance-mapping artifacts (which CRA/PSTI clauses each feature satisfies) can be authored immediately
[74][76]
           .


4.5 White-Space Assessment

White space is moderate-to-high but non-patentable in kind. The gap the concept exploits — the distance
between "secure boot exists" and "a two-person team actually ships it" — is visible across practitioner literature and
open-source issue trackers [74][78]. It is not filled by patents because it is a usability/services gap; incumbents ignore
it because enterprise security vendors monetize at price points inaccessible to the long tail, and open-source
projects deliberately stop at reference code [75][80].

The thin patent zones that do exist are peripheral: factory key-provisioning workflows for secure-element-less
MCUs (compare US 11,042,609's provisioning focus, aimed at SE-equipped devices) [121], and compliance-
automation tooling (mapping firmware-update capabilities to regulatory clauses). The board should not expect a
patent moat here; the realistic protection is brand, certification-mapping content, and network effects in an
open-core model.


22

4.6 Competitive & Defensibility Analysis

Competition comes from four directions: do-it-yourself open source (MCUboot + Mender CE, free but
unopinionated) [75][80]; silicon-vendor tooling (free but single-vendor and legally non-committal); enterprise
security platforms (comprehensive, enterprise-priced); and internal security teams at larger OEMs (who will never
buy). TrustLatch's wedge is the cross-vendor long tail with a compliance deadline — precisely the customers the
first three options fail [74][76].

Defensibility: weak in patents, potentially strong in trust assets — audited reference ports, a compliance-mapping
knowledge base, signed-release provenance, and community adoption. These compound with usage and are hard
for a vendor tool to copy credibly. The strategic posture should be open-core: give away the per-MCU integrations
(maximize adoption and trust), monetize fleet key management, update operations, and compliance reporting.


4.7 Regulatory / Standards Context

This is TrustLatch's decisive advantage: it is the only portfolio concept with a hard regulatory clock. The EU
Cyber Resilience Act obligates manufacturers of products with digital elements to provide secure update
mechanisms and vulnerability handling, with penalties on turnover; the UK PSTI Act already bans universal default
passwords and requires vulnerability disclosure; US federal procurement flows through NISTIR 8259 / the IoT
Cybersecurity Improvement Act; ETSI EN 303 645 and IEC 62443 provide the harmonized technical baselines —
all converging on "secure boot + signed update capability" as table stakes [74][76]. Practitioner coverage frames
secure OTA explicitly as the compliance mechanism, not merely good hygiene [74].

Every one of these instruments converts TrustLatch's value proposition from optional to obligatory for exactly the
resource-constrained manufacturers least able to self-implement [76][77]. The regulatory pull score for this concept is
the portfolio maximum (9/10).


4.8 Risk Matrix

 Risk                                                   Likelihood   Impact        Mitigation

 Open-source      projects    ship     "good-enough"    Medium       High          Contribute               upstream;                monetize
 opinionated tooling, erasing the wedge                                                                                         [75][79]
                                                                                   operations/compliance, not the boot chain

 Silicon vendors bundle free toolkits to sell chips     Medium       High          Stay     cross-vendor;   target   multi-silicon    product
                                                                                   companies

 No patent moat → easy imitation                        High         Medium        Accept; build brand/audit/compliance assets instead

 External-RoT patent exposure if hardware dongle        Low–Med      Medium        Avoid companion-RoT hardware or license '166-
 pursued later                                                                     family [120]

 Security defect in the toolkit itself destroys trust   Low          Existential   Third-party audits, signed releases, reproducible
                                                                                   builds

 CRA enforcement slower than expected delays            Medium       Medium        Sell PSTI/NIST procurement hooks in parallel [74][76]
 urgency


23

4.9 Recommended Next Step

Advance immediately — as an open-core product, not a patent program. Ship v1 covering three MCU families
(ESP32, STM32, nRF52) with one-command provisioning, CI signing, and a CRA/PSTI compliance-mapping
whitepaper; price fleet key management and update operations as SaaS. Do not spend on filings beyond trademark.
Use VibeGuard-style connected-sensor products as first design partners — the portfolio's own concepts are
reference customers [74][75].


4.10 Key Patent & Prior-Art Table

 Document                Year        Holder / type             Content                                          Status & relevance

 US 9,953,166            2018        Microsemi/Microchip-      External secure RoT boots non-secure             Active      (~2033)        —
                                     family                    processors; challenge–response MAC +             constrains     hardware-
                                                               PUF binding [120]                                RoT variants

 US 10,740,084           2020        Major SoC vendor          In-SoC              immutable              RoT   Active — rich-platform
                                                               authenticates/applies firmware updates;          fence
                                                                          [119]
                                                               recovery

 US 11,042,609           2021        Industrial assignee       Secure-element registration & deferred           Active — provisioning
                                                                                          [121]                 fence
                                                               PKI provisioning for IoT

 US 8,589,302 / US       2013/2016   PC-industry assignees     Secure boot / firmware update [82]               PC/server-oriented
 9,483,246

 US 10,839,080           2020        —                         Hardware-enforced firmware security [82]         Active — platform fence

 MCUboot (docs +         2016–       Linux Foundation          Open secure bootloader, signing, slots,          Free — the toolkit's
 repo)                                                         rollback [75][79]                                substrate

 Mender      (repo   +   2016–       Northern.tech             Open-core OTA update server [80][81]             Free core — business-
 SaaS)                                                                                                          model template

 MCU      secure-boot    2020–       Academic                  Constrained-device boot frameworks [76][7        Non-patent prior art
 academic                2025                                  7]

 frameworks


4.11 Commercial & OSS Landscape Table

 Player                                           Layer                               Model                                    Evidence

 MCUboot / Zephyr                                 Bootloader                          Open source (Linux Foundation)           [75][78][79]


 Mender                                           OTA server                          Open core + SaaS                         [80][81]


 RAUC / SWUpdate / hawkBit                        Linux-class OTA                     Open source                              [74]


 Silicon vendors (ESP, ST, NXP, Microchip)        ROM boot + vendor tools             Free with silicon                        [74][120]


 Secure-element/PKI provisioning vendors          RoT hardware + provisioning         Per-unit + service                       [121][83]


24

 Enterprise security platforms            End-to-end device security             Enterprise license         [82]


4.12 Confidence Score & Evidence Gaps

Confidence: 8/10. The open-source substrate, the compliance calendar, and the three anchor patents were all
verified at primary-source level; the "usability gap" premise is corroborated across practitioner and academic
sources [74][75][76][120].

Evidence gaps: (1) CRA delegated-act details (exact product-scope thresholds and dates) were not re-verified this
pass and should be pinned before go-to-market claims; (2) Mender's current pricing/ARPU is inferred from its
model, not from financials [81]; (3) no measured baseline exists for "weeks-to-hours" integration effort — the core
value metric needs a benchmark study; (4) the '166 patent family continuations (Microchip) should be enumerated
if any hardware-RoT roadmap emerges [120].


25

5. ColdTrace — Multi-Modal Cold-Chain Integrity Logger

5.1 Problem Summary

Temperature-sensitive products — vaccines first among them — are damaged by both heat and freezing during
storage and transport, and the damage is often invisible at the point of care. A systematic literature review found
freezing exposure in 14–35% of vaccine shipments studied, with the problem persisting in a 2018 follow-up
review [93][95][97]; WHO immunization guidance and industry whitepapers treat excursion management as a core
cold-chain discipline [100][92]. The monitoring status quo has two failure modes that Phase 1C targeted. First, alarm
fatigue: loggers that record air temperature inside a shipper alarm on every door opening or defrost cycle because
air responds in seconds while the product's thermal mass moves in hours — pharmacy and vaccine-monitoring
guidance consequently recommends buffered probes that approximate product temperature [90][91][96][98]. Second,
single-modality: temperature loggers see thermal history but not handling; shock/tilt indicators see handling but
not potency-relevant thermal dose — and vibration/handling stress matters for sensitive biologics and food quality
alike [102][103].

ColdTrace, as framed in Phase 1C, is a multi-modal logger — temperature modeled against product (not air)
response, plus shock/tilt/light context — delivering excursion classification ("harmless door opening" vs "product-
threatening event") rather than raw threshold alarms. The evidence for need is strong and programmatic
(WHO/CDC/GDP), not merely anecdotal [93][100][92].


5.2 Commercial Ecosystem Scan

The incumbent stack is layered and surprisingly cheap at the bottom: chemical time-temperature indicators (TTIs)
and vaccine vial monitors cost cents-to-dollars per unit and are mandated on many vaccine shipments [116]; single-
use USB/PDF loggers and 30-day electronic temperature recorders serve shipment and storage roles [88][96];
reusable multi-use loggers and pharmacy monitoring systems serve the CDC VFC-program storage segment, where
                                                     [96][98]
buffered       probes   are   standard    practice              .   Condition-indicator   specialists   —   SpotSee
(ShockWatch/ShockLog/SpotBot brands) — sell shock, tilt, and temperature indicators as parallel product families
across pharma, food, and electronics logistics [102][103][104], and real-time cellular trackers occupy the premium
pallet tier [88].

The structural gap: each layer answers a different question (Was it ever too hot? Was it dropped? What is the
temperature now?), and none answers ColdTrace's question — "did this specific excursion actually threaten the
product, and what should I do?" — at commodity prices. Excursion intelligence exists today only inside expensive
real-time platforms or as human interpretation of downloaded traces [91][98]. The gap is real, but the patent scan
below shows two active fences around the most obvious implementations.


5.3 Patent & Prior-Art Landscape

Read at full text, four documents define the terrain. US 7,102,526 — "Electronic time-temperature indicator and
logger" (2003 priority): the canonical stability-bank algorithm, integrating temperature-dependent degradation
P(T) against a budget F to compute remaining shelf life, with explicit discussion of non-Arrhenius profiles, freeze


26

damage, and phase-transition penalties; it also surveys the chemical TTI art (3M MonitorMark US 5,667,303;
TempTime Heatmarker) and the Sensitech TagAlert alarm (US RE 36,200) [116]. With 2003 effective priority, this
foundational algorithmic-TTI patent is expected expired (~2023–24) — freeing model-based excursion scoring as
a design approach [116]. US 10,887,735 — "Vaccine monitoring system" (priority 2018, granted 2021): an insulated
container with a buffered temperature sensor chamber whose buffering agent "simulates the physics that the
vaccines undergo", plus cellular alerting, 2–8 °C notification ranges, and rate-of-change logic that predicts
whether the shipment will arrive before limits are exceeded [117]. This is the single most on-point active patent
against ColdTrace: the thermal-mass/buffered-probe mechanism that solves alarm fatigue is claimed here in a
vaccine-carrier embodiment, active to roughly 2038 [117].

The surrounding result sets reinforce the picture: recent pallet/container monitoring patents (US 12,248,900; US
12,524,729 — 2024–25 filings showing continued activity), cellular cold-chain logistics families (US 10,592,849),
temperature-limit indicators (US 11,467,042), and vaccine monitoring variants (US 8,671,871) [88][89]. Conclusion:
(a) algorithmic excursion scoring is now free (expired '526) — a genuine white-space gift; (b) physical buffered-
probe implementations for vaccine carriers are fenced by '735 — ColdTrace must implement product-
temperature estimation differently (e.g., a two-sensor air+thermal-model approach — a virtual thermal mass
computed in firmware — rather than a physical buffer chamber), and obtain a formal FTO opinion on '735's claim
scope [117]; (c) multi-modal shock+temp fusion at the logger level appears in indicator-brand product lines but is
thinner in the patent record than cellular pallet tracking, suggesting room for specific fusion/claims [88][102].


5.4 Technical Prior-Art and Feasibility

Feasibility is high. The sensing set (NTC/digital temperature, MEMS accelerometer for shock/tilt, light sensor,
coin-cell or LiSOCl₂ power, local logging plus BLE/NFC readout) is commodity engineering, and the expired '526
patent supplies a complete, validated algorithmic framework — stability banking with arbitrary P(T) tables — that
can be implemented in a few hundred lines of firmware [116]. The alarm-fatigue solution has two technical routes
with different IP exposure: the physical buffered probe (standard pharmacy practice [96][98], but fenced for vaccine
carriers by '735 [117]) versus a virtual thermal mass — estimating product temperature from air-temperature
dynamics via a first-order thermal model, computable on any MCU. The virtual route is standard control-systems
engineering and, on this record, does not appear claimed for the excursion-classification use-case.

The differentiating intelligence — classifying excursions by integrating thermal dose, rate-of-change, shock events,
and lid-open (light) events into an actionable verdict — is an embedded-analytics problem with no physics barrier.
Feasibility risk is mostly product: hitting 30–60-day battery life, unit-cost targets competitive with single-use
loggers, and regulatory documentation (21 CFR Part 11-style records) that pharma customers demand [98][90].


5.5 White-Space Assessment

White space is moderate, and newly improved by an expiry. Open zones: (a) virtual-thermal-mass excursion
classification — model-based product-temperature estimation with multi-modal context, distinct from '735's
physical buffer [117]; (b) the expired stability-bank algorithm as a free algorithmic base for potency-aware scoring [1
16]
      ; (c) low-cost multi-modal fusion (temperature + shock + light) positioned below real-time cellular trackers — a
price/feature tier the indicator brands (discrete, single-modality) and tracker platforms (expensive, subscription)


27

both miss [102][88]. Closed or fenced zones: physical buffered-chamber vaccine carriers ('735) [117]; cellular real-time
pallet logistics (dense, active) [88]; chemical TTI chemistry (3M/TempTime families) [116].

The white-space verdict: pursue the intelligence layer (classification, virtual mass, fusion) at commodity hardware
prices; avoid claiming buffered probes and avoid the cellular-tracker business.


5.6 Competitive & Defensibility Analysis

Competitors by layer: chemical TTI/VVM suppliers (cents per unit, mandated — coexistence, not competition);
single-use logger brands (DeltaTrak/Sensitech-class) and pharmacy monitoring systems serving VFC storage [96][8
8]
     ; SpotSee's indicator families on the shock/condition side [102][104]; and real-time tracker platforms above.
ColdTrace's wedge is the interpretation gap between these layers: it sells fewer false alarms and a defensible
disposition record.

Defensibility: one possible narrow patent position exists — the specific multi-modal excursion-classification
method (virtual thermal mass + shock/light context + stability scoring) — subject to FTO review against '735 and
the indicator-brand portfolios [117][102]. Stronger protection is again evidentiary: published false-alarm-reduction
benchmarks against standard air-temperature loggers would be a marketable, hard-to-copy asset, and 21 CFR Part
11-style audit trails create switching costs in pharma accounts [98][90].


5.7 Regulatory / Standards Context

Demand-side regulation is strong and specific. WHO Performance, Quality and Safety (PQS) specifications govern
vaccine cold-chain devices; CDC's Vaccines for Children program requires calibrated continuous temperature
monitoring with buffered probes in storage units [96][98]; WHO immunization handbooks operationalize excursion
handling [100]; EU GDP and 21 CFR Part 11 frame pharma distribution records and electronic data integrity; FSMA
covers food. Freezing — the under-recognized killer — is explicitly documented by the WHO-cited systematic
review at 14–35% shipment exposure [93][95].

These frameworks do not mandate ColdTrace's multi-modal classification, but they (i) mandate the monitoring
layer it attaches to, (ii) increasingly demand defensible excursion disposition (exactly the product), and (iii) the
VFC buffered-probe norm validates the product-temperature logic at the concept's core [96][98]. Regulatory pull:
8/10 — second only to TrustLatch.


5.8 Risk Matrix

 Risk                                                  Likelihood   Impact   Mitigation

 US 10,887,735 claims read onto buffered/thermal-      Medium–      High     Use virtual (model-based) thermal mass; formal FTO
 mass implementation                                   High                  opinion pre-launch [117]

 Incumbent     logger      brands   add   excursion-   Medium       High     Ship benchmark data fast; lock pharma accounts with
 classification firmware                                                     audit-trail feature

 Price floor set by single-use loggers compresses      High         Medium   Multi-use design + service record; target storage +
 margin                                                                      last-mile, not single-use freight


28

 Validation burden (multi-product stability          Medium      Medium          Start with 2–8 °C vaccine profile + one food profile using
 tables) slows launch                                                            published stability data [116][93]

 Regulatory documentation underestimated             Medium      High            Budget compliance engineering from day one [98]
 (Part 11, PQS)

 Chemical TTI/VVM incumbency at vial level           Low–        Low             Position at shipper/storage level, complementary to VVM [116]
                                                     Med


5.9 Recommended Next Step

Advance with conditions. Proceed to Phase 3 prototype on the virtual-thermal-mass + multi-modal classification
architecture, gated on (i) a formal FTO opinion on US 10,887,735 and the indicator-brand portfolios, and (ii) a
bench validation showing false-alarm reduction versus an air-temperature logger on standardized door-
opening/defrost profiles [91][96]. File narrowly on the classification method if FTO clears; anchor go-to-market on
VFC storage monitoring and vaccine last-mile carriers where freezing risk (14–35% exposure) is documented [93][9
6]
     .


5.10 Key Patent & Prior-Art Table

 Document                     Year         Holder / type       Content                                                        Status & relevance

 US 7,102,526                 2006 (2003   TTI algorithm       Electronic TTI/logger with stability-bank P(T)                 Expected expired —
                              priority)                                                                               [116]   free algorithmic base
                                                               model; surveys 3M/TempTime/Sensitech art

 US       RE        36,200    reissue      Sensitech           Threshold temperature alarm [116]                              Expired                —
 (Sensitech TagAlert)                                                                                                         background

 US 5,667,303 (3M             1997         3M                  Wicking chemical TTI [116]                                     Expired                —
 MonitorMark)                                                                                                                 background

 US 10,887,735                2021 (2018   Vaccine             Buffered-sensor        chamber      simulating    vaccine      Active    (~2038)      —
                              priority)    monitoring          thermal physics + cellular alerting + rate-of-                 primary FTO fence
                                           system                        [117]
                                                               change

 US 8,671,871                 2014         —                   Vaccine monitoring variant [89]                                Active — secondary
                                                                                                                              fence

 US 10,592,849                2020         —                   Cellular cold-chain logistics [88]                             Active — tracker tier

 US 12,248,900 / US           2024–25      —                   Pallet/container monitoring                                    Active     —        filing
 12,524,729                                                                                                                   velocity signal [88]

 Matthias      et      al.,   2007; 2018   Peer-reviewed       Freezing exposure in 14–35% of shipments [93][95]              Key demand evidence
 Vaccine                      follow-up                        [97]


5.11 Commercial Landscape Table

 Player                                      Layer                    Positioning                                                        Evidence

 Chemical TTI / VVM suppliers                Vial/unit level          Cents-per-unit, mandated on many shipments                         [116]


29

 Single-use & 30-day loggers (DeltaTrak/Sensitech-   Shipment level        Commodity hardware                          [88][96]

 class)

 Pharmacy/VFC monitoring systems                     Storage level         Buffered probes standard; compliance-       [96][98][90]

                                                                           driven

 SpotSee (ShockWatch/ShockLog/SpotBot)               Condition             Shock/tilt/temperature indicator families   [102][103][10

                                                     indicators                                                        4]


 Real-time cellular trackers                         Premium pallet tier   Hardware + subscription                     [88]


 SenseAnywhere-type guidance vendors                 Excursion practice    Alarm-fatigue discourse validates need      [91]


5.12 Confidence Score & Evidence Gaps

Confidence: 7/10. The two decisive patents ('526 expired base, '735 active fence) were read in full; the freezing-
exposure statistics come from the canonical peer-reviewed review; the buffered-probe norm is documented across
CDC-facing guidance [116][117][93][96].

Evidence gaps: (1) '735's continuation family and any design-around case law not reviewed — requires counsel; (2)
unit economics of single-use loggers (true street prices) were not retrievable this pass, so the price-tier gap is
characterized qualitatively; (3) shock-damage dose-response data for specific vaccines/foods is thin in open
literature, weakening the multi-modal value claim quantitatively; (4) WHO PQS device-category specifics (E006)
should be pinned before regulatory marketing claims [100].


30

6. Comparative Portfolio Analysis

6.1 Cross-Concept Evidence Matrix

The table below aggregates the twelve-section findings into one decision surface. "Free base" identifies lapsed
patents each concept may build on; "Active fence" names the document most likely to require design-around or
licensing.

 Dimension              OpenBraille                      VibeGuard                         TrueMoist               TrustLatch                    ColdTrace

 Incumbent price        $3.5k–15k        displays        Enterprise-tier           PdM     Research-grade          Weeks of         specialist   False    alarms      /
 pain                   [2]                                         [43]                   probes      premium              [74]                                     [9
                                                         pricing                                                   effort                        freezing losses
                                                                                           [59]                                                  1][93]


 Disruption proof       Orbit $449; Braille              Infinite Uptime $35M              CropX         venture   Mender SaaS model [8          VFC          buffered-
                                        [107][110]               [56]                                 [71]
 in market              Me $515.50                       raise                             traction                0]                            probe norm [96]

 Free            base   SMA '721, EAP '063               Navy           '349      (near    '179, '104, '620        MCUboot/TF-M                  Stability-bank
                        [27][26]                                    [118]                             [114]                  [75]
 (expired art)                                           expiry)                           (~2028)                 (open)                        '526 [116]

 Active fence           Dot        estate;        US     Dense          platform       +   US 11,598,743 [11       US               9,953,166    US 10,887,735 [11
                                       [19][29]                             [46][47]                                                   [120]
                        11,410,574                       CNN filings                       5]                      (hardware only)               7]


 Patent saturation      Moderate                         High                              Moderate                Moderate (mis-aimed)          Moderate–High

 White space            Moderate–High                    Low                               Low–Moderate            Moderate–High (non-           Moderate
                                                                                                                   patent)

 Feasibility            High            (market-         High                              Moderate–High           Highest                       High
                        proven)                          (undifferentiated)

 Regulatory pull        7/10                             4/10                              5/10                    9/10                          8/10

 Defensibility          Mechanism                    +   Deployment                        Validation data +       Brand/community               Narrow method +
 path                   manufacturing IP                 economics only                    trade secret            (open-core)                   benchmark data

 Confidence             8/10                             7/10                              7/10                    8/10                          7/10


6.2 Portfolio Maps

Figure 1 plots each concept on patent saturation versus white-space opportunity; Figure 2 shows the six-dimension
score profile; Figure 3 anchors the OpenBraille analysis in verified market prices — the strongest single piece of
evidence in the portfolio that a 5–10× price disruption is executable.


31

Figure 1. Patent saturation vs. white-space opportunity for the five concepts (analyst scores; bubble size = composite).


Figure 2. Six-dimension radar comparison (analyst scores, 0–10).


32

Figure 3. Refreshable braille display price ladder (log scale) — verified street prices against the incumbent band.


6.3 Scoring Rationale

Scores are equal-weighted across six dimensions (patent white space, commercial headroom, technical feasibility,
defensibility potential, regulatory/demand pull, evidence confidence), each on a 0–10 ordinal scale justified in the
concept chapters. OpenBraille (7.0) wins on the combination of a verified $449 market proof against a $3.5k–15k
incumbent band, an expired mechanism base to build on, and identifiable residual novelty in manufacturing
methods [107][2][27]. TrustLatch (6.8) scores highest on feasibility and regulatory pull but is structurally capped on
defensibility — its ranking reflects a product opportunity, not an IP opportunity [75][74]. ColdTrace (6.3) would rank
second on need alone (documented 14–35% freezing exposure) but carries the portfolio's single sharpest active-
patent fence [93][117]. TrueMoist (5.5) has a real problem with partially fenced solutions and an unproven core
                         [115][65]
performance claim                    . VibeGuard (5.0) combines the highest patent saturation with the weakest
differentiation — strong technology, wrong battlefield [46][118].

Sensitivity: the ranking of the top two is stable (both lead by ≥0.5 over third place under any plausible weighting);
ColdTrace and TrustLatch swap positions if defensibility is weighted above regulatory pull; TrueMoist rises above
ColdTrace only if calibration-free field performance validates.


33

7. Final Ranking & Portfolio Recommendations

 Rank   Concept       Composite   Decision                           First gate

 1      OpenBraille   7.0         Advance — patent-track prototype   10⁷-cycle endurance + dot-force parity at <$15 cell cost

 2      TrustLatch    6.8         Advance — open-core product, no    v1 on 3 MCU families + compliance whitepaper
                                  filings

 3      ColdTrace     6.3         Conditional advance                FTO opinion on US 10,887,735 + bench false-alarm
                                                                     benchmark [117]

 4      TrueMoist     5.5         Hold                               Two-season, three-soil validation of self-correction

 5      VibeGuard     5.0         Demote                             Re-scope to niche or exit


Three portfolio-level recommendations. First, sequence the two advances in parallel: OpenBraille consumes
hardware-engineering resources, TrustLatch consumes firmware/community resources — they do not contend, and
TrustLatch's compliance whitepaper doubles as the security foundation for every connected product this pipeline
may ship. Second, run ColdTrace's FTO review immediately, because its result determines whether the concept
is third or drops below TrueMoist: if '735's claims reach virtual thermal-mass estimation, the concept's
differentiation collapses into a commodity-logger play [117]. Third, harvest VibeGuard rather than killing it
outright: its security requirements make it TrustLatch's first internal design partner, and its field-trial data on
single-node attribution would be a publishable benchmark with option value.


34

8. Evidence Gaps & Phase 3 Hooks

The highest-value evidence gaps, in priority order: (1) Claim-charting of Dot Incorporation's actuator estate
(blocks OpenBraille multiline work) and of US 10,887,735 (blocks ColdTrace's architecture choice) — both are
counsel-level tasks that should be commissioned before Phase 3 spending [19][117]. (2) InPASS and CNIPA
coverage — Indian and Chinese filings in braille cells, soil sensors, and vibration diagnostics were outside this
pass; given that two key competitors (Innovision, Infinite Uptime) are Indian and the CNN-diagnosis filing tail is
largely Chinese, this gap is material to three of five concepts [34][54][46]. (3) Unit economics — Orbit/Braille Me cell
costs, single-use logger street prices, and CropX/Sensoterra per-point pricing are inferred rather than measured [110]
[88][71]
           . (4) Performance benchmarks that do not yet exist anywhere: calibration-free multi-season soil accuracy,
single-node vibration attribution in dense shops, and virtual-thermal-mass false-alarm reduction — each is a Phase
3 experiment whose result, positive or negative, is decision-grade [65][48][91].

Phase 3 should therefore open with two parallel tracks: a legal track (claim charts, InPASS/CNIPA sweep, FTO
opinions on the two named fences) and an engineering track (OpenBraille endurance gate, TrustLatch v1,
ColdTrace bench benchmark). The Phase 2 verdict for the board: advance OpenBraille and TrustLatch now, gate
ColdTrace on counsel, hold TrueMoist for field data, and demote VibeGuard to harvest status.

This report is for general informational and internal decision-support purposes only. It does not constitute legal
advice, a freedom-to-operate opinion, or a patentability determination; patent status and expiry estimates must be
verified by qualified counsel before reliance.


35

Annex A — References

Bracketed numbers in the text correspond to the sources below. Patent records were consulted at full-text level via the
FreePatentsOnline mirror of USPTO publications. Result-set entries represent screened candidate-document lists; individually read
documents are marked “full text.”

[1] "This $500 Tablet Brings Words to Blind Users’ Fingertips," MIT Technology Review (2017).
        https://www.technologyreview.com/2017/01/12/243813/this-500-tablet-brings-words-to-blind-users-fingertips/
[2] "Refreshable Braille Displays," American Foundation for the Blind (AFB) product guide. https://afb.org/blindness-and-low-vision/using-
        technology/assistive-technology-products/refreshable-braille
[3] "Text to Braille Scanner with Ultra Low Cost Refreshable Braille Display," ResearchGate.
        https://www.researchgate.net/publication/330246078_Text_to_Braille_Scanner_with_Ultra_Low_Cost_Refreshable_Braille_Display
[4] "Low-Cost Solution for Accessible Braille Displays," ISEF project EBED033T. https://isef.net/project/ebed033t-low-cost-solution-for-
        accessible-braille-displays
[5] "BLITAB: Android Tablet with 14-Row Braille Display," Perkins School for the Blind. https://www.perkins.org/resource/blitab-android-tablet-
        14-row-braille-display/
[6] Braille display design entry, Create the Future Design Contest (Tech Briefs, 2020). https://contest.techbriefs.com/2020/entries/consumer-
        product-design/10450
[8] Community discussion of braille display pricing, Reddit r/Blind. https://www.reddit.com/r/Blind/comments/1jztglk/expensive/
[9] "Affordable Braille Displays," Foundation for Blind Children. https://seeitourway.org/affordable-braille-displays/
[11] Low-cost piezoelectric braille display analysis, JIC 2024 poster (Mehta, Y.).
        https://sspcdn.blob.core.windows.net/files/Documents/SEP/JIC/2024/Posters/2024_JIC_Mehta_Yash_Poster.pdf
[14] "Spotlighting Multi-Line Displays," AFB AccessWorld. https://afb.org/blog/entry/spotlighting-multi-line-displays
[15] HumanWare Monarch product listing, Sterling Adaptives. https://sterlingadaptives.com/products/humanware-monarch?
        srsltid=AfmBOooSVqGySaj9Y7Gl41BlmDaw09JElL9X4vWAXyEPjXxzjdvE5prU
[16] "Innovative Dot Pad from South Korea Makes Images Touchable," Branding in Asia. https://www.brandinginasia.com/innovative-dot-pad-
        from-south-korea-makes-images-touchable-for-the-visually-impaired/
[17] "Dot Pad Picks Up Fast Company World-Changing Idea Accolade," LBBOnline. https://lbbonline.com/news/dot-pad-picks-up-fast-company-
        world-changing-idea-accolade
[19] Dot Pad X product page, Dot Incorporation. https://www.dotincorp.com/en/product/dotpadx
[20] Monarch product page, American Printing House (APH). https://www.aph.org/product/monarch/
[21] Pin-array product architecture survey, ACM Trans. on Computer-Human Interaction (DOI 10.1145/3626468).
        https://dl.acm.org/doi/pdf/10.1145/3626468
[22] Multi-line tactile graphics display discussion, AppleVis forum. https://www.applevis.com/forum/assistive-technology/discussion-about-top-
        multi-line-tactile-graphics-displays-out-there
[25] US patent result set: "refreshable braille display actuator," FreePatentsOnline. https://www.freepatentsonline.com/result.html?
        query_txt=refreshable+braille+display+actuator&submit=&patents_us=on
[26] US 6,881,063 — Electroactive polymer actuator braille cell (full text, FreePatentsOnline). https://www.freepatentsonline.com/6881063.html
[27] US 5,685,721 — Refreshable braille-cell display implemented with shape memory alloys (full text).
        https://www.freepatentsonline.com/5685721.html
[28] US 2024/0363022 A1 — Refreshable braille display system (full text). https://www.freepatentsonline.com/y2024/0363022.html
[29] US 11,410,574 — Layered electromagnetic braille display (full text, FreePatentsOnline). https://www.freepatentsonline.com/11410574.html
[33] "Ultra-Low-Cost, Low-Power, High-Speed Electronic Braille Device," M.Z.A. Mia. https://zesun33.github.io/assets/pdf/Ultra-Low-Cost-Low-
        Power-High-Speed-Electronic-Braille-Device-for-Visually-Impaired-People-preprint.pdf
[34] Braille Me technology page, National Braille Press (NBP). https://www.nbp.org/ic/nbp/technology/brailleme.html?from_search=1
[36] "Bristol Braille Canute Multi-Line Refreshable Braille Display," Perkins. https://www.perkins.org/resource/bristol-braille-canute-multi-line-
        refreshable-braille/
[37] "Canute Scientific," Crowd Supply. https://www.crowdsupply.com/bristol-braille-technology/canute-scientific


36

[38] "Canute: the world’s first working refreshable multiline braille display," EMF2016 talk, media.ccc.de. https://media.ccc.de/v/emf2016-176-
        canute-the-worlds-first-working-refreshable-multiline-braille-display
[39] "About Canute," Bristol Braille Technology. https://bristolbraille.org/about-canute/
[42] Journal of Vibration (MDPI) — vibration engineering research index. https://www.mdpi.com/journal/vibration
[43] Augury corporate site — machine and process health platform. https://www.augury.com/
[44] Augury — About page. https://www.augury.com/about/
[45] Augury peer reviews, Gartner. https://www.gartner.com/reviews/product/augury
[46] US patent result set: "vibration monitoring bearing fault diagnosis," FreePatentsOnline. https://www.freepatentsonline.com/result.html?
        query_txt=vibration+monitoring+bearing+fault+diagnosis&submit=&patents_us=on
[47] US patent result set: "predictive maintenance + vibration + edge + machine learning," FreePatentsOnline.
        https://www.freepatentsonline.com/result.html?
        query_txt=%22predictive+maintenance%22+vibration+edge+machine+learning&submit=&patents_us=on
[48] Noise-robust bearing fault diagnosis study, MDPI Sensors 23(4):1902. https://www.mdpi.com/1424-8220/23/4/1902
[49] Vibration/fault-diagnosis research article, Extrica. https://www.extrica.com/article/21928
[50] Condition-monitoring techniques and vendor survey, Brunel University research archive (thesis).
        https://bura.brunel.ac.uk/bitstream/2438/31919/1/FulltextThesis.pdf
[51] Tractian corporate site. https://tractian.com/en
[52] Infinite Uptime directory profile, Industrial Automation India. https://www.industrialautomationindia.in/directory/infinite-uptime
[54] "Infinite Uptime Redefines the Predictive Maintenance…" (press release), Business Standard. https://www.business-
        standard.com/content/press-releases-ani/infinite-uptime-redefines-the-predictive-maintenance-category-121042800696_1.html
[55] Infinite Uptime corporate site. https://www.infinite-uptime.com/
[56] "Infinite Uptime bags $35M…," Yahoo Finance (AU). https://au.finance.yahoo.com/news/infinite-uptime-bags-35m-help-033028049.html
[59] TEROS soil-sensor line (METER Group), teros.ai. https://teros.ai/en
[60] teros.dev — https://teros.dev/. https://teros.dev/
[63] Salinity/temperature effects on capacitive soil-moisture sensors, SciELO – Revista Caatinga.
        https://www.scielo.br/j/rca/a/XhFvbZGrWy7Z4NYGWMK9hRn/?lang=en
[64] Soil-moisture sensor temperature/salinity study, MDPI Sensors 20(24):7041. https://www.mdpi.com/1424-8220/20/24/7041
[65] Soil-moisture sensing review, JSAN 13(1):32 (HAL open archive). https://hal.science/hal-04873514v1/file/jsan-13-00032.pdf
[66] Capacitive soil-sensor evaluation study, PMC11478466. https://pmc.ncbi.nlm.nih.gov/articles/PMC11478466/
[68] US patent result set: "soil moisture sensor temperature compensation salinity," FreePatentsOnline.
        https://www.freepatentsonline.com/result.html?
        query_txt=soil+moisture+sensor+temperature+compensation+salinity&submit=&patents_us=on
[69] US patent result set: "soil moisture sensor calibration correction conductivity," FreePatentsOnline.
        https://www.freepatentsonline.com/result.html?
        query_txt=soil+moisture+sensor+calibration+correction+conductivity&submit=&patents_us=on
[70] CropX corporate site. https://cropx.com/
[71] CropX profile, Crunchbase. https://www.crunchbase.com/organization/cropx
[74] "Secure OTA Updates & IoT Firmware," Platanor Technologies. https://www.platanor.com/blog/secure-ota-updates-iot-firmware
[75] MCUboot documentation (docs.mcuboot.com). https://docs.mcuboot.com/
[76] IoT device security / secure-boot study, PMC12987191. https://pmc.ncbi.nlm.nih.gov/articles/PMC12987191/
[77] Secure boot on constrained devices, BME CrySyS thesis. https://static.crysys.hu/publications/files/setit/thesis_bme_Gedeon20bsc.pdf
[78] "MCUboot: Secure Boot in Zephyr," DEV Community. https://dev.to/ripan030/mcuboot-secure-boot-in-zephyr-4aoi
[79] GitHub — mcu-tools/mcuboot. https://github.com/mcu-tools/mcuboot
[80] GitHub — mendersoftware/mender. https://github.com/mendersoftware/mender
[81] Mender.io — OTA update platform. https://mender.io/
[82] US patent result set: "secure boot firmware update microcontroller root of trust," FreePatentsOnline.
        https://www.freepatentsonline.com/result.html?
        query_txt=secure+boot+firmware+update+microcontroller+root+of+trust&submit=&patents_us=on


37

[83] US patent result set: "key provisioning microcontroller secure element IoT," FreePatentsOnline.
       https://www.freepatentsonline.com/result.html?
       query_txt=key+provisioning+microcontroller+secure+element+IoT&submit=&patents_us=on
[88] US patent result set: "cold chain temperature monitoring excursion logger," FreePatentsOnline. https://www.freepatentsonline.com/result.html?
       query_txt=cold+chain+temperature+monitoring+excursion+logger&submit=&patents_us=on
[89] US patent result set: "vaccine temperature monitoring time temperature indicator," FreePatentsOnline.
       https://www.freepatentsonline.com/result.html?
       query_txt=vaccine+temperature+monitoring+time+temperature+indicator&submit=&patents_us=on
[90] "Pharmacy Temperature Monitoring," Envigilance. https://envigilance.com/blog/pharmacy-temperature-monitoring/
[91] "How Do You Detect a Cold-Chain Excursion Quickly?," SenseAnywhere. https://www.senseanywhere.com/how-do-you-detect-a-cold-chain-
       excursion-quickly/
[92] "The Tip of the Iceberg" — economic analysis of cold-chain losses, IQVIA EMEA whitepaper.
       https://www.iqvia.com/-/media/iqvia/pdfs/emea/library/whitepaper/tip-of-the-iceberg-economic-and-environmental-impact-of-the-vaccine-
       cold-chain.pdf
[93] Matthias et al., "Freezing temperatures in the vaccine cold chain: a systematic literature review," Vaccine (2007) — PubMed record.
       https://pubmed.ncbi.nlm.nih.gov/17382434/
[95] Matthias et al., Vaccine (2007) — ScienceDirect record. https://www.sciencedirect.com/science/article/abs/pii/S0264410X07002289
[96] "VFC Data Loggers & Vaccine Temperature Monitoring," Plumsense. https://www.plumsense.com/vfc-data-loggers-vaccine-temperature-
       monitoring/
[97] Follow-up review on freezing exposure in the vaccine cold chain, Vaccine (2017/18) — ScienceDirect.
       https://www.sciencedirect.com/science/article/pii/S0264410X16309471
[98] "Vaccine Temperature Monitoring Best Practices," Dickson Data. https://dicksondata.com/vaccine-temperature-monitoring-best-practices?
       srsltid=AfmBOoo5iuJKeEqiMqB4VIP9Zkk3sABM6BLpob_JV2TWzNSwEDP2rVkl
[100] Immunization Handbook, WHO (India SEARO). https://cdn.who.int/media/docs/default-source/searo/india/publications/immunization-
       handbook-107-198-part2.pdf
[102] SpotSee corporate site — ShockWatch/ShockLog/SpotBot condition indicators. https://spotsee.io/?
       srsltid=AfmBOorJnZYBWuIn2rmJc5yOdeh4_79WffstH3on5b7I0gU1-Er1Z0B9
[103] SpotSee manufacturer page, Mouser Electronics. https://www.mouser.hk/manufacturer/spotsee/?
       srsltid=AfmBOopVSpaCGDzn17dWrvKyheTT8pasg9tju7X6u-dp5_lxDBRYq7D4
[104] SpotSee supplier center, Digi-Key Electronics. https://www.digikey.com/en/supplier-centers/spotsee
[107] Orbit Reader 20 review, AFB AccessWorld (afb.org/aw/19/1/15167). https://afb.org/aw/19/1/15167
[108] "Orbit Reader 20: The Most Inexpensive Braille Display," National Federation of the Blind. https://nfb.org/orbit-reader-20-most-inexpensive-
       braille-display
[109] Orbit Reader / Transforming Braille Group page, RNIB. https://www.rnib.org.uk/living-with-sight-loss/assistive-aids-and-
       technology/reading-and-writing/introducing-the-orbit-reader-20/
[110] "Braille Me and Orbit Reader Braille Display Comparison," Perkins School for the Blind. https://www.perkins.org/resource/braille-me-and-
       orbit-reader-braille-display-comparison/
[111] Orbit Reader 20 product page, American Printing House (tech.aph.org/or20). https://tech.aph.org/or20/
[112] Orbit Reader 20 Plus listing, A.T. Guys. https://atguys.com/products/orbit-reader-20-plus-braille-display-book-reader-and-note-taker?
       srsltid=AfmBOoonI2XdtKbAGe3N9bE8whj9mZlfYlMjKKt9ZY662qrxB4VDOvdZ
[113] Orbit Reader 20 listing (manufacturer description), MaxiAids. https://www.maxiaids.com/product/orbit-reader-20
[114] US 7,884,620 — Sensor for measuring moisture and salinity (full text, FreePatentsOnline). https://www.freepatentsonline.com/7884620.html
[115] US 11,598,743 — Soil monitoring sensor including single probe and temperature compensation (full text).
       https://www.freepatentsonline.com/11598743.html
[116] US 7,102,526 — Electronic time-temperature indicator and logger (full text). https://www.freepatentsonline.com/7102526.html
[117] US 10,887,735 — Vaccine monitoring system (full text). https://www.freepatentsonline.com/10887735.html
[118] US 7,421,349 — Bearing fault signature detection (full text). https://www.freepatentsonline.com/7421349.html
[119] US 10,740,084 — SoC-assisted resilient boot (full text). https://www.freepatentsonline.com/10740084.html


38

[120] US 9,953,166 — Method for securely booting a target processor using a secure root of trust (full text).
        https://www.freepatentsonline.com/9953166.html
[121] US 11,042,609 — Systems and methods for secure element registration and provisioning (full text).
        https://www.freepatentsonline.com/11042609.html


39
