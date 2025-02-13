# 29.2.1. Introducción a Tkinter
# Definición y características de Tkinter: Es una biblioteca estándar de Python para crear interfaces gráficas.
# Ventajas de usar Tkinter para desarrollo de GUI: Fácil de usar y viene preinstalado con Python.

# 29.2.2. Creación de una ventana básica
# Uso de Tk para crear una ventana principal
# Ejemplos de creación de una ventana básica
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Aplicación")
ventana.geometry("300x200")

# 29.2.3. Componentes básicos de Tkinter
# Uso de botones, etiquetas, cuadros de texto, listas desplegables, etc.
# Ejemplos de uso de componentes básicos
etiqueta = tk.Label(ventana, text="Hola, Tkinter!")
etiqueta.pack()

boton = tk.Button(ventana, text="Haz clic")
boton.pack()

cuadro_texto = tk.Entry(ventana)
cuadro_texto.pack()

lista_desplegable = tk.Listbox(ventana)
lista_desplegable.insert(1, "Opción 1")
lista_desplegable.insert(2, "Opción 2")
lista_desplegable.pack()

# 29.2.4. Manejo de eventos
# Uso de bind y command para manejar eventos de usuario
# Ejemplos de manejo de eventos
def on_click():
    etiqueta.config(text="Botón clickeado")

boton.config(command=on_click)

ventana.mainloop()