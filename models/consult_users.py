from config.database import db

def ObtenerUusarioLogin(user, password):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE user="'+user+'" AND PASSWORD="'+password+'"')

    usuario = cursor.fetchall()
    cursor.close()
    return usuario

def ObtenerUusarioUser(user):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE user="'+user+'"')

    usuario = cursor.fetchall()
    cursor.close()
    return usuario

def ObtenerUsuarioValidar(token):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE validate="'+token+'" ')

    usuario = cursor.fetchall()
    cursor.close()
    return usuario

def traerUrlUsuario(url):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE tokenPass ="'+url+'" ')

    usuario = cursor.fetchall()
    cursor.close()
    return usuario