import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="Stratégie Candidats WhatsApp", layout="wide")

# --- LOGOS ---
col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.image("1.png", width=100)  # ton logo entreprise
with col3:
    st.image("9914549e-8403-4fbb-9b00-938454800f08.jpg", width=100)  # logo WhatsApp

st.markdown("---")

# --- CONTENU DE LA PAGE ---
st.title("Stratégie Candidats WhatsApp")

# Objectifs
st.header("Objectifs")
st.write("- Construire une communauté qualifiée de candidats")
st.write("- Diffuser directement les offres d’emploi")
st.write("- Encourager le partage entre pairs")
st.write("- Améliorer la réactivité aux offres")

# Concept général
st.header("Concept général")
st.write("- Inviter candidats retenus et écartés à rejoindre WhatsApp")
st.write("- Segmentation par secteur ou localisation")
st.write("- Publication d’offres directement dans les canaux")
st.write("- Les candidats invitent leurs contacts similaires")

# Groupes vs Chaînes
st.header("Groupes vs Chaînes")
st.write("- Groupes : interaction bidirectionnelle")
st.write("- Chaînes : diffusion unidirectionnelle")
st.write("- Préconisation : utiliser les chaînes pour diffuser")

# Segmentation
st.header("Segmentation")
st.write("- Par secteur (IT, santé, industrie…)")
st.write("- Par région")
st.write("- Possibilité de combiner secteur + région")

# Intégration Jarvi
st.header("Intégration Jarvi")
st.write("- Export automatique des candidats depuis Jarvi")
st.write("- Invitations automatisées aux bons segments")
st.write("- Suivi centralisé de la base")

# WhatsApp Business
st.header("WhatsApp Business")
st.write("- API Cloud, catalogues, messages automatisés")
st.write("- Tarification officielle Meta (France 2025) : environ 0,1186 € par message marketing")
st.write("- Pas de coût fixe Meta ; frais possibles si prestataire tiers")
st.write("- Automatisation et suivi à grande échelle")

# Mesure & KPIs
st.header("Mesure & KPIs")
st.write("- Nombre d’abonnés par chaîne")
st.write("- Taux de clics sur liens trackés")
st.write("- Nombre de candidatures issues de WhatsApp")
st.write("- Croissance mensuelle de la base")
st.write("- Engagement (partages, réponses)")

# Roadmap 30 jours
st.header("Roadmap 30 jours")
st.write("- S1 : création chaînes + intégration Jarvi")
st.write("- S2 : segmentation et invitations")
st.write("- S3 : publication offres et contenus")
st.write("- S4 : suivi KPIs et ajustements")

# Résultat attendu
st.header("Résultat attendu")
st.write("- Audience qualifiée et réactive")
st.write("- Diffusion rapide des offres")
st.write("- Suivi précis du ROI via KPIs")
st.write("- Canal propriétaire complémentaire aux emails")
