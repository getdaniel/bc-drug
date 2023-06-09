// Get a reference to the Firebase Realtime Database
const database = firebase.database();

// Get a reference to the Firebase Authentication service
const auth = firebase.auth();

// Get the form element and listen for the submit event
const registerForm = document.querySelector('.register-form');
const messageDiv = document.getElementById('message');

registerForm.addEventListener('submit', event => {
    event.preventDefault(); // Prevent the form from submitting

    // Get the form values
    const firstName = registerForm.firstname.value.trim();
    const lastName = registerForm.lastname.value.trim();
    const email = registerForm.email.value.trim();
    const password = registerForm.password.value.trim();
    const confirmPassword = registerForm.confirm_password.value.trim();

    // Check if the password and confirm password match
    if (password !== confirmPassword) {
        showMessage('Password and confirm password do not match', 'red');
        return; // Exit the function
    }

    // Create the user with email and password
    auth.createUserWithEmailAndPassword(email, password)
        .then(userCredential => {
            // Save the user to the database
            const { user } = userCredential;
            const userId = user.uid;
            database.ref(`users/${userId}`).set({
                firstName,
                lastName,
                email
            })
                .then(() => {
                    registerForm.reset(); // Clear the form
                    showMessage('User registered successfully', 'green');
                    window.location.href = 'https://getdaniel-bc-drug.streamlit.app/'; // Redirect to Streamlit app
                })
                .catch(error => {
                    showMessage('Error registering user: ' + error.message, 'red');
                });
        })
        .catch(error => {
            showMessage('Error creating user: ' + error.message, 'red');
        });
});

function showMessage(message, color) {
    messageDiv.textContent = message;
    messageDiv.style.color = color;
    messageDiv.style.fontWeight = 'bold';
    messageDiv.style.marginTop = '10px';
  }