from sqlalchemy import desc

from src.core.feedback.models import FeedbackMessage
from src.app.database import db


class FeedbackService:
    def create_message(self, creator: str, content: str) -> None:
        """Creates a message with given creator and content"""

        new_message = FeedbackMessage(creator=creator, content=content)
        db.session.add(new_message)
        db.session.commit()

    def get_all(self) -> list[FeedbackMessage]:
        """Returns all messages from the database"""

        messages = (
            db.session.execute(db.select(FeedbackMessage).order_by(desc(FeedbackMessage.created_at))).scalars().all()
        )
        return messages


feedback_service = FeedbackService()
