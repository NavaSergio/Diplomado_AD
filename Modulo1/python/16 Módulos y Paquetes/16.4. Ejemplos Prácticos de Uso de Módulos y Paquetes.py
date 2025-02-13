# Ejemplo 1: Importación de módulos estándar
import math
import random
import datetime

print(math.pi)  # Salida: 3.141592653589793
print(random.randint(1, 10))  # Salida: Un número aleatorio entre 1 y 10
print(datetime.datetime.now())  # Salida: Fecha y hora actual

# Ejemplo 2: Creación y uso de módulos personalizados
# mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

# otro_script.py
import mi_modulo

mi_modulo.saludar("Pedro")  # Salida: Hola, Pedro!

# Ejemplo 3: Creación y uso de paquetes personalizados
# mi_paquete/submodulo.py
def funcion_submodulo():
    print("Función del submódulo")

# otro_script.py
from mi_paquete.submodulo import funcion_submodulo

funcion_submodulo()  # Salida: Función del submódulo

# Ejemplo 4: Uso de if __name__ == "__main__":
# mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

if __name__ == "__main__":
    print("Este código solo se ejecuta si este archivo es el script principal.")
    saludar("Mundo")  # Salida: Hola, Mundo!