# Para trabajar con archivos en Python, primero se debe abrir el archivo y luego cerrarlo después de realizar las operaciones necesarias.

# 14.1.1. Introducción al manejo de archivos
# Python proporciona funciones para abrir, leer, escribir y cerrar archivos.

# 14.1.2. Apertura de archivos
# Se utiliza la función `open()` para abrir un archivo. Se debe especificar el modo de apertura (lectura, escritura, etc.).
archivo = open("ejemplo.txt", "r")  # Abre el archivo en modo lectura

# 14.1.3. Cierre de archivos
# Es importante cerrar el archivo después de realizar las operaciones para liberar recursos.
archivo.close()  # Cierra el archivo

# 14.1.4. Uso de `with` para manejo seguro de archivos
# La sentencia `with` se utiliza para asegurar que el archivo se cierre automáticamente después de las operaciones.
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)  # Salida: Contenido del archivo: [contenido del archivo]