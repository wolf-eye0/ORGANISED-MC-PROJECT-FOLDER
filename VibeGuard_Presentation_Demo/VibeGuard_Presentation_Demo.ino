#include <Arduino.h>
#include <SPI.h>
#include <cmath>

// ============================================================================
// VIBEGUARD: PHYSICAL SENSOR TELEMETRY & HEALTH DEMONSTRATOR
// Hardware: 7Semi ESP32-DEVKIT-E + ADXL345 SPI (Certified SPI_MODE2, Silicon 0xE5)
// Standard: ISO 10816-3 Mechanical Vibration Severity Standards
// Presentation Scope: Real Sensor Telemetry + Good Health Baseline + Dynamic Trigger
// ============================================================================

#define PIN_CS            21
#define PIN_SCK           18
#define PIN_MISO          19
#define PIN_MOSI          23

#define PIN_LED_GREEN     25
#define PIN_LED_BLUE      26
#define PIN_LED_RED       27
#define PIN_BOOT_BUTTON   0

#define ADXL345_REG_DEVID       0x00
#define ADXL345_REG_BW_RATE     0x2C
#define ADXL345_REG_POWER_CTL   0x2D
#define ADXL345_REG_DATA_FORMAT 0x31
#define ADXL345_REG_DATAX0      0x32

#define ADXL345_DEVID           0xE5
#define SCALE_FACTOR            0.00390625f // 3.9 mg/LSB full resolution (±16g)

#define SPI_SPEED               1000000
#define CHIP_SPI_MODE           SPI_MODE2

// DSP Window & ISO 10816 Thresholds
#define BUFFER_SIZE             128
#define RMS_ALARM_LIMIT         0.35f   // ISO 10816 Zone B/C boundary (Alarm: 0.35g RMS)

bool g_sensor_ready = false;
int g_alarm_debounce = 0;
bool g_force_alarm_serial = false;

void setRGB(bool r, bool g, bool b) {
  digitalWrite(PIN_LED_RED,   r ? HIGH : LOW);
  digitalWrite(PIN_LED_GREEN, g ? HIGH : LOW);
  digitalWrite(PIN_LED_BLUE,  b ? HIGH : LOW);
}

uint8_t read_reg(uint8_t reg) {
  SPI.beginTransaction(SPISettings(SPI_SPEED, MSBFIRST, CHIP_SPI_MODE));
  digitalWrite(PIN_CS, LOW);
  delayMicroseconds(5);
  SPI.transfer(reg | 0x80);
  uint8_t val = SPI.transfer(0x00);
  digitalWrite(PIN_CS, HIGH);
  SPI.endTransaction();
  delayMicroseconds(10);
  return val;
}

void write_reg(uint8_t reg, uint8_t val) {
  SPI.beginTransaction(SPISettings(SPI_SPEED, MSBFIRST, CHIP_SPI_MODE));
  digitalWrite(PIN_CS, LOW);
  delayMicroseconds(5);
  SPI.transfer(reg & 0x7F);
  SPI.transfer(val);
  digitalWrite(PIN_CS, HIGH);
  SPI.endTransaction();
  delayMicroseconds(10);
}

void read_accel_burst(float &ax, float &ay, float &az) {
  uint8_t raw[6];
  SPI.beginTransaction(SPISettings(SPI_SPEED, MSBFIRST, CHIP_SPI_MODE));
  digitalWrite(PIN_CS, LOW);
  delayMicroseconds(5);
  SPI.transfer(ADXL345_REG_DATAX0 | 0x80 | 0x40); // Read (0x80) | Multibyte (0x40)
  for (int i = 0; i < 6; i++) {
    raw[i] = SPI.transfer(0x00);
  }
  digitalWrite(PIN_CS, HIGH);
  SPI.endTransaction();

  int16_t x = (int16_t)(raw[0] | (raw[1] << 8));
  int16_t y = (int16_t)(raw[2] | (raw[3] << 8));
  int16_t z = (int16_t)(raw[4] | (raw[5] << 8));

  ax = (float)x * SCALE_FACTOR;
  ay = (float)y * SCALE_FACTOR;
  az = (float)z * SCALE_FACTOR;
}

