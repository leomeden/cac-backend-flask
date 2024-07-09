from flask import jsonify, request
from app.database import testear_conexion, crear_tabla_tragos
from app.models import Trago

def index():
    return jsonify({"mensaje": "Soy una api nuevita nuevita"}), 200

def test():
    return jsonify({"mensaje": "Esto es un Test"}), 200

def testear_base():
    try:
        testear_conexion()
        hola = "hola"
        return jsonify({"mensaje": "La conexión es un éxito"}), 200
    except BaseException as be:

        return jsonify({f"mensaje": "NO ANDA NADA{be}"}), 500
    


def crear_tabla():
    try:
        crear_tabla_tragos()
        return jsonify({"mensaje": "Ya se creó la tabla"}), 200, {'Access-Control-Allow-Origin':'*'}
    except BaseException as be:
        return jsonify({"mensaje": f"Se rompió todo {be}"}), 500
    
def traer_tragos():
    print(Trago.traerTragos())
    return jsonify(Trago.traerTragos()), 200

def traer_trago_codigo(codigo):
    print(codigo)
    trago = Trago.traerTragoPorCodigo(codigo)
    return jsonify(trago), 200

def agregar_trago():
    data = request.json
    trago = Trago(id=None, codigo=data['codigo'], nombre=data['nombre'], instrucciones=data['instrucciones'], vaso=data['vaso'], imagen=data['imagen'], alcohol=data['alcohol'], categoria=data['categoria'])
    trago.save()
    return jsonify({'message': 'El trago fue exitosamente creado'}), 201

def eliminar_trago_codigo(codigo):
    print(codigo)
    Trago.eliminarTragoPorCodigo(codigo)
    return jsonify({'message': 'El trago fue exitosamente eliminado'}),204
