import streamlit as st


def handle_settings(modal):
    if modal.is_open():
        st.info("Settings")