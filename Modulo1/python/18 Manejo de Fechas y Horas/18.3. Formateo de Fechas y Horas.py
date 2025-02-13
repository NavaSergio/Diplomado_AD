# 18.3.1. Formateo de fechas y horas con strftime
# Uso de strftime para formatear fechas y horas como cadenas
from datetime import datetime

fecha_actual = datetime.now()
fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
print(f"Fecha formateada: {fecha_formateada}")

# 18.3.2. Parseo de cadenas a fechas y horas con strptime
# Uso de strptime para convertir cadenas en objetos de fecha y hora
cadena_fecha = "2023-10-05 14:30:00"
fecha_parseada = datetime.strptime(cadena_fecha, "%Y-%m-%d %H:%M:%S")
print(f"Fecha parseada: {fecha_parseada}")

# 18.3.3. Formateo automático con isoformat
# Uso de isoformat para formatear fechas y horas en formato ISO
fecha_iso = fecha_actual.isoformat()
print(f"Fecha ISO: {fecha_iso}")

# 18.3.4. Formateo personalizado
# Uso de especificadores de formato personalizados
fecha_personalizada = fecha_actual.strftime("Hoy es %A, %d de %B de %Y")
print(f"Fecha personalizada: {fecha_personalizada}")