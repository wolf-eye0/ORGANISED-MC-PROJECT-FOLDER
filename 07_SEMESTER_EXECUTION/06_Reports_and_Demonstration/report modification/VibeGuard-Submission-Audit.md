# VibeGuard Submission Audit

## Review scope

The reviewed submission is **VibeGuard_Overleaf_Report.pdf** (67 PDF pages); **VibeGuard_Final_Report_Overleaf__1.pdf** is the initial comparison copy (68 pages). The final copy incorporates substantial revisions, but several explicit requests remain incomplete, and internal technical contradictions require correction before submission.[^1][^2]

**Page convention:** “PDF p.” means the page number shown by the PDF viewer, counting the cover as page 1. From PDF p. 23 onward, the printed body page is PDF page minus 22. Thus PDF p. 52 is printed p. 30. Notes such as “×”, “PO table at mc”, “Table(out)”, and “Sample” are abbreviated; interpretations are stated rather than treated as certain institutional requirements.

## Requested changes checklist

| Requested change | Status | Evidence and remaining action |
|---|---|---|
| October 2026 | Done | Cover, certificate, and body footers use October 2026. [^2] |
| Remove brackets around Sagna | Done | Cover now uses “Ms. Sagna L T” without the initial version’s square brackets. [^2][^1] |
| Names alphabetically | Done | Amith Krishna Das, Archa Pramod, Nihad P C, Sreehari K, Sreeprada K S appear in this order on the cover and declaration. [^2] |
| Place/date removed or repositioned | Partly / ambiguous | Declaration PDF p. 2 retains Place: THRISSUR and Date: 06-10-2026, on the right. This satisfies “Place ryt”, but not an instruction to remove them altogether. Retain only the actual approved place and signing date. [^2] |
| Signature above names | Incomplete | Declaration names are closely stacked without separate designated signature spaces above each name. Certificate has available space above staff names, but the PDF is unsigned. Provide individual signature spaces and obtain required signatures. [^2] |
| PO–CO table for microcontrollers | Substantially done | PDF p. 9 combines Microcontrollers COs and a mapping matrix. It identifies PBCST504; correctness of the exact course code and mapping needs the faculty-approved syllabus. [^2] |
| Organisation section: 1.5/spacing | Partly / ambiguous | Organisation is section 1.6, not 1.5; it says “seven subsequent chapters” although only Chapters 2–7 follow. If “1.5” means line spacing, the PDF alone does not establish the intended source setting; rendered body baselines are approximately 25.9 points for 12-point text. [^2] |
| Remove bill | Conditional | No purchase invoice/costed bill appears, but a hardware bill-of-materials/component table remains at PDF p. 45. That is not a receipt; remove it only if the instruction specifically meant all BOM content. [^2] |
| Correct block diagram | Partly | Figures 3.1 and 3.2 are present, but the detailed architecture still shows older state names and an outdated “Revised 2024” label. It does not fully match the newer J(t) pipeline. PDF pp. 33–34. [^2] |
| Pinout diagram | Present, not consistently correct | Figure 3.3 and Table 3.1 exist at PDF p. 35, but Figure 3.4 at PDF p. 36 contradicts their chip-select and RGB connections. [^2] |
| Architecture diagram | Present; update required | Figure 3.2 is present but should include the actual filtering, J(t), threshold/hysteresis, warning/alarm, and dashboard path used by the final implementation. [^2] |
| Results: no equations; photo + table | Done in structure | Chapter 5 has physical photographs, tables, calibration logs, and dashboard graphs, without a displayed numbered-equation block. Its numerical consistency still needs correction. PDF pp. 51–58. [^2] |
| Design: equations, algorithm, flowchart | Present; layout/correctness fixes | Chapter 3 includes formulations, Algorithm 1, and Figure 3.5. The flowchart caption collides with the footer and its decision logic is underspecified. PDF pp. 37–43. [^2] |
| Remove Chapter 7; appendix code, ten lines | Not done | “CHAPTER 7 CODE” remains on PDF p. 62 and in the contents. Listings span approximately 30, 34, and 28 numbered lines, not ten. Move the approved excerpt to Appendix A and update the contents and Organisation section. [^2] |
| Tables inside page / changed tables | Not done | Tables 5.2, 5.3, and 5.5 visibly extend off the right page edge, clipping the last column. PDF pp. 52, 56, 57. [^2] |
| Table borders removed (“Table(out)”) | Ambiguous | Ruled/boxed tables remain. If this meant removing outer borders, the change was not made; if it meant overflow, overflow also remains. [^2] |
| Footer | Done on body pages | College/location left and department/month right are present; front matter uses roman page numbering without the same body footer. Whether every preliminary page requires it depends on the template. [^2] |
| Times New Roman | Not done literally | Embedded body fonts are NimbusRomNo9L regular/bold/italic, not Times New Roman; the initial copy used the same family. Switch fonts if literal Times New Roman is required. [^2][^1] |
| College mission and vision | Inserted; wording approval needed | College vision/mission are on PDF p. 4; department vision/mission on p. 5. The college wording differs from the official public material checked; department wording matches the current department page. Do not replace approved new wording merely because an older official page differs. [^2][^3] |
| Header with Jyothi symbol | Partly | Jyothi letterhead appears on the cover and selected preliminary pages, including pp. 4–6, 8–9. Regular body headers contain only the report title and page number. Add the symbol to regular headers only if that was the requested scope. [^2] |
| Graph | Done | Figures 5.2–5.3 contain dashboard time-series graphs. They are screenshots, not standalone measured FFT plots. [^2] |
| Results page / sample output | Substantially done | Chapter 5 begins at PDF p. 51; photographs, sample calibration output, and dashboards are included. “Sample” is too abbreviated to determine whether a separate sample-calculation section was intended. [^2] |
| Normal-to-alarm transition | Present; description inconsistent | Figure 5.3 shows the transition, but its current reading, peak value, state text, and LED description do not all match the accompanying paragraph. PDF p. 55. [^2] |
| RGB alerts | Present; consistency fixes | Photographs, truth table, and indicator code are included. GPIO colors, standby/calibration behavior, and solid/flashing/strobe terminology differ across sections. [^2] |

