
const contrasenaInput = document.getElementById("pass");
const confirmarInput = document.getElementById("pass-con");


const button = document.getElementById("submit");
const errorTxt = document.getElementById("errorTxt");
const successTxt = document.getElementById("successTxt");


function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}


function validarContrasena(contrasena) {
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$/;
    return regex.test(contrasena);
}


function validarNombre(nombre) {
    return nombre.trim().length > 0;
}

function validarTelefono(telefono) {
    const regex = /^[0-9]{7,15}$/; 
    return regex.test(telefono);
}

function validarFormulario() {

    const contrasena = contrasenaInput.value.trim();
    const confirmar = confirmarInput.value.trim();
  


    errorTxt.textContent = "";
    successTxt.textContent = "";

    if (!contrasena || !confirmar ) {
        errorTxt.textContent = "Por favor, completa todos los campos.";
        return false;
    }



    if (!validarContrasena(contrasena)) {
        errorTxt.textContent = "La contraseña debe tener al menos 6 caracteres, una letra mayúscula y un número.";
        return false;
    }

    if (contrasena !== confirmar) {
        errorTxt.textContent = "Las contraseñas no coinciden.";
        return false;
    }


    return true;
}

const pathParts = window.location.pathname.split("/");


const uidb64 = pathParts[pathParts.length - 2]; 



button.addEventListener("click", (event) => {
    event.preventDefault();

    if (validarFormulario()) {
        fetch(`/auth/changepass/${uidb64}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
           
                contrasena: contrasenaInput.value.trim(),
          
            }),
        })
        .then(response => {
          
            return response.json();
        })
        .then(data => {
            console.log(data, "data")
            if (data.success) {
                successTxt.textContent = "Clave cambiada exitosamente.";
                errorTxt.textContent = "";
            } else {
                successTxt.textContent = "";
                errorTxt.textContent = data.error ;
            }
        })
        .catch(error => {
            console.error("Error:", error);
            successTxt.textContent = "";
            errorTxt.textContent = `${error}`;
        });
    }
});