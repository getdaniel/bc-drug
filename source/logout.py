import streamlit as st
import streamlit.components.v1 as components

logout_modal = components.declare_component("logout_modal")

# Confirmation modal for logging out
components.html(
    """
    <logout_modal
        open=props.open
        on_close=props.on_close
        submit_label="Log Out"
        close_label="Cancel"
    ></logout_modal>
    """
)

def handle_logout(modal):
    if modal["state"]["closed"]:
        st.info("Logged out")