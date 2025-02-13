# calculadora/aritmetica.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# calculadora/geometria.py
import math

def area_circulo(radio):
    return math.pi * radio ** 2

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

# script_principal.py
from calculadora.aritmetica import sumar, restar, multiplicar, dividir
from calculadora.geometria import area_circulo, perimetro_rectangulo

# Uso de las funciones
print(sumar(5, 3))  # Salida: 8
print(restar(5, 3))  # Salida: 2
print(multiplicar(5, 3))  # Salida: 15
print(dividir(5, 3))  # Salida: 1.6666666666666667

print(area_circulo(5))  # Salida: 78.53981633974483
print(perimetro_rectangulo(5, 3))  # Salida: 16