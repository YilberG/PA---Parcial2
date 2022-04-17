from itertools import product
from colorama import Cursor
from config.database import db
#TRAE ARCHIVOS PARA MOSTRARLOS EN EL INDEX
def traerArchivos ():
    Cursor = db.cursor(dictionary = True)
    Cursor.execute('select * from archivos where acceso_archivo = "SI" order by id_producto desc')
    productos = Cursor.fetchall()
    Cursor.close()
    return productos
#TRAE ARCHIVOS PARA MOSTRARLOS SEGUN EL USUARIO
def traerArchivos_usuario(IDUsuario):
    Cursor = db.cursor(dictionary = True)
    Cursor.execute('select * from archivos where id_usuario = "'+IDUsuario+'" order by id_producto desc')
    productos = Cursor.fetchall()
    Cursor.close()
    return productos

#ELIMINAR PRODUCTOS
def eliminar_productos(id_producto_eliminar, id_usuario):
    Cursor = db.cursor(dictionary = True)
    Cursor.execute('delete from archivos where id_producto = "'+id_producto_eliminar+'" and id_usuario = "'+id_usuario+'" ')
    Cursor.close()

#VISTA PREVIA DE LOS ARCHIVOS
def vistaPrevia_archivos(vistaPrevia):
    Cursor = db.cursor(dictionary = True)
    Cursor.execute('select * from archivos where id_producto = "'+vistaPrevia+'" ')
    productos = Cursor.fetchone()
    Cursor.close()
    return productos