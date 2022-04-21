const button = document.querySelector('.copy')

const input = document.querySelector('.copiar')

const message = document.querySelector("#message")

button.addEventListener('click', function(){
    input.focus();
    document.execCommand('selectAll');
    document.execCommand('copy');

    message.innerHTML = "COPIADO AL PORTAPAPELES"

    setTimeout(()=> message.innerHTML = "", 2000);
})