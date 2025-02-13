# 12.2.1. Métodos de búsqueda y reemplazo
posicion = mensaje.find("mundo")  # Encuentra la posición de la subcadena "mundo"
print("Posición de 'mundo':", posicion)  # Salida: Posición de 'mundo': 6

mensaje_reemplazado = mensaje.replace("mundo", "Python")  # Reemplaza "mundo" por "Python"
print("Mensaje reemplazado:", mensaje_reemplazado)  # Salida: Mensaje reemplazado: Hola, Python!

# 12.2.2. Métodos de transformación
mensaje_mayusculas = mensaje.upper()  # Convierte la cadena a mayúsculas
print("Mensaje en mayúsculas:", mensaje_mayusculas)  # Salida: Mensaje en mayúsculas: HOLA, MUNDO!

mensaje_minusculas = mensaje.lower()  # Convierte la cadena a minúsculas
print("Mensaje en minúsculas:", mensaje_minusculas)  # Salida: Mensaje en minúsculas: hola, mundo!

mensaje_capitalizado = mensaje.capitalize()  # Capitaliza la primera letra de la cadena
print("Mensaje capitalizado:", mensaje_capitalizado)  # Salida: Mensaje capitalizado: Hola, mundo!

# 12.2.3. Métodos de división y unión
palabras = mensaje.split(", ")  # Divide la cadena en una lista de palabras
print("Palabras:", palabras)  # Salida: Palabras: ['Hola', 'mundo!']

mensaje_unido = " ".join(palabras)  # Une las palabras en una cadena
print("Mensaje unido:", mensaje_unido)  # Salida: Mensaje unido: Hola mundo!

# 12.2.4. Métodos de validación
es_alfanumerico = mensaje.isalnum()  # Verifica si la cadena es alfanumérica
print("¿Es alfanumérica?:", es_alfanumerico)  # Salida: ¿Es alfanumérica?: False

es_numerico = "123".isnumeric()  # Verifica si la cadena es numérica
print("¿Es numérica?:", es_numerico)  # Salida: ¿Es numérica?: True