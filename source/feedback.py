import streamlit as st


def handle_user_feedback(modal):
    if modal.is_open():
        with modal.container():
            # email = st.text_input("Email")
            # message = st.text_area("Message")
            # if st.button("Submit", use_container_width=True):
            #     # Handle the feedback submission
            #     st.success("Feedback submitted successfully.")
            # HTML code for the form
            html_form = """
                <form>
                    <label> Email: </label>
                    <input type="email">
                    <label> Message: </label>
                    <textarea></textarea>
                    <input type="submit">
                </form>
            """

            # Render the HTML form
            st.components.v1.html(html_form, width=500, height=300)