from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

from src.app.services.user.service import user_service


class RegisterForm(FlaskForm):
    register_name = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=16)])
    email = EmailField("Email: ")
    submit = SubmitField("Register")
    identifier = StringField()

    def validate(self):
        validation = super().validate()
        if not validation:
            return False
        if user_service.get_by_username(self.register_name.data):
            self.register_name.errors.append("Name already registered")
            return False
        if user_service.get_by_email(self.email.data):
            self.email.errors.append("Email already registered")
            return False

        return True


class LoginForm(FlaskForm):
    login_name = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=16)])
    submit = SubmitField("Login")
    identifier = StringField()

    def validate(self):
        validation = super().validate()
        if not validation:
            return False
        user = user_service.get_by_username(self.login_name.data)
        if not user:
            self.login_name.errors.append("No user with such name")
            return False
        elif not user.verify_password(self.password.data):
            self.password.errors.append("Invalid password")
            return False

        return True