## Submission blockers

### Conflicting wiring diagrams

Table 3.1 at PDF p. 35 specifies CS = GPIO21, Green = GPIO25, Blue = GPIO26, Red = GPIO27. Figure 3.4 at PDF p. 36 instead says CS = GPIO5, Red = GPIO25, Green = GPIO26, Blue = GPIO27, and 220-ohm LED resistors; the hardware text/table specifies 330 ohms. Its labels also mention ±16g and 240 MHz while the selected configuration elsewhere is ±4g and 160 MHz.[^2]

**Required correction:** Verify the actual board wiring and firmware constants, choose one authoritative as-built map, then redraw both diagrams and update every related table. Table 3.1’s MOSI/MISO “VSPI Data In/Data Out” descriptions should also be written from a clear master/sensor perspective. The ADXL345 datasheet specifies SPI CPOL = 1, CPHA = 1, so Figure 3.4’s “Mode 3 / Mode 0” wording should be replaced by the actual supported setting, Mode 3.[^4][^2]

### Code appendix not implemented

Chapter 7 remains a main chapter across PDF pp. 62–65. This directly conflicts with the likely meaning of “Chal 7 × appendix code 10 line”.[^2]

**Required correction:** Remove the numbered code chapter, create Appendix A, include the faculty-requested approximately ten-line core excerpt, and identify where the complete real firmware is available. Update the contents, cross-references, list of listings if used, and section 1.6. Do not simply remove code without preserving an implementation reference.

### Table and flowchart overflow

Table 5.2 (PDF p. 52), Table 5.3 (p. 56), and Table 5.5 (p. 57) lose their rightmost content beyond the physical page boundary. Table 3.1 also exceeds the regular right text margin, although its visible content remains on the page. Figure 3.5’s last box, caption, and footer overlap at PDF p. 43.[^2]

**Required correction:** Use wrapping columns, shorter headings, or a landscape page; do not solve clipping only by shrinking everything to unreadable text. Scale/reflow the flowchart so its caption stays above the footer. Inspect the exported PDF rather than relying only on a successful Overleaf compilation.

### Timing contradictions

The report defines 256 samples at 800 Hz, giving a 320 ms analysis window. It also reports 50 consecutive windows in 8 seconds, 100 windows in 16 seconds, and profiling “per 160 ms window”. Those timings imply a different hop/update interval from the non-overlapping acquisition loop printed in Listing 7.1.[^2]

