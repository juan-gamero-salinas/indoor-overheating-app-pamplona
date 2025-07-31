# 🔥 ¿Sufres sobrecalentamiento en tu vivienda durante olas de calor en Pamplona (Navarra)?

Este es un prototipo interactivo desarrollado para estimar el **riesgo de sobrecalentamiento en el interior de viviendas** durante olas de calor en Pamplona, Navarra. El objetivo es ayudar a identificar **hogares vulnerables** usando un modelo de clasificación basado en datos reales (encuestas).

---

## 🧠 ¿Qué hace esta herramienta?

🔍 Evalúa tu riesgo en función de:
- Temperatura interior registrada
- Presencia o ausencia de aire acondicionado
- Si hay o no una ola de calor activa
- Sexo de la persona usuaria
  
Utiliza un **modelo de clustering + probabilidad supervisada** entrenado con datos de encuesta.

---

## 🛠 ¿Cómo usarla?

1. Abre la aplicación en [Streamlit](https://indoor-overheating-app-pamplona.streamlit.app/)  
2. Responde a preguntas breves como:
   - ¿Cuál es la temperatura del termostato?
   - ¿Tienes aire acondicionado?
   - ¿Hay ola de calor?
   - ¿Cuál es tu sexo?
3. La herramienta calcula tu riesgo y muestra:
   - 🔴 Probabilidad estimada de sobrecalentamiento
   - 🟥 Nivel de riesgo (alto o bajo)
   - 📊 Probabilidades de pertenencia a cada grupo (clúster)
   - 🧪 Nivel de confianza del modelo en su predicción

---


## 📊 Ejemplo de salida:

Probabilidad estimada de sobrecalentamiento: 0.91
Tu perfil pertenece al grupo de: 🟥 Alto riesgo de sobrecalentamiento

🟦 Bajo riesgo (Cluster 0): 0.10
🟥 Alto riesgo (Cluster 1): 0.90
🔶 Nivel de confianza en la clasificación: 0.90



---

## 🧩 Tecnologías utilizadas

- `Streamlit` – para la interfaz web
- `scikit-learn` – para clustering y predicción probabilística
- `Pandas` / `NumPy` – procesamiento de datos
- Basado en datos reales de encuestas locales en Pamplona [ClimateReady Project Survey Data](https://github.com/juan-gamero-salinas/climateready-survey-pamplona)
  

---

## 📍 Sobre el autor

Juan Gamero-Salinas  
PhD en Diseño Ambiental y Tecnológico en Arquitectura por la Universidad de Navarra (2021)
👨‍💻 [GitHub](https://github.com/juan-gamero-salinas) | 🔗 [LinkedIn](https://www.linkedin.com/in/juangamerosalinas/) | 📧 arqgamero@gmail.com

---

## 🧪 Disclaimer

Este modelo es una **herramienta exploratoria!!** basada en datos de encuesta. **No reemplaza diagnósticos técnicos, asesoría profesional o normativas**, pero puede ayudar a orientar decisiones sobre ventilación, reformas o instalación de sistemas de climatización.

