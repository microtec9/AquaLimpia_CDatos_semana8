# SEMANA 8 - TAREA - PREGUNTA 1.1
import pandas as pd
import matplotlib.pyplot as plt

# aqui abrimos el archivo excel de la semana
archivo = r"C:\Users\User\Desktop\IACC INGENIERIA\2. CIENCIA DE DATOS\8. SEMANA 8\TAREA SEMANA\CODIGO_TAREA\dataset_set_A_aguas_residuales.xlsx"

datos = pd.read_excel(archivo)

# borrar datos vacios por si acaso
datos = datos.dropna()

print("datos cargados")
print(datos.head())

# sacar eficiencia de tratamiento
datos["ef"] = (
    (datos["DBO_entrada_mg_L"] - datos["DBO_salida_mg_L"])
    / datos["DBO_entrada_mg_L"]
) * 100

# promedio de eficiencia
promedio = datos.groupby("planta")["ef"].mean()

print("\npromedio por planta")
print(promedio)

# hacer grafico
promedio.plot(kind="bar")

plt.title("eficiencia de las plantas")
plt.ylabel("porcentaje")
plt.xlabel("plantas")

plt.show()