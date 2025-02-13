# 28.2.1. Introducción a SQLite
# Definición y características de SQLite: Es una base de datos liviana y embebida.
# Ventajas de usar SQLite para desarrollo local: Fácil de usar y no requiere un servidor.

# 28.2.2. Instalación y configuración de SQLite
# Instalación de SQLite en diferentes sistemas operativos: SQLite viene preinstalado en Python.
# Configuración del entorno de desarrollo

# 28.2.3. Conexión a una base de datos SQLite
# Uso de sqlite3 para conectar a una base de datos SQLite
# Ejemplos de conexión a una base de datos SQLite
import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conn.cursor()

# Ejecutar consultas SQL
cursor.execute('SELECT * FROM usuarios')
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

# Cerrar la conexión
conn.close()