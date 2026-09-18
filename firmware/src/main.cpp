#include <Arduino.h>

/*
 * AuraSense - Wearable Ambient & Health Predictive System
 * Platform: ESP32-S3 / NRF52840 (Bluetooth Low Energy + Edge AI)
 */

struct SensorData {
  float aqi;
  float co2_ppm;
  float temperature_c;
  float humidity_pct;
  float noise_db;
  float heart_rate_bpm;
  float spo2_pct;
};

// Función de Inferencia Local Embebida (Edge AI Decision Tree Quantized)
uint8_t predict_health_risk(const SensorData& data) {
  // Evaluación en tiempo real sin latencia de nube (0: Normal, 1: Moderado, 2: Severo)
  if (data.spo2_pct < 90.0f || (data.temperature_c > 38.0f && data.heart_rate_bpm > 120.0f) || (data.aqi > 200.0f && data.spo2_pct < 94.0f)) {
    return 2; // Riesgo Alto (Activar vibración local + Alerta BLE)
  } else if (data.aqi > 120.0f || data.co2_ppm > 1500.0f || data.heart_rate_bpm > 100.0f || data.temperature_c > 35.0f) {
    return 1; // Alerta Preventiva
  }
  return 0; // Estado Óptimo
}

SensorData current_telemetry;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("==================================================");
  Serial.println("   AuraSense Wearable Firmware - Booting System   ");
  Serial.println("   Hardware: ESP32-S3 Dual Core + BLE 5.0 + NPU   ");
  Serial.println("==================================================");
}

void loop() {
  // Simulación de lectura de bus I2C/SPI de sensores MEMS y Ópticos
  current_telemetry.aqi = random(40, 180);
  current_telemetry.co2_ppm = random(400, 1600);
  current_telemetry.temperature_c = random(24, 37) + random(0, 9) / 10.0f;
  current_telemetry.humidity_pct = random(40, 80);
  current_telemetry.noise_db = random(35, 85);
  current_telemetry.heart_rate_bpm = random(60, 110);
  current_telemetry.spo2_pct = random(93, 100);

  // Ejecutar Inferencia de IA Embebida
  uint8_t risk_level = predict_health_risk(current_telemetry);

  Serial.printf("[Telemetria] AQI: %.0f | CO2: %.0fppm | Temp: %.1fC | SpO2: %.0f%% | HR: %.0fbpm\n",
                current_telemetry.aqi, current_telemetry.co2_ppm, 
                current_telemetry.temperature_c, current_telemetry.spo2_pct, 
                current_telemetry.heart_rate_bpm);

  if (risk_level == 2) {
    Serial.println("⚠️ [AURASENSE EDGE AI] ALERTA CRÍTICA DETECTADA: Riesgo de crisis/exposición severa!");
  } else if (risk_level == 1) {
    Serial.println("⚡ [AURASENSE EDGE AI] PRECAUCIÓN: Calidad ambiental o estrés elevado.");
  } else {
    Serial.println("✅ [AURASENSE EDGE AI] Estado ambiental y biométrico normal.");
  }

  Serial.println("--------------------------------------------------");
  delay(3000);
}
