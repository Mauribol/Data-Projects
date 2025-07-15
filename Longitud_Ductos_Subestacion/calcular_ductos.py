#programa calculo de lingitudes de ductos

 

import pandas as pd

 

# Cargar DataFrame

df_ductos = xl("A1:C2637", headers=True).drop(columns=["Nombre"])

 

# Lista de tipos de ducto

tipos_ductos = ["TRAFOS", "CUCHILLAS", "INTERRUPTORES", "BANCO 1T", "BANCO 4T", "BANCO 3T", "TRSP 8T"]

 

# Filtrar solo los tipos de ductos requeridos

df_ductos = df_ductos[df_ductos["Capa"].isin(tipos_ductos)]

 

# Convertir longitudes de mm a metros

df_ductos["Longitud"] /= 1000

 

# Crear diccionario de DataFrames por tipo de ducto

dfs_ductos = {tipo: df_ductos[df_ductos["Capa"] == tipo] for tipo in tipos_ductos}

 

# Calcular la suma de longitudes por tipo de ducto

longitudes_totales = df_ductos.groupby("Capa")["Longitud"].sum().to_dict()

 

# Mostrar resultados

print(pd.DataFrame(list(longitudes_totales.items()), columns=["Capa", "Total Longitud (m)"]))
