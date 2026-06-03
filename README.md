# Sistema de Análisis y Predicción de Rentabilidad Comercial con Streamlit

## Descripción del proyecto

Este proyecto desarrolla una solución de analítica comercial utilizando Python, machine learning y Streamlit para analizar ventas de productos de mobiliario, evaluar la rentabilidad del negocio e identificar operaciones con riesgo de pérdida.

El flujo del proyecto incluye limpieza y preparación de datos, análisis exploratorio, entrenamiento de un modelo predictivo, generación de predicciones y visualización interactiva mediante una aplicación web desarrollada en Streamlit.

El objetivo principal es transformar un dataset comercial en una herramienta de apoyo para la toma de decisiones, permitiendo identificar patrones de rentabilidad, analizar el impacto de los descuentos y priorizar ventas con mayor probabilidad de no ser rentables.

---

## Objetivo general

Desarrollar un sistema de analítica comercial que permita analizar ventas, utilidad, descuentos y comportamiento de productos de mobiliario, incorporando un modelo predictivo para clasificar ventas con posible riesgo de pérdida comercial.

---

## Problema de negocio

En un entorno comercial, no todas las ventas generan utilidad para la empresa. Algunas operaciones pueden presentar pérdida debido a factores como altos descuentos, baja cantidad vendida, características del producto, segmento del cliente o región.

Por ello, se plantea la necesidad de analizar la rentabilidad de las ventas e identificar aquellas operaciones que podrían representar un riesgo comercial. Esta información puede ayudar a mejorar la toma de decisiones relacionadas con precios, descuentos, productos y estrategias comerciales.

---

## Dataset utilizado

El dataset utilizado corresponde a registros de ventas de una tienda, enfocado en productos de mobiliario. Contiene información relacionada con pedidos, clientes, productos, regiones, ventas, descuentos y utilidad.

Entre las principales variables se encuentran:

* `Order Date`: fecha del pedido.
* `Ship Date`: fecha de envío.
* `Ship Mode`: modo de envío.
* `Customer ID`: identificador del cliente.
* `Segment`: segmento del cliente.
* `Region`: región de venta.
* `Category`: categoría del producto.
* `Sub-Category`: subcategoría del producto.
* `Product Name`: nombre del producto.
* `Sales`: monto de venta.
* `Quantity`: cantidad vendida.
* `Discount`: descuento aplicado.
* `Profit`: utilidad obtenida.

A partir de estas variables se construyeron nuevas características para el análisis, como días de envío, margen de utilidad, nivel de descuento, nivel de rentabilidad y la variable objetivo `venta_no_rentable`.

---

## Metodología aplicada

El proyecto sigue un enfoque basado en la metodología CRISP-DM, adaptada a un caso de analítica comercial.

### 1. Comprensión del negocio

Se definió como problema principal la identificación de ventas no rentables y el análisis de factores que pueden afectar la utilidad comercial. El objetivo fue construir una solución capaz de analizar los datos históricos y detectar operaciones con riesgo de pérdida.

### 2. Comprensión de los datos

Se revisó la estructura del dataset, sus columnas, dimensiones, tipos de datos, valores nulos, duplicados y principales variables comerciales. Esta etapa permitió conocer la calidad inicial de los datos y determinar qué transformaciones eran necesarias.

### 3. Preparación de los datos

Se realizó un proceso de limpieza y transformación mediante Python. Se normalizaron nombres de columnas, se convirtieron fechas, se eliminaron duplicados, se trataron valores nulos y se generaron nuevas variables útiles para el análisis y el modelado.

### 4. Análisis exploratorio de datos

Se generaron estadísticas descriptivas y visualizaciones para analizar ventas, utilidad, descuentos, regiones, segmentos, subcategorías y productos. Esta etapa permitió identificar patrones generales de comportamiento comercial.

### 5. Modelado

Se entrenó un modelo de clasificación con Random Forest para predecir si una venta puede ser no rentable. Para evitar fuga de información, las variables directamente relacionadas con la utilidad final, como `profit` y `margen_utilidad`, no fueron utilizadas como variables predictoras del modelo.

