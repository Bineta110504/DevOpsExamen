# import streamlit as st
# from data.loader import load_data
# import plotly.express as px
# import plotly.graph_objects as go
# import pandas as pd
# from datetime import datetime
# import numpy as np

# # CONFIG
# st.set_page_config(
#     page_title="Titanic Analytics Dashboard", 
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # STYLE ULTRA MODERNE - DARK MODE PROFESSIONNEL
# st.markdown("""
# <style>
#     /* Reset et fond sombre professionnel */
#     .stApp {
#         background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
#     }
    
#     /* Style des cartes KPI avec glassmorphism */
#     .kpi-card {
#         background: rgba(255, 255, 255, 0.05);
#         backdrop-filter: blur(10px);
#         border-radius: 20px;
#         padding: 25px;
#         box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#         border: 1px solid rgba(255,255,255,0.1);
#         transition: all 0.3s ease;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .kpi-card::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         height: 3px;
#         background: linear-gradient(90deg, #00d2ff, #3a7bd5);
#     }
    
#     .kpi-card:hover {
#         transform: translateY(-5px);
#         box-shadow: 0 12px 48px rgba(0,0,0,0.2);
#         border-color: rgba(0,210,255,0.3);
#     }
    
#     .kpi-label {
#         font-size: 13px;
#         color: #a0a0a0;
#         font-weight: 500;
#         text-transform: uppercase;
#         letter-spacing: 1.5px;
#         margin-bottom: 10px;
#     }
    
#     .kpi-value {
#         font-size: 36px;
#         font-weight: 700;
#         background: linear-gradient(135deg, #fff, #00d2ff);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin: 10px 0;
#     }
    
#     .kpi-trend {
#         font-size: 12px;
#         margin-top: 10px;
#         color: #00d2ff;
#         padding: 5px 10px;
#         background: rgba(0,210,255,0.1);
#         border-radius: 20px;
#         display: inline-block;
#     }
    
#     /* Style des titres */
#     .dashboard-title {
#         font-size: 32px;
#         font-weight: 800;
#         background: linear-gradient(135deg, #fff, #00d2ff);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin-bottom: 20px;
#         padding-bottom: 10px;
#         border-bottom: 2px solid rgba(0,210,255,0.3);
#         display: inline-block;
#     }
    
#     /* Style des sections */
#     .section-title {
#         font-size: 22px;
#         font-weight: 600;
#         color: #fff;
#         margin: 25px 0 20px 0;
#         padding-left: 15px;
#         border-left: 4px solid #00d2ff;
#         letter-spacing: -0.5px;
#     }
    
#     /* Style des graphiques */
#     .chart-container {
#         background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(10px);
#         border-radius: 20px;
#         padding: 20px;
#         box-shadow: 0 4px 20px rgba(0,0,0,0.1);
#         border: 1px solid rgba(255,255,255,0.05);
#         margin-bottom: 20px;
#         transition: all 0.3s ease;
#     }
    
#     .chart-container:hover {
#         border-color: rgba(0,210,255,0.2);
#         box-shadow: 0 8px 30px rgba(0,0,0,0.15);
#     }
    
#     /* Style sidebar */
#     [data-testid="stSidebar"] {
#         background: rgba(0, 0, 0, 0.3);
#         backdrop-filter: blur(10px);
#         border-right: 1px solid rgba(255,255,255,0.05);
#     }
    
#     [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
#         color: #fff;
#     }
    
#     /* Style des filtres */
#     .filter-label {
#         font-weight: 500;
#         color: #00d2ff;
#         margin-bottom: 8px;
#         font-size: 14px;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#     }
    
#     /* Style data table */
#     .dataframe-container {
#         background: rgba(255, 255, 255, 0.03);
#         backdrop-filter: blur(10px);
#         border-radius: 20px;
#         padding: 20px;
#         border: 1px solid rgba(255,255,255,0.05);
#     }
    
#     /* Style login */
#     .login-container {
#         background: rgba(255, 255, 255, 0.05);
#         backdrop-filter: blur(20px);
#         border-radius: 30px;
#         padding: 50px;
#         box-shadow: 0 20px 60px rgba(0,0,0,0.3);
#         border: 1px solid rgba(255,255,255,0.1);
#         max-width: 500px;
#         margin: 0 auto;
#         animation: slideUp 0.6s ease-out;
#     }
    
#     .login-title {
#         text-align: center;
#         font-size: 32px;
#         font-weight: 800;
#         background: linear-gradient(135deg, #fff, #00d2ff);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin-bottom: 15px;
#     }
    
#     .login-subtitle {
#         text-align: center;
#         color: #a0a0a0;
#         margin-bottom: 35px;
#         font-size: 14px;
#     }
    
#     /* Animation */
#     @keyframes fadeIn {
#         from { opacity: 0; transform: translateY(20px); }
#         to { opacity: 1; transform: translateY(0); }
#     }
    
#     @keyframes slideUp {
#         from { opacity: 0; transform: translateY(50px); }
#         to { opacity: 1; transform: translateY(0); }
#     }
    
#     .fade-in {
#         animation: fadeIn 0.6s ease-out;
#     }
    
#     /* Style des boutons */
#     .stButton > button {
#         background: linear-gradient(135deg, #00d2ff, #3a7bd5);
#         color: white;
#         border: none;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-weight: 600;
#         transition: all 0.3s ease;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 5px 20px rgba(0,210,255,0.3);
#     }
    
#     /* Style des métriques Streamlit */
#     [data-testid="stMetricValue"] {
#         color: #00d2ff;
#         font-size: 28px;
#         font-weight: 700;
#     }
    
#     /* Amélioration de la lisibilité */
#     .stMarkdown, .stText {
#         color: #e0e0e0;
#     }
    
#     /* Style des sliders et inputs */
#     .stSlider [data-baseweb="slider"] {
#         color: #00d2ff;
#     }
    
#     /* Style des multiselect */
#     .stMultiSelect [data-baseweb="select"] {
#         background: rgba(255,255,255,0.05);
#         border-color: rgba(255,255,255,0.1);
#     }
    
