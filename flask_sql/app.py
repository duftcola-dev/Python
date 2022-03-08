from api.config.config import myconfig
from api.routes.status.status import appstatus
from api.routes.vehicles.vehicles import vehicles
from flask import Flask
app = Flask(__name__)
app.register_blueprint(appstatus)
app.register_blueprint(vehicles)
app.config.from_object(myconfig)
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)


