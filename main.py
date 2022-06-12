from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from ubidots import ApiClient

api = ApiClient(token='BBFF-64938518cc32029778d00492468aec11406')

app = Flask(__name__)

@app.route('/')
def index():
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