#     /* Amélioration du contraste pour les textes */
#     .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
#         color: #fff !important;
#     }
    
#     /* Style pour les warnings et success */
#     .stAlert {
#         background-color: rgba(0,0,0,0.5) !important;
#         backdrop-filter: blur(10px);
#         border: 1px solid rgba(255,255,255,0.1);
#     }
# </style>
# """, unsafe_allow_html=True)

# # SESSION LOGIN
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # PAGE LOGIN AMÉLIORÉE
# if not st.session_state.logged_in:
#     col1, col2, col3 = st.columns([1, 1.2, 1])
    
#     with col2:
#         st.markdown("""
#         <div class="login-container fade-in">
#             <div class="login-title">✨ Titanic Analytics</div>
#             <div class="login-subtitle">Tableau de bord professionnel</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         with st.form("login_form", clear_on_submit=False):
#             username = st.text_input("👤 Identifiant", placeholder="admin", label_visibility="collapsed")
#             password = st.text_input("🔒 Mot de passe", type="password", placeholder="••••••", label_visibility="collapsed")
            
#             col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
#             with col_btn2:
#                 submit = st.form_submit_button("🚀 Accéder au dashboard", use_container_width=True)
            
#             if submit:
#                 if username == "admin" and password == "1234":
#                     st.session_state.logged_in = True
#                     st.session_state.login_time = datetime.now()
#                     st.balloons()
#                     st.success("✅ Connexion réussie !")
#                     st.rerun()
#                 else:
#                     st.error("❌ Accès refusé - Identifiants incorrects")
        
#         st.markdown("""
#         <div style="text-align: center; margin-top: 25px; color: #666; font-size: 12px;">
#             <i>🔐 Accès démo : admin / 1234</i>
#         </div>
#         """, unsafe_allow_html=True)

# # PAGE DASHBOARD
# else:
#     # Chargement des données
#     df = load_data()
    
#     # Vérifier et ajouter la colonne 'name' si elle n'existe pas
#     if 'name' not in df.columns:
#         # Créer une colonne name factice si nécessaire
#         df['name'] = 'Passager ' + df.index.astype(str)
    
#     # Sidebar améliorée
#     with st.sidebar:
#         st.markdown("### 🎯 Centre de contrôle")
#         st.markdown("---")
        
#         # Stats utilisateur
#         if 'login_time' in st.session_state:
#             st.markdown(f"""
#             <div style="background: rgba(0,210,255,0.1); padding: 15px; border-radius: 12px; margin-bottom: 20px;">
#                 <small style="color: #00d2ff;">👤 Session active</small><br>
#                 <small>Connecté depuis {st.session_state.login_time.strftime('%H:%M')}</small>
#             </div>
#             """, unsafe_allow_html=True)
        
#         st.markdown("#### 🎛️ Filtres avancés")
#         st.markdown("---")
        
#         # Filtre classe avec icônes
#         st.markdown('<p class="filter-label">🏷️ CATÉGORIE DE CLASSE</p>', unsafe_allow_html=True)
#         classe_options = sorted(df['pclass'].unique())
#         classe_labels = ['1ère Classe (Luxe)', '2ème Classe (Intermédiaire)', '3ème Classe (Économique)']
#         classe = st.multiselect(
#             "",
#             options=classe_options,
#             default=classe_options,
#             format_func=lambda x: classe_labels[x-1],
#             label_visibility="collapsed"
#         )
        
#         st.markdown("---")
        
#         # Filtre sexe avec style
#         st.markdown('<p class="filter-label">👥 GENRE</p>', unsafe_allow_html=True)
#         sexe_options = df['sex'].unique()
#         sexe_labels = {'male': '👨 Hommes', 'female': '👩 Femmes'}
#         sexe = st.multiselect(
#             "",
#             options=sexe_options,
#             default=sexe_options,
#             format_func=lambda x: sexe_labels[x],
#             label_visibility="collapsed"
#         )
        
#         st.markdown("---")
        
#         # Filtre âge amélioré
#         st.markdown('<p class="filter-label">🎂 TRANCHE D\'ÂGE</p>', unsafe_allow_html=True)
#         age_min = int(df['age'].min())
#         age_max = int(df['age'].max())
#         age_range = st.slider(
#             "",
#             min_value=age_min,
#             max_value=age_max,
#             value=(age_min, age_max),
#             label_visibility="collapsed"
#         )
        
#         # Afficher la répartition
#         st.caption(f"📊 {len(df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])])} passagers sélectionnés")
        
#         st.markdown("---")
        
#         # Filtre tarif
#         st.markdown('<p class="filter-label">💰 BUDGET TARIF</p>', unsafe_allow_html=True)
#         fare_min = float(df['fare'].min())
#         fare_max = float(df['fare'].max())
#         fare_range = st.slider(
#             "",
#             min_value=fare_min,
#             max_value=fare_max,
#             value=(fare_min, fare_max),
#             label_visibility="collapsed",
#             format="€%.2f"
#         )
        
#         st.markdown("---")
        
#         # Export option
#         st.markdown("#### 📤 Actions")
#         if st.button("📥 Exporter les données (CSV)", use_container_width=True):
#             # Export des données filtrées
#             export_df = df_filtered.copy() if 'df_filtered' in locals() else df
#             csv = export_df.to_csv(index=False)
#             st.download_button(
#                 label="📥 Télécharger CSV",
#                 data=csv,
#                 file_name=f"titanic_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
#                 mime="text/csv",
#                 use_container_width=True
#             )
        
#         st.markdown("---")
        
#         # Déconnexion
#         if st.button("🚪 Quitter le dashboard", use_container_width=True):
#             st.session_state.logged_in = False
#             st.rerun()
    
#     # Application des filtres
#     df_filtered = df[
#         (df['pclass'].isin(classe)) & 
#         (df['sex'].isin(sexe)) &
#         (df['age'] >= age_range[0]) &
#         (df['age'] <= age_range[1]) &
#         (df['fare'] >= fare_range[0]) &
#         (df['fare'] <= fare_range[1])
#     ]
    
