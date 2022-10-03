from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth_bp.login"


def setup_login(app):
    login_manager.init_app(app)
