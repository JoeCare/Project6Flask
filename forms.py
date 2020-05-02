from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
        validators=[DataRequired(), Email()])
    password = PasswordField('Password') 
        validators=[DataRequired()]
    confirm_password = PasswordField('Confirm Password',
        validators=[RataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', 
        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')