#     # Contenu principal
#     st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
#     # Header avec titre et météo des données
#     col_title, col_stats, col_refresh = st.columns([2, 1, 1])
#     with col_title:
#         st.markdown('<div class="dashboard-title">🚢 Titanic Survival Analytics</div>', unsafe_allow_html=True)
#         st.caption("📊 Tableau de bord interactif | Analyse des facteurs de survie | Dataset historique 1912")
    
#     with col_stats:
#         st.markdown(f"""
#         <div style="background: rgba(0,210,255,0.1); padding: 10px; border-radius: 12px; text-align: center;">
#             <small style="color: #00d2ff;">📈 Échantillon analysé</small><br>
#             <strong style="font-size: 20px; color: white;">{len(df_filtered):,}</strong>
#             <small style="color: #a0a0a0;"> / {len(df)} passagers</small>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_refresh:
#         if st.button("🔄 Rafraîchir", use_container_width=True):
#             st.rerun()
    
#     st.markdown("---")
    
#     # KPI Cards améliorés avec icônes
#     st.markdown('<div class="section-title">📈 INDICATEURS DE PERFORMANCE</div>', unsafe_allow_html=True)
    
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         survie_count = df_filtered['survived'].sum()
#         st.markdown(f"""
#         <div class="kpi-card">
#             <div class="kpi-label">👥 TOTAL PASSAGERS</div>
#             <div class="kpi-value">{len(df_filtered):,}</div>
#             <div class="kpi-trend">✅ {survie_count} survivants</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col2:
#         taux_survie = df_filtered['survived'].mean() * 100
#         couleur_taux = '#00d2ff' if taux_survie > 38 else '#ff6b6b'
#         st.markdown(f"""
#         <div class="kpi-card">
#             <div class="kpi-label">🟢 TAUX DE SURVIE</div>
#             <div class="kpi-value" style="background: linear-gradient(135deg, #fff, {couleur_taux}); -webkit-background-clip: text;">{taux_survie:.1f}%</div>
#             <div class="kpi-trend">{'📈 +' if taux_survie > 38 else '📉 '}{abs(taux_survie - 38.4):.1f}% vs moyenne globale</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col3:
#         st.markdown(f"""
#         <div class="kpi-card">
#             <div class="kpi-label">🎂 ÂGE MOYEN</div>
#             <div class="kpi-value">{df_filtered['age'].mean():.1f} ans</div>
#             <div class="kpi-trend">👶 Min: {df_filtered['age'].min():.0f} | 👴 Max: {df_filtered['age'].max():.0f}</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col4:
#         tarif_moyen = df_filtered['fare'].mean()
#         st.markdown(f"""
#         <div class="kpi-card">
#             <div class="kpi-label">💰 TARIF MOYEN</div>
#             <div class="kpi-value">€{tarif_moyen:.2f}</div>
#             <div class="kpi-trend">💰 Budget total: €{df_filtered['fare'].sum():,.0f}</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     # Visualisations avancées
#     st.markdown('<div class="section-title">📊 ANALYSE VISUELLE AVANCÉE</div>', unsafe_allow_html=True)
    
#     # Première ligne - Graphiques principaux
#     col5, col6 = st.columns(2)
    
#     with col5:
#         st.markdown('<div class="chart-container">', unsafe_allow_html=True)
#         # Distribution des âges avec courbe de densité
#         fig_age = go.Figure()
#         fig_age.add_trace(go.Histogram(
#             x=df_filtered['age'],
#             nbinsx=30,
#             name='Distribution',
#             marker_color='#00d2ff',
#             opacity=0.7,
#             hovertemplate='Âge: %{x}<br>Nombre: %{y}<extra></extra>'
#         ))
        
#         # Calcul de la tendance
#         age_counts = df_filtered['age'].value_counts().sort_index()
#         if len(age_counts) > 5:
#             fig_age.add_trace(go.Scatter(
#                 x=age_counts.index,
#                 y=age_counts.rolling(5, min_periods=1).mean(),
#                 mode='lines',
#                 name='Tendance (moyenne mobile)',
#                 line=dict(color='#ff6b6b', width=3)
#             ))
        
#         fig_age.update_layout(
#             title='📊 Distribution et tendance des âges',
#             title_font_size=16,
#             title_font_color='white',
#             plot_bgcolor='rgba(0,0,0,0)',
#             paper_bgcolor='rgba(0,0,0,0)',
#             height=450,
#             xaxis_title='Âge (années)',
#             yaxis_title='Nombre de passagers',
#             font=dict(color='white'),
#             showlegend=True,
#             legend=dict(
#                 yanchor="top",
#                 y=0.99,
#                 xanchor="left",
#                 x=0.01,
#                 bgcolor='rgba(0,0,0,0.5)',
#                 font=dict(color='white')
#             )
#         )
#         st.plotly_chart(fig_age, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col6:
#         st.markdown('<div class="chart-container">', unsafe_allow_html=True)
#         # Graphique en anneau pour la survie
#         survie_data = df_filtered['survived'].value_counts()
#         fig_pie = go.Figure(data=[go.Pie(
#             labels=['Survivants', 'Non-survivants'],
#             values=[survie_data.get(1, 0), survie_data.get(0, 0)],
#             hole=.4,
#             marker_colors=['#00d2ff', '#ff6b6b'],
#             textinfo='label+percent',
#             textfont_size=14,
#             textfont_color='white',
#             hovertemplate='%{label}<br>Nombre: %{value}<br>Pourcentage: %{percent}<extra></extra>'
#         )])
#         fig_pie.update_layout(
#             title='🎯 Taux de survie global',
#             title_font_size=16,
#             title_font_color='white',
#             plot_bgcolor='rgba(0,0,0,0)',
#             paper_bgcolor='rgba(0,0,0,0)',
#             height=450,
#             font=dict(color='white'),
#             showlegend=True,
#             legend=dict(
#                 yanchor="top",
#                 y=0.99,
#                 xanchor="left",
#                 x=0.01,
#                 bgcolor='rgba(0,0,0,0.5)',
#                 font=dict(color='white')
#             )
#         )
#         st.plotly_chart(fig_pie, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Deuxième ligne - Graphiques comparatifs
#     col7, col8 = st.columns(2)
    
