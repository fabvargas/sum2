// cambiar contraseña

const emailInput = document.getElementById("email");
const button = document.getElementById("submit");
const successTxt = document.getElementById("successTxt");
const errorTxt = document.getElementById("errorTxt");


function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}


function validarFormulario() {
    const email = emailInput.value;

    successTxt.textContent = "";

    if (!validarEmail(email)) {
        errorTxt.textContent = "El correo electrónico no es válido.";
        return false;
    }

   

    errorTxt.textContent = "";
    return true;
}

button.addEventListener("click", (event) => {
    event.preventDefault(); 
    if (validarFormulario()) {      
       fetch("/auth/pass_recovery/",{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: emailInput.value,
             
            }),
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                successTxt.textContent = "Registro exitoso.";
                errorTxt.textContent = "";
            } else {
                errorTxt.textContent = data.error;
                successTxt.textContent = "";
            }
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    }
});