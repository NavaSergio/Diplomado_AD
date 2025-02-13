# 27.2.1. Definición de rutas
# Uso de @app.route para definir rutas en Flask
# Ejemplos de definición de rutas
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Página de inicio"

@app.route('/acerca')
def acerca():
    return "Acerca de nosotros"

# 27.2.2. Manejo de métodos HTTP
# Uso de methods para manejar métodos HTTP (GET, POST, PUT, DELETE)
# Ejemplos de manejo de métodos HTTP
from flask import request

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        return "Formulario enviado"
    else:
        return "Página de contacto"

# 27.2.3. Parámetros de ruta
# Uso de parámetros de ruta en Flask
# Ejemplos de uso de parámetros de ruta
@app.route('/usuario/<int:id>')
def usuario(id):
    return f"Detalles del usuario {id}"

# 27.2.4. Redirecciones y errores
# Uso de redirect() y abort() para manejar redirecciones y errores
# Ejemplos de redirecciones y errores
from flask import redirect, url_for, abort

@app.route('/redirigir')
def redirigir():
    return redirect(url_for('home'))

@app.route('/error')
def error():
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)