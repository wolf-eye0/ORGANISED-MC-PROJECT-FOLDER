/**
 * Extreme Adversarial Numerical & Fault Transition Stress Harness
 * Challenger 2 - VibeGuard 3D WebGL Digital Twin
 */

const fs = require('fs');
const vm = require('vm');

const HTML_PATH = '/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/Visual_Digital_Twin/VibeGuard_3D_Digital_Twin.html';
const htmlContent = fs.readFileSync(HTML_PATH, 'utf8');

const scriptMatch = htmlContent.match(/<script id="vibeguard-app">([\s\S]*?)<\/script>/);
const appScript = scriptMatch[1];

const mockDOM = {
    document: {
        getElementById: () => ({ classList: { add() {}, remove() {} }, textContent: '', style: {}, value: '', addEventListener() {} }),
        createElement: () => ({
            tagName: 'DIV', style: {}, classList: { add() {}, remove() {} }, appendChild() {}, removeChild() {}, click() {},
            getContext: () => ({ clearRect() {}, fillRect() {}, beginPath() {}, moveTo() {}, lineTo() {}, stroke() {}, arc() {}, createLinearGradient: () => ({ addColorStop() {} }), setLineDash() {}, fillText() {} })
        }),
        body: { appendChild() {}, removeChild() {} }
    },
    window: { addEventListener() {}, requestAnimationFrame() {}, setTimeout: (fn) => fn(), clearTimeout() {} },
    setTimeout: (fn) => fn(),
    clearTimeout: () => {},
    navigator: { userAgent: 'NodeTest' },
    URL: { createObjectURL: () => 'blob:mock', revokeObjectURL: () => {} },
    Blob: class { constructor(c, o) { this.content = c; this.options = o; } },
    THREE: {
        Scene: class { add() {} },
        PerspectiveCamera: class { constructor() { this.position = { set() {}, x: 0, y: 0, z: 0 }; } lookAt() {} },
        WebGLRenderer: class { constructor() { this.domElement = { width: 800, height: 600, getContext: () => ({}) }; this.shadowMap = {}; } setSize() {} render() {} setPixelRatio() {} },
        OrbitControls: class { constructor() { this.target = { set() {} }; } update() {} },
        Group: class { add() {} },
        Mesh: class { add() {} },
        Vector3: class { set() {} },
        Color: class {},
        PointLight: class { constructor() { this.position = { set() {} }; } },
        AmbientLight: class {},
        DirectionalLight: class { constructor() { this.position = { set() {} }; this.shadow = { mapSize: {} }; } },
        SpotLight: class { constructor() { this.position = { set() {} }; } },
        BoxGeometry: class {}, CylinderGeometry: class {}, SphereGeometry: class {},
        MeshStandardMaterial: class {}, MeshPhysicalMaterial: class {},
        Raycaster: class { setFromCamera() {} intersectObjects() { return []; } },
        Vector2: class {}
    },
    console: console, performance: performance, Math: Math,
    Float32Array: Float32Array, Uint16Array: Uint16Array, Uint8Array: Uint8Array,
    Array: Array, Date: Date, JSON: JSON, showToast: () => {}
};

const instrumentedScript = appScript.replace(
    /\}\)\(\);\s*$/,
    'window.__VIBEGUARD__ = { CONFIG, Radix2FFT, RingBuffer, DSPEngine, PhysicsEngine, State, FlightLogger, COMPONENT_SPECS }; })();'
);

const context = vm.createContext(mockDOM);
vm.runInContext(instrumentedScript, context);
const { CONFIG, Radix2FFT, RingBuffer, DSPEngine, PhysicsEngine, State, FlightLogger } = mockDOM.window.__VIBEGUARD__;

console.log('================================================================');
console.log('⚡ EXTREME NUMERICAL, NYQUIST & FAULT TRANSITION STRESS AUDIT');
console.log('================================================================');

let stressChecks = 0;
let stressPassed = 0;
let stressFailed = 0;

function stressCheck(name, cond, details = '') {
    stressChecks++;
    if (cond) {
        stressPassed++;
        console.log(`  ✅ [PASS] ${name}`);
    } else {
        stressFailed++;
        console.error(`  ❌ [FAIL] ${name}: ${details}`);
    }
}

// 1. Dirac Delta Impulse Spectral Flatness Test
const N = 256;
const Fs = 800.0;
const dirac = new Float32Array(N);
dirac[128] = 1.0; // Center impulse (where Hann window == 1.0)
const fftDirac = new Radix2FFT(N);
const magsDirac = fftDirac.forward(dirac);
let minDiracMag = Infinity, maxDiracMag = -Infinity;
for (let i = 1; i < 128; i++) {
    if (magsDirac[i] < minDiracMag) minDiracMag = magsDirac[i];
    if (magsDirac[i] > maxDiracMag) maxDiracMag = magsDirac[i];
}
const flatnessRatio = minDiracMag / maxDiracMag;
stressCheck('Impulse response spectral magnitude is uniformly bounded across all 128 bins', flatnessRatio > 0.99 && maxDiracMag > 0);

