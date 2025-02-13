# 20.2.1. Introducción a los generadores
# Concepto de generadores en Python: Son funciones que devuelven un iterador.
# Ventajas de los generadores sobre las listas: Eficiencia en memoria y rendimiento.

# 20.2.2. Creación de generadores con yield
# Sintaxis básica para crear generadores con yield
def generador_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# 20.2.3. Uso de generadores en bucles for
# Uso de generadores en bucles for
for par in generador_pares(10):
    print(par)  # Salida: 0 2 4 6 8

# 20.2.4. Ventajas de los generadores
# Eficiencia en memoria y rendimiento
numeros = [x for x in range(1000000)]  # Lista
generador = (x for x in range(1000000))  # Generador

print(f"Tamaño de la lista: {numeros.__sizeof__()} bytes")
print(f"Tamaño del generador: {generador.__sizeof__()} bytes")