# 11.4.1. Ejemplo 1: Eliminación de duplicados
numeros_duplicados = [1, 2, 2, 3, 4, 4, 5]
numeros_unicos = list(set(numeros_duplicados))  # Convierte la lista a conjunto y luego de nuevo a lista
print("Números únicos:", numeros_unicos)  # Salida: Números únicos: [1, 2, 3, 4, 5]

# 11.4.2. Ejemplo 2: Verificación de membresía
vocales = {'a', 'e', 'i', 'o', 'u'}
letra = 'e'
es_vocal = letra in vocales
print(f"¿'{letra}' es una vocal?:", es_vocal)  # Salida: ¿'e' es una vocal?: True

# 11.4.3. Ejemplo 3: Operaciones de conjuntos en datos
estudiantes_python = {"Ana", "Juan", "María"}
estudiantes_java = {"Juan", "Pedro", "María"}
estudiantes_ambos_cursos = estudiantes_python & estudiantes_java  # Intersección de conjuntos
print("Estudiantes inscritos en ambos cursos:", estudiantes_ambos_cursos)  # Salida: Estudiantes inscritos en ambos cursos: {'Juan', 'María'}

# 11.4.4. Ejemplo 4: Funciones que trabajan con conjuntos
def contar_elementos_unicos(lista):
    return len(set(lista))

lista_numeros = [1, 2, 2, 3, 4, 4, 5]
cantidad_unicos = contar_elementos_unicos(lista_numeros)
print("Cantidad de elementos únicos:", cantidad_unicos)  # Salida: Cantidad de elementos únicos: 5