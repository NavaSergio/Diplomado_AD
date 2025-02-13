# La sentencia `else` se utiliza para ejecutar un bloque de código si ninguna de las condiciones anteriores es verdadera.

# Ejemplo de uso de `else`
numero = 3

if numero > 10:
    print(numero, "es mayor que 10.")
elif numero > 5:
    print(numero, "es mayor que 5 pero menor o igual que 10.")
else:
    print(numero, "es menor o igual que 5.")  # Este bloque se ejecuta