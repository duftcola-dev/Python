from crypt import methods
from flask import Blueprint

users = Blueprint("users",__name__)

@users.route("/register",methods=["GET","POST"])
def resgister_user():

    return "<p> users - route --> register</p>"

@users.route("/delete",methods=["GET","POST"])
def delete_user():

    return "<p> users - route --> delete</p>"

@users.route("/add",methods=["GET","POST"])
def add_user():

    return "<p> users - route --> add</p>"