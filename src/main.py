from flask import Flask

from src.core.config import setup_config
from src.core.database import setup_db
from src.core.login import setup_login
from src.app.routers.auth import auth_bp


def setup_app():
    app = Flask("foo")
    app.register_blueprint(auth_bp)
    setup_config(app)
    setup_db(app)
    setup_login(app)
    return app
