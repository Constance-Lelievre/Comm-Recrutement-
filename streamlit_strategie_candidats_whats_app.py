import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="Stratégie Candidats WhatsApp",
    layout="wide",
    page_background_color="white",  # Fond blanc
    initial_sidebar_state="collapsed"  # Masque la sidebar si tu ne l'utilises pas
)

# Style CSS pour centrer le contenu et texte noir
st.markdown("""
<style>
    .stApp {
        background-color: white;
        color: black;
    }
    .stMarkdown, .stTitle, .stHeader, .stWrite {
        text-align: center;
        color: black;
    }
    .stButton>button {
        color: black;
        background-color: white;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        color: black;
        background-color: white;
    }
    .st-bf {  /* Pour les colonnes */
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGOS ---
col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.image("1.png", width=100)
with col3:
    st.image("9914549e-8403-4fbb-9b00-938454800f08.jpg", width=100)
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
st.write("- Les candidats invitent leurs