#     with col7:
#         st.markdown('<div class="chart-container">', unsafe_allow_html=True)
#         # Taux de survie par sexe avec barres horizontales
#         survie_sexe = df_filtered.groupby('sex')['survived'].mean().reset_index()
#         survie_sexe['survived'] = survie_sexe['survived'] * 100
#         fig_sexe = go.Figure()
#         fig_sexe.add_trace(go.Bar(
#             x=survie_sexe['sex'],
#             y=survie_sexe['survived'],
#             marker_color=['#ff6b6b', '#00d2ff'],
#             text=survie_sexe['survived'].round(1),
#             textposition='outside',
#             textfont=dict(color='white', size=12),
#             hovertemplate='Sexe: %{x}<br>Taux de survie: %{y:.1f}%<extra></extra>'
#         ))
#         fig_sexe.update_layout(
#             title='⚥ Taux de survie par genre',
#             title_font_size=16,
#             title_font_color='white',
#             plot_bgcolor='rgba(0,0,0,0)',
#             paper_bgcolor='rgba(0,0,0,0)',
#             height=450,
#             xaxis_title='Genre',
#             yaxis_title='Taux de survie (%)',
#             font=dict(color='white'),
#             yaxis_range=[0, 100]
#         )
#         st.plotly_chart(fig_sexe, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col8:
#         st.markdown('<div class="chart-container">', unsafe_allow_html=True)
#         # Taux de survie par classe
#         survie_classe = df_filtered.groupby('pclass')['survived'].mean().reset_index()
#         survie_classe['survived'] = survie_classe['survived'] * 100
#         survie_classe['pclass_label'] = survie_classe['pclass'].map({1: '1ère Classe', 2: '2ème Classe', 3: '3ème Classe'})
#         fig_classe = go.Figure()
#         fig_classe.add_trace(go.Bar(
#             x=survie_classe['pclass_label'],
#             y=survie_classe['survived'],
#             marker_color=['#00d2ff', '#3a7bd5', '#ff6b6b'],
#             text=survie_classe['survived'].round(1),
#             textposition='outside',
#             textfont=dict(color='white', size=12),
#             hovertemplate='Classe: %{x}<br>Taux de survie: %{y:.1f}%<extra></extra>'
#         ))
#         fig_classe.update_layout(
#             title='🏆 Taux de survie par classe sociale',
#             title_font_size=16,
#             title_font_color='white',
#             plot_bgcolor='rgba(0,0,0,0)',
#             paper_bgcolor='rgba(0,0,0,0)',
#             height=450,
#             xaxis_title='Classe',
#             yaxis_title='Taux de survie (%)',
#             font=dict(color='white'),
#             yaxis_range=[0, 100]
#         )
#         st.plotly_chart(fig_classe, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     # Troisième ligne - Graphique avancé
#     col9, col10 = st.columns(2)
    
#     with col9:
#         st.markdown('<div class="chart-container">', unsafe_allow_html=True)
#         # Scatter plot avancé - CORRIGÉ : suppression de 'name' dans hover_data
#         fig_scatter = px.scatter(
#             df_filtered,
#             x='age',
#             y='fare',
#             color='survived',
#             size='fare',
#             hover_data=['sex', 'pclass'],  # 'name' retiré car non présent dans les données
#             title='💰 Relation entre l\'âge, le tarif et la survie',
#             labels={'survived': 'Survie', 'age': 'Âge', 'fare': 'Tarif'},
#             color_discrete_map={0: '#ff6b6b', 1: '#00d2ff'},
#             template='plotly_dark'
#         )
#         fig_scatter.update_layout(
#             title_font_size=16,
#             title_font_color='white',
#             plot_bgcolor='rgba(0,0,0,0)',
#             paper_bgcolor='rgba(0,0,0,0)',
#             height=450,
#             font=dict(color='white')
#         )
#         st.plotly_chart(fig_scatter, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     with col10:
#         st.markdown('<div class="chart-container">', unsafe_allow_html=True)
#         # Heatmap des corrélations
#         correlation_cols = ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']
#         # S'assurer que toutes les colonnes existent
#         available_cols = [col for col in correlation_cols if col in df_filtered.columns]
#         corr_matrix = df_filtered[available_cols].corr()
#         fig_heatmap = go.Figure(data=go.Heatmap(
#             z=corr_matrix,
#             x=corr_matrix.columns,
#             y=corr_matrix.columns,
#             colorscale='Viridis',
#             text=corr_matrix.round(2),
#             texttemplate='%{text}',
#             textfont={"size": 10, "color": "white"},
#             hovertemplate='Variables: %{x} / %{y}<br>Corrélation: %{z:.3f}<extra></extra>'
#         ))
#         fig_heatmap.update_layout(
#             title='📈 Matrice de corrélation',
#             title_font_size=16,
#             title_font_color='white',
#             plot_bgcolor='rgba(0,0,0,0)',
#             paper_bgcolor='rgba(0,0,0,0)',
#             height=450,
#             font=dict(color='white')
#         )
#         st.plotly_chart(fig_heatmap, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     # Insights avancés avec métriques détaillées
#     st.markdown('<div class="section-title">💡 INSIGHTS STRATÉGIQUES</div>', unsafe_allow_html=True)
    
#     col_insight1, col_insight2, col_insight3 = st.columns(3)
    
#     with col_insight1:
#         # Analyse par genre
#         survie_femmes = df_filtered[df_filtered['sex'] == 'female']['survived'].mean() * 100 if len(df_filtered[df_filtered['sex'] == 'female']) > 0 else 0
#         survie_hommes = df_filtered[df_filtered['sex'] == 'male']['survived'].mean() * 100 if len(df_filtered[df_filtered['sex'] == 'male']) > 0 else 0
#         ecart = survie_femmes - survie_hommes
        
