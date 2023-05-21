import streamlit as st


def handle_history(modal):
    if modal.is_open():
        with modal.container():
            st.info("Prediction History")