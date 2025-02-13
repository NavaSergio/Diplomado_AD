# 24.2.1. Uso de map()
# Definición y uso de map() para aplicar una función a una secuencia
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, numeros)
print(list(cuadrados))  # Salida: [1, 4, 9, 16, 25]

# 24.2.2. Uso de filter()
# Definición y uso de filter() para filtrar elementos de una secuencia
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Salida: [2, 4]

# 24.2.3. Uso de reduce()
# Definición y uso de reduce() para aplicar una función acumulativa a una secuencia
from functools import reduce
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Salida: 15

# 24.2.4. Uso de lambda
# Definición y uso de funciones lambda
suma = lambda x, y: x + y
print(suma(3, 5))  # Salida: 8