import random
import string
import streamlit as st

st.set_page_config(layout="wide", page_title="Mots de passe forts")

length = st.slider("Taille du mot de passe :", min_value=8, max_value=32, value=12, step=1)

chars = string.ascii_letters + string.digits + string.punctuation

password_type = st.selectbox("Type de caractères :",
    ["Lettres et chiffres", "Tous les caractères"])

if password_type == "Tous les caractères":
    chars = string.ascii_letters + string.digits + string.punctuation
else:
    chars = string.ascii_letters + string.digits

@st.cache
def generate_password(length, chars):
    password = "".join(random.choice(chars) for i in range(length))
    return password

password = generate_password(length, chars)

st.write("Voici votre mot de passe fort :")
st.write(password)
