# prediccion-desercion-estudiantil
Proyecto de minería de datos para predicción de deserción estudiantil
## Autora
Allison Castro

## Descripción del Proyecto
La deserción estudiantil es un problema crítico en la educación superior. Este proyecto implementa un sistema de predicción basado en reglas y análisis de datos históricos para identificar estudiantes en riesgo, permitiendo la toma de decisiones oportunas.

## Dataset
Se utiliza un dataset anonimizado del récord académico estudiantil que incluye variables como:
- Promedio académico
- Asistencia
- Estado académico

Por motivos de privacidad, el dataset puede no estar incluido directamente en el repositorio.

## Metodología
El proyecto sigue la metodología CRISP-DM:
1. Comprensión del negocio
2. Comprensión de los datos
3. Preparación de los datos
4. Modelado
5. Evaluación
6. Despliegue

## Modelo
Se utiliza un modelo de clasificación basado en reglas:
- Si el promedio < 7 o la asistencia < 70 → Riesgo de deserción
- Caso contrario → No presenta riesgo

Este enfoque fue seleccionado por su interpretabilidad y alineación con criterios académicos institucionales.

## Tecnologías utilizadas
- Python
- Pandas
- Scikit-learn
- Streamlit

## Ejecución del proyecto
1. Instalar dependencias:
