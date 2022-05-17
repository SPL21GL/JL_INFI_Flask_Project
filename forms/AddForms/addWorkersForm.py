from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField
from wtforms import validators


class addWorkersForm(FlaskForm):
    Voname = StringField("Firstname", validators=[validators.Length(
        3, 100), validators.input_required()])
    Nachname = StringField("Lastname", validators=[validators.Length(
        3, 100), validators.input_required()])
    Lohn = DecimalField("Salary", validators=[validators.input_required()])
    Adresse = StringField("Address", validators=[validators.Length(
        10, 100), validators.input_required()])
    Beschäftigung = StringField("Employment", validators=[validators.Length(
        5, 30), validators.input_required()])
    Geburtsdatum = DateField("Birthday", [validators.input_required()])
