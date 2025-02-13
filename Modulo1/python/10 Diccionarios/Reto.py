# Reto: Crear un diccionario que almacene la información de varios libros y luego buscar y mostrar los títulos de los libros escritos por un autor específico.

# Solución:

# Paso 1: Crear un diccionario que almacene la información de varios libros
libros = {
    "1984": {"autor": "George Orwell", "año": 1949, "genero": "Ciencia ficción"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "genero": "Realismo mágico"},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "genero": "Literatura infantil"},
    "1984": {"autor": "George Orwell", "año": 1949, "genero": "Ciencia ficción"}
}

# Paso 2: Función para buscar y mostrar los títulos de los libros escritos por un autor específico
def buscar_libros_por_autor(libros, autor):
    titulos = []
    for titulo, info in libros.items():
        if info["autor"] == autor:
            titulos.append(titulo)
    return titulos

# Paso 3: Llamar a la función con un autor específico
autor_buscado = "George Orwell"
titulos_encontrados = buscar_libros_por_autor(libros, autor_buscado)

# Paso 4: Mostrar los títulos encontrados
print(f"Libros escritos por {autor_buscado}: {titulos_encontrados}")  # Salida: Libros escritos por George Orwell: ['1984', '1984']