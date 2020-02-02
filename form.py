from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class SendForm(FlaskForm):
    username = StringField('Короткое название магазина', validators=[DataRequired()])
    company = StringField('Полное наименование компании', validators=[DataRequired()])
    url = StringField('Url')
    upload = FileField(validators=[FileRequired(), FileAllowed(['xls', 'xlsx'], 'Excel only!'),])
    submit = SubmitField('Send')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')

class UploadForm(FlaskForm):
    upload = FileField(validators=[FileRequired(), FileAllowed(['xls', 'xlsx'], 'Excel only!'),])
    submit = SubmitField('Send')
