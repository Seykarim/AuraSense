import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def generate_synthetic_data(samples=2000):
    np.random.seed(42)
    
    # Variables de Entorno
    aqi = np.random.uniform(10, 300, samples)            # AQI (0-500)
    co2 = np.random.uniform(400, 2500, samples)          # ppm
    temp = np.random.uniform(15, 42, samples)            # °C
    humidity = np.random.uniform(20, 95, samples)        # %
    noise = np.random.uniform(30, 100, samples)          # dB
    
    # Variables Biométricas
    hr = np.random.uniform(50, 160, samples)             # BPM
    spo2 = np.random.uniform(85, 100, samples)           # %
    
    # Regla Lógica de Riesgo (Ground Truth para Entrenamiento de IA)
    # Risk 0: Normal | Risk 1: Alerta Ambiental/Estrés | Risk 2: Riesgo Severo (Asma/Golpe de Calor)
    risk = []
    for i in range(samples):
        if spo2[i] < 90 or (temp[i] > 38 and hr[i] > 120) or (aqi[i] > 200 and spo2[i] < 94):
            risk.append(2) # Riesgo Severo
        elif aqi[i] > 120 or co2[i] > 1500 or hr[i] > 100 or temp[i] > 35:
            risk.append(1) # Riesgo Moderado
        else:
            risk.append(0) # Normal
            
    df = pd.DataFrame({
        'aqi': aqi, 'co2': co2, 'temp': temp, 'humidity': humidity,
        'noise': noise, 'hr': hr, 'spo2': spo2, 'risk': risk
    })
    return df

def main():
    print("🧠 AuraSense Edge AI - Entrenando Modelo de Predicción de Riesgo...")
    df = generate_synthetic_data()
    
    X = df.drop('risk', axis=1)
    y = df['risk']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    clf = RandomForestClassifier(n_estimators=10, max_depth=5, random_state=42)
    clf.fit(X_train, y_train)
    
    acc = clf.score(X_test, y_test)
    print(f"✅ Exactitud del Modelo Evaluado: {acc * 100:.2f}%\n")
    print(classification_report(y_test, clf.predict(X_test)))

    # Guardar resumen de reglas exportables a C++
    with open("edge_ai/model_summary.txt", "w") as f:
        f.write(f"AuraSense Edge AI Model\nAccuracy: {acc*100:.2f}%\nNum Features: {X.shape[1]}\n")
    print("💾 Resumen guardado en edge_ai/model_summary.txt")

if __name__ == "__main__":
    main()
