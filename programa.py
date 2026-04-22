import os
os.system("cls")

import time

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

# Parte del ejercicio 2
    def eliminar_conexion(self, nodo):
        self.conexiones.remove(nodo)

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

# Parte del ejercicio 2. Quito las conexion usando el metodo eliminar_conexion
servidor.eliminar_conexion(cliente1)
servidor.eliminar_conexion(cliente2)
servidor.eliminar_conexion(cliente3)
# Utilizo time para esperar 5 segundos para asi dar un mensaje
time.sleep(5)
print("Simulando desconexión y reconexión dinámica...")
# Luego hago otro sleep para decir un mensaje y asi reconectar todo y dar un mensaje general
time.sleep(5)
print("Conexion conectada!")
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)
servidor.enviar_mensaje("Hola denuevo a todos")