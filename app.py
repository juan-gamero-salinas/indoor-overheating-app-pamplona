# Copyright [2025] [Juan Carlos Gamero Salinas]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import streamlit as st
import numpy as np
import pandas as pd
from scipy.special import expit
from sklearn.mixture import BayesianGaussianMixture
import matplotlib.pyplot as plt

# Load the uploaded CSV
merge_gdf = pd.read_csv("df.csv")

# Fit the Bayesian GMM with 2 components
gmm = BayesianGaussianMixture(n_components=2, random_state=0)
X = merge_gdf[["prob_overheat_skater"]].values  # shape: (n_samples, 1)
gmm.fit(X)

# Predict probabilities and labels for the dataset
probs = gmm.predict_proba(X)
preds = gmm.predict(X)

# Store in dataframe
merge_gdf["GMM_Cluster"] = preds
for i in range(2):
    merge_gdf[f"Prob_Cluster_{i}"] = probs[:, i]

# ──────────────────────────────────────────────────────────────
# Streamlit Interface

st.title("¿Tu vivienda se sobrecalienta durante olas de calor en Pamplona, Navarra?")

st.markdown("""
Esta herramienta interactiva estima el riesgo de **sobrecalentamiento interior** durante una ola de calor, basándose en datos de encuestas realizadas en Pamplona en los veranos de 2021 y 2022. 

Responde las siguientes preguntas para saber si tu vivienda podría estar en riesgo de **sobrecalentamiento** durante una ola de calor.
""")

# User inputs
temp = st.slider("Temperatura del termostato (°C)", 22.0, 31.0, 24.0)
has_ac = st.selectbox("¿Tienes al menos un aparato de aire acondicionado instalado en la casa?", ["Sí", "No"])
hw = st.selectbox("¿Está Pamplona sufriendo una ola de calor?", ["No", "Sí"])
gender = st.selectbox("Sexo", ["Mujer", "Hombre"])

# Encode inputs
x = [
    temp,
    1 if has_ac == "No" else 0,
    1 if hw == "Sí" else 0,
    1 if gender == "Mujer" else 0
]

# Logistic regression calculation
intercept = -19.0980
coeffs = [0.6331, 2.0876, 0.9799, 0.9758]
linear_combination = intercept + np.dot(coeffs, x)
prob = expit(linear_combination)

# Predict with GMM
prob_array = np.array([[prob]])
posterior = gmm.predict_proba(prob_array)
cluster = gmm.predict(prob_array)[0]

# Rearranged for consistent labeling (Cluster 1 = high risk)
prob_cluster_0 = posterior[0][1]
prob_cluster_1 = posterior[0][0]

cluster_info = {
    0: {'label': 'Bajo riesgo de sobrecalentamiento', 'color': 'blue', 'icon': '🟦'},
    1: {'label': 'Alto riesgo de sobrecalentamiento', 'color': 'red', 'icon': '🟥'},
    'intermedio': {'label': 'Riesgo intermedio', 'color': 'orange', 'icon': '⚪'}
}

confidence_threshold = 0.8
if max(prob_cluster_0, prob_cluster_1) < confidence_threshold:
    most_likely_cluster = 'intermedio'
else:
    most_likely_cluster = int(np.argmax([prob_cluster_0, prob_cluster_1]))

risk_label = cluster_info[most_likely_cluster]['icon'] + " " + cluster_info[most_likely_cluster]['label']

# Results
st.subheader("Tu riesgo de sobrecalentamiento:")
st.write(f"Probabilidad estimada de sobrecalentamiento: **{prob:.2f}**")
st.success(f"**Tu perfil pertenece al grupo de: {risk_label}**")

cluster_probs = [prob_cluster_0, prob_cluster_1]

with st.expander("Detalles del riesgo"):
    st.markdown("### Probabilidades de pertenencia a cada grupo:")
    for i in [0, 1]:
        info = cluster_info[i]
        st.write(f"{info['icon']} {info['label']} (Cluster {i}): **{cluster_probs[i]:.2f}**")
    st.write(f"🔶 Nivel de confianza en la clasificación: **{max(cluster_probs):.2f}**")



# ──────────────────────────────────────────────────────────────
# Información adicional y disclaimer

st.markdown("""
---

📖 **Referencia científica**:  
Gamero-Salinas, J., López-Hernández, D., González-Martínez, P., Arriazu-Ramos, A., Monge-Barrio, A., & Sánchez-Ostiz, A. (2024).  
*Exploring indoor thermal comfort and its causes and consequences amid heatwaves in a Southern European city—An unsupervised learning approach*.  
*Building and Environment, 265, 111986.*

⚠️ **Disclaimer**:  
Este modelo es una herramienta **exploratoria** basada en datos de encuestas.  
**No reemplaza diagnósticos técnicos, asesoría profesional ni normativas legales**, pero puede ayudar a orientar decisiones relacionadas al diagnóstico de sobrecalentamiento interior.
""")

