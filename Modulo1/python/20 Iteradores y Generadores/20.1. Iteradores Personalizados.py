# 20.1.1. Introducción a los iteradores
# Concepto de iteradores en Python: Son objetos que permiten recorrer secuencias de elementos.
# Importancia de los iteradores en la iteración de objetos: Facilitan la iteración sobre colecciones de datos.

# 20.1.2. Creación de iteradores personalizados
# Implementación del protocolo de iteración: __iter__() y __next__()
class Contador:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __iter__(self):
        self.actual = self.inicio
        return self

    def __next__(self):
        if self.actual > self.fin:
            raise StopIteration
        valor_actual = self.actual
        self.actual += 1
        return valor_actual

# 20.1.3. Uso de iteradores en bucles for
# Uso de iteradores personalizados en bucles for
contador = Contador(1, 5)
for numero in contador:
    print(numero)  # Salida: 1 2 3 4 5

# 20.1.4. Manejo de la detención de la iteración
# Uso de StopIteration para detener la iteración
contador = Contador(1, 5)
iterador = iter(contador)

try:
    while True:
        print(next(iterador))
except StopIteration:
    print("Fin de la iteración")