# Reto: Crear una función que encripte un mensaje usando el cifrado César con un desplazamiento dado.
# El cifrado César es un tipo de cifrado por sustitución en el que cada letra del texto original
# se desplaza un número fijo de posiciones hacia adelante en el alfabeto.

# Solución:

# Paso 1: Crear la función de cifrado César
def cifrado_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():  # Verifica si el caracter es una letra
            mayuscula = caracter.isupper()  # Verifica si el caracter es mayúscula
            caracter = caracter.lower()  # Convierte a minúscula para facilitar el cifrado
            nuevo_caracter = chr((ord(caracter) - ord('a') + desplazamiento) % 26 + ord('a'))
            if mayuscula:
                nuevo_caracter = nuevo_caracter.upper()  # Convierte de nuevo a mayúscula si era mayúscula
            mensaje_cifrado += nuevo_caracter
        else:
            mensaje_cifrado += caracter  # Mantiene caracteres no alfabéticos sin cambios
    return mensaje_cifrado

# Paso 2: Probar la función con un mensaje y un desplazamiento
mensaje = "Hola, mundo!"
desplazamiento = 3
mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)

# Paso 3: Mostrar el mensaje cifrado
print("Mensaje cifrado:", mensaje_cifrado)  # Salida: Mensaje cifrado: Krnc, pxqgr!

# Solución:
# La función `cifrado_cesar` toma un mensaje y un desplazamiento como argumentos.
# Itera sobre cada caracter del mensaje y, si es una letra, lo cifra desplazándolo
# en el alfabeto según el desplazamiento dado. Los caracteres no alfabéticos se mantienen sin cambios.
# Finalmente, devuelve el mensaje cifrado.