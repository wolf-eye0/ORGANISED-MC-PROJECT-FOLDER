/**
 * VibeGuard 3D WebGL Digital Twin - E2E Test Suite Helpers & Authoritative Oracles
 * 
 * Provides:
 * 1. Self-contained testing harness (describe, test, assertions, runner).
 * 2. Authoritative DSP mathematical oracles (matching C++ firmware & ISO 10816).
 * 3. Synthetic signal generation engine for physics-based fault simulations.
 * 4. HTML/DOM static & structure inspection utilities.
 * 5. RFC 4180 CSV and JSON diagnostic schema validators.
 */

const fs = require('fs');
const path = require('path');

// ============================================================================
// 1. Lightweight Test Framework Primitives
// ============================================================================

class TestContext {
    constructor() {
        this.currentSuite = '';
        this.results = {
            total: 0,
            passed: 0,
            failed: 0,
            skipped: 0,
            suites: []
        };
        this.currentSuiteObj = null;
    }

    startSuite(name) {
        this.currentSuite = name;
        this.currentSuiteObj = {
            name,
            tests: [],
            passed: 0,
            failed: 0
        };
        this.results.suites.push(this.currentSuiteObj);
    }

    recordPass(testName, durationMs = 0) {
        this.results.total++;
        this.results.passed++;
        this.currentSuiteObj.passed++;
        this.currentSuiteObj.tests.push({
            name: testName,
            status: 'PASS',
            durationMs
        });
    }

    recordFail(testName, error, durationMs = 0) {
        this.results.total++;
        this.results.failed++;
        this.currentSuiteObj.failed++;
        this.currentSuiteObj.tests.push({
            name: testName,
            status: 'FAIL',
            error: error.message || String(error),
            stack: error.stack,
            durationMs
        });
    }
}

const testCtx = new TestContext();

function describe(suiteName, suiteFn) {
    testCtx.startSuite(suiteName);
    try {
        suiteFn();
    } catch (err) {
        testCtx.recordFail(`[Suite Setup Failure] ${suiteName}`, err);
    }
}

function test(testName, testFn) {
    const t0 = performance.now();
    try {
        testFn();
        const dur = performance.now() - t0;
        testCtx.recordPass(testName, dur);
    } catch (err) {
        const dur = performance.now() - t0;
        testCtx.recordFail(testName, err, dur);
    }
}

async function testAsync(testName, asyncTestFn) {
    const t0 = performance.now();
    try {
        await asyncTestFn();
        const dur = performance.now() - t0;
        testCtx.recordPass(testName, dur);
    } catch (err) {
        const dur = performance.now() - t0;
        testCtx.recordFail(testName, err, dur);
    }
}

// Assertions
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || 'Assertion failed: condition is falsy');
    }
}

function assertEqual(actual, expected, message) {
    if (actual !== expected) {
        throw new Error(`${message || 'assertEqual failed'}: Expected ${JSON.stringify(expected)}, got ${JSON.stringify(actual)}`);
    }
}

function assertClose(actual, expected, tolerance = 1e-4, message) {
    const diff = Math.abs(actual - expected);
    if (diff > tolerance) {
        throw new Error(`${message || 'assertClose failed'}: Expected ${expected} +/- ${tolerance}, got ${actual} (diff: ${diff.toExponential(4)})`);
    }
}

function assertArrayClose(actualArr, expectedArr, tolerance = 1e-4, message) {
    if (!actualArr || !expectedArr || actualArr.length !== expectedArr.length) {
        throw new Error(`${message || 'assertArrayClose failed'}: Array lengths differ (${actualArr?.length} vs ${expectedArr?.length})`);
    }
    for (let i = 0; i < actualArr.length; i++) {
        const diff = Math.abs(actualArr[i] - expectedArr[i]);
        if (diff > tolerance) {
            throw new Error(`${message || 'assertArrayClose failed'} at index ${i}: Expected ${expectedArr[i]} +/- ${tolerance}, got ${actualArr[i]} (diff: ${diff})`);
        }
    }
}

