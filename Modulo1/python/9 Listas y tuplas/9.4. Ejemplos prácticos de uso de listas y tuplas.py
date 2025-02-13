# 9.4.1. Ejemplo 1: Manipulación de datos en listas
numeros = [5, 3, 8, 1, 2]
numeros.sort()  # Ordena la lista de números
print("Lista ordenada:", numeros)  # Salida: Lista ordenada: [1, 2, 3, 5, 8]

# 9.4.2. Ejemplo 2: Uso de tuplas para datos inmutables
punto = (3, 4)
print("Coordenadas del punto:", punto)  # Salida: Coordenadas del punto: (3, 4)

# 9.4.3. Ejemplo 3: Iteración sobre listas y tuplas
nombres = ["Ana", "Juan", "María"]
for nombre in nombres:
    print("Nombre:", nombre)  # Salida: Nombre: Ana, Nombre: Juan, Nombre: María

# 9.4.4. Ejemplo 4: Funciones que trabajan con listas y tuplas
def calcular_area(base, altura):
    return base * altura

dimensiones = (10, 5)
area = calcular_area(*dimensiones)  # Desempaqueta la tupla para pasar los argumentos
print("Área del rectángulo:", area)  # Salida: Área del rectángulo: 50