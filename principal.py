import pandas as pd
from funciones import eficiencia_numpy, resumen_estadistico, guardar_resultado, cargar_resultado

# datos de ejemplo
df = pd.DataFrame({
    "planta": ["A", "A", "B"],
    "entrada": [200, 180, 220],
    "salida": [50, 60, 80]
})

# usar función modular con NumPy
df["eficiencia"] = eficiencia_numpy(df["entrada"], df["salida"])

print(df)

# análisis con SciPy
media, mediana, moda = resumen_estadistico(df["eficiencia"])
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# guardar resultado con Joblib
guardar_resultado(df, "resultado.pkl")

# cargar resultado
df_cargado = cargar_resultado("resultado.pkl")
print(df_cargado)