# Las funciones lambda se pueden usar en combinación con otras funciones como `map()`, `filter()`, `reduce()`.

# Ejemplo de uso de funciones lambda con `map()`
numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))  # Aplica la función lambda a cada elemento de la lista
print("Dobles:", dobles)  # Salida: Dobles: [2, 4, 6, 8, 10]

# Ejemplo de uso de funciones lambda con `filter()`
pares = list(filter(lambda x: x % 2 == 0, numeros))  # Filtra los números pares de la lista
print("Pares:", pares)  # Salida: Pares: [2, 4]

# Ejemplo de uso de funciones lambda con `reduce()`
from functools import reduce
suma = reduce(lambda x, y: x + y, numeros)  # Suma todos los elementos de la lista
print("Suma:", suma)  # Salida: Suma: 15