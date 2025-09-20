import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from load_data import load_titanic_data
from feature_engineering import engineer_features
from visualizations import plot_heatmap
from visualizations import plot_dispersion
from visualizations import plot_pie_survival_by_class

# Carregar e preparar dados
df = load_titanic_data()
df = engineer_features(df)

st.title("🚢 Painel do Titanic")

# 🔍 Mapa de calor

st.subheader("🔍 Correlações entre variáveis")
st.plotly_chart(plot_heatmap(df))

# 📈 Dispersão com filtro de idade
st.subheader("📈 Dispersão: Idade vs Tarifa")
idade_min, idade_max = st.slider("Selecione a faixa de idade", 0, 80, (10, 50))
st.plotly_chart(plot_dispersion(df, idade_min, idade_max))

# 🧁 Pizza com filtro de classe
st.subheader("🧁 Sobrevivência por Classe")
classes = st.multiselect("Escolha as classes", options=df['class'].unique(), default=df['class'].unique())
st.plotly_chart(plot_pie_survival_by_class(df, classes))