# Estructura básica de un paquete: __init__.py y submódulos
# Crear un paquete llamado 'mi_paquete' con un submódulo 'submodulo.py'

# submodulo.py
def funcion_submodulo():
    print("Función del submódulo")

# __init__.py (puede estar vacío o contener inicializaciones)

# Uso del paquete y submódulo en otro script
from mi_paquete.submodulo import funcion_submodulo

# Llamada a la función del submódulo
funcion_submodulo()  # Salida: Función del submódulo