function assertThrows(fn, message) {
    let threw = false;
    try {
        fn();
    } catch (err) {
        threw = true;
    }
    if (!threw) {
        throw new Error(message || 'Expected function to throw, but it succeeded');
    }
}

function assertRegex(text, regex, message) {
    if (!regex.test(text)) {
        throw new Error(`${message || 'assertRegex failed'}: String "${text.slice(0, 80)}..." does not match regex ${regex}`);
    }
}

function assertGreaterThan(actual, min, message) {
    if (!(actual > min)) {
        throw new Error(`${message || 'assertGreaterThan failed'}: Expected ${actual} > ${min}`);
    }
}

function assertLessThan(actual, max, message) {
    if (!(actual < max)) {
        throw new Error(`${message || 'assertLessThan failed'}: Expected ${actual} < ${max}`);
    }
}

function assertBetween(actual, min, max, message) {
    if (actual < min || actual > max) {
        throw new Error(`${message || 'assertBetween failed'}: Expected ${actual} between [${min}, ${max}]`);
    }
}

// ============================================================================
// 2. Authoritative DSP Mathematical Oracles (Exact C++ & ISO 10816 Spec)
// ============================================================================

/**
 * In-place or new array DC offset removal.
 * Subtracts the arithmetic mean from all elements.
 */
function removeDC(data) {
    const n = data.length;
    if (n === 0) return new Float32Array(0);
    let sum = 0.0;
    for (let i = 0; i < n; i++) sum += data[i];
    const mean = sum / n;
    const out = new Float32Array(n);
    for (let i = 0; i < n; i++) out[i] = data[i] - mean;
    return out;
}

/**
 * 1D Root Mean Square.
 */
function computeRMS(data) {
    const n = data.length;
    if (n === 0) return 0.0;
    let sumSq = 0.0;
    for (let i = 0; i < n; i++) {
        sumSq += data[i] * data[i];
    }
    return Math.sqrt(sumSq / n);
}

/**
 * 3-Axis Euclidean Vector RMS: RMS(sqrt(x^2 + y^2 + z^2))
 */
function computeVectorRMS(x, y, z) {
    const n = x.length;
    if (n === 0 || y.length !== n || z.length !== n) return 0.0;
    let sumSq = 0.0;
    for (let i = 0; i < n; i++) {
        const dx = x[i];
        const dy = y[i];
        const dz = z[i];
        sumSq += (dx * dx + dy * dy + dz * dz);
    }
    return Math.sqrt(sumSq / n);
}

/**
 * Peak dynamic acceleration magnitude: max(|x_i|).
 */
function computePeak(data) {
    let max = 0.0;
    for (let i = 0; i < data.length; i++) {
        const abs = Math.abs(data[i]);
        if (abs > max) max = abs;
    }
    return max;
}

/**
 * Peak-to-peak amplitude: max(x_i) - min(x_i).
 */
function computePeakToPeak(data) {
    if (data.length === 0) return 0.0;
    let min = data[0];
    let max = data[0];
    for (let i = 1; i < data.length; i++) {
        if (data[i] < min) min = data[i];
        if (data[i] > max) max = data[i];
    }
    return max - min;
}

/**
 * Crest Factor: Peak / RMS.
 */
function computeCrestFactor(peak, rms) {
    if (rms <= 1e-9) return 0.0;
    return peak / rms;
}

/**
 * 4th-Order Kurtosis Shock Index.
 * Kurtosis = E[(X - mu)^4] / (E[(X - mu)^2])^2
 */
function computeKurtosis(data) {
    const n = data.length;
    if (n < 4) return 0.0;
    let sum = 0.0;
    for (let i = 0; i < n; i++) sum += data[i];
    const mean = sum / n;

    let m2 = 0.0;
    let m4 = 0.0;
    for (let i = 0; i < n; i++) {
        const diff = data[i] - mean;
        const diff2 = diff * diff;
        m2 += diff2;
        m4 += diff2 * diff2;
    }
    m2 /= n;
    m4 /= n;
    if (m2 <= 1e-12) return 0.0;
    return m4 / (m2 * m2);
}

