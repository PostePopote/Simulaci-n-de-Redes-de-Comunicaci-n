 Parte uno de Simulaci-n-de-Redes-de-Comunicaci-n
Trabajo de clase, con fecha de entrega el 22 de abril a las 10 de la mañana

Objetivo:
El objetivo de esta actividad es comprender el concepto de redes de comunicación y practicar la implementación de una simulación básica de una red utilizando programación orientada a objetos en Python.
Instrucciones:
Implementación del código:
Escribe el código necesario para crear la simulación de red. De un servidor y tres clientes.
Crea la clase Nodo con sus métodos __init__, agregar_conexion, enviar_mensaje y recibir_mensaje.
Crea instancias de la clase Nodo para representar el servidor y los clientes.
Establece las conexiones entre el servidor y los clientes utilizando el método agregar_conexion.
Simula el envío de un mensaje desde el servidor a todos los clientes conectados utilizando el método enviar_mensaje.
Prueba y depuración:
Ejecuta tu código para verificar que funcione correctamente.
Comprueba que los mensajes se envíen y reciban correctamente entre el servidor y los clientes.
Ayuda: uno de los posibles componentes que se podría usar es : append:
append() es un método de las listas en Python que se utiliza para agregar un elemento al final de la lista.
Entrega:
● Deberán presentar los archivos .py identificados de manera clara y ordenada.
● Trabajar una buena documentación. Subir al repositorio.
● Se debe enviar el enlace al repositorio correspondiente via classroom

Parte dos de Simulaci-n-de-Redes-de-Comunicaci-n
Actividad:

Una vez que tenemos el código de la simulación de red básico vamos a simular una desconexión y conexión de un enrutamiento de la red.

Agregar un método: eliminar_conexion, que a diferencia con agregar usaremos .remove.

Utilizaremos una función de Python “time.sleep(segundos)” , tenemos que importar “time” .Esto hace que el programa se detenga durante los segundos que determinemos antes de continuar con la ejecución del código siguiente. En este caso, se está utilizando para simular un retraso entre la desconexión y la reconexión dinámica de los nodos en la red de comunicación.

Luego del retraso temporal imprimirá el mensaje : “Simulando desconexión y reconexión dinámica…”

Por último imprimirá el mensaje : "¡Hola de nuevo a todos!".
