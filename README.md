AuraSense — Wearable Ambiental & Salud con IA Predictiva Embebida

[![Hardware](https://img.shields.io/badge/Hardware-ESP32--S3%20%2F%20NRF52840-red.svg)](#hardware)
[![Edge AI](https://img.shields.io/badge/Edge%20AI-TinyML%20%2F%20Scikit--Learn-green.svg)](#edge-ai)
[![Connectivity](https://img.shields.io/badge/BLE-Bluetooth%205.0%20Low%20Energy-blue.svg)](#conectividad)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AuraSense** es un ecosistema wearable ultracompacto (tipo pin, colgante o pulsera) que integra captura multivariable en tiempo real de exposición ambiental y parámetros fisiológicos. Mediante modelos de **IA Embebida (Edge AI)**, anticipa riesgos de salud como crisis de asma, deshidratación, migrañas por fatiga y estrés térmico sin depender de conectividad a la nube.

---

## 🌟 Características Clave

- **Monitoreo Ambiental Integrado:** Medición de calidad del aire (AQI, CO2, COV), temperatura, humedad y niveles de contaminación acústica.
- **Biometría Continua:** Oximetría de pulso ($SpO_2$), frecuencia cardíaca y temperatura corporal cutánea.
- **Inferencia Local (Edge AI):** Clasificación predictiva de riesgo ejecutada directamente en la NPU del microcontrolador.
- **Alertas Hápticas e Interfaz Móvil:** Notificaciones por vibración discreta y sincronización vía Bluetooth Low Energy (BLE).
- **Enfoque Colaborativo:** Datos anónimos listos para alimentar mapas comunitarios de salud ambiental urbana.

---

## 📁 Estructura del Repositorio

```text
AuraSense/
├── README.md
├── LICENSE
├── .gitignore
├── firmware/
│   ├── src/
│   │   └── main.cpp
│   └── platformio.ini
├── edge_ai/
│   ├── train_model.py
│   ├── requirements.txt
│   └── model_summary.txt
├── mobile_app/
│   └── mock_ble_receiver.py
└── docs/
    ├── architecture.md
    └── hardware_bom.md
