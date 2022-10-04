from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app: Flask):
    # imports are required for proper migration
    from src.core.feedback.models import FeedbackMessage
    from src.core.user.models import User

    db.init_app(app)
    with app.app_context():
        db.create_all()
