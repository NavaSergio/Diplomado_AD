# 22.1.1. Concepto de JSON
# Definición y usos de JSON (JavaScript Object Notation): Es un formato ligero de intercambio de datos.
# Importancia de JSON en el intercambio de datos: Es ampliamente utilizado en APIs y almacenamiento de datos.

# 22.1.2. Estructura básica de JSON
# Objetos JSON, arrays, valores y tipos de datos
import json

# Ejemplo de estructura básica de JSON
datos_json = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["leer", "correr", "viajar"]
}

# 22.1.3. Uso del módulo json
# Introducción al módulo json en Python
# Importación y uso básico del módulo json

# Convertir un diccionario a JSON
json_string = json.dumps(datos_json)
print(f"JSON: {json_string}")