from flask import Blueprint, redirect, render_template, flash

errors_bp = Blueprint("errors", __name__)


def redirect_to_not_found(e):
    return redirect("/notfound")


def redirect_to_access_denied(e):
    flash("You should login to access the resource")
    return redirect("/")


@errors_bp.route("/notfound")
def page_not_found():
    return render_template("notfound.html")