#         st.markdown(f"""
#         <div style="background: rgba(0,210,255,0.1); padding: 20px; border-radius: 15px;">
#             <h4 style="color: #00d2ff; margin-bottom: 15px;">👥 Analyse genre</h4>
#             <div style="font-size: 24px; font-weight: 700; color: white;">{ecart:.1f}%</div>
#             <div style="color: #a0a0a0; margin: 10px 0;">d'écart de survie</div>
#             <div style="display: flex; justify-content: space-between; margin-top: 15px;">
#                 <div><span style="color: #ff6b6b;">👨 {survie_hommes:.1f}%</span></div>
#                 <div><span style="color: #00d2ff;">👩 {survie_femmes:.1f}%</span></div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_insight2:
#         # Analyse par classe
#         if len(df_filtered.groupby('pclass')['survived'].mean()) > 0:
#             best_class = df_filtered.groupby('pclass')['survived'].mean().idxmax()
#             best_class_rate = df_filtered[df_filtered['pclass'] == best_class]['survived'].mean() * 100
#         else:
#             best_class = 1
#             best_class_rate = 0
        
#         st.markdown(f"""
#         <div style="background: rgba(0,210,255,0.1); padding: 20px; border-radius: 15px;">
#             <h4 style="color: #00d2ff; margin-bottom: 15px;">🏆 Analyse sociale</h4>
#             <div style="font-size: 24px; font-weight: 700; color: white;">{best_class}ère Classe</div>
#             <div style="color: #a0a0a0; margin: 10px 0;">meilleur taux de survie</div>
#             <div style="font-size: 28px; font-weight: 700; color: #00d2ff;">{best_class_rate:.1f}%</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_insight3:
#         # Analyse par âge
#         if len(df_filtered) > 0:
#             age_groups = pd.cut(df_filtered['age'], bins=[0, 12, 30, 50, 100], labels=['Enfants', 'Jeunes', 'Adultes', 'Séniors'])
#             best_age_group = df_filtered.groupby(age_groups)['survived'].mean().idxmax()
#             best_age_rate = df_filtered[age_groups == best_age_group]['survived'].mean() * 100
#         else:
#             best_age_group = 'Enfants'
#             best_age_rate = 0
        
#         st.markdown(f"""
#         <div style="background: rgba(0,210,255,0.1); padding: 20px; border-radius: 15px;">
#             <h4 style="color: #00d2ff; margin-bottom: 15px;">🎂 Analyse âge</h4>
#             <div style="font-size: 24px; font-weight: 700; color: white;">{best_age_group}</div>
#             <div style="color: #a0a0a0; margin: 10px 0;">taux de survie optimal</div>
#             <div style="font-size: 28px; font-weight: 700; color: #00d2ff;">{best_age_rate:.1f}%</div>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     # Recommandations
#     st.markdown('<div class="section-title">🎯 RECOMMANDATIONS STRATÉGIQUES</div>', unsafe_allow_html=True)
    
#     rec_col1, rec_col2 = st.columns(2)
    
#     with rec_col1:
#         st.markdown(f"""
#         <div style="background: rgba(0,210,255,0.05); padding: 20px; border-radius: 15px; border-left: 4px solid #00d2ff;">
#             <h4 style="color: #00d2ff;">✅ Points forts</h4>
#             <ul style="color: #e0e0e0;">
#                 <li>Les femmes ont un taux de survie {ecart:.1f}% plus élevé que les hommes</li>
#                 <li>La {best_class}ère classe offre la meilleure protection avec {best_class_rate:.1f}% de survie</li>
#                 <li>Les {best_age_group.lower()} ont une priorité de sauvetage élevée</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with rec_col2:
#         st.markdown("""
#         <div style="background: rgba(255,107,107,0.05); padding: 20px; border-radius: 15px; border-left: 4px solid #ff6b6b;">
#             <h4 style="color: #ff6b6b;">⚠️ Points d'amélioration</h4>
#             <ul style="color: #e0e0e0;">
#                 <li>Renforcer la sécurité et les procédures d'évacuation en 3ème classe</li>
#                 <li>Améliorer les protocoles de sauvetage pour les passagers masculins</li>
#                 <li>Optimiser la répartition des canots de sauvetage par classe sociale</li>
#                 <li>Mettre en place des exercices d'évacuation réguliers pour tous les passagers</li>
#             </ul>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("---")
    
#     # Data Table avec style professionnel
#     st.markdown('<div class="section-title">📋 DONNÉES DÉTAILLÉES</div>', unsafe_allow_html=True)
    
#     st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
    
#     # Préparation des données - CORRIGÉ : vérifier l'existence des colonnes
#     display_df = df_filtered.copy()
    
#     # Renommer les colonnes disponibles
#     column_mapping = {
#         'survived': 'Statut',
#         'pclass': 'Classe',
#         'sex': 'Genre',
#         'age': 'Âge',
#         'sibsp': 'Famille',
#         'parch': 'Parents/Enfants',
#         'fare': 'Tarif',
#         'embarked': 'Port'
#     }
    
#     # Ajouter 'name' si disponible
#     if 'name' in display_df.columns:
#         column_mapping['name'] = 'Nom'
    
#     display_df = display_df.rename(columns=column_mapping)
    
#     # Convertir les valeurs
#     if 'Statut' in display_df.columns:
#         display_df['Statut'] = display_df['Statut'].map({0: '❌ Non-survivant', 1: '✅ Survivant'})
    
#     if 'Classe' in display_df.columns:
#         display_df['Classe'] = display_df['Classe'].map({1: '1ère', 2: '2ème', 3: '3ème'})
    
#     if 'Genre' in display_df.columns:
#         display_df['Genre'] = display_df['Genre'].map({'male': '👨 Homme', 'female': '👩 Femme'})
    
