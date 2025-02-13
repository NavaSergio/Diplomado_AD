# Definición de un módulo personalizado (mi_modulo.py)
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Uso del módulo personalizado en otro script
import mi_modulo

# Llamada a la función del módulo personalizado
mi_modulo.saludar("Ana")  # Salida: Hola, Ana!

# Uso de if __name__ == "__main__":
if __name__ == "__main__":
    print("Este código solo se ejecuta si este archivo es el script principal.")