For non-overlapping windows, 50 windows represent 16 seconds and 100 represent 32 seconds, before extra processing overhead. A 160 ms hop may be possible with overlapping windows, but this requires an explicit 128-sample hop/ring-buffer description; calibration warm-up must also be accounted for.[^2]

**Required correction:** Document window length, hop size, overlap, acquisition scheduling, and measurement timestamps separately. Recheck the claimed 1.28-second alert latency against the actual K-of-M logic and actual run logs; multiplying four windows by 0.32 seconds is not, by itself, experimental latency evidence.

### Code versus proposed method

Listing 7.1 compares Vector RMS in g against `warning_threshold_g` and `alarm_threshold_g`, whereas Algorithm 1 describes classification using dimensionless J(t). Listing 7.1 also reads a sensor sample and then delays 1250 microseconds, so the total sample-to-sample interval includes read/loop overhead; it does not establish an exact zero-jitter 800 Hz rate.[^2]

Listing 7.2 is called only once after the acquisition block in the shown loop. Consequently, that loop cannot demonstrate an 80 ms on/off alarm strobe while blocked for approximately 320 ms acquiring samples. The separate timer/task that actually services the LED, if present, must be shown or explained.[^2]

**Required correction:** Use a real excerpt from the submitted firmware, distinguish illustrative pseudocode from production code, and align the diagram, method, code, and results. ADXL345 DATA_READY synchronization or stream/FIFO handling should be documented where used; the datasheet explicitly addresses synchronization of host reads.[^4]

### Threshold and state contradictions

Table 5.1 reports Stage 2 at J(t) = 5.70 ± 0.26 and labels it ALARM, while Table 5.2 gives an alarm entry threshold of 5.80. This is not impossible with time-varying readings and hysteresis, but the report must explain entry history instead of implying that the mean alone causes the transition.[^2]

Stage 3 is reported at J(t) = 8.90 ± 0.38, below the listed 10.50 entry threshold for the Stage 2-to-3 transition. Algorithm 1 accepts T23 as an input but never uses it, and the indicator code gives the same fast-red pattern to all ALARM states. Table 5.1 assigns stationary operation blue standby, while the truth table reserves solid blue for calibration.[^2]

**Required correction:** Decide whether stages are physical test configurations or distinct firmware states. Publish one transition table with enter threshold, exit threshold, persistence, output state, and RGB pattern; preserve physical stage labels separately if needed.

## Numerical results needing verification

These checks use the values printed in the report; they are not replacement measurements. Recompute from the original per-window logs before changing a result.[^2]

| Check | Printed statement/data | Audit finding |
|---|---|---|
| Stage 1 Vector RMS | Axis RMS 0.584, 0.492, 0.210 g; vector 0.842 g | Root-sum-square of the displayed axis values is approximately 0.792 g, not 0.842 g. If columns use different aggregation procedures, define those procedures and show matched-window evidence. [^2] |
| Stage 2 Vector RMS | Axis RMS 0.785, 0.662, 0.295 g; vector 1.079 g | Root-sum-square is approximately 1.068 g. Smaller discrepancy, but still check rounding and aggregation. [^2] |
| Claimed 423% increase | Baseline 0.013–0.060 g, fault 1.079 g | Increase is approximately 1698% relative to 0.060 g, or 8200% relative to 0.013 g, not 423%. State the actual same-run baseline used. This error repeats in the abstract and results summary. [^2] |
| “16-fold energy” | Spectral magnitudes 0.014 g and 0.224 g | Magnitude ratio is 16. Energy/power proxy scales with squared magnitude under equivalent normalization, giving 256, not 16. Use “16-fold spectral amplitude” unless an actual energy measure was calculated. [^2] |
| Exact 10 Hz FFT peak | 800 Hz / 256 = 3.125 Hz bins | Nearby bins are 9.375 and 12.5 Hz. Claim “near the 10 Hz shaft frequency” unless an interpolation method and its uncertainty are shown. [^2] |
| Autocorrelation work | “51 MAC operations” | The printed nested loop performs 8976 multiply-accumulate iterations for N = 256 and lags 55–105. Fifty-one is the number of lags, not MACs. The printed function also lacks the claimed three-point interpolation. PDF pp. 40 and 64. [^2] |
| Calibration baseline | Log rx0 = 0.00515, ry0 = 0.00646, rz0 = 0.00942 | These differ substantially from the healthy-running axis values in Table 5.1. Explain whether they are filtered signals, a different run, or a different configuration. [^2] |

