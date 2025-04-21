const nameInput = document.getElementById("name");
const phoneInput = document.getElementById("phone");
const countryInput = document.getElementById("country");
const submitBtn = document.getElementById("submitBtn");

const errorTxt = document.getElementById("errorTxt");
const successTxt = document.getElementById("successTxt");

function validarNombre(nombre) {
    return nombre.trim().length > 0;
}

function validarTelefono(telefono) {
    const regex = /^[0-9]{7,15}$/; 
    return regex.test(telefono);
}

function validarFormulario() {
    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();
    const country = countryInput.value;

    errorTxt.textContent = "";  // Limpiar mensaje de error
    successTxt.textContent = "";  // Limpiar mensaje de éxito

    if (!name || !phone || !country) {
        errorTxt.textContent = "Todos los campos son obligatorios.";
        return false;
    }

    if (!validarNombre(name)) {
        errorTxt.textContent = "El nombre no puede estar vacío.";
        return false;
    }

    if (!validarTelefono(phone)) {
        errorTxt.textContent = "El teléfono debe contener solo números y al menos 7 dígitos.";
        return false;
    }

    console.log(name, phone, country);

    return true;
}

const userId = window.location.pathname.split('/')[3];

// Enviar el formulario al servidor
submitBtn.addEventListener("click", (event) => {
    event.preventDefault();
    

    if (validarFormulario()) {

        fetch(`/perfil/editar/${userId}/`, {
            method: "POST",  // Si estás actualizando datos, también podrías usar PUT, pero POST es más común para este caso
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: nameInput.value,
                phone: phoneInput.value,
                country: countryInput.value
            }),
        })
        .then(response => 
            
            response.json()

        )
        .then(data => {
            if (!data.success) {
                errorTxt.textContent = data.error;  // Mostrar error si hay uno
            } else {
                successTxt.textContent = "Perfil actualizado exitosamente.";  // Mensaje de éxito
                errorTxt.textContent = "";  // Limpiar mensaje de error
                setTimeout(() => {
                    window.location.href = "/dashboard";  // Redirigir si el perfil se guarda exitosamente
                }, 1500); // Redirigir después de un breve mensaje de éxito
            }
        })
        .catch(error => {
            console.error("Error:", error);
            errorTxt.textContent = "Hubo un error al guardar el perfil.";
            successTxt.textContent = "";  // Limpiar mensaje de éxito en caso de error
        });
    }
});
