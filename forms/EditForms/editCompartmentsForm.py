from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, TextAreaField, HiddenField,DecimalField

class EditCompartmentsForm(FlaskForm):
    AbteilungsId = HiddenField("CompartmentId")
    Name = StringField("Name")
    Gebäude = DecimalField("Building")