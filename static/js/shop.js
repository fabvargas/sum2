   const userIdInput = document.getElementById("userId");
  const versionInput = document.getElementById("version");
  const precioInput = document.getElementById("precio");
  const submitBtn = document.getElementById("submit");
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

    if ( !version || !precio) {
      errorTxt.textContent = "Por favor, completa todos los campos.";
      return false;
    }

    

  if (isNaN(precioInput.value) || precioInput.value <= 0) {
    errorTxt.textContent = "Selecciona una versión válida.";
    return false;
  }

    return true;
  }

  console.log(userIdInput.value);
  console.log(versionInput.value);
  console.log(precioInput.value);


  submitBtn.addEventListener("click", function (e) {
    e.preventDefault();

    if (validarFormulario()) {
      fetch("/comprar/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
         
        },
        body: JSON.stringify({
            userId: userIdInput.value,
          version: versionInput.value,
          precio: precioInput.value,
        })
      })
      .then(response => {
        if (!response.ok) throw new Error("Error del servidor");
        return response.json();
      })
      .then(data => {
        if (data.success) {
          successTxt.textContent = "Compra realizada con éxito.";
          errorTxt.textContent = "";
        } else {
          successTxt.textContent = "";
          errorTxt.textContent = data.error || "Error al procesar la compra.";
        }
      })
      .catch(error => {
        console.error("Error:", error);
        errorTxt.textContent = "Hubo un problema con la solicitud.";
        successTxt.textContent = "";
      });
    }
  });



