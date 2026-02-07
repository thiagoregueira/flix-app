import streamlit as st

from login.service import login


def show_login_page():
    st.title('Login')
    username = st.text_input(label='Usuário')
    password = st.text_input(label='Senha', type='password')
    if st.button('Login'):
        login(username=username, password=password)
