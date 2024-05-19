
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

        let errorField = document.getElementById("confirmPasswordError");

        if(errorField == null) {
            password.classList.add('is-invalid');
            confirmPassword.classList.add('is-invalid');
            errorField = document.createElement('div');
            errorField.classList.add('invalid-feedback');
            errorField.classList.add('mb-1');
            errorField.id = "confirmPasswordError";
            errorField.textContent = "Passwords must match.";
            let parentNode = confirmPassword.parentNode.parentNode;
            parentNode.insertBefore(errorField, confirmPassword.parentNode.nextSibling);
            errorField.style.display="block";

        }

        password.value = '';
        confirmPassword.value = '';

    }
})