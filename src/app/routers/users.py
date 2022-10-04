from flask import Blueprint, redirect, render_template
from flask_babel import format_datetime
from flask_login import current_user, login_required

from src.app.services.feedback.service import feedback_service
from src.app.services.user.service import user_service

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
@login_required
def get_users():
    """
    Renders all users and feedback messages
    """

    users = user_service.get_all()
    messages = feedback_service.get_all()
    for m in messages:
        m.created_at = format_datetime(m.created_at)
    return render_template("users.html", users=users, feedback_messages=messages)


@users_bp.route("/users/delete/<int:user_id>", methods=["GET", "POST"])
@login_required
def delete_user(user_id):
    """
    Deletes the user. Does nothing on attempt to delete self. Requires login
    """

    if current_user.id != user_id:
        user_service.delete_by_id(user_id)
    return redirect("/users")
