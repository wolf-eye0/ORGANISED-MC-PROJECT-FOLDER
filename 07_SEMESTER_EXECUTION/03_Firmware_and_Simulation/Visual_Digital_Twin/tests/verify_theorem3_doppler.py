#!/usr/bin/env python3
"""
Empirical and Symbolic Verification of Theorem 3 & Kinematic Doppler Derivations
VibeGuard Phase 2 Patent Upgradation Journal 2026 (Section 3.4)

Challenger 1 - Mathematical & Prior Art Challenger
"""

import sys
import numpy as np
import sympy as sp

def symbolic_analysis():
    print("=" * 70)
    print("1. SYMBOLIC VERIFICATION OF THEOREM 3 (EQUATION IN SECTION 3.4)")
    print("=" * 70)
    
    t, v, c, d, f0 = sp.symbols('t v c d f0', positive=True, real=True)
    
    # Line 298: g(t) definition
    # Note: t is offset such that t_CPA = 0
    g = 1 + (v / c) * (v * t) / sp.sqrt(d**2 + v**2 * t**2)
    f_obs = f0 / g
    
    # 1st derivative with respect to t
    df_dt = sp.diff(f_obs, t)
    # 2nd derivative with respect to t
    d2f_dt2 = sp.diff(df_dt, t)
    
    # Evaluate at t = 0 (t_CPA)
    f_CPA = f_obs.subs(t, 0)
    df_CPA = sp.simplify(df_dt.subs(t, 0))
    d2f_CPA = sp.simplify(d2f_dt2.subs(t, 0))
    
    print(f"f_obs(0) [Expected: f0]: {f_CPA}")
    print(f"df/dt(0) [Expected: -f0*v^2 / (c*d)]: {df_CPA}")
    print(f"d2f/dt2(0) [Claimed in Theorem 3: 0]: {d2f_CPA}")
    
    # Check velocity inversion formula
    # v_inv = sqrt( (c * d / f0) * |df_CPA| )
    v_inv_sq = sp.simplify((c * d / f0) * sp.Abs(df_CPA))
    v_inv = sp.sqrt(v_inv_sq)
    print(f"Recovered v: {v_inv}")
    
    # Let's inspect g(t) derivatives at t=0
    dg_dt = sp.diff(g, t)
    d2g_dt2 = sp.diff(dg_dt, t)
    
    dg_CPA = sp.simplify(dg_dt.subs(t, 0))
    d2g_CPA = sp.simplify(d2g_dt2.subs(t, 0))
    print(f"dg/dt(0): {dg_CPA}")
    print(f"d2g/dt2(0): {d2g_CPA}")
    
    # Journal line 329:
    # d2f/dt2 = 2*f0*(g)^(-3) * (dg/dt)^2 - f0*(g)^(-2) * (d2g/dt2)
    term1 = 2 * f0 * (g**(-3)) * (dg_dt**2)
    term2 = f0 * (g**(-2)) * d2g_dt2
    journal_formula = term1 - term2
    diff_check = sp.simplify(d2f_dt2 - journal_formula)
    print(f"Journal Line 329 formula identity check (diff == 0): {diff_check == 0}")
    print(f"Term 1 at t=0: {sp.simplify(term1.subs(t, 0))}")
    print(f"Term 2 at t=0: {sp.simplify(term2.subs(t, 0))}")
    
    # Actual inflection point where d2f/dt2 = 0
    # Solve 2 * (dg/dt)^2 - g * (d2g/dt2) = 0
    print("-" * 70)
    print("Exact inflection point search:")
    xi = sp.symbols('xi', real=True)
    M = sp.symbols('M', positive=True, real=True)
    # In terms of normalized xi = v*t/d, M = v/c:
    # 2*M + 3*xi*sqrt(1+xi**2) + 3*M*xi**2 = 0
    infl_poly = 2*M + 3*xi*sp.sqrt(1 + xi**2) + 3*M*xi**2
    # Series expansion around xi = 0:
    # infl_poly approx 2*M + 3*xi + O(xi^2) => xi_inf approx -2/3 * M
    infl_series = sp.series(infl_poly, xi, 0, 2)
    print(f"Series of numerator around xi=0: {infl_series}")
    print("Thus, to first order in Mach number M, xi_inf = -2/3 * M")
    print("In time units: t_inf = xi_inf * d / v = -2/3 * (v/c) * (d/v) = -2/3 * (d/c)")
    
    return {
        "df_CPA": df_CPA,
        "d2f_CPA": d2f_CPA,
        "v_inv": v_inv,
        "term1_CPA": sp.simplify(term1.subs(t, 0)),
        "term2_CPA": sp.simplify(term2.subs(t, 0))
    }

