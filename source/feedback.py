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
            <div class="container">
            <h1>Email Form</h1>
            <form>
                <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" placeholder="Enter your email" required>
                </div>
                <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" placeholder="Enter your message" rows="4" required></textarea>
                </div>
                <div class="form-group">
                <button type="submit">Submit</button>
                </div>
            </form>
            </div>
            """

            # Render the HTML form
            st.components.v1.html(html_form, width=500, height=300)