# Las cadenas de texto son secuencias de caracteres encerradas entre comillas simples o dobles.

# 12.1.1. Introducción a las cadenas de texto
mensaje = "Hola, mundo!"
print("Mensaje:", mensaje)  # Salida: Mensaje: Hola, mundo!

# 12.1.2. Creación de cadenas
nombre = "Juan"
apellido = 'Pérez'
nombre_completo = nombre + " " + apellido
print("Nombre completo:", nombre_completo)  # Salida: Nombre completo: Juan Pérez

# 12.1.3. Acceso a caracteres de una cadena
primer_caracter = mensaje[0]
print("Primer caracter:", primer_caracter)  # Salida: Primer caracter: H

# 12.1.4. Modificación de cadenas
# Las cadenas en Python son inmutables, por lo que no se pueden modificar directamente.
# En su lugar, se puede crear una nueva cadena con los cambios deseados.
mensaje_modificado = mensaje.replace("mundo", "Python")
print("Mensaje modificado:", mensaje_modificado)  # Salida: Mensaje modificado: Hola, Python!