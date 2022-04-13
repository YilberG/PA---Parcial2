from config.database import db

def CrearUsuario(nombre, apellido, user, password, validate):
    cursor = db.cursor()

    cursor.execute("insert into usuarios(nombre_usuario, apellido_usuario, user, password, validate) values(%s,%s,%s,%s,%s)", (
        nombre, 
        apellido, 
        user, 
        password,
        validate,
    ))

    cursor.close()

def UsuarioValidado(token):
    cursor = db.cursor()
    
    cursor.execute('UPDATE usuarios SET validate = "si" WHERE validate="'+token+'" ')

    cursor.close()

def urlcontraseña(user, url):
    cursor = db.cursor()
    cursor.execute('UPDATE usuarios SET tokenPass = "'+url+'" WHERE user="'+user+'" ')
    cursor.close()

def Cambiodecontraseña(url, password):
    cursor = db.cursor()
    cursor.execute('UPDATE usuarios SET password = "'+password+'", tokenPass="" WHERE tokenPass="'+url+'" ')
    User = cursor.fetchone()
    
    cursor.close()
    return User