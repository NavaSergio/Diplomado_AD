# Si una función no tiene una sentencia `return`, devuelve `None` implícitamente.

# Ejemplo de función sin retorno
def saludar(nombre):
    print("Hola,", nombre)

# Llamada a la función y almacenamiento del resultado
resultado = saludar("Pedro")  # Salida: Hola, Pedro
print(resultado)  # Salida: None