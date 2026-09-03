#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <sstream>
#include <fstream>
#include "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/VibeGuard_ESP32_Firmware/features.h"
#include "/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/VibeGuard_ESP32_Firmware/state.h"

int main() {
    std::cout << std::fixed << std::setprecision(6);
    std::ofstream out("/home/paradoxpete/Documents/PROJECT_ORGANIZED/07_SEMESTER_EXECUTION/03_Firmware_and_Simulation/Visual_Digital_Twin/scratch/cpp_oracle_results.json");
    
    out << "{\n";

    // 1. Hann Window Verification
    const size_t N = 256;
    std::vector<float> hann_test(N, 1.0f);
    apply_hann_window(hann_test.data(), N);

    out << "  \"hann_window\": {\n";
    out << "    \"w_0\": " << hann_test[0] << ",\n";
    out << "    \"w_1\": " << hann_test[1] << ",\n";
    out << "    \"w_center_127\": " << hann_test[127] << ",\n";
    out << "    \"w_center_128\": " << hann_test[128] << ",\n";
    out << "    \"w_last\": " << hann_test[N - 1] << ",\n";
    
    double hann_sum = 0.0;
    double hann_sq_sum = 0.0;
    bool symmetric = true;
    for (size_t i = 0; i < N; ++i) {
        hann_sum += hann_test[i];
        hann_sq_sum += hann_test[i] * hann_test[i];
        if (std::abs(hann_test[i] - hann_test[N - 1 - i]) > 1e-6) {
            symmetric = false;
        }
    }
    out << "    \"coherent_gain\": " << (hann_sum / N) << ",\n";
    out << "    \"rms_gain\": " << std::sqrt(hann_sq_sum / N) << ",\n";
    out << "    \"symmetric\": " << (symmetric ? "true" : "false") << "\n";
    out << "  },\n";

    // 2. DC Removal Test
    std::vector<float> dc_test = { 1.5f, 2.5f, 3.5f, 4.5f, 5.5f };
    remove_dc(dc_test.data(), dc_test.size());
    out << "  \"dc_removal\": {\n";
    out << "    \"values\": [" << dc_test[0] << ", " << dc_test[1] << ", " << dc_test[2] << ", " << dc_test[3] << ", " << dc_test[4] << "],\n";
    float sum_after_dc = 0.0f;
    for (float v : dc_test) sum_after_dc += v;
    out << "    \"mean_after\": " << sum_after_dc << "\n";
    out << "  },\n";

    // 3. RMS and Vector RMS Test
    std::vector<float> x(N), y(N), z(N);
    const float Fs = 800.0f;
    const float f_sine = 10.0f; // 10 Hz (600 RPM)
    const float two_pi = 6.283185307179586f;
    const float amp = 1.0f;

    for (size_t i = 0; i < N; ++i) {
        float t = static_cast<float>(i) / Fs;
        x[i] = amp * std::sin(two_pi * f_sine * t);
        y[i] = amp * std::cos(two_pi * f_sine * t);
        z[i] = 1.0f + 0.2f * std::sin(two_pi * 2.0f * f_sine * t); // 1g static + 2X
    }

    float raw_rms_x = compute_rms(x.data(), N);
    float raw_rms_y = compute_rms(y.data(), N);
    float raw_rms_z = compute_rms(z.data(), N);
    float raw_vec_rms = compute_vector_rms(x.data(), y.data(), z.data(), N);

    // After DC removal on Z
    std::vector<float> z_ac = z;
    remove_dc(z_ac.data(), N);
    float ac_rms_z = compute_rms(z_ac.data(), N);
    float ac_vec_rms = compute_vector_rms(x.data(), y.data(), z_ac.data(), N);

    out << "  \"rms\": {\n";
    out << "    \"rms_x\": " << raw_rms_x << ",\n";
    out << "    \"rms_y\": " << raw_rms_y << ",\n";
    out << "    \"rms_z_raw\": " << raw_rms_z << ",\n";
    out << "    \"rms_z_ac\": " << ac_rms_z << ",\n";
    out << "    \"vector_rms_raw\": " << raw_vec_rms << ",\n";
    out << "    \"vector_rms_ac\": " << ac_vec_rms << ",\n";
    out << "    \"theoretical_rms_sine_1g\": " << (amp / std::sqrt(2.0f)) << "\n";
    out << "  },\n";

    // 4. FFT Peak Frequency & Magnitude Test
    out << "  \"fft_tests\": [\n";
    std::vector<float> test_freqs = { 5.0f, 10.0f, 15.625f, 20.0f, 50.0f, 100.0f };
    for (size_t k = 0; k < test_freqs.size(); ++k) {
        float f_target = test_freqs[k];
        std::vector<float> sig(N);
        for (size_t i = 0; i < N; ++i) {
            float t = static_cast<float>(i) / Fs;
            sig[i] = amp * std::sin(two_pi * f_target * t);
        }
        float out_f = 0.0f, out_m = 0.0f;
        compute_fft_peak(sig.data(), N, Fs, out_f, out_m);
        out << "    {\n";
        out << "      \"target_freq\": " << f_target << ",\n";
        out << "      \"detected_freq\": " << out_f << ",\n";
        out << "      \"detected_mag\": " << out_m << ",\n";
        out << "      \"delta_f\": " << (Fs / N) << "\n";
        out << "    }" << (k + 1 < test_freqs.size() ? "," : "") << "\n";
    }
    out << "  ],\n";

    // 5. Persistence State Machine Test
    PersistenceParams params_persist{ 3, 5, 3, false };
    PersistenceParams params_consec{ 3, 5, 3, true };

    out << "  \"persistence_tests\": {\n";
    // Sequence 1: 2 abnormal out of 5 -> false
    WindowHistory h1{ { false, false, true, false, true } };
    out << "    \"seq_2_of_5\": " << (should_enter_abnormal(h1, params_persist) ? "true" : "false") << ",\n";

    // Sequence 2: 3 abnormal out of 5 (non-consecutive) -> true (persist), false (consecutive)
    WindowHistory h2{ { true, false, true, false, true } };
    out << "    \"seq_3_of_5_non_consec\": " << (should_enter_abnormal(h2, params_persist) ? "true" : "false") << ",\n";
    out << "    \"seq_3_of_5_consec_mode\": " << (should_enter_abnormal(h2, params_consec) ? "true" : "false") << ",\n";

    // Sequence 3: 3 abnormal consecutive -> true for both
    WindowHistory h3{ { false, false, true, true, true } };
    out << "    \"seq_3_consecutive\": " << (should_enter_abnormal(h3, params_persist) ? "true" : "false") << ",\n";

    // Sequence 4: Clearing hysteresis: 2 normal after alarm -> false
    WindowHistory h_clear_fail{ { true, true, true, false, false } };
    out << "    \"clear_2_of_3_clean\": " << (should_clear_abnormal(h_clear_fail, params_persist) ? "true" : "false") << ",\n";

    // Sequence 5: Clearing hysteresis: 3 clean -> true
    WindowHistory h_clear_pass{ { true, true, false, false, false } };
    out << "    \"clear_3_of_3_clean\": " << (should_clear_abnormal(h_clear_pass, params_persist) ? "true" : "false") << "\n";
    out << "  }\n";

    out << "}\n";
    out.close();

    std::cout << "C++ Oracle Execution Completed Successfully." << std::endl;
    return 0;
}