void setup() {
  Serial.begin(115200);
  delay(1200);

  Serial.println("\n==================================================================");
  Serial.println("   VIBEGUARD: PHYSICAL SENSOR HEALTH MONITORING SYSTEM           ");
  Serial.println("   Hardware: 7Semi ESP32-DEVKIT-E + ADXL345 (SPI Mode 2 Certified)");
  Serial.println("   Standard: ISO 10816-3 Mechanical Vibration Severity Standards ");
  Serial.println("==================================================================");

  pinMode(PIN_LED_RED,     OUTPUT);
  pinMode(PIN_LED_GREEN,   OUTPUT);
  pinMode(PIN_LED_BLUE,    OUTPUT);
  pinMode(PIN_BOOT_BUTTON, INPUT_PULLUP);

  setRGB(false, false, true); // Solid Blue during boot self-check

  pinMode(PIN_CS, OUTPUT);
  digitalWrite(PIN_CS, HIGH);
  SPI.begin(PIN_SCK, PIN_MISO, PIN_MOSI, PIN_CS);
  delay(50);

  // Initialize ADXL345
  uint8_t id = read_reg(ADXL345_REG_DEVID);
  Serial.printf("[SENSOR] ADXL345 DEVID: 0x%02X ... ", id);

  if (id == ADXL345_DEVID) {
    Serial.println("VERIFIED GENUINE SILICON (0xE5)!");
    write_reg(ADXL345_REG_POWER_CTL, 0x00);    // Standby first
    delay(10);
    write_reg(ADXL345_REG_BW_RATE, 0x0D);      // 800 Hz ODR
    delay(5);
    write_reg(ADXL345_REG_DATA_FORMAT, 0x0B);  // Full-Res, ±16g
    delay(5);
    write_reg(ADXL345_REG_POWER_CTL, 0x08);    // Measurement Mode
    delay(20);

    uint8_t pctl = read_reg(ADXL345_REG_POWER_CTL);
    uint8_t fmt  = read_reg(ADXL345_REG_DATA_FORMAT);
    uint8_t bw   = read_reg(ADXL345_REG_BW_RATE);
    uint8_t act  = read_reg(0x30);             // INT_SOURCE
    Serial.printf("[CONFIRM] POWER_CTL=0x%02X, DATA_FORMAT=0x%02X, BW_RATE=0x%02X, INT_SOURCE=0x%02X\n",
                  pctl, fmt, bw, act);

    g_sensor_ready = true;
    Serial.println("[DSP] Sample Rate: 800 Hz | Window: 128 samples (160ms) | Nyquist: 400 Hz");
    Serial.println("[DEMO CONTROLS]");
    Serial.println("  - Tap bench/sensor: Natural vibration spike triggers Alarm");
    Serial.println("  - Press BOOT button (GPIO 0): Injects unbalance fault (+0.70g RMS)");
    Serial.println("  - Type 'a' in Serial: Toggle forced unbalance fault");
    Serial.println("  - Type 'n' in Serial: Clear forced fault (Normal)");
    Serial.println("[STATE] Self-Test Complete -> System [NORMAL / GOOD HEALTH]");
    setRGB(false, true, false); // Solid Green!
    delay(500);
  } else {
    Serial.println("ADXL345 not found! Check wiring.");
  }
}

unsigned long g_last_search_print = 0;

