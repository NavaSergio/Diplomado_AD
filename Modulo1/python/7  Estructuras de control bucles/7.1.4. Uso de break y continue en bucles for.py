# La sentencia `break` se utiliza para salir de un bucle antes de que termine.
# La sentencia `continue` se utiliza para saltar a la siguiente iteración del bucle.

# Ejemplo de uso de `break`
for i in range(10):
    if i == 5:
        break  # El bucle se detiene cuando i es igual a 5
    print(i)  # Este bloque se ejecuta para cada número en el rango (0, 1, 2, 3, 4)

# Ejemplo de uso de `continue`
for i in range(10):
    if i % 2 == 0:
        continue  # Se salta la iteración si i es par
    print(i)  # Este bloque se ejecuta para cada número impar en el rango (1, 3, 5, 7, 9)