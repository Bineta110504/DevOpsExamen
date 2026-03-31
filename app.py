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

import streamlit as st
from data.loader import load_data
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# CONFIG
st.set_page_config(
    page_title="Titanic Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD DATA
df = load_data()

# ✅ CORRECTION IMPORTANTE
df_filtered = df.copy()

# SESSION LOGIN
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN
if not st.session_state.logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong credentials")

# DASHBOARD
else:

    # SIDEBAR
    with st.sidebar:
        st.title("Filtres")

        classe = st.multiselect(
            "Classe",
            options=sorted(df['pclass'].unique()),
            default=sorted(df['pclass'].unique())
        )

        sexe = st.multiselect(
            "Sexe",
            options=df['sex'].unique(),
            default=df['sex'].unique()
        )

        age_range = st.slider(
            "Age",
            int(df['age'].min()),
            int(df['age'].max()),
            (int(df['age'].min()), int(df['age'].max()))
        )

        fare_range = st.slider(
            "Fare",
            float(df['fare'].min()),
            float(df['fare'].max()),
            (float(df['fare'].min()), float(df['fare'].max()))
        )

    # ✅ FILTRAGE CORRECT (APRÈS sidebar)
    df_filtered = df[
        (df['pclass'].isin(classe)) &
        (df['sex'].isin(sexe)) &
        (df['age'] >= age_range[0]) &
        (df['age'] <= age_range[1]) &
        (df['fare'] >= fare_range[0]) &
        (df['fare'] <= fare_range[1])
    ]

    # HEADER
    st.title("🚢 Titanic Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Passagers", len(df_filtered))
    col2.metric("Taux survie", f"{df_filtered['survived'].mean()*100:.1f}%")
    col3.metric("Age moyen", f"{df_filtered['age'].mean():.1f}")

    # GRAPH 1
    fig1 = px.histogram(df_filtered, x="age", nbins=30)
    st.plotly_chart(fig1, use_container_width=True)

    # GRAPH 2
    fig2 = px.pie(
        df_filtered,
        names="survived",
        title="Survie"
    )
    st.plotly_chart(fig2, use_container_width=True)

    # GRAPH 3
    fig3 = px.bar(
        df_filtered.groupby("sex")["survived"].mean().reset_index(),
        x="sex",
        y="survived"
    )
    st.plotly_chart(fig3, use_container_width=True)

    # EXPORT
    csv = df_filtered.to_csv(index=False)

    st.download_button(
        label="📥 Télécharger CSV",
        data=csv,
        file_name="titanic_filtered.csv",
        mime="text/csv"
    )

    # TABLE
    st.dataframe(df_filtered, use_container_width=True)