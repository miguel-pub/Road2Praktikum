import uuid
from flask import Flask, request
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
app = Flask(__name__)

app.config["PROPAGATE_EXCEPTION"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
#  docker run -p 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api:latest    
# runs container and syncs with updated files

api.register_blueprint(StoreBlueprint)
api.register_blueprint(ItemBlueprint)