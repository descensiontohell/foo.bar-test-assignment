from flask import Flask

from src.app.routers.auth import auth_bp
from src.app.routers.errors import errors_bp, redirect_to_access_denied, redirect_to_not_found
from src.app.routers.feedback import feedback_bp
from src.app.routers.users import users_bp
from src.core.database import setup_db
from src.core.login import setup_login
from src.core.babel import setup_babel


def setup_routes(app: Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(feedback_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(errors_bp)
    app.register_error_handler(404, redirect_to_not_found)
    app.register_error_handler(403, redirect_to_access_denied)
    app.register_error_handler(401, redirect_to_access_denied)


def create_app():
    app = Flask("foo", instance_relative_config=True, template_folder="src/templates/")
    app.config.from_object("src.core.config.Config")
    setup_routes(app)
    setup_babel(app)
    setup_db(app)
    setup_login(app)
    return app
