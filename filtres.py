import streamlit as st
from data.loader import load_data

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }
    </style>
    """,
    unsafe_allow_html=True
)
df = load_data()

st.title("🎛️ Filtres")

classe = st.multiselect("Classe", df["pclass"].unique())
sexe = st.multiselect("Sexe", df["sex"].unique())

filtered = df.copy()

if classe:
    filtered = filtered[filtered["pclass"].isin(classe)]

if sexe:
    filtered = filtered[filtered["sex"].isin(sexe)]

st.dataframe(filtered)