import streamlit as st


def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.info("Logged out")