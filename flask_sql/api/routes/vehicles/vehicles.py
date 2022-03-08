from crypt import methods
from unittest import result
from flask import Blueprint,make_response,request
from api.mysql_driver import mysql_driver
from api.mysql_driver import queries
from api.schemes import schemes_factory

vehicles = Blueprint("vehicles",__name__)

@vehicles.route("/update_vehicles_state",methods=["GET"])
def update_vehicles():
    db = mysql_driver.get_cursor()
    vehicle_scheme = schemes_factory.create_vehicle_scheme()
    cursor = db.cursor()
    cursor.execute(queries.get("select_by_speed"))
    result = cursor.fetchall()
    sql = queries.get("update_state_to_1")
    for item in result:
        val = (1,item[0])
        cursor.execute(sql,val)
    db.commit()
    cursor.execute(queries.get("select_all_vehicles"))
    result = cursor.fetchall()
    data = {
        "data":vehicle_scheme.get_collection(result)
    }
    cursor.close()
    response = make_response(data,200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response


@vehicles.route("/get_vehicles",methods=["GET"])
def get_vehicles():
    db = mysql_driver.get_cursor()
    vehicle_scheme = schemes_factory.create_vehicle_scheme()
    cursor = db.cursor()
    cursor.execute(queries.get("select_all_vehicles"))
    result = cursor.fetchall()
    cursor.close()
    data = {
        "data":vehicle_scheme.get_collection(result)
    }
    response = make_response(data,200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

@vehicles.route("/get_vehicle",methods=["GET"])
def get_vehicle():
    id = request.args.get("matricula")
    db = mysql_driver.get_cursor()
    vehicle_scheme = schemes_factory.create_vehicle_scheme()
    cursor = db.cursor()
    querie = queries.get("select_by_matricula").format(id)
    cursor.execute(querie)
    result = cursor.fetchall()
    response = make_response(vehicle_scheme.get_item(result),200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

@vehicles.route("/get_positions",methods=["GET"])
def get_positions():
    db = mysql_driver.get_cursor()
    position_scheme = schemes_factory.create_position_scheme()
    cursor = db.cursor()
    querie = queries.get("select_posiciones")
    cursor.execute(querie)
    result = cursor.fetchall()
    response = make_response({"data":position_scheme.get_collection(result)},200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response