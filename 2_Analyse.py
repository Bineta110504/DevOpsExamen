import streamlit as st
import plotly.express as px
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

st.title("📈 Analyse de survie")

col1, col2 = st.columns(2)

fig1 = px.bar(df, x="sex", y="survived", color="sex")
col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(df, names="pclass")
col2.plotly_chart(fig2, use_container_width=True)

fig3 = px.histogram(df, x="age", color="survived")
st.plotly_chart(fig3, use_container_width=True)