import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ==========================
# Configuración de página
# ==========================

st.set_page_config(
    page_title="Rentabilidad Comercial",
    page_icon="📊",
    layout="wide"
)

# ==========================
# Rutas
# ==========================

BASE_DIR = Path(__file__).resolve().parent

ruta_predicciones = BASE_DIR / "data" / "outputs" / "predicciones_rentabilidad.csv"

# ==========================
# Cargar datos
# ==========================

@st.cache_data
def cargar_datos():
    if not ruta_predicciones.exists():
        st.error("No se encontró el archivo de predicciones. Ejecuta primero los módulos de ETL, entrenamiento y predicción.")
        st.stop()

    df = pd.read_csv(ruta_predicciones)

    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    if "ship_date" in df.columns:
        df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

    return df


df = cargar_datos()

# ==========================
# Título
# ==========================

st.title("📊 Sistema de Análisis y Predicción de Rentabilidad Comercial")

st.markdown(
    """
    Esta aplicación permite analizar ventas de productos de mobiliario, evaluar indicadores comerciales
    y visualizar ventas con posible riesgo de pérdida mediante un modelo predictivo.
    """
)

# ==========================
# Sidebar - Filtros
# ==========================

st.sidebar.header("Filtros")

region_opciones = ["Todas"] + sorted(df["region"].dropna().unique().tolist())
segmento_opciones = ["Todos"] + sorted(df["segment"].dropna().unique().tolist())
subcategoria_opciones = ["Todas"] + sorted(df["sub_category"].dropna().unique().tolist())
riesgo_opciones = ["Todos"] + sorted(df["nivel_riesgo_comercial"].dropna().unique().tolist())

region = st.sidebar.selectbox("Región", region_opciones)
segmento = st.sidebar.selectbox("Segmento", segmento_opciones)
subcategoria = st.sidebar.selectbox("Subcategoría", subcategoria_opciones)
riesgo = st.sidebar.selectbox("Nivel de riesgo comercial", riesgo_opciones)

df_filtrado = df.copy()

if region != "Todas":
    df_filtrado = df_filtrado[df_filtrado["region"] == region]

if segmento != "Todos":
    df_filtrado = df_filtrado[df_filtrado["segment"] == segmento]

if subcategoria != "Todas":
    df_filtrado = df_filtrado[df_filtrado["sub_category"] == subcategoria]

if riesgo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["nivel_riesgo_comercial"] == riesgo]

# ==========================
# KPIs
# ==========================

st.subheader("Indicadores generales")

ventas_totales = df_filtrado["sales"].sum()
utilidad_total = df_filtrado["profit"].sum()
ordenes = df_filtrado["order_id"].nunique() if "order_id" in df_filtrado.columns else len(df_filtrado)
ventas_no_rentables = df_filtrado["venta_no_rentable"].sum()
porcentaje_no_rentable = (ventas_no_rentables / len(df_filtrado) * 100) if len(df_filtrado) > 0 else 0
descuento_promedio = df_filtrado["discount"].mean() if len(df_filtrado) > 0 else 0

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

col1.metric("Ventas totales", f"${ventas_totales:,.2f}")
col2.metric("Utilidad total", f"${utilidad_total:,.2f}")
col3.metric("Órdenes", f"{ordenes:,}")

col4.metric("Ventas no rentables", f"{int(ventas_no_rentables):,}")
col5.metric("% no rentables", f"{porcentaje_no_rentable:.2f}%")
col6.metric("Descuento promedio", f"{descuento_promedio:.2%}")

st.divider()

# ==========================
# Gráficos principales
# ==========================

st.subheader("Análisis visual")

col_a, col_b = st.columns(2)

with col_a:
    utilidad_region = (
        df_filtrado.groupby("region", as_index=False)["profit"]
        .sum()
        .sort_values(by="profit", ascending=False)
    )

    fig_region = px.bar(
        utilidad_region,
        x="region",
        y="profit",
        title="Utilidad por región",
        labels={"region": "Región", "profit": "Utilidad"}
    )

    st.plotly_chart(fig_region, use_container_width=True)

with col_b:
    utilidad_segmento = (
        df_filtrado.groupby("segment", as_index=False)["profit"]
        .sum()
        .sort_values(by="profit", ascending=False)
    )

    fig_segmento = px.bar(
        utilidad_segmento,
        x="segment",
        y="profit",
        title="Utilidad por segmento",
        labels={"segment": "Segmento", "profit": "Utilidad"}
    )

    st.plotly_chart(fig_segmento, use_container_width=True)

