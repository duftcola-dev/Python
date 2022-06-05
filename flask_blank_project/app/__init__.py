import os
from flask import Flask
from .config.config import ProductionConfig,DevelopmentConfig,TestConfig
from .db import db
from .routes import auth
from .cli import manage_db

def set_configuration(app:Flask)->Flask: # load configuration
    """Set app configuration.
    A different configuration is loaded deppending on the
    ENV variable

    Args:
        app (Flask): Flask class

    Returns:
        Flask: Flask class
    """
    if app.config["ENV"] == "production":
        app.config.from_object(ProductionConfig())
    if app.config["ENV"] == "development":
        app.config.from_object(DevelopmentConfig())
    if app.config["ENV"] == "testing":
        app.config.from_object(TestConfig())
    return app
    

def create_app()->Flask:
    """Creates the main instance of the Flask class

    Returns:
        Flask: instance of flask class
    """
    app = Flask(__name__) # build app
    app = set_configuration(app) # set configuration
    app.register_blueprint(auth.bp) # registter blueprint
    app = manage_db.init_app(app) # register cli commands
    db.init__app(app) # intialize database instance

     # a simple page that says hello
    @app.route('/status')
    def status():
        return 'IT WORKS!'
    return app


