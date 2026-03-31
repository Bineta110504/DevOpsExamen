import streamlit as st

# DOIT être en premier
st.set_page_config(
    page_title="Titanic Dashboard",
    page_icon="🚢",
    layout="wide"
)

# Style
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

st.title("🚢 Dashboard Titanic")
st.markdown("### Analyse interactive des passagers")

st.markdown("---")

st.info("Utilisez le menu à gauche pour naviguer entre les pages 📊")

st.image(
    "https://images.unsplash.com/photo-1544551763-cede2b27b6bc",
    use_column_width=True
)