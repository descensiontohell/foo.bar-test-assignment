from flask import Flask

from src.core.config import setup_config
from src.core.database import setup_db
from src.core.login import setup_login
from src.app.routers.auth import auth_bp
from src.app.routers.feedback import feedback_bp
from src.app.routers.errors import errors_bp, redirect_to_not_found, redirect_to_access_denied


def setup_app():
    app = Flask("foo")
    app.register_blueprint(auth_bp)
    app.register_blueprint(feedback_bp)
    app.register_error_handler(404, redirect_to_not_found)
    app.register_error_handler(403, redirect_to_access_denied)
    app.register_error_handler(401, redirect_to_access_denied)
    setup_config(app)
    setup_db(app)
    setup_login(app)
    return app
