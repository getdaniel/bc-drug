import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components

modal = Modal("Feedback", key="feedback_button")


def user_feedback():
    modal.open()

    if modal.is_open():
        with modal.container():
            email = st.text_input("Email")
            message = st.text_area("Message")
            if st.button("Submit", use_container_width=True):
                # Handle the feedback submission
                st.success("Feedback submitted successfully.")