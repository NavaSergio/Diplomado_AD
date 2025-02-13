# 21.2.1. Búsqueda de coincidencias
# Uso de re.search() para buscar la primera coincidencia
texto = "Hola mundo 123"
patron = r"\d+"  # Busca uno o más dígitos

coincidencia = re.search(patron, texto)
if coincidencia:
    print(f"Coincidencia encontrada: {coincidencia.group()}")  # Salida: Coincidencia encontrada: 123

# 21.2.2. Búsqueda de todas las coincidencias
# Uso de re.findall() para buscar todas las coincidencias
texto = "Hola mundo 123 y 456"
patron = r"\d+"  # Busca uno o más dígitos

coincidencias = re.findall(patron, texto)
print(f"Todas las coincidencias: {coincidencias}")  # Salida: Todas las coincidencias: ['123', '456']

# 21.2.3. Sustitución de coincidencias
# Uso de re.sub() para sustituir coincidencias
texto = "Hola mundo 123"
patron = r"\d+"  # Busca uno o más dígitos

texto_sustituido = re.sub(patron, "###", texto)
print(f"Texto sustituido: {texto_sustituido}")  # Salida: Texto sustituido: Hola mundo ###

# 21.2.4. División de cadenas
# Uso de re.split() para dividir cadenas basadas en patrones
texto = "Hola mundo 123"
patron = r"\s"  # Busca espacios en blanco

partes = re.split(patron, texto)
print(f"Partes divididas: {partes}")  # Salida: Partes divididas: ['Hola', 'mundo', '123']