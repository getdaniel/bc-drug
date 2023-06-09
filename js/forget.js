// Get a reference to the Firebase Authentication service
var auth = firebase.auth();

// Get the form element and listen for the submit event
var forgotPasswordForm = document.querySelector('.forgotPasswordForm');
var emailInput = document.getElementById('email');
var messageDiv = document.getElementById('message');

forgotPasswordForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting

    var email = emailInput.value;

    // Validate the email format
    var emailRegex = /^\S+@\S+\.\S+$/;
    if (!emailRegex.test(email)) {
        messageDiv.textContent = 'Invalid email format. Please enter a valid email.';
        return; // Exit the function
    }

    // Check if the email exists in the Firebase Authentication system
    auth.fetchSignInMethodsForEmail(email)
        .then(function (signInMethods) {
            if (signInMethods.length === 0) {
                messageDiv.textContent = 'Email not found. Please enter a registered email.';
                return; // Exit the function
            }

            // Send password reset email
            auth.sendPasswordResetEmail(email)
                .then(function () {
                    messageDiv.textContent = 'Password reset email sent. Check your inbox.';
                    forgotPasswordForm.reset(); // Clear the form
                })
                .catch(function (error) {
                    messageDiv.textContent = 'Error sending password reset email: ' + error.message;
                });
        })
        .catch(function (error) {
            messageDiv.textContent = 'Error checking email: ' + error.message;
        });
});