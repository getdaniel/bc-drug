import streamlit as st


def handle_user_feedback(modal):
    if modal.is_open():
        st.markdown(
            """
            <style>
            /* Adjust the color and background-color properties as needed */
            .stTextInput, .stTextArea, .stButton {
                color: #ffffff !important;
                background-color: #000000 !important;
            }
            </style>
            """
        )
        with modal.container():
            email = st.text_input("Email")
            message = st.text_area("Message")
            if st.button("Submit", use_container_width=True):
                # Handle the feedback submission
                st.success("Feedback submitted successfully.")