from ast import Return
from cmath import pi
from email.quoprimime import body_check
from pickletools import read_uint1
from random import random
import string
from turtle import title
from click import password_option
from flask import Flask, render_template, request, redirect, url_for, flash
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

app = Flask(__name__)
app.secret_key = 'XDXDXDXDXDX'

@app.get("/")
def index():
    return render_template("index.html")

#LOGIN
@app.get("/login")
def login():
    return render_template("usuarios/login.html")

@app.post("/login")
def loginPost():
    user = request.form.get('user')
    contraseña = request.form.get('password')
    if not login_controlador.login_controlador(user, contraseña):
        return render_template("usuarios/login.html", user = user)
    return redirect(url_for('index'))

@app.get("/register")
def register():
    return render_template("usuarios/register.html")

@app.post("/register")
def registerPost():
    name = request.form.get('name')
    user = request.form.get('user')
    contraseña = request.form.get('password')
    last_name = request.form.get('last_name')
    

    if not registro_controlador.registro_controlador(name,user,contraseña):
        return render_template("usuarios/register.html", name=name, user = user, last_name = last_name)
    
    registro_controlador.DBregistro_controlador(name,last_name,user,contraseña)
    return redirect(url_for('index')) 

@app.get("/validar-cuenta/<token>")
def validar_cuenta(token):
    validar = consult_users.ObtenerUsuarioValidar(token = token)

    if not validar:
        return "USUARIO NO EXISTE: "+token
    else:
        register_user.UsuarioValidado(token = token)
        return render_template("usuarios/validado.html")
#RESTABLECER LA CONTRASEÑA
@app.get('/recuperarPass')
def recuperarPass():
    return render_template("/usuarios/recuperarPass.html")

@app.post('/recuperarPass')
def recuperarPassPost():
    user = request.form.get('user')
    if not recuperarPass_controlador.recuperarPassControlador(user):
        return render_template("/usuarios/recuperarPass.html", user = user)
    
    recuperarPass_controlador.DBrecuperarPassControlador(user)
    return render_template('index.html')
    
@app.get('/recuperarPass/<url>')
def formularioPassRec(url):
    usuario = consult_users.traerUrlUsuario(url)
    if not usuario:
        return render_template('/fallos/urlnotexits.html')
    else:
        return render_template('/usuarios/formularioPass.html',url=url)
@app.post('/recuperarPass/<url>')
def formularioPassRecPost(url):
    usuario = consult_users.traerUrlUsuario(url)
    if not usuario:
        return render_template('/fallos/urlnotexits.html')
    else:
        contraseña = request.form.get('password')
        if not contraseña_controlador.validacionPassControlador(contraseña):
            return render_template('/usuarios/formularioPass.html',url=url)
        contraseña_controlador.enviarBDNewPassword(url,contraseña)
        return render_template('index.html')
    
app.run(debug=True)