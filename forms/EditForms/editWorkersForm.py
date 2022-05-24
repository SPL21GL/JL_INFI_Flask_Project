from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class EditWorkersForm(FlaskForm):
    '# Defines the fields for edit workers form.'
    MitarbeiterId = HiddenField("WorkerId")
    Voname = StringField("Firstname")
    Nachname = StringField("Lastname")
    Lohn = DecimalField("Salary")
    Adresse = StringField("Address")
    Beschäftigung = StringField("Employment")
    Geburtsdatum = DateField("Birthday")
