// Get references to the email and password input fields and the login form
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const loginForm = document.querySelector('.login-form');
const messageDiv = document.getElementById('message');

// Function to show the spinning/loading indicator
function showSpinner() {
  // Add a CSS class to display the spinning/loading effect
  messageDiv.classList.add('spinner');
}

// Function to hide the spinning/loading indicator
function hideSpinner() {
  // Remove the CSS class to hide the spinning/loading effect
  messageDiv.classList.remove('spinner');
}

// Add an event listener to the login form submit button
loginForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent the form from submitting

  const email = emailInput.value;
  const password = passwordInput.value;

  // Show the spinning/loading indicator
  showSpinner();

  // Sign in the user with email and password
  firebase.auth().signInWithEmailAndPassword(email, password)
    .then(() => {
      // Hide the spinning/loading indicator
      hideSpinner();

      loginForm.reset(); // Clear the form
      window.location.href = 'https://getdaniel-bc-drug.streamlit.app/'; // Redirect to Streamlit app
    })
    .catch((error) => {
      // Hide the spinning/loading indicator
      hideSpinner();

      if (error.code === 'auth/wrong-password') {
        messageDiv.textContent = 'Wrong password';
      } else if (error.code === 'auth/user-not-found') {
        messageDiv.textContent = 'Email not found';
      }
    });
});