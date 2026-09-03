#include "wokwi-api.h"
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  pin_t pin_12v;
  pin_t pin_gnd;
  pin_t pin_tach;
  pin_t pin_fault;

  uint32_t attr_rpm;
  uint32_t attr_imbalance;

  timer_t pulse_timer;
  bool tach_state;
} n20_motor_t;

static void on_pulse_timer(void *user_data) {
  n20_motor_t *chip = (n20_motor_t *)user_data;

  // Check if 12V power is applied
  uint32_t pwr = pin_read(chip->pin_12v);
  if (pwr == LOW) {
    pin_write(chip->pin_tach, LOW);
    // Arm timer to re-check every 50ms
    timer_start(chip->pulse_timer, 50000, false);
    return;
  }

  // Read current RPM slider
  float rpm_val = attr_read_float(chip->attr_rpm);
  if (rpm_val < 100.0f) rpm_val = 600.0f;

  // Toggle tachometer pin to simulate 1 pulse per revolution
  chip->tach_state = !chip->tach_state;
  pin_write(chip->pin_tach, chip->tach_state ? HIGH : LOW);

  // Period in microseconds for half-cycle: (60 / RPM / 2) * 1,000,000
  uint32_t half_period_us = (uint32_t)((30.0f / rpm_val) * 1000000.0f);
  if (half_period_us < 5000) half_period_us = 5000;

  timer_start(chip->pulse_timer, half_period_us, false);
}

void chip_init(void) {
  n20_motor_t *chip = (n20_motor_t *)calloc(1, sizeof(n20_motor_t));

  chip->pin_12v   = pin_init("12V", INPUT_PULLDOWN);
  chip->pin_gnd   = pin_init("GND", INPUT_PULLDOWN);
  chip->pin_tach  = pin_init("TACH", OUTPUT_LOW);
  chip->pin_fault = pin_init("FAULT", OUTPUT_LOW);

  chip->attr_rpm = attr_init_float("rpm", 600.0f);
  chip->attr_imbalance = attr_init_float("imbalance", 3.5f);

  const timer_config_t timer_cfg = {
    .callback = on_pulse_timer,
    .user_data = chip,
  };
  chip->pulse_timer = timer_init(&timer_cfg);

  // Start timer
  timer_start(chip->pulse_timer, 50000, false);

  printf("[N20-MOTOR] 12V DC Gear Motor & Rig Initialized (Nominal 600 RPM)\n");
}
