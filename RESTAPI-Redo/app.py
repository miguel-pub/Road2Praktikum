import uuid
import os
from flask import Flask, request
from flask_smorest import Api
from db import db
import models


from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTION"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    api = Api(app)

    with app.app_context():
        db.create_all()
    #  docker run -p 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api:latest    
    # runs container and syncs with updated files

    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(ItemBlueprint)
    return app