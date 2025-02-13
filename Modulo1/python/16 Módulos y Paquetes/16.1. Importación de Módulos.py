# Ejemplo de importación de un módulo estándar
import math

# Uso de una función del módulo math
print(math.sqrt(16))  # Salida: 4.0

# Importación de un módulo personalizado
import mi_modulo

# Uso de una función del módulo personalizado
mi_modulo.saludar("Juan")

# Importación de una función específica de un módulo
from math import sqrt

# Uso de la función sqrt directamente
print(sqrt(16))  # Salida: 4.0

# Importación con alias
import math as matematica

# Uso del alias
print(matematica.sqrt(16))  # Salida: 4.0