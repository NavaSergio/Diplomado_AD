# 27.3.1. Uso de plantillas con Jinja2
# Introducción a Jinja2 y su uso en Flask
# Ejemplos de uso de plantillas Jinja2
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# 27.3.2. Variables y bucles en plantillas
# Uso de variables y bucles en plantillas Jinja2
# Ejemplos de variables y bucles en plantillas
@app.route('/usuarios')
def usuarios():
    usuarios = ['Juan', 'Ana', 'Pedro']
    return render_template('usuarios.html', usuarios=usuarios)

# 27.3.3. Herencia de plantillas
# Uso de herencia de plantillas en Jinja2
# Ejemplos de herencia de plantillas
@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

# 27.3.4. Formateo de fechas y horas en plantillas
# Uso de filtros para formatear fechas y horas en plantillas Jinja2
# Ejemplos de formateo de fechas y horas en plantillas
from datetime import datetime

@app.route('/fecha')
def fecha():
    fecha_actual = datetime.now()
    return render_template('fecha.html', fecha_actual=fecha_actual)

if __name__ == '__main__':
    app.run(debug=True)