/**
 * Hann Window: w(i) = 0.5 * (1 - cos(2*pi*i / (N - 1)))
 */
function applyHannWindow(data) {
    const n = data.length;
    const out = new Float32Array(n);
    if (n <= 1) return out;
    const twoPi = 2.0 * Math.PI;
    const denom = n - 1;
    for (let i = 0; i < n; i++) {
        const factor = 0.5 * (1.0 - Math.cos(twoPi * i / denom));
        out[i] = data[i] * factor;
    }
    return out;
}

/**
 * In-place Cooley-Tukey Radix-2 Real/Imaginary FFT.
 */
function fftRadix2(real, imag) {
    const n = real.length;
    // Bit-reversal permutation
    let j = 0;
    for (let i = 0; i < n - 1; i++) {
        if (i < j) {
            const tr = real[i]; real[i] = real[j]; real[j] = tr;
            const ti = imag[i]; imag[i] = imag[j]; imag[j] = ti;
        }
        let k = n >> 1;
        while (k > 0 && k <= j) {
            j -= k;
            k >>= 1;
        }
        j += k;
    }

    // Cooley-Tukey computation
    for (let len = 2; len <= n; len <<= 1) {
        const angle = -2.0 * Math.PI / len;
        const wlenR = Math.cos(angle);
        const wlenI = Math.sin(angle);
        for (let i = 0; i < n; i += len) {
            let wR = 1.0;
            let wI = 0.0;
            const halfLen = len >> 1;
            for (let k = 0; k < halfLen; k++) {
                const uR = real[i + k];
                const uI = imag[i + k];
                const vR = real[i + k + halfLen] * wR - imag[i + k + halfLen] * wI;
                const vI = real[i + k + halfLen] * wI + imag[i + k + halfLen] * wR;
                real[i + k] = uR + vR;
                imag[i + k] = uI + vI;
                real[i + k + halfLen] = uR - vR;
                imag[i + k + halfLen] = uI - vI;
                const nextWR = wR * wlenR - wI * wlenI;
                const nextWI = wR * wlenI + wI * wlenR;
                wR = nextWR;
                wI = nextWI;
            }
        }
    }
}

/**
 * Complete Real FFT processing pipeline matching C++ features.cpp.
 * Computes frequency bins, single-sided magnitude spectrum (normalized by N/2),
 * dominant peak frequency, dominant peak magnitude, and harmonic markers (1X, 2X, 3X).
 */
function computeFFT(timeData, samplingRate = 800) {
    const n = timeData.length;
    const numBins = n / 2;
    const real = new Float32Array(n);
    const imag = new Float32Array(n);

    // Apply Hann window
    const windowed = applyHannWindow(timeData);
    for (let i = 0; i < n; i++) real[i] = windowed[i];

    fftRadix2(real, imag);

    const magnitudes = new Float32Array(numBins);
    const frequencies = new Float32Array(numBins);
    const deltaF = samplingRate / n;

    let maxMag = 0.0;
    let maxBin = 1;

    for (let i = 0; i < numBins; i++) {
        frequencies[i] = i * deltaF;
        // Single-sided amplitude normalization (2 / N)
        const mag = Math.sqrt(real[i] * real[i] + imag[i] * imag[i]) * (2.0 / n);
        magnitudes[i] = mag;

        // Skip DC (bin 0) for dominant peak selection
        if (i >= 1 && mag > maxMag) {
            maxMag = mag;
            maxBin = i;
        }
    }

    const dominantFreq = maxBin * deltaF;
    const dominantMag = maxMag;

    // Harmonic extraction
    function getPeakNear(targetFreq, windowBins = 2) {
        const centerBin = Math.round(targetFreq / deltaF);
        let localMax = 0.0;
        for (let b = Math.max(1, centerBin - windowBins); b <= Math.min(numBins - 1, centerBin + windowBins); b++) {
            if (magnitudes[b] > localMax) localMax = magnitudes[b];
        }
        return localMax;
    }

    return {
        frequencies,
        magnitudes,
        dominantFreq,
        dominantMag,
        deltaF,
        harmonicPeaks: {
            h1: getPeakNear(dominantFreq),
            h2: getPeakNear(2.0 * dominantFreq),
            h3: getPeakNear(3.0 * dominantFreq)
        }
    };
}

