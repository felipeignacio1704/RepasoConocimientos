# Además de utilizar los módulos estándar de Python, también podemos crear nuestros propios módulos para organizar y reutilizar nuestro código.

# Crear y utilizar módulos personalizados


# Para crear un módulo personalizado, simplemente creamos un nuevo archivo Python con el nombre deseado y definimos las funciones, clases y variables que queremos incluir en el módulo. Por ejemplo, creamos un archivo (en el mismo directorio donde estamos ejecutando Python) llamado mi_modulo.py con el siguiente contenido:
    

#mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")


def calcular_suma(a, b):
    return a + b

# Luego, podemos importar y utilizar las funciones definidas en mi_modulo.py en otro archivo Python.

import mi_modulo


mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

# En este ejemplo, se importa el módulo mi_modulo y se utilizan las funciones saludar() y calcular_suma() definidas en él.


# Organización del código en módulos

# A medida que nuestros programas crecen en tamaño y complejidad, es una buena práctica organizar nuestro código en módulos separados según su funcionalidad. Esto nos permite conservar un código más legible, agrupado en módulos y fácil de mantener.

# Por ejemplo, podemos tener un módulo operaciones.py que contenga funciones relacionadas con operaciones matemáticas, y otro módulo utilidades.py que contenga funciones de uso general.

# operaciones.py
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


# utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)


def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")

# Luego, podemos importar y utilizar estas funciones en nuestro programa principal.

import operaciones
import utilidades


resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

# Al organizar nuestro código en módulos, podemos reutilizar funciones y mantener un código más estructurado y agrupado en módulos.

# Un paquete es una forma de organizar módulos relacionados en una estructura jerárquica de directorios. Los paquetes nos permiten agrupar módulos relacionados y evitar conflictos de nombres entre módulos.

# Crear y utilizar paquetes

# Para crear un paquete, creamos un directorio con el nombre deseado y agregamos un archivo especial llamado __init__.py dentro del directorio. Este archivo puede estar vacío o contener código de inicialización del paquete.

# Por ejemplo, creamos un directorio llamado mi_paquete con la siguiente estructura:

mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
# Luego, podemos importar y utilizar los módulos del paquete en nuestro programa.

from mi_paquete import modulo1, modulo2


modulo1.funcion1()
modulo2.funcion2()

# En este ejemplo, se importan los módulos modulo1 y modulo2 del paquete mi_paquete y se utilizan las funciones definidas en ellos.


# La importación y creación de módulos y paquetes en Python nos permite organizar y reutilizar nuestro código de manera eficiente. Al modularizar nuestro código, podemos mantener un código más legible, estructurado y fácil de mantener.

# Recuerda explorar la biblioteca estándar de Python y aprovechar los módulos existentes, que pueden facilitarte muchas tareas comunes. Además, no dudes en crear tus propios módulos y paquetes para organizar y reutilizar tu código de manera efectiva.