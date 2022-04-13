from telnetlib import ENCRYPT
from flask import flash
import hashlib
from models import register_user
def validacionPassControlador(password):
    try:
        password = password
    except:
        password = ""
    isValid = True
    if password == "":
        isValid = False
        flash ("Debe ingresar una contrseña obligatoriamente :v")
    else:
        if len(password) < 8:
            isValid = False
            flash("La contraseña debe contener minimo 8 caracteres")
        else:
            SpecialSym =['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','=','?','@','[',']','^','_','`','{','|','}','~']
            if not any(char.isdigit() for char in password):
                isValid = False
                flash("La contraseña debe contener almenos un numero")
            if not any(char.isupper() for char in password):
                isValid = False
                flash("La contraseña debe contener almenos una mayuscula")
            if not any(char in SpecialSym for char in password):
                isValid = False
                flash("La contraseña debe contener almenos un caracter especial")
    if isValid == False:
        return False
    return True
def enviarBDNewPassword(url,password):
    encrypt = hashlib.sha512(password.encode()).hexdigest()
    register_user.Cambiodecontraseña(url=url,password=encrypt)