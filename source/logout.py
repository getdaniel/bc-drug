import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            
            # Add buttons in one row with CSS styling
            st.markdown("""
            <style>
            .button-row {
                display: flex;
                justify-content: space-between;
            }
            </style>
            """, unsafe_allow_html=True)
            
            # Button row
            col1, col2 = st.columns(2)
            with st.markdown('<div class="button-row">', unsafe_allow_html=True):
                if col1.button("No", type="secondary"):
                    modal.close()
                
                if col2.button("OK", type="primary"):
                    # Redirect to another link
                    logout_url = "https://getdaniel.github.io/bc-drug/"  # Replace with the desired link
                    redirect_js = f"window.location.href = '{logout_url}';"
                    st.write(f'<script>{redirect_js}</script>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)