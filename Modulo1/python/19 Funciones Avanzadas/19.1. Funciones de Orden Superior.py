# 19.1.1. Introducción a las funciones de orden superior
# Concepto de funciones de orden superior en programación: Son funciones que pueden tomar otras funciones como argumentos o devolver funciones como resultado.
# Importancia de las funciones de orden superior en Python: Permiten escribir código más modular y reutilizable.

# 19.1.2. Funciones que reciben funciones como argumentos
# Uso de funciones como argumentos en otras funciones
def aplicar_funcion(func, lista):
    return [func(x) for x in lista]

def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = aplicar_funcion(cuadrado, numeros)
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

# 19.1.3. Funciones que devuelven funciones
# Uso de funciones que devuelven otras funciones
def crear_multiplicador(n):
    def multiplicador(x):
        return x * n
    return multiplicador

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(duplicar(5))  # Salida: 10
print(triplicar(5))  # Salida: 15

# 19.1.4. Funciones integradas de orden superior
# Uso de funciones integradas como map(), filter(), reduce()
from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Uso de map()
cuadrados = map(cuadrado, numeros)
print(list(cuadrados))  # Salida: [1, 4, 9, 16, 25]

# Uso de filter()
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Salida: [2, 4]

# Uso de reduce()
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Salida: 15