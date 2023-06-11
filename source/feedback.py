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
                <style>
                    .login-form {
                        max-width: 750px;
                        margin: 0 auto;
                        width: 100%;
                        padding: 5px;
                        display: flex;
                        flex-direction: column;
                    }

                    .login-form label {
                        display: block;
                        margin-bottom: 5px;
                        font-weight: bold;
                    }

                    .login-form input[type="email"],
                    .login-form textarea {
                        width: 100%;
                        padding: 10px;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                        margin-bottom: 5px;
                    }

                    .login-form input[type="submit"] {
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 5px;
                        cursor: pointer;
                        width: 100%;
                    }

                    .login-form input[type="submit"]:hover {
                        background-color: #45a049;
                    }
                </style>

                <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
                    <form class="login-form" id="feedback-form">
                        <h3 style="text-align: center;">Send Us Feedback</h3>
                        <label for="email">
                            Email:
                            <input type="email" id="email" name="email" placeholder="Enter your email" required>
                        </label>
                        <label for="message">
                            Message:
                            <textarea id="message" placeholder="Enter your message" rows="4" required></textarea>
                        </label>
                        <input type="submit" value="Submit">
                    </form>
                </div>

                <script src="https://cdnjs.cloudflare.com/ajax/libs/firebase/7.14.1-0/firebase.js"></script>
                <script src="./js/firebase-config.js"></script>
                <script>
                    // Get a reference to the Firebase database
                    var database = firebase.database();
                    
                    document.addEventListener("DOMContentLoaded", function() {
                        var form = document.getElementById("feedback-form");
                        form.addEventListener("submit", function (e) {
                            e.preventDefault(); // Prevent form submission

                            // Get form values
                            var email = document.getElementById("email").value;
                            var message = document.getElementById("message").value;

                            // Save feedback to Firebase database
                            var feedbackRef = database.ref("feedbacks").push();
                            feedbackRef.set({
                                email: email,
                                message: message
                            });

                            // Reset form fields
                            form.reset();
                            alert("Feedback submitted successfully.");
                        });
                    });
                </script>
            """

            # Render the HTML form
            st.components.v1.html(html_form, width=500, height=300)