from flask import flash
from models import consult_archivos
from controllers import validacion_archivo_controlador
import os
from controllers import tipo_imagen_controlador

def retornar_acceso(acceso):
    if acceso is None:
        return 'NO'
    return 'SI'

def cambiar_nombre(nombre_archivo, id_archivo, acceso_archivo):
    consult_archivos.editarNombre(nombre_archivo,id_archivo, acceso_archivo)

def cambiar_todo(nombre_archivo, id_archivo, acceso_archivo, imagen_archivo):
    ruta_archivo = validacion_archivo_controlador.ruta_archivo(imagen_archivo)
    extension = imagen_archivo.filename
    extension = extension.split('.')
    tipo_archivo = extension[-1]
    peso_archivo = validacion_archivo_controlador.convert(os.stat('./static/images/'+ruta_archivo).st_size)
    ruta_imagen_archivo = tipo_imagen_controlador.tipo_archivo(tipo_archivo,ruta_archivo)
    consult_archivos.editarTodo(nombre_archivo, ruta_archivo, ruta_imagen_archivo, tipo_archivo, peso_archivo, id_archivo, acceso_archivo)
