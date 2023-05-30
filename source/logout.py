import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            # Add buttons in one row
            col1, col2 = st.columns(2)
            
            # Cancel button in left corner
            if col1.button("No"):
                modal.close()
            
            if col2.button("OK"):
                # Redirect to another link
                logout_url = "https://getdaniel.github.io/bc-drug/"  # Replace with the desired link
                redirect_js = f"window.location.href = '{logout_url}';"
                st.write(f'<script>{redirect_js}</script>', unsafe_allow_html=True)
