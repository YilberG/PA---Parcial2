from flask import flash 
from models import consult_users
from models import register_user
import send_mail
import string
import random
def recuperarPassControlador(user):
    isValid = True

    if user == "":
        isValid = False
        flash("Ingrese su email")
    else:
        usuario = consult_users.ObtenerUusarioUser(user=user)
        if not usuario:
            isValid("este email NO esta registrado")
    if isValid == False:
        return False
    return True

def DBrecuperarPassControlador(user):
    url = (''.join(random.choice(string.ascii_letters + string.digits)for _ in range(10)))

    register_user.urlcontraseña( user=user, url=url )

    title = 'RECUPERACION DE LA CUENTA'
    body = '<h3> para recuperar la cuenta ingresar a <a style="color: blue;" href="http://127.0.0.1:5000/recuperarPass/'+url+'">aqui</a> '
    send_mail.send_validate_email(user = user, title = title, body = body)