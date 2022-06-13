from flask import Flask, render_template, request, redirect, url_for, flash
from ubidots import ApiClient
import sqlite3

conexion = sqlite3.connect('iot.db', check_same_thread=False)
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
   error = ""
   if request.method == 'POST':
      if request.form['username'] != 'admin' or request.form['password'] != 'admin':
         error = "Datos incorrectos. Intente de nuevo"
      else:
         return render_template('dashboard.html')

   return render_template('login.html',error=error) 

@app.route('/registro', methods=['GET','POST'])
def registro():
   error = ""
   if request.method == 'POST':
      if request.form['username'] != '' or request.form['password'] != '' or request.form['confirmar_pass'] != '' or request.form['mail'] != '' or request.form['api_key'] != '' or request.form['token'] != '' or request.form['ubidots_app'] != '' or request.form['telefono'] != '':
         if request.form['password'] != request.form['confirmar_pass']:
            error = "Las contraseñas no coinciden"
         else:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (id_user,user, pass, mail, api_key, token, ubidots_app, num_telefono) VALUES(null,?, ?, ?, ?, ?, ?, ?)",(request.form['username'],request.form['password'],request.form['mail'],request.form['api_key'],request.form['token'],request.form['ubidots_app'],request.form['telefono']))
            conexion.commit()
            api = ApiClient(request.form['api_key'])
            return render_template('dashboard.html') 
      else:
         error = "Aun faltan datos por capturar"

   return render_template('registro.html',error=error) 

@app.route('/home')
def home():
   return render_template('dashboard.html') 
   
@app.route('/frecuencia')
def frecuencia():
   return render_template('frecuencia.html') 
   
@app.route('/humedad')
def humedad():
   return render_template('humedad.html') 
   
@app.route('/presion')
def presion():
   return render_template('presion.html')
   
@app.route('/temperatura')
def temperatura():
   return render_template('temperatura.html')

@app.route('/voltaje')
def voltaje():
   return render_template('voltaje.html')


if __name__ == '__main__':
   app.debug = True
   app.run(host="127.0.0.1",port=5000)