/**
 * Drift-Free Double Numerical Integration (accel g -> velocity mm/s -> displacement µm).
 * Utilizes trapezoidal integration with high-pass IIR filtering to prevent low-frequency drift.
 */
function doubleIntegrate(accelG, samplingRate = 800, cutoffHz = 3.0) {
    const n = accelG.length;
    const dt = 1.0 / samplingRate;
    const gToMmS2 = 9806.65; // 1g = 9806.65 mm/s^2

    // 1. Convert to mm/s^2 and remove DC
    const aAc = removeDC(accelG);
    const aMms2 = new Float32Array(n);
    for (let i = 0; i < n; i++) aMms2[i] = aAc[i] * gToMmS2;

    // 2. High-pass filter coefficient for integrator
    const rc = 1.0 / (2.0 * Math.PI * cutoffHz);
    const alpha = rc / (rc + dt);

    // 3. First Integration: Velocity (mm/s)
    const vel = new Float32Array(n);
    let vRunning = 0.0, vPrevRunning = 0.0, vFilt = 0.0;
    for (let i = 1; i < n; i++) {
        vRunning += 0.5 * (aMms2[i] + aMms2[i - 1]) * dt;
        vFilt = alpha * (vFilt + vRunning - vPrevRunning);
        vPrevRunning = vRunning;
        vel[i] = vFilt;
    }

    // 4. Second Integration: Displacement (µm)
    const disp = new Float32Array(n);
    let dRunning = 0.0, dPrevRunning = 0.0, dFilt = 0.0;
    for (let i = 1; i < n; i++) {
        dRunning += 0.5 * (vel[i] + vel[i - 1]) * dt * 1000.0; // mm to µm
        dFilt = alpha * (dFilt + dRunning - dPrevRunning);
        dPrevRunning = dRunning;
        disp[i] = dFilt;
    }

    const velRms = computeRMS(vel);
    const dispPkPk = computePeakToPeak(disp);

    return {
        velocity: vel,
        displacement: disp,
        velRmsMmS: velRms,
        dispPeakToPeakUm: dispPkPk
    };
}

/**
 * ISO 10816-3 Machinery Severity Zone Classifier.
 * Class I/II Industrial Machines:
 * - Zone A (Good): < 0.71 mm/s RMS (or < 0.35 g RMS dynamic)
 * - Zone B (Acceptable): 0.71 - 1.80 mm/s RMS (or 0.35 - 0.70 g RMS)
 * - Zone C (Unsatisfactory / Warning): 1.80 - 4.50 mm/s RMS (or > 0.70 g RMS)
 * - Zone D (Unacceptable / Critical Alarm): > 4.50 mm/s RMS
 */
function evaluateISO10816(vectorRmsG, velRmsMmS = 0) {
    if (vectorRmsG < 0.35) {
        return {
            zone: 'Zone_A',
            severity: 'Normal',
            badgeClass: 'status-normal',
            badgeText: 'STATE: NORMAL (HEALTHY)',
            ledColor: 0x00ff88 // Green
        };
    } else if (vectorRmsG < 0.70) {
        return {
            zone: 'Zone_B',
            severity: 'Warning',
            badgeClass: 'status-warning',
            badgeText: 'STATE: WARNING PRE-ALARM (>0.35g)',
            ledColor: 0xffb800 // Amber
        };
    } else if (vectorRmsG < 1.20) {
        return {
            zone: 'Zone_C',
            severity: 'Abnormal',
            badgeClass: 'status-alarm',
            badgeText: 'STATE: ABNORMAL ALARM (>0.70g)',
            ledColor: 0xff2d55 // Red
        };
    } else {
        return {
            zone: 'Zone_D',
            severity: 'Abnormal',
            badgeClass: 'status-alarm',
            badgeText: 'STATE: CRITICAL ALARM (>1.20g)',
            ledColor: 0xff2d55 // Pulsing Red
        };
    }
}

