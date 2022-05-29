# computacion-ubicua
Sistema de alarmas IoT con ubidots y python haciendo uso de interfaz web en html5, base de datos en mysql y arduino para manejar las alarmas.

Especificaciones:

* Poder controlar de manera remota las alarmas
* Aplicación web respondiva compatible con todos los navegadores
* Envío de correos, mensajes de texto (proximamente) y llamadas (proximamente) al activarse para llevar un monitoreo

Requerimientos para Python:

* pip install ubidots==1.6.6    #conexión IoT
* pip install flask             #Web server (Backend)
* pip install pymysql           #Conexión con base de datos

Requerimientos para mysql:

* base de datos "IoT"
* Ejecutar el script proporcionado en el repositorio

Requerimientos para arduino:

* librería UbidotsEsp32Mqtt.h

## Resources

* https://github.com/ubidots/ubidots-python
* http://copitosystem.com/es/python-mysql-database/
* https://github.com/FaztWeb/flask-crud-contacts-app