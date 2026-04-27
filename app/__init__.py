from flask import Flask
from flasgger import Swagger
from app.routes.package_routes import bp as package_bp
import logging

logging.basicConfig(level=logging.INFO)

def create_app():
    app = Flask(__name__)

    Swagger(app)

    app.register_blueprint(package_bp)

    return app