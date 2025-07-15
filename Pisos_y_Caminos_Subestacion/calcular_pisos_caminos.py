Programa de pisos y caminos

# Creación del dataframe general

df_tabla = xl("Tabla1[#Todo]", headers=True).drop(columns=["Total", "Nombre"])

 

# Creación del filtro con `isin()`

categorias_pyc = [

    "CAMINO DE ASFALTO", "CAMINO DE CONCRETO", "DEMOLICION ASFALTO",

    "DESPLAME", "PISO DE CONCRETO", "PISO DE GRAVA", "RETIRO GRAVA"

]

df_pyc = df_tabla[df_tabla["Capa"].isin(categorias_pyc)].sort_values(by="Capa")

 

# Creación de DataFrames separados usando un diccionario

dfs_pyc = {capa: df_pyc[df_pyc["Capa"] == capa] for capa in categorias_pyc}

 

# Cálculo de áreas por tipo

area_totales = {capa: df["Área"].sum() for capa, df in dfs_pyc.items()}

 

# Mostrar resultados

print(area_totales)
