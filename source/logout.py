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
            
            # OK button in right corner
            if col2:
                # Redirect to another link
                logout_url = "https://getdaniel.github.io/bc-drug/"  # Replace with the desired link
                
                # Generate HTML for opening link in new tab
                new_tab_html = f'<a href="{logout_url}" target="_self" rel="noopener noreferrer">OK</a>'
                
                # Display the HTML
                st.write(new_tab_html, unsafe_allow_html=True)