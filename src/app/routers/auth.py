from flask import Blueprint, flash, g, redirect, render_template
from flask_babel import _
from flask_login import current_user, login_user, logout_user

from src.app.services.user.forms import LoginForm, RegisterForm
from src.app.services.user.service import user_service

auth_bp = Blueprint("auth", __name__)


@auth_bp.before_request
def before_request():
    g.user = current_user


@auth_bp.route("/", methods=("GET", "POST"))
def index():
    """
    Renders an auth page with two forms: login form and register form
    """

    login_form = LoginForm()
    register_form = RegisterForm()

    if login_form.identifier.data == "LOGIN" and login_form.validate_on_submit():
        user = user_service.get_by_username(username=login_form.login_name.data)
        login_user(user)
        return redirect("/users")

    if register_form.identifier.data == "REGISTER" and register_form.validate_on_submit():
        user_service.create_user(
            email=register_form.email.data,
            username=register_form.register_name.data,
            password=register_form.password.data,
        )
        flash(_("Successful registration"))

    return render_template("login.html", login_form=login_form, register_form=register_form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")
