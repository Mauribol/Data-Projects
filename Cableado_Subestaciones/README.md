# Clasificación de Cableado en Subestaciones

Este proyecto analiza el cableado de subestaciones eléctricas a partir de colores en el plano y calcula la longitud total por equipo.

## Lógica de clasificación

- 🔴 Rojo → Transformadores
- 🟡 Amarillo → Cuchillas
- 🟢 Verde → Interruptores

## Cómo ejecutar

1. Asegúrate de tener un archivo con columnas: `Capa`, `Color`, `Longitud`, etc.
2. Coloca el archivo en `data/` y actualiza el nombre en el script.
3. Ejecuta:

```bash
python src/cableado.py
