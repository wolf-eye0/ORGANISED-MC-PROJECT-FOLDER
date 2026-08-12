# OpenBraille Pre-Build Future Patent-Case Simulation Instructions

## Purpose

Conduct an independent pre-build hypothetical patent-case simulation for
OpenBraille alone.

This is not legal advice, a patentability opinion, claim construction,
infringement analysis, FTO clearance, filing recommendation or prediction of
patent grant.

Use fresh web research and primary patent and technical sources. Do not rely
only on the attached synthesis reports.

The future mechanisms are hypothetical and unbuilt. Do not assume that they
work.

## Authority order

1. Engineering Design Review.
2. Project mC Decision Register v1.2.
3. Final OpenBraille Architecture Report.
4. Final OpenBraille Memory.
5. Final OpenBraille SOP.
6. Uncertainty and Test Register.
7. Valid OpenBraille syntheses after reliability audit.
8. Cross-concept adjudications as decision context, not votes.
9. Fresh primary-source patent and technical verification.

## Frozen semester MVP

Preserve:

- one macro-scale six-dot Braille cell;
- six SG90-class servos;
- ESP32 local control;
- direct PWM actuation;
- one eccentric cam per dot;
- follower and guided vertically translating pin per dot;
- FDM frame, pin guides and cams;
- active cam retraction unless a physical passive return is experimentally
  proven;
- regulated external servo power;
- USB/serial character input;
- local pattern refresh and fault logging;
- single-dot-first validation;
- no moving embossing roller;
- no encoder wheel;
- no RAMPS or Arduino-Mega embosser;
- no continuous-paper system;
- no electromagnetic-actuator substitution.

Treat the frozen MVP as a strong semester prototype and Track D as a patent
target unless fresh claim-focused evidence establishes otherwise.

Do not use exact part numbers, macro scale, FDM manufacture or low price as
the invention.

## Hypothetical future invention space

Investigate later OpenBraille architectures involving materially different
combinations of:

1. a mechanically defined datum or reference state;
2. per-dot actuator calibration and bounded operating windows;
3. isolated high-bandwidth current or voltage sensing;
4. independent optical, displacement or mechanical ground truth during
   development;
5. completed, incomplete, jammed and Unknown physical-state classification;
6. bounded retry and fault isolation;
7. current-aware or power-aware sequencing;
8. remount, servo-replacement or reassembly acceptance;
9. practical Braille-scale transfer;
10. multi-dot coordinated refresh without silent wrong tactile states.

Do not assume that every feature belongs in one architecture.

Do not treat servo current, calibration, homing, retries, current limiting,
fault isolation, staggered actuation or tactile pins as novel by themselves.

## Mandatory fresh research

Search primary patent databases and primary technical literature for:

- refreshable Braille displays;
- dynamic tactile displays;
- independently actuated tactile pins;
- servo-driven tactile mechanisms;
- eccentric-cam and follower tactile mechanisms;
- guided vertical Braille pins;
- actuator homing and mechanical datum systems;
- per-channel actuator calibration;
- motor-current position, endpoint and jam detection;
- sensorless position or state estimation;
- shared or multiplexed actuator-current sensing;
- bounded retry and actuator fault isolation;
- actuator sequencing and power-rail management;
- tactile-state verification;
- practical Braille dimensions, force, protrusion and human-factor standards;
- replaceable actuator calibration;
- FDM tolerance, friction, wear and practical-scale transfer.

At minimum investigate and verify the relevance of:

- US8483018B2;
- US20130017516A1;
- US8690576B2;
- US7410359B1;
- US12080182B2;
- Freedom Scientific and Enhanced Vision tactile/Braille families;
- public servo/cam Braille projects;
- Indian application `5559/CHE/2014` and any family or successor record;
- any closer Indian, US, EP, WO/PCT, Chinese, Japanese or Korean record found
  during fresh research.

For each load-bearing patent:

- verify publication/application number;
- verify priority and family;
- verify applicant or assignee;
- read independent claims;
- separate dependent-claim and description-only disclosure;
- verify official legal status where feasible;
- distinguish prior-art relevance from FTO relevance;
- record unresolved status, translation and claim-scope limits.

Do not call FTO clear.

## Candidate architectures

Define at least five materially different future OpenBraille architectures.

They must differ in physical sensing, control or state-verification mechanism,
not merely in classifier or microcontroller choice.

At minimum assess:

1. mechanical datum plus per-dot calibration without current sensing;
2. datum plus isolated shared-current physical-state inference;
3. direct position or optical verification architecture;
4. replacement/remount acceptance and bounded recalibration;
5. coordinated low-peak-power refresh with fault isolation;
6. a reduced D11 architecture containing only indispensable elements;
7. any stronger alternative found during fresh research.

For every candidate report:

- physical technical problem;
- exact architecture and state transitions;
- permanent versus development-only sensors;
- measurable physical effect;
- closest patent art;
- closest non-patent art;
- likely single-reference novelty issue;
- strongest obviousness combination;
- US, EPO and Indian eligibility risk;
- enablement and written-description burden;
- FTO and design-around risk;
- plausible useful claim scope;
- commercially trivial narrowness risk;
- cost and compute burden;
- semester-MVP compatibility;
- future experiments;
- strongest conventional baseline;
- critical ablations;
- earliest kill condition;
- confidentiality boundary;
- preserve, redesign, test later or reject classification.

