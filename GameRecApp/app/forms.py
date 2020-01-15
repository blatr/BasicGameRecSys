from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    steamid = StringField('SteamID', validators=[DataRequired()])
    submit = SubmitField('Next best game for me')