col_c, col_d = st.columns(2)

with col_c:
    utilidad_subcategoria = (
        df_filtrado.groupby("sub_category", as_index=False)["profit"]
        .sum()
        .sort_values(by="profit", ascending=False)
    )

    fig_subcategoria = px.bar(
        utilidad_subcategoria,
        x="sub_category",
        y="profit",
        title="Utilidad por subcategoría",
        labels={"sub_category": "Subcategoría", "profit": "Utilidad"}
    )

    st.plotly_chart(fig_subcategoria, use_container_width=True)

with col_d:
    riesgo_comercial = (
        df_filtrado["nivel_riesgo_comercial"]
        .value_counts()
        .reset_index()
    )

    riesgo_comercial.columns = ["nivel_riesgo_comercial", "cantidad"]

    fig_riesgo = px.pie(
        riesgo_comercial,
        names="nivel_riesgo_comercial",
        values="cantidad",
        title="Distribución de riesgo comercial"
    )

    st.plotly_chart(fig_riesgo, use_container_width=True)

# ==========================
# Ventas por mes
# ==========================

if "order_date" in df_filtrado.columns:
    st.subheader("Evolución mensual de ventas y utilidad")

    df_tiempo = df_filtrado.dropna(subset=["order_date"]).copy()
    df_tiempo["periodo"] = df_tiempo["order_date"].dt.to_period("M").astype(str)

    ventas_mes = (
        df_tiempo.groupby("periodo", as_index=False)[["sales", "profit"]]
        .sum()
        .sort_values(by="periodo")
    )

    fig_tiempo = px.line(
        ventas_mes,
        x="periodo",
        y=["sales", "profit"],
        markers=True,
        title="Ventas y utilidad por mes",
        labels={"periodo": "Periodo", "value": "Monto", "variable": "Indicador"}
    )

    st.plotly_chart(fig_tiempo, use_container_width=True)

# ==========================
# Relación descuento vs utilidad
# ==========================

st.subheader("Relación entre descuento y utilidad")

fig_descuento = px.scatter(
    df_filtrado,
    x="discount",
    y="profit",
    color="nivel_riesgo_comercial",
    hover_data=["product_name", "region", "segment", "sales", "quantity"],
    title="Descuento vs utilidad",
    labels={
        "discount": "Descuento",
        "profit": "Utilidad",
        "nivel_riesgo_comercial": "Nivel de riesgo"
    }
)

st.plotly_chart(fig_descuento, use_container_width=True)

# ==========================
# Ranking de riesgo
# ==========================

st.subheader("Top ventas con mayor riesgo de pérdida")

columnas_ranking = [
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
    "probabilidad_perdida",
    "nivel_riesgo_comercial"
]

columnas_existentes = [col for col in columnas_ranking if col in df_filtrado.columns]

ranking = (
    df_filtrado[columnas_existentes]
    .sort_values(by="probabilidad_perdida", ascending=False)
    .head(20)
)

st.dataframe(ranking, use_container_width=True)

# ==========================
# Tabla general
# ==========================

with st.expander("Ver datos filtrados"):
    st.dataframe(df_filtrado, use_container_width=True)

# ==========================
# Conclusiones automáticas simples
# ==========================

st.subheader("Conclusiones generales")

if len(df_filtrado) > 0:
    region_mayor_utilidad = df_filtrado.groupby("region")["profit"].sum().idxmax()
    subcategoria_mayor_perdida = df_filtrado.groupby("sub_category")["profit"].sum().idxmin()
    riesgo_alto = (df_filtrado["nivel_riesgo_comercial"] == "Alto").sum()

    st.markdown(f"""
    - La región con mayor utilidad en los datos filtrados es **{region_mayor_utilidad}**.
    - La subcategoría con menor utilidad acumulada es **{subcategoria_mayor_perdida}**.
    - Se identificaron **{riesgo_alto}** registros con nivel de riesgo comercial alto.
    - El porcentaje de ventas no rentables en el conjunto filtrado es **{porcentaje_no_rentable:.2f}%**.
    """)
else:
    st.warning("No hay datos disponibles con los filtros seleccionados.")