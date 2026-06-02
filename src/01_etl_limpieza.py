import pandas as pd
import os
from pathlib import Path
from pandas.api.types import is_numeric_dtype

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

# Rutas
ruta_dataset = BASE_DIR / "data" / "raw" / "Super_Store_data.csv"
ruta_processed = BASE_DIR / "data" / "processed"
ruta_salida = ruta_processed / "ventas_limpias.csv"

# Crear carpeta de salida
os.makedirs(ruta_processed, exist_ok=True)

# Verificar existencia del dataset
if not ruta_dataset.exists():
    raise FileNotFoundError(f"No se encontró el archivo: {ruta_dataset}")

# Cargar dataset
# Se usa latin1 porque el archivo puede contener caracteres especiales
df = pd.read_csv(ruta_dataset, encoding="latin1")

print("=" * 60)
print("ETL Y LIMPIEZA DE DATOS")
print("=" * 60)

print("\nDimensiones iniciales:")
print(df.shape)

print("\nColumnas originales:")
print(df.columns)

# Normalizar nombres de columnas
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.replace("/", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
    .str.replace("'", "", regex=False)
)

print("\nColumnas normalizadas:")
print(df.columns)

# Eliminar duplicados
duplicados_iniciales = df.duplicated().sum()
df = df.drop_duplicates()

print("\nDuplicados eliminados:")
print(duplicados_iniciales)

# Tratamiento de valores nulos
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

print("\nValores nulos después del tratamiento:")
print(df.isnull().sum())

# Convertir fechas
columnas_fecha = ["order_date", "ship_date"]

for col in columnas_fecha:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    else:
        raise ValueError(f"No se encontró la columna de fecha: {col}")

# Crear variables temporales
df["anio"] = df["order_date"].dt.year
df["mes"] = df["order_date"].dt.month
df["trimestre"] = df["order_date"].dt.quarter

# Crear variable de días de envío
df["dias_envio"] = (df["ship_date"] - df["order_date"]).dt.days

# Crear margen de utilidad
# Se evita división entre cero
df["margen_utilidad"] = df.apply(
    lambda row: row["profit"] / row["sales"] if row["sales"] != 0 else 0,
    axis=1
)

# Crear variable objetivo: venta no rentable
# 1 = venta con pérdida o utilidad cero
# 0 = venta rentable
df["venta_no_rentable"] = df["profit"].apply(
    lambda x: 1 if x <= 0 else 0
)

# Crear nivel de descuento
df["nivel_descuento"] = pd.cut(
    df["discount"],
    bins=[-0.01, 0.10, 0.30, 1.00],
    labels=["Bajo", "Medio", "Alto"]
)

# Crear nivel de rentabilidad
df["nivel_rentabilidad"] = pd.cut(
    df["margen_utilidad"],
    bins=[-float("inf"), 0, 0.15, 0.30, float("inf")],
    labels=["Perdida", "Baja", "Media", "Alta"]
)

# Reordenar columnas principales al inicio
columnas_principales = [
    "order_id",
    "order_date",
    "ship_date",
    "dias_envio",
    "ship_mode",
    "customer_id",
    "customer_name",
    "segment",
    "region",
    "state",
    "city",
    "category",
    "sub_category",
    "product_name",
    "sales",
    "quantity",
    "discount",
    "profit",
    "margen_utilidad",
    "nivel_descuento",
    "nivel_rentabilidad",
    "venta_no_rentable",
    "anio",
    "mes",
    "trimestre"
]

columnas_existentes = [col for col in columnas_principales if col in df.columns]
columnas_restantes = [col for col in df.columns if col not in columnas_existentes]

df = df[columnas_existentes + columnas_restantes]

# Guardar dataset limpio
df.to_csv(ruta_salida, index=False, encoding="utf-8")

print("\nETL finalizado correctamente.")
print("Archivo guardado en:", ruta_salida)

print("\nDimensiones finales:")
print(df.shape)

print("\nDistribución de ventas rentables y no rentables:")
print(df["venta_no_rentable"].value_counts())

print("\nDistribución porcentual de ventas rentables y no rentables:")
print(df["venta_no_rentable"].value_counts(normalize=True).round(4) * 100)

print("\nDistribución por nivel de descuento:")
print(df["nivel_descuento"].value_counts())

print("\nDistribución por nivel de rentabilidad:")
print(df["nivel_rentabilidad"].value_counts())

print("\nPrimeras filas:")
print(df.head())