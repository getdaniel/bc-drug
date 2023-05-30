import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            # Add buttons in one row
            col1, col20, col21, col22, col23, col24, col25, col26, col27, col28, col3 = st.columns(11)
            
            # Cancel button in left corner
            if col1.button("No"):
                modal.close()
            
            if col3.button("OK", key="logout_ok_button"):
                # Redirect to another link
                logout_url = "https://getdaniel.github.io/bc-drug/"  # Replace with the desired link
                redirect_html = f'<a href="{logout_url}""> </a>'
                st.markdown(redirect_html, unsafe_allow_html=True)
