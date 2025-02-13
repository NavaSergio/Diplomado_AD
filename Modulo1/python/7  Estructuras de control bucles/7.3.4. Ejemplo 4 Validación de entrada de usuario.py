# Ejemplo de validación de entrada de usuario usando un bucle `while`

while True:
    try:
        edad = int(input("Ingresa tu edad: "))  # Solicita al usuario que ingrese su edad
        if edad > 0:
            print("Tu edad es:", edad)  # Muestra la edad si es válida
            break  # Sale del bucle si la edad es válida
        else:
            print("La edad debe ser un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")