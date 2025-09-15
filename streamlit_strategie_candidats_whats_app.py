import streamlit as st

# --- CONFIG PAGE ---
st.set_page_config(page_title="Stratégie Candidats WhatsApp", layout="wide")

# --- LOGOS ---
col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.image("1.png", width=100)  # ton logo entreprise
with col3:
    st.image("9914549e-8403-4fbb-9b00-938454800f08.jpg", width=100)  # logo WhatsApp

st.markdown("---")

# --- CONTENU DES SLIDES (TRAME SIMPLIFIÉE) ---
slides = [
    {
        "title": "Stratégie Candidats WhatsApp",
        "content": [
            "Objectifs et contexte"
        ]
    },
    {
        "title": "Objectifs",
        "content": [
            "Construire une communauté qualifiée de candidats",
            "Diffuser directement les offres d’emploi",
            "Encourager le partage entre pairs",
            "Améliorer la réactivité aux offres"
        ]
    },
    {
        "title": "Concept général",
        "content": [
            "Inviter candidats retenus et écartés à rejoindre WhatsApp",
            "Segmentation par secteur ou localisation",
            "Publication d’offres directement dans les canaux",
            "Les candidats invitent leurs contacts similaires"
        ]
    },
    {
        "title": "Groupes vs Chaînes",
        "content": [
            "Groupes : interaction bidirectionnelle",
            "Chaînes : diffusion unidirectionnelle",
            "Préconisation : utiliser les chaînes pour diffuser"
        ]
    },
    {
        "title": "Segmentation",
        "content": [
            "Par secteur (IT, santé, industrie…)",
            "Par région",
            "Possibilité de combiner secteur + région"
        ]
    },
    {
        "title": "Intégration Recruitee",
        "content": [
            "Export automatique des candidats",
            "Invitations automatisées aux bons segments",
            "Suivi centralisé de la base"
        ]
    },
    {
        "title": "WhatsApp Business",
        "content": [
            "API Cloud, catalogues, messages automatisés",
            "Tarification officielle Meta (France 2025) : environ 0,1186 € par message marketing",
            "Pas de coût fixe Meta ; frais possibles si prestataire tiers",
            "Automatisation et suivi à grande échelle"
        ]
    },
    {
        "title": "Mesure & KPIs",
        "content": [
            "Nombre d’abonnés par chaîne",
            "Taux de clics sur liens trackés",
            "Nombre de candidatures issues de WhatsApp",
            "Croissance mensuelle de la base",
            "Engagement (partages, réponses)"
        ]
    },
    {
        "title": "Roadmap 30 jours",
        "content": [
            "S1 : création chaînes + intégration Recruitee",
            "S2 : segmentation et invitations",
            "S3 : publication offres et contenus",
            "S4 : suivi KPIs et ajustements"
        ]
    },
    {
        "title": "Résultat attendu",
        "content": [
            "Audience qualifiée et réactive",
            "Diffusion rapide des offres",
            "Suivi précis du ROI via KPIs",
            "Canal propriétaire complémentaire aux emails"
        ]
    }
]

# --- GESTION DE L'ÉTAT DE PAGE ---
if "page" not in st.session_state:
    st.session_state.page = 0

# --- NAVIGATION ---
col_prev, col_next = st.columns([1,1])
with col_prev:
    if st.button("⬅️ Précédent") and st.session_state.page > 0:
        st.session_state.page -= 1
with col_next:
    if st.button("Suivant ➡️") and st.session_state.page < len(slides)-1:
        st.session_state.page += 1

# --- AFFICHAGE SLIDE ---
slide = slides[st.session_state.page]
st.header(f"Slide {st.session_state.page+1} / {len(slides)} : {slide['title']}")
for bullet in slide["content"]:
    st.write(f"- {bullet}")
