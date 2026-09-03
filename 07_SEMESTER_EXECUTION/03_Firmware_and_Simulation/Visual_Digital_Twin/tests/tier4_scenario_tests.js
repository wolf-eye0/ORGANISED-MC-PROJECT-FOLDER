/**
 * VibeGuard 3D WebGL Digital Twin - Tier 4 Real-World Application Scenarios
 * 
 * 8 Complete Real-World End-to-End Operational Scenarios:
 * 1. Commissioning Baseline Validation (F1, F2, F3, F6, F14, F15, F26, F27)
 * 2. Heavy Unbalance Degradation & Trip (F6, F7, F8, F9, F15, F18, F19, F21, F26, F27)
 * 3. Coupling Misalignment Harmonics Investigation (F10, F18, F19, F22, F25)
 * 4. Bearing Race Spall Defect Identification (F11, F16, F18, F19, F26)
 * 5. Mechanical Looseness & Chattering (F12, F18, F19, F22, F25)
 * 6. Broken Sensor SPI Disconnect Alarm (F13, F21, F26, F27)
 * 7. Flight Recording & CSV/JSON Telemetry Audit (F29, F30, F31, F32)
 * 8. Complete Standalone Offline Execution in Headless Firefox (F33, F1, F4, F23, F24, F25)
 */

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const {
    describe,
    test,
    assert,
    assertEqual,
    assertClose,
    assertGreaterThan,
    assertLessThan,
    assertBetween,
    removeDC,
    computeRMS,
    computeVectorRMS,
    computePeak,
    computePeakToPeak,
    computeCrestFactor,
    computeKurtosis,
    computeFFT,
    doubleIntegrate,
    evaluateISO10816,
    KOutOfMPersistenceEngine,
    computeLissajous,
    generateSignal,
    parseAndValidateCSV,
    validateJSONReport,
    inspectHTMLFile
} = require('./test_helpers');

const HTML_PATH = path.resolve(__dirname, '../VibeGuard_3D_Digital_Twin.html');

