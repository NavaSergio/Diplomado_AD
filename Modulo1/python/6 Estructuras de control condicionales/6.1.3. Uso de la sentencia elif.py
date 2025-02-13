# La sentencia `elif` se utiliza para evaluar múltiples condiciones en secuencia.
# Solo se ejecuta el bloque de código correspondiente a la primera condición verdadera.

# Ejemplo de uso de `elif`
numero = 7

if numero > 10:
    print(numero, "es mayor que 10.")
elif numero > 5:
    print(numero, "es mayor que 5 pero menor o igual que 10.")  # Este bloque se ejecuta
else:
    print(numero, "es menor o igual que 5.")