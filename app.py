#Desde la libreria "flask"
#Se importa la clase Flask
from flask import Flask
#Desde flask_restful importamos la clase API y la clase Resource
from flask_restful import Api, Resource
from Routes import crear_rutas


#Se crea un objeto de tipo Flask
app = Flask(__name__)

#Creamos un objeto de tipo API y como argumento
#le pasamos el objeto app

#El parametro/Argumento que espera recibir es el objeto de Flask
api = Api(app)

#La API es el programa que se comunicará con el dispositivo físico


crear_rutas(api)


#Del objeto app ejecutamos el método run
app.run(port=8080, debug=True)
#127.0.0.1 - LoopBack | IP local

