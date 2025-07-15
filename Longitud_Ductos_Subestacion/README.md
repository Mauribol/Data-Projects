# Cálculo de Longitud de Ductos por Equipo – Subestación

Este script clasifica y suma la longitud de ductos para distintos equipos de una subestación eléctrica.

## Equipos analizados

- TRAFOS
- CUCHILLAS
- INTERRUPTORES
- BANCO 1T, 3T, 4T
- TRSP 8T

## 📁 Estructura

- `data/ductos_subestacion.xlsx`: Archivo original con los ductos
- `script/calcular_ductos.py`: Script principal
- `data/resumen_longitudes.xlsx`: Resultado exportado

## ⚙️ Requisitos

```txt
pandas
openpyxl
