from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    creator = StringField("Name", validators=[DataRequired()])
    content = StringField("Message", validators=[DataRequired()])
    recaptcha = RecaptchaField("Captcha")
    submit = SubmitField("Submit")
