# 21.3.1. Cuantificadores
# Uso de cuantificadores como *, +, ?, {n}, {n,}, {n,m}
texto = "abc aabc aaabc"
patron = r"a{2,3}"  # Busca 'a' repetido de 2 a 3 veces

coincidencias = re.findall(patron, texto)
print(f"Coincidencias con cuantificadores: {coincidencias}")  # Salida: Coincidencias con cuantificadores: ['aa', 'aaa']

# 21.3.2. Agrupaciones y referencias
# Uso de paréntesis para agrupar patrones
# Uso de referencias hacia atrás (\1, \2, etc.)
texto = "abc abc abc"
patron = r"(\w+) \1"  # Busca palabras repetidas

coincidencias = re.findall(patron, texto)
print(f"Coincidencias con agrupaciones: {coincidencias}")  # Salida: Coincidencias con agrupaciones: ['abc']

# 21.3.3. Clases de caracteres
# Uso de clases de caracteres como [abc], [^abc], [a-z], [0-9]
texto = "abc 123"
patron = r"[a-z]+"  # Busca una o más letras minúsculas

coincidencias = re.findall(patron, texto)
print(f"Coincidencias con clases de caracteres: {coincidencias}")  # Salida: Coincidencias con clases de caracteres: ['abc']

# 21.3.4. Anclas y límites
# Uso de anclas como ^, $
# Uso de límites como \b, \B
texto = "abc abc"
patron = r"^\w+"  # Busca una palabra al inicio del texto

coincidencia = re.search(patron, texto)
if coincidencia:
    print(f"Coincidencia con anclas: {coincidencia.group()}")  # Salida: Coincidencia con anclas: abc