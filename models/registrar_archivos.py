from config.database import db
def crearArchivo(id_usuario,nombre_archivo,ruta_archivo,tipo_archivo,peso_archivo,acceso_archivo,ruta_imagen_archivo):
    Cursor = db.cursor()

    Cursor.execute('insert into archivos(id_usuario,nombre_archivo,ruta_archivo,tipo_archivo,peso_archivo,acceso_archivo,ruta_imagen_archivo) values(%s,%s,%s,%s,%s,%s,%s)',(
        id_usuario,
        nombre_archivo,
        ruta_archivo,
        tipo_archivo,
        peso_archivo,
        acceso_archivo,
        ruta_imagen_archivo
    ))


    Cursor.close()