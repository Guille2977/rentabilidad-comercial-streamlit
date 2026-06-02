import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parents[1]

# Rutas
ruta_dataset = BASE_DIR / "data" / "processed" / "ventas_limpias.csv"
ruta_figuras = BASE_DIR / "reports" / "figuras"

# Crear carpeta para figuras
os.makedirs(ruta_figuras, exist_ok=True)

# Verificar existencia del dataset limpio
if not ruta_dataset.exists():
    raise FileNotFoundError(f"No se encontró el archivo limpio: {ruta_dataset}")

# Cargar dataset limpio
df = pd.read_csv(ruta_dataset)

print("=" * 60)
print("ANÁLISIS EXPLORATORIO DE DATOS - EDA")
print("=" * 60)

print("\nDimensiones del dataset:")
print(df.shape)

print("\nPrimeras filas:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nDistribución de ventas rentables y no rentables:")
print(df["venta_no_rentable"].value_counts())

print("\nDistribución porcentual:")
print(df["venta_no_rentable"].value_counts(normalize=True).round(4) * 100)

print("\nVentas totales:")
print(round(df["sales"].sum(), 2))

print("\nUtilidad total:")
print(round(df["profit"].sum(), 2))

print("\nMargen promedio:")
print(round(df["margen_utilidad"].mean(), 4))

print("\nDescuento promedio:")
print(round(df["discount"].mean(), 4))


# ==========================
# Gráfico 1: Distribución de rentabilidad
# ==========================

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="venta_no_rentable")
plt.title("Distribución de ventas rentables y no rentables")
plt.xlabel("Venta no rentable")
plt.ylabel("Cantidad de registros")
plt.xticks([0, 1], ["Rentable", "No rentable"])
plt.tight_layout()
plt.savefig(ruta_figuras / "01_distribucion_rentabilidad.png")
plt.close()


# ==========================
# Gráfico 2: Ventas por mes
# ==========================

ventas_mes = df.groupby(["anio", "mes"])["sales"].sum().reset_index()
ventas_mes["periodo"] = ventas_mes["anio"].astype(str) + "-" + ventas_mes["mes"].astype(str).str.zfill(2)

plt.figure(figsize=(12, 5))
sns.lineplot(data=ventas_mes, x="periodo", y="sales", marker="o")
plt.title("Ventas totales por mes")
plt.xlabel("Periodo")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(ruta_figuras / "02_ventas_por_mes.png")
plt.close()


# ==========================
# Gráfico 3: Utilidad por región
# ==========================

utilidad_region = df.groupby("region")["profit"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(7, 4))
sns.barplot(data=utilidad_region, x="region", y="profit")
plt.title("Utilidad total por región")
plt.xlabel("Región")
plt.ylabel("Utilidad")
plt.tight_layout()
plt.savefig(ruta_figuras / "03_utilidad_por_region.png")
plt.close()


# ==========================
# Gráfico 4: Utilidad por segmento
# ==========================

utilidad_segmento = df.groupby("segment")["profit"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(7, 4))
sns.barplot(data=utilidad_segmento, x="segment", y="profit")
plt.title("Utilidad total por segmento")
plt.xlabel("Segmento")
plt.ylabel("Utilidad")
plt.tight_layout()
plt.savefig(ruta_figuras / "04_utilidad_por_segmento.png")
plt.close()


# ==========================
# Gráfico 5: Utilidad por subcategoría
# ==========================

utilidad_subcategoria = df.groupby("sub_category")["profit"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8, 4))
sns.barplot(data=utilidad_subcategoria, x="sub_category", y="profit")
plt.title("Utilidad total por subcategoría")
plt.xlabel("Subcategoría")
plt.ylabel("Utilidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(ruta_figuras / "05_utilidad_por_subcategoria.png")
plt.close()


# ==========================
# Gráfico 6: Relación descuento vs utilidad
# ==========================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="discount",
    y="profit",
    hue="venta_no_rentable",
    alpha=0.7
)
plt.title("Relación entre descuento y utilidad")
plt.xlabel("Descuento")
plt.ylabel("Utilidad")
plt.tight_layout()
plt.savefig(ruta_figuras / "06_descuento_vs_utilidad.png")
plt.close()


# ==========================
# Gráfico 7: Top productos con mayor pérdida
# ==========================

productos_perdida = (
    df.groupby("product_name")["profit"]
    .sum()
    .sort_values()
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 5))
sns.barplot(data=productos_perdida, x="profit", y="product_name")
plt.title("Top 10 productos con mayor pérdida acumulada")
plt.xlabel("Utilidad")
plt.ylabel("Producto")
plt.tight_layout()
plt.savefig(ruta_figuras / "07_top_productos_perdida.png")
plt.close()


# ==========================
# Gráfico 8: Top productos con mayor ganancia
# ==========================

productos_ganancia = (
    df.groupby("product_name")["profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 5))
sns.barplot(data=productos_ganancia, x="profit", y="product_name")
plt.title("Top 10 productos con mayor ganancia acumulada")
plt.xlabel("Utilidad")
plt.ylabel("Producto")
plt.tight_layout()
plt.savefig(ruta_figuras / "08_top_productos_ganancia.png")
plt.close()


# ==========================
# Gráfico 9: Nivel de descuento
# ==========================

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="nivel_descuento")
plt.title("Distribución por nivel de descuento")
plt.xlabel("Nivel de descuento")
plt.ylabel("Cantidad de ventas")
plt.tight_layout()
plt.savefig(ruta_figuras / "09_nivel_descuento.png")
plt.close()


# ==========================
# Gráfico 10: Matriz de correlación
# ==========================

numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(10, 7))
sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Matriz de correlación de variables numéricas")
plt.tight_layout()
plt.savefig(ruta_figuras / "10_matriz_correlacion.png")
plt.close()


print("\nEDA finalizado correctamente.")
print("Figuras guardadas en:", ruta_figuras)

print("\nFiguras generadas:")
print("01_distribucion_rentabilidad.png")
print("02_ventas_por_mes.png")
print("03_utilidad_por_region.png")
print("04_utilidad_por_segmento.png")
print("05_utilidad_por_subcategoria.png")
print("06_descuento_vs_utilidad.png")
print("07_top_productos_perdida.png")
print("08_top_productos_ganancia.png")
print("09_nivel_descuento.png")
print("10_matriz_correlacion.png")