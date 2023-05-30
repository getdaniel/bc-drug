import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            
            # Add buttons in one row with HTML and CSS
            st.markdown("""
            <style>
            .button-container {
                display: flex;
                justify-content: space-between;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Button container
            st.markdown('<div class="button-container">', unsafe_allow_html=True)
            
            # Cancel button
            if st.button("No", key="cancel_button"):
                modal.close()
            
            # OK button
            if st.button("OK", key="ok_button"):
                # Redirect to another link
                logout_url = "https://getdaniel.github.io/bc-drug/"  # Replace with the desired link
                redirect_js = f"window.location.href = '{logout_url}';"
                st.write(f'<script>{redirect_js}</script>', unsafe_allow_html=True)
            
            # Close button container
            st.markdown('</div>', unsafe_allow_html=True)