### Dashboard interpretation

Figure 5.3 shows a **current Vector RMS of 0.758 g**, a plotted historical maximum around **1.0794 g**, an **ALARM** banner, and **RED -  solid** in the hardware panel. The paragraph calls the banner “CRITICAL ALARM”, states that a persistence meter saturated at 100%, and describes a fast-red hardware strobe; the reproduced screenshot does not establish all those details.[^2]

**Required correction:** Describe current reading and historical peak separately. Use the actual visible state text; explain hysteresis/latching if the state remains ALARM below the plotted raw-RMS threshold. Capture an updated genuine dashboard output if the screenshot predates the final firmware. A static image cannot independently verify flash frequency.

## Claims exceeding the evidence

### Substrate-invariance proof

Equations 3.14–3.15 cancel a scale factor only when both current and baseline quantities share that same factor. If a baseline is stored on one substrate and only the subsequent measurement changes after relocation, the factor does not cancel from the stored denominator. Moreover, the proof assumes a common multiplicative response; it does not establish every possible mounting response.[^2]

**Required correction:** Replace “guaranteeing identical threshold performance across any mounting substrate without recalibration” with a limited, assumption-specific claim. If genuine cross-substrate experiments exist, include substrate identities, baseline treatment, repeated runs, and results. Otherwise describe the method as baseline normalization rather than universal proven invariance.

### Empirical performance claims

The initial report explicitly said final quantitative validation was unavailable. The revised copy introduces specific measured results, calibration logs, execution times, and strong claims such as “100% false-alarm rejection”, “permanently eliminates”, and industrial protection. This change can be legitimate, but supporting raw records are not supplied with these two PDFs, so their authenticity and reproducibility cannot be independently established from the reports alone.[^1][^2]

**Required correction:** Retain only real measurements and provide a run/evidence manifest containing timestamp, physical configuration, firmware version, frozen parameters, number of independent runs, and raw-log location. Identify what ± means in Table 5.1, and distinguish correlated consecutive windows from independent tests. Prefer “no false alarms in the documented test” to a universal 100% guarantee.

Table 2.1 and Table 5.6 give generic costs, power, and latency for broad competing approaches without method-specific evidence. The report’s references are largely project documents, device documentation, one ISO standard, and one textbook rather than studies establishing those benchmark ranges.[^2]

**Required correction:** Cite actual comparable systems, label the tables as qualitative design comparisons, or remove unsupported numerical ranges. State whether “under 1.5 W” covers only the monitor electronics or includes the motor and host computer; provide the measurement method if reported as measured performance.

## Front matter and typography

| Location | Issue | Recommended correction |
|---|---|---|
| PDF p. 3, certificate | Says “seminar report” despite being a micro-project report. [^2] | Change to “micro project report” and have the certificate approved before signatures. |
| PDF p. 10, acknowledgement | Principal appears as “Dr. Sojan P Lal”. [^2] | Use the official “Dr. P. Sojan Lal”. [^5] |
| PDF p. 8 | “PROGRAMME SPECIFIC OBJECTIVES (PSOs)” conflicts with the official “Programme Specific Outcomes”. [^2] | Change the heading to Outcomes. |
| PDF pp. 10–11 | Two student names spill onto an otherwise almost empty page. [^2] | Keep the author block together and rebalance the acknowledgement. |
| PDF pp. 15–16 | Abstract spills onto a short second page. [^2] | Condense it to the approved length, removing repeated claims and correcting percentages/FFT terminology. |
| PDF pp. 20–21 | “LIST OF ABBREVIATIONS” occupies a heading-only page, with entries starting on the next page. [^2] | Keep the heading with the entries. |
| PDF p. 17, contents | References are absent; code remains Chapter 7. [^2] | Include References and the new Appendix A, then regenerate all lists. |
| PDF p. 26, section 1.6 | “Seven subsequent chapters” does not match Chapters 2–7. [^2] | Rewrite after moving code to an appendix; there would be five following body chapters, 2–6. |
| PDF p. 39 | Literal Markdown asterisks surround a phrase inside the typeset text. [^2] | Replace with LaTeX emphasis rather than printing `**`. |
| Body text | Embedded font is Nimbus Roman, not literal Times New Roman. [^2] | Use XeLaTeX/LuaLaTeX with `fontspec` and `\setmainfont{Times New Roman}`, then verify embedded fonts after export. [^6] |

