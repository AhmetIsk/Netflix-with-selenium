let inputTouched = {
  email: false,
  password: false,
};

const inputEmail = document.getElementById("inputEmail");
const inputPassword = document.getElementById("inputPassword");
const inputWrapperEmail = document.getElementById("input-wrapper-email");
const inputWrapperPassword = document.getElementById("input-wrapper-password");
const warningEmail = document.getElementById("warningEmail");
const warningPassword = document.getElementById("warningPassword");
const loginButton = document.getElementById("sign-button");
const otherPage = document.getElementById("homepage");
const wrongEmail = document.getElementById("wrong-email");
const wrongPassword = document.getElementById("wrong-pass");
const loginWithFacebookButton = document.getElementById("login-facebook");
const facebookEmail = document.getElementById("email");
const facebookPassword = document.getElementById("pass");

loginButton.addEventListener("click", (e) => {
  // Prevent the default submission of the form
  e.preventDefault();
  // Get the values input by the user in the form fields
  const username = inputEmail.value;
  const password = inputPassword.value;

  if (username === "bobross@outlook.com" && password === "test") {
    // If the credentials are valid, show an alert box and reload the page
    document.location.href = "homepage.html";
  } else if (username === "bobross@outlook.com" && password !== "test") {
    wrongPassword.style.display = "block";
  } else if (username !== "bobross@outlook.com") {
    wrongEmail.style.display = "block";
  } else {
    // Otherwise, make the login error message show (change its oppacity)
    document.location.reload();
  }
});

const inputOnBlur = (ev) => {
  if (inputTouched.email) {
    if (!validateEmail(inputEmail.value) && !validatePhone(inputEmail.value)) {
      warningEmail.style.display = "block";
      inputEmail.style.borderBottom = "2px solid #e87c03";
      loginButton.disabled = true;
    } else {
      warningEmail.style.display = "none";
      inputEmail.style.borderBottom = "none";
      loginButton.disabled = false;
    }
  }
  if (inputTouched.password) {
    if (
      !(inputPassword.value.length >= 4 && inputPassword.value.length <= 60)
    ) {
      warningPassword.style.display = "block";
      inputPassword.style.borderBottom = "2px solid #e87c03";
      loginButton.disabled = true;
    } else {
      warningPassword.style.display = "none";
      inputPassword.style.borderBottom = "none";
      loginButton.disabled = false;
    }
  }
};

const inputOnFocus = (ev) => {
  inputTouched[ev.name] = true;
};

const validateEmail = (email) => {
  const re =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
};

const validatePhone = (email) => {
  const re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
  return re.test(String(email).toLowerCase());
};
