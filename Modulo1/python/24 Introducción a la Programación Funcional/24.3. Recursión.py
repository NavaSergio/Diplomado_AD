# 24.3.1. Introducción a la recursión
# Definición y concepto de recursión: Es una técnica en la que una función se llama a sí misma para resolver un problema.
# Ventajas y desventajas de la recursión: Simplifica la solución de algunos problemas, pero puede consumir mucha memoria.

# 24.3.2. Ejemplos de recursión
# Ejemplos de funciones recursivas en Python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Salida: 120

# 24.3.3. Recursión de cola
# Definición y uso de recursión de cola: Es una técnica en la que la llamada recursiva es la última operación de la función.
def factorial_cola(n, acumulador=1):
    if n == 0:
        return acumulador
    else:
        return factorial_cola(n - 1, n * acumulador)

print(factorial_cola(5))  # Salida: 120