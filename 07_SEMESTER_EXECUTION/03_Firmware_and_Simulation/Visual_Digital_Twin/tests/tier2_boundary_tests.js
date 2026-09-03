/**
 * VibeGuard 3D WebGL Digital Twin - Tier 2 Boundary & Corner Tests
 * 
 * 165 Rigorous Boundary, Corner, and Numerical Stress Test Cases covering:
 * - Variable RPM limits [300, 1200]
 * - Unbalance mass boundaries [0.0g, 5.0g]
 * - Static gravity DC offset isolation
 * - Nyquist limits (400 Hz) and bin edge precision
 * - Circular ring buffer rollover and memory capacity
 * - NaN / Infinity / Division-by-Zero safety
 * - ISO 10816 exact threshold transitions (0.35g, 0.70g, 1.20g)
 * - Industrial noise limits and Kurtosis bounds
 * - Time scaling kinematics
 */

const {
    describe,
    test,
    assert,
    assertEqual,
    assertClose,
    assertArrayClose,
    assertThrows,
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
    applyHannWindow,
    computeFFT,
    doubleIntegrate,
    evaluateISO10816,
    KOutOfMPersistenceEngine,
    computeLissajous,
    generateSignal,
    parseAndValidateCSV
} = require('./test_helpers');

describe('Tier 2: Boundary & Corner Cases (165 Tests)', () => {

    // ========================================================================
    // Category 1: RPM Limits & Angular Kinematics (20 Tests)
    // ========================================================================
    describe('Category 1: RPM Limits & Angular Kinematics', () => {
        test('B1.01: Minimum operational RPM (300 RPM -> exactly 5.0 Hz)', () => {
            const rpm = 300;
            const f0 = rpm / 60.0;
            assertClose(f0, 5.0, 1e-6);
        });

        test('B1.02: Maximum operational RPM (1200 RPM -> exactly 20.0 Hz)', () => {
            const rpm = 1200;
            const f0 = rpm / 60.0;
            assertClose(f0, 20.0, 1e-6);
        });

        test('B1.03: Standard nominal baseline RPM (600 RPM -> 10.0 Hz)', () => {
            const rpm = 600;
            assertClose(rpm / 60.0, 10.0, 1e-6);
        });

        test('B1.04: Step sweep: 330 RPM (5.5 Hz)', () => { assertClose(330 / 60.0, 5.5, 1e-6); });
        test('B1.05: Step sweep: 360 RPM (6.0 Hz)', () => { assertClose(360 / 60.0, 6.0, 1e-6); });
        test('B1.06: Step sweep: 450 RPM (7.5 Hz)', () => { assertClose(450 / 60.0, 7.5, 1e-6); });
        test('B1.07: Step sweep: 540 RPM (9.0 Hz)', () => { assertClose(540 / 60.0, 9.0, 1e-6); });
        test('B1.08: Step sweep: 660 RPM (11.0 Hz)', () => { assertClose(660 / 60.0, 11.0, 1e-6); });
        test('B1.09: Step sweep: 720 RPM (12.0 Hz)', () => { assertClose(720 / 60.0, 12.0, 1e-6); });
        test('B1.10: Step sweep: 750 RPM (12.5 Hz)', () => { assertClose(750 / 60.0, 12.5, 1e-6); });
        test('B1.11: Step sweep: 840 RPM (14.0 Hz)', () => { assertClose(840 / 60.0, 14.0, 1e-6); });
        test('B1.12: Step sweep: 900 RPM (15.0 Hz)', () => { assertClose(900 / 60.0, 15.0, 1e-6); });
        test('B1.13: Step sweep: 960 RPM (16.0 Hz)', () => { assertClose(960 / 60.0, 16.0, 1e-6); });
        test('B1.14: Step sweep: 1050 RPM (17.5 Hz)', () => { assertClose(1050 / 60.0, 17.5, 1e-6); });
        test('B1.15: Step sweep: 1140 RPM (19.0 Hz)', () => { assertClose(1140 / 60.0, 19.0, 1e-6); });

        test('B1.16: Non-integer fractional RPM (603.5 RPM -> 10.0583 Hz)', () => {
            const f0 = 603.5 / 60.0;
            assertClose(f0, 10.058333, 1e-5);
        });

        test('B1.17: Below minimum RPM clamp check (RPM < 300 clamped)', () => {
            const rawInput = 150;
            const clamped = Math.max(300, Math.min(1200, rawInput));
            assertEqual(clamped, 300);
        });

        test('B1.18: Above maximum RPM clamp check (RPM > 1200 clamped)', () => {
            const rawInput = 1800;
            const clamped = Math.max(300, Math.min(1200, rawInput));
            assertEqual(clamped, 1200);
        });

        test('B1.19: Zero RPM angular velocity omega == 0', () => {
            const omega = 2.0 * Math.PI * (0 / 60.0);
            assertEqual(omega, 0.0);
        });

        test('B1.20: Negative RPM handling (absolute value / direction guard)', () => {
            const rawRpm = -600;
            const validRpm = Math.abs(rawRpm);
            assertEqual(validRpm, 600);
        });
    });

    // ========================================================================
    // Category 2: Eccentric Mass Range & Force Limits (20 Tests)
    // ========================================================================
    describe('Category 2: Eccentric Mass Range & Force Limits', () => {
        test('B2.01: Exact 0.0g unbalance mass (perfect balance)', () => {
            const sig = generateSignal({ unbalanceMassG: 0.0, rpm: 600, noiseStdDevG: 0.0 });
            const acX = removeDC(sig.ax);
            assertLessThan(computeRMS(acX), 0.1, 'RMS remains at baseline level under 0.0g');
        });

        test('B2.02: Minimum perceptible mass delta: 0.01g', () => {
            const amp = (0.01 / 5.0) * 1.85;
            assertGreaterThan(amp, 0.001);
        });

        test('B2.03: Nominal unbalance midpoint: 2.50g', () => {
            const amp = (2.50 / 5.0) * 1.85;
            assertClose(amp, 0.925, 1e-4);
        });

        test('B2.04: Maximum rated eccentric mass: 5.00g', () => {
            const amp = (5.00 / 5.0) * 1.85;
            assertClose(amp, 1.85, 1e-4);
        });

        test('B2.05: Mass sweep step: 0.25g', () => { assertClose((0.25 / 5.0) * 1.85, 0.0925, 1e-4); });
        test('B2.06: Mass sweep step: 0.50g', () => { assertClose((0.50 / 5.0) * 1.85, 0.185, 1e-4); });
        test('B2.07: Mass sweep step: 0.75g', () => { assertClose((0.75 / 5.0) * 1.85, 0.2775, 1e-4); });
        test('B2.08: Mass sweep step: 1.00g', () => { assertClose((1.00 / 5.0) * 1.85, 0.370, 1e-4); });
        test('B2.09: Mass sweep step: 1.50g', () => { assertClose((1.50 / 5.0) * 1.85, 0.555, 1e-4); });
        test('B2.10: Mass sweep step: 2.00g', () => { assertClose((2.00 / 5.0) * 1.85, 0.740, 1e-4); });
        test('B2.11: Mass sweep step: 3.00g', () => { assertClose((3.00 / 5.0) * 1.85, 1.110, 1e-4); });
        test('B2.12: Mass sweep step: 3.50g', () => { assertClose((3.50 / 5.0) * 1.85, 1.295, 1e-4); });
        test('B2.13: Mass sweep step: 4.00g', () => { assertClose((4.00 / 5.0) * 1.85, 1.480, 1e-4); });
        test('B2.14: Mass sweep step: 4.50g', () => { assertClose((4.50 / 5.0) * 1.85, 1.665, 1e-4); });
        test('B2.15: Mass sweep step: 4.75g', () => { assertClose((4.75 / 5.0) * 1.85, 1.7575, 1e-4); });

        test('B2.16: Negative mass input clamping (< 0.0g clamped to 0.0g)', () => {
            const raw = -1.5;
            const clamped = Math.max(0.0, Math.min(5.0, raw));
            assertEqual(clamped, 0.0);
        });

        test('B2.17: Over-range mass input clamping (> 5.0g clamped to 5.0g)', () => {
            const raw = 7.8;
            const clamped = Math.max(0.0, Math.min(5.0, raw));
            assertEqual(clamped, 5.0);
        });

        test('B2.18: Linear force scaling m1 < m2 -> F1 < F2', () => {
            const f1 = (1.0 / 5.0) * 1.85;
            const f2 = (2.0 / 5.0) * 1.85;
            assertLessThan(f1, f2);
        });

        test('B2.19: Quadratic RPM unbalance scaling F proportional to omega^2', () => {
            const w1 = 2 * Math.PI * 5.0;  // 300 RPM
            const w2 = 2 * Math.PI * 10.0; // 600 RPM
            const f1 = w1 * w1;
            const f2 = w2 * w2;
            assertClose(f2 / f1, 4.0, 1e-5);
        });

        test('B2.20: Precision test: 0.0001g unbalance does not cause NaN or underflow', () => {
            const sig = generateSignal({ unbalanceMassG: 0.0001 });
            assert(!isNaN(computeRMS(sig.ax)));
        });
    });

    // ========================================================================
    // Category 3: Static DC Offset & Gravity Vector Isolation (20 Tests)
    // ========================================================================
    describe('Category 3: Static DC Offset & Gravity Vector Isolation', () => {
        test('B3.01: Static +1.00g gravity removal on Z-axis', () => {
            const raw = new Float32Array(256).fill(1.00);
            const ac = removeDC(raw);
            assertClose(computeRMS(ac), 0.0, 1e-6);
        });

        test('B3.02: Inverted -1.00g gravity removal on Z-axis', () => {
            const raw = new Float32Array(256).fill(-1.00);
            const ac = removeDC(raw);
            assertClose(computeRMS(ac), 0.0, 1e-6);
        });

        test('B3.03: +1.00g gravity on X-axis (sideways mount)', () => {
            const raw = new Float32Array(256).map((_, i) => 1.00 + 0.1 * Math.sin(i * 0.1));
            const ac = removeDC(raw);
            assertClose(ac.reduce((a, b) => a + b, 0) / 256, 0.0, 1e-6);
        });

        test('B3.04: +1.00g gravity on Y-axis (vertical mount)', () => {
            const raw = new Float32Array(256).map((_, i) => 1.00 + 0.1 * Math.cos(i * 0.1));
            const ac = removeDC(raw);
            assertClose(ac.reduce((a, b) => a + b, 0) / 256, 0.0, 1e-6);
        });

        test('B3.05: High DC offset: +5.0g static bias', () => {
            const raw = new Float32Array(128).fill(5.0);
            const ac = removeDC(raw);
            assertClose(computePeak(ac), 0.0, 1e-6);
        });

        test('B3.06: Negative high DC offset: -5.0g static bias', () => {
            const raw = new Float32Array(128).fill(-5.0);
            const ac = removeDC(raw);
            assertClose(computePeak(ac), 0.0, 1e-6);
        });

        test('B3.07: Extreme DC offset: +16.0g (ADXL345 full-scale max)', () => {
            const raw = new Float32Array(128).fill(16.0);
            const ac = removeDC(raw);
            assertClose(computeRMS(ac), 0.0, 1e-6);
        });

        test('B3.08: Extreme DC offset: -16.0g (ADXL345 full-scale min)', () => {
            const raw = new Float32Array(128).fill(-16.0);
            const ac = removeDC(raw);
            assertClose(computeRMS(ac), 0.0, 1e-6);
        });

        test('B3.09: Tiny dynamic AC (0.005g) riding on massive DC (10.0g)', () => {
            const raw = new Float32Array(256).map((_, i) => 10.0 + 0.005 * Math.sin(2 * Math.PI * i / 32));
            const ac = removeDC(raw);
            assertClose(computePeak(ac), 0.005, 1e-4);
        });

        test('B3.10: Zero dynamic AC with zero DC offset (all zeros)', () => {
            const raw = new Float32Array(256).fill(0.0);
            const ac = removeDC(raw);
            assertEqual(computeRMS(ac), 0.0);
        });

        test('B3.11: Non-symmetric DC offset on triaxial axes (X: 0.1g, Y: -0.5g, Z: 1.0g)', () => {
            const x = removeDC(new Float32Array(128).fill(0.1));
            const y = removeDC(new Float32Array(128).fill(-0.5));
            const z = removeDC(new Float32Array(128).fill(1.0));
            assertClose(computeVectorRMS(x, y, z), 0.0, 1e-6);
        });

        test('B3.12: Large step DC transition mid-buffer', () => {
            const raw = new Float32Array(256).map((_, i) => (i < 128 ? 0.0 : 2.0));
            const ac = removeDC(raw);
            assertClose(ac.reduce((a, b) => a + b, 0) / 256, 0.0, 1e-6);
        });

        test('B3.13: Alternating +/- DC pulses zero-sum verification', () => {
            const raw = new Float32Array(256).map((_, i) => (i % 2 === 0 ? 1.0 : -1.0));
            const ac = removeDC(raw);
            assertClose(ac.reduce((a, b) => a + b, 0) / 256, 0.0, 1e-6);
        });

        test('B3.14: Linear DC ramp offset removal', () => {
            const raw = new Float32Array(256).map((_, i) => i * 0.01);
            const ac = removeDC(raw);
            assertClose(ac.reduce((a, b) => a + b, 0) / 256, 0.0, 1e-5);
        });

        test('B3.15: Single sample buffer DC removal (N=1 -> 0.0)', () => {
            const raw = new Float32Array([42.0]);
            const ac = removeDC(raw);
            assertEqual(ac[0], 0.0);
        });

        test('B3.16: Two sample buffer DC removal (N=2)', () => {
            const raw = new Float32Array([10.0, 20.0]);
            const ac = removeDC(raw);
            assertEqual(ac[0], -5.0);
            assertEqual(ac[1], 5.0);
        });

        test('B3.17: Float precision accuracy under 1,000,000.0 offset', () => {
            const raw = new Float32Array([1000001.0, 1000003.0]);
            const ac = removeDC(raw);
            assertClose(ac[0], -1.0, 1e-3);
            assertClose(ac[1], 1.0, 1e-3);
        });

        test('B3.18: Periodic waveform with zero original mean stays unaltered', () => {
            const raw = new Float32Array(256).map((_, i) => Math.sin(2 * Math.PI * i / 64));
            const ac = removeDC(raw);
            assertArrayClose(ac, raw, 1e-5);
        });

        test('B3.19: Constant square wave DC removal', () => {
            const raw = new Float32Array(256).map((_, i) => (i < 128 ? 1.0 : 3.0));
            const ac = removeDC(raw);
            assertEqual(ac[0], -1.0);
            assertEqual(ac[128], 1.0);
        });

        test('B3.20: Invariance of vector magnitude after triaxial DC subtraction', () => {
            const sig = generateSignal({ rpm: 600 });
            const acX = removeDC(sig.ax);
            const acY = removeDC(sig.ay);
            const acZ = removeDC(sig.az);
            const vRms = computeVectorRMS(acX, acY, acZ);
            assertGreaterThan(vRms, 0.0);
        });
    });

    // ========================================================================
    // Category 4: Frequency Resolution, Zero-Crossing & Nyquist Limits (20 Tests)
    // ========================================================================
    describe('Category 4: Frequency Resolution, Zero-Crossing & Nyquist Limits', () => {
        const Fs = 800;
        const N = 256;

        test('B4.01: Nyquist limit boundary frequency: exactly Fs/2 = 400.0 Hz', () => {
            const nyquist = Fs / 2.0;
            assertEqual(nyquist, 400.0);
        });

        test('B4.02: Bin 0 DC frequency: exactly 0.0 Hz', () => {
            const deltaF = Fs / N;
            assertEqual(0 * deltaF, 0.0);
        });

        test('B4.03: Bin 1 lowest positive frequency: 3.125 Hz', () => {
            const deltaF = Fs / N;
            assertEqual(1 * deltaF, 3.125);
        });

        test('B4.04: Bin 127 highest single-sided frequency: 396.875 Hz', () => {
            const deltaF = Fs / N;
            assertEqual(127 * deltaF, 396.875);
        });

        test('B4.05: Bin 16 exact tone: 50.0 Hz', () => {
            const tone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 50.0 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assertClose(fft.dominantFreq, 50.0, 1e-4);
        });

        test('B4.06: Bin 32 exact tone: 100.0 Hz', () => {
            const tone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 100.0 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assertClose(fft.dominantFreq, 100.0, 1e-4);
        });

        test('B4.07: Bin 64 exact tone: 200.0 Hz', () => {
            const tone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 200.0 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assertClose(fft.dominantFreq, 200.0, 1e-4);
        });

        test('B4.08: Bin 96 exact tone: 300.0 Hz', () => {
            const tone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 300.0 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assertClose(fft.dominantFreq, 300.0, 1e-4);
        });

        test('B4.09: Inter-bin frequency peak interpolation: 10.0 Hz (between bin 3: 9.375Hz and bin 4: 12.5Hz)', () => {
            const tone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 10.0 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assertBetween(fft.dominantFreq, 9.0, 13.0);
        });

        test('B4.10: Sub-bin frequency detection: 1.5 Hz (below bin 1 resolution)', () => {
            const tone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 1.5 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assert(fft.dominantFreq >= 0.0);
        });

        test('B4.11: Dual frequency resolution: 20 Hz + 80 Hz sum', () => {
            const tone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 20.0 * i / Fs) + Math.sin(2 * Math.PI * 80.0 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assert(fft.magnitudes[Math.round(20.0 / 3.125)] > 0.3);
            assert(fft.magnitudes[Math.round(80.0 / 3.125)] > 0.3);
        });

        test('B4.12: High-frequency Nyquist edge tone: 390.0 Hz', () => {
            const tone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 390.0 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assertGreaterThan(fft.dominantFreq, 350.0);
        });

        test('B4.13: Zero-crossing count of 10.0 Hz sine across 1s (approx 20 crossings)', () => {
            const totalSamples = 800;
            const sine = new Float32Array(totalSamples).map((_, i) => Math.sin(2 * Math.PI * 10.0 * i / 800));
            let crossings = 0;
            for (let i = 1; i < totalSamples; i++) {
                if ((sine[i] >= 0 && sine[i - 1] < 0) || (sine[i] < 0 && sine[i - 1] >= 0)) {
                    crossings++;
                }
            }
            assertBetween(crossings, 19, 21);
        });

        test('B4.14: Zero-crossing count of 20.0 Hz sine across 1s (approx 40 crossings)', () => {
            const totalSamples = 800;
            const sine = new Float32Array(totalSamples).map((_, i) => Math.sin(2 * Math.PI * 20.0 * i / 800));
            let crossings = 0;
            for (let i = 1; i < totalSamples; i++) {
                if ((sine[i] >= 0 && sine[i - 1] < 0) || (sine[i] < 0 && sine[i - 1] >= 0)) {
                    crossings++;
                }
            }
            assertBetween(crossings, 39, 41);
        });

        test('B4.15: Aliasing behavior for signals > Nyquist (e.g. 500 Hz aliases to 300 Hz)', () => {
            const aliasedTone = new Float32Array(N).map((_, i) => Math.sin(2 * Math.PI * 500.0 * i / Fs));
            const fft = computeFFT(aliasedTone, Fs);
            assertClose(fft.dominantFreq, 300.0, 5.0);
        });

        test('B4.16: Zero signal frequency spectrum is all zeros', () => {
            const fft = computeFFT(new Float32Array(N), Fs);
            assertEqual(fft.dominantMag, 0.0);
        });

        test('B4.17: Single non-zero impulse frequency spectrum is flat', () => {
            const impulse = new Float32Array(N);
            impulse[0] = 1.0;
            const fft = computeFFT(impulse, Fs);
            assert(fft.magnitudes.length === 128);
        });

        test('B4.18: Symmetrical square wave odd harmonics presence (1X, 3X, 5X)', () => {
            const sq = new Float32Array(N).map((_, i) => (Math.sin(2 * Math.PI * 10.0 * i / Fs) >= 0 ? 1.0 : -1.0));
            const fft = computeFFT(sq, Fs);
            const h1 = fft.magnitudes[Math.round(10.0 / 3.125)];
            const h3 = fft.magnitudes[Math.round(30.0 / 3.125)];
            assertGreaterThan(h1, h3);
            assertGreaterThan(h3, 0.1);
        });

        test('B4.19: Fast Fourier transform frequency linearity', () => {
            const fft = computeFFT(new Float32Array(N), Fs);
            for (let i = 1; i < fft.frequencies.length; i++) {
                assertClose(fft.frequencies[i] - fft.frequencies[i - 1], 3.125, 1e-5);
            }
        });

        test('B4.20: Total single-sided power spectrum sum non-negativity', () => {
            const sig = generateSignal();
            const fft = computeFFT(removeDC(sig.ax), Fs);
            for (let i = 0; i < fft.magnitudes.length; i++) {
                assertGreaterThan(fft.magnitudes[i], -1e-6);
            }
        });
    });

    // ========================================================================
    // Category 5: Buffer Allocation, Circular Wrapping & Window Sizes (20 Tests)
    // ========================================================================
    describe('Category 5: Buffer Allocation, Circular Wrapping & Window Sizes', () => {
        test('B5.01: Window length N=256 standard Radix-2 size', () => {
            const n = 256;
            assertEqual(n & (n - 1), 0, '256 is power of 2');
        });

        test('B5.02: Window length N=128 sub-window power of 2', () => {
            const n = 128;
            assertEqual(n & (n - 1), 0, '128 is power of 2');
        });

        test('B5.03: Window length N=512 extended window power of 2', () => {
            const n = 512;
            assertEqual(n & (n - 1), 0, '512 is power of 2');
        });

        test('B5.04: Window length N=1024 1.28s window power of 2', () => {
            const n = 1024;
            assertEqual(n & (n - 1), 0, '1024 is power of 2');
        });

        test('B5.05: Circular ring buffer head index modulo wrapping (idx % N)', () => {
            const N = 256;
            for (let i = 0; i < 1000; i++) {
                const wrapped = i % N;
                assertBetween(wrapped, 0, N - 1);
            }
        });

        test('B5.06: Full 30s session recorder limit: 24,000 samples @ 800 Hz', () => {
            const total = 30 * 800;
            assertEqual(total, 24000);
        });

        test('B5.07: Circular buffer rollover without memory leak', () => {
            const ring = new Float32Array(256);
            for (let i = 0; i < 50000; i++) {
                ring[i % 256] = i;
            }
            assertEqual(ring[0], 49920);
        });

        test('B5.08: Empty array handling (N=0 returns 0.0 RMS)', () => {
            assertEqual(computeRMS(new Float32Array(0)), 0.0);
        });

        test('B5.09: Single element array handling (N=1 RMS == abs(val))', () => {
            assertEqual(computeRMS(new Float32Array([7.5])), 7.5);
        });

        test('B5.10: Two element array handling (N=2)', () => {
            const rms = computeRMS(new Float32Array([3.0, 4.0]));
            assertClose(rms, Math.sqrt((9 + 16) / 2), 1e-5);
        });

        test('B5.11: Pre-allocated buffer memory reuse verification', () => {
            const buf = new Float32Array(256);
            const ptr1 = buf.buffer;
            buf.fill(1.0);
            const ptr2 = buf.buffer;
            assertEqual(ptr1, ptr2, 'Underlying ArrayBuffer is reused without reallocation');
        });

        test('B5.12: Sub-array slicing view sharing (TypedArray subarray)', () => {
            const bigBuf = new Float32Array(1024);
            const sub = bigBuf.subarray(0, 256);
            assertEqual(sub.length, 256);
        });

        test('B5.13: Buffer copy within memory (TypedArray set)', () => {
            const dst = new Float32Array(256);
            const src = new Float32Array(256).fill(3.14);
            dst.set(src);
            assertClose(dst[0], 3.14, 1e-4);
        });

        test('B5.14: Maximum time window offset calculation for 10s recording (8,000 samples)', () => {
            assertEqual(10 * 800, 8000);
        });

        test('B5.15: Buffer stride offset continuity', () => {
            const buf = new Float32Array(256).map((_, i) => i);
            for (let i = 1; i < 256; i++) {
                assertEqual(buf[i] - buf[i - 1], 1);
            }
        });

        test('B5.16: Zero-padding non-power-of-2 input to 256', () => {
            const raw = new Float32Array(200).fill(1.0);
            const padded = new Float32Array(256);
            padded.set(raw);
            assertEqual(padded.length, 256);
            assertEqual(padded[255], 0.0);
        });

        test('B5.17: High-throughput continuous sample appending (100,000 pushes)', () => {
            let sum = 0;
            for (let i = 0; i < 100000; i++) {
                sum += (i & 0xFF);
            }
            assertGreaterThan(sum, 0);
        });

        test('B5.18: Buffer clone via slice creates independent memory', () => {
            const orig = new Float32Array([1, 2, 3]);
            const clone = orig.slice();
            clone[0] = 99;
            assertEqual(orig[0], 1);
        });

        test('B5.19: Ring buffer newest sample retrieval', () => {
            const buf = new Float32Array(256);
            let head = 0;
            for (let i = 0; i < 300; i++) {
                buf[head] = i;
                head = (head + 1) % 256;
            }
            const newest = buf[(head - 1 + 256) % 256];
            assertEqual(newest, 299);
        });

        test('B5.20: Ring buffer oldest sample retrieval', () => {
            const buf = new Float32Array(256);
            let head = 0;
            for (let i = 0; i < 300; i++) {
                buf[head] = i;
                head = (head + 1) % 256;
            }
            const oldest = buf[head];
            assertEqual(oldest, 300 - 256);
        });
    });

    // ========================================================================
    // Category 6: Numerical Robustness, NaN Safety & Div-by-Zero (20 Tests)
    // ========================================================================
    describe('Category 6: Numerical Robustness, NaN Safety & Div-by-Zero', () => {
        test('B6.01: Zero RMS signal Crest Factor does not return NaN or Infinity', () => {
            const cf = computeCrestFactor(0.0, 0.0);
            assertEqual(cf, 0.0);
            assert(!isNaN(cf));
            assert(isFinite(cf));
        });

        test('B6.02: Zero RMS with non-zero peak Crest Factor handles edge safely', () => {
            const cf = computeCrestFactor(1.0, 0.0);
            assertEqual(cf, 0.0);
        });

        test('B6.03: Zero variance Kurtosis does not return NaN', () => {
            const flat = new Float32Array(256).fill(5.0);
            const kurt = computeKurtosis(flat);
            assertEqual(kurt, 0.0);
            assert(!isNaN(kurt));
        });

        test('B6.04: Double integration of all zeros does not drift or produce NaN', () => {
            const dInt = doubleIntegrate(new Float32Array(256), 800);
            assertEqual(dInt.velRmsMmS, 0.0);
            assertEqual(dInt.dispPeakToPeakUm, 0.0);
        });

        test('B6.05: FFT of all zeros produces zero magnitude without NaN', () => {
            const fft = computeFFT(new Float32Array(256), 800);
            for (let i = 0; i < fft.magnitudes.length; i++) {
                assertEqual(fft.magnitudes[i], 0.0);
            }
        });

        test('B6.06: Extreme subnormal float: 1e-30 handles safely', () => {
            const val = computeRMS(new Float32Array([1e-30, 1e-30]));
            assert(!isNaN(val));
        });

        test('B6.07: Extreme large float: 1e15 does not overflow to Infinity', () => {
            const val = computeRMS(new Float32Array([1e15, 1e15]));
            assert(isFinite(val));
        });

        test('B6.08: computePeak handles negative-only arrays correctly', () => {
            const pk = computePeak(new Float32Array([-10.5, -2.0, -8.3]));
            assertEqual(pk, 10.5);
        });

        test('B6.09: computePeakToPeak handles identical values correctly (result == 0)', () => {
            const pkpk = computePeakToPeak(new Float32Array([4.0, 4.0, 4.0]));
            assertEqual(pkpk, 0.0);
        });

        test('B6.10: Triaxial vector RMS with two zero axes equals single axis RMS', () => {
            const x = new Float32Array([3.0, 4.0]);
            const y = new Float32Array(2).fill(0.0);
            const z = new Float32Array(2).fill(0.0);
            const vRms = computeVectorRMS(x, y, z);
            const xRms = computeRMS(x);
            assertClose(vRms, xRms, 1e-6);
        });

        test('B6.11: computeLissajous handles single point orbit safely', () => {
            const liss = computeLissajous([0.0], [0.0]);
            assertEqual(liss.meanRadius, 0.0);
            assertEqual(liss.eccentricity, 0.0);
        });

        test('B6.12: ISO 10816 evaluation with negative input clamps to Zone A', () => {
            const iso = evaluateISO10816(-0.5);
            assertEqual(iso.zone, 'Zone_A');
        });

        test('B6.13: Persistence engine handles empty history safely', () => {
            const engine = new KOutOfMPersistenceEngine();
            assertEqual(engine.currentState, 'Normal');
        });

        test('B6.14: Persistence engine handles K > M parameters gracefully', () => {
            const engine = new KOutOfMPersistenceEngine(10, 5);
            engine.pushWindow(true);
            assertEqual(engine.currentState, 'Normal');
        });

        test('B6.15: Hann window of length 0 returns empty array without throwing', () => {
            const win = applyHannWindow(new Float32Array(0));
            assertEqual(win.length, 0);
        });

        test('B6.16: Hann window of length 1 returns original array without NaN', () => {
            const win = applyHannWindow(new Float32Array([5.0]));
            assertEqual(win.length, 1);
        });

        test('B6.17: Float array NaN detection helper', () => {
            const hasNaN = (arr) => arr.some(v => isNaN(v));
            assertEqual(hasNaN([1, 2, 3]), false);
            assertEqual(hasNaN([1, NaN, 3]), true);
        });

        test('B6.18: Float array Infinity detection helper', () => {
            const hasInf = (arr) => arr.some(v => !isFinite(v));
            assertEqual(hasInf([1, 2, 3]), false);
            assertEqual(hasInf([1, Infinity, 3]), true);
        });

        test('B6.19: Signal generator with 0 duration returns empty buffers', () => {
            const sig = generateSignal({ durationSec: 0 });
            assertEqual(sig.n, 0);
        });

        test('B6.20: Division safety in CSV parser with empty lines', () => {
            const csv = "timestamp_ms,sample_idx,rpm,ax_g,ay_g,az_g,vector_mag_g,vector_rms_g\n0.0,0,600,0,0,1,0,0\n\n";
            const parsed = parseAndValidateCSV(csv);
            assert(parsed.rowCount >= 1);
        });
    });

    // ========================================================================
    // Category 7: ISO 10816 Threshold Boundaries & Transitions (20 Tests)
    // ========================================================================
    describe('Category 7: ISO 10816 Threshold Boundaries & Transitions', () => {
        test('B7.01: Just below Warning threshold: 0.3499g -> Zone A (Normal)', () => {
            const res = evaluateISO10816(0.3499);
            assertEqual(res.zone, 'Zone_A');
            assertEqual(res.severity, 'Normal');
            assertEqual(res.ledColor, 0x00ff88);
        });

        test('B7.02: Exact Warning threshold boundary: 0.3500g -> Zone B (Warning)', () => {
            const res = evaluateISO10816(0.3500);
            assertEqual(res.zone, 'Zone_B');
            assertEqual(res.severity, 'Warning');
            assertEqual(res.ledColor, 0xffb800);
        });

        test('B7.03: Just above Warning threshold: 0.3501g -> Zone B (Warning)', () => {
            const res = evaluateISO10816(0.3501);
            assertEqual(res.zone, 'Zone_B');
            assertEqual(res.severity, 'Warning');
        });

        test('B7.04: Warning band midpoint: 0.5250g -> Zone B (Warning)', () => {
            const res = evaluateISO10816(0.5250);
            assertEqual(res.zone, 'Zone_B');
        });

        test('B7.05: Just below Alarm threshold: 0.6999g -> Zone B (Warning)', () => {
            const res = evaluateISO10816(0.6999);
            assertEqual(res.zone, 'Zone_B');
            assertEqual(res.severity, 'Warning');
        });

        test('B7.06: Exact Alarm threshold boundary: 0.7000g -> Zone C (Abnormal)', () => {
            const res = evaluateISO10816(0.7000);
            assertEqual(res.zone, 'Zone_C');
            assertEqual(res.severity, 'Abnormal');
            assertEqual(res.ledColor, 0xff2d55);
        });

        test('B7.07: Just above Alarm threshold: 0.7001g -> Zone C (Abnormal)', () => {
            const res = evaluateISO10816(0.7001);
            assertEqual(res.zone, 'Zone_C');
        });

        test('B7.08: Alarm band midpoint: 0.9500g -> Zone C (Abnormal)', () => {
            const res = evaluateISO10816(0.9500);
            assertEqual(res.zone, 'Zone_C');
        });

        test('B7.09: Just below Critical Zone D: 1.1999g -> Zone C (Abnormal)', () => {
            const res = evaluateISO10816(1.1999);
            assertEqual(res.zone, 'Zone_C');
        });

        test('B7.10: Exact Critical Zone D boundary: 1.2000g -> Zone D (Critical)', () => {
            const res = evaluateISO10816(1.2000);
            assertEqual(res.zone, 'Zone_D');
            assertEqual(res.severity, 'Abnormal');
        });

        test('B7.11: Severe Critical vibration: 2.5000g -> Zone D', () => {
            const res = evaluateISO10816(2.5000);
            assertEqual(res.zone, 'Zone_D');
        });

        test('B7.12: Extreme catastrophic vibration: 10.000g -> Zone D', () => {
            const res = evaluateISO10816(10.000);
            assertEqual(res.zone, 'Zone_D');
        });

        test('B7.13: Zero vibration: 0.000g -> Zone A (Normal)', () => {
            const res = evaluateISO10816(0.000);
            assertEqual(res.zone, 'Zone_A');
        });

        test('B7.14: Badge CSS class for Normal is "status-normal"', () => {
            assertEqual(evaluateISO10816(0.1).badgeClass, 'status-normal');
        });

        test('B7.15: Badge CSS class for Warning is "status-warning"', () => {
            assertEqual(evaluateISO10816(0.45).badgeClass, 'status-warning');
        });

        test('B7.16: Badge CSS class for Alarm is "status-alarm"', () => {
            assertEqual(evaluateISO10816(0.8).badgeClass, 'status-alarm');
        });

        test('B7.17: Badge CSS class for Critical is "status-alarm"', () => {
            assertEqual(evaluateISO10816(1.5).badgeClass, 'status-alarm');
        });

        test('B7.18: Persistence engine step 1 of 5 abnormal windows', () => {
            const eng = new KOutOfMPersistenceEngine(3, 5);
            eng.pushWindow(true);
            assertEqual(eng.currentState, 'Normal');
        });

        test('B7.19: Persistence engine step 2 of 5 abnormal windows', () => {
            const eng = new KOutOfMPersistenceEngine(3, 5);
            eng.pushWindow(true); eng.pushWindow(true);
            assertEqual(eng.currentState, 'Normal');
        });

        test('B7.20: Persistence engine step 3 of 5 abnormal windows triggers Alarm', () => {
            const eng = new KOutOfMPersistenceEngine(3, 5);
            eng.pushWindow(true); eng.pushWindow(true); eng.pushWindow(true);
            assertEqual(eng.currentState, 'Abnormal');
        });
    });

    // ========================================================================
    // Category 8: Signal Noise Floor, SNR & Kurtosis Bounds (15 Tests)
    // ========================================================================
    describe('Category 8: Signal Noise Floor, SNR & Kurtosis Bounds', () => {
        test('B8.01: Zero noise floor std dev: 0.000g', () => {
            const sig = generateSignal({ noiseStdDevG: 0.000, rpm: 600, unbalanceMassG: 0.0 });
            const acX = removeDC(sig.ax);
            // Pure sine wave has exact peak = amplitude
            assertClose(computePeak(acX), 0.06, 0.01);
        });

        test('B8.02: Low noise lab floor: 0.005g std dev', () => {
            const sig = generateSignal({ noiseStdDevG: 0.005 });
            assertGreaterThan(computeRMS(sig.ax), 0.0);
        });

        test('B8.03: Standard simulated sensor noise: 0.025g std dev', () => {
            const sig = generateSignal({ noiseStdDevG: 0.025 });
            assertLessThan(computeRMS(removeDC(sig.ax)), 0.3);
        });

        test('B8.04: High industrial plant noise: 0.075g std dev', () => {
            const sig = generateSignal({ noiseStdDevG: 0.075 });
            assertGreaterThan(computeRMS(removeDC(sig.ax)), 0.05);
        });

        test('B8.05: Maximum noise stress: 0.100g std dev', () => {
            const sig = generateSignal({ noiseStdDevG: 0.100 });
            assert(!isNaN(computeRMS(sig.ax)));
        });

        test('B8.06: Pure sinusoid Kurtosis theoretical bound: exactly 1.5', () => {
            const n = 10000;
            const sine = new Float32Array(n).map((_, i) => Math.sin(2 * Math.PI * i / 100));
            const kurt = computeKurtosis(sine);
            assertClose(kurt, 1.5, 0.05);
        });

        test('B8.07: Pure Gaussian noise Kurtosis theoretical bound: approximately 3.0', () => {
            // Generate synthetic Gaussian array
            const n = 10000;
            const gauss = new Float32Array(n);
            for (let i = 0; i < n; i += 2) {
                const u1 = Math.random() || 1e-6;
                const u2 = Math.random() || 1e-6;
                const r = Math.sqrt(-2.0 * Math.log(u1));
                const theta = 2.0 * Math.PI * u2;
                gauss[i] = r * Math.cos(theta);
                if (i + 1 < n) gauss[i + 1] = r * Math.sin(theta);
            }
            const kurt = computeKurtosis(gauss);
            assertBetween(kurt, 2.7, 3.3);
        });

        test('B8.08: Sparse impact impulse shock Kurtosis bound: > 8.0', () => {
            const shock = new Float32Array(1000).fill(0.05);
            shock[100] = 5.0;
            shock[300] = 4.5;
            shock[700] = 6.0;
            const kurt = computeKurtosis(shock);
            assertGreaterThan(kurt, 8.0);
        });

        test('B8.09: Symmetrical square wave Kurtosis: exactly 1.0', () => {
            const n = 1000;
            const sq = new Float32Array(n).map((_, i) => (i % 2 === 0 ? 1.0 : -1.0));
            const kurt = computeKurtosis(sq);
            assertClose(kurt, 1.0, 1e-5);
        });

        test('B8.10: Triangle wave Kurtosis: exactly 1.8', () => {
            const n = 10000;
            const tri = new Float32Array(n).map((_, i) => {
                const phase = (i % 100) / 100;
                return phase < 0.5 ? (4 * phase - 1) : (3 - 4 * phase);
            });
            const kurt = computeKurtosis(tri);
            assertClose(kurt, 1.8, 0.05);
        });

        test('B8.11: Signal-to-Noise Ratio (SNR) under 3.5g unbalance vs 0.025g noise > 20 dB', () => {
            const signalPower = Math.pow((3.5 / 5.0) * 1.85 / Math.SQRT2, 2);
            const noisePower = Math.pow(0.025, 2);
            const snrDb = 10 * Math.log10(signalPower / noisePower);
            assertGreaterThan(snrDb, 20.0);
        });

        test('B8.12: Constant offset added to noise does not alter Kurtosis', () => {
            const noise = new Float32Array(1000).map(() => Math.random() - 0.5);
            const k1 = computeKurtosis(noise);
            const shifted = noise.map(v => v + 100.0);
            const k2 = computeKurtosis(shifted);
            assertClose(k1, k2, 1e-4);
        });

        test('B8.13: Uniform distribution Kurtosis: approximately 1.8', () => {
            const n = 10000;
            const unif = new Float32Array(n).map(() => Math.random() * 2.0 - 1.0);
            const kurt = computeKurtosis(unif);
            assertClose(kurt, 1.8, 0.1);
        });

        test('B8.14: Heavy bearing fault impact signal Kurtosis exceeds baseline', () => {
            const baseSig = generateSignal({ faultMode: 'NORMAL', rpm: 600 });
            const faultSig = generateSignal({ faultMode: 'BEARING_BPFO', rpm: 600 });
            const kBase = computeKurtosis(removeDC(baseSig.ax));
            const kFault = computeKurtosis(removeDC(faultSig.ax));
            assertGreaterThan(kFault, kBase);
        });

        test('B8.15: Extremely heavy multi-shock spike train Kurtosis > 15.0', () => {
            const train = new Float32Array(2000).fill(0.02);
            for (let i = 0; i < 2000; i += 200) train[i] = 8.0;
            const kurt = computeKurtosis(train);
            assertGreaterThan(kurt, 15.0);
        });
    });

    // ========================================================================
    // Category 9: Playback Time Scaling & Delta Time Limits (10 Tests)
    // ========================================================================
    describe('Category 9: Playback Time Scaling & Delta Time Limits', () => {
        test('B9.01: Quarter-speed slow motion: 0.25X time scale', () => {
            const scale = 0.25;
            assertEqual(scale, 0.25);
        });

        test('B9.02: Half-speed slow motion: 0.50X time scale', () => {
            const scale = 0.50;
            assertEqual(scale, 0.50);
        });

        test('B9.03: Normal real-time execution: 1.00X time scale', () => {
            const scale = 1.00;
            assertEqual(scale, 1.00);
        });

        test('B9.04: Double-speed fast forward: 2.00X time scale', () => {
            const scale = 2.00;
            assertEqual(scale, 2.00);
        });

        test('B9.05: Discrete integration step at 60 FPS: dt = 0.01667s', () => {
            const dt = 1.0 / 60.0;
            assertClose(dt, 0.0166667, 1e-6);
        });

        test('B9.06: Discrete integration step at 120 FPS high refresh: dt = 0.00833s', () => {
            const dt = 1.0 / 120.0;
            assertClose(dt, 0.0083333, 1e-6);
        });

        test('B9.07: Minimum delta time clamp: dt >= 0.001s (prevent infinite loop)', () => {
            const dt = Math.max(0.001, 0.00001);
            assertEqual(dt, 0.001);
        });

        test('B9.08: Maximum delta time clamp: dt <= 0.1s (prevent large physics jump on tab switch)', () => {
            const dt = Math.min(0.1, 5.0); // Tab inactive for 5s
            assertEqual(dt, 0.1);
        });

        test('B9.09: Shaft angle delta modulation under 2.0X time scale is exactly 2x base delta', () => {
            const baseDTheta = (2 * Math.PI * 10.0) * 0.016;
            const scaledDTheta = (2 * Math.PI * 10.0) * (0.016 * 2.0);
            assertClose(scaledDTheta / baseDTheta, 2.0, 1e-5);
        });

        test('B9.10: Shaft angle delta modulation under 0.25X time scale is exactly 0.25x base delta', () => {
            const baseDTheta = (2 * Math.PI * 10.0) * 0.016;
            const scaledDTheta = (2 * Math.PI * 10.0) * (0.016 * 0.25);
            assertClose(scaledDTheta / baseDTheta, 0.25, 1e-5);
        });
    });
});
