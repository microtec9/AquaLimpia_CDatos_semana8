# SEMANA 8 - TAREA - PREGUNTA 1.1
# SCRIPT PRINCIPAL - OSCAR ORTEGA MORALES
# AQUALIMPIA S.A.

import pandas as pd
import matplotlib.pyplot as plt

# Importar funciones desde archivo externo (modular)
from funciones import calcular_eficiencia, calcular_promedios_por_planta, correlacion_variables, analisis_calidad_datos

# ============================================
# 1. CARGA DE DATOS
# ============================================

archivo = r"C:\Users\User\Desktop\IACC INGENIERIA\2. CIENCIA DE DATOS\8. SEMANA 8\TAREA SEMANA\CODIGO_TAREA\dataset_set_A_aguas_residuales.xlsx"

datos = pd.read_excel(archivo)

print("="*60)
print("DASHBOARD EXPLORATORIO - AQUALIMPIA S.A.")
print("="*60)

# ============================================
# 2. ANÁLISIS DE CALIDAD DE DATOS (función importada)
# ============================================

print("\n1. ANALISIS DE CALIDAD DE DATOS")
print("-"*40)
analisis_calidad_datos(datos)

# ============================================
# 3. LIMPIEZA DE DATOS
# ============================================

# Separar columna energía/lodos (están juntas en algunos datasets)
if "energia_aeracion_kWh/lodos_generados_kg_d" in datos.columns:
    datos[["energia_aeracion_kWh", "lodos_generados_kg_d"]] = datos["energia_aeracion_kWh/lodos_generados_kg_d"].str.split("/", expand=True)
    datos["energia_aeracion_kWh"] = pd.to_numeric(datos["energia_aeracion_kWh"])
    datos["lodos_generados_kg_d"] = pd.to_numeric(datos["lodos_generados_kg_d"])

# Eliminar filas con valores nulos
datos_original = len(datos)
datos = datos.dropna()
print(f"\nFilas eliminadas por nulos: {datos_original - len(datos)}")
print(f"Filas finales: {len(datos)}")

# ============================================
# 4. CÁLCULOS PRINCIPALES (usando funciones)
# ============================================

# Calcular eficiencia (función importada)
datos["eficiencia"] = calcular_eficiencia(datos)

# Calcular promedios por planta (función importada)
eficiencia_prom, caudal_prom, energia_prom, lodos_prom = calcular_promedios_por_planta(datos)

# Correlación entre caudal y eficiencia (función importada)
corr, p_valor = correlacion_variables(datos)

# ============================================
# 5. RESULTADOS EN CONSOLA
# ============================================

print("\n2. RESULTADOS POR PLANTA")
print("-"*40)
print("\nPROMEDIO DE EFICIENCIA (%):")
print(eficiencia_prom.round(2))
print("\nPROMEDIO DE CAUDAL (m3/d):")
print(caudal_prom.round(2))
print("\nPROMEDIO DE ENERGIA (kWh):")
print(energia_prom.round(2))
print("\nPROMEDIO DE LODOS (kg/d):")
print(lodos_prom.round(2))

print("\n3. CORRELACIONES")
print("-"*40)
print(f"Correlación entre caudal y eficiencia: {corr:.4f}")
print(f"Valor p: {p_valor:.4f}")
if p_valor < 0.05:
    print("→ Existe correlación significativa")
else:
    print("→ No existe correlación significativa")

# ============================================
# 6. DASHBOARD EXPLORATORIO (4 gráficos en una ventana)
# ============================================

print("\n4. GENERANDO DASHBOARD...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("DASHBOARD EXPLORATORIO - PLANTAS DE TRATAMIENTO", fontsize=16, fontweight='bold')

# Gráfico 1: Eficiencia
axes[0,0].bar(eficiencia_prom.index, eficiencia_prom.values, color='green')
axes[0,0].set_title("Eficiencia de Tratamiento", fontsize=12)
axes[0,0].set_ylabel("Porcentaje (%)")
axes[0,0].set_ylim(80, 100)
axes[0,0].grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(eficiencia_prom.values):
    axes[0,0].text(i, v + 0.5, f"{v:.1f}%", ha='center', fontsize=9)

# Gráfico 2: Caudal
axes[0,1].bar(caudal_prom.index, caudal_prom.values, color='blue')
axes[0,1].set_title("Caudal de Entrada", fontsize=12)
axes[0,1].set_ylabel("Caudal (m3/d)")
axes[0,1].grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(caudal_prom.values):
    axes[0,1].text(i, v + 100, f"{v:.0f}", ha='center', fontsize=9)

# Gráfico 3: Energía
axes[1,0].bar(energia_prom.index, energia_prom.values, color='orange')
axes[1,0].set_title("Consumo de Energía en Aeración", fontsize=12)
axes[1,0].set_ylabel("Energía (kWh)")
axes[1,0].grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(energia_prom.values):
    axes[1,0].text(i, v + 10, f"{v:.0f}", ha='center', fontsize=9)

# Gráfico 4: Lodos
axes[1,1].bar(lodos_prom.index, lodos_prom.values, color='brown')
axes[1,1].set_title("Lodos Generados", fontsize=12)
axes[1,1].set_ylabel("Lodos (kg/d)")
axes[1,1].grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(lodos_prom.values):
    axes[1,1].text(i, v + 10, f"{v:.0f}", ha='center', fontsize=9)

plt.tight_layout()
plt.show()

# ============================================
# 7. EXPORTAR REPORTES PARA CADA ÁREA
# ============================================

print("\n5. EXPORTANDO REPORTES...")

# Reporte para Área de Operaciones
reporte_operaciones = datos[["fecha_registro", "planta", "caudal_entrada_m3_d", 
                              "DBO_entrada_mg_L", "DBO_salida_mg_L", 
                              "energia_aeracion_kWh", "lodos_generados_kg_d", "eficiencia"]]
reporte_operaciones.to_csv("reporte_operaciones.csv", index=False, encoding='utf-8-sig')
print("✓ Reporte de Operaciones guardado: reporte_operaciones.csv")

# Reporte para Área de Gestión Ambiental
reporte_ambiental = datos[["fecha_registro", "planta", "DBO_salida_mg_L", "cumplimiento_norma"]]
reporte_ambiental["estado_normativo"] = reporte_ambiental["cumplimiento_norma"].apply(
    lambda x: "CUMPLE" if x == 1 else "NO CUMPLE"
)
reporte_ambiental.to_csv("reporte_ambiental.csv", index=False, encoding='utf-8-sig')
print("✓ Reporte de Gestión Ambiental guardado: reporte_ambiental.csv")

# ============================================
# 8. RESUMEN FINAL
# ============================================

print("\n" + "="*60)
print("RESUMEN EJECUTIVO")
print("="*60)
print(f"✓ Total de plantas analizadas: {datos['planta'].nunique()}")
print(f"✓ Período de análisis: {datos['fecha_registro'].min()} al {datos['fecha_registro'].max()}")
print(f"✓ Planta con mayor eficiencia: {eficiencia_prom.idxmax()} ({eficiencia_prom.max():.2f}%)")
print(f"✓ Planta con menor eficiencia: {eficiencia_prom.idxmin()} ({eficiencia_prom.min():.2f}%)")
print("\n✓ Reportes generados para Operaciones y Gestión Ambiental")
print("="*60)