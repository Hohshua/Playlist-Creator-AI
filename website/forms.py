from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo

class InfoForm(FlaskForm):
    artist = StringField('Artist', validators=[DataRequired(), Length(max=50)])
    song = StringField('Song Title', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Submit')