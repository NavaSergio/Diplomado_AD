# 11.3.1. Métodos de adición y eliminación
conjunto1.add(6)  # Añade un elemento al conjunto
print("Conjunto después de añadir 6:", conjunto1)  # Salida: Conjunto después de añadir 6: {1, 2, 3, 6}

conjunto1.remove(2)  # Elimina un elemento del conjunto
print("Conjunto después de eliminar 2:", conjunto1)  # Salida: Conjunto después de eliminar 2: {1, 3, 6}

# 11.3.2. Métodos de verificación
existe_elemento = 3 in conjunto1  # Verifica si un elemento existe en el conjunto
print("¿Existe el elemento 3?:", existe_elemento)  # Salida: ¿Existe el elemento 3?: True

# 11.3.3. Métodos de copia
copia_conjunto = conjunto1.copy()  # Crea una copia del conjunto
print("Copia del conjunto:", copia_conjunto)  # Salida: Copia del conjunto: {1, 3, 6}