from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import path
import config


def create_app():
    thisApp = Flask(__name__)
    # thisApp.config["SECRET_KEY"] = "build test" #encrypt or secure the cookies
    thisApp.config["SECRET_KEY"] = config.DevelopmentConfig.OPENAI_KEY

    #import the modules
    from .routes import app

    thisApp.register_blueprint(app, url_prefix = "/")

    return thisApp