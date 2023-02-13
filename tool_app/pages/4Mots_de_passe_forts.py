import random
import string
import streamlit as st

st.set_page_config(layout="wide", page_title="Mots de passe forts")
st.markdown("<h1 style='text-align: center'>Mots de passe forts</h1>", unsafe_allow_html=True)

password_type = st.selectbox("Type de caractères :",
    [ "Tous les caractères", "Lettres et chiffres"])
length = st.slider("Taille du mot de passe :", min_value=8, max_value=32, value=12, step=1)

chars = string.ascii_letters + string.digits + string.punctuation



if password_type == "Tous les caractères":
    chars = string.ascii_letters + string.digits + string.punctuation+ string.punctuation
else:
    chars = string.ascii_letters + string.digits

def generate_password(length, chars):
    password = "".join(random.choice(chars) for i in range(length))
    return password

password = generate_password(length, chars)

st.write("Voici votre mot de passe fort :")
code = st.code(password, language="text")


def refresh():
    st.write("Page actualisée!")

st.button("Nouveau mot de passe", refresh)