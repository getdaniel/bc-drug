import streamlit as st


def handle_user_feedback(modal):
    if modal.is_open():
        st.markdown(
            """
            <style>
            /* Adjust the color and background-color properties as needed */
            .modal-content .stTextInput, .modal-content .stTextArea {
                color: #ffffff !important;
                background-color: #000000 !important;
            }
            .modal-content .stButton button {
                color: #ffffff !important;
                background-color: #1e88e5 !important;
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