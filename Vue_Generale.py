import streamlit as st
from data.loader import load_data

df = load_data()

st.title("📊 Vue Générale")

col1, col2, col3 = st.columns(3)

col1.metric("👥 Passagers", len(df))
col2.metric("💀 Taux de survie", f"{df['survived'].mean()*100:.1f}%")
col3.metric("🎂 Age moyen", f"{df['age'].mean():.1f}")

st.markdown("---")

st.dataframe(df.head())