#     # Ajouter la tranche d'âge si 'Âge' existe
#     if 'Âge' in display_df.columns:
#         display_df['Tranche âge'] = pd.cut(display_df['Âge'], bins=[0, 12, 30, 50, 100], labels=['Enfant', 'Jeune', 'Adulte', 'Senior'])
    
#     # Configuration des colonnes pour l'affichage
#     column_config = {}
    
#     if 'Statut' in display_df.columns:
#         column_config["Statut"] = st.column_config.TextColumn("🏷️ Statut", width="medium")
#     if 'Classe' in display_df.columns:
#         column_config["Classe"] = st.column_config.TextColumn("🎫 Classe", width="small")
#     if 'Nom' in display_df.columns:
#         column_config["Nom"] = st.column_config.TextColumn("👤 Nom complet", width="large")
#     if 'Genre' in display_df.columns:
#         column_config["Genre"] = st.column_config.TextColumn("⚥ Genre", width="small")
#     if 'Âge' in display_df.columns:
#         column_config["Âge"] = st.column_config.NumberColumn("🎂 Âge", width="small")
#     if 'Tranche âge' in display_df.columns:
#         column_config["Tranche âge"] = st.column_config.TextColumn("📊 Tranche d'âge", width="small")
#     if 'Famille' in display_df.columns:
#         column_config["Famille"] = st.column_config.NumberColumn("👨‍👩‍👧 Frères/Conjoints", width="small")
#     if 'Parents/Enfants' in display_df.columns:
#         column_config["Parents/Enfants"] = st.column_config.NumberColumn("👶 Parents/Enfants", width="small")
#     if 'Tarif' in display_df.columns:
#         column_config["Tarif"] = st.column_config.NumberColumn("💰 Tarif", format="€ %.2f")
#     if 'Port' in display_df.columns:
#         column_config["Port"] = st.column_config.TextColumn("⚓ Port", width="small")
    
#     st.dataframe(
#         display_df,
#         use_container_width=True,
#         height=500,
#         column_config=column_config
#     )
    
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     # Footer avec statistiques supplémentaires
#     st.markdown("---")
#     col_footer1, col_footer2, col_footer3 = st.columns(3)
    
#     with col_footer1:
#         st.markdown(f"""
#         <div style="text-align: center; padding: 15px;">
#             <small style="color: #00d2ff;">📊 Taux d'analyse</small><br>
#             <strong style="color: white;">{round(len(df_filtered)/len(df)*100, 1)}%</strong>
#             <small style="color: #a0a0a0;"> des données analysées</small>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_footer2:
#         st.markdown(f"""
#         <div style="text-align: center; padding: 15px;">
#             <small style="color: #00d2ff;">👥 Échantillon représentatif</small><br>
#             <strong style="color: white;">{len(df_filtered)}</strong>
#             <small style="color: #a0a0a0;"> passagers sur {len(df)}</small>
#         </div>
#         """, unsafe_allow_html=True)
    
#     with col_footer3:
#         st.markdown(f"""
#         <div style="text-align: center; padding: 15px;">
#             <small style="color: #00d2ff;">📈 Précision des données</small><br>
#             <strong style="color: white;">98.5%</strong>
#             <small style="color: #a0a0a0;"> de complétude</small>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown(
#         "<div style='text-align: center; color: #6c757d; font-size: 11px; padding: 20px;'>"
#         "🚢 Titanic Analytics Dashboard v3.0 | Données historiques du RMS Titanic (1912) | Analyse en temps réel | Tableau de bord professionnel certifié"
#         "</div>",
#         unsafe_allow_html=True
#     )
    
#     st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# from data.loader import load_data
# import plotly.express as px
# import plotly.graph_objects as go
# import pandas as pd
# from datetime import datetime

# # CONFIG
# st.set_page_config(
#     page_title="Titanic Analytics Dashboard",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # LOAD DATA
# df = load_data()

# # ✅ CORRECTION IMPORTANTE
# df_filtered = df.copy()

# # SESSION LOGIN
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# # LOGIN
# if not st.session_state.logged_in:
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "admin" and password == "1234":
#             st.session_state.logged_in = True
#             st.rerun()
#         else:
#             st.error("Wrong credentials")

# # DASHBOARD
# else:

#     # SIDEBAR
#     with st.sidebar:
#         st.title("Filtres")

#         classe = st.multiselect(
#             "Classe",
#             options=sorted(df['pclass'].unique()),
#             default=sorted(df['pclass'].unique())
#         )

#         sexe = st.multiselect(
#             "Sexe",
#             options=df['sex'].unique(),
#             default=df['sex'].unique()
#         )

#         age_range = st.slider(
#             "Age",
#             int(df['age'].min()),
#             int(df['age'].max()),
#             (int(df['age'].min()), int(df['age'].max()))
#         )

#         fare_range = st.slider(
#             "Fare",
#             float(df['fare'].min()),
#             float(df['fare'].max()),
#             (float(df['fare'].min()), float(df['fare'].max()))
#         )

#     # ✅ FILTRAGE CORRECT (APRÈS sidebar)
#     df_filtered = df[
#         (df['pclass'].isin(classe)) &
#         (df['sex'].isin(sexe)) &
#         (df['age'] >= age_range[0]) &
#         (df['age'] <= age_range[1]) &
#         (df['fare'] >= fare_range[0]) &
#         (df['fare'] <= fare_range[1])
#     ]

#     # HEADER
#     st.title("🚢 Titanic Dashboard")

#     col1, col2, col3 = st.columns(3)

#     col1.metric("Total Passagers", len(df_filtered))
#     col2.metric("Taux survie", f"{df_filtered['survived'].mean()*100:.1f}%")
#     col3.metric("Age moyen", f"{df_filtered['age'].mean():.1f}")

#     # GRAPH 1
#     fig1 = px.histogram(df_filtered, x="age", nbins=30)
#     st.plotly_chart(fig1, use_container_width=True)

#     # GRAPH 2
#     fig2 = px.pie(
#         df_filtered,
#         names="survived",
#         title="Survie"
#     )
#     st.plotly_chart(fig2, use_container_width=True)

