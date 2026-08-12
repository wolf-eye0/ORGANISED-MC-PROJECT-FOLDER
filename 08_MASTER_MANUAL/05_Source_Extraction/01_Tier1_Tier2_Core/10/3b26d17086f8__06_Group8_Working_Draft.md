# Source Extraction

- Chapter: `10` — Teacher Reviews and Presentation Record
- Authority tier: `TIER_2`
- Manual treatment: `CORE_OR_HISTORICAL`
- Original source: `05_TEACHER_AND_REVIEWS/02_Zeroth_Review_OpenBraille/02_Drafts_and_Working_Files/06_Group8_Working_Draft.pptx`
- Current SHA-256: `3b26d17086f86b420a9fce25d4ac17eea063d206981651325313de99d3156225`
- Extraction method: `PPTX_XML`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

## Slide 1

MICRO PROJECT
Zeroth Review
30-07-2026
PBCST504-MICROCONTROLLERS

## Slide 2

Title:- OpenBraille: Affordable Refreshable Single-Cell Braille Display
Group No: Group 8
Members:

Amith Krishna Das
 JEC24CC016
                 Archa Pramod
 JEC24CC023
                 Nihad P C
  JEC24CC044
                 Sreehari K
  JEC24CC055
                 Sreeprada K S
  JEC24CC056

Project Coordinator:
Ms.Sagna L T
Asst. Prof. CSE(CY)
30-07-2026

## Slide 3

DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
(Cyber Security)

Vision of the Department
To be a globally recognized centre of excellence in Cyber Security education, research and innovation by nurturing ethical professionals , fostering technological advancement through responsible practice and contributing to a secure and sustainable digital society.
30-07-2026

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
30-07-2026

## Slide 5

Programme Educational Objectives (PEOs)
PEO 1:

Graduates will apply strong foundations in computer science and cybersecurity to design, develop, and manage secure and reliable computing systems for industry and society.
PEO 2:

Graduates will pursue successful careers as professionals, innovators or entrepreneurs engaged in technology development, deployment or engineering system implementation in industry and society and contribute to the economic growth of the country.
PEO 3:

Graduates will demonstrate ethical responsibility, leadership, teamwork, and effective communication while adapting to evolving global technological environments through lifelong learning.
30-07-2026

## Slide 6

Programme Outcomes
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
30-07-2026

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
30-07-2026

## Slide 8

Programme Specific Outcomes (PSOs)
 On the completion of Computer Science & Engineering program, the students will possess:

PSO 1
: Apply cyber security principles to mitigate cyber risk and analyze security requirements of an organization.
PSO 2
: Develop and deploy secure software and infrastructure using modern tools and industry standards.
PSO 3
: Uphold ethical, legal, and societal responsibilities while protecting privacy, data, and digital assets.
30-07-2026

## Slide 9

CONTENTS
Motivation
Introduction
Problem Statement
Proposed Method
Basic Block Diagram
Conclusion
References
30-07-2026

## Slide 10

Motivation
Commercial refreshable Braille displays remain expensive because  each tactile dot requires precise actuation and specialized manufacturing.
Audio screen readers are useful, but tactile Braille supports literacy,  spelling, mathematics and structured learning.
The high cost of refreshable displays limits access in schools,  libraries and resource-constrained institutions.
 OpenBraille explores whether low-cost embedded actuation can provide  an affordable refreshable tactile interface.
30-07-2026

## Slide 11

Introduction
OpenBraille is an assistive embedded system exploring lower-cost  actuation for refreshable Braille.
 The objective is to validate whether affordable electromechanical  components can generate refreshable tactile output.
The semester prototype targets one six-dot Braille cell.
 The cell is intentionally macro-scaled to improve FDM buildability  and reduce dimensional-tolerance risk.
30-07-2026

## Slide 12

Problem Statement
Conventional refreshable Braille systems depend on expensive  actuation and precision manufacturing.
Standard-size Braille geometry creates severe alignment, friction  and pin-binding risks for low-cost FDM fabrication.
Engineering hypothesis:  A lower-cost actuation strategy can replace conventional  piezoelectric actuation while maintaining acceptable tactile performance.
Constraints
:
Preferred budget ≤ ₹3,000  Maximum budget ≤ ₹5,000  Development period approximately two months  Five-member student team
30-07-2026

## Slide 13

Proposed Method
Six positional SG90-class micro servos drive eccentric cams.
Each cam converts servo rotation into vertical movement of one  tactile pin.
An ESP32-WROOM-32 development board generates six independent  servo-control signals.
Servos use a separate external 5 V power rail with a common ground  connection to the ESP32.
 A 1,000 µF capacitor is proposed across the servo power rail to help  reduce transient voltage dips.
 The frame and cam mechanisms are produced using in-house FDM  fabrication and off-the-shelf parts..
30-07-2026

## Slide 14

Basic Block Diagram
30-07-2026

## Slide 15

Conclusion
OpenBraille proposes a macro-scaled single-cell refreshable Braille  prototype using ESP32-controlled servo-cam actuation.
Macro-scaling reduces the dominant FDM tolerance risk, but friction,  alignment, tactile force and repeatability still require validation.
The estimated BOM is ₹2,060–₹2,850, subject to component prices  and prototype revisions.
Development will follow a bottom-up, single-dot-first validation  strategy before integrating the complete six-dot cell.
Future work may investigate multi-cell scaling and potential IP  directions after experimental validation.
30-07-2026

## Slide 16

References
1. ISO 17049:2013,   Accessible design — Application of Braille on signage,   equipment and appliances.
2. Espressif Systems,   ESP32-WROOM-32 Datasheet, Version 3.6.
3. Espressif Systems,   ESP32-DevKitC V4 User Guide.
4. TowerPro,   SG90 Analog Micro Servo — Official Product Specifications.
5. Engineering_Design_Review.md,   Project mC, OpenBraille section, July 2026.
6. Project_mC_Decision_Register_v1.2.md,   PDR-001, PDR-002 and PDR-015 to PDR-022.
7. Phase3C_OpenBraille_Architecture_Report_Final.md,   Project mC, July 2026.
30-07-2026
