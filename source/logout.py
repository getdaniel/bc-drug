import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            
            # Add buttons in one row
            col1, col10, col11, col12, col2 = st.columns(5)
            
            # Cancel button in left corner
            if col1.button("No"):
                modal.close()
            
            if col2.button("OK", type="primary"):
                # Redirect to another link
                logout_url = "https://getdaniel.github.io/bc-drug/"  # Replace with the desired link
                
                # Generate the HTML for the redirect
                redirect_html = f'<meta http-equiv="refresh" content="0; URL={logout_url}">'
                
                # Use components.html to display the HTML
                components.html(redirect_html)