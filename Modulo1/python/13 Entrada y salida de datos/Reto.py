# Reto: Crear un programa que simule un juego de adivinanzas. El programa debe generar un número aleatorio
# entre 1 y 100, y el usuario debe adivinar el número. El programa debe proporcionar pistas al usuario
# indicando si el número a adivinar es mayor o menor que el número ingresado.

# Solución:

# Paso 1: Importar el módulo `random` para generar números aleatorios
import random

# Paso 2: Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Paso 3: Iniciar el juego
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")

# Paso 4: Bucle para que el usuario adivine el número
while True:
    try:
        intento = int(input("Ingresa tu adivinanza: "))
        if intento < 1 or intento > 100:
            print("Por favor, ingresa un número entre 1 y 100.")
        elif intento < numero_secreto:
            print("El número secreto es mayor.")
        elif intento > numero_secreto:
            print("El número secreto es menor.")
        else:
            print("¡Felicidades! Adivinaste el número secreto.")
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Solución:
# El programa genera un número aleatorio entre 1 y 100 y pide al usuario que adivine el número.
# Si el número ingresado es menor que el número secreto, el programa indica que el número secreto es mayor.
# Si el número ingresado es mayor que el número secreto, el programa indica que el número secreto es menor.
# El juego continúa hasta que el usuario adivina el número secreto.