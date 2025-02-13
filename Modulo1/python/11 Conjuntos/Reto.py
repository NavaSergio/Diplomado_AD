# Reto: Crear dos conjuntos que representen los estudiantes de dos cursos diferentes y luego encontrar los estudiantes que están inscritos en ambos cursos.

# Solución:

# Paso 1: Crear dos conjuntos que representen los estudiantes de dos cursos diferentes
curso_python = {"Ana", "Juan", "María", "Pedro"}
curso_java = {"Juan", "María", "Luis", "Laura"}

# Paso 2: Encontrar los estudiantes que están inscritos en ambos cursos
estudiantes_ambos_cursos = curso_python & curso_java  # Intersección de conjuntos

# Paso 3: Mostrar los estudiantes que están inscritos en ambos cursos
print("Estudiantes inscritos en ambos cursos:", estudiantes_ambos_cursos)  # Salida: Estudiantes inscritos en ambos cursos: {'Juan', 'María'}