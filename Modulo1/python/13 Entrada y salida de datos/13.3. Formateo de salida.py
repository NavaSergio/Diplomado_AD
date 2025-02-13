# El formateo de salida permite mostrar datos de manera más clara y estructurada.

# 13.3.1. Formateo con `%`
nombre = "Ana"
edad = 30
print("Nombre: %s, Edad: %d" % (nombre, edad))  # Salida: Nombre: Ana, Edad: 30

# 13.3.2. Formateo con `format()`
print("Nombre: {}, Edad: {}".format(nombre, edad))  # Salida: Nombre: Ana, Edad: 30

# 13.3.3. Formateo con f-strings
print(f"Nombre: {nombre}, Edad: {edad}")  # Salida: Nombre: Ana, Edad: 30

# 13.3.4. Formateo avanzado
import datetime
hoy = datetime.datetime.now()
print("Hoy es {:%d/%m/%Y}.".format(hoy))  # Salida: Hoy es 01/01/2023.