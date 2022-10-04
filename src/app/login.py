from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = "strong"


def setup_login(app) -> None:
    login_manager.init_app(app)
