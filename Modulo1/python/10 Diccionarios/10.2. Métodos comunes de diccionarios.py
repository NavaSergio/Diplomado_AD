# 10.2.1. Métodos de adición de elementos
persona["email"] = "juan@example.com"  # Añade un nuevo par clave-valor
print("Diccionario después de añadir email:", persona)  # Salida: Diccionario después de añadir email: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'email': 'juan@example.com'}

# 10.2.2. Métodos de eliminación de elementos
del persona["ciudad"]  # Elimina el par clave-valor con la clave "ciudad"
print("Diccionario después de eliminar ciudad:", persona)  # Salida: Diccionario después de eliminar ciudad: {'nombre': 'Juan', 'edad': 31, 'email': 'juan@example.com'}

# 10.2.3. Métodos de iteración y búsqueda
for clave, valor in persona.items():
    print(clave, ":", valor)  # Salida: nombre : Juan, edad : 31, email : juan@example.com

existe_email = "email" in persona  # Verifica si la clave "email" existe en el diccionario
print("¿Existe email?:", existe_email)  # Salida: ¿Existe email?: True

# 10.2.4. Métodos de copia y concatenación
copia_persona = persona.copy()  # Crea una copia del diccionario
print("Copia del diccionario:", copia_persona)  # Salida: Copia del diccionario: {'nombre': 'Juan', 'edad': 31, 'email': 'juan@example.com'}