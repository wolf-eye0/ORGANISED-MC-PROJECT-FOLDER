// ESP32 DevKit WROOM-E - Blink Test
// LED blinks slowly (1 second ON, 1 second OFF) for easy confirmation
// Built-in LED is on GPIO2 for most ESP32 DevKit boards

#define LED_PIN 2        // Built-in LED on ESP32 DevKit
#define BLINK_ON_MS  1000  // LED ON duration (ms)
#define BLINK_OFF_MS 1000  // LED OFF duration (ms)

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("ESP32 Blink Test Started - 1 second ON / 1 second OFF");
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  Serial.println("LED ON");
  delay(BLINK_ON_MS);

  digitalWrite(LED_PIN, LOW);
  Serial.println("LED OFF");
  delay(BLINK_OFF_MS);
}
