# La sentencia `break` se utiliza para salir de un bucle `while` antes de que la condición sea falsa.
# La sentencia `continue` se utiliza para saltar a la siguiente iteración del bucle `while`.

# Ejemplo de uso de `break`
contador = 0

while True:
    print(contador)  # Este bloque se ejecuta indefinidamente
    contador += 1  # Incrementa el contador en 1 en cada iteración
    if contador == 5:
        break  # El bucle se detiene cuando contador es igual a 5

# Ejemplo de uso de `continue`
contador = 0

while contador < 10:
    contador += 1  # Incrementa el contador en 1 en cada iteración
    if contador % 2 == 0:
        continue  # Se salta la iteración si contador es par
    print(contador)  # Este bloque se ejecuta para cada número impar en el rango (1, 3, 5, 7, 9)