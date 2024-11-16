import threading

#Clase para gestionar la sesión de usuario
class sesionUsuario:
    def __init__(self):
        self.nombreUsuario = None #Variable para poder almacenar el nombre de usuario

    #Metodo para almacenar el nombre del usuario
    def iniciarSesion(self, nombreUsuario):
        self.nombreUsuario = nombreUsuario

    #Metodo para imprimir el nombre del usuario
    def msotrarSesion(self):
        print(f"Sesión iniciada para el usuario: {self.nombreUsuario}")


#Creamos un objeto local para almacenar los datos específicos de cada hilo
datosSesion = threading.local()

#Función para gestionar la sesión de usuario en un hilo
def gestionarSesion(nombreUsuario):
    datosSesion = sesionUsuario() #Almacenamos la instancia en el objeto local del hilo
    datosSesion.iniciarSesion((nombreUsuario)) #Iniciamos sesión con el nombre de usuario
    datosSesion.msotrarSesion() #Mostramos la sesión para el hilo actual

#Lista con los nombres de usuario
usuarios = ["Ana", "Carlos", "Beatriz", "David", "Elena"]

#Lista para almacenar los hilos
hilos = []

for nombre in usuarios:
    hilo = threading.Thread(target=gestionarSesion, args=(nombre,)) #Creamos el hilo pasándole como parámetro el nombre del usuario

    # Añadimos el hilo a la lista y lo iniciamos
    hilos.append(hilo)
    hilo.start()

#Esperamos a que todos los hilos terminen
for hilo in hilos:
    hilo.join()


