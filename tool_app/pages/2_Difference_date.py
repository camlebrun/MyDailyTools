import streamlit as st
from datetime import datetime, timedelta

st.markdown("<h1 style='text-align: center'>Calcul de différence de dates</h1>", unsafe_allow_html=True)

def format_timedelta(delta):
    if delta.days < 0:
        return "La date de départ doit être antérieure à la date de fin."
    else:
        days = delta.days
        months = days // 30
        years = months // 12
        months = months % 12
        days = days % 30
        if years == 0:
            if months == 0:
                return f"{days} jour(s)"
            else:
                return f"{months} mois et {days} jour(s)"
        else:
            return f"{years} an(s),  {months} mois, et {days} jour(s)"


def date_difference():
    start_date = st.date_input("Entrez la date de départ :")
    end_date = st.date_input("Entrez la date de fin :")
    delta = end_date - start_date
    st.markdown("### Différence : %s" % format_timedelta(delta))

if __name__ == '__main__':
    date_difference()