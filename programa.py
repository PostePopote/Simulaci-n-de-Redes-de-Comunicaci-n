import os
os.system("cls")

# Creo la clase Nodo junto a sus metodos
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def enviar_mensaje(self, mensaje):
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibio: {mensaje}")

# Hago el objeto que sera el servidor
servidor = Nodo("Servidor")

# Hago objetos con el nombre de los clientes
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")
# Conecto las conexiones de los clientes con el servidor
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)
# Envio un mensaje a cada uno
servidor.enviar_mensaje("Hola chicos, mañana traigan impreso el teorico")