function togglePasswordVisibility(inputId) {
  const passwordInput = document.getElementById(inputId);
  const passwordToggle = passwordInput.nextElementSibling;

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    passwordToggle.innerHTML = '<i class="fa fa-eye-slash"></i>';
  } else {
    passwordInput.type = 'password';
    passwordToggle.innerHTML = '<i class="fa fa-eye"></i>';
  }
}