import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            button_col1, button_col2, button_col3 = st.columns([1, None, 1])
            if button_col1.button("Cancel"):
                # Handle cancel logic here
                pass
            if button_col2.button("OK"):
                # Handle OK logic here
                pass