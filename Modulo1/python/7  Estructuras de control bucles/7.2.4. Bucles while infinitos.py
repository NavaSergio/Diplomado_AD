# Es posible crear bucles `while` infinitos si la condición siempre es verdadera.
# Se debe tener cuidado al usar bucles infinitos para evitar bucles sin fin.

# Ejemplo de bucle `while` infinito
contador = 0

while True:
    print("Este bucle es infinito.")  # Este bloque se ejecuta indefinidamente
    contador += 1  # Incrementa el contador en 1 en cada iteración
    if contador == 5:
        break  # El bucle se detiene cuando contador es igual a 5