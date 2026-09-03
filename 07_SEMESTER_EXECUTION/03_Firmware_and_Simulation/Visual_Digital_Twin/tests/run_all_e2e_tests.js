#!/usr/bin/env node
/**
 * VibeGuard 3D WebGL Digital Twin - Master E2E Automated Test Runner
 * 
 * Executes all 4 Test Tiers:
 * 1. Tier 1: Feature Tests (>= 165 tests across all 33 features)
 * 2. Tier 2: Boundary & Corner Tests (>= 165 tests)
 * 3. Tier 3: Pairwise Combinatorial Tests (>= 33 tests)
 * 4. Tier 4: Real-World Application Scenarios (>= 8 scenarios)
 * 
 * Enforces strict pass/fail semantics and exits with code 0 on success.
 */

const { testCtx } = require('./test_helpers');

console.log('='.repeat(80));
console.log('🛡️  VIBEGUARD 3D DIGITAL TWIN - AUTOMATED E2E TEST SUITE RUNNER');
console.log('='.repeat(80));
console.log(`Started at: ${new Date().toISOString()}`);
console.log('');

const startTime = performance.now();

try {
    console.log('>>> [1/4] Loading & Executing Tier 1: Feature Tests (F1 to F33)...');
    require('./tier1_feature_tests');

    console.log('>>> [2/4] Loading & Executing Tier 2: Boundary & Corner Tests...');
    require('./tier2_boundary_tests');

    console.log('>>> [3/4] Loading & Executing Tier 3: Pairwise Combinatorial Tests...');
    require('./tier3_pairwise_tests');

    console.log('>>> [4/4] Loading & Executing Tier 4: Real-World Application Scenarios...');
    require('./tier4_scenario_tests');
} catch (fatalErr) {
    console.error('FATAL UNHANDLED ERROR IN TEST SUITE EXECUTION:', fatalErr);
    process.exit(1);
}

const totalDurationMs = performance.now() - startTime;
const { total, passed, failed, suites } = testCtx.results;

console.log('');
console.log('='.repeat(80));
console.log('📊 TEST EXECUTION SUMMARY & TIER BREAKDOWN');
console.log('='.repeat(80));

let tier1Count = 0, tier2Count = 0, tier3Count = 0, tier4Count = 0;

suites.forEach((s, idx) => {
    const statusIcon = s.failed === 0 ? '✅' : '❌';
    console.log(`${statusIcon} Suite ${idx + 1}: ${s.name.padEnd(55)} [${s.passed}/${s.tests.length} PASS]`);
    
    if (s.name.includes('Tier 1') || s.name.startsWith('F')) {
        tier1Count += s.tests.length;
    } else if (s.name.includes('Tier 2') || s.name.startsWith('Category')) {
        tier2Count += s.tests.length;
    } else if (s.name.includes('Tier 3') || s.name.startsWith('Matrix')) {
        tier3Count += s.tests.length;
    } else if (s.name.includes('Tier 4') || s.name.startsWith('Scenario')) {
        tier4Count += s.tests.length;
    }

    if (s.failed > 0) {
        s.tests.filter(t => t.status === 'FAIL').forEach(f => {
            console.log(`   ❌ FAIL: ${f.name}`);
            console.log(`      Error: ${f.error}`);
        });
    }
});

console.log('-'.repeat(80));
console.log('📈 COVERAGE THRESHOLD COMPLIANCE:');
console.log(`   - Tier 1 (Feature Coverage):     ${tier1Count.toString().padStart(4)} tests (Requirement: >= 165) ${tier1Count >= 165 ? '✅ MET' : '❌ SHORT'}`);
console.log(`   - Tier 2 (Boundary & Corner):    ${tier2Count.toString().padStart(4)} tests (Requirement: >= 165) ${tier2Count >= 165 ? '✅ MET' : '❌ SHORT'}`);
console.log(`   - Tier 3 (Pairwise Interaction): ${tier3Count.toString().padStart(4)} tests (Requirement: >= 33)  ${tier3Count >= 33 ? '✅ MET' : '❌ SHORT'}`);
console.log(`   - Tier 4 (Real-World Scenarios): ${tier4Count.toString().padStart(4)} tests (Requirement: >= 8)   ${tier4Count >= 8 ? '✅ MET' : '❌ SHORT'}`);
console.log(`   - TOTAL TEST SUITE:              ${total.toString().padStart(4)} tests (Requirement: >= 371) ${total >= 371 ? '✅ MET' : '❌ SHORT'}`);
console.log('-'.repeat(80));
console.log(`⏱️  Total Execution Time: ${(totalDurationMs / 1000).toFixed(2)}s`);
console.log(`🎯 Final Result: ${passed} PASSED, ${failed} FAILED`);
console.log('='.repeat(80));

if (failed > 0) {
    console.error(`\n❌ TEST SUITE FAILED WITH ${failed} ASSERTION FAILURES!`);
    process.exit(1);
} else {
    console.log(`\n✅ ALL ${passed} E2E TEST CASES PASSED WITH 100% SUCCESS!`);
    process.exit(0);
}