### 6. Evaluación

El modelo fue evaluado mediante métricas como accuracy, precision, recall, F1-score, ROC-AUC, matriz de confusión y validación cruzada. Las métricas obtenidas se almacenan en el archivo `reports/metricas_modelo.txt`.

### 7. Despliegue

Se desarrolló una aplicación interactiva en Streamlit que permite explorar indicadores comerciales, aplicar filtros, visualizar gráficos y revisar el ranking de ventas con mayor riesgo de pérdida.

---

## Estructura del proyecto

```text
rentabilidad-comercial-streamlit/
│
├── data/
│   ├── raw/
│   │   └── Super_Store_data.csv
│   │
│   ├── processed/
│   │   └── ventas_limpias.csv
│   │
│   └── outputs/
│       └── predicciones_rentabilidad.csv
│
├── models/
│   └── modelo_rentabilidad.pkl
│
├── reports/
│   ├── figuras/
│   │   ├── 01_distribucion_rentabilidad.png
│   │   ├── 02_ventas_por_mes.png
│   │   ├── 03_utilidad_por_region.png
│   │   ├── 04_utilidad_por_segmento.png
│   │   ├── 05_utilidad_por_subcategoria.png
│   │   ├── 06_descuento_vs_utilidad.png
│   │   ├── 07_top_productos_perdida.png
│   │   ├── 08_top_productos_ganancia.png
│   │   ├── 09_nivel_descuento.png
│   │   └── 10_matriz_correlacion.png
│   │
│   └── metricas_modelo.txt
│
├── src/
│   ├── 01_etl_limpieza.py
│   ├── 02_eda.py
│   ├── 03_entrenamiento.py
│   └── 04_prediccion.py
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Módulos desarrollados

### `01_etl_limpieza.py`

Este módulo realiza la limpieza y preparación inicial del dataset. Sus principales tareas son:

* Cargar el dataset original desde `data/raw/`.
* Normalizar los nombres de columnas.
* Eliminar registros duplicados.
* Tratar valores nulos.
* Convertir columnas de fecha.
* Crear variables temporales como año, mes y trimestre.
* Calcular los días de envío.
* Calcular el margen de utilidad.
* Crear la variable objetivo `venta_no_rentable`.
* Crear variables categóricas como nivel de descuento y nivel de rentabilidad.
* Guardar el dataset limpio en `data/processed/ventas_limpias.csv`.

La variable objetivo se define de la siguiente manera:

```text
1 = venta no rentable, cuando Profit <= 0
0 = venta rentable, cuando Profit > 0
```

---

### `02_eda.py`

Este módulo realiza el análisis exploratorio de datos. Permite revisar la estructura del dataset limpio, generar estadísticas descriptivas y crear gráficos que ayudan a comprender el comportamiento comercial.

Entre los gráficos generados se encuentran:

* Distribución de ventas rentables y no rentables.
* Ventas totales por mes.
* Utilidad total por región.
* Utilidad total por segmento.
* Utilidad total por subcategoría.
* Relación entre descuento y utilidad.
* Top productos con mayor pérdida acumulada.
* Top productos con mayor ganancia acumulada.
* Distribución por nivel de descuento.
* Matriz de correlación de variables numéricas.

Las figuras generadas se almacenan en la carpeta `reports/figuras/`.

---

### `03_entrenamiento.py`

Este módulo entrena el modelo predictivo encargado de clasificar ventas con posible riesgo de pérdida.

El modelo utilizado es:

```text
Random Forest Classifier
```

Las variables predictoras utilizadas incluyen información comercial disponible antes de conocer la utilidad final, como:

* Modo de envío.
* Segmento.
* Región.
* Subcategoría.
* Ventas.
* Cantidad.
* Descuento.
* Días de envío.
* Año.
* Mes.
* Trimestre.

Para evitar fuga de información, no se utilizan como variables predictoras `profit`, `margen_utilidad`, `nivel_rentabilidad` ni `venta_no_rentable`, ya que están directamente relacionadas con el resultado final.

El módulo guarda:

* El modelo entrenado en `models/modelo_rentabilidad.pkl`.
* Las métricas del modelo en `reports/metricas_modelo.txt`.

---

### `04_prediccion.py`

Este módulo utiliza el modelo entrenado para generar predicciones sobre el dataset limpio.

Como resultado, se crean las siguientes columnas:

* `prediccion_perdida`: clasificación del modelo.
* `probabilidad_perdida`: probabilidad estimada de que una venta sea no rentable.
* `nivel_riesgo_comercial`: clasificación interpretativa del riesgo.

Los niveles de riesgo comercial se definen como:

```text
Bajo: 0.00 a 0.40
Medio: 0.40 a 0.70
Alto: 0.70 a 1.00
```

El archivo final se guarda en:

```text
data/outputs/predicciones_rentabilidad.csv
```

---

### `app.py`

Este archivo contiene la aplicación interactiva desarrollada con Streamlit. Permite visualizar los resultados del proyecto mediante una interfaz web.

La aplicación incluye:

* Indicadores generales de ventas y utilidad.
* Filtros por región, segmento, subcategoría y nivel de riesgo.
* Gráficos interactivos.
* Evolución mensual de ventas y utilidad.
* Análisis de relación entre descuento y utilidad.
* Ranking de ventas con mayor probabilidad de pérdida.
* Tabla completa de datos filtrados.
* Conclusiones generales automáticas.

---

## Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Plotly
* Streamlit
* Git y GitHub

---

## Resultados generados

El proyecto genera los siguientes archivos principales:

```text
data/processed/ventas_limpias.csv
data/outputs/predicciones_rentabilidad.csv
models/modelo_rentabilidad.pkl
reports/metricas_modelo.txt
reports/figuras/
```

Estos archivos permiten conservar el flujo completo del proyecto, desde los datos procesados hasta las predicciones finales y visualizaciones generadas.

---

## Aplicación en Streamlit

La aplicación permite analizar el comportamiento comercial de las ventas de mobiliario mediante una interfaz interactiva.

<img width="1890" height="863" alt="image" src="https://github.com/user-attachments/assets/23ea5ac3-f64e-4e02-bb05-509f15875e47" />

Principales funcionalidades:

* Visualización de KPIs comerciales.
* Filtros dinámicos por región, segmento, subcategoría y riesgo.
* Análisis de utilidad por región, segmento y subcategoría.
* Visualización de riesgo comercial.
* Ranking de ventas con mayor probabilidad de pérdida.
* Exploración de los datos filtrados.

Cuando la aplicación esté desplegada, se podrá acceder desde el siguiente enlace:

```text
[Enlace de la app: pendiente de despliegue](https://rentabilidad-comercial-app-fe2xk7fe52fpseafjtfawt.streamlit.app/)
```

---

## Buenas prácticas aplicadas

En el desarrollo del proyecto se consideraron algunas buenas prácticas de analítica y modelado:

* Organización modular del código.
* Separación entre datos originales, datos procesados y salidas.
* Uso de rutas relativas mediante `Path`.
* Creación automática de carpetas de salida.
* Validación de existencia de archivos.
* Uso de `Pipeline` para integrar preprocesamiento y modelo.
* Separación entre variables de análisis y variables predictoras.
* Prevención de fuga de información en el entrenamiento del modelo.
* Documentación del flujo completo en GitHub.

---

## Conclusiones

Este proyecto permitió construir una solución completa de analítica comercial, desde la preparación de datos hasta la visualización interactiva de resultados.

El análisis permite identificar patrones relevantes relacionados con ventas, utilidad, descuentos, segmentos, regiones y productos. Además, el modelo predictivo permite clasificar ventas con posible riesgo de pérdida, generando una probabilidad de riesgo que puede ser utilizada como apoyo para priorizar revisiones comerciales.

La aplicación en Streamlit facilita la exploración de los resultados de forma interactiva, convirtiendo el proyecto en una herramienta práctica de análisis y toma de decisiones.

---

