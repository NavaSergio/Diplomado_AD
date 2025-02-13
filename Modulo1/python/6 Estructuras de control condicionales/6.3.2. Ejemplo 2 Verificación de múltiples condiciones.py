# Ejemplo de verificación de múltiples condiciones
edad = 25
es_estudiante = False

if edad >= 18 and not es_estudiante:
    print("Eres mayor de edad y no eres estudiante.")  # Este bloque se ejecuta
elif edad >= 18 and es_estudiante:
    print("Eres mayor de edad y estudiante.")
else:
    print("Eres menor de edad.")