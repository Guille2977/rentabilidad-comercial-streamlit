# Reporte de Gráficos e Interpretación

## Proyecto: Sistema de Análisis y Predicción de Rentabilidad Comercial con Streamlit

Este reporte documenta las visualizaciones generadas durante la etapa de Análisis Exploratorio de Datos, con el objetivo de interpretar el comportamiento comercial de las ventas de mobiliario. Cada figura permite analizar aspectos relevantes como rentabilidad, ventas, utilidad, descuentos, productos y relaciones entre variables.

---

## Figura 1. Distribución de ventas rentables y no rentables

<img width="600" height="400" alt="01_distribucion_rentabilidad" src="https://github.com/user-attachments/assets/afefe696-d6e9-46f5-b271-24d8be9f6539" />


Esta figura muestra la cantidad de ventas clasificadas como rentables y no rentables. La clasificación se realiza a partir de la variable `venta_no_rentable`, donde una venta se considera no rentable cuando su utilidad es menor o igual a cero.

**Interpretación:**

El gráfico permite observar la proporción entre ventas que generan utilidad positiva y aquellas que representan pérdida o utilidad nula. Esta distribución es importante porque permite identificar si el problema de pérdida comercial es frecuente dentro del dataset o si corresponde a un grupo reducido de operaciones.

**Conclusión:**

La figura permite comprender el balance inicial de la variable objetivo utilizada en el modelo predictivo. Si existe una cantidad considerable de ventas no rentables, se justifica el desarrollo de un modelo que ayude a detectar operaciones con riesgo de pérdida.

---

## Figura 2. Ventas totales por mes

<img width="1200" height="500" alt="02_ventas_por_mes" src="https://github.com/user-attachments/assets/6f52abb5-c074-4825-9b41-fac39f69427d" />

Esta figura muestra la evolución de las ventas totales a lo largo del tiempo, agrupadas por año y mes.

**Interpretación:**

El gráfico permite identificar tendencias, incrementos, disminuciones o posibles comportamientos estacionales en las ventas. También ayuda a detectar meses con mayor actividad comercial y periodos donde las ventas fueron más bajas.

**Conclusión:**

La visualización temporal permite analizar el comportamiento comercial del negocio en el tiempo. Esta información puede apoyar decisiones relacionadas con planificación de inventario, campañas comerciales o evaluación de periodos de mayor demanda.

---

## Figura 3. Utilidad total por región

<img width="700" height="400" alt="03_utilidad_por_region" src="https://github.com/user-attachments/assets/a69f39ea-7054-4ea3-8936-f586934aba15" />

Esta figura presenta la utilidad acumulada por cada región incluida en el dataset.

**Interpretación:**

El gráfico permite comparar el desempeño económico de las regiones. Una región con utilidad alta representa un mejor resultado comercial, mientras que una región con utilidad baja o negativa puede requerir mayor análisis.

**Conclusión:**

La utilidad por región ayuda a identificar zonas geográficas con mejor o peor desempeño. Esta información puede ser útil para orientar estrategias comerciales, revisar políticas de descuento o analizar diferencias operativas entre regiones.

---

## Figura 4. Utilidad total por segmento

<img width="700" height="400" alt="04_utilidad_por_segmento" src="https://github.com/user-attachments/assets/2721b6c1-6d06-469d-bfc7-ff541cf2aa12" />

Esta figura muestra la utilidad total generada por cada segmento de cliente.

**Interpretación:**

El gráfico permite comparar qué segmentos aportan mayor utilidad al negocio. También ayuda a identificar si ciertos tipos de clientes generan mejores márgenes o si algún segmento presenta menor rentabilidad.

**Conclusión:**

El análisis por segmento permite orientar mejor las estrategias comerciales. Si un segmento genera mayor utilidad, puede ser priorizado en campañas o acciones de fidelización. Si un segmento presenta bajo rendimiento, puede ser necesario revisar precios, descuentos o condiciones comerciales.

---

## Figura 5. Utilidad total por subcategoría

<img width="800" height="400" alt="05_utilidad_por_subcategoria" src="https://github.com/user-attachments/assets/82c57ea2-4ea2-41bb-ae81-dffe88518a37" />

Esta figura muestra la utilidad acumulada por subcategoría de producto.

**Interpretación:**

El gráfico permite identificar qué subcategorías generan mayores ganancias y cuáles tienen menor desempeño. En el contexto de productos de mobiliario, esta comparación es útil para evaluar si ciertas líneas de producto son más rentables que otras.

**Conclusión:**

La figura permite detectar subcategorías que aportan valor al negocio y subcategorías que podrían estar asociadas a pérdidas. Esto puede apoyar decisiones sobre precios, descuentos, inventario o promoción de productos.

---

