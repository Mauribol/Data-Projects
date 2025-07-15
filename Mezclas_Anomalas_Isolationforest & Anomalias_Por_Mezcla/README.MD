# Detección de Mezclas de Concreto Anómalas (Isolation Forest)

Este script detecta mezclas de concreto atípicas utilizando el modelo de machine learning no supervisado **Isolation Forest**.

## ⚙️ Flujo del proceso

1. Se cargan los datos de producción
2. Se seleccionan columnas clave de ingredientes
3. Se codifica la mezcla (`ID_MEZCLA`) con One-Hot Encoding
4. Se entrena un modelo `IsolationForest`
5. Se predicen y visualizan las mezclas anómalas

## 📁 Archivos

- `data/CONCRETERA 1.1.xlsx`: Datos históricos de producción
- `src/Proyecto1 Isolation forest.ipynb`: Script principal

## ▶️ Cómo ejecutar

```bash
python src/Proyecto1 Isolation forest.ipynb

# Detección de Anomalías por Tipo de Mezcla

Este script detecta mezclas anómalas de concreto **individualmente por tipo de mezcla**, usando el modelo `IsolationForest`.

## 🎯 Ventaja sobre modelos globales

Este enfoque entrena un modelo diferente para cada mezcla (`ID_MEZCLA`), logrando una mejor detección contextual.

## 🧪 Entradas

- `CANTIDAD_M3`
- `MAT005` a `MAT002` (componentes de la mezcla)
