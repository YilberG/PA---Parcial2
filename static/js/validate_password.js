document.getElementById('password').addEventListener('input', function(evt) {
    const campo = evt.target,
          cantidad = document.getElementById('cantidad'),
          caracteres = document.getElementById("caracteres"),
          regex = /^(?=.*\d)(?=.*[a-záéíóúüñ]).*[A-ZÁÉÍÓÚÜÑ]/;
    let cant = campo.value
    if(cant.length < 8){
        cantidad.innerText = "Su debe contener minimo 8 digitos";
    }else{
        cantidad.innerText = "";
    }
    
    if (regex.test(campo.value)) {
      caracteres.innerText = "";
    } else {
      caracteres.innerText = "Almenos una mayuscula, un numero y un caracter especial";
    }
});