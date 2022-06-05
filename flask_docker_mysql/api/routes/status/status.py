from crypt import methods
from flask import Blueprint,make_response
from api.mysql_driver import mysql_driver
appstatus = Blueprint("status",__name__)

@appstatus.route("/status")
def get_status():
    database = "Not_OK"
    if mysql_driver.ping()==True:
        database = "OK"
    data = {
        "server":"OK",
        "database":database
    }
    response = make_response(data,200)
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response