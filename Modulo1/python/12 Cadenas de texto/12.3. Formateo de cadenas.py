# 12.3.1. Formateo con `%`
nombre = "Juan"
edad = 25
mensaje_formateado = "Hola, mi nombre es %s y tengo %d años." % (nombre, edad)
print("Mensaje formateado:", mensaje_formateado)  # Salida: Mensaje formateado: Hola, mi nombre es Juan y tengo 25 años.

# 12.3.2. Formateo con `format()`
mensaje_formateado = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print("Mensaje formateado:", mensaje_formateado)  # Salida: Mensaje formateado: Hola, mi nombre es Juan y tengo 25 años.

# 12.3.3. Formateo con f-strings
mensaje_formateado = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print("Mensaje formateado:", mensaje_formateado)  # Salida: Mensaje formateado: Hola, mi nombre es Juan y tengo 25 años.

# 12.3.4. Formateo avanzado
import datetime
hoy = datetime.datetime.now()
mensaje_formateado = f"Hoy es {hoy:%d/%m/%Y}."
print("Mensaje formateado:", mensaje_formateado)  # Salida: Mensaje formateado: Hoy es 01/01/2023.