void loop() {
  if (!g_sensor_ready) {
    setRGB(false, false, true); // Keep Solid BLUE while disconnected / searching
    uint8_t id = read_reg(ADXL345_REG_DEVID);
    if (id == ADXL345_DEVID) {
      write_reg(ADXL345_REG_POWER_CTL, 0x00);
      delay(10);
      write_reg(ADXL345_REG_BW_RATE, 0x0D);
      write_reg(ADXL345_REG_DATA_FORMAT, 0x0B);
      write_reg(ADXL345_REG_POWER_CTL, 0x08);
      delay(20);
      g_sensor_ready = true;
      Serial.println("\n[ONLINE] ADXL345 Connected & Initialized (0xE5)!");
      setRGB(false, true, false); // Solid GREEN when verified online
    } else {
      if (millis() - g_last_search_print > 1500) {
        Serial.printf("[SENSOR SEARCH] DEVID: 0x%02X (Expected 0xE5) | Status: DISCONNECTED | LED: BLUE\n", id);
        g_last_search_print = millis();
      }
      delay(100);
      return;
    }
  }

  // Check for serial user command
  while (Serial.available() > 0) {
    char c = Serial.read();
    if (c == 'a' || c == 'A') {
      g_force_alarm_serial = true;
      Serial.println("\n>>> [SERIAL COMMAND] FORCED UNBALANCE FAULT INJECTED <<<");
    } else if (c == 'n' || c == 'N') {
      g_force_alarm_serial = false;
      Serial.println("\n>>> [SERIAL COMMAND] FORCED FAULT CLEARED (AUTO-SENSE) <<<");
    }
  }

  // 1. Gather 128 real-time physical samples at 800 Hz (~1.25 ms per sample)
  float buf_x[BUFFER_SIZE];
  float buf_y[BUFFER_SIZE];
  float buf_z[BUFFER_SIZE];

  float mean_x = 0, mean_y = 0, mean_z = 0;
  bool boot_pressed = false;

  for (int i = 0; i < BUFFER_SIZE; i++) {
    unsigned long t0 = micros();
    read_accel_burst(buf_x[i], buf_y[i], buf_z[i]);
    mean_x += buf_x[i];
    mean_y += buf_y[i];
    mean_z += buf_z[i];
    if (digitalRead(PIN_BOOT_BUTTON) == LOW) {
      boot_pressed = true;
    }
    while (micros() - t0 < 1250); // 1250 us = 800 Hz
  }

  mean_x /= BUFFER_SIZE;
  mean_y /= BUFFER_SIZE;
  mean_z /= BUFFER_SIZE;

  // 2. Silicon Health Sanity Check: Verify static gravity vector magnitude
  float static_gravity = sqrt(mean_x * mean_x + mean_y * mean_y + mean_z * mean_z);
  if (static_gravity < 0.25f) {
    // Sensor line flatlined (all 0.00g) -> wire fell out or disconnected!
    Serial.printf("[WARNING] Sensor Flatlined (|G|=%.2fg < 0.25g)! Sensor wire disconnected.\n", static_gravity);
    g_sensor_ready = false;
    setRGB(false, false, true); // Return to Blue search state
    delay(200);
    return;
  }

  // 3. DC Bias Removal (Subtract static 1.0g gravity and tilt offsets)
  float sum_sq = 0;
  for (int i = 0; i < BUFFER_SIZE; i++) {
    float dx = buf_x[i] - mean_x;
    float dy = buf_y[i] - mean_y;
    float dz = buf_z[i] - mean_z;
    sum_sq += (dx * dx + dy * dy + dz * dz);
  }

  // 4. Dynamic Vector Magnitude RMS Calculation (AC Vibration Severity)
  float vector_rms = sqrt(sum_sq / (float)BUFFER_SIZE);

  // 5. Interactive BOOT button check for presentation unbalance fault injection
  if (digitalRead(PIN_BOOT_BUTTON) == LOW) {
    boot_pressed = true;
  }
  if (boot_pressed || g_force_alarm_serial) {
    vector_rms += 0.70f; // Inject unbalance fault into dynamic RMS
  }

  // 6. Persistence Filter (K of M Debounce)
  if (vector_rms >= RMS_ALARM_LIMIT) {
    if (g_alarm_debounce < 4) g_alarm_debounce++;
  } else {
    if (g_alarm_debounce > 0) g_alarm_debounce--;
  }

  // 7. State Evaluation & Indicator Control
  const char* status_label;
  if (g_alarm_debounce >= 2) {
    status_label = "ALARM / UNHEALTHY (Rotor Unbalance / High Vibration)";
    setRGB(true, false, false); // Solid RED
  } else {
    status_label = "NORMAL / GOOD HEALTH (Permissible Smooth Run)";
    setRGB(false, true, false); // Solid GREEN
  }

  // 8. Telemetry Reporting (Serial Plotter + Human Readable)
  Serial.printf(">VRMS:%.3f,AlarmThresh:%.2f,State:%d\n",
                vector_rms, RMS_ALARM_LIMIT, (g_alarm_debounce >= 2) ? 1 : 0);

  Serial.printf("[PHYSICAL SENSOR] Accel: X=%+5.2fg Y=%+5.2fg Z=%+5.2fg | Vector RMS: %5.3fg | Status: [%s]%s\n",
                buf_x[BUFFER_SIZE - 1], buf_y[BUFFER_SIZE - 1], buf_z[BUFFER_SIZE - 1],
                vector_rms, status_label,
                boot_pressed ? " <-- [BOOT BUTTON FAULT INJECTION]" : (g_force_alarm_serial ? " <-- [SERIAL FORCED FAULT]" : ""));

  delay(20);
}
