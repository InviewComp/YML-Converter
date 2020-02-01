from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SendForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    url = StringField('Url')
    platform = StringField('Platform')
    version = StringField('Version')
    agency = StringField('Agency')
    email = StringField('Email')
    submit = SubmitField('Send')
