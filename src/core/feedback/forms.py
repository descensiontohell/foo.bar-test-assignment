from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    creator = StringField(_l("Name"), validators=[DataRequired()])
    content = StringField(_l("Message"), validators=[DataRequired()])
    recaptcha = RecaptchaField(_l("Captcha"))
    submit = SubmitField(_l("Submit"))
