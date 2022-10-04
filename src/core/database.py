from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app: Flask):
    from src.app.services.feedback.models import FeedbackMessage
    from src.app.services.user.models import User

    db.init_app(app)
    with app.app_context():
        db.create_all()
