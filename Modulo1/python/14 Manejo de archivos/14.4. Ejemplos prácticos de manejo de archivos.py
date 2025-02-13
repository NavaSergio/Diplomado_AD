# 14.4.1. Ejemplo 1: Lectura de un archivo de texto
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)  # Salida: Contenido del archivo: [contenido del archivo]

# 14.4.2. Ejemplo 2: Escritura de un archivo de texto
with open("nuevo_archivo.txt", "w") as archivo:
    archivo.write("Este es un nuevo archivo.\n")
    archivo.write("Contenido adicional.\n")

# 14.4.3. Ejemplo 3: Añadir contenido a un archivo existente
with open("nuevo_archivo.txt", "a") as archivo:
    archivo.write("Este contenido se añade al final del archivo.\n")

# 14.4.4. Ejemplo 4: Manejo de excepciones en operaciones de archivos
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")  # Salida: El archivo no existe.
except PermissionError:
    print("No tienes permisos para acceder al archivo.")
except IOError:
    print("Ocurrió un error de entrada/salida.")