/**
 * K-out-of-M Persistence State Machine Engine.
 * Matches C++ state.cpp.
 */
class KOutOfMPersistenceEngine {
    constructor(k = 3, m = 5, kClear = 3) {
        this.k = k;
        this.m = m;
        this.kClear = kClear;
        this.history = [];
        this.currentState = 'Normal'; // 'Normal' | 'Abnormal' | 'FaultInvalid'
    }

    reset() {
        this.history = [];
        this.currentState = 'Normal';
    }

    pushWindow(isAbnormal, isFault = false) {
        if (isFault) {
            this.currentState = 'FaultInvalid';
            return this.currentState;
        }

        this.history.push(Boolean(isAbnormal));
        if (this.history.length > 50) this.history.shift(); // Keep rolling bounded

        const n = this.history.length;
        const windowSize = Math.min(this.m, n);

        if (this.currentState === 'Normal') {
            // Check if at least K of the last M windows were abnormal
            let count = 0;
            for (let i = n - windowSize; i < n; i++) {
                if (this.history[i]) count++;
            }
            if (count >= this.k) {
                this.currentState = 'Abnormal';
            }
        } else if (this.currentState === 'Abnormal') {
            // Check if last K_clear windows were strictly normal
            if (n >= this.kClear) {
                let allClean = true;
                for (let i = n - this.kClear; i < n; i++) {
                    if (this.history[i]) {
                        allClean = false;
                        break;
                    }
                }
                if (allClean) {
                    this.currentState = 'Normal';
                }
            }
        }

        return this.currentState;
    }
}

/**
 * 2D/3D Lissajous Shaft Orbit Metrics.
 */
function computeLissajous(x, y) {
    const n = Math.min(x.length, y.length);
    let minX = Infinity, maxX = -Infinity;
    let minY = Infinity, maxY = -Infinity;
    let sumR = 0.0;

    for (let i = 0; i < n; i++) {
        if (x[i] < minX) minX = x[i];
        if (x[i] > maxX) maxX = x[i];
        if (y[i] < minY) minY = y[i];
        if (y[i] > maxY) maxY = y[i];
        sumR += Math.sqrt(x[i] * x[i] + y[i] * y[i]);
    }

    const spanX = maxX - minX;
    const spanY = maxY - minY;
    const meanRadius = n > 0 ? sumR / n : 0.0;
    const eccentricity = Math.abs(spanX - spanY) / (Math.max(spanX, spanY) || 1.0);

    return {
        spanX,
        spanY,
        meanRadius,
        eccentricity,
        boundingBox: { minX, maxX, minY, maxY }
    };
}

// ============================================================================
// 3. Multi-Fault Synthetic Signal Generator
// ============================================================================

/**
 * Physics-based acceleration time-series synthesis.
 */
