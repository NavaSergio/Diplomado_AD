# 19.3.1. Introducción a los closures
# Concepto de closures en Python: Son funciones que capturan variables del ámbito en el que fueron creadas.
# Importancia de los closures en la programación funcional: Permiten crear funciones con estado.

# 19.3.2. Creación de closures
# Sintaxis básica para crear closures
def crear_multiplicador(n):
    def multiplicador(x):
        return x * n
    return multiplicador

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(duplicar(5))  # Salida: 10
print(triplicar(5))  # Salida: 15

# 19.3.3. Introducción a los decoradores
# Concepto de decoradores en Python: Son funciones que modifican el comportamiento de otras funciones.
# Importancia de los decoradores en la modificación de funciones: Permiten extender funcionalidades sin modificar el código original.

# 19.3.4. Creación de decoradores
# Sintaxis básica para crear decoradores
def decorador(func):
    def envoltura(*args, **kwargs):
        print("Antes de la función")
        resultado = func(*args, **kwargs)
        print("Después de la función")
        return resultado
    return envoltura

@decorador
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Juan"))
# Salida:
# Antes de la función
# Hola, Juan
# Después de la función

# 19.3.5. Uso de decoradores en funciones
# Aplicación de decoradores a funciones
@decorador
def sumar(a, b):
    return a + b

print(sumar(3, 5))
# Salida:
# Antes de la función
# 8
# Después de la función