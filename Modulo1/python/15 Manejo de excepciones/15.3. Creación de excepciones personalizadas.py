# Se pueden crear excepciones personalizadas heredando de la clase `Exception`.

# 15.3.1. Introducción a las excepciones personalizadas
# Las excepciones personalizadas permiten manejar errores específicos de una aplicación.

# 15.3.2. Creación de excepciones personalizadas
class ValorNegativoError(Exception):
    def __init__(self, mensaje="El valor no puede ser negativo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# 15.3.3. Uso de excepciones personalizadas
def validar_valor(valor):
    if valor < 0:
        raise ValorNegativoError("El valor no puede ser negativo.")
    else:
        print("Valor válido:", valor)

try:
    validar_valor(-5)  # Esto generará una excepción ValorNegativoError
except ValorNegativoError as e:
    print("Error:", e)  # Salida: Error: El valor no puede ser negativo.