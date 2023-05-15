// Get references to the email and password input fields and the login form
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const loginForm = document.querySelector('.login-form');

// Add an event listener to the login form submit button
loginForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Prevent the form from submitting

  const email = emailInput.value;
  const password = passwordInput.value;

  // Sign in the user with email and password
  firebase.auth().signInWithEmailAndPassword(email, password)
    .then(() => {
      alert('Login successful!');
      loginForm.reset(); // Clear the form
      window.location.href = 'https://getdaniel-bc-drug.streamlit.app/'; // Redirect to Streamlit app
    })
    .catch((error) => {
      alert('Error signing in: ' + error.message);
    });
});
