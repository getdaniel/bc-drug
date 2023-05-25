import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            st.write(
                '<div style="display: flex; justify-content: space-between;">'
                '<button style="margin-right: 10px;">Cancel</button>'
                '<button>OK</button>'
                '</div>',
                unsafe_allow_html=True
            )