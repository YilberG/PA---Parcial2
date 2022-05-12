from config.database import db
#INSERTAR LA URLS-------------------------------------
def paginaUrls(url, nueva):
    cursor = db.cursor()
    cursor.execute("insert into urls(url,nueva) values(%s,%s)",(
        url,
        nueva,
    ))
    cursor.close()

#MOSTRAR URLS EN TABLA---------------------------------
def tablaUrl():
    cursor = db.cursor(dictionary=True)
    cursor.execute('select * from urls')
    urls = cursor.fetchall()
    cursor.close()
    return urls

#MOSTRAR ULTIMA URL ACORTADA----------------------------------
def ultimaUrl():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select nueva from urls order by id desc limit 1')
    ultima = cursor.fetchone()
    cursor.close()
    return ultima

#REDIRECCION DE LA NUEVA URL-----------------------------------------
def nueva(shorturl):
    cursor = db.cursor()
    cursor.execute("select url from urls where nueva = %s", (shorturl,))
    url = cursor.fetchone()
    cursor.close()
    return url
