from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField, SelectField
from wtforms import validators

choices = [("Website", "Website"), ("Product", "Product"), ("App Devolopment", "App Development")]


class addWorkersForm(FlaskForm):
    '# Defines the fields for add workers form.'
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
    Arbeitergruppe = SelectField("status", choices=choices)
