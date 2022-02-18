from crypt import methods
from email.message import Message
from flask import Flask,make_response,request,url_for,redirect
from flask_mail import Mail,Message
from users.routes import users
from config.config import myconfig
# testing blueprints 

app=Flask(__name__)
app.config.from_object(myconfig)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'duftcoladev@gmail.com'
app.config['MAIL_PASSWORD'] = 'pythontestservice'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#configuring mail 

mail = Mail()
mail.init_app(app)


@app.route("/")
def index():

    return " IT WORKS"+str(app.config.get("PORT"))


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

# using blueprint ---> similar to router in nodejs
app.register_blueprint(users) # registering the users blueprint
#now the routes created in the blueprint users can be used


#using flask mailing service
@app.route("/mail/<string:message>",methods=["GET"])
def send_main(message):
    print(message)
    msg = Message("From flask :"+message,sender= "testingFlask@app.com",recipients = ["robinviera@hotmail.com"])
    msg.body="testing"
    msg.html="<p>some html</p>"
    mail.send(msg)
    return "mail sent "


if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0',port=5000)