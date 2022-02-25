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

  if (username === "bobross@outlook.com" && password === "test") {
    // If the credentials are valid, show an alert box and reload the page
    window.open("homepage.html", "_blank");
    window.close();
  } else if (username === "bobross@outlook.com" && password !== "test") {
    wrongPassword.style.display = "block";
  } else if (username !== "bobross@outlook.com") {
    wrongEmail.style.display = "block";
  } else {
    // Otherwise, make the login error message show (change its oppacity)
    document.location.reload();
  }
});
