# 14.3.1. Introducción a las excepciones en el manejo de archivos
# Es importante manejar excepciones para evitar errores al trabajar con archivos.

# 14.3.2. Uso de `try`, `except`, `finally`
# Se utiliza `try` para envolver operaciones de archivos, `except` para manejar excepciones y `finally` para asegurar el cierre del archivo.
try:
    archivo = open("ejemplo.txt", "r")
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)  # Salida: Contenido del archivo: [contenido del archivo]
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    archivo.close()  # Asegura que el archivo se cierre incluso si ocurre una excepción

# 14.3.3. Excepciones comunes en el manejo de archivos
# Algunas excepciones comunes incluyen `FileNotFoundError`, `PermissionError`, `IOError`.
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")  # Salida: El archivo no existe.
except PermissionError:
    print("No tienes permisos para acceder al archivo.")
except IOError:
    print("Ocurrió un error de entrada/salida.")