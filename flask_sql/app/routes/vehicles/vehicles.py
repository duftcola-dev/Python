from crypt import methods
from flask import Blueprint

vehicles = Blueprint("users",__name__)

@vehicles.route("/update_vehicles",methods=["GET"])
def update_vehicles():
    print("Update vehicles states")


@vehicles.route("/get_vehicles",methods=["GET"])
def get_vehicles():
    print("get all vehicles")

@vehicles.route("/vehicle/<string:id>",methods=["GET"])
def vehicles(id:str):
    print("get vehicle by id")