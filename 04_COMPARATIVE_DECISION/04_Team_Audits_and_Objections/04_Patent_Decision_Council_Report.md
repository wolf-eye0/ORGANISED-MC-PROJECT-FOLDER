# Patent Decision Council Report: VibeGuard vs. OpenBraille

**Question put to the council:** Which project — VibeGuard (PBCST504 Microcontrollers) or OpenBraille — should be pursued for actual patent possibility?

**Method:** Five-advisor LLM Council (Contrarian, First-Principles, Expansionist, Outsider, Executor), each independently analyzing the two attached pre-build patent-case simulations, cross-examined, then synthesized into a chairman's verdict.

**Source documents used:**
- `VibeGuard_Pre-Build_Future_Patent-Case_Simulation.md`
- `OpenBraille_Pre-Build_Future_Patent-Case_Simulation.md`
- `VibeGuard_Semester_Implementation_and_Future_Research_Roadmap.pdf`
- `OpenBraille_Semester_Architecture_and_Future_Research_Reference_Dossier.docx`

---

## Executive Answer

**Neither project currently has a patentable invention.** Both source documents independently arrive at the identical formal recommendation — **"B: redesign the prospective mechanism before testing"** — not "file," not "abandon." Whatever patent potential exists lives entirely in each project's *unbuilt future mechanism*, not in the semester MVP.

**If forced to choose which future mechanism to keep researching toward eventual patentability: VibeGuard.** Its future PIRG mechanism currently faces a *combination* obviousness attack (several separate references would need to be stitched together by an examiner). OpenBraille's future VPD-C7 mechanism sits much closer to a single, very recent (2026) patent that nearly overlaps it. That is a materially different — and worse — risk profile for OpenBraille.

---

## 1. What each project's semester build actually is (not patentable, by design)

| | VibeGuard | OpenBraille |
|---|---|---|
| Frozen MVP | One rigid ADXL345-class accelerometer + ESP32, local RMS+persistence classifier, RGB/USB output | One macro-scale six-dot Braille cell, six SG90-class servos + cams, ESP32 direct PWM, active retraction |
| Own document's patent framing | "Not represented as a patent-ready invention" | "Track D / no-current-filing patent position" |
| Purpose of the MVP | Prove a controlled engineering hypothesis and generate evidence | Prove a controlled engineering hypothesis and generate evidence |

Both documents are explicit and consistent: the graded semester deliverable is an evidence-generation exercise, not IP. This part of the question is already settled and doesn't need a council — it's stated directly in both dossiers.

## 2. Where the real patent question lives: the future mechanisms

| | VibeGuard → **PIRG** | OpenBraille → **VPD-C7** |
|---|---|---|
| What it is | Paired-Intervention Residual Gate: two contrast subspaces built from reciprocal commissioning interventions (target changes / interferer changes), compared at runtime via dual residuals, with `Unknown` for ambiguous cases | Verified Pin-Datum Cell: an endpoint datum that both mechanically constrains pin travel *and* generates the pin-side electrical endpoint event, with current used only as independent effort evidence, never as completion proof |
| Closest prior art found | No single reference disclosing the *exact* paired-intervention/dual-residual combination. Obviousness attack must be assembled from several references (Nguyen, Seitz, Gelle, Lundgren, Oracle/Rolls-Royce, Kannan, KCF, Mitsubishi, Tractian) | US 11,455,910 B2 (motor-cam actuation + angular-position sensing) and the 2026 US 12,548,467 B2 (removable constrained Braille dots + dependent PWM/current-control) sit very close to the core idea |
| Document's own obviousness rating | "High risk and **presently the dominant patentability problem**" | "An ordinary endpoint/limit contact; moving sensing downstream to detect backlash is an evident design response" |
| Document's own enablement rating | "Severe present risk and **an independent reason not to file now**" | "Contact force/resistance, wear, debounce, safety, practical pitch, and manufacturing tolerances are unknown" |
| Executive framing | "A narrower testable architecture **may be worth preserving**" | "The fresh claim-level search makes the current patent case **weaker, not stronger**" |
| Kill conditions (either kills the patent route) | Collinear/unstable target-interference contrasts; mechanism fails to beat strongest baseline; effect needs a permanent reference sensor; ADXL345 misses the discriminating band | No advantage over a separate sensor; current adds no diagnostic value; practical-scale/lifecycle testing fails; transfer fails after replacement/reassembly; closer reference surfaces |
| Formal recommendation | **B — redesign the prospective mechanism before testing** | **B — redesign the prospective mechanism before testing** |

**Reading the gap:** both mechanisms are hypotheses with real obviousness and enablement problems. The difference is *what kind* of obviousness problem each faces. VibeGuard's requires an examiner to combine ~6 references in a reasoned chain — arguable, contestable, and exactly the kind of combination a patent attorney can push back on. OpenBraille's is closer to a two-reference read where the "inventive" step (moving sensing downstream to the pin/datum contact) is described in its own document as an "evident design response" — the kind of gap examiners close quickly, and it's made worse by a 2026 patent that's essentially adjacent to it right now, with no time for the landscape to move.

