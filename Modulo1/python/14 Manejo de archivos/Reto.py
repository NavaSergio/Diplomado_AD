# Reto: Crear un programa que lea un archivo de texto, cuente la frecuencia de cada palabra y escriba los resultados en un nuevo archivo.

# Solución:

# Paso 1: Crear una función para contar la frecuencia de las palabras
def contar_frecuencia_palabras(archivo):
    frecuencia = {}
    with open(archivo, "r") as file:
        texto = file.read()
        palabras = texto.split()
        for palabra in palabras:
            palabra = palabra.strip(".,!?()[]{}\"'").lower()  # Limpia la palabra de signos de puntuación y convierte a minúsculas
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
    return frecuencia

# Paso 2: Crear una función para escribir los resultados en un archivo
def escribir_resultados(frecuencia, archivo_salida):
    with open(archivo_salida, "w") as file:
        for palabra, count in frecuencia.items():
            file.write(f"{palabra}: {count}\n")

# Paso 3: Probar las funciones con un archivo de texto
archivo_entrada = "texto.txt"
archivo_salida = "frecuencia_palabras.txt"

frecuencia = contar_frecuencia_palabras(archivo_entrada)
escribir_resultados(frecuencia, archivo_salida)

# Solución:
# La función `contar_frecuencia_palabras` lee un archivo de texto, divide el contenido en palabras,
# limpia las palabras de signos de puntuación y convierte a minúsculas, y cuenta la frecuencia de cada palabra.
# La función `escribir_resultados` escribe los resultados en un nuevo archivo.