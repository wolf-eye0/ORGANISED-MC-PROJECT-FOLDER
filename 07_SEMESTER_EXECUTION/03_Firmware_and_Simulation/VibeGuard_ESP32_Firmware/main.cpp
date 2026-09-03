#include <iostream>
#include <cmath>
#include "features.h"
#include "state.h"

// Helper: generate a simple sine wave.
std::vector<float> make_sine(int n, float amplitude) {
    std::vector<float> v(n);
    const float two_pi = 6.2831853f;
    for (int i = 0; i < n; ++i) {
        float phase = two_pi * static_cast<float>(i) / static_cast<float>(n);
        v[i] = amplitude * std::sin(phase);
    }
    return v;
}

int main() {
    // ---- Test 1: DC removal + RMS on a constant ----
    {
        std::vector<float> data(8, 1.0f); // all ones
        remove_dc(data);
        float rms = compute_rms(data);
        std::cout << "[Test1] RMS of constant after DC removal: " << rms << "\n";
    }

    // ---- Test 2: DC removal + RMS on a sine ----
    {
        std::vector<float> data = make_sine(256, 1.0f);
        remove_dc(data);
        float rms = compute_rms(data);
        std::cout << "[Test2] RMS of sine after DC removal: " << rms << "\n";
    }

    // ---- Test 3: Persistence and state machine ----
    WindowHistory hist;
    PersistenceParams params{ .k_required = 3, .m_window = 5, .require_consecutive = true };

    SystemState state = SystemState::Calibrating;

    bool config_ok = true;
    bool calibration_done = true; // pretend calibration finished
    bool fault_condition = false;

    // Simulate windows: 0=normal, 1=above threshold
    int windows[] = {0, 1, 1, 1, 0, 0, 1, 1, 1};
    for (int i = 0; i < static_cast<int>(sizeof(windows)/sizeof(windows[0])); ++i) {
        bool above = (windows[i] != 0);
        hist.is_above_threshold.push_back(above);

        bool enter_abn = should_enter_abnormal(hist, params);
        bool clear_abn = should_clear_abnormal(hist, params);

        state = update_state(state,
                             config_ok,
                             calibration_done,
                             enter_abn,
                             clear_abn,
                             fault_condition);

        std::cout << "[Window " << i
                  << "] above=" << above
                  << " enter_abn=" << enter_abn
                  << " clear_abn=" << clear_abn
                  << " state=" << to_string(state)
                  << "\n";
    }

    return 0;
}