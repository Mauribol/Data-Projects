#PROGRAMA PARA CLASIFICAR ESTRUCTURAS

 

import pandas as pd

import os

import matplotlib.pyplot as plt

 

# Obtener la ruta absoluta de los archivos de Excel

archivo1 = os.path.abspath("lt cha gue.xlsx")

archivo2 = os.path.abspath("lt gue reg.xlsx")

 

# Cargar los datos en DataFrames

dfch_gu = pd.read_excel(archivo1, sheet_name="database 2")

dfgu_re = pd.read_excel(archivo2, sheet_name="database 1")

 

# Revisar las columnas del DataFrame

print("Columnas antes de limpiar:", dfch_gu.columns)

 

# Eliminar columnas innecesarias si existen

columnas_a_eliminar = ["Columna1", "Columna2", "Columna3", "OBSERVACIONES",

                        "No. De torres sin montar", "No. DE TORRE",

                        "No. consecutivos de torres montadas", "No. DE TORRES A DESMANTELAR"]

 

dfch_gu = dfch_gu.drop(columns=[col for col in columnas_a_eliminar if col in dfch_gu.columns], errors="ignore")

 

print("Columnas después de limpiar:", dfch_gu.columns)

 

# Rellenar espacios vacíos con 0

dfch_gu = dfch_gu.fillna(0)

 

# Convertir columnas a numéricas donde sea posible

cols_numericas = dfch_gu.columns[dfch_gu.columns != "TIPO Y NIVEL DE\nLAS ESTRUCTURAS"]

dfch_gu[cols_numericas] = dfch_gu[cols_numericas].apply(pd.to_numeric, errors="coerce")

dfch_gu = dfch_gu.fillna(1)  # Reemplazar valores NaN por 1

 

# Obtener tipos únicos de torres

torres = dfch_gu["TIPO Y NIVEL DE\nLAS ESTRUCTURAS"].unique()

 

# Crear un DataFrame para almacenar los resultados agrupados

df_r_cg = pd.DataFrame({"TIPO Y NIVEL DE\nLAS ESTRUCTURAS": torres})

 

# Agrupar por tipo de torre y sumar valores numéricos

grupo = dfch_gu.groupby("TIPO Y NIVEL DE\nLAS ESTRUCTURAS").sum(numeric_only=True).reset_index()

 

# Unir los resultados al nuevo DataFrame

df_r_cg = df_r_cg.merge(grupo, on="TIPO Y NIVEL DE\nLAS ESTRUCTURAS", how="left")

 

# Guardar los resultados en un archivo de Excel

df_r_cg.to_excel("equipo_montado_cha_gue.xlsx", index=False)

 

print("✅ Archivo 'equipo_montado_cha_gue.xlsx' guardado correctamente.")

