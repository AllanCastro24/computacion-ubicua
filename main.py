from flask import Flask, render_template, request, redirect, url_for, flash
from ubidots import ApiClient
import sqlite3

conexion = sqlite3.connect('iot.db', check_same_thread=False)
app = Flask(__name__)

#LOGIN
@app.route('/', methods=['GET','POST'])
def index():
   error = ""
   if request.method == 'POST':
      if request.form['username'] == '' or request.form['password'] == '':
         error = "Datos incorrectos. Intente de nuevo"
      else:
         cursor = conexion.cursor()
         cursor.execute('SELECT * FROM usuarios WHERE user == ? AND pass == ?',(request.form['username'],request.form['password']))
         if cursor.fetchone() is not None:
            registro = cursor.fetchall()
            return redirect('/home/'+registro[0])
         else:
            error = "El usuario no existe"

   return render_template('login.html',error=error) 

#REGISTRO
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
            return redirect('/home/'+str(4))
      else:
         error = "Aun faltan datos por capturar"

   return render_template('registro.html',error=error) 

#HOME
@app.route('/home/<id>', methods=['GET','POST'])
def home(id):
   cursor = conexion.cursor()
   cursor.execute('SELECT * FROM dispositivos WHERE usuario == ?',id)
   datos = cursor.fetchall()
   return render_template('dashboard.html',dispositivos=datos)
   
#REGISTRAR DEVICE
@app.route('/registerdevices', methods=['GET','POST'])
def registrardevices():
   error = ""
   id=4
   if request.method == 'POST':
      if request.form['api_label'] != '' or request.form['id_ubidots'] != '' or request.form['token'] != '':
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO dispositivos (id_device, api_label, id_ubidots, token, usuario) VALUES(null,?, ?, ?, ?)",(request.form['api_label'],request.form['id_ubidots'],request.form['token'],id))
            conexion.commit()
            return redirect('/home/'+str(id)) 
      else:
         error = "Aun faltan datos por capturar"

   return render_template('dispositivos.html',error=error)
   
#REGISTRAR VARIABLES
@app.route('/registervariable', methods=['GET','POST'])
def registrarvariable():
   id=1
   error = ""
   if request.method == 'POST':
      if request.form['api_label'] != '' or request.form['id_ubidots'] != '' or request.form['dispositivo'] != '' or request.form['tipo_modulo'] != '':
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO variables (id_variable, api_label, id_ubidots, dispositivo, tipo_modulo) VALUES(null,?, ?, ?, ?)",(request.form['api_label'],request.form['id_ubidots'],id,request.form['tipo_modulo']))
            conexion.commit()
            return redirect('/home/'+str(id)) 
      else:
         error = "Aun faltan datos por capturar"

   return render_template('register_variable.html',error=error)

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
