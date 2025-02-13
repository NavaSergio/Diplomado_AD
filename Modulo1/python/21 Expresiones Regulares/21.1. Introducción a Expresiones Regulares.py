# 21.1.1. Concepto de expresiones regulares
# Definición y usos de las expresiones regulares: Son patrones utilizados para buscar y manipular cadenas de texto.
# Importancia de las expresiones regulares en el procesamiento de texto: Permiten realizar búsquedas y manipulaciones complejas de texto.

# 21.1.2. Uso del módulo re
# Introducción al módulo re en Python: Proporciona funciones para trabajar con expresiones regulares.
import re

# 11.1.3. Patrones básicos
# Caracteres especiales y metacaracteres: ., ^, $, *, +, ?, {n}, {n,}, {n,m}, [], |, (), \
texto = "Hola mundo 123"
patron = r"\d+"  # Busca uno o más dígitos

# Uso de re.search() para buscar la primera coincidencia
coincidencia = re.search(patron, texto)
if coincidencia:
    print(f"Coincidencia encontrada: {coincidencia.group()}")  # Salida: Coincidencia encontrada: 123