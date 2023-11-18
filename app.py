import os
import logging
from dotenv import load_dotenv

from flask import Flask, jsonify
from flask_cors import CORS
from controllers.UserController import user_blueprint
from controllers.PostController import post_blueprint
from controllers.RecipeController import recipe_blueprint
from controllers.GroupController import group_blueprint
from controllers.ErrorController import error_blueprint


app = Flask(__name__)
# allow cors on all endpoints for all domains
CORS(app, supports_credentials=True)
app.logger.setLevel(logging.INFO)

if load_dotenv(os.getenv("ENV_PATH")):
    app.logger.info(f"Loaded env from path: {os.getenv('ENV_PATH')}")
else:
    app.logger.warning(f"Unable to load env from path: {os.getenv('ENV_PATH')}")


loglevel = logging.INFO
if os.getenv("LOG_LEVEL"):
    match os.getenv("LOG_LEVEL").lower():
        case "debug":
            loglevel = logging.DEBUG
        case "info":
            loglevel = logging.INFO
        case "warn":
            loglevel = logging.WARN
        case "error":
            loglevel = logging.ERROR
        case "critical":
            loglevel = logging.CRITICAL
        case _:
            loglevel = logging.INFO

    app.logger.setLevel(loglevel)
    del loglevel


# Register the blueprints (controllers)
app.register_blueprint(user_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(recipe_blueprint)
app.register_blueprint(group_blueprint)
app.register_blueprint(error_blueprint)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": 200}), 200


if __name__ == '__main__':
    app.run()
