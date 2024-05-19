
const form = document.getElementById('signUpForm');


form.addEventListener("submit", function (event) {
    event.preventDefault();

    const password = form.elements["signUpPassword"];
    const confirmPassword = form.elements["signUpConfirmPassword"];

    const passwordValue = password.value;
    const confirmPasswordValue = confirmPassword.value;

    if(passwordValue == confirmPasswordValue) {
        form.submit();
    }
    else {

        password.classList.add('is-invalid');
        confirmPassword.classList.add('is-invalid');
        let errorField = document.createElement('div');
        errorField.classList.add('invalid-feedback');
        errorField.classList.add('mb-1');
        errorField.textContent = "Passwords do not match.";
        let parentNode = confirmPassword.parentNode.parentNode;
        parentNode.insertBefore(errorField, confirmPassword.parentNode.nextSibling);
        errorField.style.display="block";
    }
})