## 3. The Council

### The Contrarian
Fatal-flaw hunt: the premise of the question — "which one *has* the patent" — is false for both. Flag that plainly rather than picking a favorite by default. If a choice must be made, OpenBraille is closer to abandonment-worthy: it already concedes its own patent case got *weaker* after a fresh search, and a 2026 patent sits almost on top of the core mechanism. VibeGuard's obviousness problem is serious but still a multi-reference combination argument, which is contestable in prosecution in a way a near-identical single reference is not.

### First-Principles Thinker
Reframe the question: it isn't "VibeGuard or OpenBraille" as builds — VibeGuard is already the approved, frozen, in-progress semester project (Q1 in its own approval checklist). The actual decision on the table is which *future research thread* (PIRG or VPD-C7) deserves the 6–12 months of post-semester effort described in each roadmap. Stripped of hardware and team logistics, the only fair comparison is novelty headroom and enablement distance-to-proof — and on both counts VibeGuard's PIRG is currently better positioned.

### The Expansionist
Upside case: single-sensor multi-source vibration attribution (VibeGuard/PIRG) targets a market where funded competitors (Augury, Tractian) already prove commercial demand — if PIRG survives its own kill gate, it has real licensing/product upside beyond a patent certificate. OpenBraille's VPD-C7 is a narrower safety/verification feature bolted onto an already crowded actuator space (HumanWare, Freedom Scientific, Enhanced Vision) — even a successful result is a smaller win. Vote: VibeGuard, on upside-if-it-works grounds, not just lower obviousness risk.

### The Outsider
Fresh-eyes flag: both documents are strikingly similar in structure and conclusion (same "B" recommendation, same evidence-gate language), which is either a sign of a well-calibrated, consistent evaluation process — or a sign the process outputs the same cautious verdict regardless of the underlying idea. Worth independently sanity-checking rather than trusting either simulation as gospel. Separately: OpenBraille's assistive-tech framing is a much easier story for a teacher, grant panel, or accessibility-focused funding body than VibeGuard's more abstract sensor-fusion pitch — that's a real asset, just not a patent asset.

### The Executor
What to actually do Monday morning: nothing patent-related. Finish the frozen VibeGuard Level-1 build on the existing 12-week roadmap — that decision is already made. The patent question isn't due for 6–12 months (gates G6/G7 in the roadmap), and the correct action today is evidence preservation, not drafting or counsel spend. If forced to allocate future research hours to one mechanism now, put them on PIRG: it doesn't require rebuilding hardware from scratch the way VPD-C7's mechanical/electrical redesign does, and its earliest defining experiment (the two-machine factorial rig) is already fully specified in the VibeGuard document.

### Peer-review synthesis
**Agreement:** neither mechanism is patentable today; the correct immediate action is finishing the approved VibeGuard build, not filing anything; obviousness and enablement independently block both right now.
**Clash:** Expansionist/Executor/First-Principles favor VibeGuard on novelty-headroom and upside grounds; Outsider notes OpenBraille wins on narrative/fundability despite the weaker patent case — a real but separate axis.
**Blind spot the group corrected for:** every advisor's first pass ignored cost. A real filing needs professional prior-art search, drafting, and prosecution across jurisdictions — both documents explicitly warn against assuming a grace period or promising a grant. That cost is the same order of magnitude regardless of which idea is chosen, and dwarfs either project's semester budget (₹2,200–3,900 / macro-scale six-dot equivalent). The real gating decision is each mechanism's own kill-condition test at month 4–6, not a VibeGuard-vs-OpenBraille popularity contest today.

## 4. Verdict

Continue building VibeGuard as the semester project — that's already decided and frozen, independent of this question. For **future patent trajectory specifically**, **VibeGuard's PIRG mechanism is the stronger bet**: it faces a multi-reference combination-obviousness argument rather than a single near-identical 2026 patent, and its own document frames it as "worth preserving" rather than conceding the case got weaker after a fresh search, as OpenBraille's does. Neither is patentable today, and both require the full 10–12 month evidence, redesign, and professional-review path described in their own roadmaps before a real filing decision is even possible.

## 5. What to actually do first

Don't engage a patent attorney or draft a claim. Finish the Level-1 VibeGuard build through Week 12. Then run the earliest experiment PIRG's own document already specifies: a randomized two-machine factorial rig with one permanent target sensor and temporary synchronized references, benchmarked against the mandatory conventional baselines (RMS/persistence, FFT/bands, ordinary Mahalanobis). That single dataset — not this council, not either simulation document — is what actually decides whether PIRG survives past its month 4–6 kill gate.

---

*This report synthesizes two internal, non-exhaustive pre-build patent-case simulations. It is not a patentability opinion, freedom-to-operate clearance, or legal advice. Both source documents state this explicitly, and that caveat carries through unchanged here.*
