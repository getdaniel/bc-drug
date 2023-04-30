// Get a reference to the Firebase Realtime Database
const database = firebase.database();

// Get a reference to the Firebase Authentication service
const auth = firebase.auth();

// Get the form element and listen for the submit event
const registerForm = document.querySelector('.register-form');
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
        alert('Password and confirm password do not match');
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
                    alert('User registered successfully');
                    registerForm.reset(); // Clear the form
                    window.location.href = 'http://localhost:8501'; // Redirect to Streamlit app
                })
                .catch(error => {
                    alert('Error registering user: ' + error.message);
                });
        })
        .catch(error => {
            alert('Error creating user: ' + error.message);
        });
});