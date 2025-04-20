const emailInput = document.getElementById("email");
const contrasenaInput = document.getElementById("pass");
const confirmarInput = document.getElementById("pass-con");
const nombreInput = document.getElementById("nombre");
const telefonoInput = document.getElementById("telefono");

const paisInput = document.getElementById("pais");
const permisosInput = document.getElementById("permisos");

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
    const email = emailInput.value.trim();
    const contrasena = contrasenaInput.value.trim();
    const confirmar = confirmarInput.value.trim();
    const nombre = nombreInput.value.trim();
    const telefono = telefonoInput.value.trim();
    const pais = paisInput.value;

    console.log(email, contrasena, nombre, telefono, pais);

    errorTxt.textContent = "";
    successTxt.textContent = "";

    if (!email || !contrasena || !confirmar || !nombre || !telefono  || !pais) {
        errorTxt.textContent = "Por favor, completa todos los campos.";
        return false;
    }

    if (!validarEmail(email)) {
        errorTxt.textContent = "El correo electrónico no es válido.";
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

    if (!validarNombre(nombre)) {
        errorTxt.textContent = "El nombre no puede estar vacío.";
        return false;
    }

    if (!validarTelefono(telefono)) {
        errorTxt.textContent = "El teléfono debe contener solo números y al menos 7 dígitos.";
        return false;
    }

    const permisos = permisosInput.value;

if (!permisos) {
    errorTxt.textContent = "Selecciona un permiso válido.";
    return false;
}

    return true;
}


button.addEventListener("click", (event) => {
    event.preventDefault();

    if (validarFormulario()) {
        fetch("/auth/registrar_usuario/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: emailInput.value.trim(),
                contrasena: contrasenaInput.value.trim(),
                nombre: nombreInput.value.trim(),
                telefono: telefonoInput.value.trim(),
                pais: paisInput.value,
                permisos: permisosInput.value
            }),
        })
        .then(response => {
          
            return response.json();
        })
        .then(data => {
            console.log(data, "data")
            if (data.status === "success") {
                successTxt.textContent = "Cuenta creada exitosamente.";
                errorTxt.textContent = "";
            } else {
                successTxt.textContent = "";
                errorTxt.textContent = data.message ;
            }
        })
        .catch(error => {
            console.error("Error:", error);
            successTxt.textContent = "";
            errorTxt.textContent = `${error}`;
        });
    }
});