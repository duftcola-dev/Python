from flask import Flask,make_response,request,url_for,redirect




app=Flask(__name__)



@app.route("/")
def index():

    return " IT WORKS"


@app.route("/testing_get",methods=["GET"])
def testing_get():

    respose_struct={
        "type":"get",
        "data":"aknowledge",
        "success":True
    }
    response=make_response(respose_struct,200)
    return response


@app.route("/testing/redirect",methods=["GET"])
def redirect_funct():
    return redirect(url_for("index"))


@app.route("/testing_route_variable/<string:some_variable>/test")
def route_variable(some_variable):
    response_struct = {
        "content":some_variable
    }
    response = make_response(response_struct,200)
    return response


@app.route("/testing_query/",methods=["GET"])
def testing_query():
    
    response_structure={
        "type":"get",
        "data":request.args.get("data"),
        "success":True
    }
    response=make_response(response_structure,200)
    return  response


@app.route("/testing_post/",methods=["POST"])
def testing_post():

    response_structure={
        "user":request.args.get("user"), #query
        "app":request.args.get("app"),
        "content":{
            "id":request.form.get("id"), #body
            "type":request.form.get("type"),
            "data":request.form.get("data")
        }
    }    
    response=make_response(response_structure,200)
    return response


@app.route("/testing_put/",methods=["PUT"])
def testing_put():

    response_structure={
        "user":request.args.get("user"),
        "type":request.args.get("type"),
        "content":{
            "item": request.form.get("item")
        }
    }
    response=make_response(response_structure,200)
    return response


if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0',port=5000)