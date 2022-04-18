from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField

class EditWorkersForm(FlaskForm):
    MitarbeiterId = HiddenField("WorkerId")
    Voname = StringField("Firstname")
    Nachname = StringField("Lastname")
    Lohn = DecimalField("Salary")
    Adresse = StringField("Address")
    Beschäftigung = StringField("Employment")
    Geburtsdatum = DateField("Birthday")