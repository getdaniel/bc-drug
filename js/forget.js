// Get a reference to the Firebase Authentication service
var auth = firebase.auth();

// Get the form element and listen for the submit event
var forgotPasswordForm = document.querySelector('.forgotPasswordForm');
var emailInput = document.getElementById('email');
var messageDiv = document.getElementById('message');

forgotPasswordForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting

    var email = emailInput.value;

    // Check if the email exists in the Firebase Authentication system
    auth.fetchSignInMethodsForEmail(email)
        .then(function (signInMethods) {
            if (signInMethods.length === 0) {
                showMessage('Email not found. Please enter a registered email.', 'red');
                return; // Exit the function
            }

            // Send password reset email
            auth.sendPasswordResetEmail(email)
                .then(function () {
                    showMessage('Password reset email sent. Check your inbox.', 'green');
                    forgotPasswordForm.reset(); // Clear the form
                })
                .catch(function (error) {
                    showMessage('Error sending password reset email: ' + error.message, 'red');
                });
        })
        .catch(function (error) {
            showMessage('Error checking email: ' + error.message, 'red');
        });
});

function showMessage(message, color) {
    messageDiv.textContent = message;
    messageDiv.style.color = color;
    messageDiv.style.fontWeight = 'bold';
    messageDiv.style.marginTop = '10px';
  }