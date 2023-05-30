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
            
            # OK button in right corner
            if col3.button("OK"):
                # Redirect to another link
                # Replace 'https://example.com' with the desired link
                st.experimental_set_query_params(logout=True)  # Set a query parameter to indicate logout
                # Replace 'https://example.com/logout' with the logout link
                st.experimental_rerun()  # Rerun the app to trigger the redirect
