import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data.loader import load_titanic_data
import logging
import json
from datetime import datetime
import os
import uuid
import hashlib

# ============================================
# Configuration des logs
# ============================================
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler('logs/app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def log_interaction(page, filters=None):
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'page': page,
        'filters': filters or {},
        'session_id': st.session_state.get('session_id', 'unknown')
    }
    logging.info(json.dumps(log_entry, ensure_ascii=False))

# ============================================
# Configuration Streamlit
# ============================================
st.set_page_config(
    page_title="Titanic Dashboard",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    /* Fond principal */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Cartes KPI */
    .kpi-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.05));
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .kpi-card:hover {
        transform: translateY(-5px);
        border-color: #00d4ff;
        box-shadow: 0 10px 30px rgba(0,212,255,0.2);
    }
    
    .kpi-value {
        font-size: 36px;
        font-weight: 700;
        background: linear-gradient(135deg, #fff, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .kpi-label {
        font-size: 14px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 8px;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Titres */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        background: linear-gradient(135deg, #fff, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .section-title {
        font-size: 24px;
        font-weight: 600;
        color: #fff;
        border-left: 4px solid #00d4ff;
        padding-left: 15px;
        margin: 30px 0 20px 0;
    }
    
    /* Login container */
    .login-container {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 50px;
        border: 1px solid rgba(255,255,255,0.1);
        max-width: 450px;
        margin: 100px auto;
        text-align: center;
    }
    
    .login-title {
        font-size: 32px;
        font-weight: 700;
        background: linear-gradient(135deg, #fff, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# Initialisation session
# ============================================
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# ============================================
# Fonction d'authentification
# ============================================
def check_password(username, password):
    """Vérifie les identifiants (admin/1234)"""
    return username == "admin" and password == "1234"

# ============================================
# PAGE DE LOGIN
# ============================================
if not st.session_state.logged_in:
    st.markdown("""
    <div class="login-container">
        <div class="login-title">🚢 Titanic Dashboard</div>
        <p style="color: #94a3b8;">Accès sécurisé</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("👤 Identifiant", placeholder="admin")
            password = st.text_input("🔒 Mot de passe", type="password", placeholder="••••••")
            
            submitted = st.form_submit_button("🚀 Se connecter", use_container_width=True)
            
            if submitted:
                if check_password(username, password):
                    st.session_state.logged_in = True
                    st.session_state.login_time = datetime.now()
                    st.success("✅ Connexion réussie !")
                    st.rerun()
                else:
                    st.error("❌ Identifiants incorrects")
    
    st.stop()

# ============================================
# Chargement des données (après login)
# ============================================
@st.cache_data
def load_data():
    return load_titanic_data()

df = load_data()

# ============================================
# Sidebar - Filtres
# ============================================
with st.sidebar:
    # Info utilisateur
    st.markdown(f"""
    <div style="background: rgba(0,212,255,0.1); padding: 12px; border-radius: 12px; margin-bottom: 20px;">
        <small style="color: #00d4ff;">👤 Connecté</small><br>
        <small style="color: #94a3b8;">{st.session_state.login_time.strftime('%d/%m/%Y %H:%M')}</small>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## 🎯 **Filtres**")
    st.markdown("---")
    
    # Filtres
    class_list = list(df['class'].unique())
    selected_class = st.multiselect(
        "🏷️ **Classe**",
        options=class_list,
        default=class_list
    )
    
    sex_list = ['male', 'female']
    selected_sex = st.multiselect(
        "👥 **Sexe**",
        options=sex_list,
        default=sex_list,
        format_func=lambda x: "👨 Homme" if x == "male" else "👩 Femme"
    )
    
    age_list = list(df['age_group'].unique())
    selected_age = st.multiselect(
        "🎂 **Tranche d'âge**",
        options=age_list,
        default=age_list
    )
    
    st.markdown("---")
    st.markdown("### 📊 **Navigation**")
    
    # 4 PAGES comme demandé dans l'examen
    page = st.radio(
        "",
        ["🏠 Vue Générale", "📈 Analyse de Survie", "🎛️ Filtres Interactifs", "📋 Données Brutes"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Déconnexion
    if st.button("🚪 Se déconnecter", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

# Application des filtres
filtered_df = df[
    (df['class'].isin(selected_class)) &
    (df['sex'].isin(selected_sex)) &
    (df['age_group'].isin(selected_age))
]

log_interaction(page, {'class': selected_class, 'sex': selected_sex, 'age': selected_age})

# ============================================
# Header
# ============================================
st.markdown('<p class="main-title">🚢 Titanic Dashboard</p>', unsafe_allow_html=True)
st.markdown("*Analyse interactive des facteurs de survie du RMS Titanic*")
st.markdown("---")

# ============================================
# PAGE 1 - VUE GÉNÉRALE
# ============================================
if page == "🏠 Vue Générale":
    st.markdown('<p class="section-title">📊 Indicateurs clés</p>', unsafe_allow_html=True)
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{len(filtered_df):,}</div>
            <div class="kpi-label">👥 Total passagers</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{filtered_df['survived'].mean()*100:.1f}%</div>
            <div class="kpi-label">💀 Taux de survie</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">{filtered_df['age'].mean():.1f} ans</div>
            <div class="kpi-label">📅 Âge moyen</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-value">${filtered_df['fare'].mean():.2f}</div>
            <div class="kpi-label">💰 Prix moyen du billet</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">📊 Visualisations</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_class = px.pie(
            filtered_df, 
            names='class', 
            title='Répartition par classe',
            color_discrete_sequence=['#00d4ff', '#ff6b6b', '#f9ca24'],
            hole=0.4
        )
        fig_class.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title_font_color='white'
        )
        st.plotly_chart(fig_class, use_container_width=True)
    
    with col2:
        survival_sex = filtered_df.groupby('sex')['survived'].mean() * 100
        fig_sex = px.bar(
            x=['👨 Hommes', '👩 Femmes'],
            y=survival_sex.values,
            title='Taux de survie par sexe',
            text=[f"{v:.1f}%" for v in survival_sex.values],
            color=['#ff6b6b', '#00d4ff']
        )
        fig_sex.update_traces(textposition='outside')
        fig_sex.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title_font_color='white',
            xaxis_title='',
            yaxis_title='Taux de survie (%)',
            yaxis_range=[0, 100]
        )
        st.plotly_chart(fig_sex, use_container_width=True)
    
    # Distribution des âges
    fig_age = px.histogram(
        filtered_df, 
        x='age', 
        nbins=30, 
        title='Distribution des âges',
        color_discrete_sequence=['#00d4ff'],
        marginal='box'
    )
    fig_age.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title_font_color='white'
    )
    st.plotly_chart(fig_age, use_container_width=True)

  # ============================================
  # JOB 2: Generate Report & Upload to Nexus
  # ============================================
  generate-report:
    needs: lint-and-test
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    
    - name: Setup Python 3.11
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install pandas seaborn ydata-profiling
    
    - name: Generate HTML report
      run: |
        python -c "
import seaborn as sns
import pandas as pd
from ydata_profiling import ProfileReport

print('📊 Loading Titanic dataset...')
df = sns.load_dataset('titanic')

print('🧹 Cleaning data...')
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df['deck'] = df['deck'].astype(str).fillna('Unknown')

print('📝 Generating report...')
profile = ProfileReport(df, title='Titanic Dataset Report', explorative=True)
profile.to_file('titanic-report.html')

print('✅ Report generated: titanic-report.html')
"
    
    - name: Upload report as artifact (GitHub)
      uses: actions/upload-artifact@v4
      with:
        name: titanic-report
        path: titanic-report.html
    
    - name: Upload report to Nexus
      if: false
      env:
        NEXUS_USER: ${{ secrets.NEXUS_USERNAME }}
        NEXUS_PASS: ${{ secrets.NEXUS_PASSWORD }}
        NEXUS_URL: ${{ secrets.NEXUS_URL }}
      run: |
        echo "📤 Upload du rapport vers Nexus..."
        
        if [ -f "titanic-report.html" ]; then
          echo "✅ Fichier trouvé: titanic-report.html"
          ls -la titanic-report.html
        else
          echo "❌ Fichier non trouvé!"
          exit 1
        fi
        
        curl -v -u $NEXUS_USER:$NEXUS_PASS \
          --upload-file titanic-report.html \
          "$NEXUS_URL/repository/titanic-reports/titanic-report-v${{ github.run_number }}.html"
        
        if [ $? -eq 0 ]; then
          echo "✅ Rapport uploadé avec succès vers Nexus"
          echo "📍 URL: $NEXUS_URL/repository/titanic-reports/titanic-report-v${{ github.run_number }}.html"
        else
          echo "⚠️ Échec de l'upload vers Nexus"
        fi

# ============================================
# PAGE 3 - FILTRES INTERACTIFS
# ============================================
elif page == "🎛️ Filtres Interactifs":
    st.markdown('<p class="section-title">🎛️ Filtres interactifs avancés</p>', unsafe_allow_html=True)
    
    st.info("💡 Utilisez les filtres dans la barre latérale gauche pour explorer les données en temps réel")
    
    # Affichage des filtres actifs
    st.subheader("📌 Filtres actuellement appliqués")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"**🏷️ Classe:** {', '.join(selected_class)}")
    with col2:
        st.markdown(f"**👥 Sexe:** {', '.join(['Homme' if s=='male' else 'Femme' for s in selected_sex])}")
    with col3:
        st.markdown(f"**🎂 Tranche d'âge:** {', '.join(selected_age)}")
    
    st.markdown("---")
    
    # Visualisation interactive
    st.subheader("📊 Impact des filtres sur la survie")
    
    # Graphique comparatif avant/après filtres
    fig_comparison = go.Figure()
    fig_comparison.add_trace(go.Bar(
        name='Avant filtres',
        x=['Survie globale', 'Femmes', 'Hommes', '1ère classe'],
        y=[
            df['survived'].mean() * 100,
            df[df['sex']=='female']['survived'].mean() * 100,
            df[df['sex']=='male']['survived'].mean() * 100,
            df[df['class']=='First']['survived'].mean() * 100
        ],
        marker_color='#64748b'
    ))
    fig_comparison.add_trace(go.Bar(
        name='Après filtres',
        x=['Survie globale', 'Femmes', 'Hommes', '1ère classe'],
        y=[
            filtered_df['survived'].mean() * 100,
            filtered_df[filtered_df['sex']=='female']['survived'].mean() * 100 if len(filtered_df[filtered_df['sex']=='female']) > 0 else 0,
            filtered_df[filtered_df['sex']=='male']['survived'].mean() * 100 if len(filtered_df[filtered_df['sex']=='male']) > 0 else 0,
            filtered_df[filtered_df['class']=='First']['survived'].mean() * 100 if len(filtered_df[filtered_df['class']=='First']) > 0 else 0
        ],
        marker_color='#00d4ff'
    ))
    fig_comparison.update_layout(
        title="Comparaison avant/après filtres",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        barmode='group',
        yaxis_title="Taux de survie (%)"
    )
    st.plotly_chart(fig_comparison, use_container_width=True)
    
    # Statistiques détaillées
    with st.expander("📊 Statistiques détaillées", expanded=True):
        st.dataframe(filtered_df.describe(), use_container_width=True)

# ============================================
# PAGE 4 - DONNÉES BRUTES
# ============================================
elif page == "📋 Données Brutes":
    st.markdown('<p class="section-title">📋 Données des passagers</p>', unsafe_allow_html=True)
    
    # Recherche
    search = st.text_input("🔍 Rechercher un passager", placeholder="Nom...")
    
    if search:
        if 'name' in filtered_df.columns:
            display_df = filtered_df[filtered_df['name'].str.contains(search, case=False, na=False)]
        else:
            display_df = filtered_df
        st.info(f"🔎 {len(display_df)} résultat(s) trouvé(s)")
    else:
        display_df = filtered_df
    
    # Pagination
    col1, col2 = st.columns([1, 3])
    with col1:
        page_size = st.selectbox("Lignes par page", [10, 25, 50, 100])
    with col2:
        total_pages = max(1, (len(display_df) + page_size - 1) // page_size)
        page_number = st.number_input("Page", min_value=1, max_value=total_pages, value=1)
    
    start_idx = (page_number - 1) * page_size
    end_idx = min(start_idx + page_size, len(display_df))
    
    st.caption(f"Affichage des lignes {start_idx + 1} à {end_idx} sur {len(display_df)}")
    
    st.dataframe(display_df.iloc[start_idx:end_idx], use_container_width=True, height=500)
    
    # Export CSV
    csv = display_df.to_csv(index=False)
    st.download_button(
        "📥 Télécharger les données (CSV)",
        csv,
        "titanic_data.csv",
        "text/csv",
        use_container_width=True
    )

# ============================================
# Footer
# ============================================
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #64748b; padding: 20px;">
        🚢 <strong>Titanic Dashboard</strong> | Données historiques du RMS Titanic (1912)<br>
        <small>© 2025 - Projet DevOps Data/IA</small>
    </div>
    """,
    unsafe_allow_html=True
)