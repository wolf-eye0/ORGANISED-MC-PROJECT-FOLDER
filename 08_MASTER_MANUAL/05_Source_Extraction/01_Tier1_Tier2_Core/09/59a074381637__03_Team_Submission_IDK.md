# Source Extraction

- Chapter: `09` — Comparative Decision and Proposed Concept Shift
- Authority tier: `TIER_2`
- Manual treatment: `CORE_DECISION_EVIDENCE`
- Original source: `04_COMPARATIVE_DECISION/04_Team_Audits_and_Objections/03_Team_Submission_IDK.pdf`
- Current SHA-256: `59a07438163718094c4cd4704016cee80bacce689939eafa52eb9cb91e56f126`
- Extraction method: `PDFTOTEXT_LAYOUT`
- Extraction rule: Full text extraction only; no summarization or reconciliation performed.

---

The application of Braille on equipment and appliances is strictly governed by the ISO
17049:2013 standard. To ensure tactile readability, this standard dictates precise dimen-
sional parameters: a dot base diameter of 1.0 to 1.7 mm (specifically 1.5 mm to 1.6 mm
in many regional adoptions), a horizontal dot spacing of 2.0 to 2.8 mm, and a dot height
of 0.3 to 0.7 mm. The biomechanics of tactile reading depend entirely on these precise di-
mensions, as the human fingertip must cover multiple dots simultaneously to recognize a cell
pattern instantly. Fused Deposition Modeling (FDM) 3D printers using standard 0.4 mm
nozzles struggle immensely to resolve a 1.5 mm domed dot reliably without severe stringing
or layer-line artifacts that degrade tactile readability.
While ”macro-scaling” the physical cell mathematically solves the mechanical FDM tolerance
risk, it introduces a severe factual and logical error: a macro-scaled Braille cell violates the
strict ISO 17049 dimensional parameters and actively destroys tactile readability, rendering
the device useless for an actual Braille reader. If the distance between corresponding dots
in adjacent cells exceeds the standard 6.1 mm to 7.6 mm, the user cannot read the display
fluidly. Claiming to build a Braille display while intentionally violating the foundational
standard that defines Braille geometry is a critical technical flaw that must be addressed.a
catastrophic academic and architectural misalignment exists. The presentation is explicitly
designated for the course ”PBCST504,” which is the KTU Microcontrollers course (Semester
5, 2024 Scheme). The official university syllabus for this course explicitly focuses on the
ARM Cortex-M architecture—specifically the Cortex-M23 and Cortex-M33 processors—and
mandates the use of STM32 microcontrollers (such as the STM32U575) for peripheral pro-
gramming, TrustZone implementation, and FreeRTOS deployment.
However, Slide 11 states that the project utilizes an ”ESP32-WROOM-32” development
board. The ESP32 is based on the Tensilica Xtensa Dual-Core 32-bit LX6 microprocessor
architecture, not the ARM Cortex-M architecture. Using an Espressif Xtensa-based micro-
controller for a project assigned under a curriculum strictly dedicated to ARM Cortex-M
and STM32 microcontrollers represents a fundamental failure to meet the core academic
requirements of the course.
Second, the slide demonstrates a technical terminology error regarding the hardware itself.
The text specifies the use of an ”ESP32-WROOM-32 development board”. The ESP32-
WROOM-32 is a surface-mount module consisting of the SoC, flash memory, and an antenna.
It is not a development board. The development board that houses this module, providing
the USB-to-UART bridge, voltage regulation, and pin headers, is officially designated as
the ESP32-DevKitC. Conflating a bare module with a populated development board is an
elementary hardware engineering mistake.
Third, the electrical power architecture described in the slide requires immediate verification.
The text states: ”Six positional SG90-class micro servos drive eccentric cams,” and ”A 1,000
µF capacitor is proposed across the servo power rail to help reduce transient voltage dips.” The
SG90 micro servo is a standard 9-gram actuator that operates via Pulse Width Modulation
(PWM) at a 50Hz frequency, requiring 1ms to 2ms duty cycles. While the ESP32’s LEDC
peripheral features 16 independent hardware PWM channels capable of driving these signal
lines simultaneously, the power draw is a major concern. An SG90 servo typically draws
between 100mA and 250mA during standard movement, but stall currents can spike up to


                                               1

