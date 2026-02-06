# 📊 Proyecto de Minería de Datos  
## Predicción de Deserción Estudiantil  

**Autor:** Allison Castro  
**Asignatura:** Minería de Datos  
**Herramientas:** Python, Pandas, Scikit-learn, Streamlit  

---

## Proyecto

La deserción estudiantil representa uno de los principales desafíos que enfrentan las instituciones de educación superior. Identificar de manera temprana a los estudiantes con riesgo de abandono permite implementar estrategias de intervención oportunas.

En este proyecto se aplican técnicas de minería de datos para desarrollar un modelo predictivo que identifique estudiantes en riesgo de deserción a partir de información académica histórica, y se presentan los resultados mediante una interfaz gráfica interactiva desarrollada con Streamlit.

---

## Objetivo General

Desarrollar un sistema de predicción de deserción estudiantil aplicando técnicas de minería de datos, que permita identificar estudiantes en riesgo y visualizar los resultados mediante una interfaz gráfica interactiva.

---

## Objetivos Específicos

- Realizar un análisis exploratorio del conjunto de datos.
- Identificar las variables más relevantes para la predicción de deserción.
- Definir la variable objetivo a partir de los datos históricos.
- Aplicar técnicas de preprocesamiento de datos.
- Construir y evaluar un modelo de clasificación.
- Desarrollar una aplicación interactiva con Streamlit.
- Documentar el proceso siguiendo la metodología CRISP-DM.

---

## 🗂️ Dataset

El proyecto utiliza un archivo Excel anonimizado:

- **REPORTE_RECORD_ESTUDIANTIL_ANONIMIZADO.xlsx**

Variables principales utilizadas:
- PROMEDIO
- ASISTENCIA
- ESTADO (variable objetivo)

---

## Metodología

El desarrollo del proyecto sigue la metodología **CRISP-DM**, abordando las siguientes fases:

1. Comprensión del negocio  
2. Comprensión de los datos  
3. Preparación de los datos  
4. Modelado  
5. Evaluación  
6. Despliegue  

---

## Modelo de Machine Learning

Se implementó un modelo de **Regresión Logística** para la predicción de deserción estudiantil.

### Criterio de Riesgo
Un estudiante se considera **en riesgo de deserción** si:
- El promedio es menor a 7 **o**
- La asistencia es menor a 7  

Caso contrario, el estudiante **no se considera en riesgo**.

---

## 📈 Evaluación del Modelo

El modelo fue evaluado utilizando las siguientes métricas:
- Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusión

---

## Aplicación Streamlit

La aplicación permite:
- Visualizar el análisis exploratorio de los datos.
- Mostrar estadísticas descriptivas.
- Ingresar datos de un estudiante.
- Obtener la predicción de riesgo de deserción en tiempo real.

Para ejecutar la aplicación:

```bash
streamlit run app.py

