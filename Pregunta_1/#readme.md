# Proyecto AquaLimpia S.A. - Análisis de Aguas Residuales

**Estudiante:** Oscar Ortega Morales
**Asignatura:** Ciencia de Datos - Semana 8
**Fecha:** 25-05-2026

## Objetivo del Proyecto

Analizar el comportamiento de las plantas de tratamiento de AquaLimpia S.A. para identificar patrones en la eficiencia de remoción de DBO y su relación con caudal, consumo energético y generación de lodos.

## Preguntas de Investigación

1. ¿Qué planta tiene mayor eficiencia de tratamiento?
2. ¿Existe correlación entre el caudal de entrada y la eficiencia?
3. ¿Cómo se comportan el consumo energético y la generación de lodos por planta?

## Datos Utilizados

- **Fuente:** dataset_set_A_aguas_residuales.xlsx
- **Registros:** 200
- **Plantas:** Centro, Norte, Sur
- **Variables:** caudal, DBO entrada/salida, energía, lodos, cumplimiento normativo

## Metodología

1. Carga y limpieza de datos
2. Análisis de calidad de datos (nulos, tipos)
3. Cálculo de eficiencia de tratamiento
4. Cálculo de promedios por planta
5. Correlación entre variables (Pearson)
6. Generación de dashboard con 4 gráficos
7. Exportación de reportes por área

## Resultados Obtenidos

| Planta | Eficiencia (%) | Caudal (m3/d) | Energía (kWh) | Lodos (kg/d) |
|--------|---------------|---------------|---------------|---------------|
| Centro | 87.51 | 5112.72 | 1260.85 | 433.01 |
| Norte | 86.65 | 5287.87 | 1299.31 | 450.47 |
| Sur | 87.10 | 4684.52 | 1193.78 | 394.44 |

**Correlación caudal-eficiencia:** -0.1228 (No significativa, p=0.0833)

## Dashboard

El dashboard generado muestra 4 gráficos de barras comparativos entre plantas:
- Eficiencia de tratamiento (%)
- Caudal de entrada (m3/d)
- Consumo de energía en aeración (kWh)
- Lodos generados (kg/d)

## Reportes Entregables

| Área | Archivo | Contenido |
|------|---------|-----------|
| Operaciones | reporte_operaciones.csv | fecha, planta, caudal, DBO entrada/salida, energía, lodos, eficiencia |
| Gestión Ambiental | reporte_ambiental.csv | fecha, planta, DBO salida, cumplimiento normativo, estado |

## Reflexión

Se identificó que las tres plantas tienen eficiencias similares (86-88%), sin una diferencia significativa. No existe correlación entre caudal y eficiencia, lo que sugiere que otros factores (como carga contaminante o mantenimiento) podrían explicar los incumplimientos. Se recomienda analizar DBO de entrada y pH en futuras iteraciones.

## Trabajo Colaborativo

El proyecto se gestionó con Git, realizando commits periódicos. Repositorio disponible en:
[https://github.com/microtec9/Aqualimpia_CDatos_semana8](https://github.com/microtec9/Aqualimpia_CDatos_semana8)

## Librerías Utilizadas

- pandas (2.0.3)
- numpy (1.24.3)
- matplotlib (3.7.1)
- scipy (1.10.1)

## Cómo Ejecutar

```bash
pip install pandas numpy matplotlib scipy
python Preg_1.1.py