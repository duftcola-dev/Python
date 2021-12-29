from flask import Flask


app=Flask(__name__)



@app.route("/")
def index():

    return " IT WORKS"


@app.route("/testing_get",methods=["GET"])
def testing_get():

    pass

@app.route("/testing_query/{data}",methods=["GET"])
def testing_query(data):

    pass


@app.route("/testing_post",methods=["POST"])
def testing_post():

    pass

if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0',port=5000)