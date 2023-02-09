import streamlit as st
from datetime import datetime, timedelta

st.markdown("<h1 style='text-align: center'>Calcul de différence de dates</h1>", unsafe_allow_html=True)

def format_timedelta(delta):
    if delta.days < 0:
        return 
    if delta.days == 0:
        return 
    if delta.days == 1:
        return "1 jour"
    else:
        days = delta.days
        months = days // 30
        years = months // 12
        months = months % 12
        days = days % 30
        if years == 0:
            if months == 0:
                return f"{days} jours"
            else:
                return f"{months} mois et {days} jours"
        else:
            return f"{years} an(s),  {months} mois, et {days} jours"


def date_difference():
    start_date = st.date_input("Entrez la date de départ :")
    end_date = st.date_input("Entrez la date de fin :")
    delta = end_date - start_date
    if delta.days < 0:
        st.warning("La date de départ doit être antérieure à la date de fin.")
    elif delta.days == 0:
        st.warning("Les deux dates sont identiques.")
    else:
        delta_str = format_timedelta(delta)
        st.metric("Différence :", delta_str)


if __name__ == '__main__':
    date_difference()