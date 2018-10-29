from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    userage = StringField('UserAge', validators=[DataRequired(), Length(min=1, max=2)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    Model = StringField('Model', validators=[DataRequired()])
    Mark = StringField('Mark', validators=[DataRequired()])
    Horsepower = StringField('Horsepower', validators=[DataRequired()])
    Year = StringField('Year', validators=[DataRequired()])
    Origin = StringField('Origin', validators=[DataRequired()])
