# 11.2.1. Unión de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2  # Unión de conjuntos
print("Unión de conjuntos:", union)  # Salida: Unión de conjuntos: {1, 2, 3, 4, 5}

# 11.2.2. Intersección de conjuntos
interseccion = conjunto1 & conjunto2  # Intersección de conjuntos
print("Intersección de conjuntos:", interseccion)  # Salida: Intersección de conjuntos: {3}

# 11.2.3. Diferencia de conjuntos
diferencia = conjunto1 - conjunto2  # Diferencia de conjuntos
print("Diferencia de conjuntos:", diferencia)  # Salida: Diferencia de conjuntos: {1, 2}

# 11.2.4. Diferencia simétrica de conjuntos
diferencia_simetrica = conjunto1 ^ conjunto2  # Diferencia simétrica de conjuntos
print("Diferencia simétrica de conjuntos:", diferencia_simetrica)  # Salida: Diferencia simétrica de conjuntos: {1, 2, 4, 5}