from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, EqualTo
from ai_api import generatePlaylist

class InputForm(FlaskForm):
    artist = StringField('Artist', validators=[DataRequired(), Length(max=50)])
    song = StringField('Song Title', validators=[DataRequired(), Length(max=50)])
    number_of_songs = IntegerField('Number of Songs', validators=[DataRequired(), NumberRange(max=20)])
    submit = SubmitField('Submit')