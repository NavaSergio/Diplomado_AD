# `*args` permite pasar un número variable de argumentos posicionales a una función.
# `**kwargs` permite pasar un número variable de argumentos por nombre a una función.

# Ejemplo de `*args`
def sumar(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

# Llamada a la función con múltiples argumentos posicionales
print(sumar(1, 2, 3, 4))  # Salida: 10

# Ejemplo de `**kwargs`
def saludar(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, ":", valor)

# Llamada a la función con múltiples argumentos por nombre
saludar(nombre="Juan", edad=25, ciudad="Madrid")  # Salida: nombre : Juan, edad : 25, ciudad : Madrid