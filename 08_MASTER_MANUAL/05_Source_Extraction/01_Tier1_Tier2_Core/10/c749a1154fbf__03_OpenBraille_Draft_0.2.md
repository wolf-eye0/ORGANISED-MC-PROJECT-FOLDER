# Source Extraction

- Chapter: `10` — Teacher Reviews and Presentation Record
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_HISTORICAL`
- Original source: `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/03_OpenBraille_Draft_0.2.pptx`
- Current SHA-256: `c749a1154fbfb70df38e30e65620c0f734d8ac98c23892207dcd3e535e8507d1`
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
 K S

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
Cost Barrier:
 Refreshable Braille displays are still expensive because each dot needs careful movement and special hardware.
Beyond Audio:
 Audio screen readers are helpful, but Braille is better for reading, spelling,
maths
 and structured learning.
Limited Access:
 High device cost makes it hard for schools, libraries and small institutions to provide refreshable Braille.
Low-Cost Trial:

OpenBraille
 tests whether cheaper embedded parts can give a refreshable tactile interface.

## Slide 11

Introduction
Project Idea:

OpenBraille
 is an embedded assistive system that looks at lower-cost ways to move Braille dots.
Main Goal:
 Check if affordable electro‑mechanical parts can create refreshable tactile Braille output.
Prototype Scope:
 The semester work focuses on one six‑dot Braille cell.
Macro Scale Choice:
 The cell is made larger on purpose to make FDM 3D printing easier and reduce dimension issues.

## Slide 12

Problem Statement
Expensive Systems:
 Most refreshable Braille devices use costly actuators and precise manufacturing.
Small-Scale Issues:
 Normal Braille sizes cause alignment, friction and jamming problems when made with low‑cost FDM printing.
Working Hypothesis:
 A cheaper actuation method might replace piezoelectric actuators while still giving usable tactile Braille.
Project Limits:
 Prefer budget ≤ ₹3,000; maximum budget ≤ ₹5,000; about two months of work; five‑member student team.

## Slide 13

Proposed Method
Servo Drive:
 Six SG90‑class micro servos move eccentric cams.
Dot Movement:
 Each cam turns servo rotation into up‑and‑down motion of one tactile pin.
Controller Board:
 An ESP32‑WROOM‑32 board creates six separate servo control signals.
Power Setup:
 Servos run from an external 5 V line with a shared ground to the ESP32 board.
Power Support:
 A 1,000 µF capacitor is planned on the servo power line to help smooth voltage changes.
Mechanics Build:
 The frame and cam parts are made using college FDM printers and easily available components.

## Slide 14

Basic Block Diagram

## Slide 15

Conclusion
Prototype Proposal:

OpenBraille
 suggests a macro‑scaled single‑cell refreshable Braille prototype using ESP32‑controlled servo‑cam actuation.
Remaining Checks:
 Making the cell larger helps with FDM tolerances, but friction, alignment, feel of the dots and repeatability still need testing.
Cost Estimate:
 The estimated BOM is in the range ₹2,060–₹2,850, depending on part prices and design changes.
Test Plan:
 Work will start with one dot, then move step‑by‑step to the full six‑dot cell after basic validation.
Future Steps:
 After experiments, the project may explore multi‑cell designs and possible IP options.

## Slide 16

References
1. ISO 17049:2013,   Accessible design — Application of Braille on signage,   equipment and appliances.
2.
Espressif
 Systems,   ESP32-WROOM-32 Datasheet, Version 3.6.
3.
Espressif
 Systems,   ESP32-DevKitC V4 User Guide.
4.
TowerPro
,   SG90 Analog Micro Servo — Official Product Specifications.
5. Engineering_Design_Review.md,   Project
mC
,
OpenBraille
 section, July 2026.
6. Project_mC_Decision_Register_v1.2.md,   PDR-001, PDR-002 and PDR-015 to PDR-022.
7. Phase3C_OpenBraille_Architecture_Report_Final.md,   Project
mC
, July 2026.
