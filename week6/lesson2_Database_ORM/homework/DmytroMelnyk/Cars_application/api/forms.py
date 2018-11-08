from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AddCarForm(FlaskForm):
    model = StringField('Model', validators=[DataRequired()])
    mark = StringField('Mark', validators=[DataRequired()])
    horsepower = StringField('Horsepower', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    origin = StringField('Origin', validators=[DataRequired()])

