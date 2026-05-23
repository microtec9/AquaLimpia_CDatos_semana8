# Pregunta 1.1
# funciones.py
# Archivo con funciones reutilizables para AquaLimpia S.A.

import pandas as pd
import numpy as np
from scipy import stats

def calcular_eficiencia(df):
    """Calcula eficiencia de tratamiento por cada registro"""
    return ((df["DBO_entrada_mg_L"] - df["DBO_salida_mg_L"]) / df["DBO_entrada_mg_L"]) * 100

def calcular_promedios_por_planta(df):
    """Calcula promedios de todas las variables por planta"""
    eficiencia = df.groupby("planta")["eficiencia"].mean()
    caudal = df.groupby("planta")["caudal_entrada_m3_d"].mean()
    energia = df.groupby("planta")["energia_aeracion_kWh"].mean()
    lodos = df.groupby("planta")["lodos_generados_kg_d"].mean()
    return eficiencia, caudal, energia, lodos

def correlacion_variables(df):
    """Calcula correlación entre caudal y eficiencia usando SciPy"""
    correlacion, p_valor = stats.pearsonr(df["caudal_entrada_m3_d"], df["eficiencia"])
    return correlacion, p_valor

def analisis_calidad_datos(df):
    """Analiza la calidad de los datos"""
    print(f"Total de registros: {len(df)}")
    print(f"Total de columnas: {len(df.columns)}")
    print("\nValores nulos por columna:")
    print(df.isnull().sum())
    print("\nTipos de datos:")
    print(df.dtypes)