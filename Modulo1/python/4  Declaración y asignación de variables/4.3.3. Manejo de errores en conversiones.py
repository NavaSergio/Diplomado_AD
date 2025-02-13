# En algunas conversiones, pueden ocurrir errores si el valor no se puede convertir correctamente.

# Ejemplo de error en conversión
try:
    numero_str = "abc"
    numero_int = int(numero_str)  # Esto generará un error porque "abc" no es un número válido
except ValueError:
    print("Error: No se puede convertir 'abc' a un número entero.")

# Ejemplo de conversión correcta
try:
    numero_str = "123"
    numero_int = int(numero_str)  # Esto funcionará correctamente
    print("Conversión exitosa:", numero_int)
except ValueError:
    print("Error: No se puede convertir a un número entero.")