function generateSignal(params = {}) {
    const {
        durationSec = 0.32,      // 256 samples @ 800 Hz
        samplingRate = 800,
        rpm = 600,
        unbalanceMassG = 0.0,
        faultMode = 'NORMAL',    // 'NORMAL' | 'UNBALANCE' | 'MISALIGNMENT' | 'BEARING_BPFO' | 'BEARING_BPFI' | 'LOOSENESS' | 'SPI_DISCONNECT'
        faultSeverityPct = 100,
        noiseStdDevG = 0.025,
        gravityG = 1.0           // Static Z gravity
    } = params;

    const n = Math.round(durationSec * samplingRate);
    const t = new Float32Array(n);
    const ax = new Float32Array(n);
    const ay = new Float32Array(n);
    const az = new Float32Array(n);

    if (faultMode === 'SPI_DISCONNECT') {
        // Flatline 0g
        return { t, ax, ay, az, samplingRate, rpm, n };
    }

    const f0 = rpm / 60.0;
    const omega = 2.0 * Math.PI * f0;
    const sev = faultSeverityPct / 100.0;
    const dt = 1.0 / samplingRate;

    // Pseudo-random Gaussian noise generator (Box-Muller)
    let spareNoise = null;
    function randn() {
        if (spareNoise !== null) {
            const val = spareNoise;
            spareNoise = null;
            return val;
        }
        let u = 0, v = 0;
        while (u === 0) u = Math.random();
        while (v === 0) v = Math.random();
        const mag = Math.sqrt(-2.0 * Math.log(u));
        spareNoise = mag * Math.sin(2.0 * Math.PI * v);
        return mag * Math.cos(2.0 * Math.PI * v);
    }

    const unbalanceAmp = (unbalanceMassG / 5.0) * 1.85 * sev;

    for (let i = 0; i < n; i++) {
        const time = i * dt;
        t[i] = time;
        const phase = omega * time;

        const nx = noiseStdDevG > 0 ? (Math.random() - 0.5) * 2.0 * noiseStdDevG : 0.0;
        const ny = noiseStdDevG > 0 ? (Math.random() - 0.5) * 2.0 * noiseStdDevG : 0.0;
        const nz = noiseStdDevG > 0 ? (Math.random() - 0.5) * 2.0 * noiseStdDevG : 0.0;

        // Baseline 1X + 2X residual
        let x = 0.06 * Math.sin(phase) + 0.015 * Math.sin(2 * phase) + nx;
        let y = 0.06 * Math.cos(phase) + 0.015 * Math.cos(2 * phase) + ny;
        let z = gravityG + 0.02 * Math.sin(3 * phase) + nz;

        // Fault Modes
        if (faultMode === 'UNBALANCE' || unbalanceMassG > 0) {
            x += unbalanceAmp * Math.sin(phase);
            y += unbalanceAmp * Math.cos(phase);
            z += (unbalanceAmp * 0.35) * Math.sin(2 * phase);
        } else if (faultMode === 'MISALIGNMENT') {
            // Pronounced 1X + 2X harmonics with 180 deg phase shift
            const misAmp = 0.8 * sev;
            x += misAmp * Math.sin(phase) + (misAmp * 0.75) * Math.sin(2 * phase + Math.PI);
            y += misAmp * Math.cos(phase) + (misAmp * 0.75) * Math.cos(2 * phase);
            z += (misAmp * 0.5) * Math.sin(phase + Math.PI);
        } else if (faultMode === 'BEARING_BPFO') {
            // BPFO = 3.05 * f0 impact pulses
            const fBPFO = 3.05 * f0;
            const pulse = Math.exp(-Math.pow((time * fBPFO) % 1.0 - 0.1, 2) / 0.005) * 2.2 * sev;
            x += pulse * Math.sin(2 * Math.PI * 120.0 * time); // Ringing resonance
            y += pulse * 0.5;
            z += pulse * 0.3;
        } else if (faultMode === 'BEARING_BPFI') {
            // BPFI = 4.95 * f0 modulated by 1X rotation
            const fBPFI = 4.95 * f0;
            const mod = (1.0 + 0.6 * Math.sin(phase));
            const pulse = Math.exp(-Math.pow((time * fBPFI) % 1.0 - 0.1, 2) / 0.004) * 2.8 * sev * mod;
            x += pulse * Math.sin(2 * Math.PI * 180.0 * time);
            y += pulse * 0.7;
        } else if (faultMode === 'LOOSENESS') {
            // 0.5X subharmonic + truncation non-linearity (comb spectrum)
            const looseAmp = 1.1 * sev;
            const subPhase = 0.5 * phase;
            let valX = looseAmp * (Math.sin(subPhase) + 0.8 * Math.sin(phase) + 0.6 * Math.sin(1.5 * phase) + 0.4 * Math.sin(2 * phase));
            if (valX < -0.2) valX = -0.2; // Half-wave rectification / clipping due to structural bounce
            x += valX;
            y += valX * 0.6;
            z += valX * 0.4;
        }

        ax[i] = x;
        ay[i] = y;
        az[i] = z;
    }

    return { t, ax, ay, az, samplingRate, rpm, n };
}

