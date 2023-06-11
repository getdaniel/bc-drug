import streamlit as st

def handle_user_feedback(modal):
    if modal.is_open():
        with modal.container():
            html_form = """
                <!-- HTML code for the form -->
                <div id="feedback-container">
                    <style>
                        .login-form {
                            max-width: 350px;
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

                        .success-message {
                            color: green;
                            margin-top: 10px;
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

                            <!-- Success message container -->
                            <div id="message-container"></div>
                        </form>
                    </div>

                    
                </div>

                <!-- Firebase SDK and JavaScript code -->
                <script src="https://www.gstatic.com/firebasejs/9.1.3/firebase-app.js"></script>
                <script src="https://www.gstatic.com/firebasejs/9.1.3/firebase-database.js"></script>
                <script>
                    const firebaseConfig = {
                        apiKey: "AIzaSyDWlsnIKRS93tzZkb58NjvW0c7BIkUMwvA",
                        authDomain: "drug-discovery-cbde6.firebaseapp.com",
                        databaseURL: "https://drug-discovery-cbde6-default-rtdb.firebaseio.com",
                        projectId: "drug-discovery-cbde6",
                        storageBucket: "drug-discovery-cbde6.appspot.com",
                        messagingSenderId: "504463909250",
                        appId: "1:504463909250:web:d1fb6476bb4a59ca8d6f9b",
                        measurementId: "G-0GMN586SER"
                    };

                    firebase.initializeApp(firebaseConfig);

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
                            
                            // Display success message
                            var messageContainer = document.getElementById("message-container");
                            var successMessage = document.createElement("div");
                            successMessage.className = "success-message";
                            successMessage.textContent = "Feedback submitted successfully.";
                            messageContainer.appendChild(successMessage);
                        });
                    });
                </script>
            """

            # Render the HTML form
            st.components.v1.html(html_form, height=300)