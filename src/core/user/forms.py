from flask_wtf import FlaskForm
from flask_babel import _, lazy_gettext as _l
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

from src.core.user.service import user_service


class RegisterForm(FlaskForm):
    register_name = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired(), Length(min=4, max=16)])
    email = EmailField(_l("Email"), validators=[DataRequired()])
    submit = SubmitField(_l("Register"))
    identifier = StringField()

    def validate(self) -> bool:
        """
        Makes sure that username and email are not taken
        """

        validation = super().validate()
        if not validation:
            return False
        if user_service.get_by_username(self.register_name.data):
            self.register_name.errors.append(_("Name already registered"))
            return False
        if user_service.get_by_email(self.email.data):
            self.email.errors.append(_("Email already registered"))
            return False

        return True


class LoginForm(FlaskForm):
    login_name = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired(), Length(min=4, max=16)])
    submit = SubmitField(_l("Login"))
    identifier = StringField()

    def validate(self) -> bool:
        """
        Makes sure that user exists and the password is correct
        """

        validation = super().validate()
        if not validation:
            return False
        user = user_service.get_by_username(self.login_name.data)
        if not user:
            self.login_name.errors.append(_("No user with such name"))
            return False
        elif not user.verify_password(self.password.data):
            self.password.errors.append(_("Invalid password"))
            return False

        return True
