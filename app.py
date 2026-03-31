import streamlit as st
from data.loader import load_data
import plotly.express as px

# CONFIG PAGE
st.set_page_config(page_title="Titanic Dashboard", page_icon="📊", layout="wide")

# STYLE CSS
st.markdown("""
<style>
.main { background-color: #f8fafc; }
h1 { color: #1f77b4; }
div[data-testid="metric-container"] {
    background-color: white;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# LOAD DATA
df = load_data()

# SIDEBAR
st.sidebar.title("Filtres")

classe = st.sidebar.multiselect(
    "Classe",
    options=df['pclass'].unique(),
    default=df['pclass'].unique()
)

sexe = st.sidebar.multiselect(
    "Sexe",
    options=df['sex'].unique(),
    default=df['sex'].unique()
)

# FILTRE
df = df[(df['pclass'].isin(classe)) & (df['sex'].isin(sexe))]

# TITRE
st.title("📊 Dashboard Titanic")
st.markdown("Analyse des passagers du Titanic")

# KPI
col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Total", len(df))
col2.metric("🟢 Survie", f"{round(df['survived'].mean()*100,2)} %")
col3.metric("🎂 Age moyen", round(df['age'].mean(), 1))
col4.metric("👩 Femmes", len(df[df['sex']=="female"]))

# GRAPHIQUES
col5, col6 = st.columns(2)

fig1 = px.histogram(
    df,
    x="age",
    nbins=30,
    title="Distribution des âges",
    color_discrete_sequence=["#1f77b4"]
)

fig2 = px.bar(
    df,
    x="sex",
    y="survived",
    color="sex",
    title="Survie par sexe",
    color_discrete_sequence=["#ff7f0e","#1f77b4"]
)

col5.plotly_chart(fig1, use_container_width=True)
col6.plotly_chart(fig2, use_container_width=True)

# INSIGHTS
st.markdown("### 🧠 Insights")

taux = df['survived'].mean()

if taux > 0.5:
    st.success("✔️ Bon taux de survie global")
elif taux > 0.3:
    st.info("⚠️ Taux de survie moyen")
else:
    st.error("❌ Faible taux de survie")

# ANALYSE
st.markdown("### 📌 Analyse rapide")

st.write("""
- La majorité des survivants sont des **femmes**
- Les passagers de **1ère classe survivent plus**
- Les jeunes ont plus de chances de survie
""")

# TABLE
st.subheader("📋 Données")
st.dataframe(df, use_container_width=True)