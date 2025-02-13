# La función `print()` se utiliza para mostrar datos en la consola.

# 13.2.1. Introducción a `print()`
print("Hola, mundo!")  # Salida: Hola, mundo!

# 13.2.2. Sintaxis básica de `print()`
nombre = "Juan"
edad = 25
print("Nombre:", nombre, "Edad:", edad)  # Salida: Nombre: Juan Edad: 25

# 13.2.3. Formateo de salida con `print()`
# Se pueden usar diferentes métodos de formateo para mostrar datos de manera más clara.
print("Nombre: %s, Edad: %d" % (nombre, edad))  # Salida: Nombre: Juan, Edad: 25
print("Nombre: {}, Edad: {}".format(nombre, edad))  # Salida: Nombre: Juan, Edad: 25
print(f"Nombre: {nombre}, Edad: {edad}")  # Salida: Nombre: Juan, Edad: 25

# 13.2.4. Salida de múltiples valores
# Se pueden imprimir múltiples valores separados por comas.
print("Nombre:", nombre, "Edad:", edad, "Años.")  # Salida: Nombre: Juan Edad: 25 Años.