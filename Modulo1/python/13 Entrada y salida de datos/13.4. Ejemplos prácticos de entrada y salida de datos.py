# 13.4.1. Ejemplo 1: Interacción básica con el usuario
nombre = input("Ingresa tu nombre: ")
print("Hola,", nombre)  # Salida: Hola, [nombre ingresado]

# 13.4.2. Ejemplo 2: Validación de entrada de usuario
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

# 13.4.3. Ejemplo 3: Formateo de salida de datos
nombre = "María"
edad = 28
print("Nombre: {}, Edad: {}".format(nombre, edad))  # Salida: Nombre: María, Edad: 28

# 13.4.4. Ejemplo 4: Funciones que trabajan con entrada y salida
def saludar(nombre):
    print("Hola,", nombre)

nombre = input("Ingresa tu nombre: ")
saludar(nombre)  # Salida: Hola, [nombre ingresado]