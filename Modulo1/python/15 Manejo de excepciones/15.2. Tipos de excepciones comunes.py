# Python tiene varios tipos de excepciones predefinidas que se pueden manejar.

# 15.2.1. Excepciones de valor (`ValueError`)
# Se genera cuando una función recibe un argumento de tipo correcto pero valor inapropiado.
try:
    valor = int("abc")  # Esto generará una excepción ValueError
except ValueError:
    print("Error: No se puede convertir 'abc' a un número entero.")  # Salida: Error: No se puede convertir 'abc' a un número entero.

# 15.2.2. Excepciones de índice (`IndexError`)
# Se genera cuando se intenta acceder a un índice fuera de rango en una secuencia.
try:
    lista = [1, 2, 3]
    valor = lista[5]  # Esto generará una excepción IndexError
except IndexError:
    print("Error: Índice fuera de rango.")  # Salida: Error: Índice fuera de rango.

# 15.2.3. Excepciones de clave (`KeyError`)
# Se genera cuando se intenta acceder a una clave que no existe en un diccionario.
try:
    diccionario = {"nombre": "Juan"}
    valor = diccionario["edad"]  # Esto generará una excepción KeyError
except KeyError:
    print("Error: La clave 'edad' no existe en el diccionario.")  # Salida: Error: La clave 'edad' no existe en el diccionario.

# 15.2.4. Excepciones de archivo (`FileNotFoundError`, `PermissionError`)
# Se generan cuando se intenta acceder a un archivo que no existe o no se tienen permisos.
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")  # Salida: Error: El archivo no existe.
except PermissionError:
    print("Error: No tienes permisos para acceder al archivo.")