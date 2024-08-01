from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username',validators=[DataRequired(), Length (1, 64)])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username',validators=[DataRequired(), Length (1, 64)])
    password = PasswordField('Password',validators=[DataRequired()])
    retype_password = PasswordField(' Retype Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('register')