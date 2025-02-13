# Ejemplo de contador de ocurrencias usando un bucle `while`
numeros = [1, 2, 3, 2, 4, 2, 5]
contador = 0
indice = 0

while indice < len(numeros):
    if numeros[indice] == 2:
        contador += 1  # Incrementa el contador si el número es 2
    indice += 1  # Incrementa el índice en 1 en cada iteración

print("El número 2 aparece", contador, "veces.")  # Salida: El número 2 aparece 3 veces.