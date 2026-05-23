# archivo: funciones.py

import pandas as pd

# funcion para limpiar datos
def limpiar_datos(df):
    df = df.dropna()
    return df

# funcion para calcular eficiencia
def calcular_eficiencia(df):

    df["ef"] = (
        (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"])
        / df["DBO_entrada_mg_L"]
    ) * 100

    return df

# funcion para sacar promedio por planta
def promedio_plantas(df):

    prom = df.groupby("planta")["ef"].mean()

    return prom