def retarded_time_symbolic_analysis():
    print("=" * 70)
    print("2. SYMBOLIC VERIFICATION UNDER RETARDED TIME (TRUE ACOUSTIC PROPAGATION)")
    print("=" * 70)
    tau, v, c, d, f0 = sp.symbols('tau v c d f0', real=True)
    # Source trajectory: x(tau) = v * tau
    # Distance to stationary wayside receiver at (0, d):
    # R(tau) = sqrt(d^2 + v^2 * tau^2)
    # Observer reception time: t(tau) = tau + R(tau) / c
    # dt/dtau = 1 + (v^2 * tau) / (c * sqrt(d^2 + v^2 * tau^2))
    dt_dtau = 1 + (v**2 * tau) / (c * sp.sqrt(d**2 + v**2 * tau**2))
    
    # Received instantaneous frequency f_rec(tau) = f0 / (dt/dtau)
    f_rec = f0 / dt_dtau
    
    # df_rec / dt = (df_rec / dtau) / (dt / dtau)
    df_rec_dtau = sp.diff(f_rec, tau)
    df_rec_dt = df_rec_dtau / dt_dtau
    
    # d2f_rec / dt2 = [d/dtau (df_rec / dt)] / (dt / dtau)
    d2f_rec_dt2 = sp.diff(df_rec_dt, tau) / dt_dtau
    
    # At CPA of emission: tau = 0 (which arrives at receiver at t = d / c)
    df_rec_dt_CPA = sp.simplify(df_rec_dt.subs(tau, 0))
    d2f_rec_dt2_CPA = sp.simplify(d2f_rec_dt2.subs(tau, 0))
    
    print(f"True physical Doppler df/dt at CPA (tau=0): {df_rec_dt_CPA}")
    print(f"True physical Doppler d2f/dt2 at CPA (tau=0): {d2f_rec_dt2_CPA}")
    
    return {
        "df_rec_dt_CPA": df_rec_dt_CPA,
        "d2f_rec_dt2_CPA": d2f_rec_dt2_CPA
    }

