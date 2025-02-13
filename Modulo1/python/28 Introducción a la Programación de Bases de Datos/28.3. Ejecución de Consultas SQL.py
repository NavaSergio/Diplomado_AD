# 28.3.1. Creación de tablas
# Uso de CREATE TABLE para crear tablas en SQLite
# Ejemplos de creación de tablas
import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conn.cursor()

# Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

# 28.3.2. Inserción de datos
# Uso de INSERT INTO para insertar datos en tablas
# Ejemplos de inserción de datos
import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conn.cursor()

# Insertar datos en la tabla
cursor.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', ('Producto 1', 10.99))
cursor.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', ('Producto 2', 15.99))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

# 28.3.3. Consulta de datos
# Uso de SELECT para consultar datos de tablas
# Ejemplos de consultas de datos
import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conn.cursor()

# Consultar datos
cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall()
for producto in productos:
    print(producto)

# Cerrar la conexión
conn.close()

# 28.3.4. Actualización y eliminación de datos
# Uso de UPDATE y DELETE para actualizar y eliminar datos
# Ejemplos de actualización y eliminación de datos
import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conn.cursor()

# Actualizar datos
cursor.execute('UPDATE productos SET precio = ? WHERE id = ?', (12.99, 1))

# Eliminar datos
cursor.execute('DELETE FROM productos WHERE id = ?', (2,))

# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()