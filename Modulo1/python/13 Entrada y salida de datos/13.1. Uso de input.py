# La función `input()` se utiliza para capturar datos ingresados por el usuario desde la consola.

# 13.1.1. Introducción a `input()`
nombre = input("Ingresa tu nombre: ")  # Captura el nombre ingresado por el usuario
print("Hola,", nombre)  # Salida: Hola, [nombre ingresado]

# 13.1.2. Sintaxis básica de `input()`
edad = input("Ingresa tu edad: ")  # Captura la edad ingresada por el usuario
print("Tienes", edad, "años.")  # Salida: Tienes [edad ingresada] años.

# 13.1.3. Conversión de tipos de datos
# La entrada capturada con `input()` es siempre una cadena, por lo que a veces es necesario convertirla a otro tipo de dato.
edad_int = int(edad)  # Convierte la cadena de edad a un entero
print("En 10 años tendrás", edad_int + 10, "años.")  # Salida: En 10 años tendrás [edad ingresada + 10] años.

# 13.1.4. Validación de entrada de usuario
# Es importante validar la entrada del usuario para evitar errores.
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad > 0:
            print("Edad válida:", edad)
            break
        else:
            print("La edad debe ser un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")