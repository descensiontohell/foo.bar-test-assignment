from flask import Blueprint, render_template

from src.core.feedback.forms import FeedbackForm
from src.core.feedback.service import feedback_service

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.route("/feedback", methods=("GET", "POST"))
def feedback():
    """
    Renders a page with a feedback form. Displays a message when user submits the form
    """

    feedback_form = FeedbackForm()
    is_submitted = False

    if feedback_form.validate_on_submit():
        feedback_service.create_message(creator=feedback_form.creator.data, content=feedback_form.content.data)
        is_submitted = True

    return render_template("feedback.html", feedback_form=feedback_form, is_submitted=is_submitted)
