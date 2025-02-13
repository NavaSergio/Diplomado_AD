# 28.1.1. Introducción a las bases de datos
# Definición y características de las bases de datos: Son sistemas que almacenan y organizan datos de manera estructurada.
# Tipos de bases de datos: relacionales, NoSQL, etc.

# 28.1.2. Modelo relacional
# Concepto de modelo relacional: Los datos se organizan en tablas con filas y columnas.
# Componentes del modelo relacional: tablas, filas, columnas, claves primarias y foráneas

# 28.1.3. Lenguaje SQL
# Introducción a SQL (Structured Query Language): Es un lenguaje para gestionar y manipular bases de datos relacionales.
# Ejemplos básicos de consultas SQL
import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
''')

# Insertar datos en la tabla
cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Juan', 30))
cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Ana', 25))

# Guardar los cambios
conn.commit()

# Consultar datos
cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

# Cerrar la conexión
conn.close()