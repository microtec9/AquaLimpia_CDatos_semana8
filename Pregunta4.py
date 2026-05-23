# archivo funciones.py

import pandas as pd

# limpiar datos vacios
def limpiar(df):

    datos_limpios = df.dropna()

    return datos_limpios


# calcular eficiencia
def eficiencia(df):

    df["ef"] = (
        (df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"])
        / df["DBO_entrada_mg_L"]
    ) * 100

    return df


# promedio por planta
def promedio(df):

    prom = df.groupby("planta")["ef"].mean()

    return prom