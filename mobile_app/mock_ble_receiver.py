import time
import random

def main():
    print("📱 AuraSense Mobile App Client - Simulador de Consola BLE")
    print("Conectando con AuraSense Wearable via Bluetooth Low Energy...\n")
    time.sleep(1)
    print("✅ Dispositivo vinculado: AuraSense-A78C (RSSI: -58 dBm)\n")

    try:
        while True:
            aqi = random.randint(30, 220)
            spo2 = random.randint(88, 99)
            hr = random.randint(65, 125)
            
            # Evaluación local
            if spo2 < 90 or aqi > 200:
                risk_status = "🔴 ALERTA ROJA: Usar mascarilla / Salir del área"
            elif aqi > 120:
                risk_status = "🟡 PRECAUCIÓN: Mala calidad de aire detectada"
            else:
                risk_status = "🟢 ZONA SEGURA: Parámetros dentro del rango"

            print(f"[{time.strftime('%H:%M:%S')}] Telemetría -> AQI: {aqi} | SpO2: {spo2}% | Pulso: {hr} BPM")
            print(f"  └─ Estado AI: {risk_status}\n")
            time.sleep(2.5)
    except KeyboardInterrupt:
        print("\nDesconectado de AuraSense.")

if __name__ == "__main__":
    main()
