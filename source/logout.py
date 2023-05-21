import streamlit as st


def handle_logout(modal):
    if modal.is_open():
        st.info("Logged out")