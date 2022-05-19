const cheken = document.getElementsByName("letra")
function pacman(){
    for(var y = 0; y < cheken.length; y++){
        console.log(cheken[y].checked)
        if(cheken[y].checked){
            if (cheken[y].value == '1'){
                document.getElementById("mayusculas").checked = true
                document.getElementById("minusculas").checked = true
                document.getElementById("numeros").checked = false
                document.getElementById("simbolos").checked = false
            }
            else{
                document.getElementById("mayusculas").checked = true
                document.getElementById("minusculas").checked = true
                document.getElementById("numeros").checked = true
                document.getElementById("simbolos").checked = true
            }
            break;
        }
    }
}