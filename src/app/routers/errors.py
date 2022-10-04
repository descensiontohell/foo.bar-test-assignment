from flask import Blueprint, redirect, render_template


errors_bp = Blueprint("errors", __name__)


def redirect_to_not_found(e):
    return redirect("/notfound")


def redirect_to_access_denied(e):
    return redirect("/denied")


@errors_bp.route("/notfound")
def page_not_found():
    return render_template("notfound.html")


@errors_bp.route("/denied")
def access_denied():
    return render_template("denied.html")
