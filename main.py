from ast import Return
from cmath import pi
from email.mime import image
from email.quoprimime import body_check
from operator import truediv
from pickletools import read_uint1
from random import random
import string
from turtle import title
from click import password_option
from flask import Flask, render_template, request, redirect, url_for, flash,session
from models import consult_users
from models import register_user
import hashlib
import send_mail
import random
import string
from controllers import login_controlador
from controllers import registro_controlador
from controllers import recuperarPass_controlador
from controllers import contraseña_controlador
from controllers import archivo_controlador

app = Flask(__name__)
app.secret_key = 'XDXDXDXDXDX'

@app.get("/")
def index():
    validarLogin = True
    if not login_controlador.estaIniciado():
        validarLogin = False
    return render_template("index.html",validarLogin=validarLogin)

#LOGIN------------------------------------------------------
@app.get("/login")
def login():
    return render_template("usuarios/login.html")

@app.post("/login")
def loginPost():
    user = request.form.get('user')
    contraseña = request.form.get('password')
    if not login_controlador.login_controlador(user, contraseña):
        return render_template("usuarios/login.html", user = user)
    password_encrypt = hashlib.sha512(contraseña.encode()).hexdigest()
    crearID = consult_users.ObtenerUusarioLogin(user=user, password=password_encrypt)
    
    for val in crearID:
        id = val['id_usuario']
    session['usuario_id'] = id
    
    return redirect(url_for('index'))
    

#REGISTRO DEL USUARIO-------------------------------------------

@app.get("/register")
def register():
    return render_template("registros/register.html")

@app.post("/register")
def registerPost():
    name = request.form.get('name')
    user = request.form.get('user')
    contraseña = request.form.get('password')
    last_name = request.form.get('last_name')
    

    if not registro_controlador.registro_controlador(name,user,contraseña):
        return render_template("registros/register.html", name=name, user = user, last_name = last_name)
    
    registro_controlador.DBregistro_controlador(name,last_name,user,contraseña)
    return redirect(url_for('index')) 

#VALIDAR CUENTA USUARIO---------------------------------------------------------

@app.get("/validar-cuenta/<token>")
def validar_cuenta(token):
    validar = consult_users.ObtenerUsuarioValidar(token = token)

    if not validar:
        return "USUARIO NO EXISTE: "+token
    else:
        register_user.UsuarioValidado(token = token)
        return render_template("usuarios/validado.html")
#RESTABLECER LA CONTRASEÑA------------------------------------------------------------
@app.get('/recuperarPass')
def recuperarPass():
    return render_template("/formularios/recuperarPass.html")

@app.post('/recuperarPass')
def recuperarPassPost():
    user = request.form.get('user')
    if not recuperarPass_controlador.recuperarPassControlador(user):
        return render_template("/formularios/recuperarPass.html", user = user)
    
    recuperarPass_controlador.DBrecuperarPassControlador(user)
    return render_template('index.html')
    
@app.get('/recuperarPass/<url>')
def formularioPassRec(url):
    usuario = consult_users.traerUrlUsuario(url)
    if not usuario:
        return render_template('/fallos/urlnotexits.html')
    else:
        return render_template('/formularios/formularioPass.html',url=url)
@app.post('/recuperarPass/<url>')
def formularioPassRecPost(url):
    usuario = consult_users.traerUrlUsuario(url)
    if not usuario:
        return render_template('/fallos/urlnotexits.html')
    else:
        contraseña = request.form.get('password')
        if not contraseña_controlador.validacionPassControlador(contraseña):
            return render_template('/formularios/formularioPass.html',url=url)
        contraseña_controlador.enviarBDNewPassword(url,contraseña)
        return render_template('index.html')
#PERFIL DEL PERFIL-----------------------------------------------------------
@app.get('/perfil')
def perfilUsuario():
    if not login_controlador.estaIniciado():
        return redirect(url_for('login'))
    return render_template('/usuarios/perfil.html')

#SUBIR PRODUCTOS------------------------------------------------
@app.get('/subirProducto')
def subirprod():
    validarLogin = True
    if not login_controlador.estaIniciado():
        return redirect(url_for('login'))
    return render_template('/archivos/subirProducto.html',validarLogin=validarLogin)

@app.post('/subirProducto')
def subirprodPost():
    validarLogin = True
    if not login_controlador.estaIniciado():
        return redirect(url_for('login'))
    nombre = request.form.get('nombre')
    archivo = request.files['imagen']
    acceso = request.form.get('acceso')
    print (archivo)
    if not archivo_controlador.validarArchivo(nombre,archivo,acceso):
        return render_template('/archivos/subirProducto.html',nombre=nombre,validarLogin=validarLogin)
    archivo_controlador.enviar_archivo_BD(str(session.get('usuario_id')),nombre,archivo,acceso)
    return render_template('index.html',validarLogin=validarLogin)

#ACTUALIZAR PRODUCTOS-------------------------------------------------------
@app.get('/actualizarProducto')
def actualizarProducto():
    return render_template('/archivos/actualizarProducto.html')

#@app.post('actualizarProducto')
#def actualizarProductoPost(actualizarProducto):
#    return actualizarProducto

#CERRRAR SESSION

@app.get("/cerrar_sesion")
def cerrarSesion():
    session.clear()
    
    return redirect(url_for('login'))
app.run(debug=True)