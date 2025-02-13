# 19.2.1. Introducción a las funciones anidadas
# Concepto de funciones anidadas en Python: Son funciones definidas dentro de otras funciones.
# Ventajas de usar funciones anidadas: Encapsulamiento y reutilización de código.

# 19.2.2. Definición de funciones anidadas
# Sintaxis básica para definir funciones anidadas
def funcion_externa():
    def funcion_interna():
        return "Hola desde la función interna"
    return funcion_interna()

print(funcion_externa())  # Salida: Hola desde la función interna

# 19.2.3. Acceso a variables de la función externa
# Uso de variables de la función externa dentro de la función anidada
def funcion_externa(mensaje):
    def funcion_interna():
        return f"Mensaje: {mensaje}"
    return funcion_interna()

print(funcion_externa("Hola"))  # Salida: Mensaje: Hola

# 19.2.4. Funciones anidadas en práctica
# Ejemplos de uso práctico de funciones anidadas
def calcular_potencia(base):
    def potencia(exponente):
        return base ** exponente
    return potencia

cuadrado = calcular_potencia(2)
cubo = calcular_potencia(3)

print(cuadrado(3))  # Salida: 8
print(cubo(2))  # Salida: 9