# 29.3.1. Uso de geometría de rejilla (grid)
# Uso de grid para organizar componentes en una rejilla
# Ejemplos de uso de geometría de rejilla
import tkinter as tk

ventana = tk.Tk()
ventana.title("Uso de Grid")
ventana.geometry("300x200")

etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
etiqueta1.grid(row=0, column=0)

etiqueta2 = tk.Label(ventana, text="Etiqueta 2")
etiqueta2.grid(row=1, column=0)

cuadro_texto = tk.Entry(ventana)
cuadro_texto.grid(row=0, column=1)

boton = tk.Button(ventana, text="Haz clic")
boton.grid(row=1, column=1)

ventana.mainloop()

# 29.3.2. Uso de geometría de empaquetado (pack)
# Uso de pack para organizar componentes en un contenedor
# Ejemplos de uso de geometría de empaquetado
import tkinter as tk

ventana = tk.Tk()
ventana.title("Uso de Pack")
ventana.geometry("300x200")

etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
etiqueta1.pack()

etiqueta2 = tk.Label(ventana, text="Etiqueta 2")
etiqueta2.pack()

cuadro_texto = tk.Entry(ventana)
cuadro_texto.pack()

boton = tk.Button(ventana, text="Haz clic")
boton.pack()

ventana.mainloop()

# 29.3.3. Uso de geometría de lugar (place)
# Uso de place para organizar componentes en coordenadas específicas
# Ejemplos de uso de geometría de lugar
import tkinter as tk

ventana = tk.Tk()
ventana.title("Uso de Place")
ventana.geometry("300x200")

etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
etiqueta1.place(x=10, y=10)

etiqueta2 = tk.Label(ventana, text="Etiqueta 2")
etiqueta2.place(x=10, y=50)

cuadro_texto = tk.Entry(ventana)
cuadro_texto.place(x=100, y=10)

boton = tk.Button(ventana, text="Haz clic")
boton.place(x=100, y=50)

ventana.mainloop()

# 29.3.4. Uso de marcos (Frame)
# Uso de Frame para organizar componentes en grupos lógicos
# Ejemplos de uso de marcos
import tkinter as tk

ventana = tk.Tk()
ventana.title("Uso de Frame")
ventana.geometry("300x200")

marco1 = tk.Frame(ventana)
marco1.pack()

etiqueta1 = tk.Label(marco1, text="Etiqueta 1")
etiqueta1.pack()

cuadro_texto = tk.Entry(marco1)
cuadro_texto.pack()

marco2 = tk.Frame(ventana)
marco2.pack()

etiqueta2 = tk.Label(marco2, text="Etiqueta 2")
etiqueta2.pack()

boton = tk.Button(marco2, text="Haz clic")
boton.pack()

ventana.mainloop()