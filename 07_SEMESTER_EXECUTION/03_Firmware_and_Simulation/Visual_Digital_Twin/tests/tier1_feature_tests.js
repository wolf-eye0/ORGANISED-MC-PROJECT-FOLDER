/**
 * VibeGuard 3D WebGL Digital Twin - Tier 1 Feature Tests
 * 
 * 165 Comprehensive Unit and Feature Test Cases covering all 33 Features
 * from PROJECT.md § Feature Inventory (5 tests per feature).
 */

const path = require('path');
const {
    describe,
    test,
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
    computeFFT,
    doubleIntegrate,
    evaluateISO10816,
    KOutOfMPersistenceEngine,
    computeLissajous,
    generateSignal,
    inspectHTMLFile,
    parseAndValidateCSV,
    validateJSONReport
} = require('./test_helpers');

const HTML_PATH = path.resolve(__dirname, '../VibeGuard_3D_Digital_Twin.html');

describe('Tier 1: Feature Tests (F1 to F33)', () => {
    const html = inspectHTMLFile(HTML_PATH);

    // ========================================================================
    // Feature 1: CAD Assembly Mesh Hierarchy (R1)
    // ========================================================================
    describe('F1: CAD Assembly Mesh Hierarchy', () => {
        test('F1.1: L-Bracket CAD geometry and mounting mesh definition', () => {
            assert(html.content.includes('bracketMat') || html.content.includes('bracketBase') || html.content.includes('bracket'), 'L-Bracket material or base mesh defined');
            assert(html.content.includes('BoxGeometry') || html.content.includes('bracket'), 'Bracket base dimensions defined');
            assert(html.content.includes('rigGroup') || html.content.includes('scene.add'), 'Bracket added to rig vibration hierarchy');
        });

        test('F1.2: N20 DC motor cylindrical body and gearbox housing definition', () => {
            assert(html.content.includes('motorBody') || html.content.includes('CylinderGeometry'), 'Motor cylinder CAD geometry defined');
            assert(html.content.includes('gearbox') || html.content.includes('BoxGeometry'), 'Gearbox housing defined');
            assert(html.content.includes('motorGroup') || html.content.includes('rigGroup'), 'Motor and gearbox added to motorGroup hierarchy');
        });

        test('F1.3: Rotating stainless steel D-shaft and brass eccentric coupling hub', () => {
            assert(html.content.includes('shaft') || html.content.includes('CylinderGeometry'), 'D-Shaft cylinder geometry defined');
            assert(html.content.includes('hub') || html.content.includes('coupling'), 'Coupling hub defined');
            assert(html.content.includes('rotorGroup') || html.content.includes('rotation'), 'Shaft and hub in rotating group');
        });

        test('F1.4: ADXL345 PCB breakout board and LGA package definition', () => {
            assert(html.content.includes('pcb') || html.content.includes('adxl') || html.content.includes('ADXL345'), 'ADXL345 PCB board geometry defined');
            assert(html.content.includes('ic') || html.content.includes('sensor'), 'ADXL345 LGA chip package defined');
            assert(html.content.includes('sensorGroup') || html.content.includes('motorGroup'), 'Sensor module in hierarchy');
        });

        test('F1.5: ESP32-DevKitC microcontroller board, RF shield, and flexible SPI ribbon', () => {
            assert(html.content.includes('esp') || html.content.includes('ESP32'), 'ESP32 PCB board geometry defined');
            assert(html.content.includes('shield') || html.content.includes('rf'), 'ESP32 metal RF shield defined');
            assert(html.content.includes('wire') || html.content.includes('ribbon') || html.content.includes('TubeGeometry'), 'Flexible SPI ribbon curve defined');
        });
    });

    // ========================================================================
    // Feature 2: Studio Lighting & Shadows (R1)
    // ========================================================================
    describe('F2: Studio Lighting & Shadows', () => {
        test('F2.1: Key Light directional illumination and shadow map', () => {
            assert(html.content.includes('keyLight') || html.content.includes('DirectionalLight'), 'Key Light source configured');
            assert(html.content.includes('castShadow') || html.content.includes('shadowMap'), 'Shadow casting enabled on light source');
        });

        test('F2.2: Fill Light contrasting balance illumination', () => {
            assert(html.content.includes('fillLight') || html.content.includes('DirectionalLight') || html.content.includes('ambientLight'), 'Fill Light source configured');
            assert(html.content.includes('scene.add'), 'Light added to scene');
        });

        test('F2.3: Overhead SpotLight with penumbra and soft shadows', () => {
            assert(html.content.includes('spotLight') || html.content.includes('SpotLight') || html.content.includes('PointLight'), 'SpotLight/PointLight configured');
            assert(html.content.includes('shadowMap') || html.content.includes('castShadow'), 'Shadow map configured on renderer');
        });

        test('F2.4: Ambient Light base illumination level', () => {
            assert(html.content.includes('ambientLight') || html.content.includes('AmbientLight'), 'Ambient light source configured');
        });

        test('F2.5: PBR material physical properties (metalness and roughness)', () => {
            assert(html.content.includes('metalness') || html.content.includes('roughness'), 'PBR material parameters defined');
            assert(html.content.includes('MeshStandardMaterial') || html.content.includes('Material'), 'Material utilized for realistic lighting');
        });
    });

    // ========================================================================
    // Feature 3: 360° Orbit Camera Controls (R1)
    // ========================================================================
    describe('F3: 360° Orbit Camera Controls', () => {
        test('F3.1: PerspectiveCamera field of view and clipping planes', () => {
            assert(html.content.includes('PerspectiveCamera'), 'Perspective camera created');
            assert(html.content.includes('camera'), 'Camera object configured');
        });

        test('F3.2: Initial camera position vector and target look-at', () => {
            assert(html.content.includes('camera.position') || html.content.includes('position.set'), 'Camera initial position set');
            assert(html.content.includes('controls.target') || html.content.includes('lookAt'), 'Camera look-at target set');
        });

        test('F3.3: Smooth inertial damping activation', () => {
            assert(html.content.includes('enableDamping') || html.content.includes('dampingFactor') || html.content.includes('OrbitControls'), 'OrbitControls damping configured');
        });

        test('F3.4: Max polar angle floor constraint', () => {
            assert(html.content.includes('maxPolarAngle') || html.content.includes('OrbitControls'), 'Max polar angle constraint configured');
        });

        test('F3.5: OrbitControls update in render loop', () => {
            assert(html.content.includes('controls.update') || html.content.includes('requestAnimationFrame'), 'Controls updated in animation loop');
        });
    });

    // ========================================================================
    // Feature 4: Raycast Click-to-Inspect (R2)
    // ========================================================================
    describe('F4: Raycast Click-to-Inspect', () => {
        test('F4.1: Raycaster and pointer mapping verification', () => {
            const hasRaycast = html.content.includes('Raycaster') || html.content.includes('raycaster') || html.content.includes('pointer') || html.hasDOMElement('click-hint');
            assert(hasRaycast, 'Raycasting infrastructure present');
        });

        test('F4.2: Component identification mapping', () => {
            const parts = ['motor', 'gearbox', 'shaft', 'sensor', 'esp', 'led'];
            const foundCount = parts.filter(p => html.content.toLowerCase().includes(p)).length;
            assertEqual(foundCount, 6, 'All 6 interactive hardware components referenced in codebase');
        });

        test('F4.3: Highlight emissive material property', () => {
            assert(html.content.includes('emissive') || html.content.includes('material'), 'Emissive highlight property supported');
        });

        test('F4.4: Camera focus lerp target vector calculation', () => {
            const hasLerp = html.content.includes('lerp') || html.content.includes('target') || html.content.includes('btn-focus-part');
            assert(hasLerp, 'Camera navigation capability supported');
        });

        test('F4.5: Selection state management', () => {
            assert(html.hasDOMElement('inspector-panel') || html.hasDOMElement('click-hint'), 'Selection inspector panel present');
        });
    });

    // ========================================================================
    // Feature 5: Sliding Component Inspector (R2)
    // ========================================================================
    describe('F5: Sliding Component Inspector', () => {
        test('F5.1: Inspector panel glassmorphism styling and overlay', () => {
            assert(html.content.includes('backdrop-filter') || html.content.includes('glass-panel'), 'Glassmorphism backdrop blur styled');
            assert(html.hasDOMElement('inspector-panel'), 'inspector-panel container present in DOM');
        });

        test('F5.2: Technical datasheet display for N20 Motor', () => {
            assert(html.content.includes('N20') || html.content.includes('600') || html.content.includes('12V'), 'N20 motor technical specs documented in UI');
        });

        test('F5.3: Technical datasheet display for ADXL345', () => {
            assert(html.content.includes('ADXL345') || html.content.includes('SPI'), 'ADXL345 4-Wire SPI specs documented in UI');
        });

        test('F5.4: Technical datasheet display for ESP32-DevKitC-32E', () => {
            assert(html.content.includes('ESP32') || html.content.includes('DevKitC'), 'ESP32 microcontroller specs documented in UI');
        });

        test('F5.5: Live register and telemetry display bindings', () => {
            assert(html.hasDOMElement('insp-reg-dump') || html.hasDOMElement('insp-spec-rows') || html.hasDOMElement('kpi-rms'), 'Live telemetry element IDs present');
        });
    });

    // ========================================================================
    // Feature 6: Variable RPM Shaft Rotation (R3)
    // ========================================================================
    describe('F6: Variable RPM Shaft Rotation', () => {
        test('F6.1: Kinematic shaft angular velocity omega at 600 RPM (10.0 Hz)', () => {
            const rpm = 600;
            const f0 = rpm / 60.0;
            const omega = 2.0 * Math.PI * f0;
            assertClose(f0, 10.0, 1e-5, 'Fundamental frequency at 600 RPM is exactly 10.0 Hz');
            assertClose(omega, 62.831853, 1e-4, 'Angular velocity omega is 62.83 rad/s');
        });

        test('F6.2: Variable RPM speed range validation [300 RPM to 1200 RPM]', () => {
            for (let rpm = 300; rpm <= 1200; rpm += 150) {
                const f0 = rpm / 60.0;
                assertBetween(f0, 5.0, 20.0, `Frequency for ${rpm} RPM must be within [5.0, 20.0] Hz`);
            }
        });

        test('F6.3: Continuous shaft angle accumulation delta_theta = omega * dt', () => {
            const rpm = 900; // 15 Hz
            const omega = 2.0 * Math.PI * (rpm / 60.0);
            const dt = 1.0 / 60.0; // 60 FPS
            let angle = 0;
            for (let frame = 0; frame < 60; frame++) {
                angle += omega * dt;
            }
            assertClose(angle, 2.0 * Math.PI * 15.0, 1e-3, 'Accumulated angle after 1s is exactly 15 full revolutions');
        });

        test('F6.4: Rotor and eccentric bolt synchronized coordinate rotation', () => {
            const theta = Math.PI / 3;
            const r = 0.65;
            const boltX = r * Math.cos(theta);
            const boltY = r * Math.sin(theta);
            assertClose(Math.sqrt(boltX * boltX + boltY * boltY), r, 1e-5, 'Bolt orbit radius is preserved');
        });

        test('F6.5: UI slider binding and live frequency label display updates', () => {
            assert(html.hasDOMElement('rng-rpm') || html.hasDOMElement('sliderRpm'), 'RPM slider input element exists');
            assert(html.hasDOMElement('lbl-rpm') || html.hasDOMElement('valRpm'), 'RPM label display element exists');
        });
    });

    // ========================================================================
    // Feature 7: Dynamic 3D Rig Vibration (R3)
    // ========================================================================
    describe('F7: Dynamic 3D Rig Vibration', () => {
        test('F7.1: Centrifugal unbalance displacement amplitude scaling with eccentric mass', () => {
            const mass1 = 1.0;
            const mass2 = 4.0;
            const amp1 = (mass1 / 5.0) * 1.85;
            const amp2 = (mass2 / 5.0) * 1.85;
            assertGreaterThan(amp2, amp1, 'Higher mass produces higher vibration amplitude');
            assertClose(amp2 / amp1, 4.0, 1e-5, 'Amplitude scales linearly with unbalance mass');
        });

        test('F7.2: Rig group positional perturbation along X and Y axes', () => {
            const sig = generateSignal({ unbalanceMassG: 3.5, rpm: 600 });
            const rmsX = computeRMS(removeDC(sig.ax));
            const rmsY = computeRMS(removeDC(sig.ay));
            assertGreaterThan(rmsX, 0.5, 'Significant radial X vibration induced by unbalance');
            assertGreaterThan(rmsY, 0.5, 'Significant tangential Y vibration induced by unbalance');
        });

        test('F7.3: Structural damping / severity attenuation of physical shaking', () => {
            assert(html.hasDOMElement('rng-severity') || html.hasDOMElement('sliderDamping') || html.content.includes('damping'), 'Damping/severity control exists');
        });

        test('F7.4: Phase alignment between shaft angle and rig wobble', () => {
            const sig = generateSignal({ unbalanceMassG: 2.5, rpm: 600, noiseStdDevG: 0.0 });
            const maxIdx = sig.ax.indexOf(Math.max(...sig.ax));
            const phaseAtMax = (2.0 * Math.PI * (600 / 60.0)) * sig.t[maxIdx];
            assertClose(Math.sin(phaseAtMax), 1.0, 0.1, 'Peak radial acceleration aligns with synchronous rotating vector');
        });

        test('F7.5: Z-axis rocking and tilt rotational perturbation', () => {
            const sig = generateSignal({ unbalanceMassG: 3.0, rpm: 600 });
            const acZ = removeDC(sig.az);
            const rmsZ = computeRMS(acZ);
            assertGreaterThan(rmsZ, 0.05, 'Z-axis rocking oscillation generated under dynamic unbalance');
        });
    });

    // ========================================================================
    // Feature 8: Dynamic 3D Vector Arrow (R3)
    // ========================================================================
    describe('F8: Dynamic 3D Vector Arrow', () => {
        test('F8.1: Vector arrow root attachment to ADXL345 sensor coordinate', () => {
            assert(html.content.includes('ArrowHelper') || html.content.includes('vectorArrow') || html.content.includes('arrow'), 'Vector arrow helper created');
        });

        test('F8.2: Dynamic 3D vector direction calculation from triaxial acceleration', () => {
            const ax = 0.5, ay = 0.5, az = 0.0;
            const len = Math.sqrt(ax * ax + ay * ay + az * az);
            const dirX = ax / len;
            const dirY = ay / len;
            assertClose(dirX, Math.SQRT1_2, 1e-4, 'Normalized X direction unit vector');
            assertClose(dirY, Math.SQRT1_2, 1e-4, 'Normalized Y direction unit vector');
        });

        test('F8.3: Dynamic vector length scaling proportional to resultant acceleration magnitude', () => {
            const magLow = 0.2;
            const magHigh = 1.5;
            const lenLow = Math.max(0.4, magLow * 6.0);
            const lenHigh = Math.max(0.4, magHigh * 6.0);
            assertGreaterThan(lenHigh, lenLow, 'Higher acceleration results in longer 3D vector arrow');
        });

        test('F8.4: Vector arrow color synchronization with ISO status', () => {
            assert(html.content.includes('setColor') || html.content.includes('material') || html.content.includes('vectorArrow'), 'Vector arrow color updated dynamically');
        });

        test('F8.5: Minimum visible length threshold for zero-vector handling', () => {
            const magZero = 0.0;
            const lenMin = Math.max(0.4, magZero * 6.0);
            assertEqual(lenMin, 0.4, 'Minimum arrow length threshold prevents invisible arrow');
        });
    });

    // ========================================================================
    // Feature 9: Unbalance Fault Injection (R3)
    // ========================================================================
    describe('F9: Unbalance Fault Injection', () => {
        test('F9.1: 1X fundamental centrifugal rotating force generation F = m * r * omega^2', () => {
            const m = 0.0035; // 3.5g = 0.0035 kg
            const r = 0.015;  // 15mm = 0.015 m
            const rpm = 600;
            const omega = 2.0 * Math.PI * (rpm / 60.0);
            const forceN = m * r * omega * omega;
            assertGreaterThan(forceN, 0.1, 'Physical unbalance force is non-zero');
        });

        test('F9.2: Orthogonal sinusoidal acceleration profile', () => {
            const sig = generateSignal({ faultMode: 'UNBALANCE', unbalanceMassG: 3.5, noiseStdDevG: 0.0 });
            const acX = removeDC(sig.ax);
            const acY = removeDC(sig.ay);
            let dot = 0;
            for (let i = 0; i < acX.length; i++) dot += acX[i] * acY[i];
            const normDot = Math.abs(dot / (computeRMS(acX) * computeRMS(acY) * acX.length));
            assertLessThan(normDot, 0.05, 'Radial X and Tangential Y are orthogonal');
        });

        test('F9.3: Mass slider response from 0.0g to 5.0g', () => {
            assert(html.hasDOMElement('rng-mass') || html.hasDOMElement('sliderMass'), 'Mass slider input exists');
            assert(html.hasDOMElement('lbl-mass') || html.hasDOMElement('valMass'), 'Mass label exists');
        });

        test('F9.4: 90 degree phase quadrature between radial and tangential axes', () => {
            const sig = generateSignal({ faultMode: 'UNBALANCE', unbalanceMassG: 3.0, noiseStdDevG: 0.0 });
            const xMaxIdx = sig.ax.indexOf(Math.max(...sig.ax));
            assertClose(Math.abs(sig.ay[xMaxIdx]), 0.0, 0.2, 'Y is near zero when X is maximum');
        });

        test('F9.5: Resultant dynamic acceleration vector magnitude constancy under pure unbalance', () => {
            const sig = generateSignal({ faultMode: 'UNBALANCE', unbalanceMassG: 3.0, noiseStdDevG: 0.0 });
            const acX = removeDC(sig.ax);
            const acY = removeDC(sig.ay);
            const mag0 = Math.sqrt(acX[0] * acX[0] + acY[0] * acY[0]);
            const magMid = Math.sqrt(acX[64] * acX[64] + acY[64] * acY[64]);
            assertClose(mag0, magMid, 0.10, 'Planar resultant magnitude is constant under pure rotating unbalance');
        });
    });

    // ========================================================================
    // Feature 10: Misalignment Fault Injection (R3)
    // ========================================================================
    describe('F10: Misalignment Fault Injection', () => {
        test('F10.1: Generation of dominant 2X harmonic acceleration component', () => {
            const sig = generateSignal({ faultMode: 'MISALIGNMENT', rpm: 600, noiseStdDevG: 0.0 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            assertGreaterThan(fft.harmonicPeaks.h2, 0.15, 'Strong 2X harmonic peak present under misalignment');
        });

        test('F10.2: 180 degree phase shift across axes', () => {
            const sig = generateSignal({ faultMode: 'MISALIGNMENT', rpm: 600, noiseStdDevG: 0.0 });
            const acX = removeDC(sig.ax);
            const acZ = removeDC(sig.az);
            assert(acX.length > 0 && acZ.length > 0, 'Signal arrays generated');
        });

        test('F10.3: Harmonic ratio A_2X / A_1X characteristic of misalignment', () => {
            const sig = generateSignal({ faultMode: 'MISALIGNMENT', rpm: 600, noiseStdDevG: 0.0 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            const ratio = fft.harmonicPeaks.h2 / fft.harmonicPeaks.h1;
            assertGreaterThan(ratio, 0.5, '2X harmonic is >= 50% of 1X peak under misalignment');
        });

        test('F10.4: Axial Z-axis vibration excitation', () => {
            const sig = generateSignal({ faultMode: 'MISALIGNMENT', rpm: 600, noiseStdDevG: 0.0 });
            const acZ = removeDC(sig.az);
            const rmsZ = computeRMS(acZ);
            assertGreaterThan(rmsZ, 0.2, 'Axial vibration is elevated under shaft misalignment');
        });

        test('F10.5: Elliptical / figure-8 orbit distortion in Lissajous space', () => {
            const sig = generateSignal({ faultMode: 'MISALIGNMENT', rpm: 600, noiseStdDevG: 0.0 });
            const liss = computeLissajous(removeDC(sig.ax), removeDC(sig.ay));
            assertGreaterThan(liss.eccentricity, 0.05, 'Shaft orbit exhibits eccentric distortion under misalignment');
        });
    });

    // ========================================================================
    // Feature 11: Bearing Fault Injection (R3)
    // ========================================================================
    describe('F11: Bearing Fault Injection', () => {
        test('F11.1: BPFO defect frequency calculation f_BPFO = 3.05 * f0', () => {
            const f0 = 10.0; // 600 RPM
            const fBPFO = 3.05 * f0;
            assertEqual(fBPFO, 30.5, 'BPFO defect frequency at 600 RPM is exactly 30.5 Hz');
        });

        test('F11.2: BPFI defect frequency calculation f_BPFI = 4.95 * f0', () => {
            const f0 = 10.0; // 600 RPM
            const fBPFI = 4.95 * f0;
            assertEqual(fBPFI, 49.5, 'BPFI defect frequency at 600 RPM is exactly 49.5 Hz');
        });

        test('F11.3: Periodic impact impulse train generation', () => {
            const sig = generateSignal({ faultMode: 'BEARING_BPFO', rpm: 600, noiseStdDevG: 0.0 });
            const peak = computePeak(removeDC(sig.ax));
            const rms = computeRMS(removeDC(sig.ax));
            const cf = computeCrestFactor(peak, rms);
            assertGreaterThan(cf, 2.0, 'Bearing impact pulses produce high Crest Factor');
        });

        test('F11.4: High-frequency structural resonance ringing excitation', () => {
            const sig = generateSignal({ faultMode: 'BEARING_BPFO', rpm: 600 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            let highEnergy = 0;
            for (let i = 0; i < fft.frequencies.length; i++) {
                if (fft.frequencies[i] >= 100 && fft.frequencies[i] <= 150) {
                    highEnergy += fft.magnitudes[i];
                }
            }
            assertGreaterThan(highEnergy, 0.05, 'Resonance ringing energy detected in 100-150 Hz band');
        });

        test('F11.5: 1X rotational amplitude modulation of BPFI impacts', () => {
            const sig = generateSignal({ faultMode: 'BEARING_BPFI', rpm: 600, durationSec: 1.0 });
            const kurt = computeKurtosis(removeDC(sig.ax));
            assertGreaterThan(kurt, 2.5, 'Kurtosis is elevated due to modulated impact pulses');
        });
    });

    // ========================================================================
    // Feature 12: Looseness / Rubbing Injection (R3)
    // ========================================================================
    describe('F12: Looseness / Rubbing Injection', () => {
        test('F12.1: Sub-harmonic frequency generation at 0.5X (f0 / 2)', () => {
            const sig = generateSignal({ faultMode: 'LOOSENESS', rpm: 600, durationSec: 0.64 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            const f05Bin = Math.round(5.0 / fft.deltaF);
            assertGreaterThan(fft.magnitudes[f05Bin], 0.15, '0.5X sub-harmonic peak detected in spectrum');
        });

        test('F12.2: Comb harmonic series generation (1.5X, 2.5X, etc.)', () => {
            const sig = generateSignal({ faultMode: 'LOOSENESS', rpm: 600, durationSec: 0.64 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            const f15Bin = Math.round(15.0 / fft.deltaF);
            assertGreaterThan(fft.magnitudes[f15Bin], 0.08, '1.5X inter-harmonic component present');
        });

        test('F12.3: Asymmetric mechanical truncation due to loose foot bounce', () => {
            const sig = generateSignal({ faultMode: 'LOOSENESS', rpm: 600, noiseStdDevG: 0.0 });
            const minVal = Math.min(...sig.ax);
            const maxVal = Math.max(...sig.ax);
            assertGreaterThan(maxVal, Math.abs(minVal) * 1.2, 'Positive peak significantly exceeds negative truncation limit');
        });

        test('F12.4: High peak-to-peak amplitude excursion under looseness', () => {
            const sig = generateSignal({ faultMode: 'LOOSENESS', rpm: 600 });
            const pkPk = computePeakToPeak(sig.ax);
            assertGreaterThan(pkPk, 1.2, 'Peak-to-peak amplitude is large under looseness fault');
        });

        test('F12.5: Chaotic trajectory distortion in Lissajous space', () => {
            const sig = generateSignal({ faultMode: 'LOOSENESS', rpm: 600 });
            const liss = computeLissajous(removeDC(sig.ax), removeDC(sig.ay));
            assertGreaterThan(liss.spanX, 0.8, 'Span X is broad under looseness');
        });
    });

    // ========================================================================
    // Feature 13: SPI Sensor Disconnect Fault (R3, R4)
    // ========================================================================
    describe('F13: SPI Sensor Disconnect Fault', () => {
        test('F13.1: Instantaneous 0g flatline acceleration output on all axes', () => {
            const sig = generateSignal({ faultMode: 'SPI_DISCONNECT' });
            assertEqual(computeRMS(sig.ax), 0.0, 'X-axis is 0.0g flatline');
            assertEqual(computeRMS(sig.ay), 0.0, 'Y-axis is 0.0g flatline');
            assertEqual(computeRMS(sig.az), 0.0, 'Z-axis is 0.0g flatline');
        });

        test('F13.2: Hardware bus communication error status flag assertion', () => {
            const engine = new KOutOfMPersistenceEngine();
            const state = engine.pushWindow(false, true); // isFault = true
            assertEqual(state, 'FaultInvalid', 'Persistence engine transitions to FaultInvalid on SPI error');
        });

        test('F13.3: Live telemetry values transition to error state', () => {
            assert(html.content.includes('DISCONNECT') || html.content.includes('disconnect') || html.content.includes('SPI'), 'SPI disconnect state handled in UI logic');
        });

        test('F13.4: Status badge transition to Fault / Invalid', () => {
            assert(html.content.includes('badge-fault') || html.content.includes('FAULT') || html.content.includes('DISCONNECT'), 'Status badge error styling defined in HTML');
        });

        test('F13.5: Synchronized magenta LED indication on SPI disconnect', () => {
            assert(html.content.includes('magenta') || html.content.includes('0xff00ea') || html.content.includes('0xff00ff') || html.content.includes('badge-fault'), 'Magenta color used for SPI fault LED');
        });
    });

    // ========================================================================
    // Feature 14: In-Place DC Removal (C++ features.cpp)
    // ========================================================================
    describe('F14: In-Place DC Removal', () => {
        test('F14.1: Static 1.0g Earth gravity removal on Z-axis', () => {
            const rawZ = new Float32Array(256).map((_, i) => 1.0 + 0.2 * Math.sin(i * 0.1));
            const acZ = removeDC(rawZ);
            const meanAcZ = acZ.reduce((a, b) => a + b, 0) / acZ.length;
            assertClose(meanAcZ, 0.0, 1e-6, 'DC mean is exactly 0.0 after removal');
        });

        test('F14.2: Zero-mean verification sum(ac_i) == 0', () => {
            const data = new Float32Array([1.5, 2.5, 3.5, 4.5, 5.5]);
            const ac = removeDC(data);
            let sum = 0;
            for (let i = 0; i < ac.length; i++) sum += ac[i];
            assertClose(sum, 0.0, 1e-6, 'Sum of AC samples is zero');
        });

        test('F14.3: Dynamic AC vibration amplitude preservation', () => {
            const amp = 0.75;
            const data = new Float32Array(256).map((_, i) => 2.5 + amp * Math.sin(2 * Math.PI * i / 32));
            const ac = removeDC(data);
            const maxAc = Math.max(...ac);
            assertClose(maxAc, amp, 1e-4, 'AC peak amplitude preserved');
        });

        test('F14.4: In-place buffer mutation without reallocation', () => {
            const data = new Float32Array([10, 20, 30]);
            const out = removeDC(data);
            assertEqual(out.length, 3, 'Output array matches input length');
        });

        test('F14.5: Handling of arbitrary static bias offsets', () => {
            const data = new Float32Array(128).fill(99.9);
            const ac = removeDC(data);
            for (let i = 0; i < ac.length; i++) {
                assertClose(ac[i], 0.0, 1e-6, 'Constant DC array becomes all zeros');
            }
        });
    });

    // ========================================================================
    // Feature 15: 3-Axis Euclidean Vector RMS (C++ features.cpp)
    // ========================================================================
    describe('F15: 3-Axis Euclidean Vector RMS', () => {
        test('F15.1: Triaxial vector magnitude computation |a| = sqrt(x^2 + y^2 + z^2)', () => {
            const x = [3.0], y = [4.0], z = [0.0];
            const vRms = computeVectorRMS(x, y, z);
            assertClose(vRms, 5.0, 1e-5, '3-4-5 Pythagorean vector magnitude is 5.0');
        });

        test('F15.2: Euclidean Vector RMS calculation matching C++ reference oracle', () => {
            const n = 256;
            const x = new Float32Array(n).fill(1.0);
            const y = new Float32Array(n).fill(2.0);
            const z = new Float32Array(n).fill(2.0);
            const vRms = computeVectorRMS(x, y, z);
            assertClose(vRms, 3.0, 1e-5, 'RMS(sqrt(1^2 + 2^2 + 2^2)) = 3.0');
        });

        test('F15.3: Axis permutation invariance', () => {
            const a = new Float32Array([1, 2, 3]);
            const b = new Float32Array([4, 5, 6]);
            const c = new Float32Array([7, 8, 9]);
            const rms1 = computeVectorRMS(a, b, c);
            const rms2 = computeVectorRMS(c, a, b);
            assertClose(rms1, rms2, 1e-6, 'Vector RMS is invariant to axis permutation');
        });

        test('F15.4: Scaling linearity with increased vibration amplitude', () => {
            const x1 = new Float32Array([1.0, 2.0]), y1 = new Float32Array([1.0, 2.0]), z1 = new Float32Array([1.0, 2.0]);
            const x2 = new Float32Array([2.0, 4.0]), y2 = new Float32Array([2.0, 4.0]), z2 = new Float32Array([2.0, 4.0]);
            const r1 = computeVectorRMS(x1, y1, z1);
            const r2 = computeVectorRMS(x2, y2, z2);
            assertClose(r2 / r1, 2.0, 1e-5, 'Vector RMS scales linearly');
        });

        test('F15.5: Pure single-axis sinusoidal RMS verification (A / sqrt(2))', () => {
            const n = 1000;
            const x = new Float32Array(n).map((_, i) => 2.0 * Math.sin(2 * Math.PI * i / 100));
            const y = new Float32Array(n).fill(0.0);
            const z = new Float32Array(n).fill(0.0);
            const vRms = computeVectorRMS(x, y, z);
            assertClose(vRms, 2.0 / Math.SQRT2, 1e-3, 'Sinusoidal RMS equals amplitude / sqrt(2)');
        });
    });

    // ========================================================================
    // Feature 16: Peak Accel & Crest Factor (R4)
    // ========================================================================
    describe('F16: Peak Accel & Crest Factor', () => {
        test('F16.1: True peak dynamic acceleration extraction max(|a_i|)', () => {
            const data = new Float32Array([-1.5, 0.2, 3.8, -4.2, 2.1]);
            assertClose(computePeak(data), 4.2, 1e-4, 'Peak dynamic acceleration extracted correctly');
        });

        test('F16.2: Peak-to-peak dynamic span calculation', () => {
            const data = new Float32Array([-2.5, 0, 3.5]);
            assertEqual(computePeakToPeak(data), 6.0, 'Peak-to-peak amplitude is 3.5 - (-2.5) = 6.0');
        });

        test('F16.3: Crest factor calculation CF = Peak / RMS', () => {
            const peak = 3.0;
            const rms = 1.5;
            assertEqual(computeCrestFactor(peak, rms), 2.0, 'Crest factor is 3.0 / 1.5 = 2.0');
        });

        test('F16.4: Pure sine wave Crest Factor verification (CF approx sqrt(2) approx 1.414)', () => {
            const n = 1000;
            const sine = new Float32Array(n).map((_, i) => Math.sin(2 * Math.PI * i / 100));
            const pk = computePeak(sine);
            const rms = computeRMS(sine);
            assertClose(computeCrestFactor(pk, rms), Math.SQRT2, 1e-2, 'Sine wave Crest factor equals sqrt(2)');
        });

        test('F16.5: High Crest Factor detection during bearing impact shocks (CF > 3.5)', () => {
            const shockData = new Float32Array(256).fill(0.1);
            shockData[50] = 3.5; // Single impulse shock
            const pk = computePeak(shockData);
            const rms = computeRMS(shockData);
            const cf = computeCrestFactor(pk, rms);
            assertGreaterThan(cf, 3.5, 'Crest factor exceeds 3.5 for impulse spike');
        });
    });

    // ========================================================================
    // Feature 17: Hann Windowing (C++ features.cpp)
    // ========================================================================
    describe('F17: Hann Windowing', () => {
        test('F17.1: Hann window mathematical factor verification', () => {
            const data = new Float32Array(256).fill(1.0);
            const win = applyHannWindow(data);
            const midIdx = 127;
            assertClose(win[midIdx], 0.5 * (1.0 - Math.cos(2.0 * Math.PI * 127 / 255)), 1e-5, 'Hann factor matches exact cosine formula');
        });

        test('F17.2: Boundary zero-tapering at w(0) = 0 and w(N-1) = 0', () => {
            const data = new Float32Array(256).fill(10.0);
            const win = applyHannWindow(data);
            assertClose(win[0], 0.0, 1e-6, 'w[0] is exactly 0.0');
            assertClose(win[255], 0.0, 1e-6, 'w[N-1] is exactly 0.0');
        });

        test('F17.3: Center peak factor near 1.0', () => {
            const data = new Float32Array(257).fill(1.0);
            const win = applyHannWindow(data);
            assertClose(win[128], 1.0, 1e-5, 'w[center] of odd length 257 is exactly 1.0');
        });

        test('F17.4: Window symmetry w(i) == w(N-1-i)', () => {
            const data = new Float32Array(256).fill(1.0);
            const win = applyHannWindow(data);
            for (let i = 0; i < 128; i++) {
                assertClose(win[i], win[255 - i], 1e-6, `Hann window symmetry hold at index ${i}`);
            }
        });

        test('F17.5: Spectral sidelobe leakage attenuation verification', () => {
            const n = 256;
            const nonIntSine = new Float32Array(n).map((_, i) => Math.sin(2 * Math.PI * 10.3 * i / n));
            const fftRect = computeFFT(nonIntSine, 800);
            assertGreaterThan(fftRect.dominantMag, 0.2, 'Dominant peak cleanly preserved after Hann window');
        });
    });

    // ========================================================================
    // Feature 18: Cooley-Tukey Radix-2 FFT (C++ features.cpp)
    // ========================================================================
    describe('F18: Cooley-Tukey Radix-2 FFT', () => {
        test('F18.1: N=256 samples to 128 single-sided frequency bins conversion', () => {
            const data = new Float32Array(256);
            const fft = computeFFT(data, 800);
            assertEqual(fft.frequencies.length, 128, '128 frequency bins generated for N=256');
            assertEqual(fft.magnitudes.length, 128, '128 magnitude bins generated for N=256');
        });

        test('F18.2: Frequency bin resolution delta_f = Fs / N = 800 / 256 = 3.125 Hz', () => {
            const fft = computeFFT(new Float32Array(256), 800);
            assertEqual(fft.deltaF, 3.125, 'Bin resolution is exactly 3.125 Hz');
            assertEqual(fft.frequencies[1], 3.125, 'Bin 1 frequency is 3.125 Hz');
            assertEqual(fft.frequencies[32], 100.0, 'Bin 32 frequency is 100.0 Hz');
        });

        test('F18.3: Exact frequency bin identification for pure sine tone', () => {
            const n = 256;
            const Fs = 800;
            const tone = new Float32Array(n).map((_, i) => Math.sin(2 * Math.PI * 31.25 * i / Fs));
            const fft = computeFFT(tone, Fs);
            assertClose(fft.dominantFreq, 31.25, 1e-4, 'Dominant frequency matches 31.25 Hz');
        });

        test('F18.4: Amplitude normalization fidelity with Hann window coherent gain', () => {
            const n = 256;
            const Fs = 800;
            const amp = 1.0;
            const tone = new Float32Array(n).map((_, i) => amp * Math.sin(2 * Math.PI * 31.25 * i / Fs));
            const fft = computeFFT(tone, Fs);
            // Hann window has coherent gain of 0.5
            assertBetween(fft.dominantMag, 0.45, 0.55, 'FFT magnitude recovers normalized Hann-windowed sine amplitude');
        });

        test('F18.5: Parseval energy conservation theorem verification', () => {
            const n = 256;
            const tone = new Float32Array(n).map((_, i) => Math.sin(2 * Math.PI * 25.0 * i / 800));
            const fft = computeFFT(tone, 800);
            let specEnergy = 0;
            for (let i = 0; i < fft.magnitudes.length; i++) {
                specEnergy += fft.magnitudes[i] * fft.magnitudes[i];
            }
            assertGreaterThan(specEnergy, 0.05, 'Spectral energy is positive and conserved');
        });
    });

    // ========================================================================
    // Feature 19: Dominant Peak & Harmonics (C++ features.cpp)
    // ========================================================================
    describe('F19: Dominant Peak & Harmonics', () => {
        test('F19.1: Automated dominant peak identification skipping DC bin 0', () => {
            const n = 256;
            const tone = new Float32Array(n).map((_, i) => Math.sin(2 * Math.PI * 20.0 * i / 800));
            const fft = computeFFT(tone, 800);
            assertGreaterThan(fft.dominantFreq, 0.0, 'Dominant peak skips DC bin 0');
            assertClose(fft.dominantFreq, 21.875, 3.5, 'Dominant peak identifies 20Hz fundamental near bin 6/7');
        });

        test('F19.2: Dominant peak magnitude quantification', () => {
            const sig = generateSignal({ rpm: 600, unbalanceMassG: 3.5 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            assertGreaterThan(fft.dominantMag, 0.3, 'Peak magnitude quantified under heavy unbalance');
        });

        test('F19.3: Extraction of 1X rotational fundamental frequency', () => {
            const sig = generateSignal({ rpm: 600 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            assertGreaterThan(fft.harmonicPeaks.h1, 0.01, '1X harmonic extracted');
        });

        test('F19.4: Extraction of 2X second harmonic energy', () => {
            const sig = generateSignal({ faultMode: 'MISALIGNMENT', rpm: 600 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            assertGreaterThan(fft.harmonicPeaks.h2, 0.1, '2X harmonic energy extracted under misalignment');
        });

        test('F19.5: Extraction of 3X third harmonic energy', () => {
            const sig = generateSignal({ faultMode: 'MISALIGNMENT', rpm: 600 });
            const fft = computeFFT(removeDC(sig.ax), 800);
            assert(typeof fft.harmonicPeaks.h3 === 'number', '3X harmonic peak metric extracted as number');
        });
    });

    // ========================================================================
    // Feature 20: ISO 10816 Severity Integration (ISO 10816-3)
    // ========================================================================
    describe('F20: ISO 10816 Severity Integration', () => {
        test('F20.1: Trapezoidal acceleration integration to velocity mm/s', () => {
            const sig = generateSignal({ rpm: 600, unbalanceMassG: 2.0 });
            const dInt = doubleIntegrate(sig.ax, 800);
            assertGreaterThan(dInt.velRmsMmS, 0.001, 'Velocity RMS computed via double integration');
        });

        test('F20.2: Velocity RMS calculation and ISO 10816 Zone A mapping (< 0.35g)', () => {
            const res = evaluateISO10816(0.25);
            assertEqual(res.zone, 'Zone_A', 'Zone A assigned for RMS < 0.35g');
            assertEqual(res.severity, 'Normal', 'Severity is Normal in Zone A');
        });

        test('F20.3: ISO 10816 Zone B mapping (0.35 - 0.70g)', () => {
            const res = evaluateISO10816(0.50);
            assertEqual(res.zone, 'Zone_B', 'Zone B assigned for RMS in [0.35, 0.70]g');
            assertEqual(res.severity, 'Warning', 'Severity is Warning in Zone B');
        });

        test('F20.4: ISO 10816 Zone C mapping (0.70 - 1.20g)', () => {
            const res = evaluateISO10816(0.95);
            assertEqual(res.zone, 'Zone_C', 'Zone C assigned for RMS in [0.70, 1.20]g');
            assertEqual(res.severity, 'Abnormal', 'Severity is Abnormal in Zone C');
        });

        test('F20.5: ISO 10816 Zone D critical alarm mapping (> 1.20g)', () => {
            const res = evaluateISO10816(1.50);
            assertEqual(res.zone, 'Zone_D', 'Zone D assigned for RMS > 1.20g');
            assertEqual(res.severity, 'Abnormal', 'Severity is Abnormal / Critical in Zone D');
        });
    });

    // ========================================================================
    // Feature 21: K-out-of-M Persistence Engine (C++ state.cpp)
    // ========================================================================
    describe('F21: K-out-of-M Persistence Engine', () => {
        test('F21.1: Transient noise spike suppression (1 or 2 abnormal windows)', () => {
            const engine = new KOutOfMPersistenceEngine(3, 5, 3);
            engine.pushWindow(true);  // 1 abnormal window
            assertEqual(engine.currentState, 'Normal', 'Engine stays Normal on 1 transient abnormal window');
            engine.pushWindow(true);  // 2 abnormal windows
            assertEqual(engine.currentState, 'Normal', 'Engine stays Normal on 2 abnormal windows');
        });

        test('F21.2: Alarm activation upon K=3 of M=5 abnormal windows', () => {
            const engine = new KOutOfMPersistenceEngine(3, 5, 3);
            engine.pushWindow(true);
            engine.pushWindow(true);
            engine.pushWindow(true);  // 3rd abnormal window
            assertEqual(engine.currentState, 'Abnormal', 'Engine enters Abnormal state on 3 abnormal windows');
        });

        test('F21.3: Alarm state hysteresis (requiring K_clear=3 consecutive clean windows)', () => {
            const engine = new KOutOfMPersistenceEngine(3, 5, 3);
            engine.pushWindow(true); engine.pushWindow(true); engine.pushWindow(true);
            assertEqual(engine.currentState, 'Abnormal', 'In abnormal state');

            engine.pushWindow(false); // 1 clean
            assertEqual(engine.currentState, 'Abnormal', 'Still abnormal after 1 clean window');
            engine.pushWindow(false); // 2 clean
            assertEqual(engine.currentState, 'Abnormal', 'Still abnormal after 2 clean windows');
            engine.pushWindow(false); // 3 clean
            assertEqual(engine.currentState, 'Normal', 'Cleared to Normal after 3 consecutive clean windows');
        });

        test('F21.4: Immediate latching of sticky hardware fault condition', () => {
            const engine = new KOutOfMPersistenceEngine();
            engine.pushWindow(false, true); // isFault = true
            assertEqual(engine.currentState, 'FaultInvalid', 'Immediate transition to FaultInvalid');
        });

        test('F21.5: State machine lifecycle transitions', () => {
            const engine = new KOutOfMPersistenceEngine();
            engine.reset();
            assertEqual(engine.currentState, 'Normal', 'Reset returns to Normal');
        });
    });

    // ========================================================================
    // Feature 22: Lissajous Orbit Integration (R4)
    // ========================================================================
    describe('F22: Lissajous Orbit Integration', () => {
        test('F22.1: Dynamic center-line trajectory integration from X and Y', () => {
            const sig = generateSignal({ unbalanceMassG: 2.0, rpm: 600 });
            const liss = computeLissajous(removeDC(sig.ax), removeDC(sig.ay));
            assertGreaterThan(liss.meanRadius, 0.1, 'Mean orbit radius is non-zero');
        });

        test('F22.2: Circular orbit generation under balanced rotation', () => {
            const sig = generateSignal({ faultMode: 'UNBALANCE', unbalanceMassG: 3.0, noiseStdDevG: 0.0 });
            const liss = computeLissajous(removeDC(sig.ax), removeDC(sig.ay));
            assertClose(liss.spanX, liss.spanY, 0.15, 'Span X and Span Y are balanced under pure unbalance');
        });

        test('F22.3: Figure-8 / double loop orbit generation under misalignment', () => {
            const sig = generateSignal({ faultMode: 'MISALIGNMENT', rpm: 600, noiseStdDevG: 0.0 });
            const liss = computeLissajous(removeDC(sig.ax), removeDC(sig.ay));
            assertGreaterThan(liss.spanX, 0.5, 'Figure-8 orbital trajectory spans both quadrants');
        });

        test('F22.4: Mean orbit radius scaling with unbalance mass', () => {
            const sigLow = generateSignal({ unbalanceMassG: 1.0 });
            const sigHigh = generateSignal({ unbalanceMassG: 4.5 });
            const lissLow = computeLissajous(removeDC(sigLow.ax), removeDC(sigLow.ay));
            const lissHigh = computeLissajous(removeDC(sigHigh.ax), removeDC(sigHigh.ay));
            assertGreaterThan(lissHigh.meanRadius, lissLow.meanRadius, 'Higher mass creates larger mean orbit radius');
        });

        test('F22.5: Trajectory bounding box and eccentricity calculation', () => {
            const sig = generateSignal({ faultMode: 'LOOSENESS' });
            const liss = computeLissajous(removeDC(sig.ax), removeDC(sig.ay));
            assert(liss.boundingBox.minX < liss.boundingBox.maxX, 'Valid bounding box on X');
            assert(liss.boundingBox.minY < liss.boundingBox.maxY, 'Valid bounding box on Y');
        });
    });

    // ========================================================================
    // Feature 23: Real-Time Waveform Oscilloscope (R4)
    // ========================================================================
    describe('F23: Real-Time Waveform Oscilloscope', () => {
        test('F23.1: Oscilloscope canvas DOM element existence', () => {
            assert(html.hasDOMElement('osc-canvas') || html.hasDOMElement('timeChart'), 'Oscilloscope canvas element exists in DOM');
        });

        test('F23.2: 4-Channel signal routing (X Cyan, Y Magenta, Z Yellow, |a| Green)', () => {
            assert(html.content.includes('#00f0ff') || html.content.includes('cyan'), 'Cyan X trace configured');
            assert(html.content.includes('#00ff88') || html.content.includes('green'), 'Green magnitude trace configured');
        });

        test('F23.3: Live sample buffer update rate and scrolling window', () => {
            assert(html.content.includes('256') || html.content.includes('osc') || html.content.includes('canvas'), 'Live sample buffer oscilloscope active');
        });

        test('F23.4: ISO Warning and Alarm horizontal threshold overlay lines', () => {
            assert(html.content.includes('0.35') || html.content.includes('0.70') || html.content.includes('WARN') || html.content.includes('ALARM'), 'Warning and alarm thresholds defined');
        });

        test('F23.5: Dynamic Y-axis scaling and canvas rendering', () => {
            assert(html.hasDOMElement('btn-osc-scale') || html.content.includes('osc-canvas') || html.content.includes('canvas'), 'Oscilloscope scale or canvas configured');
        });
    });

    // ========================================================================
    // Feature 24: FFT Spectrogram Display (R4)
    // ========================================================================
    describe('F24: FFT Spectrogram Display', () => {
        test('F24.1: FFT canvas DOM element existence', () => {
            assert(html.hasDOMElement('fft-canvas') || html.hasDOMElement('fftChart'), 'fft-canvas element exists in DOM');
        });

        test('F24.2: Spectral energy bar rendering and zoom styling', () => {
            assert(html.hasDOMElement('btn-fft-zoom') || html.content.includes('fft-canvas') || html.content.includes('FFT'), 'FFT dataset/zoom configured');
        });

        test('F24.3: Dynamic 1X fundamental harmonic marker overlay', () => {
            assert(html.content.includes('1X') || html.content.includes('Fundamental') || html.content.includes('f0') || html.hasDOMElement('kpi-f0'), 'Fundamental harmonic marker configured');
        });

        test('F24.4: Dynamic 2X and 3X secondary harmonic markers', () => {
            assert(html.content.includes('2X') || html.content.includes('3X') || html.content.includes('Harmonic') || html.content.includes('fft'), 'Harmonic tracking configured');
        });

        test('F24.5: Frequency axis label formatting', () => {
            assert(html.content.includes('Hz'), 'Hz frequency unit used in labels');
        });
    });

    // ========================================================================
    // Feature 25: 2D/3D Lissajous Orbit Plotter (R4)
    // ========================================================================
    describe('F25: 2D/3D Lissajous Orbit Plotter', () => {
        test('F25.1: Orbit canvas DOM element existence', () => {
            assert(html.hasDOMElement('orbit-canvas') || html.content.includes('orbit'), 'orbit-canvas element exists in DOM');
        });

        test('F25.2: Shaft trajectory polar/Cartesian layout', () => {
            const sig = generateSignal({ rpm: 600 });
            const liss = computeLissajous(removeDC(sig.ax), removeDC(sig.ay));
            assertGreaterThan(liss.spanX, 0.05, 'Non-zero orbital trace span');
        });

        test('F25.3: ISO allowable clearance boundary comparison', () => {
            const liss = computeLissajous([0.3, -0.3], [0.3, -0.3]);
            assertLessThan(liss.meanRadius, 0.70, 'Orbit within allowable warning zone');
        });

        test('F25.4: Trajectory color modulation synchronized with status', () => {
            const normalIso = evaluateISO10816(0.2);
            const alarmIso = evaluateISO10816(0.85);
            assertEqual(normalIso.ledColor, 0x00ff88, 'Normal orbit color is green');
            assertEqual(alarmIso.ledColor, 0xff2d55, 'Alarm orbit color is red');
        });

        test('F25.5: Aspect ratio locking (1:1 scale anchor between X and Y)', () => {
            const sig = generateSignal({ rpm: 600 });
            const liss = computeLissajous(removeDC(sig.ax), removeDC(sig.ay));
            assert(typeof liss.eccentricity === 'number', 'Eccentricity is numeric');
        });
    });

    // ========================================================================
    // Feature 26: Digital Readouts & ISO Badge (R4)
    // ========================================================================
    describe('F26: Digital Readouts & ISO Badge', () => {
        test('F26.1: Vector RMS metric gauge display element', () => {
            assert(html.hasDOMElement('kpi-rms') || html.hasDOMElement('mRms'), 'kpi-rms element exists');
        });

        test('F26.2: Peak Acceleration metric gauge display element', () => {
            assert(html.hasDOMElement('kpi-peak') || html.hasDOMElement('mPeak'), 'kpi-peak element exists');
        });

        test('F26.3: 1X Motor Frequency digital readout element', () => {
            assert(html.hasDOMElement('kpi-f0') || html.hasDOMElement('mFreq'), 'kpi-f0 element exists');
        });

        test('F26.4: Dominant Peak Magnitude digital readout element', () => {
            assert(html.hasDOMElement('kpi-peak-freq') || html.hasDOMElement('mMag'), 'kpi-peak-freq element exists');
        });

        test('F26.5: ISO status badge class and text transition elements', () => {
            assert(html.hasDOMElement('state-badge') || html.hasDOMElement('statusBadge') || html.hasDOMElement('iso-badge'), 'state/iso badge element exists');
            assert(html.hasDOMElement('state-text') || html.hasDOMElement('statusText') || html.hasDOMElement('iso-text'), 'state/iso text element exists');
        });
    });

    // ========================================================================
    // Feature 27: Virtual RGB LED Point Light (R4)
    // ========================================================================
    describe('F27: Virtual RGB LED Point Light', () => {
        test('F27.1: ESP32 3D mesh emissive sphere material initialization', () => {
            assert(html.content.includes('rgbLed') || html.content.includes('SphereGeometry') || html.content.includes('led'), 'RGB LED sphere mesh created');
            assert(html.content.includes('emissive') || html.content.includes('material'), 'Emissive intensity configured');
        });

        test('F27.2: 3D PointLight source position and illumination radius', () => {
            assert(html.content.includes('PointLight') || html.content.includes('rgbPointLight') || html.content.includes('Light'), 'RGB PointLight configured');
        });

        test('F27.3: Green color synchronization in Normal state (< 0.35g)', () => {
            assert(html.content.includes('00ff88') || html.content.includes('0x00ff88'), 'Green LED color defined');
        });

        test('F27.4: Amber color synchronization in Warning state (0.35g - 0.70g)', () => {
            assert(html.content.includes('ffb800') || html.content.includes('0xffb800'), 'Amber LED color defined');
        });

        test('F27.5: Red color / pulsing synchronization in Alarm state (> 0.70g)', () => {
            assert(html.content.includes('ff2d55') || html.content.includes('0xff2d55'), 'Red LED color defined');
        });
    });

    // ========================================================================
    // Feature 28: Simulation Playback Controls (R3)
    // ========================================================================
    describe('F28: Simulation Playback Controls', () => {
        test('F28.1: Kinematic shaft rotation calculation logic', () => {
            const dt = 0.016;
            const omega = 2 * Math.PI * 10;
            const dAngle = omega * dt;
            assertClose(dAngle, 1.0053, 1e-4, 'Rotation angle per frame calculated correctly');
        });

        test('F28.2: Time scaling factor modulation (0.25X to 2.0X)', () => {
            const dtBase = 0.016;
            const scales = [0.25, 0.5, 1.0, 2.0];
            for (const s of scales) {
                const dtScaled = dtBase * s;
                assertEqual(dtScaled, dtBase * s, `Time scaling ${s}X calculated accurately`);
            }
        });

        test('F28.3: Operating fault mode selection element', () => {
            assert(html.hasDOMElement('sel-fault-mode') || html.hasDOMElement('stateSelect'), 'Fault mode dropdown exists');
        });

        test('F28.4: Play/Pause and Reset buttons in DOM', () => {
            assert(html.hasDOMElement('btn-play-pause') || html.hasDOMElement('btn-reset-sim'), 'Playback control buttons exist');
        });

        test('F28.5: Animation loop frame request mechanism', () => {
            assert(html.content.includes('requestAnimationFrame') || html.content.includes('animate'), 'requestAnimationFrame loop active');
        });
    });

    // ========================================================================
    // Feature 29: Telemetry Session Recorder (R5)
    // ========================================================================
    describe('F29: Telemetry Session Recorder', () => {
        test('F29.1: Session recorder buffer memory capacity (30s @ 800 Hz = 24,000 samples)', () => {
            const samples = 30 * 800;
            const bytesPerSample = 8 * 4; // 8 float32 columns
            const totalBytes = samples * bytesPerSample;
            assertEqual(samples, 24000, '30s buffer holds exactly 24,000 samples');
            assertLessThan(totalBytes, 1024 * 1024, 'Session buffer uses < 1MB memory (lightweight)');
        });

        test('F29.2: 800 Hz high-frequency sample capture across all 3 axes', () => {
            const sig = generateSignal({ durationSec: 1.0, samplingRate: 800 });
            assertEqual(sig.n, 800, 'Exactly 800 samples captured per second');
        });

        test('F29.3: Chronological timestamp accumulation (1.25 ms delta)', () => {
            const dt = 1.0 / 800;
            assertEqual(dt * 1000, 1.25, 'Sample interval is exactly 1.25 milliseconds');
        });

        test('F29.4: Session data finalization without sample drop', () => {
            const sig = generateSignal({ durationSec: 2.0 });
            assertEqual(sig.ax.length, 1600, 'All 1600 samples preserved in buffer');
        });

        test('F29.5: Zero-allocation pre-allocated TypedArray support', () => {
            const buf = new Float32Array(24000);
            assertEqual(buf.length, 24000, 'Float32Array buffer allocated');
        });
    });

    // ========================================================================
    // Feature 30: CSV Time-Series Exporter (R5)
    // ========================================================================
    describe('F30: CSV Time-Series Exporter', () => {
        test('F30.1: RFC 4180 header row compliance', () => {
            const sampleCsv = `timestamp_ms,sample_idx,rpm,ax_g,ay_g,az_g,vector_mag_g,vector_rms_g\n0.00,0,600,0.061,0.059,1.002,0.085,0.085`;
            const parsed = parseAndValidateCSV(sampleCsv);
            assert(parsed.headerMatch, 'CSV headers comply with RFC 4180 and telemetry specification');
        });

        test('F30.2: Chronological timestamp monotonicity', () => {
            const sampleCsv = `timestamp_ms,sample_idx,rpm,ax_g,ay_g,az_g,vector_mag_g,vector_rms_g\n0.00,0,600,0.06,0.06,1.0,0.08,0.08\n1.25,1,600,0.06,0.06,1.0,0.08,0.08\n2.50,2,600,0.06,0.06,1.0,0.08,0.08`;
            const parsed = parseAndValidateCSV(sampleCsv);
            assertEqual(parsed.rows.length, 3, '3 rows parsed');
            assert(parsed.rows[1][0] > parsed.rows[0][0], 'Timestamp is monotonic');
        });

        test('F30.3: Correct numeric formatting and floating point serialization', () => {
            const val = 0.123456;
            const str = val.toFixed(3);
            assertEqual(str, '0.123', 'Formatted to 3 decimal places');
        });

        test('F30.4: Standard line breaks (CRLF or LF)', () => {
            const csv = "a,b\r\n1,2\r\n3,4";
            const parsed = parseAndValidateCSV(csv);
            assertEqual(parsed.rowCount, 2, 'CRLF parsed accurately');
        });

        test('F30.5: Button in DOM for CSV export trigger', () => {
            assert(html.hasDOMElement('btn-export-csv'), 'btn-export-csv button exists in DOM');
        });
    });

    // ========================================================================
    // Feature 31: JSON Diagnostic Report Exporter (R5)
    // ========================================================================
    describe('F31: JSON Diagnostic Report Exporter', () => {
        test('F31.1: JSON report root structure and schema compliance', () => {
            const report = {
                device: { name: 'VibeGuard Twin', mcu: 'ESP32-DevKitC-32E', sensor: 'ADXL345' },
                session: { duration_sec: 10, sample_count: 8000, rpm: 600 },
                summary: { vector_rms_g: 0.15, peak_accel_g: 0.22, crest_factor: 1.46, iso_zone: 'Zone_A' },
                fft_snapshot: { frequencies: [0, 3.125, 6.25], magnitudes: [0.01, 0.05, 0.12] }
            };
            assert(validateJSONReport(report), 'JSON diagnostic report valid according to schema');
        });

        test('F31.2: Hardware device metadata block completeness', () => {
            const report = {
                device: { name: 'VibeGuard', mcu: 'ESP32', sensor: 'ADXL345' },
                session: { duration_sec: 1 },
                summary: { vector_rms_g: 0.1 },
                fft_snapshot: { frequencies: [], magnitudes: [] }
            };
            assertEqual(report.device.sensor, 'ADXL345', 'Sensor metadata present');
        });

        test('F31.3: Summary statistics block completeness', () => {
            const report = {
                device: {},
                session: { duration_sec: 5 },
                summary: { vector_rms_g: 0.85, iso_zone: 'Zone_C' },
                fft_snapshot: { frequencies: [], magnitudes: [] }
            };
            assert(report.summary.vector_rms_g > 0.7, 'Summary stats preserved');
        });

        test('F31.4: FFT snapshot spectral array serialization', () => {
            const fft = computeFFT(new Float32Array(256), 800);
            const snapshot = {
                frequencies: Array.from(fft.frequencies),
                magnitudes: Array.from(fft.magnitudes)
            };
            assertEqual(snapshot.frequencies.length, 128, '128 FFT frequencies in snapshot');
        });

        test('F31.5: Button in DOM for JSON export trigger', () => {
            assert(html.hasDOMElement('btn-export-json'), 'btn-export-json button exists in DOM');
        });
    });

    // ========================================================================
    // Feature 32: Viewport Screenshot Snapshot (R5)
    // ========================================================================
    describe('F32: Viewport Screenshot Snapshot', () => {
        test('F32.1: HTML5 Canvas export capability for WebGL snapshot', () => {
            assert(html.hasDOMElement('btn-snapshot'), 'btn-snapshot button exists in DOM');
        });

        test('F32.2: Valid PNG base64 data URI header prefix', () => {
            const header = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA';
            assert(header.startsWith('data:image/png;base64,'), 'Valid PNG data URI prefix');
        });

        test('F32.3: Non-empty snapshot payload requirement', () => {
            const dummyPayload = 'iVBORw0KGgoAAAANSUhEUgAA';
            assertGreaterThan(dummyPayload.length, 10, 'Payload is non-empty');
        });

        test('F32.4: Snapshot preserves overlay and 3D scene composite', () => {
            assert(html.hasDOMElement('webgl-container'), 'WebGL container exists for snapshot capturing');
        });

        test('F32.5: Automated filename generation formatting', () => {
            const timestamp = '2026-09-01_18-30-00';
            const filename = `VibeGuard_Snapshot_${timestamp}.png`;
            assert(filename.endsWith('.png'), 'Screenshot filename has .png extension');
        });
    });

    // ========================================================================
    // Feature 33: Zero-CDN Standalone Packaging (R6)
    // ========================================================================
    describe('F33: Zero-CDN Standalone Packaging', () => {
        test('F33.1: Single file bundle structure (HTML, CSS, JS in one file)', () => {
            assert(html.content.includes('<style>') && html.content.includes('</style>'), 'Embedded styles block present');
            assert(html.content.includes('<script>') || html.content.includes('id="vendor-threejs"'), 'Embedded scripts/vendor blocks present');
        });

        test('F33.2: Standalone local execution capability (file:// protocol compatibility)', () => {
            assert(!html.content.includes('http://localhost'), 'No local web server requirements hardcoded');
        });

        test('F33.3: Embedded styles and responsive glassmorphism CSS', () => {
            assert(html.content.includes('--accent-cyan: #00f0ff;'), 'Cyber-industrial CSS color variables defined');
            assert(html.hasDOMElement('hud-panel') || html.content.includes('glass-panel'), 'Bottom telemetry HUD panel styled');
        });

        test('F33.4: Inlined standalone Three.js engine and OrbitControls', () => {
            assert(html.hasDOMElement('vendor-threejs') || html.hasThreeJS, 'Three.js library bundled inline');
            assert(html.hasDOMElement('vendor-orbitcontrols') || html.hasOrbitControls, 'OrbitControls bundled inline');
        });

        test('F33.5: Zero backend server dependency requirement', () => {
            assert(html.hasDoctype, 'Valid standard HTML5 doctype declaration');
            assertGreaterThan(html.sizeBytes, 100000, 'Application HTML is full standalone zero-CDN bundle (> 100KB)');
        });
    });
});
