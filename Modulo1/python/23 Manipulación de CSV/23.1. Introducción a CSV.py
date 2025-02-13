# 23.1.1. Concepto de CSV
# Definición y usos de CSV (Comma-Separated Values): Es un formato de archivo para almacenar datos tabulares.
# Importancia de CSV en el intercambio de datos: Es ampliamente utilizado para importar y exportar datos.

# 23.1.2. Estructura básica de CSV
# Archivos CSV, filas, columnas y delimitadores
import csv

# Ejemplo de estructura básica de CSV
datos_csv = [
    ["nombre", "edad", "ciudad"],
    ["Juan", "30", "Madrid"],
    ["Ana", "25", "Barcelona"],
    ["Pedro", "35", "Valencia"]
]

# 23.1.3. Uso del módulo csv
# Introducción al módulo csv en Python
# Importación y uso básico del módulo csv

# Escribir datos en un archivo CSV
with open('datos.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerows(datos_csv)
    print("Datos escritos en archivo CSV")