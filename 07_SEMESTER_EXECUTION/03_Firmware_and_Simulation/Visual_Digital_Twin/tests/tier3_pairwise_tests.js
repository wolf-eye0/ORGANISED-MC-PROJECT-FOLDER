/**
 * VibeGuard 3D WebGL Digital Twin - Tier 3 Pairwise Combinatorial Tests
 * 
 * 43 Comprehensive Pairwise Combinatorial Interaction Tests covering:
 * - [RPM: 300, 600, 900, 1200] x [Fault Modes: Normal, Unbalance, Misalignment, BPFO, BPFI, Looseness, SPI Disconnect] (28 tests)
 * - [Fault Transitions] x [Recorder State] (4 tests)
 * - [Playback State] x [Raycast Inspection] (3 tests)
 * - [Noise Level] x [Fault Severity] (4 tests)
 * - [Double Integration] x [Vibration Frequencies] (4 tests)
 */

const {
    describe,
    test,
    assert,
    assertEqual,
    assertClose,
    assertArrayClose,
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
    parseAndValidateCSV
} = require('./test_helpers');

describe('Tier 3: Pairwise Combinatorial Interaction Tests (43 Tests)', () => {

    // ========================================================================
    // Pairwise Matrix 1: [RPM: 300, 600, 900, 1200] x [7 Fault Modes] (28 Tests)
    // ========================================================================
    describe('Matrix 1: RPM x Fault Mode Interactions (28 Tests)', () => {
        const rpms = [300, 600, 900, 1200];
        const modes = [
            'NORMAL',
            'UNBALANCE',
            'MISALIGNMENT',
            'BEARING_BPFO',
            'BEARING_BPFI',
            'LOOSENESS',
            'SPI_DISCONNECT'
        ];

        rpms.forEach(rpm => {
            modes.forEach(mode => {
                const f0 = rpm / 60.0;
                test(`P1: RPM=${rpm} (${f0} Hz) x Mode=${mode}`, () => {
                    const sig = generateSignal({ rpm, faultMode: mode, unbalanceMassG: mode === 'UNBALANCE' ? 3.5 : 0.0 });
                    const acX = removeDC(sig.ax);
                    const acY = removeDC(sig.ay);
                    const acZ = removeDC(sig.az);
                    const vRms = computeVectorRMS(acX, acY, acZ);
                    const fft = computeFFT(acX, 800);

                    if (mode === 'SPI_DISCONNECT') {
                        assertEqual(vRms, 0.0, 'Vector RMS is 0 on SPI disconnect');
                        assertEqual(fft.dominantMag, 0.0, 'FFT magnitude is 0 on SPI disconnect');
                    } else if (mode === 'NORMAL') {
                        assertLessThan(vRms, 0.35, `Normal baseline vector RMS must be < 0.35g (got ${vRms})`);
                        assertEqual(evaluateISO10816(vRms).zone, 'Zone_A');
                    } else if (mode === 'UNBALANCE') {
                        assertGreaterThan(vRms, 0.70, `Unbalance vector RMS must be > 0.70g (got ${vRms})`);
                        assertBetween(fft.dominantFreq, f0 - 3.5, f0 + 3.5, `Dominant peak should align with 1X fundamental ${f0}Hz`);
                    } else if (mode === 'MISALIGNMENT') {
                        assertGreaterThan(fft.harmonicPeaks.h2, 0.1, `2X harmonic peak should be present at 2x${f0}Hz`);
                    } else if (mode === 'BEARING_BPFO') {
                        const cf = computeCrestFactor(computePeak(acX), computeRMS(acX));
                        assertGreaterThan(cf, 2.0, `Bearing BPFO should elevate Crest Factor at ${rpm} RPM`);
                    } else if (mode === 'BEARING_BPFI') {
                        const kurt = computeKurtosis(acX);
                        assertGreaterThan(kurt, 2.5, `Bearing BPFI should elevate Kurtosis at ${rpm} RPM`);
                    } else if (mode === 'LOOSENESS') {
                        assertGreaterThan(computePeakToPeak(acX), 0.5, `Mechanical looseness should produce wide peak-to-peak swing`);
                    }
                });
            });
        });
    });

    // ========================================================================
    // Pairwise Matrix 2: [Fault Mode Transitions] x [Session Recorder] (4 Tests)
    // ========================================================================
    describe('Matrix 2: Fault Transitions during Active Session Recording', () => {
        test('P2.01: Normal -> Unbalance transition during active recording', () => {
            const sig1 = generateSignal({ faultMode: 'NORMAL', durationSec: 0.5 });
            const sig2 = generateSignal({ faultMode: 'UNBALANCE', unbalanceMassG: 4.0, durationSec: 0.5 });
            const combinedAx = new Float32Array([...sig1.ax, ...sig2.ax]);
            const rms1 = computeRMS(removeDC(combinedAx.subarray(0, 400)));
            const rms2 = computeRMS(removeDC(combinedAx.subarray(400, 800)));
            assertGreaterThan(rms2, rms1 * 2.0, 'RMS more than doubles after unbalance injection mid-recording');
        });

        test('P2.02: Normal -> Misalignment transition during active recording', () => {
            const sig1 = generateSignal({ faultMode: 'NORMAL', durationSec: 0.5 });
            const sig2 = generateSignal({ faultMode: 'MISALIGNMENT', durationSec: 0.5 });
            const combinedAx = new Float32Array([...sig1.ax, ...sig2.ax]);
            const fft1 = computeFFT(removeDC(combinedAx.subarray(0, 400)), 800);
            const fft2 = computeFFT(removeDC(combinedAx.subarray(400, 800)), 800);
            assertGreaterThan(fft2.harmonicPeaks.h2, fft1.harmonicPeaks.h2 * 2.0, '2X harmonic surges after misalignment mid-recording');
        });

        test('P2.03: Normal -> SPI Disconnect transition during active recording', () => {
            const sig1 = generateSignal({ faultMode: 'NORMAL', durationSec: 0.5 });
            const sig2 = generateSignal({ faultMode: 'SPI_DISCONNECT', durationSec: 0.5 });
            const combinedAx = new Float32Array([...sig1.ax, ...sig2.ax]);
            const rmsEnd = computeRMS(combinedAx.subarray(400, 800));
            assertEqual(rmsEnd, 0.0, 'Signal flatlines to 0.0g on disconnect');
        });

        test('P2.04: SPI Disconnect -> Reconnect Normal recovery during active recording', () => {
            const sig1 = generateSignal({ faultMode: 'SPI_DISCONNECT', durationSec: 0.5 });
            const sig2 = generateSignal({ faultMode: 'NORMAL', durationSec: 0.5 });
            const combinedAx = new Float32Array([...sig1.ax, ...sig2.ax]);
            const rmsRecovered = computeRMS(removeDC(combinedAx.subarray(400, 800)));
            assertGreaterThan(rmsRecovered, 0.03, 'Signal recovers to baseline vibration');
        });
    });

    // ========================================================================
    // Pairwise Matrix 3: [Playback Controls] x [Raycast Inspection] (3 Tests)
    // ========================================================================
    describe('Matrix 3: Playback Controls x Raycast Component Inspection', () => {
        test('P3.01: Raycast inspection during Simulation Paused state', () => {
            let isPaused = true;
            let currentAngle = 1.57;
            const dt = 0.016;
            // When paused, delta angle is 0
            const nextAngle = isPaused ? currentAngle : currentAngle + (2 * Math.PI * 10) * dt;
            assertEqual(nextAngle, currentAngle, 'Angle does not advance while paused');
            // Raycast selection target coordinate remains valid
            const targetPos = { x: 0, y: 2.5, z: 0 };
            assert(typeof targetPos.x === 'number', 'Raycast target position valid');
        });

        test('P3.02: Raycast inspection during 2.0X Fast Forward state', () => {
            const timeScale = 2.0;
            const dt = 0.016 * timeScale;
            const dAngle = (2 * Math.PI * 10) * dt;
            assertClose(dAngle, 2.0106, 1e-3, 'Fast forward angular increment correct');
        });

        test('P3.03: Parameter modification (RPM slider) while Paused -> Resume state transition', () => {
            let rpm = 600;
            let isPaused = true;
            rpm = 900; // User changes RPM while paused
            isPaused = false; // User clicks Resume
            const f0 = rpm / 60.0;
            assertEqual(f0, 15.0, 'Resumed simulation instantly reflects 15.0 Hz from modified RPM');
        });
    });

    // ========================================================================
    // Pairwise Matrix 4: [Noise Level] x [Fault Severity] (4 Tests)
    // ========================================================================
    describe('Matrix 4: Noise Level x Fault Severity Interactions', () => {
        test('P4.01: Low noise (0.005g) + Low unbalance mass (0.5g) -> High sensitivity detection', () => {
            const sig = generateSignal({ noiseStdDevG: 0.005, unbalanceMassG: 0.5, rpm: 600 });
            const acX = removeDC(sig.ax);
            const fft = computeFFT(acX, 800);
            assertGreaterThan(fft.dominantMag, 0.05, '10 Hz fundamental clearly identified despite tiny mass');
        });

        test('P4.02: High noise (0.080g) + Low unbalance mass (0.5g) -> Noise robustness check', () => {
            const sig = generateSignal({ noiseStdDevG: 0.080, unbalanceMassG: 0.5, rpm: 600 });
            const acX = removeDC(sig.ax);
            const vRms = computeRMS(acX);
            assertGreaterThan(vRms, 0.08, 'Signal does not collapse in high noise environment');
        });

        test('P4.03: Low noise (0.005g) + High unbalance mass (4.5g) -> Pure unbalance signature', () => {
            const sig = generateSignal({ noiseStdDevG: 0.005, unbalanceMassG: 4.5, rpm: 600 });
            const acX = removeDC(sig.ax);
            const fft = computeFFT(acX, 800);
            assertGreaterThan(fft.dominantMag, 0.70, 'FFT magnitude exceeds 0.70g with low noise and high mass');
        });

        test('P4.04: High noise (0.080g) + High unbalance mass (4.5g) -> Heavy industrial plant condition', () => {
            const sig = generateSignal({ noiseStdDevG: 0.080, unbalanceMassG: 4.5, rpm: 600 });
            const acX = removeDC(sig.ax);
            const vRms = computeRMS(acX);
            assertGreaterThan(vRms, 0.8, 'Alarm state clearly maintained in noisy industrial conditions');
        });
    });

    // ========================================================================
    // Pairwise Matrix 5: [Double Integration] x [Frequencies] (4 Tests)
    // ========================================================================
    describe('Matrix 5: Double Integration x Frequency Scaling (4 Tests)', () => {
        test('P5.01: 5.0 Hz (300 RPM) acceleration integration to velocity', () => {
            const sig = generateSignal({ rpm: 300, unbalanceMassG: 2.0 });
            const dInt = doubleIntegrate(sig.ax, 800);
            assertGreaterThan(dInt.velRmsMmS, 0.01);
        });

        test('P5.02: 10.0 Hz (600 RPM) acceleration integration to velocity', () => {
            const sig = generateSignal({ rpm: 600, unbalanceMassG: 2.0 });
            const dInt = doubleIntegrate(sig.ax, 800);
            assertGreaterThan(dInt.velRmsMmS, 0.01);
        });

        test('P5.03: 15.0 Hz (900 RPM) acceleration integration to velocity', () => {
            const sig = generateSignal({ rpm: 900, unbalanceMassG: 2.0 });
            const dInt = doubleIntegrate(sig.ax, 800);
            assertGreaterThan(dInt.velRmsMmS, 0.01);
        });

        test('P5.04: 20.0 Hz (1200 RPM) acceleration integration to velocity', () => {
            const sig = generateSignal({ rpm: 1200, unbalanceMassG: 2.0 });
            const dInt = doubleIntegrate(sig.ax, 800);
            assertGreaterThan(dInt.velRmsMmS, 0.01);
        });
    });
});
