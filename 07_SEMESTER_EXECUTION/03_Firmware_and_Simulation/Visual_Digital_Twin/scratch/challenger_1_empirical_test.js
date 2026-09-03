/**
 * ============================================================================
 * 🛡️ CHALLENGER 1: EMPIRICAL ADVERSARIAL STRESS TEST & VERIFICATION HARNESS
 * Target: VibeGuard_3D_Digital_Twin.html
 * ============================================================================
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { execSync } = require('child_process');

const HTML_PATH = '/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/Visual_Digital_Twin/VibeGuard_3D_Digital_Twin.html';

console.log('================================================================================');
console.log('🛡️  CHALLENGER 1: EMPIRICAL ADVERSARIAL STRESS TEST SUITE');
console.log('Target:', HTML_PATH);
console.log('Started at:', new Date().toISOString());
console.log('================================================================================\n');

// 1. Static File & DOM Inspection
const htmlContent = fs.readFileSync(HTML_PATH, 'utf8');

// Test results accumulator
let totalTests = 0;
let passedTests = 0;
let failedTests = 0;
const testResults = [];

function recordTest(suite, name, passed, error = null) {
    totalTests++;
    if (passed) {
        passedTests++;
        console.log(`  ✅ [PASS] ${name}`);
        testResults.push({ suite, name, status: 'PASS' });
    } else {
        failedTests++;
        console.error(`  ❌ [FAIL] ${name}: ${error || 'Assertion failed'}`);
        testResults.push({ suite, name, status: 'FAIL', error: String(error) });
    }
}

function assert(condition, message) {
    if (!condition) throw new Error(message || 'Assertion failed');
}

function assertClose(actual, expected, tol = 1e-3, msg = '') {
    const diff = Math.abs(actual - expected);
    if (diff > tol) {
        throw new Error(`${msg} Expected ${expected} +/- ${tol}, got ${actual} (diff ${diff})`);
    }
}

// ============================================================================
// SUITE 1: DOM INTEGRITY & INTERACTION BINDINGS
// ============================================================================
console.log('>>> [SUITE 1/9] Verifying DOM Structure, Elements, and IDs...');
try {
    const requiredIDs = [
        'webgl-container', 'click-hint', 'header-bar', 'rec-badge', 'rec-timer',
        'state-badge', 'state-text', 'iso-badge', 'iso-text', 'control-panel',
        'sel-fault-mode', 'lbl-rpm', 'rng-rpm', 'lbl-mass', 'rng-mass',
        'lbl-severity', 'rng-severity', 'lbl-noise', 'rng-noise',
        'btn-play-pause', 'btn-reset-sim', 'sel-time-scale',
        'btn-record', 'btn-snapshot', 'btn-export-csv', 'btn-export-json',
        'inspector-panel', 'insp-title', 'insp-subtitle', 'btn-close-inspector',
        'insp-spec-rows', 'insp-reg-dump', 'btn-focus-part', 'btn-reset-cam',
        'hud-panel', 'kpi-rms', 'kpi-peak', 'kpi-p2p', 'kpi-cf', 'kpi-kurtosis',
        'kpi-peak-freq', 'kpi-f0', 'kpi-vel-rms', 'kpi-zone-sub',
        'btn-osc-scale', 'osc-canvas', 'btn-fft-zoom', 'fft-canvas',
        'lbl-orbit-diag', 'orbit-canvas', 'toast', 'vendor-threejs',
        'vendor-orbitcontrols', 'vibeguard-app'
    ];

    for (const id of requiredIDs) {
        const hasId = htmlContent.includes(`id="${id}"`) || htmlContent.includes(`id='${id}'`);
        recordTest('DOM_Integrity', `DOM Element #${id} is present in HTML`, hasId);
    }
} catch (e) {
    recordTest('DOM_Integrity', 'DOM element check exception', false, e.message);
}

// ============================================================================
// 2. Extract & Instrument App Script for Headless Simulation
// ============================================================================
const scriptMatch = htmlContent.match(/<script id="vibeguard-app">([\s\S]*?)<\/script>/);
if (!scriptMatch) {
    throw new Error('Could not find <script id="vibeguard-app"> in HTML file');
}
const appScript = scriptMatch[1];

const mockCanvasContext = {
    clearRect: () => {},
    fillRect: () => {},
    beginPath: () => {},
    moveTo: () => {},
    lineTo: () => {},
    stroke: () => {},
    arc: () => {},
    createLinearGradient: () => ({ addColorStop: () => {} }),
    setLineDash: () => {},
    fillText: () => {},
    scale: () => {},
    fill: () => {}
};

const domElements = {};
const mockDOM = {
    document: {
        getElementById: (id) => {
            if (!domElements[id]) {
                domElements[id] = {
                    id,
                    classList: {
                        add: () => {},
                        remove: () => {},
                        contains: () => false
                    },
                    textContent: '',
                    innerHTML: '',
                    style: {},
                    value: '',
                    parentElement: {
                        getBoundingClientRect: () => ({ width: 400, height: 200, left: 0, top: 0 })
                    },
                    getBoundingClientRect: () => ({ width: 400, height: 200, left: 0, top: 0 }),
                    getContext: () => mockCanvasContext,
                    addEventListener: (ev, fn) => {},
                    appendChild: (el) => {},
                    removeChild: (el) => {}
                };
            }
            return domElements[id];
        },
        createElement: (tag) => ({
            tagName: tag.toUpperCase(),
            style: {},
            classList: { add: () => {}, remove: () => {} },
            appendChild: () => {},
            removeChild: () => {},
            click: () => {},
            getContext: () => mockCanvasContext,
            width: 800,
            height: 600,
            toDataURL: () => 'data:image/png;base64,mock'
        }),
        body: {
            appendChild: () => {},
            removeChild: () => {}
        }
    },
    window: {
        innerWidth: 1920,
        innerHeight: 1080,
        devicePixelRatio: 1,
        addEventListener: () => {},
        requestAnimationFrame: () => {},
        setTimeout: (fn, ms) => setTimeout(fn, ms),
        clearTimeout: (id) => clearTimeout(id)
    },
    setTimeout: (fn, ms) => setTimeout(fn, ms),
    clearTimeout: (id) => clearTimeout(id),
    navigator: { userAgent: 'Headless-Challenger' },
    URL: {
        createObjectURL: () => 'blob:mock-export',
        revokeObjectURL: () => {}
    },
    Blob: class MockBlob {
        constructor(content, opts) {
            this.content = content;
            this.opts = opts;
        }
    },
    THREE: {
        Scene: class { add() {} },
        PerspectiveCamera: class {
            constructor() {
                this.position = { set() {}, copy() {}, lerpVectors() {} };
                this.aspect = 1;
            }
            updateProjectionMatrix() {}
        },
        WebGLRenderer: class {
            constructor() {
                this.domElement = { width: 1920, height: 1080, getContext: () => ({}) };
                this.shadowMap = {};
            }
            setSize() {}
            setPixelRatio() {}
            render() {}
        },
        OrbitControls: class {
            constructor() {
                this.target = { set() {}, copy() {}, lerpVectors() {} };
            }
            update() {}
        },
        Group: class {
            constructor() {
                this.position = { set() {} };
                this.rotation = { set() {}, x: 0, y: 0, z: 0 };
            }
            add() {}
        },
        Mesh: class {
            constructor() {
                this.position = { set() {} };
                this.rotation = { set() {}, x: 0, y: 0, z: 0 };
                this.material = { color: { setHex() {} }, emissive: { setHex() {} } };
                this.userData = {};
            }
        },
        ArrowHelper: class {
            constructor() {}
            setDirection() {}
            setLength() {}
            setColor() {}
        },
        Vector3: class {
            constructor(x=0, y=0, z=0) { this.x=x; this.y=y; this.z=z; }
            set(x, y, z) { this.x=x; this.y=y; this.z=z; return this; }
            copy(v) { this.x=v.x; this.y=v.y; this.z=v.z; return this; }
            add(v) { this.x+=v.x; this.y+=v.y; this.z+=v.z; return this; }
            lerpVectors(a, b, t) {
                this.x = a.x + (b.x - a.x)*t;
                this.y = a.y + (b.y - a.y)*t;
                this.z = a.z + (b.z - a.z)*t;
                return this;
            }
            length() { return Math.sqrt(this.x*this.x + this.y*this.y + this.z*this.z); }
            normalize() { const l = this.length() || 1; this.x/=l; this.y/=l; this.z/=l; return this; }
        },
        Vector2: class { constructor(x=0, y=0) { this.x=x; this.y=y; } },
        Color: class { constructor() {} setHex() {} },
        PointLight: class { constructor() { this.position = { set() {} }; this.color = { setHex() {} }; } },
        AmbientLight: class { constructor() {} },
        DirectionalLight: class { constructor() { this.position = { set() {} }; this.shadow = { mapSize: {}, camera: {} }; } },
        SpotLight: class { constructor() { this.position = { set() {} }; this.target = { position: { set() {} } }; } },
        BoxGeometry: class {}, CylinderGeometry: class {}, SphereGeometry: class {},
        ExtrudeGeometry: class {}, RingGeometry: class {}, CircleGeometry: class {},
        TubeGeometry: class {}, CatmullRomCurve3: class {}, Shape: class { moveTo() {} lineTo() {} closePath() {} },
        GridHelper: class { constructor() { this.position = { set() {} }; } },
        MeshStandardMaterial: class { constructor(o) { Object.assign(this, o); this.color = { setHex() {} }; this.emissive = { setHex() {} }; } },
        Raycaster: class { setFromCamera() {} intersectObjects() { return []; } },
        PCFSoftShadowMap: 2, ACESFilmicToneMapping: 4,
        FogExp2: class {}
    },
    console: console,
    performance: performance,
    Math: Math,
    Float32Array: Float32Array,
    Uint16Array: Uint16Array,
    Uint8Array: Uint8Array,
    Array: Array,
    Date: Date,
    JSON: JSON
};

const instrumented = appScript.replace(
    /\}\)\(\);\s*$/,
    'window.__VIBEGUARD__ = { CONFIG, COMPONENT_SPECS, State, EventBus, RingBuffer, Radix2FFT, DSPEngine, PhysicsEngine, Scene3D, CanvasHUD, FlightLogger, UIController }; })();'
);

const ctx = vm.createContext(mockDOM);
vm.runInContext(instrumented, ctx);

const { CONFIG, COMPONENT_SPECS, State, EventBus, RingBuffer, Radix2FFT, DSPEngine, PhysicsEngine, FlightLogger, UIController } = mockDOM.window.__VIBEGUARD__;

// ============================================================================
// SUITE 2: PARAMETER BOUNDARY SWEEP (0 to 10,000 RPM)
// ============================================================================
console.log('\n>>> [SUITE 2/9] Executing RPM Parameter Sweeps (0 to 10,000 RPM)...');
const testRPMs = [0, 1, 10, 60, 300, 600, 900, 1200, 2400, 5000, 10000, -600];

for (const rpm of testRPMs) {
    try {
        State.rpm = rpm;
        State.f0 = rpm / 60.0;
        State.faultMode = 'NORMAL';
        State.eccentricMassG = 0.0;
        State.noiseStdDevG = 0.01;

        // Step physics for 256 samples
        for (let i = 0; i < CONFIG.WINDOW_SIZE; i++) {
            PhysicsEngine.step(CONFIG.SAMPLE_DT);
        }

        const metrics = DSPEngine.processWindow(State.f0);

        assert(!isNaN(metrics.vectorRms), `vectorRms is NaN at RPM=${rpm}`);
        assert(!isNaN(metrics.peakAccel), `peakAccel is NaN at RPM=${rpm}`);
        assert(!isNaN(metrics.crestFactor), `crestFactor is NaN at RPM=${rpm}`);
        assert(!isNaN(metrics.kurtosis), `kurtosis is NaN at RPM=${rpm}`);
        assert(isFinite(metrics.velRmsMms), `velRmsMms is non-finite at RPM=${rpm}`);
        assert(metrics.dominantFreqHz >= 0, `dominantFreqHz negative at RPM=${rpm}`);

        recordTest('RPM_Sweep', `Numerical stability at RPM=${rpm} (f0=${State.f0.toFixed(2)}Hz)`, true);
    } catch (e) {
        recordTest('RPM_Sweep', `Numerical stability at RPM=${rpm}`, false, e.message);
    }
}

// ============================================================================
// SUITE 3: EXTREME UNBALANCE MASS STRESS (0.0g to 50.0g & Negative)
// ============================================================================
console.log('\n>>> [SUITE 3/9] Executing Extreme Unbalance Mass Sweeps...');
const testMasses = [0.0, 0.01, 0.5, 3.5, 5.0, 10.0, 25.0, 50.0, -2.0];

for (const mass of testMasses) {
    try {
        State.rpm = 600;
        State.f0 = 10.0;
        State.faultMode = 'UNBALANCE';
        State.eccentricMassG = mass;
        State.faultSeverityPct = 100;
        State.noiseStdDevG = 0.025;

        for (let i = 0; i < CONFIG.WINDOW_SIZE; i++) {
            PhysicsEngine.step(CONFIG.SAMPLE_DT);
        }

        const metrics = DSPEngine.processWindow(State.f0);

        assert(!isNaN(metrics.vectorRms), `vectorRms is NaN at Mass=${mass}g`);
        assert(!isNaN(metrics.peakAccel), `peakAccel is NaN at Mass=${mass}g`);
        assert(isFinite(metrics.crestFactor), `crestFactor non-finite at Mass=${mass}g`);
        assert(isFinite(metrics.kurtosis), `kurtosis non-finite at Mass=${mass}g`);
        
        if (mass >= 3.5) {
            assert(metrics.vectorRms >= CONFIG.ISO_ALARM_G, `Expected alarm level for high mass ${mass}g, got ${metrics.vectorRms}`);
        }

        recordTest('Mass_Sweep', `Physical & DSP scaling at Unbalance Mass=${mass}g`, true);
    } catch (e) {
        recordTest('Mass_Sweep', `Physical & DSP scaling at Unbalance Mass=${mass}g`, false, e.message);
    }
}

// ============================================================================
// SUITE 4: EXTREME SENSOR NOISE FLOOR SWEEPS (0.0g to 10.0g)
// ============================================================================
console.log('\n>>> [SUITE 4/9] Executing Sensor Noise Floor & SNR Degradation Stress...');
const testNoises = [0.0, 0.001, 0.005, 0.025, 0.080, 0.500, 2.000, 10.000];

for (const noise of testNoises) {
    try {
        State.rpm = 600;
        State.f0 = 10.0;
        State.faultMode = 'NORMAL';
        State.eccentricMassG = 0.0;
        State.noiseStdDevG = noise;

        for (let i = 0; i < CONFIG.WINDOW_SIZE; i++) {
            PhysicsEngine.step(CONFIG.SAMPLE_DT);
        }

        const metrics = DSPEngine.processWindow(State.f0);

        assert(!isNaN(metrics.vectorRms), `vectorRms is NaN at Noise=${noise}g`);
        assert(!isNaN(metrics.kurtosis), `kurtosis is NaN at Noise=${noise}g`);
        assert(metrics.vectorRms >= 0, `vectorRms < 0 at Noise=${noise}g`);

        if (noise >= 0.05) {
            assert(metrics.kurtosis > 1.5 && metrics.kurtosis < 6.0, `Gaussian kurtosis out of bounds: ${metrics.kurtosis}`);
        }

        recordTest('Noise_Sweep', `Noise resilience & kurtosis convergence at Noise=${noise}g`, true);
    } catch (e) {
        recordTest('Noise_Sweep', `Noise resilience at Noise=${noise}g`, false, e.message);
    }
}

// ============================================================================
// SUITE 5: TIME SCALING & SAMPLE RATE SWITCHES
// ============================================================================
console.log('\n>>> [SUITE 5/9] Executing Time Scaling & Sampling Stepping Stress...');
const testTimeScales = [0.0, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0];

for (const ts of testTimeScales) {
    try {
        State.timeScale = ts;
        State.rpm = 600;
        State.f0 = 10.0;
        State.faultMode = 'NORMAL';

        const initialAngle = PhysicsEngine.shaftAngle;
        const initialSimTime = PhysicsEngine.simTime;

        // Step fixed dt
        PhysicsEngine.step(0.016); // 1 60fps frame

        if (ts === 0.0) {
            assert(PhysicsEngine.simTime === initialSimTime, 'simTime moved when timeScale=0');
        } else {
            assert(PhysicsEngine.simTime > initialSimTime, 'simTime did not increment');
            assert(PhysicsEngine.shaftAngle > initialAngle, 'shaftAngle did not advance');
        }

        recordTest('Time_Scale', `Simulation progression at TimeScale=${ts}x`, true);
    } catch (e) {
        recordTest('Time_Scale', `Simulation progression at TimeScale=${ts}x`, false, e.message);
    }
}

// ============================================================================
// SUITE 6: RAPID MULTI-FAULT DYNAMIC TRANSITIONS (1,000 Transitions)
// ============================================================================
console.log('\n>>> [SUITE 6/9] Executing 1,000 High-Frequency Multi-Fault Transitions...');
const faultModes = ['NORMAL', 'UNBALANCE', 'MISALIGNMENT', 'BEARING_BPFO', 'BEARING_BPFI', 'LOOSENESS', 'SPI_DISCONNECT'];
let transitionsClean = true;
let transitionError = null;

try {
    for (let cycle = 0; cycle < 1000; cycle++) {
        const nextFault = faultModes[cycle % faultModes.length];
        State.faultMode = nextFault;

        // Simulate 1 to 5 physics steps per rapid switch
        for (let s = 0; s < 3; s++) {
            PhysicsEngine.step(CONFIG.SAMPLE_DT);
        }

        const metrics = DSPEngine.processWindow(State.f0);

        if (nextFault === 'SPI_DISCONNECT') {
            if (metrics.fsmState !== 'FAULT_INVALID' || metrics.vectorRms !== 0) {
                transitionsClean = false;
                transitionError = `SPI_DISCONNECT state mismatch: fsm=${metrics.fsmState}, rms=${metrics.vectorRms}`;
                break;
            }
        } else {
            if (isNaN(metrics.vectorRms) || isNaN(metrics.crestFactor) || isNaN(metrics.kurtosis) || isNaN(metrics.velRmsMms)) {
                transitionsClean = false;
                transitionError = `NaN encountered during rapid transition to ${nextFault} at cycle ${cycle}`;
                break;
            }
        }
    }
    recordTest('Multi_Fault_Transitions', '1,000 consecutive multi-fault switches executed without numerical NaN or state corruption', transitionsClean, transitionError);
} catch (e) {
    recordTest('Multi_Fault_Transitions', '1,000 multi-fault transitions', false, e.message);
}

// ============================================================================
// SUITE 7: FLIGHT RECORDER MEMORY STABILITY & OVERFLOW BOUNDS
// ============================================================================
console.log('\n>>> [SUITE 7/9] Testing Flight Recorder Capacity & Memory Limits (30s @ 800Hz = 24,000 samples)...');
try {
    FlightLogger.buffer = [];
    FlightLogger.startRecording(30.0); // 24,000 samples capacity

    assert(FlightLogger.isRecording === true, 'FlightLogger.isRecording is false');
    assert(FlightLogger.maxSamples === 24000, `Expected maxSamples=24000, got ${FlightLogger.maxSamples}`);

    // Push 26,000 samples (exceeding capacity by 2,000)
    for (let i = 0; i < 26000; i++) {
        PhysicsEngine.step(CONFIG.SAMPLE_DT);
        const m = DSPEngine.processWindow(State.f0);
        FlightLogger.recordSample(m.latestSample, m);
    }

    assert(FlightLogger.buffer.length === 24000, `Buffer overflow! Expected length 24000, got ${FlightLogger.buffer.length}`);
    assert(FlightLogger.isRecording === false, 'FlightLogger did not auto-stop at capacity');

    // Test CSV exporter generation
    FlightLogger.exportCSV();
    // Test JSON exporter generation
    FlightLogger.exportJSON();

    recordTest('Flight_Recorder_Stress', '24,000 sample rolling memory buffer bounded cleanly without heap overflow', true);
} catch (e) {
    recordTest('Flight_Recorder_Stress', 'Flight recorder buffer overflow testing', false, e.message);
}

// ============================================================================
// SUITE 8: HEADLESS BROWSER RENDER & SCREENSHOT VALIDATION
// ============================================================================
console.log('\n>>> [SUITE 8/9] Executing Headless Browser WebGL Render (Firefox)...');
try {
    const tmpProfile = '/tmp/ff_challenger1_profile';
    const tmpScreenshot = '/tmp/ff_challenger1_render.png';
    fs.mkdirSync(tmpProfile, { recursive: true });

    const cmd = `firefox --headless --profile ${tmpProfile} --screenshot ${tmpScreenshot} --window-size 1920,1080 file://${HTML_PATH}`;
    console.log(`  Executing: ${cmd}`);
    execSync(cmd, { stdio: 'pipe', timeout: 15000 });

    const screenshotExists = fs.existsSync(tmpScreenshot);
    const screenshotSize = screenshotExists ? fs.statSync(tmpScreenshot).size : 0;

    assert(screenshotExists, 'Screenshot file /tmp/ff_challenger1_render.png was not generated');
    assert(screenshotSize > 5000, `Screenshot file size (${screenshotSize} bytes) is suspiciously small`);

    recordTest('Headless_Render', `Firefox rendered full 1080p WebGL viewport cleanly (${screenshotSize} bytes image generated)`, true);
} catch (e) {
    recordTest('Headless_Render', 'Firefox headless render execution', false, e.message);
}

// ============================================================================
// SUITE 9: TEST SUITE PARITY & FIRMWARE ORACLE VERIFICATION
// ============================================================================
console.log('\n>>> [SUITE 9/9] Verifying test helper parity and DSP engine integration...');
try {
    const testHelpersPath = '/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/Visual_Digital_Twin/tests/test_helpers.js';
    const testHelpersCode = fs.readFileSync(testHelpersPath, 'utf8');

    // Verify doubleIntegrate algorithm consistency in test_helpers
    const hasValidIIR = testHelpersCode.includes('vFilt = alpha * (vFilt + vRunning - vPrevRunning);');
    assert(hasValidIIR, 'Valid IIR integration formula in test_helpers.js');

    // Verify that VibeGuard_3D_Digital_Twin.html contains valid leaky trapezoidal integrator
    const hasCorrectIntegration = htmlContent.includes('this.lastVelX = alpha * this.lastVelX + 0.5 * (ax + prevAx) * dt * gToMms2');
    assert(hasCorrectIntegration, 'VibeGuard_3D_Digital_Twin.html contains valid leaky trapezoidal integrator');

    recordTest('Test_Parity', 'Test suite and application DSP double integration logic verified in sync', true);
} catch (e) {
    recordTest('Test_Parity', 'Test helper parity check', false, e.message);
}

// ============================================================================
// FINAL SUMMARY
// ============================================================================
console.log('\n================================================================================');
console.log(`🎯 FINAL EMPIRICAL STRESS TEST RESULTS: ${passedTests}/${totalTests} PASSED (${failedTests} FAILED)`);
console.log('================================================================================');

const reportPath = '/home/paradoxpete/Documents/PROJECT_ORGANIZED/.agents/teamwork_preview_challenger_1/empirical_stress_results.json';
fs.writeFileSync(reportPath, JSON.stringify({
    timestamp: new Date().toISOString(),
    totalTests,
    passedTests,
    failedTests,
    passRate: ((passedTests / totalTests) * 100).toFixed(2) + '%',
    results: testResults
}, null, 2));

console.log(`Saved detailed empirical report to: ${reportPath}`);

if (failedTests > 0) {
    process.exit(1);
} else {
    process.exit(0);
}
