# Los diccionarios son colecciones no ordenadas de pares clave-valor.
# Se definen usando llaves `{}` y los pares clave-valor se separan por comas.

# 10.1.1. Introducción a los diccionarios
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("Diccionario de persona:", persona)  # Salida: Diccionario de persona: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# 10.1.2. Creación de diccionarios
estudiante = dict(nombre="Ana", edad=22, carrera="Ingeniería")
print("Diccionario de estudiante:", estudiante)  # Salida: Diccionario de estudiante: {'nombre': 'Ana', 'edad': 22, 'carrera': 'Ingeniería'}

# 10.1.3. Acceso a elementos de un diccionario
nombre = persona["nombre"]
print("Nombre de la persona:", nombre)  # Salida: Nombre de la persona: Juan

# 10.1.4. Modificación de elementos de un diccionario
persona["edad"] = 31
print("Diccionario modificado:", persona)  # Salida: Diccionario modificado: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid'}