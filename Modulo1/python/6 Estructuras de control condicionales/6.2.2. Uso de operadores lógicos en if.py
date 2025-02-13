# Los operadores lógicos (`and`, `or`, `not`) se utilizan para combinar múltiples condiciones.

# Ejemplo de uso de operadores lógicos en `if`
a = 5
b = 10
c = 15

if a < b and b < c:
    print("a es menor que b y b es menor que c.")  # Este bloque se ejecuta

if a < b or b > c:
    print("a es menor que b o b es mayor que c.")  # Este bloque se ejecuta

if not a > b:
    print("a no es mayor que b.")  # Este bloque se ejecuta