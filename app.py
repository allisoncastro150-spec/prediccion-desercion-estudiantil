
import streamlit as st
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# ----------------- CONFIGURACIÓN -----------------
st.set_page_config(
    page_title="Predicción de Deserción Estudiantil",
    layout="centered"
)

# ----------------- CARGA DE MODELO -----------------
modelo = joblib.load("modelo_desercion.pkl")
scaler = joblib.load("scaler.pkl")

# ----------------- TÍTULOS -----------------
st.title("Proyecto de Minería de Datos")
st.subheader("Predicción de Riesgo de Deserción Estudiantil")
st.write("👩‍🎓 **Allison Castro**")

# ----------------- CARGA DE DATOS -----------------
@st.cache_data
def cargar_datos():
    df = pd.read_excel("REPORTE_RECORD_ESTUDIANTIL_ANONIMIZADO.xlsx")
    df = df[['ESTUDIANTE', 'PROMEDIO', 'ASISTENCIA']].copy()

    df['PROMEDIO'] = df['PROMEDIO'].astype(str).str.replace(',', '.').astype(float)
    df['ASISTENCIA'] = df['ASISTENCIA'].astype(float)

    # Variable dependiente (regla académica)
    df['DESERCION'] = ((df['PROMEDIO'] < 7) | (df['ASISTENCIA'] < 70)).astype(int)

    return df.dropna()

df = cargar_datos()

# ----------------- ANÁLISIS EXPLORATORIO -----------------
st.header("Análisis Exploratorio de Datos")

st.write("Vista general del dataset:")
st.dataframe(df.head())

st.write("Estadísticas descriptivas:")
st.dataframe(df[['PROMEDIO', 'ASISTENCIA']].describe())

st.write("Distribución de la variable objetivo (Deserción):")
st.bar_chart(df['DESERCION'].value_counts())

# ----------------- EVALUACIÓN DEL MODELO -----------------
st.header("Evaluación del Modelo")

X = df[['PROMEDIO', 'ASISTENCIA']]
y_real = df['DESERCION']

X_scaled = scaler.transform(X)
y_pred = modelo.predict(X_scaled)

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

# ----------------- INTERPRETACIÓN -----------------
st.header("🧠 Interpretación")

st.write("""
- Un promedio bajo incrementa la probabilidad de deserción.
- Una asistencia baja incrementa la probabilidad de deserción.
- El modelo de regresión logística aprende esta relación a partir de los datos históricos.
""")

# ----------------- PREDICCIÓN INTERACTIVA -----------------
st.header("🔮 Predicción de Riesgo de Deserción")

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

if st.button("📌 Predecir"):
    entrada = pd.DataFrame(
        [[promedio, asistencia]],
        columns=['PROMEDIO', 'ASISTENCIA']
    )

    entrada_scaled = scaler.transform(entrada)

    prediccion = modelo.predict(entrada_scaled)[0]
    probabilidad = modelo.predict_proba(entrada_scaled)[0][1]

    if prediccion == 1:
        st.error(
            f"⚠️ **ALTO RIESGO DE DESERCIÓN**\n\n"
            f"Probabilidad estimada: **{probabilidad*100:.2f}%**"
        )
    else:
        st.success(
            f"✅ **BAJO RIESGO DE DESERCIÓN**\n\n"
            f"Probabilidad estimada: **{probabilidad*100:.2f}%**"
        )

