# Reto: Crear una función que lea un archivo CSV, procese los datos y escriba los resultados en un nuevo archivo CSV.
# La función debe manejar excepciones para casos como archivos inexistentes, permisos insuficientes y errores de formato CSV.

# Solución:

# Paso 1: Importar el módulo `csv` para manejar archivos CSV
import csv

# Paso 2: Crear una función para procesar el archivo CSV
def procesar_csv(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, "r") as entrada:
            lector_csv = csv.reader(entrada)
            datos = list(lector_csv)

            # Procesar los datos (por ejemplo, convertir a mayúsculas)
            datos_procesados = [[valor.upper() for valor in fila] for fila in datos]

            with open(archivo_salida, "w", newline="") as salida:
                escritor_csv = csv.writer(salida)
                escritor_csv.writerows(datos_procesados)

            print("Proceso completado. Resultados escritos en", archivo_salida)

    except FileNotFoundError:
        print("Error: El archivo de entrada no existe.")
    except PermissionError:
        print("Error: No tienes permisos para acceder al archivo de entrada.")
    except csv.Error as e:
        print("Error de formato CSV:", e)

# Paso 3: Probar la función con un archivo CSV
archivo_entrada = "datos.csv"
archivo_salida = "datos_procesados.csv"

procesar_csv(archivo_entrada, archivo_salida)

# Solución:
# La función `procesar_csv` lee un archivo CSV, procesa los datos (en este caso, convirtiendo a mayúsculas)
# y escribe los resultados en un nuevo archivo CSV. La función maneja excepciones para casos como archivos
# inexistentes, permisos insuficientes y errores de formato CSV.