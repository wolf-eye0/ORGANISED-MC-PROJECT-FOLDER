# Source Extraction

- Chapter: `10` — Teacher Reviews and Presentation Record
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_HISTORICAL`
- Original source: `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/12_Presentation_Instructions_2.0.html`
- Current SHA-256: `300d2b47feb4995a5fbca41d1c475734d80075d943c14e3adb8f1fcdac1b0274`
- Extraction method: `HTML_PARSER`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

OpenBraille · Team Instruction Hub


        :root {
            --cyan: #38bdf8;
            --cyan-glow: rgba(56, 189, 248, 0.5);
            --purple: #a78bfa;
            --amber: #fbbf24;
            --pink: #f472b6;
            --teal: #2dd4bf;
            --bg-deep: #0a0f1c;
            --glass-bg: rgba(255, 255, 255, 0.03);
            --glass-border: rgba(255, 255, 255, 0.08);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-deep);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem 1.5rem;
            position: relative;
            overflow-x: hidden;
            background-image:
                radial-gradient(circle at 30% 40%, rgba(56, 189, 248, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 70% 70%, rgba(167, 139, 250, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 20% 85%, rgba(244, 114, 182, 0.08) 0%, transparent 45%);
            animation: bgShift 14s ease-in-out infinite alternate;
        }

        @keyframes bgShift {
            0% {
                background-position: 0% 0%, 100% 100%, 0% 100%;
            }
            100% {
                background-position: 20% 10%, 80% 90%, 30% 80%;
            }
        }

        /* floating animated blobs */
        .floating-blobs {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }
        .blob {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.25;
            animation: floatBlob 18s infinite ease-in-out;
        }
        .blob1 {
            width: 350px;
            height: 350px;
            background: #38bdf8;
            top: 10%;
            left: 10%;
            animation-delay: 0s;
        }
        .blob2 {
            width: 280px;
            height: 280px;
            background: #a78bfa;
            bottom: 20%;
            right: 15%;
            animation-delay: -5s;
        }
        .blob3 {
            width: 400px;
            height: 400px;
            background: #f472b6;
            top: 50%;
            left: 60%;
            animation-delay: -9s;
        }
        @keyframes floatBlob {
            0%, 100% {
                transform: translate(0, 0) scale(1);
            }
            33% {
                transform: translate(40px, -30px) scale(1.08);
            }
            66% {
                transform: translate(-20px, 50px) scale(0.94);
            }
        }

        .container {
            position: relative;
            z-index: 2;
            width: 100%;
            max-width: 1200px;
            background: rgba(18, 24, 40, 0.45);
            backdrop-filter: blur(28px);
            -webkit-backdrop-filter: blur(28px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 3.5rem;
            box-shadow: 0 35px 70px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.06),
                0 0 40px rgba(56, 189, 248, 0.15);
            padding: 2.8rem 2.5rem 2.5rem;
            transition: all 0.3s ease;
            animation: containerPulse 6s ease-in-out infinite alternate;
        }
        @keyframes containerPulse {
            0% {
                box-shadow: 0 35px 70px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.06), 0 0 40px rgba(56, 189, 248, 0.12);
            }
            100% {
                box-shadow: 0 35px 70px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.06), 0 0 60px rgba(167, 139, 250, 0.25);
            }
        }

        h1 {
            font-size: 2.7rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            text-align: center;
            margin-bottom: 0.2rem;
            background: linear-gradient(135deg, #bae6fd, #c4b5fd, #fbcfe8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            filter: drop-shadow(0 4px 10px rgba(0,0,0,0.5));
            word-break: break-word;
        }

        .subtitle {
            text-align: center;
            color: rgba(255, 255, 255, 0.6);
            font-weight: 400;
            font-size: 1rem;
            margin-bottom: 2.5rem;
            letter-spacing: 0.03em;
        }

        .tabs {
            display: flex;
            justify-content: center;
            gap: 0.9rem;
            flex-wrap: wrap;
            margin-bottom: 2.8rem;
        }

        .tab-btn {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border: 1.5px solid rgba(255, 255, 255, 0.12);
            border-radius: 3rem;
            padding: 0.9rem 2.2rem;
            font-size: 1rem;
            font-weight: 600;
            color: rgba(255, 255, 255, 0.7);
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.23, 1, 0.32, 1);
            letter-spacing: 0.02em;
            white-space: nowrap;
            position: relative;
            overflow: hidden;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.35);
        }

        .tab-btn::before {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.25), transparent 70%);
            opacity: 0;
            transition: opacity 0.4s;
        }

        .tab-btn:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(255, 255, 255, 0.4);
            color: white;
            transform: translateY(-3px);
            box-shadow: 0 16px 28px rgba(0,0,0,0.5), 0 0 18px rgba(56,189,248,0.5);
        }
        .tab-btn:hover::before {
            opacity: 1;
        }

        .tab-btn.active {
            background: rgba(56, 189, 248, 0.15);
            border-color: rgba(56, 189, 248, 0.7);
            color: #fff;
            box-shadow: 0 0 32px rgba(56, 189, 248, 0.6), 0 12px 24px rgba(0,0,0,0.6);
            font-weight: 700;
            text-shadow: 0 0 8px rgba(255,255,255,0.4);
        }

        .tab-content {
            display: none;
            animation: fadeSlide 0.5s ease;
            max-height: 70vh;
            overflow-y: auto;
            padding-right: 0.5rem;
            scrollbar-width: thin;
            scrollbar-color: rgba(56,189,248,0.3) transparent;
            color: rgba(255, 255, 255, 0.88);
        }

        .tab-content.active {
            display: block;
        }

        @keyframes fadeSlide {
            0% { opacity: 0; transform: translateY(24px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .tab-content::-webkit-scrollbar {
            width: 6px;
        }
        .tab-content::-webkit-scrollbar-track {
            background: transparent;
        }
        .tab-content::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #38bdf8, #a78bfa);
            border-radius: 12px;
        }

        .glass-card {
            background: rgba(20, 28, 48, 0.4);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 2.2rem;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 25px 45px rgba(0, 0, 0, 0.45), inset 0 0 0 1px rgba(255,255,255,0.04);
            transition: transform 0.2s ease, box-shadow 0.3s;
            position: relative;
        }
        .glass-card:hover {
            box-shadow: 0 30px 55px rgba(0,0,0,0.55), 0 0 35px rgba(56,189,248,0.2);
            transform: translateY(-2px);
        }

        .glass-card::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #38bdf8, #a78bfa, #f472b6, #fbbf24);
            border-radius: 2.2rem 2.2rem 0 0;
            opacity: 0.6;
        }

        h3 {
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 1.4rem;
            color: #fff;
            letter-spacing: -0.02em;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            background: linear-gradient(135deg, #bae6fd, #d8b4fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        h4 {
            font-size: 1.2rem;
            font-weight: 600;
            margin-top: 1.8rem;
            margin-bottom: 0.7rem;
            color: #cbd5e1;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        ul, ol {
            padding-left: 1.8rem;
            margin: 0.8rem 0 1.4rem;
            line-height: 1.8;
            color: rgba(255, 255, 255, 0.82);
        }
        li {
            margin-bottom: 0.6rem;
            position: relative;
        }
        ul li::marker {
            color: #38bdf8;
        }
        ol li::marker {
            color: #a78bfa;
            font-weight: bold;
        }

        strong {
            color: #f0f9ff;
            font-weight: 600;
        }

        pre {
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(12px);
            border-radius: 1.2rem;
            padding: 1.4rem;
            font-family: 'SF Mono', 'Fira Code', monospace;
            font-size: 0.9rem;
            color: #e2e8f0;
            overflow-x: auto;
            white-space: pre-wrap;
            word-break: break-word;
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-top: 3px solid #38bdf8;
            margin: 1.2rem 0;
            line-height: 1.7;
            box-shadow: 0 8px 20px rgba(0,0,0,0.4), 0 0 12px rgba(56,189,248,0.15);
        }

        code {
            font-family: 'SF Mono', monospace;
            background: rgba(255, 255, 255, 0.06);
            padding: 0.2rem 0.5rem;
            border-radius: 0.5rem;
            font-size: 0.9rem;
            color: #fbbf24;
        }

        a {
            color: #7dd3fc;
            text-decoration: none;
            border-bottom: 1px dotted rgba(125, 211, 252, 0.5);
            transition: 0.2s;
        }
        a:hover {
            color: #f0abfc;
            border-bottom-color: #f0abfc;
        }

        blockquote {
            border-left: 4px solid #38bdf8;
            padding-left: 1.3rem;
            margin: 1.5rem 0;
            font-style: italic;
            color: rgba(255, 255, 255, 0.7);
            background: rgba(56,189,248,0.06);
            border-radius: 0 1rem 1rem 0;
            padding: 1rem 1.2rem;
        }

        .highlight-box {
            border-radius: 1.2rem;
            padding: 1.3rem 1.5rem;
            margin: 1.8rem 0;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            font-weight: 500;
        }
        .highlight-box.info {
            background: rgba(56, 189, 248, 0.08);
            border-left: 4px solid #38bdf8;
        }
        .highlight-box.warning {
            background: rgba(251, 191, 36, 0.08);
            border-left: 4px solid #fbbf24;
        }
        .highlight-box.teal {
            background: rgba(45, 212, 191, 0.08);
            border-left: 4px solid #2dd4bf;
        }

        .inline-highlight {
            background: rgba(56,189,248,0.18);
            border-radius: 0.4rem;
            padding: 0.1rem 0.4rem;
            color: #e0f2fe;
            font-weight: 500;
            border: 1px solid rgba(56,189,248,0.3);
        }
        .pink-highlight {
            background: rgba(244,114,182,0.18);
            border-radius: 0.4rem;
            padding: 0.1rem 0.4rem;
            color: #fce7f3;
            border: 1px solid rgba(244,114,182,0.3);
        }

        @media (max-width: 700px) {
            .container {
                padding: 2rem 1.2rem;
                border-radius: 2.5rem;
            }
            h1 {
                font-size: 2rem;
            }
            .tab-btn {
                padding: 0.7rem 1.2rem;
                font-size: 0.85rem;
            }
        }


✨ OpenBraille · Instruction Hub


Final PPT production · Hardware audit · Speaker preparation


            📄 Sreehari — PPT Production
            🔍 Amith — Hardware Audit
            🎤 Sreeprada — Project Understanding


📋 1. Instructions for Sreehari — final PPT production


Sreehari is technically capable, so give him the full authoritative package rather than a simplified summary.


📚 Documents Sreehari should use


Read them in this order:


Zeroth review - Presentation.pptx
This is the mandatory structure. It contains 16 slides, including the fixed Vision, Mission, PEO, PO and PSO slides.


Engineering_Design_Review.md — OpenBraille section only
Use this for: project identity; mission; engineering hypothesis; major risks; Minimum Demonstrable Success.
The official MDS is simply demonstrating reliable refreshable tactile output for at least one Braille cell with basic tactile and repeatability requirements. It does not define ≤0.1 mm over 100 cycles as the MDS.


Project_mC_Decision_Register_v1.2.md
Read: PDR-001: budget; PDR-002: timeline/team; PDR-009: future IP direction; PDR-015 to PDR-022: OpenBraille architecture and testing.
PDR v1.2 freezes the servo-cam mechanism, macro-scaled cell, ESP32 controller, separate servo power, FDM fabrication and single-dot-first validation. It also states that the SG90 reset assumption remains physically unvalidated.


Phase3C_OpenBraille_Architecture_Report_Final.md
This is the main source for the proposed method, component architecture, BOM estimate, block diagram and validation roadmap.


Phase3C_OpenBraille_Memory_Final.md
Use this as a quick cross-check when the full architecture report is too long.


Official component sources listed later in this answer.


                    ⚠️ Do not use raw Gemini, Mistral, Qwen or Perplexity research for slide facts. Do not use the early Concept Dossier for exact price or market statistics.


📐 Template and formatting work


Sreehari must preserve all 16 slides.


Slides 1–2

                Title: OpenBraille: Affordable Refreshable Single-Cell Braille Display
Group No: Group 8

Members:
Amith Krishna Das
Archa Pramod
Nihad P C
Sreehari K
Sreeprada

Project Coordinator:
Ms. Sagna L T
Asst. Prof. CSE(CY)

Do not add technical job titles beside the member names.


Slides 3–8
Do not change the body text, wording or order.
Only add:


Header: Topic: OpenBraille


Footer: Dept of CSE(CY)


Date: 30/07/26


Slide number


Do not redesign these slides using cards, icons or shortened summaries.


Slide 9
Keep the existing contents:

                Motivation
Introduction
Problem Statement
Proposed Method
Basic Block Diagram
Conclusion
References


📝 Exact replacement content for Slides 10–16


Slide 10 — Motivation
Replace Sreehari’s current price-heavy content with:

                • Commercial refreshable Braille displays remain expensive because
  each tactile dot requires precise actuation and specialized manufacturing.

• Audio screen readers are useful, but tactile Braille supports literacy,
  spelling, mathematics and structured learning.

• The high cost of refreshable displays limits access in schools,
  libraries and resource-constrained institutions.

• OpenBraille explores whether low-cost embedded actuation can provide
  an affordable refreshable tactile interface.

Do not include: $3,500–$15,000; ₹2.9L–₹12.5L; ₹500–₹1,000 per dot; <₹100 per dot; “10× cost reduction”; “30 years of stagnation.”


Visual: a qualitative comparison:

                Commercial approach
Precision piezoelectric actuation
High manufacturing complexity

                 versus

OpenBraille prototype
Commodity servo-cam actuation
Student-accessible fabrication

Do not use a numerical price chart.


Slide 11 — Introduction

                • OpenBraille is an assistive embedded system exploring lower-cost
  actuation for refreshable Braille.

• The objective is to validate whether affordable electromechanical
  components can generate refreshable tactile output.

• The semester prototype targets one six-dot Braille cell.

• The cell is intentionally macro-scaled to improve FDM buildability
  and reduce dimensional-tolerance risk.

Add a small “Scope” box:

                IS:
A single six-dot refreshable tactile cell

IS NOT:
A Braille printer, OCR scanner, screen reader or full-page display

Use “improve buildability,” not “ensure buildability.”


Slide 12 — Problem Statement

                • Conventional refreshable Braille systems depend on expensive
  actuation and precision manufacturing.

• Standard-size Braille geometry creates severe alignment, friction
  and pin-binding risks for low-cost FDM fabrication.

• Engineering hypothesis:
  A lower-cost actuation strategy can replace conventional
  piezoelectric actuation while maintaining acceptable tactile performance.

• Constraints:
  Preferred budget ≤ ₹3,000
  Maximum budget ≤ ₹5,000
  Development period approximately two months
  Five-member student team

Do not write ≤0.1 mm repeatability over 100 cycles as the Minimum Demonstrable Success.


Slide 13 — Proposed Method

                • Six positional SG90-class micro servos drive eccentric cams.

• Each cam converts servo rotation into vertical movement of one
  tactile pin.

• An ESP32-WROOM-32 development board generates six independent
  servo-control signals.

• Servos use a separate external 5 V power rail with a common ground
  connection to the ESP32.

• A 1,000 µF capacitor is proposed across the servo power rail to help
  reduce transient voltage dips.

• The frame and cam mechanisms are produced using in-house FDM
  fabrication and off-the-shelf parts.

Important wording:


say “control signals”, not “servo power from GPIO”;


say “separate power rail”, not “isolated power rail”;


say the capacitor may help reduce voltage dips, not “prevents brownouts”;


do not claim the passive SG90 spring reset is proven;


do not claim the 5 V/2 A supply has already been validated.


Visual: exploded mechanism:

                SG90 servo → eccentric cam → follower/pin → tactile output


Slide 14 — Basic Block Diagram
Delete the current tiny diagram and recreate it using large PowerPoint shapes.

                Text / USB Input
        ↓
ESP32 Controller
and Braille Lookup Logic
        ↓
Six Servo-Control Signals
        ↓
Six Positional Micro Servos
        ↓
Six Cam-and-Follower Mechanisms
        ↓
Six Refreshable Tactile Pins

Power path should appear separately:

                External 5 V Supply
        ↓
1,000 µF Capacitor
        ↓
Servo Power Rail

Ground connection:

                ESP32 GND ↔ Servo Supply GND

Design rules: blue arrows for control/data; red arrows for power; black or grey line for common ground; no paragraph inside the diagram; every label readable from the back of a classroom.


Slide 15 — Conclusion

                • OpenBraille proposes a macro-scaled single-cell refreshable Braille
  prototype using ESP32-controlled servo-cam actuation.

• Macro-scaling reduces the dominant FDM tolerance risk, but friction,
  alignment, tactile force and repeatability still require validation.

• The estimated BOM is ₹2,060–₹2,850, subject to component prices
  and prototype revisions.

• Development will follow a bottom-up, single-dot-first validation
  strategy before integrating the complete six-dot cell.

• Future work may investigate multi-cell scaling and potential IP
  directions after experimental validation.

Do not say: the design “eliminates mechanical risk”; the project is complete in four weeks; testing has already passed; a patent filing is planned or guaranteed; BLE, Wi-Fi, cloud, AI or cybersecurity features are included.


Visual: simple eight-week roadmap:

                Weeks 1–2: electronics and single-dot mechanism
Weeks 3–4: mechanical refinement and multi-dot integration
Weeks 5–6: six-dot cell and firmware integration
Week 7: repeatability and tactile validation
Week 8: correction, documentation and final demonstration


Slide 16 — References

                1. ISO 17049:2013,
   Accessible design — Application of Braille on signage,
   equipment and appliances.

2. Espressif Systems,
   ESP32-WROOM-32 Datasheet, Version 3.6.

3. Espressif Systems,
   ESP32-DevKitC V4 User Guide.

4. TowerPro,
   SG90 Analog Micro Servo — Official Product Specifications.

5. Engineering_Design_Review.md,
   Project mC, OpenBraille section, July 2026.

6. Project_mC_Decision_Register_v1.2.md,
   PDR-001, PDR-002 and PDR-015 to PDR-022.

7. Phase3C_OpenBraille_Architecture_Report_Final.md,
   Project mC, July 2026.

ISO confirms that ISO 17049 covers fundamental Braille requirements and dimensional parameters for signage, equipment and appliances. The presentation must clarify that the semester prototype intentionally uses macro-scaled dimensions rather than claiming compliance. (ISO)


✅ Final visual and formatting checklist for Sreehari


Confirm all 16 slides remain.


Add Topic: OpenBraille.


Add Dept of CSE(CY).


Add 30/07/26.


Add slide numbers.


Keep Slides 3–8 unchanged.


Maximum four or five main bullets per technical slide.


Use consistent font sizes.


Remove unsupported exact commercial prices.


Ensure Slide 14 is readable.


Use “estimated,” “proposed,” “selected” and “requires validation” where appropriate.


Export once as PPTX and once as PDF for visual checking.


Open the PDF and verify that no text overlaps or falls outside the slide.


🔬 2. Instructions for Amith — hardware expert and final auditor


Amith should not only check spelling. His responsibility is to understand why every hardware component exists, what evidence supports it, and what remains untested.


📖 Hardware documents Amith must read


First priority


Phase3C_OpenBraille_Architecture_Report_Final.md
Read the entire hardware, mechanical, power, BOM and validation sections.


Project_mC_Decision_Register_v1.2.md
Focus on:


                PDR-015  Servo + cam actuation
PDR-016  Macro-scaled cell
PDR-017  ESP32-WROOM-32 DevKit
PDR-018  Direct GPIO servo-control architecture
PDR-019  FDM manufacturing pathway
PDR-020  External 5V/2A supply and 1,000 µF capacitor
PDR-021  Reset mechanism — technically unvalidated
PDR-022  Single-dot-first validation strategy

These decisions form the current architecture baseline.


Phase3C_OpenBraille_Memory_Final.md
Use as his compact hardware summary.


Engineering_Design_Review.md — OpenBraille section
This explains what the hardware must ultimately prove: affordable refreshable output for at least one cell with basic tactile and repeatability performance.


🔗 Official references Amith must inspect


A. ESP32-WROOM-32 official datasheet
Open the official Espressif ESP32-WROOM-32 Datasheet, Version 3.6. It is the module-level source. (Espressif Systems)


Amith should record: exact document title; version; module name; available GPIO/peripheral capability; operating and power limitations relevant to the module.

                The ESP32-WROOM-32 module datasheet is not automatically the same as the pinout of every generic “ESP32 DevKit” clone.


B. ESP32-DevKitC V4 User Guide
Open the official Espressif ESP32-DevKitC V4 User Guide. Use this for board layout, headers, power pins and pin identification. (Espressif Systems)


Amith must compare the guide against the exact board the team will buy or already owns. He should record: board marking printed on the PCB; module marking; USB connector type; 5V, 3V3 and GND pins; which GPIO pins are suitable for servo-control outputs; pins that should not be used because of boot, flash or input-only restrictions.


Do not freeze final GPIO numbers in the PPT unless the actual board is available and checked.


C. ESP32 LEDC/PWM official documentation
Open the official ESP-IDF LED Control (LEDC) documentation. It confirms that ESP32 LEDC channels can generate PWM signals through configured GPIO outputs. (Espressif Systems)


Amith should verify: six independent output channels are feasible; the firmware architecture can assign channels and timers; the slide should say “PWM control signals,” not claim that GPIO powers a servo.


D. TowerPro SG90 official page
Open the official TowerPro SG90 Analog page. The official page lists: 9 g weight; 4.8 V operating voltage; approximately 1.8 kg·cm stall torque at 4.8 V; external-adapter power; plastic/POM gears. (Tower Pro)


Amith must record what the official page does not confirm: no reliable six-servo total-current figure; no confirmation that a 5 V/2 A adapter is sufficient for six simultaneous servos; no confirmation of a passive torsion-spring reset; no confirmation that the exact local-market SG90 clone has identical performance.

                The official SG90 page supports operating voltage, torque class and external powering. It does not prove the project’s total power budget or reset mechanism.


E. Confirm the servo is positional, not continuous-rotation
TowerPro also sells a separate SG90 360-degree continuous-rotation servo. That model behaves as a speed/direction actuator rather than a normal commanded-position servo. (Tower Pro)


Amith must ensure the team purchases:

                Standard positional SG90 Analog or Digital servo

and not:

                SG90 360-degree continuous-rotation servo

A cam mechanism that must hold specific raised and lowered positions should use the positional version.


F. ISO 17049 official page
Open the ISO 17049:2013 official page. It confirms the standard concerns Braille dimensional requirements and practical implementation. (ISO)


Amith’s audit rule: the standard may be cited as a dimensional reference; the prototype must not be described as ISO-compliant; the deck should state that it is intentionally macro-scaled.


⚙️ Hardware understanding Amith must have


1. Why six servos?
A six-dot Braille cell has six individually controllable dots. The proposed architecture assigns one positional servo-cam mechanism to each dot. Audit question: Does the deck clearly show six independently controlled outputs?


2. Why a cam?
A servo produces rotary motion. The tactile pin needs vertical linear motion. The eccentric cam converts servo rotation into upward/downward pin displacement. Audit questions: Is the rotation-to-linear-motion conversion clear? Does the slide avoid claiming that the final cam geometry is already validated?


3. Why ESP32?
The project selects ESP32 because it offers sufficient control outputs, timer/PWM capability, low cost and team familiarity. PDR v1.2 freezes ESP32-WROOM-32 DevKit as the architecture choice. Audit question: Does the slide describe the ESP32 as the controller, rather than as a power source?


4. Why no external H-bridge?
A standard hobby servo already contains its motor-control electronics. The ESP32 sends a control signal; it does not directly drive the servo motor winding. Audit question: Does the slide correctly say “no intermediate motor-driver IC for the selected hobby servos”? Do not generalize this to every actuator type.


5. Why a separate power supply?
Servo motors produce current spikes, especially during acceleration, mechanical resistance and stall. Powering several servos through the ESP32 board or GPIO would be unsafe and unstable.

                ESP32: USB/board supply
Servos: separate external 5 V rail
Grounds: connected together

Audit questions: Does the block diagram show separate power paths? Is the common ground shown? Is the rail incorrectly called electrically isolated?


6. Why the 1,000 µF capacitor?
It is proposed as bulk decoupling to reduce short-duration voltage dips on the servo rail. It does not: create extra continuous power; make an undersized adapter sufficient; guarantee that brownouts cannot happen.


7. Why macro-scale?
Standard Braille geometry is difficult to fabricate using ordinary FDM printing because small clearances increase friction, misalignment and binding risk. Macro-scaling reduces this risk but does not remove it. Audit question: Does every slide say “reduces risk” rather than “eliminates risk”?


8. What is unresolved?
Amith must be able to explain that these are still untested: usable tactile force; friction and pin binding; servo-to-servo variation; exact current consumption; adequacy of the 5 V/2 A supply; cam dimensions; durability; passive reset claim; human tactile distinguishability.


🔍 Amith’s final PPT audit sequence


After Sreehari sends the final deck:


Pass 1 — template
Check: 16 slides; fixed institutional content untouched; correct header/footer/date/numbers; Group 8 and all five names.


Pass 2 — hardware claims
Mark every hardware statement: Approved architecture / Selected but untested component / Estimated value / Planned validation / Unsupported claim.


Pass 3 — red-flag phrases
Search the slides for:

                eliminates all risk
        guarantees
        fully proven
        ISO-compliant
        completed testing
        successful prototype
        patented
        certainly patentable
        GPIO powers servo
        isolated power supply
        5V/2A is sufficient
        passive reset is confirmed

Replace or remove each occurrence.


Pass 4 — reference verification
For each external reference, confirm: official organization; exact title; no invented author; no invented date; no unverifiable academic paper.


Pass 5 — visual review
Check the exported PDF at full-screen size. Slide 14 must be understandable in under ten seconds.


🗣️ 3. Instructions for Sreeprada — simple project understanding


Sreeprada should wait before assigning slides, because the final allocation depends on Sreehari’s final deck and Amith’s corrections.


For now, she only needs a simple overview.


📄 Documents for Sreeprada


Give her only:


Engineering_Design_Review.md — OpenBraille Mission, Hypothesis and MDS.


Phase3C_OpenBraille_Memory_Final.md.


The final audited PPT, once finished.


                    🚫 Do not give her: raw research; Phase 2 patent reports; the full PDR; the full architecture research corpus. That would create unnecessary confusion.


💡 Layman explanation for Sreeprada


Braille characters are made using six possible raised dots. Commercial electronic Braille displays are expensive because every dot needs a tiny, accurate mechanism that can move up and down repeatedly. Our project tries to prove a cheaper method. We use six small positional servo motors. Each servo turns a specially shaped cam, and the cam pushes one tactile pin upward or brings it downward. An ESP32 decides which of the six pins should be raised for each character. The servos receive power from a separate supply because motors need more current than the ESP32 can provide. We are first building one enlarged Braille cell so that it is easier to manufacture and test.


🧠 Five facts she must understand


It is one six-dot cell, not a full Braille display.


The six servos control six tactile pins.


The ESP32 decides which dots should rise.


The servo-cam mechanism is proposed but still needs physical testing.


The goal is to prove a low-cost alternative, not claim a finished commercial product.


After the final PPT is frozen, Sreeprada should distribute meaningful project slides among all five members. She should not base the allocation on the current draft because Slide 14 and the project-content wording are still changing.


        (function() {
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabContents = document.querySelectorAll('.tab-content');

            tabButtons.forEach(btn => {
                btn.addEventListener('click', () => {
                    const targetId = btn.getAttribute('data-tab');
                    tabButtons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');
                    tabContents.forEach(content => {
                        content.classList.remove('active');
                        if (content.id === targetId) {
                            content.classList.add('active');
                        }
                    });
                });
            });
        })();
