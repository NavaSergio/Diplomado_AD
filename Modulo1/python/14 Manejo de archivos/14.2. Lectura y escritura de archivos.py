# 14.2.1. Lectura de archivos
# Se pueden leer archivos de diferentes maneras: lectura completa, lectura línea por línea, etc.
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()  # Lee el contenido completo del archivo
    print("Contenido completo:", contenido)  # Salida: Contenido completo: [contenido del archivo]

    archivo.seek(0)  # Vuelve al inicio del archivo
    lineas = archivo.readlines()  # Lee todas las líneas del archivo y las almacena en una lista
    print("Líneas del archivo:", lineas)  # Salida: Líneas del archivo: ['línea 1\n', 'línea 2\n', 'línea 3\n']

# 14.2.2. Escritura de archivos
# Se pueden escribir archivos en modo escritura (`w`) o añadir contenido (`a`).
with open("nuevo_archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!\n")  # Escribe una línea en el archivo
    archivo.write("Este es un nuevo archivo.\n")  # Escribe otra línea en el archivo

# 14.2.3. Añadir contenido a archivos
# Se utiliza el modo `a` para añadir contenido al final de un archivo existente.
with open("nuevo_archivo.txt", "a") as archivo:
    archivo.write("Este contenido se añade al final del archivo.\n")  # Añade una línea al final del archivo

# 14.2.4. Lectura y escritura de archivos binarios
# Se pueden manejar archivos binarios utilizando los modos `rb` y `wb`.
with open("imagen.jpg", "rb") as archivo:
    contenido_binario = archivo.read()  # Lee el contenido binario del archivo
    print("Contenido binario:", contenido_binario)  # Salida: Contenido binario: [contenido binario]

with open("copia_imagen.jpg", "wb") as archivo:
    archivo.write(contenido_binario)  # Escribe el contenido binario en un nuevo archivo