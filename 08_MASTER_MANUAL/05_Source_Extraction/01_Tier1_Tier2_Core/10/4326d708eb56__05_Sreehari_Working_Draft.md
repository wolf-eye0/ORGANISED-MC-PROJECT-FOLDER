# Source Extraction

- Chapter: `10` — Teacher Reviews and Presentation Record
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_HISTORICAL`
- Original source: `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/05_Sreehari_Working_Draft.pptx`
- Current SHA-256: `4326d708eb56198773dc6f5f7e4bb49407d51c19823a87700a3e390ebcbf5b2a`
- Extraction method: `PPTX_XML`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

## Slide 1

PBCST504 – MICROCONTROLLERS
MICRO PROJECT
Zeroth Review

## Slide 2

Title:-
OpenBraille
: Affordable Refreshable Single-Cell Braille Display
Group No: Group 8
Members: Amith Krishna Das
                 Archa Pramod
                 Nihad P C
                 Sreehari K

Sreeprada

Project Coordinator:
Ms.Sagna
 L T
Asst. Prof. CSE(CY)

## Slide 3

DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
(Cyber Security)

Vision of the Department
To be a globally recognized centre of excellence in Cyber Security education, research and innovation by nurturing ethical professionals , fostering technological advancement through responsible practice and contributing to a secure and sustainable digital society.

## Slide 4

DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
(Cyber Security)

Mission of the Department
M1: Excellence in Education
 :
To provide outcome-based and industry-oriented education by integrating core computer science principles with advanced cybersecurity technologies and practices.
M2: Ethics and Professional Responsibility :
To cultivate ethical values, integrity, social responsibility, and secure computing practices for protecting digital assets and strengthening cyber trust.
M3: Research, Innovation, and Entrepreneurship :
To promote research, innovation, and entrepreneurial thinking for developing sustainable solutions to emerging cybersecurity challenges.
M4: Holistic and Global Development :
To enhance leadership, teamwork, lifelong learning, and global competence through industry collaboration, interdisciplinary activities, and community engagement.

## Slide 5

Programme
 Educational Objectives (PEOs)
PEO 1:

Graduates will apply strong foundations in computer science and cybersecurity to design, develop, and manage secure and reliable computing systems for industry and society.
PEO 2:

Graduates will pursue successful careers as professionals, innovators or entrepreneurs engaged in technology development, deployment or engineering system implementation in industry and society and contribute to the economic growth of the country.
PEO 3:

Graduates will demonstrate ethical responsibility, leadership, teamwork, and effective communication while adapting to evolving global technological environments through lifelong learning.

## Slide 6

Programme
 Outcomes
    Engineering Graduates will be able to:
1.
Engineering knowledge:
 Apply the knowledge of mathematics, science, engineering fundamentals, and an engineering specialization to the solution of complex engineering problems.
2.
Problem analysis:
 Identify, formulate, review research literature, and analyze complex engineering problems reaching substantiated conclusions using first principles of mathematics, natural sciences, and engineering sciences.
3.
Design/development of solutions:
 Design solutions for complex engineering problems and design system components or processes that meet the specified needs with appropriate consideration for the public health and safety, and the cultural, societal, and environmental considerations.
4.
Conduct investigations of complex problems:
 Use research-based knowledge and research methods including design of experiments, analysis and interpretation of data, and synthesis of the information to provide valid conclusions.
5.
Modern tool usage:
 Create, select, and apply appropriate techniques, resources, and modern engineering and IT tools including prediction and modeling to complex engineering activities with an understanding of the limitations.

## Slide 7

6.
The engineer and society:
 Apply reasoning informed by the contextual knowledge to assess societal, health, safety, legal and cultural issues and the consequent responsibilities relevant to the professional engineering practice.
7.
Environment and sustainability:
 Understand the impact of the professional engineering solutions in societal and environmental contexts, and demonstrate the knowledge of, and need for sustainable development.
8.
Ethics:
 Apply ethical principles and commit to professional ethics and responsibilities and norms of the engineering practice.
9.
Individual and team work:
 Function effectively as an individual, and as a member or leader in diverse teams, and in multidisciplinary settings.
10.
Communication:
 Communicate effectively on complex engineering activities with the engineering community and with society at large, such as, being able to comprehend and write effective reports and design documentation, make effective presentations, and give and receive clear instructions.
11.
Project management and finance:
 Demonstrate knowledge and understanding of the engineering and management principles and apply these to one’s own work, as a member and leader in a team, to manage projects and in multidisciplinary environments.
12.
Life-long learning:
 Recognize the need for, and have the preparation and ability to engage in independent and life-long learning in the broadest context of technological change
.

## Slide 8

Programme
 Specific Outcomes (PSOs)
 On the completion of Computer Science & Engineering program, the students will possess:

PSO 1
: Apply cyber security principles to mitigate cyber risk and
analyze
 security requirements of an organization.
PSO 2
: Develop and deploy secure software and infrastructure using modern tools and industry standards.
PSO 3
: Uphold ethical, legal, and societal responsibilities while protecting privacy, data, and digital assets.

## Slide 9

CONTENTS
Motivation
Introduction
Problem Statement
Proposed Method
Basic Block Diagram
Conclusion
References

## Slide 10

Motivation
Severe Economic Barrier:
 Commercial refreshable Braille displays retail between $3,500 and $15,000 USD (₹2.9L–₹12.5L INR).
Market Stagnation:
 Reliance on hand-assembled, high-voltage (60–200V) piezoelectric bimorph actuators for over 30 years.
Literacy & Employment Crisis:
 Tactile Braille remains essential for STEM education, coding, and formal literacy despite audio screen readers.
Frugal Innovation Opportunity:
 Disrupting actuator costs from ₹500–₹1,000 per dot down to <₹100 per dot enables affordable assistive tech.

## Slide 11

Introduction
Engineering Identity:
 An assistive embedded platform investigating lower-cost electromechanical actuation to present tactile Braille.
Engineering Hypothesis:
 Low-cost commodity actuators can replace conventional piezoelectric bimorphs while maintaining acceptable tactile performance.
System Boundaries:
IS:
 A single-cell (6-dot) refreshable tactile display module driven by an ESP32.
IS NOT:
 A Braille printer, OCR scanner, screen reader software, or full-page display.
Semester Target:
 A working 6-dot proof-of-concept cell validating tactile legibility and refresh repeatability.

## Slide 12

Problem Statement
Engineering Bottleneck:
 Standard ISO 17049 dot pitch (2.34 mm) causes mechanical binding and high failure rates on FDM 3D printers.
Minimum Demonstrable Success (MDS):
 Reliably produce refreshable, legible Braille output for one 6-dot cell with ≤0.1 mm repeatability over 100 cycles.
Immutable Constraints:
Team Scope:
 3 CS/Cybersecurity students + 2 support members (No mechanical engineer).
Budget:
 Preferred ≤ ₹3,000 INR; absolute maximum ≤ ₹5,000 INR.
Timeline:
 8-week development window.

## Slide 13

Proposed Method
Actuation Principle:
 Macro-scaled Servo + Cam linkage mechanism replacing piezo bimorphs.
Dimensional Mitigation:
 ~300% macro-scale (≈7 mm dot pitch, ≈1.5 mm pin height) eliminates FDM print tolerance failures.
Control Platform:
 ESP32-WROOM-32
DevKit
 utilizing hardware timers for jitter-free PWM.
Driver Elimination:
 Direct GPIO PWM to 6× SG90 micro servos; internal circuits eliminate H-bridge ICs.
Power Architecture:
 External 5V/2A DC power supply with a 1,000 µF decoupling capacitor.
Fabrication:
 In-house FDM 3D printing (ABS frame, PETG cams) and 2mm stainless steel pins.

## Slide 14

Basic Block Diagram

## Slide 15

Conclusion
Project Summary:

OpenBraille
 proposes a low-cost, single-cell refreshable Braille display using an ESP32 controller, servo–cam actuation, and FDM‑printed mechanics to bypass the cost and complexity of piezoelectric actuators.
Sequential Bring-Up Strategy (M1–M8):
Week 1:
 Electrical bring-up, ESP32 PWM verification, single-servo sweep.
Week 2:
 Single-dot cam integration, 6-dot cell assembly, 100-cycle repeatability test.
Week 3:
 Tactile legibility user validation and full A–Z Braille pattern display.
Week 4:
 Final Minimum Demonstrable Success (MDS) demonstration on the 6-dot cell.
Team Task Distribution:
Technical Leads:
 ESP32
FreeRTOS
/PWM timers, driver power stability, system integration.
Fabrication Leads:
 ABS frame CAD, cam-profile printing, mechanical alignment.
Software Support:
 Isolated Unicode-to-Braille lookup table and diagnostic test firmware.

## Slide 16

References
Engineering Design Review Board,

"Project
mC
: Engineering Design Review (EDR) — Concept 1:
OpenBraille
,"
 Immutable Project Specification, July 2026.
Final Engineering Architecture Review Board,

"Phase 3C —
OpenBraille
 Engineering Architecture Report,"
 Project
mC
 Technical Report, July 2026.
Lead Engineering Review Board,

"Project
mC
 Decision Register (PDR) Version 1.1,"
 Decision Log (PDR-001 to PDR-044), July 2026.
ISO/TC 173/SC 7,

ISO 17049:2013 — Accessible Design: Application of Braille on Signage, Equipment and Appliances,
 2013.
American Foundation for the Blind (AFB),

"Refreshable Braille Displays & Cost Analysis,"
 Product Technology Survey, 2024.
