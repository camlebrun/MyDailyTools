import streamlit as st

st.set_page_config(layout = "wide", page_title = "Home")
st.markdown("<h1 style='text-align: center'>My daily tools</h1>", unsafe_allow_html=True)

st.write("Bienvenue sur la page d'accueil de daily tools !")
st.write("Vous pouvez accéder aux outils suivants :")
st.write("1. Calculatrice de jours")
st.write("2. Différence de dates")
st.write("3. Générateur de liens courts")
st.write("4. Mots de passe forts")
st.write("5. Générateur de QR code")

st.write("J'ai créee cette webapp pour vous aider dans votre quotidien, en centralisant des outils que j'utilise souvent.")
st.balloons()
def page_0():
    st.empty()
def page_2():
    st.empty()

def page3():
    st.empty()



page_names_to_funcs = {
    "Home": page_0,
    "liens_court": page_2,
    "mdp": page3,

}