#Aqúi estarán las rutas de acceso a cada recurso
from Resources import *


#Tener el objeto api
def crear_rutas(api):
    # Quiero que la API pueda acceder al recurso por medio de "tal ruta"
    # Este método requiere de 2 argumentos:
    # 1. El recurso que va a ejecturar - Invocar
    # 2. La dirección de este recurso
    api.add_resource(HolaMundo, '/hola')
    # Esto es la ruta de inicio
    api.add_resource(PantallaInicio, '/')


