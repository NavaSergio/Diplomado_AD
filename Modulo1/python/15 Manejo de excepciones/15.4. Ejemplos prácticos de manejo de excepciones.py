# 15.4.1. Ejemplo 1: Manejo de errores de entrada de usuario
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad > 0:
            print("Edad válida:", edad)
            break
        else:
            print("La edad debe ser un número positivo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# 15.4.2. Ejemplo 2: Manejo de errores en operaciones matemáticas
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")  # Salida: Error: No se puede dividir por cero.

# 15.4.3. Ejemplo 3: Manejo de errores en acceso a datos
try:
    diccionario = {"nombre": "Juan"}
    valor = diccionario["edad"]
except KeyError:
    print("Error: La clave 'edad' no existe en el diccionario.")  # Salida: Error: La clave 'edad' no existe en el diccionario.

# 15.4.4. Ejemplo 4: Uso de excepciones personalizadas
class ValorNegativoError(Exception):
    def __init__(self, mensaje="El valor no puede ser negativo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_valor(valor):
    if valor < 0:
        raise ValorNegativoError("El valor no puede ser negativo.")
    else:
        print("Valor válido:", valor)

try:
    validar_valor(-5)
except ValorNegativoError as e:
    print("Error:", e)  # Salida: Error: El valor no puede ser negativo.