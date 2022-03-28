from flask import Flask,make_response;

app = Flask(__name__)


@app.route("/hello")
def hello():
    response = make_response({"response":"it works"},200)
    response.headers["Content-type"]="json"
    return response


if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0',port=5000)