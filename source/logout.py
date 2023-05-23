import streamlit as st


def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.confirm("Are you sure you want to log out?")