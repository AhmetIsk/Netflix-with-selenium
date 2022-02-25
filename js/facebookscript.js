import 'user-data-mock.js';

let inputTouched = {
  email: false,
  password: false,
};

const wrongEmail = document.getElementById("error-box");
const wrongPassword = document.getElementById("password-box");
const loginWithFacebookButton = document.getElementById("login-facebook");
const facebookEmail = document.getElementById("email");
const facebookPassword = document.getElementById("pass");

loginWithFacebookButton.addEventListener("click", (e) => {
  // Prevent the default submission of the form
  e.preventDefault();
  // Get the values input by the user in the form fields
  const username = facebookEmail.value;
  const password = facebookPassword.value;

  facebook_users.map(user => {
    if (username === user.email && password === user.password) {
      // If the credentials are valid, show an alert box and reload the page
      window.close();
      window.open("homepage.html", "_blank");
    } else if (username === user.email && password !== user.password) {
      wrongPassword.style.display = "block";
    } else if (username !== user.email) {
      wrongEmail.style.display = "block";
    } else {
      // Otherwise, make the login error message show (change its oppacity)
      document.location.reload();
    }
  });
});
