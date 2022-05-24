from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class EditCompartmentsForm(FlaskForm):
    '# Defines the fields for edit compartments form.'
    AbteilungsId = HiddenField("CompartmentId")
    Name = StringField("Name")
    Gebäude = DecimalField("Building")
