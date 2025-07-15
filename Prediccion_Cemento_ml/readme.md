# Predicción de Uso de Cemento por Mezcla (ML)

Este modelo predice cuántos kilogramos de cemento (MAT005) se deben usar por mezcla, utilizando regresión lineal entrenada con datos históricos de producción.

## 📁 Archivos

- `data/CONCRETERA 1.1.xlsx`: Archivo original con datos de producción
- `src/Proyecto1 Predecir.ipynb`: Script principal
- `data/PROYECTO1_limpio.xlsx`: Dataset procesado

## 📊 Proceso

1. Limpieza y selección de variables
2. Codificación de mezcla (`ID_MEZCLA`)
3. Entrenamiento con `LinearRegression`
4. Evaluación con MAE y R²
5. Visualización de predicciones

## ⚙️ Requisitos

```bash
pip install -r requirements.txt
