# Los parámetros posicionales se pasan en el orden en que se definen en la función.
# Los parámetros por nombre se pasan usando el nombre del parámetro.

# Ejemplo de parámetros posicionales
def saludar(nombre, edad):
    print("Hola,", nombre, "tienes", edad, "años.")

# Llamada a la función con parámetros posicionales
saludar("Pedro", 25)  # Salida: Hola, Pedro tienes 25 años.

# Ejemplo de parámetros por nombre
def saludar(nombre, edad):
    print("Hola,", nombre, "tienes", edad, "años.")

# Llamada a la función con parámetros por nombre
saludar(edad=30, nombre="María")  # Salida: Hola, María tienes 30 años.