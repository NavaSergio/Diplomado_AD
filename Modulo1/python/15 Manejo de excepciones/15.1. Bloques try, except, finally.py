# El manejo de excepciones permite capturar y manejar errores en tiempo de ejecución.

# 15.1.1. Introducción al manejo de excepciones
# Se utiliza `try` para envolver código que puede generar excepciones, `except` para manejar las excepciones y `finally` para ejecutar código que debe ejecutarse siempre.

# 15.1.2. Uso de `try`
# El bloque `try` contiene el código que puede generar una excepción.
try:
    resultado = 10 / 0  # Esto generará una excepción ZeroDivisionError
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")  # Salida: Error: No se puede dividir por cero.

# 15.1.3. Uso de `except`
# El bloque `except` maneja la excepción especificada.
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")  # Salida: Error: No se puede dividir por cero.

# 15.1.4. Uso de `finally`
# El bloque `finally` se ejecuta siempre, independientemente de si ocurrió una excepción o no.
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
finally:
    print("Este bloque siempre se ejecuta.")  # Salida: Este bloque siempre se ejecuta.