from flask import Blueprint, redirect, render_template
from flask_login import current_user, login_required

from src.app.services.user.service import user_service
from src.app.services.feedback.service import feedback_service


users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
@login_required
def get_users():
    users = user_service.get_all()
    messages = feedback_service.get_all()
    return render_template("users.html", users=users, feedback_messages=messages)


@users_bp.route("/users/delete/<int:user_id>", methods=["GET", "POST"])
@login_required
def delete_user(user_id):
    if current_user.id != user_id:
        user_service.delete_by_id(user_id)
    return redirect("/users")
