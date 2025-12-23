from flask_restful import Resource

from flask import make_response, render_template



#Aquí se pondrán los recursos que el servidor tendrá disponible
#Recursos = Información o Acciones que el servidor puede ejecutar.


#Vamos a crear Recursos = Acción/Información
#Para poder crear un recurso se hará a través de clases y objetos

class HolaMundo(Resource):
#Los recursos van a poder ejecutar 2 acciones = (métodos)
#El primer método es "get"
    def get(self):
        return {"Hola": "Mundo"}

#Será un recurso
class PantallaInicio(Resource):
    def get(self):
        #Renderizamos el contenido del archivo html
        contenido = render_template("index.html")

        #Retornamos el contenido renderizado en una respuesta
        return make_response(contenido)
