from flask import flash,session
from models import consult_users
import hashlib
def estaIniciado():
    return True if 'usuario_id' in session else False
def login_controlador(user,contraseña):
    try:
        password = contraseña
    except:
        password = ""
        
    isValid = True

    if user == "":
        isValid = False
        flash("Ingrese un Email")
    else:
        usuario = consult_users.ObtenerUusarioUser(user=user)
        if not usuario:
            isValid = False
            flash("El email no se encuentra registrado")
        else:
            if password == "":
                isValid = False
                flash("Ingrese la contraseña")
            else:
                password_encrypt = hashlib.sha512(password.encode()).hexdigest()
                usuario = consult_users.ObtenerUusarioLogin(user=user, password=password_encrypt)
                if not usuario:
                    isValid = False
                    flash("Contraseña incorrecta")
                else:
                    for resivirToken in usuario:
                        if (resivirToken['validate'] != 'si'):
                            isValid = False
                            flash("ESTA CUENTA NO AH SIDO ACTIVADA")
    if isValid == False:
        return False
    return True
