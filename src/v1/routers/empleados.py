from flask import Blueprint, jsonify, request
import uuid
from src.v1.db.conexion import get_connection


empleados=Blueprint('empleados_blueprint',__name__)

@empleados.route('/')
def home():
    try:
        resultado=[]
        connection = get_connection()
        con=connection.cursor()
        con.execute("select 'we are ready'")
        for row in con:
            resultado.append(row)
        connection.close()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500
