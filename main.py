from ubidots import ApiClient
from flask import Flask, render_template
import pymysql

#Objeto Flask
app=Flask(__name__)
#Conexión con la BD
db = pymysql.connect("localhost","root","","IoT")
cursor = db.cursor() #Objeto de basde de datos

#Empieza el programa
@app.route('/') #No se indica carpeta, por default es templates
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

#Clase main
if __name__ == '__main__':
    app.run()