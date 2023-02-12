import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

st.markdown("<h1 style='text-align: center'>Calcul de différence de dates</h1>", unsafe_allow_html=True)

def date_difference():
    start_date = st.date_input("Entrez la date de départ :")
    end_date = st.date_input("Entrez la date de fin :", datetime.datetime.now() + datetime.timedelta(days=7))    
    delta = relativedelta(end_date, start_date)
    years = delta.years
    months = delta.months
    days = delta.days

    result = ""

    if years == 0 and months == 0 and days == 0:
        result = "Les deux dates sont identiques."
    elif years < 1 and months < 1 and days <1:
        result = "La date de fin est antérieure à la date de départ."
    if years == 1:
        result += "1 an "
    elif years > 1:
        result += f"{years} ans "
    if months == 1:
        result += "1 mois "
    elif months > 1:
        result += f"{months} mois "
    if days == 1:
        result += "1 jour"
    elif days > 1:
        result += f"{days} jours"

    st.metric("Résultat :", result)


if __name__ == '__main__':
    date_difference()
