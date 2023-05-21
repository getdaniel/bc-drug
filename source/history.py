import streamlit as st


def handle_history(modal):
    if modal.is_open():
        st.info("Prediction History")