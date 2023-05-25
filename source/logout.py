import streamlit as st


def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            st.button("Cancel")
            st.button("OK")