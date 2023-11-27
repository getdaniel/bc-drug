// Get references to the email and password input fields and the login form
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const loginForm = document.querySelector('.login-form');
const messageDiv = document.getElementById('message');

// Add an event listener to the login form submit button
loginForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent the form from submitting

  const email = emailInput.value;
  const password = passwordInput.value;

  // Sign in the user with email and password
  firebase.auth().signInWithEmailAndPassword(email, password)
    .then(() => {
      loginForm.reset(); // Clear the form
      showMessage('Please Wait a moment...', 'green');
      window.location.href = 'https://bc-drug.streamlit.app/'; // Redirect to Streamlit app
    })
    .catch((error) => {
      if (error.code === 'auth/wrong-password') {
        showMessage('Wrong password', 'red');
      } else if (error.code === 'auth/user-not-found') {
        showMessage('Email not found', 'red');
      } else {
        showMessage('An error occurred. Please try again later.', 'red');
      }
    });
});

function showMessage(message, color) {
  messageDiv.textContent = message;
  messageDiv.style.color = color;
  messageDiv.style.fontWeight = 'bold';
  messageDiv.style.marginTop = '10px';
}
