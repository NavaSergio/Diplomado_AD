# Las listas son colecciones ordenadas y mutables de elementos.
# Se definen usando corchetes `[]` y los elementos se separan por comas.

# 9.1.1. Introducción a las listas
frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:", frutas)  # Salida: Lista de frutas: ['manzana', 'banana', 'cereza']

# 9.1.2. Creación de listas
lista_mixta = [1, "dos", 3.0, True]
print("Lista mixta:", lista_mixta)  # Salida: Lista mixta: [1, 'dos', 3.0, True]

# 9.1.3. Acceso a elementos de una lista
primer_elemento = frutas[0]
print("Primer elemento:", primer_elemento)  # Salida: Primer elemento: manzana

# 9.1.4. Modificación de elementos de una lista
frutas[1] = "naranja"
print("Lista modificada:", frutas)  # Salida: Lista modificada: ['manzana', 'naranja', 'cereza']