
  
    const versionInput = document.getElementById("version");
    const precioInput = document.getElementById("precio");
    const fechaInput = document.getElementById("fecha");
    const userIdInput = document.getElementById("userId");
    const sellIdInput = document.getElementById("sellId");
    const submitBtn = document.getElementById("submitBtn");
    const errorTxt = document.getElementById("errorTxt");
    const successTxt = document.getElementById("successTxt");
  
    const precioVersion = {
      "the forest": "15000",
      "son of the forest": "25000",
    };
  
    versionInput.addEventListener("change", function () {
        const versionSeleccionada = versionInput.value;
        const precio = parseInt(precioVersion[versionSeleccionada] )|| 0;
        precioInput.value = precio;
      });
    


    function validarFormulario() {
      errorTxt.textContent = "";
      successTxt.textContent = "";
  
      if (!versionInput.value || !precioInput.value || !fechaInput.value) {
        errorTxt.textContent = "Por favor, completa todos los campos.";
        return false;
      }
  
      if (isNaN(precioInput.value) || precioInput.value <= 0) {
        errorTxt.textContent = "Selecciona una versión válida.";
        return false;
      }
  
      return true;
    }
  
    submitBtn.addEventListener("click", function (e) {
      e.preventDefault();
  
      if (validarFormulario()) {
        fetch(`/sells/editar/${sellIdInput.value}/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
        
            version: versionInput.value,
            precio: precioInput.value,
            fecha: fechaInput.value,
            
          }),
        })
          .then((response) => {
            if (!response.ok) throw new Error("Error del servidor");
            return response.json();
          })
          .then((data) => {
            if (data.success) {
              successTxt.textContent = "Venta actualizada con éxito.";
              errorTxt.textContent = "";
              setTimeout(() => {
                window.location.href = "/dashboard";  
            }, 1500); 
            } else {
              errorTxt.textContent = data.error || "Error al actualizar la venta.";
              successTxt.textContent = "";
            }
          })
          .catch((error) => {
            console.error("Error:", error);
            errorTxt.textContent = "Hubo un problema con la solicitud.";
            successTxt.textContent = "";
          });
      }
    });
  