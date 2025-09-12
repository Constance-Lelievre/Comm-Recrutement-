import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Stratégie Candidats WhatsApp", layout="centered")

PPTX_PATH = "/mnt/data/Strategie_Candidats_Whatsapp.pptx"

slides = [
    {"title": "📑 Stratégie Candidats WhatsApp",
     "content": [
         "Diffuser des offres d’emploi ciblées via WhatsApp",
         "Construire et engager une communauté de talents qualifiés"
     ]},

    {"title": "Concept",
     "content": [
         "Chaînes WhatsApp : diffusion d’offres + conseils",
         "Groupes WhatsApp : échanges et qualification des candidats",
         "Suivi engagement : liens trackés + vues sur chaînes",
         "Compatible avec Jarvi et Recruitee pour automatiser et centraliser"
     ]},

    {"title": "Segmentation recommandée",
     "content": [
         "Par secteur : IT, Commercial, Industrie, Santé…",
         "Par localisation : Paris-IDF, Région Sud, Grand Ouest…",
         "Mix secteur + localisation = plus de pertinence"
     ]},

    {"title": "Mise en place",
     "content": [
         "Créer les canaux : chaînes illimitées / groupes max 1 024 membres",
         "Automatiser avec Jarvi ou Recruitee : import, tags, invitations",
         "Lancer la communauté : emailing/LinkedIn + call-to-action"
     ]},

    {"title": "Contenu type",
     "content": [
         "Offres d’emploi (format court)",
         "Conseils CV / Entretien",
         "Actualités sectorielles",
         "Événements networking"
     ]},

    {"title": "KPIs réels et actionnables",
     "content": [
         "Abonnés : nombre total d’abonnés chaîne/groupe",
         "Vues : nombre de vues par publication (visible aux admins)",
         "Clics : liens trackés via Bitly / UTM",
         "Candidatures : formulaire ou lien tracké",
         "⚡ Remarque : le taux d’ouverture WhatsApp classique n’existe pas, on suit vues et clics"
     ]},

    {"title": "WhatsApp Classique vs Business",
     "content": [
         "WhatsApp Classique : gratuit, envoi manuel, vues limitées, pas d’automatisation",
         "WhatsApp Business App : gratuit, mais toujours manuel",
         "WhatsApp Business API/Cloud : automatisation, intégration CRM, suivi livraison et lecture"
     ]},

    {"title": "Pricing WhatsApp Business (France)",
     "content": [
         "Coût par message Marketing : 0,1186 € (source Meta Developers)",
         "Autres types de messages : tarifs différents (utilitaire, authentification)",
         "Pas de coût fixe obligatoire avec Cloud API directement via Meta",
         "Coût fixe possible si fournisseur tiers (50–100 €/mois)",
         "Compatible avec Jarvi et Recruitee pour automatiser et centraliser"
     ]},

    {"title": "Roadmap 30 jours",
     "content": [
         "J1-J7 : Création canaux + paramétrage automatisation",
         "J8-J14 : Import contacts + campagnes d’invitation",
         "J15-J21 : Publication régulière + call-to-action partage",
         "J22-J30 : Analyse KPIs + ajustement segmentation"
     ]},

    {"title": "Résultat attendu",
     "content": [
         "Audience qualifiée et réactive",
         "Diffusion rapide des offres",
         "Effet viral via le partage",
         "KPIs fiables pour mesurer engagement et conversions"
     ]},

    {"title": "WhatsApp Business - Détails & Sources",
     "content": [
         "Fonctionnalités : automatisation, API Cloud, intégration CRM, dashboards",
         "Coût marketing en France : 0,1186 € / message (Meta Developers)",
         "Coûts fixes potentiels : fournisseurs tiers 50–100 €/mois (optionnel)",
         "Sources officielles :",
         " - Meta Developers - Pricing: https://developers.facebook.com/docs/whatsapp/pricing/",
         " - Meta Developers - Cloud API Pricing: https://developers.facebook.com/docs/whatsapp/cloud-api/calling/pricing/"
     ]}
]

st.title("Stratégie Candidats WhatsApp")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", [s['title'] for s in slides])

# Affichage du slide sélectionné
for s in slides:
    if s['title'] == page:
        st.header(s['title'])
        for line in s['content']:
            st.write(f"- {line}")
        break

st.sidebar.markdown("---")

# Bouton de téléchargement pour le PPTX généré
pptx_file = Path(PPTX_PATH)
if pptx_file.exists():
    with open(PPTX_PATH, 'rb') as f:
        btn = st.sidebar.download_button(
            label="📥 Télécharger le PPTX",
            data=f,
            file_name="Strategie_Candidats_Whatsapp.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )
else:
    st.sidebar.info("Le fichier PPTX n'a pas été trouvé sur le serveur.")

st.sidebar.markdown("---")
st.sidebar.markdown("© Cabinet - Stratégie Candidats WhatsApp")

# Footer with sources
st.markdown("---")
st.markdown("**Sources officielles (Meta Developers) :**")
st.markdown("- https://developers.facebook.com/docs/whatsapp/pricing/")
st.markdown("- https://developers.facebook.com/docs/whatsapp/cloud-api/calling/pricing/")
