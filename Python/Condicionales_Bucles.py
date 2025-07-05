# IF

# La estructura if se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es la siguiente:
edad = 18


if edad >= 18:
   print ("Eres mayor de edad.")

# IF-ELSE

# La estructura if-else nos permite especificar un bloque de código alternativo que se ejecutará si la condición del if es falsa. La sintaxis básica es la siguiente:
edad = 15


if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")

# IF-ELIF-ELSE

# La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos. La sintaxis básica es la siguiente:

calificacion = 85


if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")

# For

# El bucle for se utiliza para iterar sobre una secuencia (como una lista, una tupla o una cadena) o cualquier objeto iterable. La sintaxis básica es la siguiente:

frutas = ["manzana", "banana", "naranja"]


for fruta in frutas:
   print(fruta)

# While

# El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera. La sintaxis básica es la siguiente:

contador = 0


while contador < 5:

   print(contador)
   contador += 1

# Control de bucles

# Break

# La instrucción break se utiliza para salir prematuramente de un bucle, independientemente de la condición. Cuando se encuentra un break, el bucle se detiene y el flujo de ejecución continúa con la siguiente instrucción fuera del bucle.

contador = 0


while True:

   print(contador)
   contador += 1


   if contador == 5:
      break

# Continue

# La instrucción continue se utiliza para saltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración.

for i in range(10):

   if i % 2 == 0:
      continue
   print(i)


# Pass

# La instrucción pass es una operación nula que no hace nada. Se utiliza como marcador de posición cuando se requiere una instrucción sintácticamente, pero no se desea realizar ninguna acción.

for i in range(5):
   pass

# En este ejemplo, el bucle for itera sobre los números del 0 al 4, pero no se realiza ninguna acción dentro del bucle debido a la instrucción pass. Esto puede ser útil cuando se está desarrollando un programa y se desea reservar un bloque de código para implementarlo más adelante.