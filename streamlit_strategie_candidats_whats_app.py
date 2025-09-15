import streamlit as st

st.set_page_config(page_title="Stratégie Candidats WhatsApp", layout="wide")

# --- Initialiser l'état ---
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# --- Définir tes slides ici ---
slides = [
    {
        "title": "Slide 1 : Introduction",
        "content": "Objectifs, contexte et présentation générale de la stratégie WhatsApp."
    },
    {
        "title": "Slide 2 : Segmentation",
        "content": "Segmentation des candidats par secteur et localisation."
    },
    {
        "title": "Slide 3 : WhatsApp Business",
        "content": "Comparatif WhatsApp Classique vs Business et tarification."
    },
    {
        "title": "Slide 4 : KPIs & Roadmap",
        "content": "Indicateurs de suivi, plan de déploiement et résultats attendus."
    }
]

# --- Fonctions de navigation ---
def go_next():
    if st.session_state.slide_index < len(slides) - 1:
        st.session_state.slide_index += 1

def go_prev():
    if st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1

# --- Affichage du contenu ---
current_slide = slides[st.session_state.slide_index]
st.title(current_slide["title"])
st.write(current_slide["content"])

# --- Boutons de navigation ---
col1, col2 = st.columns([1,1])
with col1:
    st.button("⬅️ Précédent", on_click=go_prev)
with col2:
    st.button("Suivant ➡️", on_click=go_next)

st.write(f"Slide {st.session_state.slide_index + 1} / {len(slides)}")

# --- Script JS pour capturer les flèches du clavier ---
keyboard_script = """
<script>
document.addEventListener('keydown', function(e) {
    if(e.key === "ArrowRight"){
        window.parent.postMessage({isStreamlitMessage: true, type: "streamlit:setComponentValue", value: "next"}, "*")
    }
    if(e.key === "ArrowLeft"){
        window.parent.postMessage({isStreamlitMessage: true, type: "streamlit:setComponentValue", value: "prev"}, "*")
    }
});
</script>
"""
st.markdown(keyboard_script, unsafe_allow_html=True)

# --- Récupérer les événements clavier ---
# Astuce : on utilise un widget invisible qui change quand JS envoie "next" ou "prev"
event = st.experimental_get_query_params().get("arrow", [""])[0]

# On lit le paramètre Streamlit spécial si dispo
if "keyboard_nav" not in st.session_state:
    st.session

