from flask import Blueprint, redirect, render_template, flash
from flask_babel import _

errors_bp = Blueprint("errors", __name__)


def redirect_to_not_found(e):
    """
    Redirects to /notfound on error 404
    """

    return redirect("/notfound")


def redirect_to_access_denied(e):
    """
    Redirects to login page on error 403
    """

    flash(_("You should login to access the resource"))
    return redirect("/")


@errors_bp.route("/notfound")
def page_not_found():
    return render_template("notfound.html")
