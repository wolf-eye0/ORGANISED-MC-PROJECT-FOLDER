#include "wokwi-api.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#define ADXL345_DEVID_VAL    0xE5
#define REG_DEVID            0x00
#define REG_BW_RATE          0x2C
#define REG_POWER_CTL        0x2D
#define REG_INT_ENABLE       0x2E
#define REG_DATA_FORMAT      0x31
#define REG_DATAX0           0x32
#define REG_DATAX1           0x33
#define REG_DATAY0           0x34
#define REG_DATAY1           0x35
#define REG_DATAZ0           0x36
#define REG_DATAZ1           0x37
#define REG_FIFO_CTL         0x38

#define SPI_BUFFER_SIZE      16
#define TWO_PI               6.28318530717958647692

typedef struct {
    pin_t pin_cs;
    pin_t pin_sck;
    pin_t pin_mosi;
    pin_t pin_miso;
    pin_t pin_int1;
    spi_dev_t spi_device;
    uint32_t attr_fault_level;
    uint8_t registers[0x40];
    uint8_t spi_rx_buf[SPI_BUFFER_SIZE];
    uint8_t spi_tx_buf[SPI_BUFFER_SIZE];
    uint8_t current_reg;
    bool is_read;
    bool multi_byte;
    uint32_t byte_counter;
    double time_sec;
    uint32_t sample_count;
} chip_state_t;

static void update_sensor_dynamics(chip_state_t *chip) {
    uint32_t fault = attr_read(chip->attr_fault_level);
    double t = chip->time_sec;

    // N20 Motor Kinematics: 600 RPM = 10.0 Hz fundamental frequency
    double f0 = 10.0;
    double omega = TWO_PI * f0;

    // Normal baseline vibration (gear mesh + motor noise floor)
    double baseline_noise_x = ((double)(rand() % 100) / 1000.0) - 0.05;
    double baseline_noise_y = ((double)(rand() % 100) / 1000.0) - 0.05;
    double baseline_noise_z = ((double)(rand() % 100) / 1000.0) - 0.05;

    double ax = 0.08 * sin(omega * t) + 0.02 * sin(2.0 * omega * t) + baseline_noise_x;
    double ay = 0.08 * cos(omega * t) + 0.02 * cos(2.0 * omega * t) + baseline_noise_y;
    double az = 1.00 + 0.04 * sin(3.0 * omega * t) + baseline_noise_z;

    // Controlled mechanical imbalance fault injection
    if (fault > 0) {
        double severity = (double)fault / 100.0;
        double unbalance_amplitude = 1.85 * severity;

        ax += unbalance_amplitude * sin(omega * t);
        ay += unbalance_amplitude * cos(omega * t);
        az += (unbalance_amplitude * 0.35) * sin(2.0 * omega * t);
    }

    // Scale to ADXL345 Full-Res mode (3.9 mg/LSB -> ~256 LSB/g)
    int16_t raw_x = (int16_t)(ax * 256.0);
    int16_t raw_y = (int16_t)(ay * 256.0);
    int16_t raw_z = (int16_t)(az * 256.0);

    chip->registers[REG_DATAX0] = (uint8_t)(raw_x & 0xFF);
    chip->registers[REG_DATAX1] = (uint8_t)((raw_x >> 8) & 0xFF);
    chip->registers[REG_DATAY0] = (uint8_t)(raw_y & 0xFF);
    chip->registers[REG_DATAY1] = (uint8_t)((raw_y >> 8) & 0xFF);
    chip->registers[REG_DATAZ0] = (uint8_t)(raw_z & 0xFF);
    chip->registers[REG_DATAZ1] = (uint8_t)((raw_z >> 8) & 0xFF);

    chip->time_sec += 0.00125; // Advance timestep by 1/800Hz
}

static void on_spi_done(void *user_data, uint8_t *buffer, uint32_t count) {
    chip_state_t *chip = (chip_state_t *)user_data;
    if (count == 0) return;

    if (chip->byte_counter == 0) {
        uint8_t header = buffer[0];
        chip->is_read = (header & 0x80) != 0;
        chip->multi_byte = (header & 0x40) != 0;
        chip->current_reg = header & 0x3F;
        chip->byte_counter = 1;

        if (chip->is_read) {
            update_sensor_dynamics(chip);
            chip->spi_tx_buf[0] = chip->registers[chip->current_reg];
            spi_start(chip->spi_device, chip->spi_tx_buf, 1);
        } else {
            spi_start(chip->spi_device, chip->spi_rx_buf, 1);
        }
    } else {
        if (!chip->is_read) {
            chip->registers[chip->current_reg] = buffer[0];
        }
        if (chip->multi_byte && chip->current_reg < 0x3F) {
            chip->current_reg++;
        }
        if (chip->is_read) {
            chip->spi_tx_buf[0] = chip->registers[chip->current_reg];
            spi_start(chip->spi_device, chip->spi_tx_buf, 1);
        } else {
            spi_start(chip->spi_device, chip->spi_rx_buf, 1);
        }
        chip->byte_counter++;
    }
}

static void on_cs_change(void *user_data, pin_t pin, uint32_t value) {
    chip_state_t *chip = (chip_state_t *)user_data;
    if (value == LOW) {
        chip->byte_counter = 0;
        spi_start(chip->spi_device, chip->spi_rx_buf, 1);
    } else {
        spi_stop(chip->spi_device);
    }
}

void chip_init(void) {
    chip_state_t *chip = (chip_state_t *)malloc(sizeof(chip_state_t));
    memset(chip, 0, sizeof(chip_state_t));

    chip->pin_cs = pin_init("CS", INPUT_PULLUP);
    chip->pin_sck = pin_init("SCK", INPUT);
    chip->pin_mosi = pin_init("MOSI", INPUT);
    chip->pin_miso = pin_init("MISO", OUTPUT);
    chip->pin_int1 = pin_init("INT1", OUTPUT);

    chip->attr_fault_level = attr_init("fault_level", 0);

    chip->registers[REG_DEVID] = ADXL345_DEVID_VAL;
    chip->registers[REG_BW_RATE] = 0x0A;
    chip->registers[REG_POWER_CTL] = 0x00;
    chip->registers[REG_DATA_FORMAT] = 0x00;

    const spi_config_t spi_config = {
        .sck = chip->pin_sck,
        .mosi = chip->pin_mosi,
        .miso = chip->pin_miso,
        .mode = 3,
        .done = on_spi_done,
        .user_data = chip
    };
    chip->spi_device = spi_init(&spi_config);

    const pin_watch_config_t watch_cs = {
        .edge = BOTH,
        .pin_change = on_cs_change,
        .user_data = chip
    };
    pin_watch(chip->pin_cs, &watch_cs);
}
