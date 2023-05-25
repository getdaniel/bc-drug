import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            
            st.write(
                '<style>.streamlit-modal-content { max-width: 600px !important; width: 80% !important; }</style>',
                unsafe_allow_html=True
            )
            
            button_container = st.beta_container()
            
            with button_container:
                st.write(
                    '<style>div.stButton > button:first-child { margin-right: 10px; }</style>',
                    unsafe_allow_html=True
                )
                
                cancel_clicked = st.button("Cancel")
                ok_clicked = st.button("OK")

                if cancel_clicked:
                    # Handle cancel logic here
                    modal.close()

                if ok_clicked:
                    # Handle OK logic here
                    modal.close()