## Figura 6. Relación entre descuento y utilidad

<img width="800" height="500" alt="06_descuento_vs_utilidad" src="https://github.com/user-attachments/assets/fd5fa272-d61f-4d95-9588-767ca50f6cad" />

Esta figura representa la relación entre el descuento aplicado y la utilidad obtenida en cada venta.

**Interpretación:**

El gráfico permite observar si los descuentos altos tienden a relacionarse con menores utilidades o pérdidas. También permite identificar operaciones donde, a pesar de tener ventas elevadas, la utilidad puede verse reducida por descuentos significativos.

**Conclusión:**

Esta visualización es clave para analizar el impacto de los descuentos en la rentabilidad. Si se observa que los descuentos altos se asocian con pérdidas frecuentes, la empresa podría revisar sus políticas comerciales para evitar operaciones no rentables.

---

## Figura 7. Top 10 productos con mayor pérdida acumulada

<img width="1000" height="500" alt="07_top_productos_perdida" src="https://github.com/user-attachments/assets/653b44ed-b22b-4618-b7aa-78b56d0569de" />

Esta figura muestra los diez productos con mayor pérdida acumulada en el dataset.

**Interpretación:**

El gráfico permite identificar productos específicos que generan mayor impacto negativo en la utilidad total. Estos productos pueden estar relacionados con descuentos elevados, bajos márgenes, costos altos o condiciones comerciales poco favorables.

**Conclusión:**

La identificación de productos con mayor pérdida es importante para la gestión comercial. Estos productos deberían ser revisados para evaluar ajustes de precio, reducción de descuentos, cambios en la estrategia de venta o incluso reconsideración de su permanencia en el catálogo.

---

## Figura 8. Top 10 productos con mayor ganancia acumulada

<img width="1000" height="500" alt="08_top_productos_ganancia" src="https://github.com/user-attachments/assets/bb5605c6-d7c4-4523-aa05-ea1c49c453c6" />

Esta figura presenta los diez productos con mayor ganancia acumulada.

**Interpretación:**

El gráfico permite reconocer los productos que generan mayor utilidad para el negocio. Estos productos pueden considerarse estratégicos por su aporte positivo al resultado comercial.

**Conclusión:**

Los productos con mayor ganancia pueden ser priorizados en campañas, promociones o estrategias de inventario. También pueden servir como referencia para analizar qué características tienen los productos más rentables.

---

## Figura 9. Distribución por nivel de descuento

<img width="600" height="400" alt="09_nivel_descuento" src="https://github.com/user-attachments/assets/12560bce-5b31-4171-8cc6-5d6a579e0597" />

Esta figura muestra la cantidad de ventas clasificadas según el nivel de descuento aplicado: bajo, medio o alto.

**Interpretación:**

El gráfico permite observar cómo se distribuyen las ventas según la intensidad del descuento. Si existe una alta cantidad de ventas con descuentos medios o altos, puede ser necesario analizar su impacto sobre la utilidad.

**Conclusión:**

La distribución del nivel de descuento ayuda a comprender la política comercial aplicada en las ventas. Esta información se complementa con el análisis de utilidad para evaluar si los descuentos están contribuyendo al resultado del negocio o si están afectando negativamente la rentabilidad.

---

## Figura 10. Matriz de correlación de variables numéricas

<img width="1000" height="700" alt="10_matriz_correlacion" src="https://github.com/user-attachments/assets/8b3fe493-7b43-4e23-be29-cd380c096e28" />

Esta figura muestra la correlación entre las variables numéricas del dataset.

**Interpretación:**

La matriz de correlación permite identificar relaciones lineales entre variables como ventas, cantidad, descuento, utilidad, días de envío, margen de utilidad y variables temporales. Una correlación positiva indica que dos variables tienden a aumentar juntas, mientras que una correlación negativa indica que una variable tiende a disminuir cuando la otra aumenta.

**Conclusión:**

La matriz de correlación ayuda a comprender qué variables pueden estar relacionadas con la rentabilidad. En particular, permite observar si el descuento, la cantidad vendida o el monto de venta tienen relación con la utilidad o con la clasificación de ventas no rentables.

---

## Conclusión general del análisis gráfico

El conjunto de visualizaciones permite comprender el comportamiento comercial de las ventas de mobiliario desde diferentes perspectivas. Se analizaron patrones temporales, desempeño por región, segmento y subcategoría, relación entre descuentos y utilidad, así como productos con mayor ganancia o pérdida.

En general, los gráficos permiten identificar factores que pueden influir en la rentabilidad comercial. Esta información sirve como base para el desarrollo del modelo predictivo, cuyo objetivo es clasificar ventas con posible riesgo de pérdida y apoyar la toma de decisiones mediante una aplicación interactiva en Streamlit.
