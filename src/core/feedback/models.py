from sqlalchemy.sql import func

from src.app.database import db


class FeedbackMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.String)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=func.now())
