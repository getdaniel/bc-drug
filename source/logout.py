import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            
            # Add buttons in one row
            col1 = st.columns(1)
            
            # OK button in right corner
            if col1:
                # Redirect to another link
                logout_url = "https://getdaniel.github.io/bc-drug/"  # Replace with the desired link
                
                # Generate HTML for opening link in new tab
                new_tab_html = f'<a href="{logout_url}" target="_self" rel="noopener noreferrer"><button style="background-color: red; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer;">OK</button></a>'

                # Display the HTML
                st.write(new_tab_html, unsafe_allow_html=True)