from itertools import product
from colorama import Cursor
from config.database import db

def traerArchivos ():
    Cursor = db.cursor(dictionary = True)
    Cursor.execute('select * from archivos where acceso_archivo = "SI" order by id_producto desc')
    productos = Cursor.fetchall()
    Cursor.close()
    return productos

def traerArchivos_usuario(IDUsuario):
    Cursor = db.cursor(dictionary = True)
    Cursor.execute('select * from archivos where id_usuario = "'+IDUsuario+'" order by id_producto desc')
    productos = Cursor.fetchall()
    Cursor.close()
    return productos