// ============================================================================
// 4. File & DOM Structure Inspection Utilities
// ============================================================================

function inspectHTMLFile(htmlPath) {
    if (!fs.existsSync(htmlPath)) {
        throw new Error(`File does not exist: ${htmlPath}`);
    }
    const content = fs.readFileSync(htmlPath, 'utf8');

    return {
        content,
        sizeBytes: content.length,
        hasDoctype: /<!DOCTYPE html>/i.test(content),
        hasThreeJS: /three(\.min)?\.js/i.test(content) || /THREE\./.test(content),
        hasOrbitControls: /OrbitControls/i.test(content),
        hasCanvasWebGL: /webgl-container|canvas/i.test(content),
        hasDOMElement: (id) => content.includes(`id="${id}"`) || content.includes(`id='${id}'`),
        hasSelector: (sel) => content.includes(sel),
        countOccurrences: (str) => {
            const matches = content.match(new RegExp(str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'));
            return matches ? matches.length : 0;
        }
    };
}

// ============================================================================
// 5. RFC 4180 CSV and JSON Diagnostic Report Validators
// ============================================================================

function parseAndValidateCSV(csvString) {
    if (typeof csvString !== 'string' || csvString.trim().length === 0) {
        throw new Error('CSV is empty or invalid string');
    }
    const lines = csvString.trim().split(/\r?\n/);
    if (lines.length < 2) {
        throw new Error(`CSV contains only ${lines.length} lines, expected at least header + 1 data row`);
    }

    const headers = lines[0].split(',').map(h => h.trim());
    const expectedHeaders = ['timestamp_ms', 'sample_idx', 'rpm', 'ax_g', 'ay_g', 'az_g', 'vector_mag_g', 'vector_rms_g'];

    const headerMatch = expectedHeaders.every(eh => headers.some(h => h.toLowerCase().includes(eh.toLowerCase().replace('_', '')) || h.toLowerCase() === eh.toLowerCase()));

    const rows = [];
    for (let i = 1; i < lines.length; i++) {
        const cols = lines[i].split(',').map(v => parseFloat(v.trim()));
        if (cols.some(v => isNaN(v))) {
            throw new Error(`CSV line ${i + 1} contains NaN value: "${lines[i]}"`);
        }
        rows.push(cols);
    }

    return {
        headers,
        rowCount: rows.length,
        headerMatch,
        rows
    };
}

function validateJSONReport(reportObj) {
    if (typeof reportObj !== 'object' || reportObj === null) {
        throw new Error('Report is not a valid JSON object');
    }
    const requiredTopLevel = ['device', 'session', 'summary', 'fft_snapshot'];
    for (const key of requiredTopLevel) {
        if (!(key in reportObj)) {
            throw new Error(`Report missing required top-level key: "${key}"`);
        }
    }

    assert(typeof reportObj.session.duration_sec === 'number', 'session.duration_sec must be numeric');
    assert(typeof reportObj.summary.vector_rms_g === 'number', 'summary.vector_rms_g must be numeric');
    assert(Array.isArray(reportObj.fft_snapshot.frequencies), 'fft_snapshot.frequencies must be an array');
    assert(Array.isArray(reportObj.fft_snapshot.magnitudes), 'fft_snapshot.magnitudes must be an array');

    return true;
}

module.exports = {
    testCtx,
    describe,
    test,
    testAsync,
    assert,
    assertEqual,
    assertClose,
    assertArrayClose,
    assertThrows,
    assertRegex,
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
    fftRadix2,
    computeFFT,
    doubleIntegrate,
    evaluateISO10816,
    KOutOfMPersistenceEngine,
    computeLissajous,
    generateSignal,
    inspectHTMLFile,
    parseAndValidateCSV,
    validateJSONReport
};
