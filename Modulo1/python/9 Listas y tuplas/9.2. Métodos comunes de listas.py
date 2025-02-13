# 9.2.1. Métodos de adición de elementos
frutas.append("banana")  # Añade "banana" al final de la lista
print("Lista después de append:", frutas)  # Salida: Lista después de append: ['manzana', 'naranja', 'cereza', 'banana']

frutas.insert(1, "uva")  # Inserta "uva" en la posición 1
print("Lista después de insert:", frutas)  # Salida: Lista después de insert: ['manzana', 'uva', 'naranja', 'cereza', 'banana']

# 9.2.2. Métodos de eliminación de elementos
frutas.remove("naranja")  # Elimina la primera ocurrencia de "naranja"
print("Lista después de remove:", frutas)  # Salida: Lista después de remove: ['manzana', 'uva', 'cereza', 'banana']

elemento_eliminado = frutas.pop(2)  # Elimina y devuelve el elemento en la posición 2
print("Elemento eliminado:", elemento_eliminado)  # Salida: Elemento eliminado: cereza
print("Lista después de pop:", frutas)  # Salida: Lista después de pop: ['manzana', 'uva', 'banana']

# 9.2.3. Métodos de ordenación y búsqueda
frutas.sort()  # Ordena la lista en orden alfabético
print("Lista ordenada:", frutas)  # Salida: Lista ordenada: ['banana', 'manzana', 'uva']

indice_uva = frutas.index("uva")  # Encuentra el índice de "uva"
print("Índice de 'uva':", indice_uva)  # Salida: Índice de 'uva': 2

# 9.2.4. Métodos de copia y concatenación
copia_frutas = frutas.copy()  # Crea una copia de la lista
print("Copia de la lista:", copia_frutas)  # Salida: Copia de la lista: ['banana', 'manzana', 'uva']

otras_frutas = ["piña", "mango"]
frutas_combinadas = frutas + otras_frutas  # Concatena dos listas
print("Listas combinadas:", frutas_combinadas)  # Salida: Listas combinadas: ['banana', 'manzana', 'uva', 'piña', 'mango']