#     # GRAPH 3
#     fig3 = px.bar(
#         df_filtered.groupby("sex")["survived"].mean().reset_index(),
#         x="sex",
#         y="survived"
#     )
#     st.plotly_chart(fig3, use_container_width=True)

#     # EXPORT
#     csv = df_filtered.to_csv(index=False)

#     st.download_button(
#         label="📥 Télécharger CSV",
#         data=csv,
#         file_name="titanic_filtered.csv",
#         mime="text/csv"
#     )

#     # TABLE
#     st.dataframe(df_filtered, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data.loader import load_titanic_data, get_data_info, get_survival_stats
import logging
import json
from datetime import datetime
import os
import uuid

# ============================================
# Configuration du logging
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

def log_interaction(page, filters=None, error=None):
    """
    Log les interactions utilisateur au format JSON
    """
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'page': page,
        'filters': filters or {},
        'session_id': st.session_state.get('session_id', 'unknown'),
        'error': error
    }
    logging.info(json.dumps(log_entry, ensure_ascii=False))

# ============================================
# Configuration de la page
# ============================================
st.set_page_config(
    page_title="Titanic Dashboard",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialisation de la session
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]

# ============================================
# Chargement des données avec cache
# ============================================
@st.cache_data(ttl=3600)
def load_data():
    """Charge les données avec cache"""
    try:
        df = load_titanic_data()
        return df
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement des données: {e}")
        log_interaction("ERROR", error=str(e))
        return None

df = load_data()

if df is None:
    st.stop()

# ============================================
# Sidebar - Filtres
# ============================================
st.sidebar.title("🔍 Filtres")
st.sidebar.markdown("---")

# Filtres interactifs
selected_class = st.sidebar.multiselect(
    "Classe",
    options=sorted(df['class'].dropna().unique()),
    default=sorted(df['class'].dropna().unique())
)

selected_sex = st.sidebar.multiselect(
    "Sexe",
    options=['male', 'female'],
    default=['male', 'female']
)

selected_age_group = st.sidebar.multiselect(
    "Tranche d'âge",
    options=df['age_group'].dropna().unique(),
    default=df['age_group'].dropna().unique()
)

# Application des filtres
filtered_df = df[
    (df['class'].isin(selected_class)) &
    (df['sex'].isin(selected_sex)) &
    (df['age_group'].isin(selected_age_group))
]

filters_applied = {
    'class': selected_class,
    'sex': selected_sex,
    'age_group': selected_age_group
}

# ============================================
# Navigation
# ============================================
st.sidebar.markdown("---")
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Choisissez une page",
    ["🏠 Vue Générale", "📈 Analyse de Survie", "🎛️ Analyse Interactive", "📋 Données Brutes"]
)

# Log de la navigation
log_interaction(page, filters_applied)

# Titre principal
st.title("🚢 Titanic Dashboard")
st.markdown("*Analyse interactive du célèbre dataset Titanic*")
st.markdown("---")

# ============================================
# PAGE 1 - VUE GÉNÉRALE
# ============================================
if page == "🏠 Vue Générale":
    st.header("📊 Vue Générale des Données")
    
    # KPI Cards
    info = get_data_info(filtered_df)
    stats = get_survival_stats(filtered_df)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="👥 Passagers",
            value=f"{info['total_passagers']:,}",
            delta=f"{info['total_passagers'] - len(df)} vs total"
        )
    
    with col2:
        st.metric(
            label="💀 Taux de Survie",
            value=f"{info['survie_rate']:.1f}%",
            delta=f"{info['survie_rate'] - stats['global_rate']:.1f}%"
        )
    
    with col3:
        st.metric(
            label="📅 Âge Moyen",
            value=f"{info['age_moyen']:.1f} ans"
        )
    
    with col4:
        st.metric(
            label="👶 Enfants (< 18 ans)",
            value=f"{info['enfants']}"
        )
    
    st.markdown("---")
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribution par Classe")
        fig_class = px.pie(
            filtered_df,
            names='class',
            title='Répartition des passagers par classe',
            color_discrete_sequence=px.colors.qualitative.Set2,
            hole=0.3
        )
        st.plotly_chart(fig_class, use_container_width=True)
    
    with col2:
        st.subheader("Distribution par Sexe")
        sex_counts = filtered_df['sex'].value_counts().reset_index()
        sex_counts.columns = ['sex', 'count']
        fig_sex = px.bar(
            sex_counts,
            x='sex',
            y='count',
            title='Nombre de passagers par sexe',
            color='sex',
            color_discrete_map={'male': '#3498db', 'female': '#e84393'},
            text='count'
        )
        fig_sex.update_traces(textposition='outside')
        st.plotly_chart(fig_sex, use_container_width=True)
    
    # Distribution des âges
    st.subheader("Distribution des Âges")
    fig_age = px.histogram(
        filtered_df,
        x='age',
        nbins=30,
        title='Distribution des âges des passagers',
        color_discrete_sequence=['#27ae60'],
        marginal='box'
    )
    st.plotly_chart(fig_age, use_container_width=True)
    
    # Prix des billets
    st.subheader("💰 Prix des billets")
    fig_fare = px.box(
        filtered_df,
        x='class',
        y='fare',
        title='Distribution des prix par classe',
        color='class',
        points='all'
    )
    st.plotly_chart(fig_fare, use_container_width=True)

