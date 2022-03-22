from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField, HiddenField,DecimalField

class EditWorkersForm(FlaskForm):
    MitarbeiterId = HiddenField("itemId")
    Voname = StringField("Firstname")
    Nachname = TextAreaField("Lastname")
    Lohn = DecimalField("Salary")
    Adresse = StringField("Address")
    Beschäftigung = StringField("Employment")
    Geburtsdatum = DateField("Birthday")