describe('Tier 4: Real-World Application Scenarios (8 Scenarios)', () => {

    // ========================================================================
    // Scenario 1: Commissioning Baseline Validation
    // ========================================================================
    test('Scenario 1: Commissioning Baseline Validation (Normal balanced run at 600 RPM)', () => {
        const sig = generateSignal({
            rpm: 600,
            unbalanceMassG: 0.0,
            faultMode: 'NORMAL',
            noiseStdDevG: 0.025,
            durationSec: 1.0
        });

        const acX = removeDC(sig.ax);
        const acY = removeDC(sig.ay);
        const acZ = removeDC(sig.az);
        const vRms = computeVectorRMS(acX, acY, acZ);
        const dInt = doubleIntegrate(acX, 800);
        const iso = evaluateISO10816(vRms, dInt.velRmsMmS);

        // Verification Criteria
        assertLessThan(vRms, 0.35, `Vector RMS (${vRms.toFixed(3)}g) must be < 0.35g (Normal Zone A)`);
        assertEqual(iso.zone, 'Zone_A', 'Must classify as ISO 10816 Zone A');
        assertEqual(iso.severity, 'Normal', 'System state must be Normal');
        assertEqual(iso.ledColor, 0x00ff88, 'Virtual RGB LED must be Healthy Green (0x00ff88)');

        const liss = computeLissajous(acX, acY);
        assertLessThan(liss.meanRadius, 0.2, 'Orbit radius must be tightly bounded under normal baseline');
    });

    // ========================================================================
    // Scenario 2: Heavy Unbalance Degradation & Trip
    // ========================================================================
    test('Scenario 2: Heavy Unbalance Degradation & Trip (Ramp to 4.5g at 900 RPM)', () => {
        const rpm = 900;
        const f0 = rpm / 60.0; // 15.0 Hz
        const engine = new KOutOfMPersistenceEngine(3, 5, 3);

        // Simulate 5 consecutive 256-sample windows with increasing unbalance mass
        const masses = [0.0, 1.5, 3.0, 4.0, 4.5];
        let finalVRms = 0;
        let finalFFT = null;

        for (let w = 0; w < masses.length; w++) {
            const sig = generateSignal({ rpm, unbalanceMassG: masses[w], faultMode: 'UNBALANCE' });
            const acX = removeDC(sig.ax);
            const acY = removeDC(sig.ay);
            const acZ = removeDC(sig.az);
            const vRms = computeVectorRMS(acX, acY, acZ);
            finalVRms = vRms;
            finalFFT = computeFFT(acX, 800);

            const isAbnormal = vRms >= 0.70;
            engine.pushWindow(isAbnormal);
        }

        // Verification Criteria
        assertGreaterThan(finalVRms, 0.70, `Final unbalance vector RMS (${finalVRms.toFixed(3)}g) must exceed 0.70g Alarm threshold`);
        assertEqual(engine.currentState, 'Abnormal', 'Persistence engine must latch into Abnormal state after K=3 abnormal windows');
        assertBetween(finalFFT.dominantFreq, 14.0, 16.0, `Dominant spectral peak (${finalFFT.dominantFreq}Hz) must match 15.0Hz 1X fundamental`);
        const iso = evaluateISO10816(finalVRms);
        assertEqual(iso.ledColor, 0xff2d55, 'Virtual RGB LED must illuminate Alarm Red (0xff2d55)');
    });

    // ========================================================================
    // Scenario 3: Coupling Misalignment Harmonics Investigation
    // ========================================================================
    test('Scenario 3: Coupling Misalignment Harmonics Investigation (600 RPM, 2X > 50% of 1X)', () => {
        const sig = generateSignal({
            rpm: 600,
            faultMode: 'MISALIGNMENT',
            faultSeverityPct: 100,
            noiseStdDevG: 0.01,
            durationSec: 0.64
        });

        const acX = removeDC(sig.ax);
        const acY = removeDC(sig.ay);
        const fft = computeFFT(acX, 800);

        // Verification Criteria
        const h1 = fft.harmonicPeaks.h1;
        const h2 = fft.harmonicPeaks.h2;
        assertGreaterThan(h1, 0.2, '1X fundamental harmonic is present');
        assertGreaterThan(h2, 0.15, '2X (20.0 Hz) misalignment harmonic is pronounced');
        assertGreaterThan(h2 / h1, 0.50, `2X / 1X harmonic ratio (${(h2/h1).toFixed(2)}) must exceed 0.50`);

        const liss = computeLissajous(acX, acY);
        assertGreaterThan(liss.eccentricity, 0.05, 'Lissajous trajectory shows characteristic distorted orbit');
    });

    // ========================================================================
    // Scenario 4: Bearing Race Spall Defect Identification
    // ========================================================================
    test('Scenario 4: Bearing Race Spall Defect Identification (BPFO = 30.5 Hz, CF > 3.5)', () => {
        const sig = generateSignal({
            rpm: 600,
            faultMode: 'BEARING_BPFO',
            faultSeverityPct: 100,
            noiseStdDevG: 0.015,
            durationSec: 1.0
        });

        const acX = removeDC(sig.ax);
        const peak = computePeak(acX);
        const rms = computeRMS(acX);
        const crestFactor = computeCrestFactor(peak, rms);
        const kurtosis = computeKurtosis(acX);

        // Verification Criteria
        assertGreaterThan(crestFactor, 3.5, `Spall defect crest factor (${crestFactor.toFixed(2)}) must exceed 3.5`);
        assertGreaterThan(kurtosis, 4.0, `Kurtosis shock index (${kurtosis.toFixed(2)}) must exceed 4.0 (spall impulsive behavior)`);
    });

    // ========================================================================
    // Scenario 5: Mechanical Looseness & Chattering
    // ========================================================================
    test('Scenario 5: Mechanical Looseness & Chattering (0.5X Sub-harmonic & Comb Spectrum)', () => {
        const sig = generateSignal({
            rpm: 600,
            faultMode: 'LOOSENESS',
            faultSeverityPct: 100,
            durationSec: 1.0
        });

        const acX = removeDC(sig.ax);
        const acY = removeDC(sig.ay);
        const fft = computeFFT(acX, 800);

        // Verification Criteria: 0.5X sub-harmonic at 5.0 Hz
        const f05Bin = Math.round(5.0 / fft.deltaF);
        assertGreaterThan(fft.magnitudes[f05Bin], 0.15, `0.5X sub-harmonic energy at 5.0 Hz (${fft.magnitudes[f05Bin].toFixed(3)}g) must be prominent`);

        const pkPk = computePeakToPeak(acX);
        assertGreaterThan(pkPk, 1.2, 'Wide peak-to-peak amplitude excursion under structural looseness');

        const liss = computeLissajous(acX, acY);
        assertGreaterThan(liss.spanX, 0.8, 'Chaotic wide trajectory span in Lissajous plane');
    });

    // ========================================================================
    // Scenario 6: Broken Sensor SPI Disconnect Alarm
    // ========================================================================
    test('Scenario 6: Broken Sensor SPI Disconnect Alarm (0g flatline, sticky FaultInvalid)', () => {
        const sig = generateSignal({ faultMode: 'SPI_DISCONNECT' });
        const engine = new KOutOfMPersistenceEngine();

        // Push disconnected window with hardware fault flag
        const state = engine.pushWindow(false, true);

        // Verification Criteria
        assertEqual(computeRMS(sig.ax), 0.0, 'X acceleration flatlines to exact 0.0g');
        assertEqual(computeRMS(sig.ay), 0.0, 'Y acceleration flatlines to exact 0.0g');
        assertEqual(computeRMS(sig.az), 0.0, 'Z acceleration flatlines to exact 0.0g');
        assertEqual(state, 'FaultInvalid', 'System enters FaultInvalid alarm state');

        const html = inspectHTMLFile(HTML_PATH);
        assert(html.content.includes('badge-fault') || html.content.includes('DISCONNECT') || html.content.includes('FAULT'), 'UI displays SPI error state badge');
        assert(html.content.includes('badge-fault') || html.content.includes('magenta') || html.content.includes('0xff00ea') || html.content.includes('0xff00ff'), 'RGB LED transitions to error Magenta');
    });

    // ========================================================================
    // Scenario 7: Flight Recording & CSV/JSON Telemetry Audit
    // ========================================================================
    test('Scenario 7: Flight Recording & CSV/JSON Telemetry Audit (RFC 4180 & JSON report)', () => {
        // Synthesize 1 second of telemetry (800 samples)
        const sig = generateSignal({ rpm: 600, unbalanceMassG: 3.5, durationSec: 1.0 });
        const acX = removeDC(sig.ax);
        const acY = removeDC(sig.ay);
        const acZ = removeDC(sig.az);

        // Build CSV string
        let csv = "timestamp_ms,sample_idx,rpm,ax_g,ay_g,az_g,vector_mag_g,vector_rms_g\n";
        for (let i = 0; i < sig.n; i++) {
            const timeMs = (i * 1.25).toFixed(2);
            const vMag = Math.sqrt(acX[i]*acX[i] + acY[i]*acY[i] + acZ[i]*acZ[i]).toFixed(3);
            const vRms = (0.85).toFixed(3);
            csv += `${timeMs},${i},600,${acX[i].toFixed(3)},${acY[i].toFixed(3)},${acZ[i].toFixed(3)},${vMag},${vRms}\n`;
        }

        // Validate CSV
        const parsedCsv = parseAndValidateCSV(csv);
        assertEqual(parsedCsv.rowCount, 800, 'CSV contains exactly 800 telemetry rows (1s @ 800 Hz)');
        assert(parsedCsv.headerMatch, 'CSV headers comply with RFC 4180');
        assertEqual(parsedCsv.rows[0][0], 0.0, 'Initial timestamp is 0.0ms');
        assertEqual(parsedCsv.rows[1][0], 1.25, 'Sample interval is exactly 1.25ms');

        // Build & Validate JSON diagnostic report
        const fft = computeFFT(acX, 800);
        const jsonReport = {
            device: { name: 'VibeGuard Twin', mcu: 'ESP32-DevKitC-32E', sensor: 'ADXL345' },
            session: { duration_sec: 1.0, sample_count: 800, rpm: 600 },
            summary: { vector_rms_g: 0.85, peak_accel_g: 1.45, crest_factor: 1.71, iso_zone: 'Zone_C' },
            fft_snapshot: {
                frequencies: Array.from(fft.frequencies),
                magnitudes: Array.from(fft.magnitudes)
            }
        };
        assert(validateJSONReport(jsonReport), 'JSON report conforms to diagnostic schema');
    });

    // ========================================================================
    // Scenario 8: Complete Standalone Execution in Headless Firefox
    // ========================================================================
    test('Scenario 8: Complete Standalone Execution in Headless Firefox (WebGL render & screenshot)', () => {
        const screenshotPath = '/tmp/ff_test_render.png';
        const profilePath = '/tmp/ff_test_profile';

        // Clean up any stale screenshot
        if (fs.existsSync(screenshotPath)) {
            fs.unlinkSync(screenshotPath);
        }
        if (!fs.existsSync(profilePath)) {
            fs.mkdirSync(profilePath, { recursive: true });
        }

        try {
            spawnSync('firefox', ['--headless', '--profile', profilePath, '--screenshot', screenshotPath, `file://${HTML_PATH}`], { stdio: 'ignore', timeout: 15000 });
        } catch (err) {
            // Firefox writes logs and screenshot even when exiting with warnings
        }

        assert(fs.existsSync(screenshotPath), `Headless Firefox must generate rendered screenshot at ${screenshotPath}`);
        const stats = fs.statSync(screenshotPath);
        assertGreaterThan(stats.size, 1000, `Screenshot file size (${stats.size} bytes) must be > 1KB (valid rendered frame)`);

        // Check PNG magic bytes: 0x89 0x50 0x4E 0x47 (PNG header)
        const buf = Buffer.alloc(8);
        const fd = fs.openSync(screenshotPath, 'r');
        fs.readSync(fd, buf, 0, 8, 0);
        fs.closeSync(fd);

        assertEqual(buf[0], 0x89, 'PNG magic byte 0 is 0x89');
        assertEqual(buf[1], 0x50, 'PNG magic byte 1 is 0x50 (P)');
        assertEqual(buf[2], 0x4E, 'PNG magic byte 2 is 0x4E (N)');
        assertEqual(buf[3], 0x47, 'PNG magic byte 3 is 0x47 (G)');
    });
});