700mA per servo. If all six servos move simultaneously or encounter mechanical resistance
(e.g., binding against the FDM printed cams), the total current draw on the 5V rail could
surge to between 1.5A and 4.2A. While a 1,000 µF bulk decoupling capacitor will smooth
short, high-frequency voltage transients and prevent the ESP32 from resetting (brownout)
due to common ground loops, it is mathematically incapable of sustaining continuous high-
current stall loads. The text critically omits any specification regarding the amperage rating
of the external 5V power supply required to drive this load.”Basic Block Diagram.” A review
of the slide reveals a critical omission: there is no diagram present. The slide contains only
the title text and is otherwise completely blank. In a technical hardware presentation, the
block diagram is essential for illustrating the interfacing between the microcontroller, the
power distribution network, the PWM signal routing, and the electromechanical actuators.
Submitting or presenting a slide deck with a missing primary visual graphic demonstrates a
severe lack of quality assurance. . Ranked Top 5 Most Serious Errors
Syllabus/Architecture Mismatch (Slide 11): The presentation proposes using an ESP32 (Ten-
silica Xtensa architecture) for a project in a KTU course (PBCST504) that strictly mandates
ARM Cortex-M and STM32 microcontrollers. This is a fatal academic failure that will result
in immediate penalization during an engineering review.
Missing Block Diagram (Slide 12): Submitting an entirely blank slide designated for the core
system architecture demonstrates a severe lack of quality control and will cause a critical
stoppage during a live presentation.
ISO 17049 Dimension Violation (Slide 9): ”Macro-scaling” the Braille cell mathematically
solves FDM printing tolerances but destroys the physiological capability of the fingertip to
read the tactile data. The text must acknowledge this as a non-standard mechanical proof-
of-concept rather than a functional Braille interface.
Hardware Terminology Conflation (Slide 11): Referring to the ”ESP32-WROOM-32” as a
development board instead of a bare surface-mount module is a rudimentary hardware en-
gineering error that undermines technical credibility.I have fact-checked the statements you
provided against official technical documentation, standards, and university curriculum guide-
lines. Here is the verification for each point:
1. ISO 17049:2013 and Braille Dimensions
The statements regarding the Braille dimensions are accurate. The ISO 17049:2013 standard
mandates strict dimensional parameters to ensure tactile readability, explicitly dictating a dot
base diameter between 1.0 and 1.7 mm and a dot height between 0.3 and 0.7 mm. Regional
accessibility guidelines that adopt these principles specify standard base diameters of 1.5 to
1.6 mm, dot spacing of 2.3 to 2.5 mm, and adjacent cell corresponding dot spacing of 6.1 to 7.6
mm. Therefore, intentionally ”macro-scaling” a Braille cell to bypass 3D printing tolerances
would fundamentally violate these standardized metrics, rendering the display functionally
useless for a tactile reader.
2. Academic Misalignment (KTU PBCST504 vs. ESP32)
The claim regarding the academic mismatch is factually correct. The APJ Abdul Kalam Tech-
nological University (KTU) 2024 Scheme defines course ”PBCST504” as ”Microcontrollers”


                                               2

for Semester 5. The official syllabus is strictly dedicated to ARM Cortex-M architecture
(specifically Cortex-M23 and M33 processors) and mandates the use of STM32 microcon-
trollers, such as the STM32U575. Conversely, the ESP32 operates on a Tensilica Xtensa
dual-core architecture. Using an ESP32 for this specific project is a direct violation of the
course’s core architectural requirements.
3. Hardware Terminology (WROOM-32 vs. DevKitC)
The hardware terminology correction is highly accurate. The ESP32-WROOM-32 is a bare
surface-mount module that contains the system-on-chip, memory, and a PCB antenna. It
requires a carrier board to provide the USB-to-UART bridge, voltage regulation, and pinout
headers for prototyping. The official Espressif development board that houses this module is
the ESP32-DevKitC. Conflating the two is a technical terminology error.
4. Power Architecture and SG90 Servos
The technical assessment of the power architecture and current draw is accurate. The ESP32
features 16 independent hardware PWM channels (via its LEDC peripheral) capable of pre-
cisely driving multiple servos. However, while an SG90 servo draws 100mA to 250mA during
standard movement, its stall current can spike from 360mA up to approximately 700mA. If
six servos move simultaneously or stall, the combined current draw on the 5V rail can easily
surge between 2.1A and 4.2A. A 1,000 µF capacitor is meant to smooth transient dips; it
cannot supply sustained high current. A dedicated external 5V power supply rated for the
total stall current is mandatory to prevent system failure.
5. Missing Block Diagram
The critique regarding the missing visual element is logically and professionally sound. In
hardware engineering presentations, a block diagram is a mandatory requirement to illustrate
power distribution, signal routing, and component interfacing. Presenting a slide with only
a title and no corresponding graphic is a critical quality assurance failure.


                                             3
