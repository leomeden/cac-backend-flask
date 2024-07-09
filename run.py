from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import index, test, testear_base, agregar_trago, crear_tabla, traer_tragos, traer_trago_codigo, eliminar_trago_codigo

app = Flask(__name__)

# Configurar la aplicación Flask
# app.config.from_pyfile('config/development.py')

# Inicializar la base de datos con la aplicación Flask
init_app(app)
#permitir solicitudes desde cualquier origen
CORS(app)
#permitir solicitudes desde un origen específico
#CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

app.route('/', methods = ['GET'])(index)
app.route('/test', methods = ['GET'])(test)
app.route('/probar_base', methods = ['POST'])(testear_base)
app.route('/tabla/crear', methods = ['POST'])(crear_tabla)
app.route('/api/drinks/', methods = ['POST'])(agregar_trago)
app.route('/api/drinks/', methods = ['GET'])(traer_tragos)
app.route('/api/drinks/<codigo>', methods = ['GET'])(traer_trago_codigo)
app.route('/api/drinks/<codigo>', methods = ['DELETE'])(eliminar_trago_codigo)


if __name__ == '__main__':
    app.run(debug=True)