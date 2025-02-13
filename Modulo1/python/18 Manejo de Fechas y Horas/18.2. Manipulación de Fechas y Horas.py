# 18.2.1. Suma y resta de fechas y horas
# Uso de timedelta para sumar y restar fechas y horas
from datetime import datetime, timedelta

fecha_actual = datetime.now()
un_dia = timedelta(days=1)
manana = fecha_actual + un_dia
ayer = fecha_actual - un_dia

print(f"Mañana: {manana}")
print(f"Ayer: {ayer}")

# 18.2.2. Comparación de fechas y horas
# Uso de operadores de comparación (<, >, ==, !=) para comparar fechas y horas
print(fecha_actual > ayer)  # Salida: True
print(fecha_actual < manana)  # Salida: True

# 18.2.3. Conversión entre zonas horarias
# Uso del módulo pytz para manejar zonas horarias
import pytz

utc = pytz.utc
fecha_utc = datetime.now(utc)
print(f"Fecha UTC: {fecha_utc}")

# 18.2.4. Cálculos con fechas y horas
# Cálculos de diferencias entre fechas y horas
diferencia = manana - fecha_actual
print(f"Diferencia en días: {diferencia.days}")  # Salida: 1