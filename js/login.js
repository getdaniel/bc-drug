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
      messageDiv.textContent = 'Login successful!';
      loginForm.reset(); // Clear the form
      window.location.href = 'https://getdaniel-bc-drug.streamlit.app/'; // Redirect to Streamlit app
    })
    .catch((error) => {
      if (error.code === 'auth/wrong-password') {
        messageDiv.textContent = 'Wrong password';
      } else if (error.code === 'auth/user-not-found') {
        messageDiv.textContent = 'Email not found';
      } else if (error.code === 'auth/invalid-email') {
        throw new Error('Invalid email');
      }
    });
});