# 24.1.1. Introducción a la programación funcional
# Definición y características de la programación funcional: Es un paradigma que trata la computación como la evaluación de funciones matemáticas.
# Ventajas de la programación funcional: Modularidad, inmutabilidad, y evitar efectos secundarios.

# 24.1.2. Funciones puras
# Definición de funciones puras: Son funciones que siempre producen el mismo resultado para los mismos argumentos y no tienen efectos secundarios.
def suma_pura(a, b):
    return a + b

# Ejemplos de funciones puras y no puras
def suma_impura(a, b):
    print(f"Sumando {a} y {b}")  # Efecto secundario
    return a + b

# 24.1.3. Inmutabilidad
# Concepto de inmutabilidad en programación funcional: Los datos no cambian una vez creados.
lista_inmutable = (1, 2, 3)  # Tupla, inmutable

# 24.1.4. Funciones de orden superior
# Definición de funciones de orden superior: Son funciones que pueden tomar otras funciones como argumentos o devolver funciones como resultado.
def aplicar_funcion(func, lista):
    return [func(x) for x in lista]

def cuadrado(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = aplicar_funcion(cuadrado, numeros)
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]