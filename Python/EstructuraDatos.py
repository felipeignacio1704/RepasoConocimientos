# Estructuras de datos

# Listas

# Para crear una lista, simplemente encierra los elementos entre corchetes

frutas = ["manzana", "banana", "naranja"]

print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

# Métodos de listas

# Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista. Algunos métodos comunes son:
    
# append(elemento): agrega un elemento al final de la lista.
# insert(indice, elemento): inserta un elemento en una posición específica de la lista.
# remove(elemento): elimina la primera aparición de un elemento en la lista.
# pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
# sort(): ordena los elementos de la lista en orden ascendente.
# reverse(): invierte el orden de los elementos en la lista.

frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

# Listas de comprensión

nueva_lista = [expresion for elemento in secuencia if condicion]

numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

# En este ejemplo, se crea una nueva lista llamada cuadrados, que contiene los cuadrados de los números pares de la lista numeros. La expresión x ** 2 eleva cada elemento al cuadrado, y la condición if x % 2 == 0 filtra solo los números pares.