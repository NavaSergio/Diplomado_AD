# Las tuplas son colecciones ordenadas e inmutables de elementos.
# Se definen usando paréntesis `()` y los elementos se separan por comas.

# 9.3.1. Introducción a las tuplas
coordenadas = (10, 20)
print("Tupla de coordenadas:", coordenadas)  # Salida: Tupla de coordenadas: (10, 20)

# 9.3.2. Creación de tuplas
tupla_mixta = (1, "dos", 3.0, True)
print("Tupla mixta:", tupla_mixta)  # Salida: Tupla mixta: (1, 'dos', 3.0, True)

# 9.3.3. Acceso a elementos de una tupla
primer_elemento = coordenadas[0]
print("Primer elemento:", primer_elemento)  # Salida: Primer elemento: 10

# 9.3.4. Métodos comunes de tuplas
indice_dos = tupla_mixta.index("dos")  # Encuentra el índice de "dos"
print("Índice de 'dos':", indice_dos)  # Salida: Índice de 'dos': 1

conteo_tres = tupla_mixta.count(3.0)  # Cuenta cuántas veces aparece 3.0 en la tupla
print("Conteo de 3.0:", conteo_tres)  # Salida: Conteo de 3.0: 1