### Mission and vision approval

The college vision in the final PDF differs from the college’s public NAAC material and the wording described on its About page. That discrepancy is a reason to verify the newest signed-off template, not a reason to assert that the PDF’s wording is necessarily wrong.[^3][^2]

The department vision/mission, PEOs, and PSOs align with the current official Cyber Security department page checked during review; the PSO **heading**, not those outcome statements, needs correction. The exact PO–CO mapping remains a faculty/syllabus approval item.

### Small technical corrections

The report calls 1N4007 a “fast recovery diode”. Vishay identifies it as a **general-purpose rectifier**; correct the component description without implying that its use for the documented switched motor is automatically invalid.[^7][^2]

Avoid “zero passband distortion” for the 25 Hz Butterworth filter unless the claimed property is defined and demonstrated. Document both biquad sections, coefficient values, sample rate, and filter-state handling if this method is genuinely implemented. The printed excerpt shows a single section-processing function, not the complete configured fourth-order cascade.[^2]

## Recommended correction order

1. Verify the actual firmware and wiring; reconcile GPIO assignments, resistors, sampling method, J(t)/RMS classifier, threshold rules, and LED scheduling.
2. Verify raw test records and repair inconsistent tables, percentages, FFT terminology, timing, and screenshot descriptions. Do not invent replacement data.
3. Replace Chapter 7 with the requested short code appendix and update section 1.6 and all automatic lists.
4. Repair clipped tables and the flowchart/footer collision; improve small diagram labels at the intended print size.
5. Apply literal Times New Roman if mandatory; verify line spacing and letterhead/footer scope against the college template.
6. Correct certificate wording, principal’s name, PSO heading, signature spaces, and the actual signing date/place.
7. Recompile, inspect every page at 100% zoom, print-test the diagrams, and obtain the guide’s final approval.

**Review limit:** The PDFs support a content/layout audit, not certification that the physical system, firmware, raw measurements, signatures, or local formatting approvals are valid. The revised report is substantially improved, but the listed blockers prevent a clean submission-readiness sign-off.[^1][^2]

---

## References

1. [VibeGuard_Final_Report_Overleaf__1.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/efad5f98-9f95-4863-8ddf-b40dc2f683d9/VibeGuard_Final_Report_Overleaf__1.pdf) - DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING CYBER ...

2. [VibeGuard_Overleaf_Report.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/144580388/affb124a-fa2e-4c22-85a1-188075285f2d/VibeGuard_Overleaf_Report.pdf) - DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING CYBER ...

3. [Self Study Report of JYOTHI ENGINEERING COLLEGE](https://www.jecc.ac.in/IQAC/iqac_admin/assets/home_img/NAAC-SSR-Feb20222.pdf) - Creating eminent and ethical leaders through quality professional education with emphasis on holisti...

4. [ADXL345 (Rev - Analog](https://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf) - The ADXL345 is a small, thin, ultralow power, 3-axis accelerometer with high resolution (13-bit) mea...

5. [Dr. P. Sojan Lal - JYOTHI ENGINEERING COLLEGE](https://www.jecc.ac.in/Department/CoursesController/staffProfile/519/0) - Principal (Professor)
...
# JYOTHI ENGINEERING COLLEGE

6. [XeLaTeX - Overleaf, Online LaTeX Editor](https://www.overleaf.com/learn/latex/XeLaTeX) - Times New Roman is a commonly-used font and here's an example of its use on Overleaf via the XeLaTeX...

7. [1N4001, 1N4002, 1N4003, 1N4004, 1N4005, 1N4006, 1N4007 ...](https://www.vishay.com/en/product/88503/tab/designtools-ppg/) - Low leakage current
High forward surge capability
...
For use in general purpose rectification of po...

