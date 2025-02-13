
# 10.3.1. Ejemplo 1: Almacenamiento de datos estructurados
libro = {
    "titulo": "1984",
    "autor": "George Orwell",
    "año": 1949,
    "genero": "Ciencia ficción"
}
print("Información del libro:", libro)  # Salida: Información del libro: {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949, 'genero': 'Ciencia ficción'}

# 10.3.2. Ejemplo 2: Conteo de ocurrencias
palabras = ["hola", "mundo", "hola", "python", "mundo"]
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Conteo de palabras:", conteo)  # Salida: Conteo de palabras: {'hola': 2, 'mundo': 2, 'python': 1}

# 10.3.3. Ejemplo 3: Búsqueda y filtrado de datos
estudiantes = {
    "Ana": 22,
    "Juan": 25,
    "María": 20,
    "Pedro": 23
}

estudiantes_mayores_de_22 = {nombre: edad for nombre, edad in estudiantes.items() if edad > 22}
print("Estudiantes mayores de 22 años:", estudiantes_mayores_de_22)  # Salida: Estudiantes mayores de 22 años: {'Juan': 25, 'Pedro': 23}

# 10.3.4. Ejemplo 4: Funciones que trabajan con diccionarios
def calcular_promedio_edades(estudiantes):
    total_edades = sum(estudiantes.values())
    promedio = total_edades / len(estudiantes)
    return promedio

promedio_edades = calcular_promedio_edades(estudiantes)
print("Promedio de edades:", promedio_edades)  # Salida: Promedio de edades: 22.5