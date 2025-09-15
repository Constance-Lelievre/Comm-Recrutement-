import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="Stratégie Candidats WhatsApp",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STYLE CSS ---
st.markdown("""
<style>
    /* Fond blanc, texte bleu par défaut */
    .stApp {
        background-color: white;
        color: #1E90FF;
        font-size: 18px;
    }
    /* Centrer TOUS les éléments enfants de .stApp */
    .stApp > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }
    /* Centrer les titres et sous-titres, couleur bleue, taille augmentée */
    h1, h2, h3, h4, h5, h6, .stTitle, .stHeader {
        text-align: center !important;
        width: 100%;
        color: #1E90FF !important;
        font-size: 24px !important;
        margin: 2rem 0 1rem 0 !important;
    }
    /* Centrer et styliser les listes à puces */
    ul {
        text-align: left !important;
        list-style-position: inside;
        padding-left: 1em !important;
        width: 100%;
        color: #1E90FF !important;
        line-height: 1.8;
        font-size: 20px !important;
        margin: 0 auto !important;
        max-width: 800px;
    }
    /* Centrer le texte des st.write et les listes */
    .stMarkdown, .stMarkdown p {
        text-align: center !important;
        width: 100%;
        color: #1E90FF !important;
        font-size: 20px !important;
        margin: 0.5rem auto !important;
        max-width: 800px;
    }
    /* Centrer les images */
    .stImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    /* Masquer la sidebar */
    .st-emotion-cache-1v0mbj {
        display: none;
    }
    /* Taille du titre principal */
    h1 {
        font-size: 32px !important;
        margin: 2rem 0 1.5rem 0 !important;
    }
    /* Espacement uniforme entre les sections */
    .stMarkdown, .stWrite {
        margin-bottom: 1.5rem !important;
    }
    /* Centrer les colonnes des logos */
    .stColumn > div {
        display: flex;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGOS ---
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image("1.png", width=100)
with col3:
    st.image("9914549e-8403-4fbb-9b00-938454800f08.jpg", width=100)
st.markdown("---")

# --- CONTENU DE LA PAGE ---
st.title("Stratégie Candidats WhatsApp")

# Utilise st.markdown pour les listes à puces (meilleur contrôle du style)
def section(title, items):
    st.header(title)
    items_html = "".join(f"<li>{item}</li>" for item in items)
    st.markdown(f"<ul>{items_html}</ul>", unsafe_allow_html=True)

# Objectifs
section("Objectifs", [
    "Construire une communauté qualifiée de candidats",
    "Diffuser directement les offres d’emploi",
    "Encourager le partage entre pairs",
    "Améliorer la réactivité aux offres"
])

# Concept général
section("Concept général", [
    "Inviter candidats retenus et écartés à rejoindre WhatsApp",
    "Segmentation par secteur ou localisation",
    "Publication d’offres directement dans les canaux",
    "Les candidats invitent leurs contacts similaires"
])

# Groupes vs Chaînes
section("Groupes vs Chaînes", [
    "Groupes : interaction bidirectionnelle",
    "Chaînes : diffusion unidirectionnelle",
    "Préconisation : utiliser les chaînes pour diffuser"
])

# Segmentation
section("Segmentation", [
    "Par secteur (IT, santé, industrie…)",
    "Par région",
    "Possibilité de combiner secteur + région"
])

# Intégration Jarvi
section("Intégration Jarvi", [
    "Export automatique des candidats depuis Jarvi",
    "Invitations automatisées aux bons segments",
    "Suivi centralisé de la base"
])

# WhatsApp Business
section("WhatsApp Business", [
    "API Cloud, catalogues, messages automatisés",
    "Tarification officielle Meta (France 2025) : environ 0,1186 € par message marketing",
    "Pas de coût fixe Meta ; frais possibles si prestataire tiers",
    "Automatisation et suivi à grande échelle"
])

# Mesure & KPIs
section("Mesure & KPIs", [
    "Nombre d’abonnés par chaîne",
    "Taux de clics sur liens trackés",
    "Nombre de candidatures issues de WhatsApp",
    "Croissance mensuelle de la base",
    "Engagement (partages, réponses)"
])

# Roadmap 30 jours
section("Roadmap 30 jours", [
    "S1 : création chaînes + intégration Jarvi",
    "S2 : segmentation et invitations",
    "S3 : publication offres et contenus",
    "S4 : suivi KPIs et ajustements"
])

# Résultat attendu
section("Résultat attendu", [
    "Audience qualifiée et réactive",
    "Diffusion rapide des offres",
    "Suivi précis du ROI via KPIs",
    "Canal propriétaire complémentaire aux emails"
])
