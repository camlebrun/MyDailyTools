import datetime
import streamlit as st

st.set_page_config(layout="wide", page_title="Calculatrice de jours")

st.markdown(
    "<h1 style='text-align: center'>Calculatrice de jours</h1>",
    unsafe_allow_html=True)


def calculate_date(operation, days_to_add, d_0):
    if operation == "Ajouter":
        d_2 = d_0 + datetime.timedelta(days=days_to_add)

    elif operation == "Soustraire":
        d_2 = d_0 - datetime.timedelta(days=days_to_add)

    return d_2


col1, col2 = st.columns(2)

with col1:
    d_0 = st.date_input("Choisir votre date", datetime.datetime.now())
    D1 = str(d_0)
    st.empty()
with col2:
    operation = st.selectbox(
        "Sélectionnez l'opération", [
            "Ajouter", "Soustraire"])
days_to_add = st.number_input(
    "Choisir le nombre de jour à ajouter/soustraire",
    min_value=0,
    step=1,
    value=7)

d_2 = calculate_date(operation, days_to_add, d_0)
D3 = str(d_2)
result = st.metric("Le résultat est : ", D3)
