# 18.1.1. Introducción al módulo datetime
# Concepto de fechas y horas en programación: El manejo de fechas y horas es crucial en muchas aplicaciones.
# Importancia del módulo datetime en Python: Proporciona clases para manipular fechas y horas.

# 18.1.2. Clases principales del módulo datetime
# datetime.date, datetime.time, datetime.datetime, datetime.timedelta
from datetime import date, time, datetime, timedelta

# 18.1.3. Creación de objetos de fecha y hora
# Creación de objetos date, time, datetime
fecha = date(2023, 10, 5)
hora = time(14, 30, 0)
fecha_hora = datetime(2023, 10, 5, 14, 30, 0)

# 18.1.4. Acceso a atributos de fecha y hora
# Acceso a año, mes, día, hora, minuto, segundo, microsegundo
print(fecha.year)  # Salida: 2023
print(hora.minute)  # Salida: 30
print(fecha_hora.second)  # Salida: 0