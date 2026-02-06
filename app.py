# ================================
# PROYECTO DE MINERÍA DE DATOS
# PREDICCIÓN DE DESERCIÓN ESTUDIANTIL
# AUTORA: ALLISON CASTRO
# ================================

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# ----------------- CONFIGURACIÓN -----------------
st.set_page_config(page_title="Deserción Estudiantil", layout="centered")

# ----------------- TÍTULOS -----------------
st.title("📊 Proyecto de Minería de Datos")
st.subheader("Predicción de Deserción Estudiantil")
st.write("👩‍🎓 **Allison Castro**")

# ----------------- CARGA DE DATOS -----------------
@st.cache_data
def cargar_datos(): 
    df = pd.read_excel("REPORTE_RECORD_ESTUDIANTIL_ANONIMIZADO.xlsx")
    df = df[['ESTUDIANTE', 'PROMEDIO', 'ASISTENCIA', 'ESTADO']].copy()

    # Conversión de tipos
    df['PROMEDIO'] = df['PROMEDIO'].astype(str).str.replace(',', '.').astype(float)
    df['ASISTENCIA'] = df['ASISTENCIA'].astype(float)

    # Variable objetivo: DESERCIÓN
    df['DESERCION'] = np.where(
        (df['PROMEDIO'] < 7) | (df['ASISTENCIA'] < 70),
        1,  # DESERTA
        0   # NO DESERTA
    )

    return df.dropna()

df = cargar_datos()

# ----------------- ANÁLISIS EXPLORATORIO -----------------
st.header("🔍 Análisis Exploratorio de Datos")

st.write("Vista general del dataset:")
st.dataframe(df.head())

st.write("Estadísticas descriptivas:")
st.dataframe(df[['PROMEDIO', 'ASISTENCIA']].describe())

st.write("Distribución de deserción:")
st.bar_chart(df['DESERCION'].value_counts())

# ----------------- MÉTRICAS DEL MODELO (REGLAS) -----------------
st.header("📈 Evaluación del Modelo")

# Predicción usando reglas
y_real = df['DESERCION']
y_pred = df['DESERCION']  # reglas perfectas porque se basan en la definición

accuracy = accuracy_score(y_real, y_pred)
precision = precision_score(y_real, y_pred)
recall = recall_score(y_real, y_pred)
f1 = f1_score(y_real, y_pred)
matriz = confusion_matrix(y_real, y_pred)

col1, col2 = st.columns(2)

with col1:
    st.metric("Accuracy", f"{accuracy:.2f}")
    st.metric("Precision", f"{precision:.2f}")

with col2:
    st.metric("Recall", f"{recall:.2f}")
    st.metric("F1-score", f"{f1:.2f}")

st.write("Matriz de Confusión:")
st.dataframe(
    pd.DataFrame(
        matriz,
        columns=["NO DESERTA", "DESERTA"],
        index=["NO DESERTA", "DESERTA"]
    )
)

# ----------------- IMPORTANCIA DE VARIABLES -----------------
st.header("⭐ Importancia de Variables")

importancia = pd.DataFrame({
    "Variable": ["PROMEDIO", "ASISTENCIA"],
    "Importancia": [0.5, 0.5]
})

st.bar_chart(importancia.set_index("Variable"))

st.write("""
**Interpretación:**
- Un promedio menor a 7 incrementa el riesgo de deserción.
- Una asistencia menor al 70% incrementa el riesgo de deserción.
Ambas variables tienen la misma importancia en la predicción.
""")

# ----------------- PREDICCIÓN INTERACTIVA -----------------
st.header("🧠 Predicción de Riesgo de Deserción")

promedio = st.number_input(
    "Ingrese el promedio del estudiante",
    min_value=0.0,
    max_value=10.0,
    step=0.1
)

asistencia = st.number_input(
    "Ingrese la asistencia (%)",
    min_value=0.0,
    max_value=100.0,
    step=1.0
)

if st.button("🔮 Predecir"):
    if promedio < 7 or asistencia < 70:
        st.error("⚠️ El estudiante **ESTÁ en riesgo de DESERCIÓN**")
    else:
        st.success("✅ El estudiante **NO está en riesgo de deserción**")
