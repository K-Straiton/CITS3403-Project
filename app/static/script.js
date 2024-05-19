function validateConfirmPassword()
{
    const form = document.getElementById
}

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
        let errormsg = document.createElement('p');
        errormsg.textContent = "aslkjdlkdsajd";
        let parentNode = confirmPassword.parentNode.parentNode;
        console.log(parentNode);
        console.log(errorField);
        console.log(confirmPassword.parentNode.nextSibling);
        console.log(confirmPassword.parentNode);
        parentNode.insertBefore(errorField, confirmPassword.parentNode.nextSibling);
        errorField.append(errormsg);
    }
})