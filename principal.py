# archivo principal

import pandas as pd
import matplotlib.pyplot as plt

# importar funciones del otro archivo
from funciones import *

# abrir excel
archivo = r"C:\Users\User\Desktop\IACC INGENIERIA\2. CIENCIA DE DATOS\8. SEMANA 8\TAREA SEMANA\CODIGO_TAREA\dataset_set_A_aguas_residuales.xlsx"

datos = pd.read_excel(archivo)

# usar funciones
datos = limpiar_datos(datos)

datos = calcular_eficiencia(datos)

promedio = promedio_plantas(datos)

print(promedio)

# grafico
promedio.plot(kind="bar")

plt.title("eficiencia de las plantas")
plt.ylabel("porcentaje")
plt.xlabel("plantas")

plt.show()