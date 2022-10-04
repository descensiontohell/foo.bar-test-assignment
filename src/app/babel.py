from flask import request
from flask_babel import Babel

babel = Babel()


def setup_babel(app):
    babel.init_app(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(["en_US", "ru_RU", "nl_NL"])