def numerical_verification(c_val=343.0, d_val=1.5, v_val=20.0, f0_val=500.0):
    print("=" * 70)
    print("3. NUMERICAL VERIFICATION WITH PHYSICAL CONSTANTS")
    print(f"c = {c_val} m/s, d = {d_val} m, v = {v_val} m/s, f0 = {f0_val} Hz")
    print("=" * 70)
    
    # Dense time grid around CPA (t = 0)
    t = np.linspace(-0.5, 0.5, 100001)
    dt = t[1] - t[0]
    
    # Theoretical Journal formulation
    g = 1.0 + (v_val / c_val) * (v_val * t) / np.sqrt(d_val**2 + (v_val * t)**2)
    f_obs = f0_val / g
    
    # Numerical derivatives (Central differences)
    df_num = np.gradient(f_obs, dt)
    d2f_num = np.gradient(df_num, dt)
    
    # Index of CPA (t = 0)
    cpa_idx = np.argmin(np.abs(t))
    
    # Closed-form theoretical values at t=0
    df_cpa_theory = -f0_val * (v_val**2) / (c_val * d_val)
    d2f_cpa_true_analytical = 2.0 * f0_val * (v_val**2 / (c_val * d_val))**2
    d2f_cpa_journal_claim = 0.0
    
    # Recover velocity from numerical and analytical df_cpa
    v_rec_num = np.sqrt((c_val * d_val / f0_val) * np.abs(df_num[cpa_idx]))
    v_rec_theory = np.sqrt((c_val * d_val / f0_val) * np.abs(df_cpa_theory))
    
    # Inflection point: find where d2f crosses zero
    # We find sign changes in d2f_num
    sign_changes = np.where(np.diff(np.sign(d2f_num)))[0]
    t_inflection = t[sign_changes[0]] if len(sign_changes) > 0 else None
    
    print(f"f_obs at CPA:                  {f_obs[cpa_idx]:.6f} Hz (Theory: {f0_val:.6f} Hz)")
    print(f"df/dt at CPA (Numerical):      {df_num[cpa_idx]:.6f} Hz/s")
    print(f"df/dt at CPA (Theory):         {df_cpa_theory:.6f} Hz/s")
    print(f"df/dt Error:                   {np.abs(df_num[cpa_idx] - df_cpa_theory):.6e} Hz/s")
    print(f"Recovered Velocity v (Num):    {v_rec_num:.6f} m/s (Target: {v_val:.6f} m/s)")
    print(f"Recovered Velocity v (Theory): {v_rec_theory:.6f} m/s")
    print("-" * 70)
    print(f"d2f/dt2 at CPA (Numerical):    {d2f_num[cpa_idx]:.6f} Hz/s^2")
    print(f"d2f/dt2 at CPA (True Analyt):  {d2f_cpa_true_analytical:.6f} Hz/s^2")
    print(f"d2f/dt2 at CPA (Journal claim):{d2f_cpa_journal_claim:.6f} Hz/s^2")
    print(f"DISCREPANCY AT CPA:            {np.abs(d2f_num[cpa_idx] - d2f_cpa_journal_claim):.6f} Hz/s^2")
    
    if t_inflection is not None:
        print(f"Actual Inflection Point t_inf: {t_inflection:.6f} s ({t_inflection*1000:.3f} ms before CPA)")
        predicted_t_inf = - (2.0 / 3.0) * (d_val / c_val)
        print(f"Predicted t_inf (-2/3 * d/c):  {predicted_t_inf:.6f} s ({predicted_t_inf*1000:.3f} ms)")
        print(f"Inflection timing match diff:  {np.abs(t_inflection - predicted_t_inf)*1000:.4f} ms")
    
    print("=" * 70)

def sweep_parameter_grid():
    print("4. MULTI-PARAMETER SENSITIVITY SWEEP")
    velocities = [5.0, 10.0, 20.0, 35.0, 50.0]
    distances = [0.5, 1.0, 1.5, 2.5, 5.0]
    c_sound = 343.0
    f0_ref = 500.0
    
    print(f"{'v (m/s)':<8} | {'d (m)':<8} | {'df/dt (Hz/s)':<14} | {'v_recovered':<12} | {'d2f/dt2 (CPA)':<14} | {'t_inf (ms)':<10}")
    print("-" * 75)
    for v in velocities:
        for d in distances:
            df = -f0_ref * (v**2) / (c_sound * d)
            v_rec = np.sqrt((c_sound * d / f0_ref) * abs(df))
            d2f_cpa = 2.0 * f0_ref * ((v**2) / (c_sound * d))**2
            t_inf_approx_ms = - (2.0 / 3.0) * (d / c_sound) * 1000.0
            print(f"{v:<8.1f} | {d:<8.1f} | {df:<14.3f} | {v_rec:<12.3f} | {d2f_cpa:<14.3f} | {t_inf_approx_ms:<10.3f}")

if __name__ == '__main__':
    symbolic_analysis()
    retarded_time_symbolic_analysis()
    numerical_verification()
    sweep_parameter_grid()
