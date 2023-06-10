import streamlit as st


def handle_user_feedback(modal):
    if modal.is_open():
        with modal.container():
            # email = st.text_input("Email")
            # message = st.text_area("Message")
            # if st.button("Submit", use_container_width=True):
            #     # Handle the feedback submission
            #     st.success("Feedback submitted successfully.")
            st.markdown(
                """
                    <h1>Feedback Form</h1>
                    <input type="text" id="email" placeholder="Email">
                    <textarea id="message" placeholder="Message"></textarea>
                    <button onclick="saveFeedback()">Submit</button>

                """)