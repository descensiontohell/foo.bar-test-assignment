from typing import Optional

from src.core.user.models import User
from src.app.database import db


class UserService:
    def get_by_username(self, username: str) -> Optional[User]:
        """
        Returns a user with given username
        """

        user = User.query.filter_by(username=username).first()
        return user

    def get_by_email(self, email: str) -> Optional[User]:
        """
        Returns a user with given email
        """

        user = User.query.filter_by(email=email).first()
        return user

    def create_user(self, email: str, username: str, password: str) -> None:
        """
        Creates user with given email, username and password
        """

        new_user = User(email=email, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

    def get_all(self) -> list[User]:
        """
        Returns all users
        """

        users = User.query.all()
        return users

    def delete_by_id(self, user_id: int) -> None:
        """
        Deletes the user by id
        """

        User.query.filter_by(id=user_id).delete()
        db.session.commit()


user_service = UserService()
