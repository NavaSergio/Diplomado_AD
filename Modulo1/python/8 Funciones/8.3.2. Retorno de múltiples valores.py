# Una función puede devolver múltiples valores usando una tupla.

# Ejemplo de retorno de múltiples valores
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta  # Devuelve una tupla con la suma y la resta

# Llamada a la función y desempaquetado de la tupla
suma, resta = operaciones(10, 4)
print("Suma:", suma)  # Salida: Suma: 14
print("Resta:", resta)  # Salida: Resta: 6