import numpy as np
from scipy import stats
from joblib import dump, load

# función con NumPy: cálculo de eficiencia promedio
def eficiencia_numpy(entrada, salida):
    entrada = np.array(entrada)
    salida = np.array(salida)

    ef = (entrada - salida) / entrada * 100
    return ef

# función con SciPy: estadística básica
def resumen_estadistico(data):
    media = np.mean(data)
    mediana = np.median(data)
    moda = stats.mode(data, keepdims=True).mode[0]

    return media, mediana, moda

# guardar resultados con Joblib
def guardar_resultado(obj, nombre_archivo):
    dump(obj, nombre_archivo)

# cargar resultados con Joblib
def cargar_resultado(nombre_archivo):
    return load(nombre_archivo)