from sqlalchemy import desc

from src.app.services.feedback.models import FeedbackMessage
from src.core.database import db


class FeedbackService:
    def create_message(self, creator: str, content: str):
        new_message = FeedbackMessage(creator=creator, content=content)
        db.session.add(new_message)
        db.session.commit()

    def get_all(self) -> list[FeedbackMessage]:
        messages = (
            db.session.execute(db.select(FeedbackMessage).order_by(desc(FeedbackMessage.created_at))).scalars().all()
        )
        return messages


feedback_service = FeedbackService()
