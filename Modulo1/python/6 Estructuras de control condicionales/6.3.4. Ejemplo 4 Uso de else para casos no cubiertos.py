# Ejemplo de uso de `else` para casos no cubiertos
dia_semana = "Lunes"

if dia_semana == "Lunes":
    print("Hoy es lunes.")  # Este bloque se ejecuta
elif dia_semana == "Martes":
    print("Hoy es martes.")
elif dia_semana == "Miércoles":
    print("Hoy es miércoles.")
else:
    print("Hoy no es lunes, martes ni miércoles.")  # Este bloque se ejecuta si ninguna condición anterior es verdadera