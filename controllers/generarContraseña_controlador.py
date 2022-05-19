import re
import string
import random

from flask import flash
def generar(longitud, mayusculas, minusculas, numeros, simbolos):
    try:
        longitud = int(longitud)
    except:
        longitud = 0
    if longitud is 0:
        flash("DEBE DAR UNA LONGITUD")
        return False
    if mayusculas == "no" and minusculas == "no" and numeros == "no" and simbolos == "no":
        flash("Debe seleccionar almenos una opcion de caracteres")
        return False

    else:
        caracteresEspeciales = "!@#$%^&*()"
        if mayusculas == "si" and minusculas == "no" and numeros == "no" and simbolos == "no":
            generar = (''.join(random.choice(string.ascii_uppercase) for _ in range (longitud)))
        elif mayusculas == "no" and minusculas == "si" and numeros == "no" and simbolos == "no":
            generar = (''.join(random.choice(string.ascii_lowercase) for _ in range (longitud)))
        elif mayusculas == "no" and minusculas == "no" and numeros == "si" and simbolos == "no":
            generar = (''.join(random.choice(string.digits) for _ in range (longitud)))
        elif mayusculas == "no" and minusculas == "no" and numeros == "no" and simbolos == "si":
            generar = (''.join(random.choice(caracteresEspeciales) for _ in range (longitud)))
        #Mayusculas - Minusculas
        elif mayusculas == "si" and minusculas == "si" and numeros == "no" and simbolos == "no":
            generar = (''.join(random.choice(string.ascii_letters) for _ in range (longitud)))
        #matusculas - numeros
        elif mayusculas == "si" and minusculas == "no" and numeros == "si" and simbolos == "no":
            generar = (''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range (longitud)))
        #mayusculas - simbolos
        elif mayusculas == "si" and minusculas == "no" and numeros == "no" and simbolos == "si":
            generar = (''.join(random.choice(string.ascii_uppercase+caracteresEspeciales) for _ in range (longitud)))
        #minusculas - numeros
        elif mayusculas == "no" and minusculas == "si" and numeros == "si" and simbolos == "no":
            generar = (''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range (longitud)))
        #minusculas - simbolos
        elif mayusculas == "no" and minusculas == "si" and numeros == "no" and simbolos == "si":
            generar = (''.join(random.choice(string.ascii_lowercase+caracteresEspeciales) for _ in range (longitud)))
        #numeros - simbolos
        elif mayusculas == "no" and minusculas == "no" and numeros == "si" and simbolos == "si":
            generar = (''.join(random.choice(string.digits+caracteresEspeciales) for _ in range (longitud)))
        #mayusculas - minusculas - numeros
        elif mayusculas == "si" and minusculas == "si" and numeros == "si" and simbolos == "no":
            generar = (''.join(random.choice(string.ascii_letters+string.digits) for _ in range (longitud)))
        #mayusculas - minusculas - simbolos
        elif mayusculas == "si" and minusculas == "si" and numeros == "no" and simbolos == "si":
            generar = (''.join(random.choice(string.ascii_lowercase+caracteresEspeciales) for _ in range (longitud)))
        #minusculas -numeros - simbolos
        elif mayusculas == "no" and minusculas == "si" and numeros == "si" and simbolos == "si":
            generar = (''.join(random.choice(string.ascii_lowercase+string.digits+caracteresEspeciales) for _ in range (longitud)))
        #todas las selecciones
        elif mayusculas == "si" and minusculas == "si" and numeros == "si" and simbolos == "si":
            generar = (''.join(random.choice(string.ascii_letters+string.digits+caracteresEspeciales) for _ in range (longitud)))
    return generar

def validarCheken(cheken):
    if cheken is None:
        return "no"
    else:
        return "si"