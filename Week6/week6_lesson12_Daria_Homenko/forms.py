from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, Length
from db.db_model import User


class LoginForms(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=35)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')

    def validate_username(self, username):
        user = User.query.filter_by(name=username.data).first()

        if not user:
            raise ValidationError('That username is not used. Please enter correct user name or SIGN IN')


class Sign_inForm(FlaskForm):
    s_username = StringField('Username', validators=[DataRequired(), Length(min=5, max=35)])
    s_age = StringField('Age', validators=[DataRequired()])
    s_email = StringField('Email', validators=[DataRequired(), Email()])
    s_password = PasswordField('Password', validators=[DataRequired()])
    s_submit = SubmitField('Sign in')

    def validate_s_email(self, s_email):
        user_email = User.query.filter_by(email=s_email.data).first()

        if user_email:
            raise ValidationError('That email is used. Please choose a different one')

    def validate_s_username(self, s_username):
        user = User.query.filter_by(name=s_username.data).first()

        if user:
            raise ValidationError('That username is taken. Please choose a different one')
