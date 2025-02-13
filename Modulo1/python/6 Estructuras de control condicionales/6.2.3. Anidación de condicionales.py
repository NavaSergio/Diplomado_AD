# Es posible anidar condicionales dentro de otros condicionales para evaluar múltiples condiciones.

# Ejemplo de anidación de condicionales
edad = 20
es_estudiante = True

if edad >= 18:
    if es_estudiante:
        print("Eres mayor de edad y estudiante.")  # Este bloque se ejecuta
    else:
        print("Eres mayor de edad pero no eres estudiante.")
else:
    print("Eres menor de edad.")