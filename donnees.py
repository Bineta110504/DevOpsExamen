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

st.title("📋 Données brutes")

st.dataframe(df)

st.download_button(
    "📥 Télécharger CSV",
    df.to_csv(index=False),
    "titanic.csv"
)