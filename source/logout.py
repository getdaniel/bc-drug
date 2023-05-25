import streamlit as st

def handle_logout(modal):
    if modal.is_open():
        with modal.container():
            st.warning("Are you sure you want to log out?")
            button_container = st.container()
            
            with button_container:
                st.write('<style>div.stButton > button:first-child { margin-right: 10px; }</style>', unsafe_allow_html=True)
                st.button("Cancel")
                st.button("OK")