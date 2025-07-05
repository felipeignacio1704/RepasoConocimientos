# Aritméticos
# Los operadores aritméticos se utilizan para realizar operaciones matemáticas básicas. Los principales operadores aritméticos en Python son:

# Suma (+): suma dos valores.
# Resta (-): resta el segundo valor del primero.
# Multiplicación (*): multiplica dos valores.
# División (/): divide el primer valor por el segundo y devuelve un resultado de tipo flotante.
# División entera (//): divide el primer valor por el segundo y devuelve un resultado de tipo entero (se descarta la parte decimal).
# Módulo (%): devuelve el resto de la división entre el primer valor y el segundo.
# Exponenciación (**): eleva el primer valor a la potencia del segundo.

a = 10
b = 3


suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1
exponenciacion = a ** b   # 1000

# De comparación
# Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano (True o False) según el resultado de la comparación. Los operadores de comparación en Python son:

# Igual a (==): devuelve True si ambos valores son iguales.
# Diferente de (!=): devuelve True si los valores son diferentes.
# Mayor que (>): devuelve True si el primer valor es mayor que el segundo.
# Menor que (<): devuelve True si el primer valor es menor que el segundo.
# Mayor o igual que (>=): devuelve True si el primer valor es mayor o igual que el segundo.
# Menor o igual que (<=): devuelve True si el primer valor es menor o igual que el segundo.

a = 10
b = 3


igual = a == b   # False
diferente = a != b   # True
mayorque = a > b   # True
menorque = a < b   # False
mayoroigual = a >= b   # True
menoroigual = a <= b   # False

# Lógicos

# Los operadores lógicos se utilizan para combinar expresiones condicionales y evaluar múltiples condiciones. Los operadores lógicos en Python son:

# AND (and): devuelve True si ambas condiciones son verdaderas.
# OR (or): devuelve True si al menos una de las condiciones es verdadera.
# NOT (not): invierte el valor de una condición, devuelve True si la condición es falsa y False si la condición es verdadera.

a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False