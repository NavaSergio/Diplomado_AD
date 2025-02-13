# Los conjuntos son colecciones no ordenadas de elementos únicos.
# Se definen usando llaves `{}` o la función `set()`.

# 11.1.1. Introducción a los conjuntos
numeros = {1, 2, 3, 4, 5}
print("Conjunto de números:", numeros)  # Salida: Conjunto de números: {1, 2, 3, 4, 5}

# 11.1.2. Creación de conjuntos
conjunto_mixto = {1, "dos", 3.0, True}
print("Conjunto mixto:", conjunto_mixto)  # Salida: Conjunto mixto: {1, 'dos', 3.0}

# 11.1.3. Acceso a elementos de un conjunto
# Los conjuntos no permiten acceso directo a elementos por índice, pero se pueden iterar.
for elemento in numeros:
    print("Elemento:", elemento)  # Salida: Elemento: 1, Elemento: 2, Elemento: 3, Elemento: 4, Elemento: 5

# 11.1.4. Modificación de elementos de un conjunto
numeros.add(6)  # Añade un elemento al conjunto
print("Conjunto después de añadir 6:", numeros)  # Salida: Conjunto después de añadir 6: {1, 2, 3, 4, 5, 6}

numeros.remove(3)  # Elimina un elemento del conjunto
print("Conjunto después de eliminar 3:", numeros)  # Salida: Conjunto después de eliminar 3: {1, 2, 4, 5, 6}