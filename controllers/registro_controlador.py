from flask import flash
from models import consult_users
from models import register_user
import send_mail
import hashlib
import string
import random
def registro_controlador(nombre,user,contraseña):
    try:
        password = contraseña
    except:
        password = ""
    print (password)

    isValid = True

    if nombre == "":
        isValid = False
        flash("debe ingresar un nombre")
    else:
        if user == "":
            isValid = False
            flash("debe ingresar un Email")
        else:
            usuario = consult_users.ObtenerUusarioUser(user=user)
            if not usuario:
                if password == "":
                    isValid = False
                    flash("Ingrese una contraseña")
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
            else:
                isValid = False
                flash("El Email ya se encuentra registrado")
    if isValid == False:
        return False
    return True
    
def DBregistro_controlador(nombre,apellido,usuario,contraseña):
    validate = (''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))) #token de la validacion de 5 caracteres
    encrypt = hashlib.sha512(contraseña.encode()).hexdigest() #encriptacion

    register_user.CrearUsuario(nombre=nombre, apellido=apellido, user=usuario, password=encrypt, validate = validate)
    title = 'VALIDACION DE USAURIO DESDE REGISTRO'
    body = '<h1>Para validar su cuentra ingrese <a style="color: blue;" href="http://127.0.0.1:5000/validar-cuenta/'+validate+'">aqui</a></h1>'

    send_mail.send_validate_email(user = usuario, title = title, body = body)
