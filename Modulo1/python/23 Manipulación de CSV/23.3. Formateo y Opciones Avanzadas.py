# 23.3.1. Especificación de delimitadores y comillas
# Uso de parámetros como delimiter, quotechar, quoting en csv.writer() y csv.reader()
datos = [
    ["nombre", "edad", "ciudad"],
    ["Juan", "30", "Madrid"],
    ["Ana", "25", "Barcelona"]
]

with open('datos_delimitados.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(datos)
    print("Datos con delimitadores y comillas escritos en archivo CSV")

# 23.3.2. Manejo de errores y excepciones
# Uso de try, except para manejar errores en la lectura y escritura de CSV
try:
    with open('datos.csv', 'r') as archivo:
        reader = csv.reader(archivo)
        for fila in reader:
            print(fila)
except FileNotFoundError:
    print("El archivo no existe")

# 23.3.3. Uso de dialectos
# Definición y uso de dialectos para personalizar el formato de CSV
class MiDialecto(csv.Dialect):
    delimiter = ';'
    quotechar = '"'
    doublequote = True
    skipinitialspace = True
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL

csv.register_dialect('mi_dialecto', MiDialecto)

with open('datos_dialecto.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo, dialect='mi_dialecto')
    writer.writerows(datos)
    print("Datos con dialecto escritos en archivo CSV")