import streamlit as st
import pandas as pd
from data.loader import load_data
import plotly.express as px
import logging
import json

# Configuration du logger pour ELK Stack [cite: 17, 39]
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(message)s"
)

def log_event(event):
    logging.info(json.dumps(event))

# Chargement du dataset Titanic via seaborn [cite: 13, 22, 54]
df = load_data()

st.title("Dashboard Titanic")

# 1. Sidebar filtres [cite: 14, 23]
st.sidebar.header("Filtres")

classe = st.sidebar.multiselect(
    "Classe", options=sorted(df["pclass"].unique()), default=df["pclass"].unique()
)

sexe = st.sidebar.multiselect(
    "Sexe", options=df["sex"].unique(), default=df["sex"].unique()
)

# Application des filtres sur le DataFrame [cite: 14]
filtered_df = df[
    (df["pclass"].isin(classe)) &
    (df["sex"].isin(sexe))
]

# --- CORRECTION : Appels des logs au bon endroit (après définition des variables) --- [cite: 15, 24]
log_event({
    "event": "filter_applied",
    "classe": classe,
    "sexe": sexe
})
log_event({
    "event": "page_view",
    "page": "dashboard"
})

# 2. KPI - Vue Générale [cite: 14]
st.subheader("Vue Générale")
col1, col2 = st.columns(2)
col1.metric("Nombre de passagers", len(filtered_df))
col2.metric("Taux de survie", f"{round(filtered_df['survived'].mean() * 100, 2)}%")

# 3. Graphique - Analyse de survie [cite: 14]
st.subheader("Survie par sexe")
fig = px.bar(filtered_df, x="sex", y="survived", color="sex", title="Taux de survie par sexe")
st.plotly_chart(fig)

# 4. Données brutes [cite: 14]
st.subheader("Données")
st.dataframe(filtered_df)