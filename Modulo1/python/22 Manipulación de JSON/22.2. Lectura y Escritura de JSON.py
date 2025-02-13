# 22.2.1. Lectura de JSON desde cadenas
# Uso de json.loads() para leer JSON desde cadenas
json_string = '{"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}'
datos = json.loads(json_string)
print(f"Datos leídos: {datos}")

# 22.2.2. Escritura de JSON a cadenas
# Uso de json.dumps() para escribir JSON a cadenas
datos = {"nombre": "Pedro", "edad": 35, "ciudad": "Valencia"}
json_string = json.dumps(datos)
print(f"JSON escrito: {json_string}")

# 22.2.3. Lectura de JSON desde archivos
# Uso de json.load() para leer JSON desde archivos
with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)
    print(f"Datos leídos desde archivo: {datos}")

# 22.2.4. Escritura de JSON a archivos
# Uso de json.dump() para escribir JSON a archivos
datos = {"nombre": "Luis", "edad": 40, "ciudad": "Sevilla"}
with open('datos_nuevo.json', 'w') as archivo:
    json.dump(datos, archivo)
    print("Datos escritos en archivo")