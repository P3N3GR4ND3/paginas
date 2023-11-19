from flask import Flask, render_template, request, redirect ,session, url_for,Response

from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL, MySQLdb
from flask.globals import session
import os
import shutil

app = Flask(__name__)
app.secret_key = "asdfghqwer"
##########################################
        #BASE DE DATOS USUARIOS Y CONTRA

app.config['MYSQL_HOST'] = '192.168.2.103'
app.config['MYSQL_PASSWORD'] = 'hacker'  #'pene1234'
app.config['MYSQL_USER'] = 'hacker' #'pene'
app.config['MYSQL_DB'] = 'usuario'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Función de filtro para verificar la ruta
def check_route(route):
    if "restriccion" in route:
        return True
    return False

@app.route("/")
def index():
    return "<center><h1>pagina de inicio</h1></center>"

@app.route("/adm")
def admon():
    return render_template("index.html")

@app.route("/acceso", methods=["POST", "GET"])
def acceso():
    if request.method == "POST":
        #if request.method == "POST" and 'name' in request.form and 'email':
        nombre = request.form['name']
        gmail = request.form['email']

        #conectamos con la base de datos 
        cur=mysql.connection.cursor()
        #ejecutamos una consulta a la base de datos comparando
        #los datos que contienen las variables "nombre" y "email"
        cur.execute('SELECT * FROM registrados WHERE nombre = %s AND email = %s',(nombre,gmail,))
        #ejecutamos la conexion y con ello la consulta
        session['nombre'] = nombre

        #en caso de que los datos comparados coincidan con las de la base de datos 
        #las guardamos en esta bariable "cuenta"
        cuenta = cur.fetchone()

        session['webos'] = nombre
        if cuenta:
            session['logeado'] = True
            session['id'] = cuenta['id']
            #return render_template("usurio.html")
            return redirect(url_for("pagina"))
        else:

            return render_template("index.html",mensaje="USUARIO NO RECONOCIDO!!", mensajedos="ACCESO DENEGADO!!")
men = "<center><h1>desgraciado <br> no entres a rutas a las que no tienes permiso!! </h1></center>"


@app.route("/setso")
def pagina():
    if "webos" in session:
        return render_template("paginados.html")
    return men

@app.route("/semen")
def siguiente():
    if "webos" in session:
        return render_template("paginados.html")
    return "no estas logeado o registrado wey"

@app.route("/webos")
def display_images():
    # La URL de tu servidor de ngrok donde se encuentran las imágenes
    ngrok_url = "https://c369-181-115-167-130.ngrok-free.app"
    
    return render_template("fotos.html", ngrok_url=ngrok_url)
if __name__=='__main__':
    app.secret_key="webos1234"
    app.run(debug=True, host="0.0.0.0", port=4444)
