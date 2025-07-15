PROGRAMA DE CABLEADO

import pandas as pd

 

# Clase para clasificar el cableado por equipo

class Bahia:

    def __init__(self, df_bahia):

        self.df_bahia = df_bahia.copy()  # Evitar modificar el original

 

    def clasificar_equipo(self, color, nombre_equipo):

        """ Filtra por color y asigna nombres a los equipos """

        df_filtrado = self.df_bahia[self.df_bahia["Color"] == color].copy()

        df_filtrado = df_filtrado.rename(columns={"Capa": "Bahia", "Color": "Equipo"})

        df_filtrado["Equipo"] = df_filtrado.index.to_series().apply(lambda x: f"{nombre_equipo} {x+1}")

        return df_filtrado

 

    def trafo_ins(self):

        return self.clasificar_equipo("rojo", "Trafo")

 

    def cuchilla(self):

        return self.clasificar_equipo("amarillo", "Cuchilla")

 

    def interruptor(self):

        return self.clasificar_equipo("verde", "Interruptor")

 

 

# Clase para calcular cantidad de equipos y longitud de cableado

class Cableado:

    def __init__(self, df_eq):

        self.df_eq = df_eq

 

    def cant_eq(self):

        """ Cuenta la cantidad de equipos """

        return len(self.df_eq)

 

    def cableado(self):

        """ Calcula la longitud total del cableado """

        return self.df_eq["Longitud"].sum()

 

# Cargar el DataFrame general

df_gral = xl("A1:E3813", headers=True)

 

# Filtrar las bahías específicas

df_bahias = df_gral[df_gral["Capa"].isin(["A SE AXTLA", "A SE VALLES"])].drop(columns=["Total", "Nombre"])

 

# Crear objetos por bahía

bahia_axt = Bahia(df_bahia=df_bahias[df_bahias["Capa"] == "A SE AXTLA"])

 

# Obtener DataFrames clasificados

df_trafo = bahia_axt.trafo_ins()

df_cuchilla = bahia_axt.cuchilla()

df_interruptor = bahia_axt.interruptor()

 

# Mostrar resultados

print("Cantidad de equipos por tipo:")

print(f"Trafos: {Cableado(df_trafo).cant_eq()}")

print(f"Cuchillas: {Cableado(df_cuchilla).cant_eq()}")

print(f"Interruptores: {Cableado(df_interruptor).cant_eq()}")

 

print("\nLongitud total de cableado por tipo:")

print(f"Trafos: {Cableado(df_trafo).cableado()} m")

print(f"Cuchillas: {Cableado(df_cuchilla).cableado()} m")

print(f"Interruptores: {Cableado(df_interruptor).cableado()} m")
