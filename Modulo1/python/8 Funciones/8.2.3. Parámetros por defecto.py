# Los parámetros por defecto tienen un valor predeterminado que se usa si no se proporciona un argumento.

# Ejemplo de parámetros por defecto
def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

# Llamada a la función sin proporcionar el parámetro por defecto
saludar("Juan")  # Salida: Hola Juan

# Llamada a la función proporcionando el parámetro por defecto
saludar("Ana", "Buenos días")  # Salida: Buenos días Ana