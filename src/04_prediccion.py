import pandas as pd
import joblib
import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

# Rutas
ruta_dataset = BASE_DIR / "data" / "processed" / "ventas_limpias.csv"
ruta_modelo = BASE_DIR / "models" / "modelo_rentabilidad.pkl"
ruta_outputs = BASE_DIR / "data" / "outputs"
ruta_predicciones = ruta_outputs / "predicciones_rentabilidad.csv"

# Crear carpeta de salida
os.makedirs(ruta_outputs, exist_ok=True)

# Verificar archivos necesarios
if not ruta_dataset.exists():
    raise FileNotFoundError(f"No se encontró el dataset limpio: {ruta_dataset}")

if not ruta_modelo.exists():
    raise FileNotFoundError(f"No se encontró el modelo entrenado: {ruta_modelo}")

# Cargar datos y modelo
df = pd.read_csv(ruta_dataset)
modelo = joblib.load(ruta_modelo)

print("=" * 60)
print("GENERACIÓN DE PREDICCIONES DE RENTABILIDAD")
print("=" * 60)

print("\nDimensiones del dataset:")
print(df.shape)

# Variables utilizadas en el entrenamiento
features = [
    "ship_mode",
    "segment",
    "region",
    "sub_category",
    "sales",
    "quantity",
    "discount",
    "dias_envio",
    "anio",
    "mes",
    "trimestre"
]

# Validar columnas necesarias
columnas_faltantes = [col for col in features if col not in df.columns]

if columnas_faltantes:
    raise ValueError(f"Faltan columnas necesarias para generar predicciones: {columnas_faltantes}")

# Separar variables predictoras
X = df[features]

# Generar predicción y probabilidad
df["prediccion_perdida"] = modelo.predict(X)
df["probabilidad_perdida"] = modelo.predict_proba(X)[:, 1]

# Crear etiqueta interpretativa de riesgo comercial
df["nivel_riesgo_comercial"] = pd.cut(
    df["probabilidad_perdida"],
    bins=[0, 0.4, 0.7, 1],
    labels=["Bajo", "Medio", "Alto"],
    include_lowest=True
)

# Ordenar de mayor a menor riesgo
df_ranking = df.sort_values(by="probabilidad_perdida", ascending=False)

# Guardar archivo final
df_ranking.to_csv(ruta_predicciones, index=False, encoding="utf-8")

print("\nPredicciones generadas correctamente.")
print("Archivo guardado en:")
print(ruta_predicciones)

print("\nTop 15 ventas con mayor riesgo de pérdida:")
columnas_mostrar = [
    "order_id",
    "customer_id",
    "segment",
    "region",
    "sub_category",
    "product_name",
    "sales",
    "quantity",
    "discount",
    "profit",
    "venta_no_rentable",
    "prediccion_perdida",
    "probabilidad_perdida",
    "nivel_riesgo_comercial"
]

columnas_existentes = [col for col in columnas_mostrar if col in df_ranking.columns]

print(df_ranking[columnas_existentes].head(15))

print("\nDistribución de niveles de riesgo comercial:")
print(df_ranking["nivel_riesgo_comercial"].value_counts())

print("\nDistribución de predicción de pérdida:")
print(df_ranking["prediccion_perdida"].value_counts())

print("\nPredicción finalizada correctamente.")