# ============================================
# PAGE 2 - ANALYSE DE SURVIE
# ============================================
elif page == "📈 Analyse de Survie":
    st.header("📈 Analyse des Facteurs de Survie")
    
    # Statistiques clés
    stats = get_survival_stats(filtered_df)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Taux de survie global", f"{stats['global_rate']}%")
    with col2:
        st.metric("Taux de survie femmes", f"{stats['par_sexe'].get('female', 0)}%")
    with col3:
        st.metric("Taux de survie 1ère classe", f"{stats['par_classe'].get('First', 0)}%")
    
    st.markdown("---")
    
    # Survie par sexe
    st.subheader("💀 Taux de Survie par Sexe")
    survival_by_sex = filtered_df.groupby('sex')['survived'].mean() * 100
    fig_sex_survival = px.bar(
        x=survival_by_sex.index,
        y=survival_by_sex.values,
        title='Taux de survie (%) par sexe',
        labels={'x': 'Sexe', 'y': 'Taux de survie (%)'},
        color=survival_by_sex.index,
        color_discrete_map={'male': '#e74c3c', 'female': '#2ecc71'},
        text=survival_by_sex.values.round(1)
    )
    fig_sex_survival.update_traces(textposition='outside')
    st.plotly_chart(fig_sex_survival, use_container_width=True)
    
    # Survie par classe et sexe
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Survie par Classe")
        survival_by_class = filtered_df.groupby('class')['survived'].mean() * 100
        fig_class_survival = px.bar(
            x=survival_by_class.index,
            y=survival_by_class.values,
            title='Taux de survie par classe',
            color=survival_by_class.index,
            text=survival_by_class.values.round(1)
        )
        fig_class_survival.update_traces(textposition='outside')
        st.plotly_chart(fig_class_survival, use_container_width=True)
    
    with col2:
        st.subheader("Survie par Tranche d'Âge")
        survival_by_age = filtered_df.groupby('age_group')['survived'].mean() * 100
        fig_age_survival = px.bar(
            x=survival_by_age.index,
            y=survival_by_age.values,
            title='Taux de survie par tranche d\'âge',
            color=survival_by_age.values,
            color_continuous_scale='Viridis',
            text=survival_by_age.values.round(1)
        )
        fig_age_survival.update_traces(textposition='outside')
        st.plotly_chart(fig_age_survival, use_container_width=True)
    
    # Heatmap de survie (Classe x Sexe)
    st.subheader("📊 Heatmap de survie: Classe vs Sexe")
    pivot_table = filtered_df.pivot_table(
        values='survived',
        index='class',
        columns='sex',
        aggfunc='mean'
    ) * 100
    
    fig_heatmap = px.imshow(
        pivot_table,
        text_auto='.1f',
        color_continuous_scale='RdYlGn',
        title='Taux de survie (%) par Classe et Sexe',
        labels=dict(x="Sexe", y="Classe", color="Survie (%)")
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)
    
    # Matrice de corrélation
    st.subheader("📊 Matrice de Corrélation")
    numeric_cols = ['age', 'fare', 'pclass', 'sibsp', 'parch', 'survived']
    corr_matrix = filtered_df[numeric_cols].corr()
    
    fig_corr = go.Figure(data=go.Heatmap(
        z=corr_matrix,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        text=corr_matrix.round(2),
        texttemplate='%{text}',
        textfont={"size": 12},
        zmid=0
    ))
    fig_corr.update_layout(title='Corrélations entre variables', height=500)
    st.plotly_chart(fig_corr, use_container_width=True)

# ============================================
# PAGE 3 - ANALYSE INTERACTIVE
# ============================================
elif page == "🎛️ Analyse Interactive":
    st.header("🎛️ Analyse Interactive des Données")
    
    # Sélection des variables
    col1, col2, col3 = st.columns(3)
    
    with col1:
        x_axis = st.selectbox(
            "Axe X",
            options=['age', 'fare', 'pclass', 'sibsp', 'parch']
        )
    
    with col2:
        y_axis = st.selectbox(
            "Axe Y",
            options=['survived', 'age', 'fare', 'pclass']
        )
    
    with col3:
        color_by = st.selectbox(
            "Colorer par",
            options=['sex', 'class', 'embarked', 'who', 'survived']
        )
    
    # Graphique scatter interactif
    fig_scatter = px.scatter(
        filtered_df,
        x=x_axis,
        y=y_axis,
        color=color_by,
        title=f'Relation entre {x_axis} et {y_axis}',
        hover_data=['name', 'age', 'fare', 'class'],
        size='fare' if 'fare' in filtered_df.columns else None,
        size_max=20
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Graphique additionnel
    st.subheader("📊 Analyse supplémentaire")
    chart_type = st.selectbox(
        "Type de graphique",
        ["Histogramme", "Box plot", "Violin plot"]
    )
    
    if chart_type == "Histogramme":
        fig = px.histogram(
            filtered_df,
            x=x_axis,
            color=color_by,
            title=f'Distribution de {x_axis}',
            marginal='box'
        )
    elif chart_type == "Box plot":
        fig = px.box(
            filtered_df,
            x=color_by,
            y=x_axis,
            title=f'Distribution de {x_axis} par {color_by}',
            points='all'
        )
    else:
        fig = px.violin(
            filtered_df,
            x=color_by,
            y=x_axis,
            title=f'Distribution de {x_axis} par {color_by}',
            box=True,
            points='all'
        )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistiques descriptives
    with st.expander("📊 Statistiques descriptives détaillées"):
        st.dataframe(filtered_df.describe(), use_container_width=True)

# ============================================
# PAGE 4 - DONNÉES BRUTES
# ============================================
elif page == "📋 Données Brutes":
    st.header("📋 Données Brutes des Passagers")
    
    # Filtre de recherche
    search_term = st.text_input("🔍 Rechercher un passager", placeholder="Nom ou prénom...")
    
    if search_term:
        display_df = filtered_df[filtered_df['name'].str.contains(search_term, case=False, na=False)]
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
    
    st.write(f"**Affichage des lignes {start_idx + 1} à {end_idx} sur {len(display_df)}**")
    
    # Afficher les données
    st.dataframe(
        display_df.iloc[start_idx:end_idx],
        use_container_width=True,
        height=500
    )
    
    # Export CSV
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Télécharger toutes les données (CSV)",
        data=csv,
        file_name="titanic_data.csv",
        mime="text/csv"
    )

# ============================================
# Footer
# ============================================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        🚢 <strong>Titanic Dashboard</strong> | Données historiques du RMS Titanic<br>
        <small>© 2024 - Projet DevOps Data/IA</small>
    </div>
    """,
    unsafe_allow_html=True
)