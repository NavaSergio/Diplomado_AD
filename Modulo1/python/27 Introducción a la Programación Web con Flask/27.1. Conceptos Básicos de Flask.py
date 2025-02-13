# 27.1.1. Introducción a Flask
# Definición y características de Flask: Es un framework web ligero y flexible para Python.
# Ventajas de usar Flask para desarrollo web: Facilita la creación de aplicaciones web con Python.

# 27.1.2. Instalación de Flask
# Instalación de Flask usando pip
# Configuración del entorno de desarrollo
from flask import Flask

app = Flask(__name__)

# 27.1.3. Estructura básica de una aplicación Flask
# Estructura de un proyecto Flask
# Ejemplo de una aplicación Flask básica
@app.route('/')
def home():
    return "¡Hola, mundo!"

if __name__ == '__main__':
    app.run(debug=True)