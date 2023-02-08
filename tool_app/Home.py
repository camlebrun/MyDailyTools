import streamlit as st

st.set_page_config(layout = "wide", page_title = "Home")
st.markdown("<h1 style='text-align: center'>Outils pratique </h1>", unsafe_allow_html=True)
st.error('This is an error', icon="🚨")
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