## D11-specific question

Independently determine whether a D11-type mechanism could create a
cooperative physical effect rather than aggregating known engineering steps.

The possible D11-type route may include:

- common or per-channel mechanical datum;
- per-dot calibrated minimum-drive windows;
- isolated high-bandwidth current capture;
- direct physical pin-state ground truth during development;
- completed, incomplete, jammed or Unknown classification;
- bounded retry;
- fault isolation;
- current-aware sequencing.

Do not assume that servo current reveals pin height or tactile correctness.

Test whether current merely measures internal servo effort, friction or supply
variation.

## Mandatory simulated attacks

For every surviving candidate perform:

1. anticipation attack;
2. obviousness or inventive-step attack;
3. US eligibility attack;
4. EPO technical-effect attack;
5. Indian eligibility and patentability attack;
6. enablement and written-description attack;
7. practical-scale support attack;
8. FTO and design-around attack.

Do not rebut an attack by assuming future experimental success.

State what evidence is missing.

## Claim simulation

Draft only simulation artefacts:

- one tentative apparatus independent claim;
- one tentative method independent claim;
- dependent fallback concepts.

Then attack and narrow them.

For every prospective claim element identify:

- architecture support;
- closest prior art;
- likely difference;
- physical experiment required;
- current enablement status;
- design-around possibility;
- whether narrowing destroys commercial usefulness.

Do not describe the claims as filing-ready.

## Strong baselines and ablations

At minimum compare future mechanisms against:

- fixed common PWM;
- calibrated open-loop per-dot PWM;
- datum-only control;
- current-sensing-only control;
- fixed one-at-a-time sequencing;
- current-aware sequencing without physical-state verification;
- direct per-dot position sensor oracle;
- full D11-type integrated mechanism;
- every critical feature removed individually.

Do not use an intentionally weak fixed-PWM baseline as the only comparator.

## Required physical effects

A surviving mechanism must be capable of being tested for:

- fewer incomplete raises or retractions;
- fewer silently wrong tactile states;
- reduced pin-height variation;
- lower unsafe stall exposure;
- reduced peak-current or brownout events;
- bounded recovery latency;
- robust operation across servo replacements and rebuilds;
- practical-scale transfer;
- a non-additive benefit not explained by ordinary calibration or sequencing.

## Twelve-month evidence roadmap

Cover:

- frozen semester foundation;
- single-dot observability gate;
- six-dot controlled invention phase;
- servo replacement and reassembly phase;
- voltage, friction, temperature and finger-load perturbations;
- 3,000-transition held-out silent-error test;
- practical Braille-scale coupons;
- longer lifecycle testing;
- refreshed claim-focused search;
- institutional invention disclosure;
- filing/no-filing decision;
- publication or trade-secret fallback.

## Semester design preservation

State what should be built or recorded now, including:

- exact CAD revisions;
- cam and guide dimensions;
- pin protrusion and repeatability;
- PWM command per dot;
- supply voltage and current;
- timestamped actuator commands;
- single-dot and multi-dot transition logs;
- fault and retry logs;
- servo identity and replacement history;
- reassembly/remount history;
- direct physical ground-truth method;
- cycle count and wear;
- temperature and load conditions;
- raw high-rate current data where available;
- held-out transitions;
- negative results;
- contributor chronology;
- confidential versus public-safe details.

Do not expand or destabilize the semester MVP merely to imitate a hypothetical
patent architecture.

## Forecast rules

Provide optimistic, base and pessimistic development scenarios.

These are management forecasts, not patent-grant probabilities.

For each report:

- assumptions;
- expected technical outcome;
- continuation or kill result;
- likely claim narrowness;
- additional time and cost;
- main decision-reversal fact.

Never promise patent grant.

## Required final recommendation

End with exactly one:

A. Preserve and test a named prospective invention architecture.
B. Redesign the prospective mechanism before testing.
C. Complete only the semester MVP and wait for evidence.
D. Retain OpenBraille as publication, accessibility or trade-secret
   engineering only.
E. Kill the OpenBraille patent route.

If A or B is selected, state:

- exact candidate mechanism;
- why it is better than alternatives;
- semester choices to preserve now;
- earliest decisive experiment;
- strongest baseline;
- primary kill condition;
- information impossible to know before building;
- confidentiality boundary;
- whether a later Deep Research verification lane remains necessary.

## Required report title

# OpenBraille Pre-Build Future Patent-Case Simulation

## Quality rules

- Do not promise patent grant.
- Do not infer experimental success.
- Do not count previous reports as votes.
- Do not treat the semester MVP as the invention.
- Do not substitute a moving roller or another architecture.
- Do not call generic servo calibration or current sensing novel.
- Do not call a patent active without official-status qualification.
- Do not call FTO clear.
- Do not infer invention from macro scale, FDM manufacture or low budget.
- Clearly label verified fact, source assertion, hypothesis, simulation,
  recommendation and unresolved uncertainty.
