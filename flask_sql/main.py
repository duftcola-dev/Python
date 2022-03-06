from app.config.config import myconfig
from app.routes.status.status import status
from app.routes.vehicles.vehicles import vehicles
from flask import Flask
app = Flask(__name__)



if __name__ == "__main__":
    app.config.from_object(myconfig)
    app.register_blueprint(status)
    app.register_blueprint(vehicles)
    app.run(
        debug=app.config.get("DEBUG"),
        hots=app.config.get("HOST"),
        port=app.config.get("PORT"))


