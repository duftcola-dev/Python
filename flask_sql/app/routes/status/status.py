from flask import Blueprint

status = Blueprint("status",__name__)

status.route("/status")
def status():
    print("app status")