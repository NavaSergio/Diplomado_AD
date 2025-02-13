# 23.2.1. Lectura de CSV desde archivos
# Uso de csv.reader() para leer CSV desde archivos
with open('datos.csv', 'r') as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)

# 23.2.2. Escritura de CSV a archivos
# Uso de csv.writer() para escribir CSV a archivos
datos_nuevos = [
    ["Luis", "40", "Sevilla"],
    ["María", "28", "Bilbao"]
]

with open('datos_nuevos.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerows(datos_nuevos)
    print("Datos nuevos escritos en archivo CSV")

# 23.2.3. Lectura de CSV con encabezados
# Uso de csv.DictReader() para leer CSV con encabezados
with open('datos.csv', 'r') as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila)

# 23.2.4. Escritura de CSV con encabezados
# Uso de csv.DictWriter() para escribir CSV con encabezados
datos_dict = [
    {"nombre": "Elena", "edad": "32", "ciudad": "Zaragoza"},
    {"nombre": "Carlos", "edad": "27", "ciudad": "Málaga"}
]

with open('datos_dict.csv', 'w', newline='') as archivo:
    campos = ["nombre", "edad", "ciudad"]
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    writer.writerows(datos_dict)
    print("Datos con encabezados escritos en archivo CSV")