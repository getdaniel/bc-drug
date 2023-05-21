import streamlit as st


def handle_settings(modal):
    if modal.is_open():
        with modal.container():
            st.info("Settings")