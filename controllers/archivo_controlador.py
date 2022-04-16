from select import select
import string
import random
import os
from flask import flash
from controllers import validacion_archivo_controlador
from models import registrar_archivos
def validarArchivo(nombre,archivo,acceso):
    isValid = True
    if acceso is None:
        acceso = 'NO'
    if nombre == '':
        isValid = False
        flash('DEBES INGRESAR UN NOMBRE')
    else:
        if archivo.filename == '':
            isValid = False
            flash('DEBES SELECCIONAR ALGUN ARCHIVO')
    if isValid == False:
        return False
    return True

def enviar_archivo_BD(id_usuario,nombre,archivo,acceso):
    if acceso is None:
        acceso = 'NO'
    ruta_archivo = validacion_archivo_controlador.ruta_archivo(archivo)
    extension = archivo.filename
    extension = extension.split('.')
    tipo_archivo = extension[-1]
    peso_archivo = os.stat(ruta_archivo).st_size
    ruta_imagen_archivo = ''
    url = (''.join(random.choice(string.ascii_letters+string.digits)for _ in range(100)))
    registrar_archivos.crearArchivo(id_usuario,nombre,ruta_archivo,tipo_archivo,peso_archivo,acceso,url,ruta_imagen_archivo)

