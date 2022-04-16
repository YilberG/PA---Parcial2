import os
from datetime import datetime
def ruta_archivo(archivo):
    hora_fecha = datetime.now()
    nombre = archivo.filename
    nombre = nombre.split('.')
    nuevo_nombre = str(hora_fecha.date())+'_'+str(hora_fecha.hour)+'_'+str(hora_fecha.minute)+'_'+str(hora_fecha.second)+'_'+str(hora_fecha.microsecond)+'.'+str(nombre[-1])
    archivo.save('./static/images/'+archivo.filename)#guardar el archivo en la ruta :v
    os.rename('./static/images/'+archivo.filename,'./static/images/'+nuevo_nombre)#renombrar el archivo :v
    ruta_archivo = './static/images/'+nuevo_nombre
    return ruta_archivo