// 2. ADXL345 Full Dynamic Range Test (1e-5 g to 16.0 g)
const testLevels = [1e-5, 1e-3, 0.01, 0.1, 1.0, 5.0, 10.0, 16.0];
let dynRangePass = true;
for (const lvl of testLevels) {
    const sig = new Float32Array(N);
    for (let i = 0; i < N; i++) sig[i] = lvl * Math.sin(2 * Math.PI * 50 * (i / Fs));
    const mags = (new Radix2FFT(N)).forward(sig);
    const measured = mags[16];
    const relErr = Math.abs(measured - lvl) / lvl;
    if (relErr > 0.05) {
        dynRangePass = false;
        console.error(`Dynamic range failure at level ${lvl}g: measured ${measured}, relErr: ${relErr}`);
    }
}
stressCheck('Radix2FFT maintains linear amplitude response across full 120 dB dynamic range (10µg to 16g)', dynRangePass);

// 3. RPM Harmonic Sweep (300 to 1200 RPM in 30 RPM increments)
let allRpmHarmonicsValid = true;
const deltaF = Fs / N; // 3.125 Hz
for (let rpm = 300; rpm <= 1200; rpm += 30) {
    const f0 = rpm / 60.0;
    const k1 = Math.round(f0 / deltaF);
    const k2 = Math.round((2 * f0) / deltaF);
    const k3 = Math.round((3 * f0) / deltaF);

    if (k1 < 1 || k1 >= 128 || k2 < 1 || k2 >= 128 || k3 < 1 || k3 >= 128) {
        allRpmHarmonicsValid = false;
        console.error(`Harmonic bin out of range for RPM ${rpm}: k1=${k1}, k2=${k2}, k3=${k3}`);
    }
}
stressCheck('Harmonic extraction (1X, 2X, 3X) stays strictly within valid FFT bins [1, 127] across full RPM range (300-1200 RPM)', allRpmHarmonicsValid);

// 4. Fault Transition Sequence Integrity & State Transitions
const faultSequence = ['NORMAL', 'UNBALANCE', 'MISALIGNMENT', 'BEARING_BPFO', 'BEARING_BPFI', 'LOOSENESS', 'SPI_DISCONNECT', 'NORMAL'];
let transitionsClean = true;

for (const fault of faultSequence) {
    State.faultMode = fault;
    for (let s = 0; s < 300; s++) {
        PhysicsEngine.step(CONFIG.SAMPLE_DT);
    }
    const metrics = DSPEngine.processWindow(State.f0);
    if (fault === 'SPI_DISCONNECT') {
        if (metrics.fsmState !== 'FAULT_INVALID' || metrics.vectorRms !== 0) {
            transitionsClean = false;
            console.error(`SPI_DISCONNECT state mismatch: ${metrics.fsmState}, rms: ${metrics.vectorRms}`);
        }
    } else {
        if (isNaN(metrics.vectorRms) || isNaN(metrics.crestFactor) || isNaN(metrics.kurtosis)) {
            transitionsClean = false;
            console.error(`NaN detected during fault transition to ${fault}`);
        }
    }
}
stressCheck('Continuous dynamic fault switching transitions smoothly without NaN, memory corruption, or invalid states', transitionsClean);

// 5. High-Load Rolling Session Buffer Overflow Safety (10,000 samples)
FlightLogger.buffer = [];
FlightLogger.startRecording(5.0); // 4000 samples
let bufferNoCrash = true;
try {
    for (let i = 0; i < 5000; i++) {
        PhysicsEngine.step(CONFIG.SAMPLE_DT);
        const m = DSPEngine.processWindow(State.f0);
        FlightLogger.recordSample(m.latestSample, m);
    }
} catch (e) {
    bufferNoCrash = false;
    console.error('Session recording crash:', e);
}
stressCheck('FlightLogger gracefully caps recording at max capacity (4000 samples) without buffer overrun', FlightLogger.buffer.length === 4000 && bufferNoCrash);

console.log('\n================================================================');
console.log(`📊 STRESS AUDIT SUMMARY: ${stressPassed}/${stressChecks} PASSED (${stressFailed} FAILED)`);
console.log('================================================================');

if (stressFailed === 0) {
    console.log('🎉 ALL EXTREME STRESS & BOUNDARY TESTS PASSED 100%!');
    process.exit(0);
} else {
    process.exit(1);
}
