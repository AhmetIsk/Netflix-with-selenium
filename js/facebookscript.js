var facebook_users = [
  {
    firstName: 'Bob',
    lastName: 'Ross',
    email: 'bobross@outlook.com',
    password: 'test'
  },
  {
    firstName: 'Nina',
    lastName: 'Williams',
    email: 'ninawilliams@outlook.com',
    password: 'tekkenchamp'
  }
];

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

  let userpass = false;
  let passwordpass = false;

  facebook_users.some(user => {
    if (username === user.email && password === user.password) {
      // If the credentials are valid, show an alert box and reload the page
      userpass = true;
      passwordpass = true;
      return true;
    } else if (username === user.email && password !== user.password) {
      userpass = true;
      passwordpass = false;
      return true;
    } else if (username !== user.email) {
      userpass = false;
      return false;
    } else {
      // Otherwise, make the login error message show (change its oppacity)
      userpass = false;
      passwordpass = false;
      return false;
    }
  });

  if (userpass && passwordpass) {
    // If the credentials are valid, show an alert box and reload the page
    window.close();
    window.open("homepage.html", "_blank");
  } else if (userpass && !passwordpass) {
    wrongPassword.style.display = "block";
  } else if (!userpass) {
    wrongEmail.style.display = "block";
  } else {
    // Otherwise, make the login error message show (change its oppacity)
    document.location.reload();
  }
});
