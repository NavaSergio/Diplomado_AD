# Ejemplo de generación de secuencias usando bucles `for` y `while`

# Generación de secuencia de números pares usando `for`
pares = []

for i in range(0, 10, 2):
    pares.append(i)  # Agrega cada número par a la lista pares

print("Secuencia de números pares:", pares)  # Salida: Secuencia de números pares: [0, 2, 4, 6, 8]

# Generación de secuencia de números impares usando `while`
impares = []
contador = 1

while contador < 10:
    impares.append(contador)  # Agrega cada número impar a la lista impares
    contador += 2  # Incrementa el contador en 2 en cada iteración

print("Secuencia de números impares:", impares)  # Salida: Secuencia de números impares: [1, 3, 5, 7, 9]